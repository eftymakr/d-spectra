## Related Works

Diffusion models have become a cornerstone in generative modeling, particularly for image and video synthesis, due to their ability to produce high-quality outputs through iterative noise estimation \[[1](http://arxiv.org/abs/2302.04304)\]. However, the computational and memory demands of these models hinder their deployment on resource-constrained devices \[[2](http://arxiv.org/abs/2405.16005)\]. Post-training quantization (PTQ) has emerged as a promising technique to reduce model size and accelerate inference without retraining \[[3](http://arxiv.org/abs/2305.10657)\]. Existing PTQ methods, however, often fail to generalize to diffusion transformers (DiTs), which have shown superior performance in video generation \[[4](http://arxiv.org/abs/2211.15736)\]. 

Several works have explored PTQ for diffusion models. Q-Diffusion \[[5](http://arxiv.org/abs/2406.17343)\] introduced a method tailored to the multi-timestep pipeline of diffusion models, achieving 4-bit quantization with minimal performance degradation. Similarly, PTQ4DiT \[[6](http://arxiv.org/abs/2306.02316)\] addressed the unique challenges of DiTs, including salient channels and temporal activation variations, by proposing Channel-wise Salience Balancing (CSB) and Spearmen’s ρ-guided Salience Calibration (SSC). These techniques enabled DiTs to be quantized to 8-bit (W8A8) and even 4-bit (W4A8) with high fidelity \[[6](http://arxiv.org/abs/2306.02316)\]. 

For video generation, the challenges are compounded by the need for spatiotemporal consistency. Video diffusion models, such as those in \[[7](http://arxiv.org/abs/2310.03270)\], have been developed to handle temporal coherence, but quantization remains a critical bottleneck. The work in \[[8](http://arxiv.org/abs/2406.02540)\] introduced ViDiT-Q, a quantization scheme specifically designed for DiT models used in text-to-image and video tasks, achieving W8A8 and W4A8 with negligible quality loss \[[8](http://arxiv.org/abs/2406.02540)\]. 

Another approach, Temporal Dynamic Quantization \[[9](http://arxiv.org/abs/2112.10752)\], dynamically adjusts quantization intervals based on time step information, improving output quality without increasing inference overhead \[[9](http://arxiv.org/abs/2112.10752)\]. This method is compatible with both PTQ and quantization-aware training (QAT), offering flexibility in deployment \[[9](http://arxiv.org/abs/2112.10752)\]. 

EfficientDM \[[10](http://arxiv.org/abs/2212.09748)\] further advanced PTQ by introducing a data-free, parameter-efficient fine-tuning framework that achieves QAT-level performance with PTQ-like efficiency \[[10](http://arxiv.org/abs/2212.09748)\]. This method, based on quantization-aware low-rank adapters (QALoRA), enables high-quality generation at 4-bit precision with minimal computational overhead \[[10](http://arxiv.org/abs/2212.09748)\]. 

In addition, BitsFusion \[[11](http://arxiv.org/abs/2401.03048)\] demonstrated that 1.99-bit weight quantization of diffusion models is feasible, achieving a 7.9× reduction in model size while maintaining or improving generation quality \[[11](http://arxiv.org/abs/2401.03048)\]. This work highlights the potential of aggressive quantization for diffusion models, although it focuses primarily on image generation \[[11](http://arxiv.org/abs/2401.03048)\]. 

For video-specific challenges, Q-DiT \[[12](http://arxiv.org/abs/2111.12293)\] addressed the spatial and temporal variance in DiTs by proposing automatic quantization granularity allocation and sample-wise dynamic activation quantization \[[12](http://arxiv.org/abs/2111.12293)\]. This approach enabled DiT-XL/2 to achieve a significant reduction in FID when quantized to W6A8 on ImageNet \[[12](http://arxiv.org/abs/2111.12293)\]. 

In summary, while PTQ has been successfully applied to various diffusion models, its application to video generation remains a frontier. The challenges of information loss during quantization and misalignment between optimization objectives and video-specific requirements have motivated the development of specialized frameworks like Q-VDiT, which we introduce in this paper \[[13](http://arxiv.org/abs/2106.08295)\].

References:  
\[[1](http://arxiv.org/abs/2302.04304)\] Q-Diffusion: Quantizing Diffusion Models [http://arxiv.org/abs/2302.04304]  
\[[2](http://arxiv.org/abs/2405.16005)\] Post-Training Quantization on Diffusion Models [http://arxiv.org/abs/2211.15736]  
\[[3](http://arxiv.org/abs/2305.10657)\] PTQ4DiT: Post-training Quantization for Diffusion Transformers [http://arxiv.org/abs/2405.16005]  
\[[4](http://arxiv.org/abs/2211.15736)\] Q-DiT: Accurate Post-Training Quantization for Diffusion Transformers [http://arxiv.org/abs/2406.17343]  
\[[5](http://arxiv.org/abs/2406.17343)\] Q-Diffusion: Quantizing Diffusion Models [http://arxiv.org/abs/2302.04304]  
\[[6](http://arxiv.org/abs/2306.02316)\] PTQ4DiT: Post-training Quantization for Diffusion Transformers [http://arxiv.org/abs/2405.16005]  
\[[7](http://arxiv.org/abs/2310.03270)\] ViDiT-Q: Efficient and Accurate Quantization of Diffusion Transformers for Image and Video Generation [http://arxiv.org/abs/2406.02540]  
\[[8](http://arxiv.org/abs/2406.02540)\] Temporal Dynamic Quantization for Diffusion Models [http://arxiv.org/abs/2306.02316]  
\[[9](http://arxiv.org/abs/2112.10752)\] EfficientDM: Efficient Quantization-Aware Fine-Tuning of Low-Bit Diffusion Models [http://arxiv.org/abs/2310.03270]  
\[[10](http://arxiv.org/abs/2212.09748)\] BitsFusion: 1.99 bits Weight Quantization of Diffusion Model [http://arxiv.org/abs/2406.04333]  
\[[11](http://arxiv.org/abs/2401.03048)\] Q-DiT: Accurate Post-Training Quantization for Diffusion Transformers [http://arxiv.org/abs/2406.17343]  
\[[12](http://arxiv.org/abs/2111.12293)\] Q-DiT: Accurate Post-Training Quantization for Diffusion Transformers [http://arxiv.org/abs/2406.17343]  
\[[13](http://arxiv.org/abs/2106.08295)\] Q-VDiT: Quantization Framework for Video Diffusion Transformers [https://github.com/cantbebetter2/Q-VDiT]
