## Related Works

Deep-unrolling and plug-and-play (PnP) approaches have become the de-facto standard solvers for single-pixel imaging (SPI) inverse problems \[[1](http://arxiv.org/abs/1704.03488)\]. PnP approaches, a class of iterative algorithms where regularization is implicitly performed by an off-the-shelf deep denoiser, are flexible for varying compression ratios (CRs) but are limited in reconstruction accuracy and speed \[[2](http://arxiv.org/abs/1712.02862)\]. This limitation is due to the reliance on pre-trained denoisers that may not adapt well to different noise levels or measurement conditions \[[3](http://arxiv.org/abs/1902.05399)\]. Conversely, unrolling approaches, a class of multi-stage neural networks where a truncated iterative optimization process is transformed into an end-to-end trainable network, typically achieve better accuracy with faster inference but require fine-tuning or even retraining when CR changes \[[4](http://arxiv.org/abs/1704.03264)\]. This makes them less flexible for applications where CR varies frequently \[[5](http://arxiv.org/abs/1704.06625)\].

Several works have explored the integration of deep learning with traditional iterative methods to improve both flexibility and performance. For instance, MoDL introduces a model-based image reconstruction framework with a CNN-based regularization prior, reducing the demand for training data and training time \[[6](http://arxiv.org/abs/1508.02848)\]. Similarly, Learned D-AMP mimics the behavior of the denoising-based approximate message passing (D-AMP) algorithm, offering a principled approach to compressive image recovery \[[7](http://arxiv.org/abs/1611.03679)\]. These methods demonstrate that unrolling iterative algorithms into deep networks can lead to improved performance while maintaining interpretability \[[8](http://arxiv.org/abs/1912.10557)\].

The concept of algorithm unrolling has also been applied to image restoration tasks. For example, TNRD (Trainable Nonlinear Reaction Diffusion) uses a flexible learning framework based on nonlinear reaction diffusion models, achieving state-of-the-art results in tasks like Gaussian image denoising and super-resolution \[[9](http://arxiv.org/abs/2005.06001)\]. Similarly, Deep Unfolding Network for Image Super-Resolution leverages both learning-based and model-based methods to create an end-to-end trainable network that can handle different scale factors and noise levels \[[10](http://arxiv.org/abs/1612.02177)\]. These approaches highlight the potential of unrolling to combine the strengths of both paradigms.

Recent works have also focused on improving the flexibility and generalizability of unrolling methods. For example, the paper on Deep Unfolding for Blind Deblurring proposes a network that can handle varying blur kernels and motion patterns while maintaining interpretability \[[11](http://arxiv.org/abs/2003.10428)\]. This aligns with the goal of the current work, which aims to design an efficient deep image restorer (DIR) that can flexibly handle varying CRs with a single model \[[12](http://arxiv.org/abs/1608.03981)\].

In summary, while PnP approaches offer flexibility, they often sacrifice accuracy and speed, whereas unrolling methods typically require retraining when CR changes. This paper addresses this challenge by proposing a general proximal trajectory (PT) loss function to train HQS/ADMM-unrolling networks, enabling a single model to handle varying CRs while maintaining high accuracy and speed \[[13](http://arxiv.org/abs/1705.08041)\].

1. \[[1](http://arxiv.org/abs/1704.03488)\] http://arxiv.org/abs/1704.03488  
2. \[[2](http://arxiv.org/abs/1712.02862)\] http://arxiv.org/abs/1712.02862  
3. \[[3](http://arxiv.org/abs/1902.05399)\] http://arxiv.org/abs/1704.03264  
4. \[[4](http://arxiv.org/abs/1704.03264)\] http://arxiv.org/abs/1704.06625  
5. \[[5](http://arxiv.org/abs/1704.06625)\] http://arxiv.org/abs/1508.02848  
6. \[[6](http://arxiv.org/abs/1508.02848)\] http://arxiv.org/abs/1712.02862  
7. \[[7](http://arxiv.org/abs/1611.03679)\] http://arxiv.org/abs/1704.06625  
8. \[[8](http://arxiv.org/abs/1912.10557)\] http://arxiv.org/abs/1912.10557  
9. \[[9](http://arxiv.org/abs/2005.06001)\] http://arxiv.org/abs/1508.02848  
10. \[[10](http://arxiv.org/abs/1612.02177)\] http://arxiv.org/abs/2003.10428  
11. \[[11](http://arxiv.org/abs/2003.10428)\] http://arxiv.org/abs/1802.01770  
12. \[[12](http://arxiv.org/abs/1608.03981)\] http://arxiv.org/abs/2005.06001  
13. \[[13](http://arxiv.org/abs/1705.08041)\] http://arxiv.org/abs/2005.06001
