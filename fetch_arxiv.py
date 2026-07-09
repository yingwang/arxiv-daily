#!/usr/bin/env python3
"""每日 arXiv 摘要。

抓取若干指定方向在最近一两天提交的新论文，生成一份 markdown 摘要，
写入 docs/digests/YYYY-MM-DD.md，并同步刷新 docs/index.md（最新一期）与
docs/archive.md（历史索引）。

设计要点：
- 纯 Python 标准库实现，无第三方依赖，运行不需要任何 API key。
- 无论抓取成功与否，每次运行都会写出一个按日期命名的新文件，
  以保证每天都产生一次提交（GitHub 贡献绿格靠的是提交，不挑内容）。
- 想加减关注方向，改下面的 TOPICS 即可。
"""

import datetime
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

# 关注方向：(显示名, arXiv search_query)。想加减方向就改这里。
TOPICS = [
    (
        "图像复原 / 低层视觉",
        '(cat:eess.IV OR cat:cs.CV) AND (abs:"super-resolution" OR abs:"super resolution" '
        'OR abs:"image restoration" OR abs:"image denoising" OR abs:"deblurring" '
        'OR abs:"deraining" OR abs:"dehazing" OR abs:"low-light image" '
        'OR abs:"image enhancement" OR abs:"compression artifact")',
    ),
    (
        "扩散模型",
        '(cat:cs.CV OR cat:cs.LG) AND (abs:"diffusion model" OR abs:"flow matching" '
        'OR abs:"rectified flow")',
    ),
    (
        "具身智能",
        '(cat:cs.RO OR cat:cs.AI OR cat:cs.LG) AND (abs:"embodied" '
        'OR abs:"vision-language-action" OR abs:"manipulation policy")',
    ),
]

MAX_PER_TOPIC = 12        # 每个方向最多收录几篇
LOOKBACK_DAYS = 2         # 只收录最近几天提交的论文
FETCH_PER_QUERY = 50      # 每次向 arXiv 拉多少条再按时间过滤
ARXIV_API = "http://export.arxiv.org/api/query"
ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV_NS = "{http://arxiv.org/schemas/atom}"

ROOT = Path(__file__).resolve().parent
DIGEST_DIR = ROOT / "docs" / "digests"


def fetch(query: str) -> bytes:
    params = urllib.parse.urlencode(
        {
            "search_query": query,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
            "max_results": str(FETCH_PER_QUERY),
        }
    )
    url = f"{ARXIV_API}?{params}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "arxiv-daily/1.0 (+https://github.com/yingwang/arxiv-daily)"},
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def parse(xml_bytes: bytes) -> list:
    root = ET.fromstring(xml_bytes)
    entries = []
    for e in root.findall(f"{ATOM}entry"):
        abs_url = e.find(f"{ATOM}id").text.strip()
        arxiv_id = abs_url.rsplit("/", 1)[-1]
        title = " ".join(e.find(f"{ATOM}title").text.split())
        summary = " ".join(e.find(f"{ATOM}summary").text.split())
        published = e.find(f"{ATOM}published").text.strip()
        authors = [a.find(f"{ATOM}name").text for a in e.findall(f"{ATOM}author")]
        primary = e.find(f"{ARXIV_NS}primary_category")
        category = primary.get("term") if primary is not None else ""
        entries.append(
            {
                "id": arxiv_id,
                "abs_url": abs_url,
                "title": title,
                "summary": summary,
                "published": published,
                "authors": authors,
                "category": category,
            }
        )
    return entries


def snippet(text: str, limit: int = 320) -> str:
    if len(text) <= limit:
        return text
    cut = text[:limit]
    dot = cut.rfind(". ")
    if dot > limit * 0.5:
        return cut[: dot + 1]
    return cut.rstrip() + "…"


def format_authors(authors: list) -> str:
    if not authors:
        return "（作者信息缺失）"
    if len(authors) <= 5:
        return ", ".join(authors)
    return ", ".join(authors[:5]) + f" 等 {len(authors)} 人"


def build_digest(date_str: str) -> str:
    cutoff = datetime.date.fromisoformat(date_str) - datetime.timedelta(days=LOOKBACK_DAYS)
    lines = [
        f"# arXiv 每日摘要 · {date_str}",
        "",
        "> 自动抓取，方向：图像复原 / 低层视觉、扩散模型、具身智能。"
        "数据来自 arXiv API，仅收录最近两天提交的论文，标题与摘要保留英文原文。",
        "",
    ]
    seen = set()
    total = 0
    for name, query in TOPICS:
        lines.append(f"## {name}")
        lines.append("")
        try:
            entries = parse(fetch(query))
        except Exception as exc:  # 单个方向失败不影响整份摘要
            lines.append(f"（该方向抓取失败：{exc}）")
            lines.append("")
            continue

        picked = []
        for item in entries:
            if item["id"] in seen:
                continue
            try:
                pub_date = datetime.date.fromisoformat(item["published"][:10])
            except ValueError:
                continue
            if pub_date < cutoff:
                continue
            seen.add(item["id"])
            picked.append(item)
            if len(picked) >= MAX_PER_TOPIC:
                break

        if not picked:
            lines.append("（最近两天该方向无新提交，或未匹配到关键词。）")
            lines.append("")
            continue

        for item in picked:
            total += 1
            lines.append(f"### [{item['title']}]({item['abs_url']})")
            lines.append("")
            lines.append(f"- 作者：{format_authors(item['authors'])}")
            lines.append(f"- 提交：{item['published'][:10]} · 分类 {item['category']} · arXiv:{item['id']}")
            lines.append("")
            lines.append(snippet(item["summary"]))
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"本期共收录 {total} 篇。")
    lines.append("")
    return "\n".join(lines)


def refresh_index_and_archive(date_str: str, digest_md: str) -> None:
    docs = ROOT / "docs"
    (docs / "index.md").write_text(digest_md, encoding="utf-8")

    files = sorted(
        (p for p in DIGEST_DIR.glob("20*.md")),
        key=lambda p: p.stem,
        reverse=True,
    )
    arch = ["# 历史摘要", "", "按日期倒序排列。", ""]
    for p in files:
        arch.append(f"- [{p.stem}](digests/{p.name})")
    arch.append("")
    (docs / "archive.md").write_text("\n".join(arch), encoding="utf-8")


def main() -> None:
    today = datetime.datetime.utcnow().date().isoformat()
    DIGEST_DIR.mkdir(parents=True, exist_ok=True)
    try:
        digest_md = build_digest(today)
    except Exception as exc:
        # 兜底：即便整体失败也写出文件，保证今天仍有一次提交。
        digest_md = (
            f"# arXiv 每日摘要 · {today}\n\n"
            f"> 今日抓取失败：{exc}\n"
        )
    (DIGEST_DIR / f"{today}.md").write_text(digest_md, encoding="utf-8")
    refresh_index_and_archive(today, digest_md)
    print(f"wrote digest for {today}")


if __name__ == "__main__":
    main()
