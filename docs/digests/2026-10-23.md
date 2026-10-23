# arXiv 每日摘要 · 2026-10-23

> 自动抓取，方向：图像复原 / 低层视觉、大语言模型、具身智能。数据来自 arXiv API，仅收录最近两天提交的论文，标题与摘要保留英文原文。

## 图像复原 / 低层视觉

### [GigaBench: Benchmarking Learnable Representations for Gigapixel Image Compression and Super-Resolution](http://arxiv.org/abs/2610.31644v1)

- 作者：Matteo Fusconi, Alex Costanzino, Pierluigi Zama Ramirez, Luigi Di Stefano
- 提交：2026-10-22 · 分类 cs.CV · arXiv:2610.31644v1

Learnable Representations (LRs) can fit parametric families of functions to diverse kinds of signals. These emergent neural-native data formats are gathering interest in the scientific community due to their compactness, resolution-agnosticism and amenability to direct neural processing.

### [Squaring-the-Sphere: Distortion-Free and Seamless Panorama Generation via CubeAtlas](http://arxiv.org/abs/2610.31565v1)

- 作者：Xuhui Zuo, Chenjie Cao, Tengfei Wang, Junta Wu, Yisu Zhang 等 6 人
- 提交：2026-10-22 · 分类 cs.CV · arXiv:2610.31565v1

Generating 360-degree panoramas requires both local perspective fidelity and global spherical continuity. Existing representations face a trade-off: equirectangular projection (ERP) enables seamless panorama modeling but suffers from severe distortion and a domain gap to pre-trained image generators, whereas cubemaps p…

### [Self-Supervised Multibeam Sonar Restoration via Coherent Forward Modeling](http://arxiv.org/abs/2610.31490v1)

- 作者：Zixin Wang, James Hopgood, Mike Davies
- 提交：2026-10-22 · 分类 eess.IV · arXiv:2610.31490v1

Multibeam imaging sonar produces intensity images degraded by coherent speckle and system-induced blur, while clean reflectivity targets are rarely available. Existing despeckling methods often rely on simplified intensity-domain noise models, synthetic clean targets, or blind-spot self-supervision, and typically do no…

### [GLOW-FM: Efficient Generative Low-Light Image Enhancement with One-Step Latent Flow Matching](http://arxiv.org/abs/2610.31222v1)

- 作者：Ariel Lapid, Yuval Haitman, Reuven Peretz, Arnon Netzer, Idit Diamant
- 提交：2026-10-22 · 分类 cs.CV · arXiv:2610.31222v1

Low-light image enhancement (LLIE) aims to recover well-exposed and perceptually faithful images from severely degraded observations. Recent diffusion-based generative methods achieve strong perceptual quality by leveraging powerful image priors, but their iterative sampling incurs substantial computational cost, limit…

### [Training-free Acceleration for Blind Compressed Image Restoration via Activation-Calibrated Singular Value Decomposition](http://arxiv.org/abs/2610.29959v2)

- 作者：Suhang Yao, Xin Li, Xijun Wang, Yufei Wang, Yeying Jin 等 6 人
- 提交：2026-10-21 · 分类 cs.CV · arXiv:2610.29959v2

Transformer-based models achieve strong performance on blind compressed image restoration (CIR) under unknown compression settings, but their densely stacked projection operators make deployment costly. We study training-free acceleration for such models through an empirical, operator-level analysis.

### [Rethinking Underwater Image Enhancement: Learning through Text-Guided Degradation Curriculum](http://arxiv.org/abs/2610.29569v2)

- 作者：Hongri Tian, Wenxue Li, Tian Ye, Sixiang Chen, Zongxian Su 等 10 人
- 提交：2026-10-21 · 分类 cs.CV · arXiv:2610.29569v2

Existing paired clean-degraded datasets have advanced learning-based underwater image enhancement, but they remain either limited in scale or difficult to acquire, and still fail to adequately cover the diverse degradations encountered in real-world underwater environments.

### [WaFIR: Wavelet-Fourier Mixture-of-Experts with Subband-Adaptive Routing for Blind All-in-One Image Restoration](http://arxiv.org/abs/2610.29108v1)

- 作者：Trong Nhan Nguyen, Vu Hoang Minh Doan, Thanh Dat Le, Truong Tien Vo, Thi Thu Ha Vu 等 9 人
- 提交：2026-10-21 · 分类 cs.CV · arXiv:2610.29108v1

Blind all-in-one image restoration must adapt a shared model to heterogeneous and sometimes mixed degradations without a task label at test time. We introduce WaFIR, a decoder module that decomposes features into Haar subbands, summarizes each subband with a compact Fourier descriptor, and routes it to prompt-condition…

