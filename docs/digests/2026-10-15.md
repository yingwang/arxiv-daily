# arXiv 每日摘要 · 2026-10-15

> 自动抓取，方向：图像复原 / 低层视觉、大语言模型、具身智能。数据来自 arXiv API，仅收录最近两天提交的论文，标题与摘要保留英文原文。

## 图像复原 / 低层视觉

### [VascuSR: Iterative Anatomy-Aware Diffusion for CT Super-Resolution](http://arxiv.org/abs/2610.20509v1)

- 作者：Hairong Ni, Jiahe Huang, Minghao Guo, Wojciech Matusik, Rose Yu
- 提交：2026-10-14 · 分类 cs.CV · arXiv:2610.20509v1

Generative super-resolution (SR) can recover sharp detail in computed tomography (CT) images from severely downsampled observations, but the missing high-frequency content is not uniquely determined by the low-resolution input.

### [Look Before You Restore: Learning to Predict Before Acting for Agentic Image Restoration](http://arxiv.org/abs/2610.20384v1)

- 作者：Xu Zhang, Jun Wan, Lefei Zhang, Liangpei Zhang
- 提交：2026-10-14 · 分类 cs.CV · arXiv:2610.20384v1

Agents for mixed-degradation image restoration typically learn what a tool does to an image only after running it: failed calls waste computation and harmful outputs go unnoticed until too late. We propose PreActIR, an agentic restoration framework that predicts tool consequences before execution.

### [Physics-Shaped, Not Physical: Auditing Physics-Guided Underwater Image Restoration](http://arxiv.org/abs/2610.19763v1)

- 作者：Mochamad Rizal Fauzan, Irgi Surya
- 提交：2026-10-14 · 分类 cs.CV · arXiv:2610.19763v1

Physics-guided networks for underwater image restoration predict transmission and backscatter and invert the image-formation model, yet rarely test whether this physics does any work.

### [Denoise X: Self-Supervised U-Net for Quantum Mottle Suppression in Chest Radiography](http://arxiv.org/abs/2610.18556v1)

- 作者：Parth Giramkar, Aryan Patle, Vanita Kshirsagar
- 提交：2026-10-13 · 分类 cs.CV · arXiv:2610.18556v1

Deep learning for medical image restoration is often constrained by the need for paired training data. Acquiring perfectly registered clean-noisy radiographs in vivo is impractical due to patient motion and radiation-dose limits.

### [$\mathrm{S}^3$-PnP: Plug-and-Play Denoising for Scientific Imaging with Self-Supervised Score Priors](http://arxiv.org/abs/2610.18458v1)

- 作者：Yukun Cui, Jiangshe Zhang, Shuang Xu, Lilun Deng, Haowen Bai 等 9 人
- 提交：2026-10-13 · 分类 cs.CV · arXiv:2610.18458v1

Modern image restoration methods increasingly rely on large-scale supervised training, yet clean targets are often prohibitively difficult to obtain in scientific imaging modalities such as hyperspectral imaging (HSI) and magnetic resonance imaging (MRI).

### [Dynamic Interpolation for Training-Time Prediction Reshaping in Low-Light Image Enhancement](http://arxiv.org/abs/2610.18018v1)

- 作者：Peirui Zhu, Shijie Hao, Jingxi Liao, Richang Hong, Meng Wang
- 提交：2026-10-13 · 分类 cs.CV · arXiv:2610.18018v1

Low-light image enhancement (LLIE) is an important image/video processing problem for reliable visual systems under poor illumination, yet it remains challenging due to the strong coupling among insufficient illumination, noise amplification, and structural degradation.

### [PolUR: Polarization Aware Multimodal Degradation Perception for Underwater Image Restoration](http://arxiv.org/abs/2610.17991v1)

- 作者：Wenshuo Zhang, Xiangyue Zhang, Junlin Li, Wenjie Tian, Yubo Zheng 等 8 人
- 提交：2026-10-13 · 分类 cs.CV · arXiv:2610.17991v1

Recovering high-quality images from degraded underwater observations is crucial for underwater exploration. Polarization observations show promise as an effective source of complementary physical cues for recovering target radiance under clear-water conditions.

### [Recovery-Oriented Optical System Design Based on Fisher Information](http://arxiv.org/abs/2610.17950v1)

- 作者：Zhuang Qian, Yan Mo, Hao Tan, Yu Chen, Haibo Wang 等 8 人
- 提交：2026-10-13 · 分类 physics.optics · arXiv:2610.17950v1

