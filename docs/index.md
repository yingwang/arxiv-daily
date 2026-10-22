# arXiv 每日摘要 · 2026-10-22

> 自动抓取，方向：图像复原 / 低层视觉、大语言模型、具身智能。数据来自 arXiv API，仅收录最近两天提交的论文，标题与摘要保留英文原文。

## 图像复原 / 低层视觉

### [Training-free Acceleration for Blind Compressed Image Restoration via Activation-Calibrated Singular Value Decomposition](http://arxiv.org/abs/2610.29959v1)

- 作者：Suhang Yao, Xin Li, Xijun Wang, Yufei Wang, Yeying Jin 等 6 人
- 提交：2026-10-21 · 分类 cs.CV · arXiv:2610.29959v1

Transformer-based models achieve strong performance on blind compressed image restoration (CIR) under unknown compression settings, but their densely stacked projection operators make deployment costly. We study training-free acceleration for such models through an empirical, operator-level analysis.

### [Rethinking Underwater Image Enhancement: Learning through Text-Guided Degradation Curriculum](http://arxiv.org/abs/2610.29569v1)

- 作者：Hongri Tian, Wenxue Li, Tian Ye, Sixiang Chen, Lujia Wang 等 9 人
- 提交：2026-10-21 · 分类 cs.CV · arXiv:2610.29569v1

Existing paired clean-degraded datasets have advanced learning-based underwater image enhancement, but they remain either limited in scale or difficult to acquire, and still fail to adequately cover the diverse degradations encountered in real-world underwater environments.

### [WaFIR: Wavelet-Fourier Mixture-of-Experts with Subband-Adaptive Routing for Blind All-in-One Image Restoration](http://arxiv.org/abs/2610.29108v1)

- 作者：Trong Nhan Nguyen, Vu Hoang Minh Doan, Thanh Dat Le, Truong Tien Vo, Thi Thu Ha Vu 等 9 人
- 提交：2026-10-21 · 分类 cs.CV · arXiv:2610.29108v1

Blind all-in-one image restoration must adapt a shared model to heterogeneous and sometimes mixed degradations without a task label at test time. We introduce WaFIR, a decoder module that decomposes features into Haar subbands, summarizes each subband with a compact Fourier descriptor, and routes it to prompt-condition…

### [Diffusion Posterior Sampling with Uncertain Forward Models](http://arxiv.org/abs/2610.29102v1)

- 作者：Wentao Shangguan, Vivek K Goyal
- 提交：2026-10-21 · 分类 cs.CV · arXiv:2610.29102v1

Diffusion posterior samplers reconstruct signals by combining a pretrained diffusion prior with a measurement likelihood specified by a forward model and a noise model. Calibration and reference data can characterize uncertainty in the forward model's parameters, such as blur kernels or detector responses.

### [WorldSR: Harnessing World Knowledge Search for Grounded Image Super-Resolution](http://arxiv.org/abs/2610.28423v1)

- 作者：Junyuan Deng, Xinyi Wu, Zhenyao Wu, Song Wang, Yu Wang 等 6 人
- 提交：2026-10-20 · 分类 cs.CV · arXiv:2610.28423v1

Generative-prior-based super-resolution (SR) methods leverage implicit knowledge learned from large-scale models to enhance low-resolution inputs. However, such priors are inherently stochastic and optimized for diverse generation, conflicting with the deterministic, high-fidelity reconstruction required for SR.

### [PixelSR: Pixel-Space Orthogonal Flow Decoupling for Real-World Image Super-Resolution](http://arxiv.org/abs/2610.27759v1)

- 作者：Xiang Lv, Kai Zhao, Qiang Wang, Qiao Mo, Chao Zhou 等 6 人
- 提交：2026-10-20 · 分类 cs.CV · arXiv:2610.27759v1

Latent diffusion models have recently achieved remarkable progress in Real-world Image Super-Resolution (Real-SR). However, existing methods consistently exhibit a persistent seesaw effect: enhancing perceptual realism compromises structural fidelity.

## 大语言模型

### [LongZero: Enhancing Long-Context Reasoning in LLMs from Zero Data](http://arxiv.org/abs/2610.30132v1)

- 作者：Zhennan Wan, Jianfei Chen
- 提交：2026-10-21 · 分类 cs.CL · arXiv:2610.30132v1