### [Diffusion Posterior Sampling with Uncertain Forward Models](http://arxiv.org/abs/2610.29102v1)

- 作者：Wentao Shangguan, Vivek K Goyal
- 提交：2026-10-21 · 分类 cs.CV · arXiv:2610.29102v1

Diffusion posterior samplers reconstruct signals by combining a pretrained diffusion prior with a measurement likelihood specified by a forward model and a noise model. Calibration and reference data can characterize uncertainty in the forward model's parameters, such as blur kernels or detector responses.

## 大语言模型

### [Reliable AI-Assisted Decisions via Selective Auditing](http://arxiv.org/abs/2610.31662v1)

- 作者：Isaac Gibbs, Elise L. Han, Ryan J. Tibshirani, Tijana Zrnic
- 提交：2026-10-22 · 分类 stat.ML · arXiv:2610.31662v1

We consider online monitoring of an AI system that produces a sequence of decisions. At each round, the system outputs a proposed decision together with a confidence score estimating the trustworthiness of the decision.

### [Cost-Aware Abstention for LLM-Based IT Ticket Classification](http://arxiv.org/abs/2610.31657v1)

- 作者：Sachin Gupta
- 提交：2026-10-22 · 分类 cs.LG · arXiv:2610.31657v1

Wrong automatic routing of an IT support ticket can cost more than human triage. We evaluate cost-aware abstention as an offline, cost-conditional readiness assessment: select a routing policy on calibration data under explicit costs, then evaluate that frozen policy once on held-out test data.

### [EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence](http://arxiv.org/abs/2610.31650v1)

- 作者：Qijin Zhang, Hanzhen Wang, Yuehan Zhao, Haoyu Dai, Yao Shu 等 7 人
- 提交：2026-10-22 · 分类 cs.AI · arXiv:2610.31650v1

Tool-using language model agents rely on environmental facts to decide whether an action is permitted. When a tool response omits a safety-relevant fact, an agent may carry out a prohibited action even though the user request is benign and every returned statement is true.

### [Causal Chain of Thought: Mitigating Attention Leakage via Context Isolation](http://arxiv.org/abs/2610.31639v1)

- 作者：Gabriele Dominici, Teague McMillan, Fazl Barez, Marc Langheinrich, Martin Gjoreski
- 提交：2026-10-22 · 分类 cs.LG · arXiv:2610.31639v1

Chain-of-thought (CoT) prompting elicits step-by-step rationales that appear to explain model predictions, but there is no guarantee these steps causally drive the final answer.

### [Can an Agent Debug a Web Corpus? Agentic Auditing of Slovak FineWeb2](http://arxiv.org/abs/2610.31636v1)

- 作者：Marek Šuppa, Ivan Vykopal, Jaroslav Kopčan
- 提交：2026-10-22 · 分类 cs.CL · arXiv:2610.31636v1

Multilingual pipelines such as FineWeb2 apply one recipe across a thousand languages, leaving the failure modes of individual languages unanticipated. We use an LLM once, as a corpus debugger rather than a classifier: a tool-using agent explores the corpus through a read-only, budgeted API and compiles each finding int…

### [Questioning Instrumental Convergence in RLVR: Checkpoint Evidence from OLMo-3](http://arxiv.org/abs/2610.31624v1)

- 作者：Barış Alparslan, Sandy Tanwisuth, Caleb Petterson
- 提交：2026-10-22 · 分类 cs.LG · arXiv:2610.31624v1

Instrumental convergence is often invoked as a general reason to expect capable agents to acquire or express power-seeking subgoals: self-preservation, resource acquisition, deception, or resistance to oversight which poses an important threat to the society.

### [How Ground Truth Shapes Retrieval Scores: Evidence-Aware Evaluation of a Retrieval-Augmented Generation System for Breast Lesions](http://arxiv.org/abs/2610.31606v1)

- 作者：Miguel Mochizuki Silva, Samuel Ismael, Mateus C. Dias, Thaís Gaudêncio, Yuri Malheiros 等 6 人
- 提交：2026-10-22 · 分类 cs.CL · arXiv:2610.31606v1

Purpose: To describe an evidence-aware retrieval evaluation protocol for a clinical retrieval-augmented generation (RAG) system over breast lesion management literature, addressing the dependence of retrieval scores on annotation coverage.

### [VERA: A Responsible AI Dashboard for Assessing LLM Deployments in Light of the EU AI Act](http://arxiv.org/abs/2610.31588v1)

