## Related Works

Deploying large language models (LLMs) on edge devices presents significant challenges due to their massive computational, memory, and energy demands, which often exceed the constraints of off-the-shelf edge hardware \[[https://www.semanticscholar.org/paper/ec93fc7ec82c65a7bf7213488327d391014539ed](https://www.semanticscholar.org/paper/ec93fc7ec82c65a7bf7213488327d391014539ed)\]. The limited storage, weight, and power of these devices necessitate a careful balance among latency, energy consumption, and model accuracy. To address these limitations, prior research has focused on three main areas: model compression, hardware acceleration, and system-level optimization.

### Model Compression and Quantization

Model compression techniques, including pruning, quantization, and sparsity exploitation, have been extensively studied to reduce the size and computational complexity of LLMs for edge deployment. Activation-aware quantization methods, such as Activation-aware Weight Quantization (AWQ), achieve significant model size reduction (up to 4×) and inference acceleration (3–4×) by selectively preserving salient weights based on activation distributions while maintaining performance \[[2306.00978](http://arxiv.org/abs/2306.00978)\]. Activation sparsity techniques further reduce memory and compute costs by enforcing zero thresholds on intermediate activations, achieving approximately 50% reduction in Feed-Forward Network (FFN) components without notable accuracy loss \[[2412.12178](http://arxiv.org/abs/2412.12178)\]. These methods are complementary and can be combined to maximize compression efficiency.

Mixture-of-Experts (MoE) LLMs introduce expert-level sparsification approaches to reduce memory overhead and inference latency. Techniques like Mixture Compressor (MC) employ adaptive bit-width quantization and dynamic pruning of activated experts, compressing over 76% of the model with minimal accuracy degradation, and reducing activated parameters during inference \[[2410.06270](http://arxiv.org/abs/2410.06270)\]. Similarly, expert pruning and skipping strategies have been proposed as plug-and-play methods to improve MoE deployment efficiency while preserving task performance \[[2402.14800](http://arxiv.org/abs/2402.14800)\]. These approaches highlight the importance of granularity-aware compression for scalable LLM deployment on resource-limited devices.

### Hardware Acceleration for Edge LLM Inference

FPGA-based accelerators have emerged as a promising solution for LLM inference on edge devices due to their reconfigurability and energy efficiency. Co-design methodologies that simultaneously optimize DNN models and FPGA hardware have demonstrated improvements in latency, power consumption, and energy efficiency compared to traditional CPU or GPU implementations \[[1904.04421](http://arxiv.org/abs/1904.04421)\]. For example, SECDA-LLM, an FPGA accelerator design platform, enables block floating-point quantized matrix multiplication tailored for LLMs, achieving an 11× latency reduction over ARM CPU baselines on edge boards \[[2408.00462](http://arxiv.org/abs/2408.00462)\]. Furthermore, algorithm-hardware co-design frameworks such as AccLLM integrate pruning, novel attention mechanisms, and mixed-precision quantization with dedicated FPGA accelerators, resulting in up to 4× energy efficiency gains and 3× throughput improvements for long-context LLM inference \[[2505.03745](http://arxiv.org/abs/2505.03745)\].

Surveys of hardware accelerators for LLMs emphasize the diversity of platforms—GPUs, FPGAs, ASICs, and Processing-in-Memory (PIM) architectures—each offering trade-offs in performance and energy efficiency \[[2410.04466](http://arxiv.org/abs/2410.04466)\]\[[2401.09890](http://arxiv.org/abs/2401.09890)\]. Comparative studies using normalized process technologies allow fair benchmarking of acceleration frameworks, revealing that hardware-aware design choices critically influence throughput and power consumption \[[2409.03384](http://arxiv.org/abs/2409.03384)\]\[[2310.04607](http://arxiv.org/abs/2310.04607)\]. These insights inform the design of scalable and energy-efficient hardware tailored for edge-oriented LLM inference.

### System-Level Optimizations and Memory Management

Beyond model and hardware optimizations, system-level techniques focus on efficient memory management and scheduling to address the dynamic and large key-value (KV) cache requirements of autoregressive LLM inference. PagedAttention, inspired by virtual memory paging, significantly reduces KV cache fragmentation and duplication, enabling 2–4× throughput improvements on popular LLMs while maintaining latency targets \[[2309.06180](http://arxiv.org/abs/2309.06180)\]. KV cache management strategies at token-, model-, and system-levels have been surveyed comprehensively, illustrating how quantization, merging, and scheduling optimizations collectively enhance memory utilization and inference speed \[[2412.19442](http://arxiv.org/abs/2412.19442)\].

Other system-level approaches include the use of flash memory to extend effective DRAM capacity through context-adaptive loading and sparsity-aware data movement, facilitating the execution of models up to twice the DRAM size with substantial speedups over naive loading methods on CPUs and GPUs \[[2312.11514](http://arxiv.org/abs/2312.11514)\]. These hardware-informed memory management techniques are critical for deploying large models on edge devices with limited volatile memory.

### Edge-Specific Challenges and Optimization Frameworks

Deploying LLMs at the edge also involves overcoming device heterogeneity and variability in hardware capabilities. Hardware-aware neural architecture search (NAS) frameworks, such as SCAN-Edge, jointly optimize self-attention, convolution, and activation modules to discover hybrid networks that meet latency and efficiency targets across diverse edge platforms including CPUs, GPUs, and accelerators \[[2408.15395](http://arxiv.org/abs/2408.15395)\]. Similarly, resource management frameworks at the edge emphasize the need for provisioning, auto-scaling, and efficient resource sharing to improve quality of service and reduce cloud reliance \[[1801.05610](http://arxiv.org/abs/1801.05610)\]\[[1709.04061](http://arxiv.org/abs/1709.04061)\].

Comprehensive surveys on GenAI and LLM deployment at the edge highlight three pillars for optimization: software-level model compression and pruning, hardware acceleration with reconfigurable platforms, and integrated frameworks for system-level resource management \[[2502.15816](http://arxiv.org/abs/2502.15816)\]. These works identify the criticality of co-design approaches that jointly address algorithmic efficiency and hardware constraints to meet real-time, energy, and privacy demands.

### Summary

The body of work on LLM deployment at the edge converges on the necessity of combined algorithm-hardware co-design strategies. Model compression via quantization, sparsity, and expert pruning reduces computational burden while preserving accuracy. FPGA and custom accelerators provide energy-efficient inference tailored to LLM workloads. Finally, system-level memory and resource management techniques enable scalable, low-latency execution on constrained devices. This multi-level optimization approach underpins recent advances such as CLONE, which integrates real-time energy optimization and hardware specialization to achieve significant acceleration and energy savings on edge platforms.

---

References:  
\[[https://www.semanticscholar.org/paper/ec93fc7ec82c65a7bf7213488327d391014539ed](https://www.semanticscholar.org/paper/ec93fc7ec82c65a7bf7213488327d391014539ed)\]  
\[[2409.03384](http://arxiv.org/abs/2409.03384)\]  
\[[2505.03745](http://arxiv.org/abs/2505.03745)\]  
\[[2306.00978](http://arxiv.org/abs/2306.00978)\]  
\[[2408.00462](http://arxiv.org/abs/2408.00462)\]  
\[[2412.19442](http://arxiv.org/abs/2412.19442)\]  
\[[2309.06180](http://arxiv.org/abs/2309.06180)\]  
\[[2408.15395](http://arxiv.org/abs/2408.15395)\]  
\[[2412.12178](http://arxiv.org/abs/2412.12178)\]  
\[[2312.11514](http://arxiv.org/abs/2312.11514)\]  
\[[1904.04421](http://arxiv.org/abs/1904.04421)\]  
\[[2410.04466](http://arxiv.org/abs/2410.04466)\]  
\[[2401.09890](http://arxiv.org/abs/2401.09890)\]  
\[[2310.04607](http://arxiv.org/abs/2310.04607)\]  
\[[2502.15816](http://arxiv.org/abs/2502.15816)\]  
\[[1801.05610](http://arxiv.org/abs/1801.05610)\]  
\[[1709.04061](http://arxiv.org/abs/1709.04061)\]  
\[[2410.06270](http://arxiv.org/abs/2410.06270)\]  
\[[2402.14800](http://arxiv.org/abs/2402.14800)\]