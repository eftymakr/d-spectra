## Related Works

Vision Transformers (ViTs) have gained significant attention for their ability to capture global context through self-attention mechanisms, leading to strong performance in computer vision tasks \[[15](http://arxiv.org/abs/2205.11397)\]. However, the high computational complexity and memory demands of ViTs pose challenges for efficient hardware acceleration, especially on resource-constrained devices \[[18](http://arxiv.org/abs/2503.02891)\]. Existing approaches often rely on CPU-based execution for complex operations like Softmax and LayerNorm, which are sensitive to model accuracy and difficult to map onto low-precision hardware \[[1](https://www.semanticscholar.org/paper/0ade4d722e48379761d17cf1efc05200315c27d9)\]. This results in suboptimal performance due to communication overhead between the CPU and accelerator \[[1](https://www.semanticscholar.org/paper/0ade4d722e48379761d17cf1efc05200315c27d9)\].

Several works have explored hardware acceleration for ViTs. HDViT proposes a heterogeneous FPGA accelerator that addresses the mismatch between operators and hardware architectures, achieving significant performance improvements \[[1](https://www.semanticscholar.org/paper/0ade4d722e48379761d17cf1efc05200315c27d9)\]. Auto-ViT-Acc introduces an FPGA-aware automatic acceleration framework with mixed-scheme quantization, achieving up to 5.6x speedup on frame rate with minimal accuracy drop \[[2](http://arxiv.org/abs/2208.05163)\]. HeatViT focuses on hardware-efficient token pruning, reducing computation and memory usage while maintaining accuracy \[[3](http://arxiv.org/abs/2211.08110)\]. ME-ViT introduces a memory-efficient design to minimize off-chip memory access, achieving substantial improvements in memory bandwidth and throughput \[[5](http://arxiv.org/abs/2402.09709)\]. ReViT leverages visual semantics to accelerate ViT execution, achieving speedup and energy efficiency improvements \[[6](https://www.semanticscholar.org/paper/f47b726ad00e1a93adc5b3e266c71d75bb05e1ff)\]. EfficientViT, a hybrid convolution-transformer architecture, has also been targeted for hardware acceleration \[[7](http://arxiv.org/abs/2403.20230)\].

Quantization techniques have been widely explored to reduce the computational and memory demands of ViTs. Q-ViT introduces a fully quantized ViT with an information rectification module to mitigate performance degradation \[[10](http://arxiv.org/abs/2210.06707)\]. Trio-ViT focuses on post-training quantization for softmax-free efficient ViTs, achieving significant speedup and DSP efficiency improvements \[[9](http://arxiv.org/abs/2405.03882)\]. BSViT employs dynamic patch and weight bit-group quantization, enhancing energy efficiency and performance \[[16](https://www.semanticscholar.org/paper/b2e51759f910101691039846bec4401a85b53309)\]. These methods highlight the importance of algorithm-hardware co-design for efficient ViT acceleration \[[18](http://arxiv.org/abs/2503.02891)\].

Recent works have also focused on reducing computational complexity through pruning and token reorganization. EViT reorganizes image tokens during inference, reducing redundant computations and improving inference speed with minimal accuracy loss \[[17](http://arxiv.org/abs/2202.07800)\]. ViTCoD proposes a dedicated algorithm and accelerator co-design framework, achieving substantial speedups by optimizing attention computations and data movements \[[14](http://arxiv.org/abs/2210.09573)\]. These approaches demonstrate the potential of combining algorithmic optimizations with hardware-specific designs to enhance ViT performance \[[18](http://arxiv.org/abs/2503.02891)\].

In summary, while existing methods have made progress in ViT acceleration, there remains a need for comprehensive solutions that address both algorithmic and hardware challenges. Our work introduces a novel approach that maps all ViT operations onto FPGAs using a new arithmetic format, achieving significant speedup and hardware efficiency improvements \[[1](https://www.semanticscholar.org/paper/0ade4d722e48379761d17cf1efc05200315c27d9)\].

### References

1. \[[1](https://www.semanticscholar.org/paper/0ade4d722e48379761d17cf1efc05200315c27d9)\] \[[15](http://arxiv.org/abs/2205.11397)\]  
2. \[[2](http://arxiv.org/abs/2208.05163)\] \[[16](https://www.semanticscholar.org/paper/b2e51759f910101691039846bec4401a85b53309)\]  
3. \[[3](http://arxiv.org/abs/2211.08110)\] \[[17](http://arxiv.org/abs/2202.07800)\]  
4. \[[4](http://arxiv.org/abs/2405.00314)\] \[[18](http://arxiv.org/abs/2503.02891)\]  
5. \[[5](http://arxiv.org/abs/2402.09709)\] \[[16](https://www.semanticscholar.org/paper/b2e51759f910101691039846bec4401a85b53309)\]  
6. \[[6](https://www.semanticscholar.org/paper/f47b726ad00e1a93adc5b3e266c71d75bb05e1ff)\] \[[14](http://arxiv.org/abs/2210.09573)\]  
7. \[[7](http://arxiv.org/abs/2403.20230)\] \[[14](http://arxiv.org/abs/2210.09573)\]  
8. \[[8](http://arxiv.org/abs/2309.02031)\] \[[18](http://arxiv.org/abs/2503.02891)\]  
9. \[[9](http://arxiv.org/abs/2405.03882)\] \[[16](https://www.semanticscholar.org/paper/b2e51759f910101691039846bec4401a85b53309)\]  
10. \[[10](http://arxiv.org/abs/2210.06707)\] \[[10](http://arxiv.org/abs/2210.06707)\]  
11. \[[11](http://arxiv.org/abs/2407.12736)\] \[[18](http://arxiv.org/abs/2503.02891)\]  
12. \[[12](http://arxiv.org/abs/2302.09108)\] \[[18](http://arxiv.org/abs/2503.02891)\]  
13. \[[13](http://arxiv.org/abs/2403.14047)\] \[[18](http://arxiv.org/abs/2503.02891)\]  
14. \[[14](http://arxiv.org/abs/2210.09573)\] \[[14](http://arxiv.org/abs/2210.09573)\]  
15. \[[15](http://arxiv.org/abs/2205.11397)\] \[[15](http://arxiv.org/abs/2205.11397)\]  
16. \[[16](https://www.semanticscholar.org/paper/b2e51759f910101691039846bec4401a85b53309)\] \[[16](https://www.semanticscholar.org/paper/b2e51759f910101691039846bec4401a85b53309)\]  
17. \[[17](http://arxiv.org/abs/2202.07800)\] \[[17](http://arxiv.org/abs/2202.07800)\]  
18. \[[18](http://arxiv.org/abs/2503.02891)\] \[[18](http://arxiv.org/abs/2503.02891)\]
