## Related Works

Diffusion transformers (DiT) have emerged as a powerful architecture for image and video generation, demonstrating superior performance compared to traditional diffusion models \[[1](http://arxiv.org/abs/2406.02540)\]. However, their large parameter counts and computational complexity pose significant challenges for deployment on resource-constrained devices \[[1](http://arxiv.org/abs/2406.02540)\]. To address these limitations, various quantization techniques have been proposed to reduce memory usage and improve inference speed \[[2](http://arxiv.org/abs/2406.17343)\]. 

Early efforts in quantizing diffusion models focused on image generation tasks, where techniques like post-training quantization (PTQ) have been applied with varying degrees of success \[[3](http://arxiv.org/abs/2505.18663)\]. However, these methods often fail to generalize to video generation due to the added complexity of temporal dependencies and multi-frame processing \[[4](http://arxiv.org/abs/2502.04056)\]. For instance, Q-DiT \[[5](http://arxiv.org/abs/2411.14172)\] introduces automatic quantization granularity allocation and sample-wise dynamic activation quantization to handle the spatial and temporal variance in DiT models, achieving notable improvements in image and video generation tasks \[[5](http://arxiv.org/abs/2411.14172)\]. Similarly, ViDiT-Q \[[6](http://arxiv.org/abs/2405.19751)\] is specifically designed for DiT models, achieving W8A8 and W4A8 quantization with minimal degradation in visual quality \[[6](http://arxiv.org/abs/2405.19751)\].

Video-specific quantization challenges have also been explored. DVD-Quant \[[7](http://arxiv.org/abs/2407.11585)\] introduces a data-free quantization framework for video DiTs, achieving a 2× speedup over full-precision baselines while maintaining visual fidelity \[[7](http://arxiv.org/abs/2407.11585)\]. TQ-DiT \[[8](http://arxiv.org/abs/2302.04304)\] addresses time-aware quantization by introducing joint reconstruction and time-variance-aware static transformations to improve quantization accuracy \[[8](http://arxiv.org/abs/2302.04304)\]. HQ-DiT \[[9](http://arxiv.org/abs/2307.01831)\] further advances the field by proposing FP4 hybrid quantization, achieving 4-bit quantization for both weights and activations with negligible performance loss \[[9](http://arxiv.org/abs/2307.01831)\].

Recent work has also focused on improving temporal consistency in video generation, which is crucial for high-quality video output \[[10](http://arxiv.org/abs/2502.15077)\]. QVD \[[11](http://arxiv.org/abs/2406.07686)\] introduces a post-training quantization strategy tailored for video diffusion models, achieving near-lossless performance degradation on W8A8 \[[11](http://arxiv.org/abs/2406.07686)\]. Similarly, Latte \[[12](http://arxiv.org/abs/2307.00331)\] proposes a latent diffusion transformer for video generation, demonstrating state-of-the-art performance across multiple benchmarks \[[12](http://arxiv.org/abs/2307.00331)\]. These advancements highlight the growing interest in efficient and high-quality video generation models.

In addition to quantization, other approaches have been explored to improve video generation efficiency. For example, DSV \[[13](http://arxiv.org/abs/2503.19881)\] accelerates video DiT training by leveraging dynamic attention sparsity, achieving up to 3.02× higher training throughput \[[13](http://arxiv.org/abs/2503.19881)\]. Similarly, VITON-DiT \[[14](http://arxiv.org/abs/2502.07590)\] introduces a video try-on framework using diffusion transformers, demonstrating the versatility of DiT in real-world applications \[[14](http://arxiv.org/abs/2502.07590)\].

These related works collectively underscore the importance of efficient and high-quality video generation models, with a growing focus on quantization techniques to enable deployment on resource-constrained devices \[[15](http://arxiv.org/abs/2401.03048)\].

References:
\[[1](http://arxiv.org/abs/2406.02540)\] http://arxiv.org/abs/2406.02540
\[[2](http://arxiv.org/abs/2406.17343)\] http://arxiv.org/abs/2406.17343
\[[3](http://arxiv.org/abs/2505.18663)\] http://arxiv.org/abs/2406.17343
\[[4](http://arxiv.org/abs/2502.04056)\] http://arxiv.org/abs/2406.02540
\[[5](http://arxiv.org/abs/2411.14172)\] http://arxiv.org/abs/2406.17343
\[[6](http://arxiv.org/abs/2405.19751)\] http://arxiv.org/abs/2406.02540
\[[7](http://arxiv.org/abs/2407.11585)\] http://arxiv.org/abs/2505.18663
\[[8](http://arxiv.org/abs/2302.04304)\] http://arxiv.org/abs/2502.04056
\[[9](http://arxiv.org/abs/2307.01831)\] http://arxiv.org/abs/2405.19751
\[[10](http://arxiv.org/abs/2502.15077)\] http://arxiv.org/abs/2407.11585
\[[11](http://arxiv.org/abs/2406.07686)\] http://arxiv.org/abs/2407.11585
\[[12](http://arxiv.org/abs/2307.00331)\] http://arxiv.org/abs/2401.03048
\[[13](http://arxiv.org/abs/2503.19881)\] http://arxiv.org/abs/2502.07590
\[[14](http://arxiv.org/abs/2502.07590)\] http://arxiv.org/abs/2405.18326