Reinforcement learning (RL) is an effective way to strengthen the long-context reasoning of large language models (LLMs), but it needs training data that are long, diverse, challenging, and verifiable.

### [Environment Duels: A Microcosm of LLM Co-Evolution](http://arxiv.org/abs/2610.30116v1)

- 作者：Shibo Jin, Zhiqiu Xu, Yiling Zou, Shangyu Gong, Mayur Naik
- 提交：2026-10-21 · 分类 cs.CL · arXiv:2610.30116v1

Through a tangle of real-world interactions, from synthetic training pipelines to data shared on the open web, frontier LLMs absorb what their predecessors and competitors create.

### [Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research](http://arxiv.org/abs/2610.30113v1)

- 作者：Houde Qian, Zheng Jiang, Wenyi Li, Chenxi Xu, Xinjie Lin 等 12 人
- 提交：2026-10-21 · 分类 cs.CL · arXiv:2610.30113v1

Quantitative research is an iterative loop: a researcher proposes a market hypothesis, implements it as an executable signal, tests it on historical data, and decides what to keep.

### [Differentially Private Sparse Reward Estimation with Preference Feedback](http://arxiv.org/abs/2610.30099v1)

- 作者：Meng Ding, Mingxi Lei, Jie Zhang, Jinyan Liu, Di Wang
- 提交：2026-10-21 · 分类 cs.LG · arXiv:2610.30099v1

Reinforcement Learning with Human Feedback (RLHF) has become a central paradigm for aligning Large Language Models with human values. However, the reliance on sensitive preference data necessitates rigorous differential privacy (DP) guarantees to prevent user information leakage.

### [Circuits of LLM Classifiers](http://arxiv.org/abs/2610.30076v1)

- 作者：Hadi Khalaf, Sajani Vithana, Kunal Talreja, Haewon Jeong, Viveck R. Cadambe 等 6 人
- 提交：2026-10-21 · 分类 cs.LG · arXiv:2610.30076v1

Language models make it easy to build classifiers by simply prompting a model with the sample to classify. However, their predictions are neither deterministic nor uniformly reliable across samples.

### [Charts as Epistemic Actions for Experience-Driven Agentic Data Analysis](http://arxiv.org/abs/2610.30072v1)

- 作者：Xinzhe Wang, Xudong Weng, Zang Li, Shaolei Zhang
- 提交：2026-10-21 · 分类 cs.AI · arXiv:2610.30072v1

Data agents built on ReAct-style loops now execute complex analytical workflows over structured data, yet their intermediate reasoning still runs almost entirely through text.

### [HGM-Dual: Lineage-Aware Guided Agent Harness Optimization for Long-Horizon Planning](http://arxiv.org/abs/2610.30042v1)

- 作者：Sudipta Paul, Pengrui Quan, Aounon Kumar, Nicholas Tzou, Vivek Kulkarni 等 6 人
- 提交：2026-10-21 · 分类 cs.AI · arXiv:2610.30042v1

Harness optimization, which improves an agent's prompts, tools, and workflows, is an increasingly effective way to enhance agents built on frozen or closed-source LLMs.

### [What the Author Wrote, What the Agent Reads: Silent Cue Loss in Enterprise Document Ingestion](http://arxiv.org/abs/2610.30026v1)

- 作者：Yikai Zhao, Saurabh Pandey, Pradeep Kumar Misra
- 提交：2026-10-21 · 分类 cs.CL · arXiv:2610.30026v1

Enterprise agents act on documents. Before an agent can follow a policy, answer a compliance question or file a ticket, some ingestion layer must turn a Word file or PDF into tokens - and that layer is where an agent deployed in the wild silently loses information.

### [Code Comprehensor: Hierarchical Documentation and Cross-Modal Retrieval for Large Repositories](http://arxiv.org/abs/2610.30016v1)

- 作者：Sujoy Roychowdhury, Joseph H. R. Isaac, Jiangning Gao, Martin Klitte, Diarmuid Corcoran
- 提交：2026-10-21 · 分类 cs.SE · arXiv:2610.30016v1

Understanding large, complex, and rapidly evolving code bases remains a core challenge for software engineering at scale, hindering onboarding, maintenance, refactoring, and impact analysis.

