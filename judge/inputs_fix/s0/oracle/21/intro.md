## Related Works

Neural rendering has emerged as a powerful paradigm for reconstructing 3D scenes from 2D images, leveraging the ability to model complex geometry and appearance \[[10](http://arxiv.org/abs/2409.02048)\]. The core idea involves optimizing the reconstructed scene by minimizing the uncertainty in geometry and appearance across multiple input views \[[10](http://arxiv.org/abs/2409.02048)\]. However, the quality of reconstruction is often constrained by the number of input views, especially in dynamic and complex environments where certain angles of objects are never captured \[[10](http://arxiv.org/abs/2409.02048)\]. To address this limitation, recent works have explored the use of video frame interpolation (VFI) as a data augmentation technique to enrich the training data \[[10](http://arxiv.org/abs/2409.02048)\].

Video frame interpolation has evolved from classical motion compensation-based methods to deep learning approaches, including kernel-, flow-, hybrid-, phase-, GAN-, Transformer-, Mamba-, and diffusion model-based methods \[[1](http://arxiv.org/abs/2506.01061)\]. These methods aim to synthesize intermediate frames between existing ones while maintaining spatial and temporal coherence \[[1](http://arxiv.org/abs/2506.01061)\]. A key challenge in VFI is handling large motion, occlusion, and lighting variation \[[1](http://arxiv.org/abs/2506.01061)\]. To address these issues, several works have proposed depth-aware flow projection layers and hierarchical feature learning to improve the quality of interpolated frames \[[2](http://arxiv.org/abs/1904.00830)\]. For instance, the depth-aware approach explicitly detects occlusion by leveraging depth information to synthesize intermediate flows that prioritize closer objects \[[2](http://arxiv.org/abs/1904.00830)\].

Real-time video frame interpolation has also been a focus of recent research, with methods like RIFE achieving state-of-the-art performance while maintaining high efficiency \[[3](http://arxiv.org/abs/2011.06294)\]. RIFE uses a neural network named IFNet to estimate intermediate flows end-to-end, enabling fast and high-quality frame interpolation \[[3](http://arxiv.org/abs/2011.06294)\]. Additionally, the proposed model supports arbitrary-timestep interpolation and is trained without relying on pre-trained optical flow models \[[3](http://arxiv.org/abs/2011.06294)\].

Efficient video frame interpolation remains a challenge, particularly when dealing with multi-frame interpolation. The Many-to-Many (M2M) splatting framework has been introduced to address this, allowing for fast and efficient interpolation by directly warping pixels to the desired time step and fusing overlapping pixels \[[4](http://arxiv.org/abs/2204.03513)\]. This approach reduces the need for post-refinement and improves efficiency while maintaining high-quality output \[[4](http://arxiv.org/abs/2204.03513)\].

Recent works have also focused on extracting motion and appearance information more effectively for VFI. A novel module has been proposed to explicitly extract both types of information via a unifying operation, improving the efficiency and performance of VFI \[[5](http://arxiv.org/abs/2303.00440)\]. This module can be seamlessly integrated into hybrid CNN and Transformer architectures, enabling efficient and high-quality frame interpolation \[[5](http://arxiv.org/abs/2303.00440)\].

In the broader context of neural rendering, methods like NeuRAD and Lightning NeRF have been developed to improve the performance of neural radiance fields (NeRFs) in autonomous driving scenarios \[[6](http://arxiv.org/abs/2311.15260)\]\[[7](http://arxiv.org/abs/2403.05907)\]. These approaches address challenges such as long training times, dense semantic supervision, and lack of generalizability by introducing efficient hybrid scene representations and robust training strategies \[[6](http://arxiv.org/abs/2311.15260)\]\[[7](http://arxiv.org/abs/2403.05907)\].

References:

1. \[[1](http://arxiv.org/abs/2506.01061)\] AceVFI: A Comprehensive Survey of Advances in Video Frame Interpolation  
2. \[[2](http://arxiv.org/abs/1904.00830)\] Depth-Aware Video Frame Interpolation  
3. \[[3](http://arxiv.org/abs/2011.06294)\] Real-Time Intermediate Flow Estimation for Video Frame Interpolation  
4. \[[4](http://arxiv.org/abs/2204.03513)\] Many-to-many Splatting for Efficient Video Frame Interpolation  
5. \[[5](http://arxiv.org/abs/2303.00440)\] Extracting Motion and Appearance via Inter-Frame Attention for Efficient Video Frame Interpolation  
6. \[[6](http://arxiv.org/abs/2311.15260)\] NeuRAD: Neural Rendering for Autonomous Driving  
7. \[[7](http://arxiv.org/abs/2403.05907)\] Lightning NeRF: Efficient Hybrid Scene Representation for Autonomous Driving  
8. \[[8](http://arxiv.org/abs/2211.09682)\] AligNeRF: High-Fidelity Neural Radiance Fields via Alignment-Aware Training  
9. \[[9](http://arxiv.org/abs/2302.12231)\] DiffusioNeRF: Regularizing Neural Radiance Fields with Denoising Diffusion Models  
10. \[[10](http://arxiv.org/abs/2409.02048)\] ViewCrafter: Taming Video Diffusion Models for High-fidelity Novel View Synthesis
