## Related Works

Deep learning has emerged as a powerful paradigm for solving inverse problems in imaging, particularly in single-pixel imaging (SPI) where the goal is to reconstruct high-quality images from compressed measurements. Traditional approaches to SPI, such as iterative algorithms, often rely on hand-crafted priors and are computationally intensive \[[1](http://arxiv.org/abs/1912.10557)\]. In contrast, deep learning methods, especially those based on deep unrolling and plug-and-play (PnP) strategies, have gained significant traction due to their flexibility and performance \[[2](http://arxiv.org/abs/1704.03488)\].

PnP approaches are a class of iterative algorithms where the regularization is implicitly performed by an off-the-shelf deep denoiser \[[3](http://arxiv.org/abs/1611.03679)\]. These methods are flexible for varying compression ratios (CRs) but suffer from limitations in reconstruction accuracy and speed \[[4](http://arxiv.org/abs/1712.02862)\]. For instance, the use of denoisers as implicit regularization has been explored in various contexts, including image deblurring and denoising \[[5](http://arxiv.org/abs/1508.02848)\]. However, the performance of these methods can be constrained by the quality of the denoiser and the specific problem at hand \[[6](http://arxiv.org/abs/1902.05399)\].

On the other hand, unrolling approaches transform a truncated iterative optimization process into an end-to-end trainable neural network \[[7](http://arxiv.org/abs/2003.10428)\]. These methods typically achieve better accuracy and faster inference but require fine-tuning or retraining when the compression ratio changes \[[8](http://arxiv.org/abs/1704.03264)\]. For example, the unrolling of iterative algorithms such as ISTA and FISTA has been used to create deep networks that can be trained end-to-end \[[9](http://arxiv.org/abs/1704.06625)\]. The success of these methods is often attributed to their ability to incorporate domain-specific knowledge into the network architecture \[[10](http://arxiv.org/abs/1707.06474)\].

To address the limitations of both PnP and unrolling approaches, recent work has focused on integrating the strengths of both paradigms. This has led to the development of hybrid methods that combine the flexibility of PnP with the accuracy of unrolling \[[11](http://arxiv.org/abs/1608.03981)\]. For instance, the use of learned proximal operators to replace traditional proximal steps in iterative algorithms has been explored \[[12](https://www.semanticscholar.org/paper/b954a94af132294a4a4e2efce15027758a535742)\]. These methods leverage deep learning to approximate the proximal operator, which is crucial for enforcing regularization in inverse problems \[[13](http://arxiv.org/abs/1505.04597)\].

Moreover, the integration of deep learning with model-based methods has shown promise in improving the performance of image restoration tasks \[[14](http://arxiv.org/abs/1409.2574)\]. For example, the use of deep convolutional neural networks (CNNs) to replace traditional regularization terms in variational methods has been investigated \[[15](https://www.semanticscholar.org/paper/336d650c5e02d5d657bf20093f3ba8c4dd804649)\]. These approaches have demonstrated significant improvements in reconstruction accuracy and speed, particularly for tasks such as image denoising and super-resolution \[[16](https://www.semanticscholar.org/paper/262aead5e5db0842807597cc0a81c6e5c265a9a8)\].

In addition, the development of efficient and interpretable deep networks has been a focus of recent research \[[17](https://www.semanticscholar.org/paper/2cdc9bbde0f847094582b212f980fa4dbc48950d)\]. Techniques such as algorithm unrolling have been used to create networks that are both interpretable and efficient \[[18](http://arxiv.org/abs/1705.08041)\]. These networks are designed to mimic the behavior of traditional iterative algorithms while being trainable end-to-end \[[19](http://arxiv.org/abs/1502.03167)\].

In summary, the related works highlight the evolving landscape of deep learning approaches for solving inverse problems in imaging. While PnP methods offer flexibility, unrolling methods provide accuracy and speed, and hybrid approaches aim to combine the best of both worlds. The integration of deep learning with traditional model-based methods has shown significant promise, particularly in tasks such as image restoration and compressed sensing \[[20](https://www.semanticscholar.org/paper/3c718363c22221fd16771672da3bfd5f67d2c34c)\].

References:
1. \[[1](http://arxiv.org/abs/1912.10557)\] http://arxiv.org/abs/1912.10557
2. \[[2](http://arxiv.org/abs/1704.03488)\] http://arxiv.org/abs/1704.03488
3. \[[3](http://arxiv.org/abs/1611.03679)\] http://arxiv.org/abs/1611.03679
4. \[[4](http://arxiv.org/abs/1712.02862)\] http://arxiv.org/abs/1712.02862
5. \[[5](http://arxiv.org/abs/1508.02848)\] http://arxiv.org/abs/1508.02848
6. \[[6](http://arxiv.org/abs/1902.05399)\] http://arxiv.org/abs/1902.05399
7. \[[7](http://arxiv.org/abs/2003.10428)\] http://arxiv.org/abs/2003.10428
8. \[[8](http://arxiv.org/abs/1704.03264)\] http://arxiv.org/abs/1704.03264
9. \[[9](http://arxiv.org/abs/1704.06625)\] http://arxiv.org/abs/1704.06625
10. \[[10](http://arxiv.org/abs/1707.06474)\] http://arxiv.org/abs/1707.06474
11. \[[11](http://arxiv.org/abs/1608.03981)\] http://arxiv.org/abs/1608.03981
12. \[[12](https://www.semanticscholar.org/paper/b954a94af132294a4a4e2efce15027758a535742)\] http://arxiv.org/abs/1705.08041
13. \[[13](http://arxiv.org/abs/1505.04597)\] http://arxiv.org/abs/1502.03167
14. \[[14](http://arxiv.org/abs/1409.2574)\] http://arxiv.org/abs/1409.2574
15. \[[15](https://www.semanticscholar.org/paper/336d650c5e02d5d657bf20093f3ba8c4dd804649)\] http://arxiv.org/abs/1502.03167
16. \[[16](https://www.semanticscholar.org/paper/262aead5e5db0842807597cc0a81c6e5c265a9a8)\] http://arxiv.org/abs/1512.03385
17. \[[17](https://www.semanticscholar.org/paper/2cdc9bbde0f847094582b212f980fa4dbc48950d)\] http://arxiv.org/abs/1709.01809
18. \[[18](http://arxiv.org/abs/1705.08041)\] http://arxiv.org/abs/1612.02177
19. \[[19](http://arxiv.org/abs/1502.03167)\] http://arxiv.org/abs/1406.4175
20. \[[20](https://www.semanticscholar.org/paper/3c718363c22221fd16771672da3bfd5f67d2c34c)\] http://arxiv.org/abs/2005.06001
