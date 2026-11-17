## Related Works

Vision Transformers (ViTs) have revolutionized computer vision by leveraging self-attention mechanisms to capture global contextual information, surpassing traditional convolutional neural networks (CNNs) in many tasks \[[2010.11929](http://arxiv.org/abs/2010.11929)\]. The original ViT architecture processes images as sequences of fixed-size patches, applying multiple Transformer layers for classification. While this design achieves strong accuracy, it entails high computational complexity and large memory footprint, which pose significant challenges for efficient hardware deployment, particularly on resource-constrained platforms such as FPGAs \[[2208.05163](http://arxiv.org/abs/2208.05163)\]\[[2201.06618](http://arxiv.org/abs/2201.06618)\].

### Hardware Acceleration Challenges and Approaches

One primary bottleneck in ViT hardware acceleration lies in the complex arithmetic operations intrinsic to the model—most notably Softmax and LayerNorm—which are highly sensitive to numerical precision and difficult to efficiently map onto hardware accelerators. Existing methods often focus on accelerating matrix multiplication operations on hardware while offloading these complex functions to CPUs, resulting in communication overhead and suboptimal system performance \[[2208.05163](http://arxiv.org/abs/2208.05163)\]\[[2201.06618](http://arxiv.org/abs/2201.06618)\].

Several FPGA-based ViT acceleration frameworks have been proposed to address these challenges. VAQF presents a fully automatic software-hardware co-design framework that incorporates low-bit quantization of ViTs and generates FPGA accelerators meeting target frame rates by adjusting activation precisions and hardware parameters \[[2201.06618](http://arxiv.org/abs/2201.06618)\]. Similarly, Auto-ViT-Acc uses mixed-scheme quantization for FPGA acceleration, achieving significant frame rate improvements with minimal accuracy loss compared to 32-bit floating-point baselines \[[2208.05163](http://arxiv.org/abs/2208.05163)\]. ME-ViT introduces a memory-efficient FPGA accelerator featuring a single-load policy to minimize off-chip memory access, thereby improving throughput and power efficiency substantially \[[2402.09709](http://arxiv.org/abs/2402.09709)\]. These works underscore the importance of quantization and memory optimization in ViT hardware acceleration.

### Quantization Techniques for ViTs

Quantization has emerged as a key technique to reduce computational and memory demands for ViTs. Low-bit quantization compresses model parameters and enables bitwise operations but often induces accuracy degradation due to information distortion, particularly within self-attention maps. The Q-ViT framework addresses this by employing an information rectification module and distribution-guided distillation to eliminate quantization-induced distortions, resulting in fully quantized ViTs that match or surpass full-precision accuracy on ImageNet \[[2210.06707](http://arxiv.org/abs/2210.06707)\]. PackQViT further advances quantization by proposing a sub-8-bit quantization-aware training framework optimized for mobile CPUs, employing integer-only computation and packed multipliers to achieve real-time acceleration with improved accuracy over prior 8-bit approaches \[[https://www.semanticscholar.org/paper/5fd1b67482e4b9fe70b480c0fd0467900d6db436](https://www.semanticscholar.org/paper/5fd1b67482e4b9fe70b480c0fd0467900d6db436)\]. These methods demonstrate the viability of aggressive low-precision quantization for ViTs without substantial accuracy sacrifices.

### Model Compression and Pruning

Besides quantization, model compression through pruning and token selection has been explored to reduce ViT complexity. Sparse training methods dynamically extract and train sparse subnetworks within ViTs, optimizing both data and architecture sparsity to reduce FLOPs and inference time with minor or even positive effects on accuracy \[[2106.04533](http://arxiv.org/abs/2106.04533)\]. Token pruning approaches such as Evo-ViT and Patch Slimming identify and remove less informative tokens dynamically during inference, preserving spatial structure and enabling significant throughput improvements while maintaining accuracy \[[2108.01390](http://arxiv.org/abs/2108.01390)\]\[[2106.02852](http://arxiv.org/abs/2106.02852)\]. Soft token pruning frameworks like SPViT further introduce latency-aware soft pruning mechanisms with token selectors and package tokens to balance accuracy and computational cost on edge devices \[[2112.13890](http://arxiv.org/abs/2112.13890)\]. These pruning techniques reduce the quadratic complexity of self-attention and improve hardware efficiency.

### Architectural Enhancements for Efficiency

Architectural innovations also aim to improve ViT efficiency. CvT integrates convolutions into the Transformer architecture, combining CNN-like inductive biases with Transformer global context modeling, yielding better accuracy with fewer parameters and FLOPs \[[2103.15808](http://arxiv.org/abs/2103.15808)\]. Similarly, LeViT designs hybrid architectures blending convolutional and Transformer components to optimize speed-accuracy trade-offs on various hardware platforms \[[2104.01136](http://arxiv.org/abs/2104.01136)\]. Tokens-to-Token ViT (T2T-ViT) incorporates progressive token aggregation to better capture local structures and reduce token length, improving training efficiency and accuracy compared to vanilla ViTs \[[2101.11986](http://arxiv.org/abs/2101.11986)\]. CrossViT employs multi-scale token branches fused via cross-attention to strengthen feature representations with moderate computational overhead \[[2103.14899](http://arxiv.org/abs/2103.14899)\]. These architectural modifications are complementary to hardware and quantization optimizations.

### Comprehensive ViT Compression and Hardware-Aware Design

Unified frameworks combining pruning, layer skipping, and knowledge distillation have been proposed to compress ViTs holistically, achieving substantial FLOPs reduction with minimal accuracy loss \[[2203.08243](http://arxiv.org/abs/2203.08243)\]. Surveys on efficient ViTs categorize key strategies into compact architectures, pruning, knowledge distillation, and quantization, analyzing trade-offs among accuracy, computational cost, and hardware resource constraints \[[2309.02031](http://arxiv.org/abs/2309.02031)\]. Hardware-aware design methodologies increasingly consider FPGA-specific limitations such as memory bandwidth and compute-to-communication ratios to optimize throughput and power efficiency \[[2402.09709](http://arxiv.org/abs/2402.09709)\].

### Summary

Despite significant progress, existing ViT acceleration methods typically either accelerate only partial operations (e.g., matrix multiplications) on hardware or rely on high-precision arithmetic for complex functions like Softmax and LayerNorm, leading to inefficiencies. The proposed approach of mapping all ViT operations, including Softmax and LayerNorm, onto FPGA hardware using a novel Microscaling Integer (MXInt) format addresses this limitation by enabling low-precision, hardware-friendly implementations of these challenging operations. This represents a novel advancement beyond current frameworks that primarily combine quantization and pruning with partial hardware acceleration.

---

### References

\[[2010.11929](http://arxiv.org/abs/2010.11929)\] http://arxiv.org/abs/2010.11929  
\[[2208.05163](http://arxiv.org/abs/2208.05163)\] http://arxiv.org/abs/2208.05163  
\[[2201.06618](http://arxiv.org/abs/2201.06618)\] http://arxiv.org/abs/2201.06618  
\[[2210.06707](http://arxiv.org/abs/2210.06707)\] http://arxiv.org/abs/2210.06707  
\[[2402.09709](http://arxiv.org/abs/2402.09709)\] http://arxiv.org/abs/2402.09709  
\[[2108.01390](http://arxiv.org/abs/2108.01390)\] http://arxiv.org/abs/2108.01390  
\[[2104.01136](http://arxiv.org/abs/2104.01136)\] http://arxiv.org/abs/2104.01136  
\[[2103.15808](http://arxiv.org/abs/2103.15808)\] http://arxiv.org/abs/2103.15808  
\[[2106.04533](http://arxiv.org/abs/2106.04533)\] http://arxiv.org/abs/2106.04533  
\[[2101.11986](http://arxiv.org/abs/2101.11986)\] http://arxiv.org/abs/2101.11986  
\[[2103.14899](http://arxiv.org/abs/2103.14899)\] http://arxiv.org/abs/2103.14899  
\[[2203.08243](http://arxiv.org/abs/2203.08243)\] http://arxiv.org/abs/2203.08243  
\[[2106.02852](http://arxiv.org/abs/2106.02852)\] http://arxiv.org/abs/2106.02852  
\[[2309.02031](http://arxiv.org/abs/2309.02031)\] http://arxiv.org/abs/2309.02031  
\[[2112.13890](http://arxiv.org/abs/2112.13890)\] http://arxiv.org/abs/2112.13890  
\[[https://www.semanticscholar.org/paper/5fd1b67482e4b9fe70b480c0fd0467900d6db436](https://www.semanticscholar.org/paper/5fd1b67482e4b9fe70b480c0fd0467900d6db436)\] https://www.semanticscholar.org/paper/5fd1b67482e4b9fe70b480c0fd0467900d6db436