## Related Works

Deep-unrolling and plug-and-play (PnP) approaches have become the de-facto standard solvers for single-pixel imaging (SPI) inverse problems \[[1](http://arxiv.org/abs/0805.0510)\]. PnP methods, a class of iterative algorithms where regularization is implicitly performed by an off-the-shelf deep denoiser, are flexible for varying compression ratios (CRs) but are limited in reconstruction accuracy and speed \[[2](http://arxiv.org/abs/1406.4175)\]. This limitation is due to the reliance on denoisers that may not be optimally adapted to the specific inverse problem at hand \[[3](http://arxiv.org/abs/2110.03220)\]. Conversely, unrolling approaches, a class of multi-stage neural networks where a truncated iterative optimization process is transformed into an end-to-end trainable network, typically achieve better accuracy with faster inference but require fine-tuning or even retraining when CR changes \[[4](http://arxiv.org/abs/2310.14344)\]. This makes them less adaptable to varying conditions \[[5](http://arxiv.org/abs/2410.02057)\].

Several works have explored the integration of denoisers into iterative algorithms for compressed sensing (CS). For instance, the D-AMP framework extends the approximate message passing (AMP) algorithm by integrating a generic denoiser, offering state-of-the-art performance while operating faster than competing methods \[[6](http://arxiv.org/abs/1601.06892)\]. Similarly, the Gradient Step Denoiser for convergent Plug-and-Play methods proposes a new type of Plug-and-Play methods based on half-quadratic splitting, where the denoiser is realized as a gradient descent step on a functional parameterized by a deep neural network \[[7](http://arxiv.org/abs/2110.09766)\]. This approach enables convergence guarantees and maintains performance comparable to state-of-the-art denoisers \[[8](http://arxiv.org/abs/2107.07225)\].

The use of learned proximal operators has also been explored to improve the performance of iterative algorithms. The learned proximal networks (LPN) framework provides exact proximal operators for a data-driven nonconvex regularizer and introduces a training strategy called proximal matching that promotes the recovery of the log-prior of the true data distribution \[[9](http://arxiv.org/abs/2204.13348)\]. This approach allows for general, unsupervised, expressive proximal operators that can be used for various inverse problems with convergence guarantees \[[10](http://arxiv.org/abs/2112.15299)\].

In addition, the use of deep neural networks for image restoration has been extensively studied. The Deep Generalized Unfolding Network (DGUNet) integrates a gradient estimation strategy into the gradient descent step of the Proximal Gradient Descent (PGD) algorithm, improving interpretability and generalizability \[[11](http://arxiv.org/abs/2304.13986)\]. Similarly, the Memory-Augmented Deep Unfolding Network (MADUN) introduces memory augmentation mechanisms to reduce information loss between stages and enhance network representation capability \[[12](http://arxiv.org/abs/2404.05001)\].

Overall, the integration of deep learning into iterative algorithms for inverse problems has led to significant improvements in performance and flexibility. However, the challenge remains to develop methods that can adapt to varying conditions without requiring extensive retraining or fine-tuning \[[13](http://arxiv.org/abs/1611.02862)\].

1. \[[1](http://arxiv.org/abs/0805.0510)\] http://arxiv.org/abs/2110.09766  
2. \[[2](http://arxiv.org/abs/1406.4175)\] http://arxiv.org/abs/2110.03220  
3. \[[3](http://arxiv.org/abs/2110.03220)\] http://arxiv.org/abs/2310.14344  
4. \[[4](http://arxiv.org/abs/2310.14344)\] http://arxiv.org/abs/2110.09766  
5. \[[5](http://arxiv.org/abs/2410.02057)\] http://arxiv.org/abs/2110.03220  
6. \[[6](http://arxiv.org/abs/1601.06892)\] http://arxiv.org/abs/1406.4175  
7. \[[7](http://arxiv.org/abs/2110.09766)\] http://arxiv.org/abs/2110.03220  
8. \[[8](http://arxiv.org/abs/2107.07225)\] http://arxiv.org/abs/2110.03220  
9. \[[9](http://arxiv.org/abs/2204.13348)\] http://arxiv.org/abs/2310.14344  
10. \[[10](http://arxiv.org/abs/2112.15299)\] http://arxiv.org/abs/2310.14344  
11. \[[11](http://arxiv.org/abs/2304.13986)\] http://arxiv.org/abs/2204.13348  
12. \[[12](http://arxiv.org/abs/2404.05001)\] http://arxiv.org/abs/2110.09766  
13. \[[13](http://arxiv.org/abs/1611.02862)\] http://arxiv.org/abs/1611.02862
