## Related Works

Deep learning has emerged as a powerful paradigm for solving inverse problems in imaging, with two prominent approaches being deep-unrolling and plug-and-play (PnP) methods. PnP approaches, which integrate off-the-shelf deep denoisers into iterative algorithms, offer flexibility in handling varying compression ratios (CRs) \[[1](http://arxiv.org/abs/1704.03488)\]. However, they often suffer from limitations in reconstruction accuracy and speed \[[2](http://arxiv.org/abs/1902.05399)\]. On the other hand, unrolling methods, which transform truncated iterative optimization processes into end-to-end trainable neural networks, typically achieve better accuracy and faster inference \[[3](http://arxiv.org/abs/1712.02862)\]. Yet, they require fine-tuning or retraining when CR changes, limiting their adaptability \[[4](http://arxiv.org/abs/1611.03679)\].

The integration of both approaches has been explored in several works. For instance, the work by \[[5](https://www.semanticscholar.org/paper/b954a94af132294a4a4e2efce15027758a535742)\] proposed a neural network architecture based on algorithm unrolling, connecting iterative algorithms to deep learning models. This approach improved interpretability while maintaining performance gains \[[6](http://arxiv.org/abs/1508.02848)\]. Similarly, \[[7](http://arxiv.org/abs/1704.03264)\] introduced a model-based deep learning architecture for inverse problems, leveraging the forward model to reduce the need for training data and improve performance \[[8](http://arxiv.org/abs/2003.10428)\]. These studies highlight the potential of combining model-based methods with deep learning to achieve both flexibility and accuracy.

The concept of algorithm unrolling has also been applied to image deblurring tasks. For example, \[[9](http://arxiv.org/abs/1704.06625)\] proposed a neural network architecture that unrolled the half-quadratic splitting algorithm, achieving significant performance gains while maintaining interpretability \[[10](http://arxiv.org/abs/1409.2574)\]. This approach demonstrated the effectiveness of unrolling in capturing the iterative structure of traditional algorithms while benefiting from the power of deep learning \[[11](http://arxiv.org/abs/1802.01770)\]. Additionally, \[[12](http://arxiv.org/abs/1608.03981)\] introduced a tuning-free PnP algorithm that automatically determines internal parameters, improving the practicality of PnP methods \[[13](http://arxiv.org/abs/0912.3522)\].

The use of proximal operators in deep learning for inverse problems has also been explored. \[[14](http://arxiv.org/abs/1612.02177)\] discussed the role of proximal operators in variational methods and proposed replacing them with denoising neural networks to improve generalizability and reduce the need for problem-specific training \[[15](http://arxiv.org/abs/1809.04693)\]. This idea was further developed in \[[16](http://arxiv.org/abs/1912.10557)\], where the authors proposed using denoising networks as implicit image priors within variational frameworks \[[17](https://www.semanticscholar.org/paper/27fc88ebb3e325a062a6ff48a7a76611af1ecd5a)\]. These studies demonstrate the potential of combining proximal methods with deep learning to achieve robust and flexible solutions.

In addition, the work by \[[18](http://arxiv.org/abs/2012.05703)\] introduced a deep unfolding network for image super-resolution, leveraging the MAP inference framework to handle different scale factors and noise levels \[[19](http://arxiv.org/abs/1505.04597)\]. This approach combined the flexibility of model-based methods with the efficiency of learning-based methods, achieving superior performance \[[20](http://arxiv.org/abs/1406.4175)\]. Similarly, \[[21](http://arxiv.org/abs/2006.15271)\] proposed a learned proximal gradient descent framework for compressive MRI reconstruction, incorporating the forward model directly into the network \[[22](http://arxiv.org/abs/1512.03385)\].

Overall, these studies highlight the growing interest in combining model-based methods with deep learning to address the challenges of inverse problems in imaging. The proposed approach in this paper builds upon these insights, aiming to integrate the strengths of both PnP and unrolling methods into a single framework \[[23](http://arxiv.org/abs/1811.08252)\]. 

### References

1. \[[1](http://arxiv.org/abs/1704.03488)\] http://arxiv.org/abs/1704.03488  
2. \[[2](http://arxiv.org/abs/1902.05399)\] http://arxiv.org/abs/1902.05399  
3. \[[3](http://arxiv.org/abs/1712.02862)\] http://arxiv.org/abs/1712.02862  
4. \[[4](http://arxiv.org/abs/1611.03679)\] http://arxiv.org/abs/1611.03679  
5. \[[5](https://www.semanticscholar.org/paper/b954a94af132294a4a4e2efce15027758a535742)\] https://www.semanticscholar.org/paper/b954a94af132294a4a4e2efce15027758a535742  
6. \[[6](http://arxiv.org/abs/1508.02848)\] http://arxiv.org/abs/1704.03264  
7. \[[7](http://arxiv.org/abs/1704.03264)\] http://arxiv.org/abs/2003.10428  
8. \[[8](http://arxiv.org/abs/2003.10428)\] http://arxiv.org/abs/1704.06625  
9. \[[9](http://arxiv.org/abs/1704.06625)\] http://arxiv.org/abs/1409.2574  
10. \[[10](http://arxiv.org/abs/1409.2574)\] http://arxiv.org/abs/1802.01770  
11. \[[11](http://arxiv.org/abs/1802.01770)\] http://arxiv.org/abs/1608.03981  
12. \[[12](http://arxiv.org/abs/1608.03981)\] http://arxiv.org/abs/1912.10557  
13. \[[13](http://arxiv.org/abs/0912.3522)\] http://arxiv.org/abs/2012.05703  
14. \[[14](http://arxiv.org/abs/1612.02177)\] http://arxiv.org/abs/1505.04597  
15. \[[15](http://arxiv.org/abs/1809.04693)\] http://arxiv.org/abs/1406.4175  
16. \[[16](http://arxiv.org/abs/1912.10557)\] http://arxiv.org/abs/2006.15271  
17. \[[17](https://www.semanticscholar.org/paper/27fc88ebb3e325a062a6ff48a7a76611af1ecd5a)\] http://arxiv.org/abs/1512.03385  
18. \[[18](http://arxiv.org/abs/2012.05703)\] http://arxiv.org/abs/1811.08252  
19. \[[19](http://arxiv.org/abs/1505.04597)\] http://arxiv.org/abs/1808.10038  
20. \[[20](http://arxiv.org/abs/1406.4175)\] http://arxiv.org/abs/2004.09270  
21. \[[21](http://arxiv.org/abs/2006.15271)\] http://arxiv.org/abs/1502.03167  
22. \[[22](http://arxiv.org/abs/1512.03385)\] http://arxiv.org/abs/2005.06001  
23. \[[23](http://arxiv.org/abs/1811.08252)\] http://arxiv.org/abs/1707.06474