Traditional optical system design for imaging applications has long been guided by image quality metrics such as geometrical RMS spot size, wavefront error, and modulation transfer function (MTF).

### [FlashVSR+: Efficient Video Super-Resolution via Hybrid Attention and Reward-Yield Distribution Matching](http://arxiv.org/abs/2610.17552v1)

- 作者：Ruchang Yao, Shi Guo, Junhao Zhuang, Mingde Yao, Xin Cai 等 10 人
- 提交：2026-10-13 · 分类 cs.CV · arXiv:2610.17552v1

Recent video super-resolution (VSR) models achieve efficient one-step generation through diffusion distillation. However, high-resolution inference remains costly, and distilled models are difficult to align with human preferences.

## 大语言模型

### [One Task, Many Interfaces: Simple Cross-Interface Consistency Training Improves LLM Agent Robustness](http://arxiv.org/abs/2610.20576v1)

- 作者：Artin Tajdini, Manpreet Kaur, Peng Qi
- 提交：2026-10-14 · 分类 cs.LG · arXiv:2610.20576v1

Post-training binds the competence of an LLM agent to the interface it was trained on. Semantics-preserving perturbations of that interface, such as renaming an action or changing the notation, leave the underlying task unchanged yet make the agent worse at it.

### [Beyond LLM Judge: Mechanical Verification for Agentic Autoformalization](http://arxiv.org/abs/2610.20573v1)

- 作者：Anna Mei, Michael R. Douglas
- 提交：2026-10-14 · 分类 cs.LO · arXiv:2610.20573v1

We introduce a novel method for verifying Lean formalizations that goes beyond LLM-judged faithfulness. Unlike most verification methods, which rely on LLMs or trained models, our method combines LLM-based semantic review with mechanical numerical and vacuity checks, providing checkable feedback and detecting errors mi…

### [Manacá-1B-Instruct-2: Reproducible Safety Alignment for a Native Brazilian-Portuguese LLM. Negative DPO Results, a Controlled Composition Scan, and a Silent Failure Mode of the LLM Judge](http://arxiv.org/abs/2610.20570v1)

- 作者：Bruno Leonardo Santos Menezes, Carlos Leonardo Souza Cardoso, Fabio André Machado Porto
- 提交：2026-10-14 · 分类 cs.CL · arXiv:2610.20570v1

Brazilian Portuguese remains underserved by open-source language models, and the few that are safety-aligned rarely document what did not work or validate comparisons with statistical significance.

### [Scaling Discovery Requires Forgetting](http://arxiv.org/abs/2610.20563v1)

- 作者：Shangyin Tan, Ben Zhou, Lakshya A Agrawal, Jialin Zhang, Yilin Chen 等 11 人
- 提交：2026-10-14 · 分类 cs.AI · arXiv:2610.20563v1

Automated research with LLM agents has shown promising results in various domains. Through iterative refinement and scored verifiers, LLM agents are capable of discovering new ideas.

### [PhySGA: A Physics-Space Grounded Agentic Framework for Generalizable and Interactive 3D Composition](http://arxiv.org/abs/2610.20560v1)

- 作者：Weichen Lyu, Chong Xia, Mingyu Dong, Long Xu, Shengjun Zhang 等 6 人
- 提交：2026-10-14 · 分类 cs.AI · arXiv:2610.20560v1

3D object composition is pivotal to digital content creation and robot simulation, while also serving as a critical testbed for physical intelligence in foundation models.

### [PerSo: Investigating Facets of LLMs' Social Intelligence in Real-World Persuasion Scenarios](http://arxiv.org/abs/2610.20548v1)

- 作者：Ali Zamani, Soroush Esfahanian, Erfan Shahabi, Mohammad Taher Pilehvar, Azadeh Shakery 等 6 人
- 提交：2026-10-14 · 分类 cs.CL · arXiv:2610.20548v1

Understanding the social intelligence of large language models (LLMs) is increasingly important for applications involving human-AI interaction and multi-agent environments.

### [Bayesian Learning to Select Fair Classifiers](http://arxiv.org/abs/2610.20514v1)

- 作者：Saatvik Kher, Hyungrok Do, Judy Zhong, Padhraic Smyth
- 提交：2026-10-14 · 分类 cs.LG · arXiv:2610.20514v1

Evaluations of classifiers (AI or human or agents) often assume a batch setting in which every agent produces labels on every example in a test set, which can be expensive or impractical in many contexts.

### [Decoupled Marginal Sharpening for Training-Free Inference-Time Scaling](http://arxiv.org/abs/2610.20483v1)

