## Related Works

Diffusion Transformers (DiTs) have become a prominent architecture for image and video generation due to their superior modeling capacities compared to traditional U-Net-based diffusion models \[[2406.0254](http://arxiv.org/abs/2406.02540)\]\[[2405.16005](http://arxiv.org/abs/2405.16005)\]\[[2307.01831](http://arxiv.org/abs/2307.01831)\]. However, the substantial parameter counts and high computational demands of DiTs present significant challenges for deployment, especially on resource-constrained edge devices. Quantization has emerged as a key approach to mitigate these issues by reducing model size and inference latency through low-bit representations of weights and activations.

### Quantization of Diffusion Transformers

Initial efforts in post-training quantization (PTQ) for diffusion transformers highlighted unique challenges stemming from the spatial and temporal variance in activations and weights, as well as the presence of outlier channels with extreme magnitudes. PTQ4DiT introduced Channel-wise Salience Balancing (CSB) and Spearman's ρ-guided Salience Calibration (SSC) to address these issues, enabling effective 8-bit and 4-bit quantization with minimal quality loss \[[2405.16005](http://arxiv.org/abs/2405.16005)\]. Likewise, ViDiT-Q proposed an improved quantization scheme tailored specifically for video and image DiTs, achieving W8A8 and W4A8 quantization with minimal degradation and practical memory and latency improvements \[[2505.18663](http://arxiv.org/abs/2505.18663)\]. 

Q-DiT further advanced PTQ by integrating automatic quantization granularity allocation and sample-wise dynamic activation quantization to manage significant variances across input channels and temporal steps, setting new benchmarks for W6A8 and W4A8 quantization in DiTs \[[2406.17343](http://arxiv.org/abs/2406.17343)\]\[[2409.07756](http://arxiv.org/abs/2409.07756)\]\[[2302.04304](http://arxiv.org/abs/2302.04304)\]. Complementing these, the HQ-DiT method employed hybrid floating-point (FP4) quantization with clipping range selection and identity transforms, allowing both weights and activations to be quantized to 4 bits with negligible performance loss \[[2405.19751](http://arxiv.org/abs/2405.19751)\]\[[2502.15077](http://arxiv.org/abs/2502.15077)\]\[[2503.15465](http://arxiv.org/abs/2503.15465)\].

Other works have proposed time-aware quantization strategies to explicitly handle temporal variations in diffusion processes. TaQ-DiT and TQ-DiT introduced time-grouping and time-variance-aware static transformations, respectively, to reduce quantization errors induced by temporal dynamics in activations, achieving superior low-bit quantization results \[[2502.04056](http://arxiv.org/abs/2502.04056)\]\[[2411.14172](http://arxiv.org/abs/2411.14172)\]. TR-DQ utilized rotation-based smoothing and timestep-adaptive parameters to dynamically optimize quantization across sampling steps, resulting in significant speedups and memory reductions \[[2503.06564](http://arxiv.org/abs/2503.06564)\]. Similarly, DiTAS applied temporal-aggregated smoothing and training-free LoRA modules to enable 4-bit weight and 8-bit activation quantization without fine-tuning \[[2409.07756](http://arxiv.org/abs/2409.07756)\].

### Quantization for Video Diffusion Transformers

Video DiTs bring additional complexity due to multi-frame processing and the necessity to preserve temporal coherence. Existing quantization methods designed for image DiTs often fail to maintain video quality post-quantization. To overcome this, DVD-Quant introduced a data-free PTQ framework for video DiTs, bypassing calibration overhead and enabling W4A4 quantization without video quality loss \[[2505.18663](http://arxiv.org/abs/2505.18663)\]\[[2502.15077](http://arxiv.org/abs/2502.15077)\]. QVD proposed High Temporal Discriminability Quantization (HTDQ) for temporal features and Scattered Channel Range Integration (SCRI) to handle inter-channel asymmetries, achieving near-lossless quantization at W8A8 and outperforming prior methods by large margins in FVD metrics \[[2407.11585](http://arxiv.org/abs/2407.11585)\].

Static quantization methods have also been explored for video diffusion transformers to enable deployment on AI processors lacking dynamic quantization support. A hardware-friendly static quantization approach for OpenSora demonstrated comparable video quality to FP16 and dynamic quantization baselines by utilizing per-step calibration and smooth quantization techniques \[[2502.15077](http://arxiv.org/abs/2502.15077)\]. Moreover, adaptive caching methods such as AdaCache have been proposed to accelerate video DiT inference by caching computations and scheduling denoising steps based on video content, achieving speedups up to 4.7× without quality degradation \[[2411.02397](http://arxiv.org/abs/2411.02397)\].

### Quantization-Aware Training and Hybrid Methods

Quantization-aware training (QAT) approaches, while resource-intensive, have demonstrated superior performance at extremely low bit-widths. The EfficientDM framework introduced a data-free and parameter-efficient fine-tuning method that achieves QAT-level results with PTQ-like efficiency, including temporal learned step-size quantization and scale-aware optimization to enhance denoising capabilities \[[2310.0327](http://arxiv.org/abs/2310.03270)\]. QVGen leveraged auxiliary modules and a rank-decay strategy to enable 3-bit and 4-bit quantization of video diffusion models with full-precision comparable quality, significantly outperforming baseline methods \[[2505.11497](http://arxiv.org/abs/2505.11497)\].

Hybrid quantization schemes combining floating-point and fixed-point formats have shown promise in aligning quantization with the distribution of DiT weights and activations, as demonstrated by FP4DiT and HQ-DiT. These approaches improve quantization fidelity and generation quality under extremely low-bit settings \[[2405.19751](http://arxiv.org/abs/2405.19751)\]\[[2503.15465](http://arxiv.org/abs/2503.15465)\].

### Challenges and Future Directions

Despite these advances, quantization of video DiTs remains challenging due to the need to preserve spatiotemporal correlations and manage dynamic activation distributions across time steps. Existing methods often overlook the misalignment between optimization objectives and video generation requirements, leading to performance degradation. Recent studies have pointed out the importance of joint reconstruction of weights and activations, temporal-aware calibration, and adaptive bit-width allocation to better capture temporal dynamics \[[2411.14172](http://arxiv.org/abs/2411.14172)\]\[[2305.10657](http://arxiv.org/abs/2305.10657)\]\[[2503.06564](http://arxiv.org/abs/2503.06564)\].

Our work, Q-VDiT, builds upon these foundations by introducing the Token-aware Quantization Estimator (TQE) to compensate quantization errors along token and feature dimensions, and Temporal Maintenance Distillation (TMD) to preserve spatiotemporal correlations across video frames. This targeted approach addresses both quantization-induced information loss and optimization misalignment, achieving state-of-the-art scene consistency and surpassing existing quantization methods for video DiTs \[[2407.11585](http://arxiv.org/abs/2407.11585)\]\[[2503.15465](http://arxiv.org/abs/2503.15465)\].

---

### References

\[[2406.0254](http://arxiv.org/abs/2406.02540)\] ViDiT-Q: Efficient and Accurate Quantization of Diffusion Transformers for Image and Video Generation [http://arxiv.org/abs/2406.02540]  
\[[2406.17343](http://arxiv.org/abs/2406.17343)\] Q-DiT: Accurate Post-Training Quantization for Diffusion Transformers [http://arxiv.org/abs/2406.17343]  
\[[2505.18663](http://arxiv.org/abs/2505.18663)\] DVD-Quant: Data-free Video Diffusion Transformers Quantization [http://arxiv.org/abs/2505.18663]  
\[[2502.04056](http://arxiv.org/abs/2502.04056)\] TQ-DiT: Efficient Time-Aware Quantization for Diffusion Transformers [http://arxiv.org/abs/2502.04056]  
\[[2411.14172](http://arxiv.org/abs/2411.14172)\] TaQ-DiT: Time-Aware Quantization for Diffusion Transformers [http://arxiv.org/abs/2411.14172]  
\[[2405.16005](http://arxiv.org/abs/2405.16005)\] PTQ4DiT: Post-training Quantization for Diffusion Transformers [http://arxiv.org/abs/2405.16005]  
\[[2310.0327](http://arxiv.org/abs/2310.03270)\] EfficientDM: Efficient Quantization-Aware Fine-Tuning of Low-Bit Diffusion Models [http://arxiv.org/abs/2310.03270]  
\[[2505.11497](http://arxiv.org/abs/2505.11497)\] QVGen: Pushing the Limit of Quantized Video Generative Models [http://arxiv.org/abs/2505.11497]  
\[[2405.19751](http://arxiv.org/abs/2405.19751)\] HQ-DiT: Efficient Diffusion Transformer with FP4 Hybrid Quantization [http://arxiv.org/abs/2405.19751]  
\[[2407.11585](http://arxiv.org/abs/2407.11585)\] QVD: Post-training Quantization for Video Diffusion Models [http://arxiv.org/abs/2407.11585]  
\[[2409.07756](http://arxiv.org/abs/2409.07756)\] Q-DiT: Accurate Post-Training Quantization for Diffusion Transformers [http://arxiv.org/abs/2406.17343]  
\[[2302.04304](http://arxiv.org/abs/2302.04304)\] Q-DiT: Accurate Post-Training Quantization for Diffusion Transformers [http://arxiv.org/abs/2406.17343]  
\[[2502.15077](http://arxiv.org/abs/2502.15077)\] Hardware-Friendly Static Quantization Method for Video Diffusion Transformers [http://arxiv.org/abs/2502.15077]  
\[[2503.15465](http://arxiv.org/abs/2503.15465)\] FP4DiT: Towards Effective Floating Point Quantization for Diffusion Transformers [http://arxiv.org/abs/2503.15465]  
\[[2305.10657](http://arxiv.org/abs/2305.10657)\] PTQD: Accurate Post-Training Quantization for Diffusion Models [http://arxiv.org/abs/2305.10657]  
\[[2503.06564](http://arxiv.org/abs/2503.06564)\] TR-DQ: Time-Rotation Diffusion Quantization [http://arxiv.org/abs/2503.06564]  
\[[2411.02397](http://arxiv.org/abs/2411.02397)\] Adaptive Caching for Faster Video Generation With Diffusion Transformers [http://arxiv.org/abs/2411.02397]  
\[[2307.01831](http://arxiv.org/abs/2307.01831)\] DiT-3D: Exploring Plain Diffusion Transformers for 3D Shape Generation [http://arxiv.org/abs/2307.01831]