### [Agent Behavior Maps: Locating Agents by What They Would Do, Without Running Them](http://arxiv.org/abs/2610.30014v1)

- 作者：Shota Fujikawa, Takuya Tamura, Kosuke Akimoto, Daichi Haraguchi, Masafumi Oyamada
- 提交：2026-10-21 · 分类 cs.LG · arXiv:2610.30014v1

LLM agents with similar success rates can follow different action sequences. An Agent Behavior Map represents LLM-harness combinations using centered action log-likelihoods on shared reference trajectories, without requiring new environment rollouts from the target agent.

### [Every Alarm Has a Cause: An Open Generator of Telecom Alarm Storms with Exact Root Causes, Bound to NORIA-O, RFC 8632 and TMF642](http://arxiv.org/abs/2610.30004v1)

- 作者：Madhulatha Mandarapu, Sandeep Kunkunuru
- 提交：2026-10-21 · 分类 cs.NI · arXiv:2610.30004v1

Alarm root-cause analysis is studied on data that cannot be shared. Operator logs are confidential, so what the field publishes is a causal graph between alarm types rather than per-incident causes, a fixed scenario set, gated, or never released.

### [EPIC: Rethinking Trust Regions for Autoregressive LLM Policies via Exact-KL Prefix Importance-Ratio Clipping](http://arxiv.org/abs/2610.29999v1)

- 作者：Chengxi Li, Hanlin Wu, Zhicheng Cai, Huan-ang Gao, Wei-Ying Ma 等 7 人
- 提交：2026-10-21 · 分类 cs.LG · arXiv:2610.29999v1

Reinforcement learning (RL) based on PPO-style clipping has become an effective approach to improving the reasoning capabilities of large language models (LLMs). However, standard token-level clipping measures policy change only through the conditional probability of the current token, while the prefix conditioning con…

## 具身智能

### [Multimodal Embodied Agents: A Unified Capability-centric Perspective from Computer-Use to Robot-Use](http://arxiv.org/abs/2610.30108v1)

- 作者：Yanzhe Chen, Ziyi Yang, Jifeng Zhu, Qiming Huang, Ruihe An 等 17 人
- 提交：2026-10-21 · 分类 cs.RO · arXiv:2610.30108v1

Multimodal agents (MMAs) sustain interaction through reasoning, memory, tools, and feedback, most visibly as computer-use agents, while robotic systems (RSs) couple sensing and actuation under physical dynamics.

### [AtomicRL: Atomic Reinforcement Learning for Long-Horizon Robotic Manipulation](http://arxiv.org/abs/2610.30097v1)

- 作者：Likui Zhang, Zhe Zhu, Zhihao Zhan, Yibo Bai, Hanlin Wang 等 10 人
- 提交：2026-10-21 · 分类 cs.RO · arXiv:2610.30097v1

Vision-language-action (VLA) models have shown promise in robotic manipulation, but imitation learning (IL) alone often struggles to master complex long-horizon skills. Reinforcement learning (RL) offers an effective avenue for further improving VLA policies.

### [SP-HLM: Sparse-Pose-Driven Motion Generation and Whole-Body Control for Humanoid Loco-Manipulation](http://arxiv.org/abs/2610.30044v1)

- 作者：Zhaohui Yang, Quanbao Lin, Chengqi Shi, Zhenglang Weng, Jicheng Lin 等 12 人
- 提交：2026-10-21 · 分类 cs.RO · arXiv:2610.30044v1

Humanoid loco-manipulation requires an effective interface between high-level task policies and whole-body control. Existing interfaces typically rely on a single action representation for both task intent and whole-body coordination. This may burden the high-level policy or leave one aspect underspecified.

### [TARSphere: A Robot-Oriented Full-Stack Framework for Long-Horizon Embodied Agents in Evolving Physical and Social Environments](http://arxiv.org/abs/2610.30043v1)

- 作者：Yicheng Xu, Zhikai Xu, Ziyuan Chen, Yuhang Dong, Tao Zhang 等 8 人
- 提交：2026-10-21 · 分类 cs.RO · arXiv:2610.30043v1

Robots must act under physical and social constraints while adapting to changes in their environment and human needs. Existing embodied-agent systems often focus on specified goals or abstract execution into symbolic actions, limiting evaluation in an evolving world.

