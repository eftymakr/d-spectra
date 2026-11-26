## Related Works

Video super-resolution (VSR) has been a focal point in computer vision, aiming to enhance low-resolution videos into high-resolution ones while preserving temporal consistency and visual quality. Early approaches relied on traditional methods such as interpolation and motion compensation, but recent advances have shifted towards deep learning-based frameworks \[[1](http://arxiv.org/abs/2502.07381)\]. These methods typically process each frame independently or use recurrent architectures to model temporal dependencies \[[2](https://www.semanticscholar.org/paper/c6a8ff4d9dcdf9e5d82310b847af999ed6655f65)\]. However, they often struggle with maintaining consistency across frames due to the inherent limitations of recurrent structures \[[3](http://arxiv.org/abs/2410.18137)\].

Diffusion models have emerged as a promising alternative for VSR, offering high-quality generation capabilities by iteratively denoising low-resolution inputs \[[4](http://arxiv.org/abs/2407.13987)\]. However, existing diffusion-based VSR methods suffer from introducing artifacts and degradations due to the stochastic nature of the diffusion process \[[5](http://arxiv.org/abs/2501.02269)\]. This issue is exacerbated in real-world scenarios where videos are often compressed and contain artifacts \[[6](http://arxiv.org/abs/2103.10081)\]. To address this, several works have proposed diffusion models tailored for compressed videos, incorporating modules to mitigate spatial distortions and refine temporal consistency \[[7](http://arxiv.org/abs/2002.11616)\]. For instance, the Spatial Degradation-Aware and Temporal Consistent (SDATC) diffusion model introduces a distortion control module and a spatio-temporal attention module to enhance the generation process \[[8](http://arxiv.org/abs/2407.01960)\].

Another line of research focuses on improving the efficiency and performance of VSR by leveraging advanced architectures. For example, the Deep Video Super-Resolution Network using Dynamic Upsampling Filters avoids explicit motion compensation by generating dynamic upsampling filters and a residual image directly from the input \[[9](https://www.semanticscholar.org/paper/a2c50f93f6d0892918e0ff653750d198ccab48d0)\]. Similarly, the RealViformer framework investigates the impact of artifacts on attention mechanisms and proposes channel-attention-based techniques to reduce feature redundancy and improve temporal consistency \[[10](http://arxiv.org/abs/2207.06345)\]. These approaches highlight the importance of modeling both spatial and temporal information effectively.

In addition to attention mechanisms, recurrent architectures have been explored to model long-term dependencies in video sequences \[[11](http://arxiv.org/abs/2201.12288)\]. The Frame-Recurrent Video Super-Resolution framework, for instance, uses previously inferred high-resolution estimates to super-resolve subsequent frames, naturally encouraging temporal consistency \[[12](http://arxiv.org/abs/1801.04590)\]. Similarly, the Video Super-Resolution Transformer (VSR-Transformer) adapts the Transformer architecture for VSR by introducing spatial-temporal convolutional self-attention and bidirectional optical flow-based feed-forward layers to capture correlations across frames \[[13](http://arxiv.org/abs/2007.10595)\].

Recent works have also focused on real-time VSR, emphasizing the need for efficient and scalable methods. The RVSRT framework, for example, introduces a real-time video super-resolution transformer that processes adjacent frames through a single UNet-style structure, significantly reducing computational costs while maintaining performance \[[14](https://www.semanticscholar.org/paper/437e15b62abf07c8bdd8ea5912dd9c83de5f5ce8)\]. Similarly, the Zooming Slow-Mo framework proposes a one-stage space-time video super-resolution approach that directly synthesizes high-resolution slow-motion videos from low-resolution, low-frame-rate inputs \[[15](http://arxiv.org/abs/1611.05250)\].

In summary, while numerous methods have been proposed to address the challenges of VSR, including artifacts, temporal inconsistency, and computational efficiency, the integration of self-supervised learning and advanced architectures like Mamba offers a promising direction for future research \[[16](http://arxiv.org/abs/2311.15127)\].

### References

1. \[[1](http://arxiv.org/abs/2502.07381)\] [Document 2]  
2. \[[2](https://www.semanticscholar.org/paper/c6a8ff4d9dcdf9e5d82310b847af999ed6655f65)\] [Document 12]  
3. \[[3](http://arxiv.org/abs/2410.18137)\] [Document 12]  
4. \[[4](http://arxiv.org/abs/2407.13987)\] [Document 1]  
5. \[[5](http://arxiv.org/abs/2501.02269)\] [Document 1]  
6. \[[6](http://arxiv.org/abs/2103.10081)\] [Document 1]  
7. \[[7](http://arxiv.org/abs/2002.11616)\] [Document 5]  
8. \[[8](http://arxiv.org/abs/2407.01960)\] [Document 5]  
9. \[[9](https://www.semanticscholar.org/paper/a2c50f93f6d0892918e0ff653750d198ccab48d0)\] [Document 2]  
10. \[[10](http://arxiv.org/abs/2207.06345)\] [Document 4]  
11. \[[11](http://arxiv.org/abs/2201.12288)\] [Document 9]  
12. \[[12](http://arxiv.org/abs/1801.04590)\] [Document 12]  
13. \[[13](http://arxiv.org/abs/2007.10595)\] [Document 21]  
14. \[[14](https://www.semanticscholar.org/paper/437e15b62abf07c8bdd8ea5912dd9c83de5f5ce8)\] [Document 14]  
15. \[[15](http://arxiv.org/abs/1611.05250)\] [Document 18]  
16. \[[16](http://arxiv.org/abs/2311.15127)\] [Document 26]