- 作者：Robin Quériaux, Solveig Bachellery, Léa Déléris, Saurabhsingh Rajput, Mariam Barry 等 7 人
- 提交：2026-10-22 · 分类 cs.SE · arXiv:2610.31588v1

Institutions that deploy large language models in regulated settings often need technical evidence of responsible AI practices before approving a deployment. COMPL-AI provides a technical interpretation of the EU AI Act that organises this evidence under six principle groups and eighteen technical requirements, twelve…

### [Who Is Sycophantic to Whom? Confident LLMs, Human Deference, and the Collapse of Trust Calibration](http://arxiv.org/abs/2610.31579v1)

- 作者：Deepthika S, Pawni Yadav, B. Sankar
- 提交：2026-10-22 · 分类 cs.AI · arXiv:2610.31579v1

Research on sycophancy asks whether large language models (LLMs) bend towards what their users want to hear. We ask the reverse question: when an LLM is confident, consistent, and wrong, do users bend towards it? In a within-subjects experiment, 32 participants learned up to five science topics by chatting with five as…

### [Rethinking Sequence Compression with Test-time Regression](http://arxiv.org/abs/2610.31574v1)

- 作者：Sihan Yang, Jie Huang, Hanxuan Li, Yifan Guo, Weigao Sun 等 7 人
- 提交：2026-10-22 · 分类 cs.LG · arXiv:2610.31574v1

Sequence compression is a fundamental operation and a critical information bottleneck in efficient language and multimodal models, and yet prevailing approaches based on pooling or learned projections remain underperforming.

### [Social-HUMINT: An LLM-Augmented Unified Framework for Measuring Social Media Exposure](http://arxiv.org/abs/2610.31573v1)

- 作者：Pellegrino Casoria, Simon Pietro Romano
- 提交：2026-10-22 · 分类 cs.CR · arXiv:2610.31573v1

In the post-API landscape, social-media profiling has become inexpensive and automated: Large Language Models (LLMs) can extract structured information from unstructured content and deduce attributes users never disclosed. A person's true exposure is not what they post but what can be inferred from it.

### [On the Token Collapse Phenomenon in Textual Graph Soft Prompting](http://arxiv.org/abs/2610.31572v1)

- 作者：Andrea Giuseppe Di Francesco, Rishabh Jain, Franco Maria Nardini, Nicola Tonellotto, Pietro Liò 等 6 人
- 提交：2026-10-22 · 分类 cs.LG · arXiv:2610.31572v1

Recent methods for injecting graph structure into LLM prompts include graph soft prompting, in which a graph neural network (GNN) learns graph-specific tokens that capture relational information among entities in textual prompts.

## 具身智能

### [Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success](http://arxiv.org/abs/2610.31670v1)

- 作者：Yunfei Xie, Howard H. Qian, Shiyi Lan, Kaiyu Hang, Chen Wei
- 提交：2026-10-22 · 分类 cs.CV · arXiv:2610.31670v1

Robotic foundation models are typically evaluated through costly closed-loop rollouts, which motivates cheap offline proxies for model capability. The Platonic Representation Hypothesis (PRH) suggests that as representations improve, different modalities such as vision and language converge toward a shared statistical…

### [OpenTac: An Open Ecosystem for Customizable, Scalable, and Transferable 3D Tactile Sensing](http://arxiv.org/abs/2610.31661v1)

- 作者：Ariel Slepyan, Geeta Chandra Raju Bethala, Jiafeng Gu, Anagha Rajendra Dangle, Yinzhe Zhou 等 15 人
- 提交：2026-10-22 · 分类 cs.RO · arXiv:2610.31661v1

We present OpenTac, a novel sensor and a full-stack ecosystem for tactile skins that are highly customizable, scalable, and readily deployed in downstream robot control and learning applications. Our core contribution is twofold.

### [Progress Probes $P^2$: Lightweight Runtime Monitoring for Vision-Language-Action Models](http://arxiv.org/abs/2610.31613v1)

- 作者：Atiksh Bhardwaj, Edward W. Duan, Junwon Seo, Prithwish Dan, Wei-Chiu Ma 等 7 人
- 提交：2026-10-22 · 分类 cs.RO · arXiv:2610.31613v1

Vision-Language-Action (VLA) models can perform diverse manipulation tasks directly from visual observations and natural language instructions, but they remain prone to mistakes and unpredictable failures.

### [Echo: Coupled Action and Task Status Signal Denoising for Vision Language Action Models](http://arxiv.org/abs/2610.31569v1)