### [Post-hoc Epistemic Uncertainty for Vision-Language-Action Policies](http://arxiv.org/abs/2610.29730v1)

- 作者：Johannes Keller, Albrecht M. Bloße, Adrian Lindenmeyer, Thomas Neumuth, Daniel Schneider
- 提交：2026-10-21 · 分类 cs.RO · arXiv:2610.29730v1

Vision-language-action (VLA) policies need to recognize gaps in their training knowledge to request useful demonstrations or assistance in new situations, especially when failures are costly.

### [Reconstruction-Augmented Visuomotor Pre-Training of 3D-Grounded Bimanual Dexterity from RGB-Only Human Videos](http://arxiv.org/abs/2610.29716v1)

- 作者：Xingyi He, Zhiwen Qiu, Adhitya Polavaram, Yunhao Cao, Cory Fan 等 8 人
- 提交：2026-10-21 · 分类 cs.RO · arXiv:2610.29716v1

We present SpatialDex, a framework that learns 3D-grounded bimanual dexterity from RGB-only human videos through reconstruction-augmented visuomotor pre-training. The central idea is to learn human behavior together with its spatial context.

### [CausGround: Causal Interaction Grounding for Adaptive Embodied Planning](http://arxiv.org/abs/2610.29702v1)

- 作者：Yijun Shen, Diqi He, Jinbang Guo, Wanyue Zhang, Jiaming Mi 等 9 人
- 提交：2026-10-21 · 分类 cs.RO · arXiv:2610.29702v1

Multimodal large language models (MLLMs) show promising reasoning capabilities, but reliable physical interaction requires planning that accounts for when actions are executable and how they change the world.

### [FlowVLA: Learning Flow-Aware Physical Completion for Quantitative Robotic Pouring](http://arxiv.org/abs/2610.29692v1)

- 作者：Liwen Yang, Yutian Zhang, Jiaqi Zhai, Li Yang, Tutian Tang 等 13 人
- 提交：2026-10-21 · 分类 cs.RO · arXiv:2610.29692v1

During steady pouring, images and robot pose may remain nearly unchanged while transferred mass accumulates, making the return decision ambiguous for a whole-task vision-language-action (VLA) policy. We present FlowVLA, which separates motor generation from physical-completion estimation.

### [From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation](http://arxiv.org/abs/2610.29560v1)

- 作者：Tingwen Du, Haoyu Guo, Hanxue Zhang, Xuanxu Wang, Junting Dong 等 12 人
- 提交：2026-10-21 · 分类 cs.RO · arXiv:2610.29560v1

Vision-language-action (VLA) models achieve strong performance across embodied manipulation tasks by unifying visual understanding, language conditioning, and action generation.

### [Plan First, Act Later: Streaming Reasoning for Executable Memory in Robot Control](http://arxiv.org/abs/2610.29329v1)

- 作者：Qinghang Liu, Conglin Wang, Zongsheng Li, Boyong He, Han Gao 等 9 人
- 提交：2026-10-21 · 分类 cs.RO · arXiv:2610.29329v1

Long-horizon robot manipulation requires a robot to remember task-relevant information beyond its short observation window. Existing memory-augmented policies typically retrieve relevant information from history and reason over it at execution time, placing a heavy reasoning burden on the high-level model.

### [Failure Modes of Vision-Language Models for Human Activity Understanding in Thermal HRI](http://arxiv.org/abs/2610.29244v1)

- 作者：Han Hu, He Chen
- 提交：2026-10-21 · 分类 cs.CV · arXiv:2610.29244v1

Thermal cameras enable robots to perceive human activities in darkness while revealing less personally identifiable appearance information and fewer details of the surrounding environment than RGB cameras.

### [NavBind: Diagnosing Instruction-Action Binding at Route Forks in Navigation VLAs](http://arxiv.org/abs/2610.29203v1)

- 作者：Josh Qixuan Sun, Xiaoying Xing, Yurun Chen, Huaiyuan Weng, Wentao Zhu 等 6 人
- 提交：2026-10-21 · 分类 cs.RO · arXiv:2610.29203v1

Vision-language-action (VLA) navigation models translate visual observations and instructions into actions. Navigation success assesses whether an agent reaches the goal.

---

本期共收录 30 篇。
