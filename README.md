# arXiv 每日摘要 · arXiv Daily Digest

每天自动抓取几个指定方向在 arXiv 上最近提交的新论文，生成一份带中文分区标注的摘要，提交到本仓库并发布到 GitHub Pages。

在线阅读：<https://yingwang.github.io/arxiv-daily/>

## 特点

- **零依赖、零 key**：抓取脚本 `fetch_arxiv.py` 只用 Python 标准库，走 arXiv 公开 API，不需要任何 API key，也不产生费用。
- **全自动**：每天由 GitHub Actions 定时运行，无需本机开机。
- **每天一次提交**：每次运行都会写出一个按日期命名的新文件，保证每天产生一次提交。

## 关注方向

当前抓取三个方向，定义在 `fetch_arxiv.py` 顶部的 `TOPICS`：

1. 图像复原 / 低层视觉
2. 扩散模型
3. 具身智能

想加减方向或调整关键词，改 `TOPICS` 即可，无需改动其它文件。

## 运行时间

定时任务见 `.github/workflows/daily-arxiv.yml`，默认每天 06:00 UTC 运行一次。也可以在仓库的 Actions 页面手动触发（workflow_dispatch）。

## 本地试跑

```bash
python3 fetch_arxiv.py
```

会在 `docs/digests/` 下生成当天的摘要，并刷新 `docs/index.md` 与 `docs/archive.md`。