- 作者：Weixin Wang, Wei Deng, Anderson Schneider, Yuriy Nevmyvaka, Pan Xu 等 6 人
- 提交：2026-10-14 · 分类 cs.LG · arXiv:2610.20483v1

We study how to improve LLM reasoning at inference time without updating model weights or using external reward models. Recent reward-free power-sampling methods define the sequence-level power target $π_α(y\mid x)\propto p_0(y\mid x)^α$, where $α>1$, which increases the relative probability of completions that are alr…

### [ChronoCulture: Evaluating Cultural Awareness Across Time in Large Language Models](http://arxiv.org/abs/2610.20472v1)

- 作者：Rusali Saha, Nitya Khurana, Ruihong Huang, Kuan-Hao Huang
- 提交：2026-10-14 · 分类 cs.CL · arXiv:2610.20472v1

Cultural attitudes and social norms evolve over time, yet most cultural benchmarks for large language models (LLMs) treat culture as a static attribute of a country or region. We introduce ChronoCulture, a benchmark of 10,360 temporal pairs built from longitudinal survey data across 72 countries.

### [Equal CER, Unequal Damage: Severity-Weighted Character Error Rate for OCR](http://arxiv.org/abs/2610.20461v1)

- 作者：Nguyen Nguyen, Yongyi Zang
- 提交：2026-10-14 · 分类 cs.CL · arXiv:2610.20461v1

Character Error Rate (CER), the standard metric for OCR and vision-language models (VLMs), charges a typo as much as a wrong name. We introduce semCER, which keeps CER's alignment and denominator and charges each grapheme edit a severity from an LLM judge, with no word segmentation.

### [MolLean: A Process-Verifiable Language for Chemical Reasoning](http://arxiv.org/abs/2610.20459v1)

- 作者：Jiatong Li, Yatao Bian
- 提交：2026-10-14 · 分类 cs.CL · arXiv:2610.20459v1

Chemical chain-of-thought can contain hallucinated structural and property claims. We thereby introduce MolLean, a process-verifiable language that grounds chemical reasoning in an explicit molecular state.

### [From Training to Escalation: Forensic Analysis and Local Recreation of RL/RLHF-Induced Privilege Escalation in AI Agents (CVE-2026-65616)](http://arxiv.org/abs/2610.20437v1)

- 作者：Alicia Colmenero-Fernández
- 提交：2026-10-14 · 分类 cs.MA · arXiv:2610.20437v1

Mid-2026 reporting on autonomous AI evaluation incidents claimed that frontier large language model (LLM) agents escaped server containment through emergent coordination and cloud infrastructure attacks.

## 具身智能

### [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](http://arxiv.org/abs/2610.20609v1)

- 作者：Shaoyuan Xie, Zihan Zhang, Jingxuan Wang, Jiashu Qu, Xiaoqing Liang 等 9 人
- 提交：2026-10-14 · 分类 cs.RO · arXiv:2610.20609v1

Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form natural-language instructions.

### [Modeling and Understanding Neural Weights of Humanoid Policies with Diffusion](http://arxiv.org/abs/2610.20606v1)

- 作者：Huixuan Cheng, Bike Zhang, Shankar Sastry, Koushil Sreenath
- 提交：2026-10-14 · 分类 cs.RO · arXiv:2610.20606v1

Recent advances in robot learning have driven rapid progress in humanoid control, enabling increasingly agile behaviors in the real world. However, humanoid control networks are typically obtained through conventional training procedures, while comparatively little attention has been given to directly modeling the dist…

### [Graph-Reweighted Behavior Cloning with Human Interventions for Precise Robotic Manipulation](http://arxiv.org/abs/2610.20504v1)

- 作者：Xiaoman Li, Zhiqiang Yang, Jiayu Hu, Jipeng Kong, Yang Zhang 等 9 人
- 提交：2026-10-14 · 分类 cs.RO · arXiv:2610.20504v1

Long-horizon precise manipulation produces mixed-quality data for post-training vision-language-action (VLA) models: even successful demonstrations and intervention-assisted rollouts may contain detours, hesitations, failed attempts, and imperfect recoveries.

### [AdaRSI: On-Demand Recursive Self-Improvement for Embodied Agents](http://arxiv.org/abs/2610.20474v1)

- 作者：Peidong Wang, Ying Chang, Zhiming Ma, Xiaocui Yang, Shi Feng 等 11 人
- 提交：2026-10-14 · 分类 cs.CL · arXiv:2610.20474v1

