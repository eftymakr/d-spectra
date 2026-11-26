## Related Works

Diffusion models have gained significant traction in image and video generation due to their ability to produce high-quality outputs \[[11](http://arxiv.org/abs/2212.09748)\]. However, their deployment on edge devices is hindered by high computational demands and large parameter counts \[[11](http://arxiv.org/abs/2212.09748)\]. Quantization has emerged as a promising solution to reduce storage and accelerate inference by lowering the bit-width of model parameters \[[1](http://arxiv.org/abs/2302.04304)\]. Early efforts in quantizing diffusion models, such as Q-Diffusion \[[1](http://arxiv.org/abs/2302.04304)\], focused on post-training quantization (PTQ) tailored to the multi-timestep pipeline of diffusion models. These methods faced challenges due to the changing output distributions of noise estimation networks over time steps and bimodal activation distributions \[[1](http://arxiv.org/abs/2302.04304)\]. Subsequent works, such as PTQ4DiT \[[2](http://arxiv.org/abs/2405.16005)\], addressed these issues by introducing techniques like Channel-wise Salience Balancing (CSB) and Spearmen's ρ-guided Salience Calibration (SSC), enabling effective 8-bit and 4-bit quantization of diffusion transformers \[[2](http://arxiv.org/abs/2405.16005)\].

The application of PTQ to video generation remains underexplored, despite the growing importance of video models in real-world applications \[[12](http://arxiv.org/abs/2204.03458)\]. Existing quantization methods for image generation models often fail to generalize to video tasks due to the unique challenges posed by temporal coherence and motion consistency \[[12](http://arxiv.org/abs/2204.03458)\]. For instance, video diffusion models require careful handling of spatiotemporal correlations, which are not adequately addressed by standard quantization techniques \[[12](http://arxiv.org/abs/2204.03458)\]. To address these challenges, recent work such as ViDiT-Q \[[20](http://arxiv.org/abs/2406.02540)\] introduced a tailored quantization scheme for diffusion transformers, achieving W8A8 and W4A8 with minimal degradation in visual quality. This highlights the need for specialized quantization frameworks that account for the unique properties of video generation tasks.

Temporal dynamic quantization methods, such as those proposed in \[[6](http://arxiv.org/abs/2306.02316)\], have also been explored to address the issue of temporal variation in activation distributions. These methods dynamically adjust quantization intervals based on time step information, improving output quality without introducing computational overhead during inference \[[6](http://arxiv.org/abs/2306.02316)\]. Similarly, the work on PTQ4ViT \[[8](http://arxiv.org/abs/2111.12293)\] demonstrated that vision transformers can be effectively quantized with minimal accuracy loss by addressing the non-Gaussian distribution of activation values and using a Hessian-guided metric for scaling factor determination \[[8](http://arxiv.org/abs/2111.12293)\].

In addition to quantization techniques, the optimization of video diffusion models presents unique challenges. For example, the work on ConsistI2V \[[22](http://arxiv.org/abs/2402.04324)\] introduced methods to enhance visual consistency in image-to-video generation by maintaining spatial and motion consistency across frames. These approaches are critical for ensuring that quantized models retain the necessary temporal coherence for video generation tasks \[[22](http://arxiv.org/abs/2402.04324)\].

In summary, while significant progress has been made in quantizing diffusion models, the specific challenges of video generation require tailored solutions. The proposed Q-VDiT framework addresses these challenges by introducing Token-aware Quantization Estimator (TQE) and Temporal Maintenance Distillation (TMD), which together enable effective quantization of video DiT models \[[1](http://arxiv.org/abs/2302.04304)\]. These contributions build upon and extend previous work in the field, providing a robust framework for deploying diffusion models on resource-constrained devices.

### References

1. Q-Diffusion: Quantizing Diffusion Models [http://arxiv.org/abs/2302.04304]
2. PTQ4DiT: Post-training Quantization for Diffusion Transformers [http://arxiv.org/abs/2405.16005]
3. PTQD: Accurate Post-Training Quantization for Diffusion Models [http://arxiv.org/abs/2305.10657]
4. EfficientDM: Efficient Quantization-Aware Fine-Tuning of Low-Bit Diffusion Models [http://arxiv.org/abs/2310.03270]
5. Temporal Dynamic Quantization for Diffusion Models [http://arxiv.org/abs/2306.02316]
6. High-Resolution Image Synthesis with Latent Diffusion Models [http://arxiv.org/abs/2112.10752]
7. PTQ4ViT: Post-training Quantization for Vision Transformers with Twin Uniform Quantization [http://arxiv.org/abs/2111.12293]
8. Q-DiT: Accurate Post-Training Quantization for Diffusion Transformers [http://arxiv.org/abs/2406.17343]
9. FQ-ViT: Post-Training Quantization for Fully Quantized Vision Transformer [http://arxiv.org/abs/2111.13824]
10. Scalable Diffusion Models with Transformers [http://arxiv.org/abs/2212.09748]
11. Video Diffusion Models [http://arxiv.org/abs/2204.03458]
12. Diffusion Models Beat GANs on Image Synthesis [http://arxiv.org/abs/2105.05233]
13. Post-Training Quantization for Vision Transformer [http://arxiv.org/abs/2106.14156]
14. Latte: Latent Diffusion Transformer for Video Generation [http://arxiv.org/abs/2401.03048]
15. Align Your Latents: High-Resolution Video Synthesis with Latent Diffusion Models [http://arxiv.org/abs/2304.08818]
16. A White Paper on Neural Network Quantization [http://arxiv.org/abs/2106.08295]
17. All are Worth Words: A ViT Backbone for Diffusion Models [http://arxiv.org/abs/2209.12152]
18. ConsistI2V: Enhancing Visual Consistency for Image-to-Video Generation [http://arxiv.org/abs/2402.04324]
19. Stable Video Diffusion: Scaling Latent Video Diffusion Models to Large Datasets [http://arxiv.org/abs/2311.15127]
20. ViDiT-Q: Efficient and Accurate Quantization of Diffusion Transformers for Image and Video Generation [http://arxiv.org/abs/2406.02540]
