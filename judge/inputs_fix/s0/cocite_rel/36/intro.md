## Related Works

Deploying large language models (LLMs) on edge devices presents significant challenges due to the limited storage, computational power, and energy resources available \[[14](https://www.semanticscholar.org/paper/ec93fc7ec82c65a7bf7213488327d391014539ed)\]. Prior work has explored various techniques to address these limitations, including model compression, efficient inference, and hardware acceleration. For instance, \[[15](http://arxiv.org/abs/2306.00978)\] introduced AWQ, an activation-aware weight quantization method that enables on-device LLM deployment by reducing model size while preserving performance. This approach has been shown to achieve up to 4x model size reduction and 3–4x acceleration across various edge platforms. Similarly, \[[21](http://arxiv.org/abs/2211.10438)\] proposed SmoothQuant, a post-training quantization method that enables 8-bit weight and activation quantization for LLMs, achieving up to 1.56x speedup and 2x memory reduction with negligible accuracy loss. These methods highlight the importance of quantization in enabling efficient LLM deployment on resource-constrained devices.

Hardware acceleration has also been a focal point for improving LLM inference on edge devices. \[[16](http://arxiv.org/abs/2409.11424)\] presented LlamaF, an FPGA-based accelerator designed to improve LLM inference performance on embedded FPGAs. The design employs post-training quantization to reduce model size and optimize for off-chip memory bandwidth, achieving a 14.3–15.8x speedup and 6.1x power efficiency improvement over running exclusively on the embedded processing system. Similarly, \[[20](http://arxiv.org/abs/2303.07470)\] introduced X-Former, a hybrid in-memory hardware accelerator that combines nonvolatile memory (NVM) and CMOS processing elements to efficiently execute transformer workloads. X-Former demonstrated up to 69.8x and 13x improvements in latency and energy over a NVIDIA GeForce GTX 1060 GPU, highlighting the potential of in-memory computing for LLM acceleration.

Efficient memory management is another critical aspect of deploying LLMs on edge devices. \[[1](http://arxiv.org/abs/2309.06180)\] proposed PagedAttention, an attention algorithm inspired by virtual memory and paging techniques, which enables near-zero waste in key-value cache memory and flexible sharing within and across requests. This approach significantly improves the throughput of large language models. Additionally, \[[17](http://arxiv.org/abs/2309.17453)\] introduced StreamingLLM, an efficient framework that enables LLMs trained with a finite length attention window to generalize to infinite sequence lengths without fine-tuning. This is particularly important for streaming applications such as multi-round dialogue, where long interactions are expected.

Several studies have also focused on reducing the computational and memory requirements of LLMs through sparsity and pruning techniques. \[[5](http://arxiv.org/abs/2310.17157)\] proposed DejaVu, a system that leverages contextual sparsity to speed up LLM inference without compromising model quality. DejaVu can reduce the inference latency of OPT-175B by over 2x compared to state-of-the-art systems. Similarly, \[[8](https://www.semanticscholar.org/paper/d6eeb0ca9e2f34f2427866aa864d364ec78e6049)\] investigated column balanced block pruning on Transformer models and demonstrated significant improvements in inference latency and energy efficiency on FPGAs.

In summary, the field of deploying LLMs on edge devices has seen significant advancements through model compression, efficient inference, and hardware acceleration techniques. These approaches collectively address the challenges of limited storage, computational power, and energy resources, paving the way for more efficient and practical LLM deployment on edge devices.

References  
\[[1](http://arxiv.org/abs/2309.06180)\] Efficient Memory Management for Large Language Model Serving with PagedAttention  
\[[2](http://arxiv.org/abs/2312.11514)\] LLM in a flash: Efficient Large Language Model Inference with Limited Memory  
\[[3](https://www.semanticscholar.org/paper/5af69480a7ae3b571df6782a11ec4437b386a7d9)\] ELSA: Hardware-Software Co-design for Efficient, Lightweight Self-Attention Mechanism in Neural Networks  
\[[4](http://arxiv.org/abs/2310.04607)\] A Comprehensive Performance Study of Large Language Models on Novel AI Accelerators  
\[[5](http://arxiv.org/abs/2310.17157)\] Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time  
\[[6](http://arxiv.org/abs/2104.06535)\] NPE: An FPGA-based Overlay Processor for Natural Language Processing  
\[[7](http://arxiv.org/abs/2307.08691)\] FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning  
\[[8](https://www.semanticscholar.org/paper/d6eeb0ca9e2f34f2427866aa864d364ec78e6049)\] Accelerating Transformer-based Deep Learning Models on FPGAs using Column Balanced Block Pruning  
\[[9](http://arxiv.org/abs/2110.09310)\] Energon: Toward Efficient Acceleration of Transformers Using Dynamic Sparse Attention  
\[[10](http://arxiv.org/abs/2007.08563)\] FTRANS: energy-efficient acceleration of transformers using FPGA  
\[[11](http://arxiv.org/abs/2307.09288)\] Llama 2: Open Foundation and Fine-Tuned Chat Models  
\[[12](http://arxiv.org/abs/2209.10797)\] DFX: A Low-latency Multi-FPGA Appliance for Accelerating Transformer-based Text Generation  
\[[13](https://www.semanticscholar.org/paper/827b0b03f54ba43596193e5d47f1ff13b3afe293)\] H3D-Transformer: A Heterogeneous 3D (H3D) Computing Platform for Transformer Model Acceleration on Edge Devices  
\[[14](https://www.semanticscholar.org/paper/ec93fc7ec82c65a7bf7213488327d391014539ed)\] An Empirical Analysis and Resource Footprint Study of Deploying Large Language Models on Edge Devices  
\[[15](http://arxiv.org/abs/2306.00978)\] AWQ: Activation-aware Weight Quantization for On-Device LLM Compression and Acceleration  
\[[16](http://arxiv.org/abs/2409.11424)\] LlamaF: An Efficient Llama2 Architecture Accelerator on Embedded FPGAs  
\[[17](http://arxiv.org/abs/2309.17453)\] Efficient Streaming Language Models with Attention Sinks  
\[[18](https://www.semanticscholar.org/paper/1107363fc2acf13f5bf5168af5f9042a07bd0a8e)\] Hardware-friendly compression and hardware acceleration for transformer: A survey  
\[[19](http://arxiv.org/abs/2401.09890)\] A Survey on Hardware Accelerators for Large Language Models  
\[[20](http://arxiv.org/abs/2303.07470)\] X-Former: In-Memory Acceleration of Transformers  
\[[21](http://arxiv.org/abs/2211.10438)\] SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models  
\[[22](http://arxiv.org/abs/2308.13137)\] OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models  
\[[23](http://arxiv.org/abs/2009.08605)\] Hardware Accelerator for Multi-Head Attention and Position-Wise Feed-Forward in the Transformer