Pretrained vision-language-action models (VLAs) often fail midway through unseen long-horizon tasks. Recursive self-improvement (RSI) offers a remedy, but embodied RSI methods either refine the harness around a frozen executor and so cannot add a missing motion, or train the executor on persistent failures without aski…

### [Towards Agentic Robots: Model, Data, Environment, and Harness](http://arxiv.org/abs/2610.20442v1)

- 作者：Chonghan Qin, Dongming Wu, Kaituo Feng, Jiaxu Wang, Xinlei Yu 等 16 人
- 提交：2026-10-14 · 分类 cs.RO · arXiv:2610.20442v1

Foundation models are driving a paradigm shift in robotic intelligence, moving beyond low-level action prediction to goal-directed orchestration of data collection, model training, task planning, and real-world execution.

### [Human Demonstrations as Post-Training Data for Any Robot Body: Retargeting the Object, Not the Hand](http://arxiv.org/abs/2610.20351v1)

- 作者：Nagasrikanth Kallakuri
- 提交：2026-10-14 · 分类 cs.RO · arXiv:2610.20351v1

Human demonstrations are today used largely for pretraining vision-language-action models, with little ability to use the same data for target-embodiment or task-oriented training, which scalable deployment of robots in industrial and general environments depends on.

### [AutoRSR: Automated Real-to-Sim-to-Real Data Generation for Scalable Robot Learning](http://arxiv.org/abs/2610.20336v1)

- 作者：Jiawei Zhang, Chang Liu, Litao Deng, Tao Zhang, Qin Jin
- 提交：2026-10-14 · 分类 cs.RO · arXiv:2610.20336v1

Scaling embodied robot learning requires large and diverse manipulation datasets, but collecting real-world demonstrations remains expensive in human effort and robot time.

### [TacClaw-Infinity: A Large-Scale Vision-Tactile-Language-Action Dataset for Dexterous Manipulation](http://arxiv.org/abs/2610.20320v1)

- 作者：Fucai Zhu, Xidong Zhang, Yichi Zhang, Yipan Wang, Fubo Wang 等 26 人
- 提交：2026-10-14 · 分类 cs.RO · arXiv:2610.20320v1

Large-scale robot learning increasingly relies on diverse human demonstrations, yet tactile manipulation data remain difficult to scale, and existing multimodal datasets often lack consistent quality control and structured supervision.

### [Reflect After Failure: Brain-Inspired Self-Evolving Agents for Embodied Spatial Intelligence](http://arxiv.org/abs/2610.20312v1)

- 作者：Xin Li, Xiaohuan Gu, Yifan Wang, Shaobin Ling, Tianli Shi 等 9 人
- 提交：2026-10-14 · 分类 cs.AI · arXiv:2610.20312v1

Vision-Language Models (VLMs) have made substantial progress in spatial reasoning, and self-evolving agents further extend these capabilities to embodied environments by learning from interactions.

### [ObjDream: Guiding Vision-Language-Action Models with Object-Level Understanding and Future State Prediction](http://arxiv.org/abs/2610.20223v1)

- 作者：Huailiang Ma, Yuxuan Li, Ziyi Zhao, Xinkai Wang, Mingyu Li 等 10 人
- 提交：2026-10-14 · 分类 cs.RO · arXiv:2610.20223v1

Vision-language-action (VLA) models have emerged as a powerful paradigm for robotic manipulation, enabling robots to generate actions from visual observations and language instructions.

### [Tactile-Guided Robot Learning: From Representation Learning to Foundation Models](http://arxiv.org/abs/2610.20134v1)

- 作者：Kiyanoush Nazari, Luchen Li, Haoshu Fang, Nima Fazeli, Zhibin Li 等 7 人
- 提交：2026-10-14 · 分类 cs.RO · arXiv:2610.20134v1

Tactile sensing is becoming central to robust, adaptive, and dexterous robotic manipulation. Beyond its traditional role in contact detection and reactive control, touch is increasingly used to learn transferable representations, condition manipulation policies, and support embodied physical reasoning.

### [FoveaVLA: Foveation Actions Replace the Wrist Camera in VLAs](http://arxiv.org/abs/2610.20064v1)

- 作者：Bingao Chen, Lihan Zha, C. Karen Liu, Guy Tevet
- 提交：2026-10-14 · 分类 cs.RO · arXiv:2610.20064v1

We present FoveaVLA, a Vision-Language-Action (VLA) model that replaces the wrist camera with learned foveation actions. Wrist cameras provide close-up detail but restrict the view to the end-effector's surroundings.

---

本期共收录 33 篇。
