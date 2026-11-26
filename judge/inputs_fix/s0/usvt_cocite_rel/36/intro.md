## Related Works

Deploying large language models (LLMs) on edge devices presents significant challenges due to limited storage, power, and computational resources \[[1](http://arxiv.org/abs/2309.06180)\]. Prior work has focused on reducing memory usage, improving inference speed, and enabling efficient execution on resource-constrained hardware. For instance, PagedAttention and vLLM address memory fragmentation and improve throughput by efficiently managing the key-value cache \[[1](http://arxiv.org/abs/2309.06180)\]. Similarly, AWQ introduces activation-aware weight quantization, enabling on-device deployment with up to 4x model size reduction and 3-4x acceleration \[[2](http://arxiv.org/abs/2306.00978)\]. These methods aim to reduce memory and computational demands, making LLMs more feasible for edge deployment.

Efforts to optimize attention mechanisms have also been crucial. ELSA proposes a hardware-software co-design solution that reduces the runtime and energy spent on self-attention by filtering out less relevant relations \[[3](https://www.semanticscholar.org/paper/5af69480a7ae3b571df6782a11ec4437b386a7d9)\]. FlashAttention-2 further improves attention efficiency by optimizing work partitioning and parallelism, achieving up to 2× speedup over its predecessor \[[10](http://arxiv.org/abs/2307.08691)\]. These techniques are essential for enabling efficient inference on devices with limited resources.

Quantization techniques such as SmoothQuant and OmniQuant have been developed to reduce memory and computational requirements while preserving accuracy \[[4](http://arxiv.org/abs/2211.10438)\]\[[11](http://arxiv.org/abs/2308.13137)\]. SmoothQuant enables 8-bit weight and activation quantization without accuracy loss, while OmniQuant introduces learnable components to optimize quantization parameters for diverse settings \[[11](http://arxiv.org/abs/2308.13137)\]. These methods are particularly relevant for edge deployment, where memory and power constraints are stringent.

Hardware accelerators have also played a critical role in enabling efficient LLM inference. DFX, a multi-FPGA appliance, achieves significant speedup and energy efficiency for transformer-based text generation \[[8](http://arxiv.org/abs/2209.10797)\]. Similarly, FTRANS leverages FPGA-based acceleration to reduce model size and improve performance, achieving up to 16× reduction in model size \[[16](http://arxiv.org/abs/2007.08563)\]. These hardware solutions complement software optimizations by providing dedicated hardware for LLM inference.

Inference with reference, as proposed by LLMA, further reduces computation by leveraging identical text spans between the decoding result and the reference \[[12](http://arxiv.org/abs/2304.04487)\]. This method enables lossless acceleration, achieving over 2× speedup in scenarios with significant overlap between reference and output. Similarly, Wanda introduces a pruning method that reduces model size without retraining, achieving competitive performance compared to magnitude pruning \[[18](http://arxiv.org/abs/2306.11695)\].

Overall, these works highlight the importance of combining algorithmic optimizations with hardware acceleration to enable efficient LLM deployment on edge devices. They provide a foundation for further research into scalable, energy-efficient, and accurate inference methods for LLMs in resource-constrained environments.

References  
\[[1](http://arxiv.org/abs/2309.06180)\] Efficient Memory Management for Large Language Model Serving with PagedAttention  
\[[2](http://arxiv.org/abs/2306.00978)\] AWQ: Activation-aware Weight Quantization for On-Device LLM Compression and Acceleration  
\[[3](https://www.semanticscholar.org/paper/5af69480a7ae3b571df6782a11ec4437b386a7d9)\] ELSA: Hardware-Software Co-design for Efficient, Lightweight Self-Attention Mechanism in Neural Networks  
\[[4](http://arxiv.org/abs/2211.10438)\] SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models  
\[[8](http://arxiv.org/abs/2209.10797)\] DFX: A Low-latency Multi-FPGA Appliance for Accelerating Transformer-based Text Generation  
\[[10](http://arxiv.org/abs/2307.08691)\] FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning  
\[[11](http://arxiv.org/abs/2308.13137)\] OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models  
\[[12](http://arxiv.org/abs/2304.04487)\] Inference with Reference: Lossless Acceleration of Large Language Models  
\[[16](http://arxiv.org/abs/2007.08563)\] FTRANS: energy-efficient acceleration of transformers using FPGA  
\[[18](http://arxiv.org/abs/2306.11695)\] A Simple and Effective Pruning Approach for Large Language Models
