## Related Works

Deploying Large Language Models (LLMs) on edge devices presents significant challenges due to limited computational resources, storage capacity, and power constraints inherent to these platforms. To address these issues, extensive research has focused on model compression, quantization, hardware acceleration, and co-design methodologies that jointly optimize algorithms and hardware for efficient edge inference.

### Model Compression and Quantization

Model compression techniques such as pruning, quantization, and sparsity exploitation are crucial to reduce the footprint and computational demands of LLMs on edge devices. Activation sparsity methods targeting the Feed-Forward Network (FFN) components have demonstrated up to 50% reductions in memory and compute with minimal accuracy loss by enforcing zero-valued activations, an approach orthogonal to traditional pruning or quantization \[[2412.12178v2](http://arxiv.org/abs/2412.12178v2)\]. Mixture-of-Experts (MoE) models also benefit from expert-level pruning and skipping strategies, which reduce model size and inference latency without degrading performance, enabling more efficient MoE deployment \[[2402.14800v2](http://arxiv.org/abs/2402.14800v2)\]. Additionally, mixed-precision quantization methods like AMED optimize bitwidth allocations dynamically during training to balance accuracy and hardware efficiency, adapting specifically to target edge device architectures \[[2205.15437v2](http://arxiv.org/abs/2205.15437v2)\]. Recent advances in quantizing weights and key-value caches (WKVQuant) further improve memory savings and speed in autoregressive LLM inference, critical for constrained hardware \[[2402.12065v2](http://arxiv.org/abs/2402.12065v2)\]. These compression strategies collectively help mitigate the model size and computation bottlenecks on edge devices.

### Hardware Acceleration and Co-Design

Hardware acceleration plays a pivotal role in enabling efficient LLM inference on edge platforms. FPGA-based accelerators are particularly promising due to their reconfigurability and favorable performance-per-watt characteristics compared to CPUs or GPUs \[[2110.00478v1](http://arxiv.org/abs/2110.00478v1)\]\[[2408.00462v1](http://arxiv.org/abs/2408.00462v1)\]. The SECDA framework exemplifies this by combining hardware/software co-design to reduce development overhead and streamline FPGA accelerator design for DNNs, achieving up to 3.5× speedup and nearly 3× energy reduction compared to CPU inference \[[2110.00478v1](http://arxiv.org/abs/2110.00478v1)\]. Extending SECDA to LLM-specific workloads, SECDA-LLM integrates model-specific optimizations such as block floating-point quantization, delivering up to 11× latency reduction on edge FPGA boards \[[2408.00462v1](http://arxiv.org/abs/2408.00462v1)\]. Similarly, AccLLM proposes an algorithm-hardware co-design approach combining pruning, novel attention mechanisms, and ultra-low-bit quantization (W2A8KV4) with FPGA accelerator architectures to achieve nearly 3× throughput and 4× energy efficiency improvements over prior art \[[2505.03745v1](http://arxiv.org/abs/2505.03745v1)\].

Beyond FPGAs, emerging resistive memory (ReRAM)-based in-memory computing architectures offer prospects for area- and power-efficient neural acceleration, potentially benefiting large-scale LLM inference at the edge \[[2109.03934v1](http://arxiv.org/abs/2109.03934v1)\]. Neuromorphic hardware architectures inspired by self-organizing neural systems also present an alternative paradigm for low-power adaptive computation, though their application to LLMs remains exploratory \[[1810.12640v1](http://arxiv.org/abs/1810.12640v1)\].

### Edge-Optimized Frameworks and Algorithmic Innovations

To further enhance LLM deployment on edge devices, frameworks and algorithmic techniques have been developed to balance latency, energy, and accuracy. Hardware-aware neural architecture search (NAS) frameworks like SCAN-Edge optimize hybrid network architectures including self-attention, convolution, and activation functions across diverse edge hardware types, ensuring consistent low latency across CPUs, GPUs, and accelerators \[[2408.15395v1](http://arxiv.org/abs/2408.15395v1)\]. Activation sparsity optimizations enable selective weight prefetching and cache management, reducing memory bandwidth and execution time for critical LLM components on constrained hardware \[[2412.12178v2](http://arxiv.org/abs/2412.12178v2)\].

Algorithmically, long-context LLM inference is improved through co-design of pruning, attention mechanisms, and quantization schemes that reduce memory and bandwidth demand, facilitating scalable deployment on FPGA accelerators \[[2505.03745v1](http://arxiv.org/abs/2505.03745v1)\]. Automatic mixed-precision quantization frameworks treat bitwidth allocation as a Markov Decision Process, optimizing precision based on direct hardware feedback to maximize efficiency on edge devices \[[2205.15437v2](http://arxiv.org/abs/2205.15437v2)\]. These algorithm-hardware synergy approaches are vital to overcoming the resource limitations of off-the-shelf edge platforms.

### Security, Privacy, and Robustness Considerations

Deploying LLMs at the edge also involves addressing security and privacy challenges. Efficient hardware accelerators paired with software optimizations can enable local inference, minimizing data transfer to cloud servers and reducing privacy risks \[[2502.15816v1](http://arxiv.org/abs/2502.15816v1)\]. However, LLM alignment vulnerabilities pose risks of adversarial exploitation, which necessitates robust model alignment and secure inference practices even on constrained edge hardware \[[2309.01446v4](http://arxiv.org/abs/2309.01446v4)\]. Additionally, model compression techniques must be evaluated for their impact on subgroup robustness to ensure equitable performance across diverse data subsets \[[2403.17811v1](http://arxiv.org/abs/2403.17811v1)\].

### Summary

The current state of research underscores the necessity of integrating model compression, quantization, and hardware acceleration through co-design methodologies tailored to edge device constraints. FPGA-based accelerators, complemented by algorithmic innovations such as activation sparsity, mixed-precision quantization, and expert pruning, constitute the backbone of efficient LLM deployment strategies. Emerging paradigms like ReRAM-based in-memory computing and neuromorphic architectures hold future promise for further gains in edge AI efficiency. Together, these advances provide a comprehensive foundation for addressing the multifaceted challenges of executing large-scale LLMs on resource-constrained edge platforms.

---

References:

\[[2409.03384v1](http://arxiv.org/abs/2409.03384v1)\] Hardware Acceleration of LLMs: A comprehensive survey and comparison (arXiv:2409.03384v1)  
\[[2110.00478v1](http://arxiv.org/abs/2110.00478v1)\] SECDA: Efficient Hardware/Software Co-Design of FPGA-based DNN Accelerators for Edge Inference (arXiv:2110.00478v1)  
\[[2408.00462v1](http://arxiv.org/abs/2408.00462v1)\] Designing Efficient LLM Accelerators for Edge Devices (arXiv:2408.00462v1)  
\[[2412.12178v2](http://arxiv.org/abs/2412.12178v2)\] Activation Sparsity Opportunities for Compressing General Large Language Models (arXiv:2412.12178v2)  
\[[2205.15437v2](http://arxiv.org/abs/2205.15437v2)\] AMED: Automatic Mixed-Precision Quantization for Edge Devices (arXiv:2205.15437v2)  
\[[2505.03745v1](http://arxiv.org/abs/2505.03745v1)\] AccLLM: Accelerating Long-Context LLM Inference Via Algorithm-Hardware Co-Design (arXiv:2505.03745v1)  
\[[2109.03934v1](http://arxiv.org/abs/2109.03934v1)\] Resistive Neural Hardware Accelerators (arXiv:2109.03934v1)  
\[[2502.15816v1](http://arxiv.org/abs/2502.15816v1)\] GenAI at the Edge: Comprehensive Survey on Empowering Edge Devices (arXiv:2502.15816v1)  
\[[2408.15395v1](http://arxiv.org/abs/2408.15395v1)\] SCAN-Edge: Finding MobileNet-speed Hybrid Networks for Diverse Edge Devices via Hardware-Aware Evolutionary Search (arXiv:2408.15395v1)  
\[[2402.12065v2](http://arxiv.org/abs/2402.12065v2)\] WKVQuant: Quantizing Weight and Key/Value Cache for Large Language Models Gains More (arXiv:2402.12065v2)  
\[[2402.14800v2](http://arxiv.org/abs/2402.14800v2)\] Not All Experts are Equal: Efficient Expert Pruning and Skipping for Mixture-of-Experts Large Language Models (arXiv:2402.14800v2)  
\[[2403.17811v1](http://arxiv.org/abs/2403.17811v1)\] Are Compressed Language Models Less Subgroup Robust? (arXiv:2403.17811v1)  
\[[1810.12640v1](http://arxiv.org/abs/1810.12640v1)\] Neuromorphic hardware as a self-organizing computing system (arXiv:1810.12640v1)  
\[[2309.01446v4](http://arxiv.org/abs/2309.01446v4)\] Open Sesame! Universal Black Box Jailbreaking of Large Language Models (arXiv:2309.01446v4)