- 作者：Yufeng Liu, Bohao Fan, Juntu Zhao, Xinyi Wang, Hang Yu 等 14 人
- 提交：2026-10-22 · 分类 cs.RO · arXiv:2610.31569v1

Recognizing task completion and failure enables robots to stop upon success and initiate recovery or replanning after failure. Existing methods augment Vision Language Action (VLA) policies with task status signal prediction to support these execution decisions.

### [Point-Level Refinable Semantic Mapping for Spatial Understanding](http://arxiv.org/abs/2610.31476v1)

- 作者：Taimeng Fu, Yi Du, Zitong Zhan, Qiwei Du, Shaoshu Su 等 7 人
- 提交：2026-10-22 · 分类 cs.RO · arXiv:2610.31476v1

Open-vocabulary 3D semantic maps have emerged as a key spatial memory representation for long-horizon robot autonomy, enabling robots to reason about objects, their spatial relationships, and past observations across time.

### [A Sparse Topometric Graph for Scalable Cross-Session Indoor Navigation](http://arxiv.org/abs/2610.31432v1)

- 作者：Eun Sun Lee, Minkyun Seo, Gwangtak Bae, Junho Kim, Seunggu Kang 等 7 人
- 提交：2026-10-22 · 分类 cs.RO · arXiv:2610.31432v1

A conventional embodied agent in an indoor environment builds a map by accumulating noisy real-world measurements and results from heavy inference to guide navigation.

### [FocusVLA: Future-Intent Guided Dynamic View Routing for Vision-Language-Action Models](http://arxiv.org/abs/2610.31423v1)

- 作者：Huixin Xu, Ziya Yu, Peng Li
- 提交：2026-10-22 · 分类 cs.RO · arXiv:2610.31423v1

Vision-language-action (VLA) models have become an important paradigm for robotic manipulation by unifying visual perception, language understanding, and action generation.

### [Learning Robot Behavior Priors from Non-Robotic Synthetic Data](http://arxiv.org/abs/2610.31275v1)

- 作者：Mateusz Odrowaz-Sypniewski, Michael Amir, Jasmine Bayrooti, Ajay Shankar, Amanda Prorok
- 提交：2026-10-22 · 分类 cs.RO · arXiv:2610.31275v1

Real robot data, rich across tasks and morphologies, is often treated as the bottleneck for training robot learning models, including embodied foundation models that aim for zero-shot physical transfer.

### [Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation](http://arxiv.org/abs/2610.31166v1)

- 作者：Chenyuan Chen, Ran Ding, Lechen Zhang, Zewen He, Yoshihiko Nakamura
- 提交：2026-10-22 · 分类 cs.RO · arXiv:2610.31166v1

Humanoid loco-manipulation in dynamic scenes is non-Markovian: cues vanish as objects change or are hidden, or leave the view as the robot turns and walks, yet whole-body vision-language-action (VLA) policies see only the present.

### [Navigating human-robot interaction challenges in private and residential aged care homes](http://arxiv.org/abs/2610.31149v1)

- 作者：David Ahmedt-Aristizabal, Mohammad Ali Armin, Akila Pemasiri, Harshala Gammulle, Tharindu Fernando 等 7 人
- 提交：2026-10-22 · 分类 cs.HC · arXiv:2610.31149v1

This chapter explores how robotic systems and ambient intelligence can enhance care for older adults in residential aged care (RAC) homes and private homes. Although these settings differ, we frame both as extreme and challenging environments for human-robot interaction (HRI), characterised by cluttered and dynamic lay…

### [Revisiting Distribution Matching for State-to-Vision Policy Distillation in Laparoscopic Robotic Manipulation](http://arxiv.org/abs/2610.31010v1)

- 作者：Mingyu Sheng, Jianan Fan, Dongnan Liu, Guoyan Zheng, Ron Kikinis 等 6 人
- 提交：2026-10-22 · 分类 cs.RO · arXiv:2610.31010v1

End-to-end control policies trained via Reinforcement Learning (RL) have emerged as an alternative to conventional surgical robotic control approaches, with recent studies exploring state-based policies trained on privileged state observations.

### [In-Context Learning World Models for Robot Dual-Arm Manipulation of Soft Garment with Partial Observations](http://arxiv.org/abs/2610.30988v1)

- 作者：Hengyi Sim, Quentin Rouxel, Dennis Hong, Darwin Caldwell, Fei Chen
- 提交：2026-10-22 · 分类 cs.RO · arXiv:2610.30988v1

Robust manipulation of soft objects, such as garments, is a critical skill for service and household robots to adopt, but remains challenging due to its high-dimensional state space, and material-dependent deformations.

---

本期共收录 32 篇。
