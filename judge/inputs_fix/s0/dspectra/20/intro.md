## Related Works

Deep-unrolling and plug-and-play (PnP) approaches have become the de-facto standard solvers for single-pixel imaging (SPI) inverse problems \[[1](http://arxiv.org/abs/1912.10557)\]. PnP approaches, a class of iterative algorithms where regularization is implicitly performed by an off-the-shelf deep denoiser, are flexible for varying compression ratios (CRs) but are limited in reconstruction accuracy and speed \[[2](http://arxiv.org/abs/1502.03167)\]. This limitation is due to the reliance on denoisers that may not be well-suited for the specific inverse problem at hand \[[3](http://arxiv.org/abs/1902.05399)\]. Conversely, unrolling approaches, a class of multi-stage neural networks where a truncated iterative optimization process is transformed into an end-to-end trainable network, typically achieve better accuracy with faster inference but require fine-tuning or even retraining when CR changes \[[4](http://arxiv.org/abs/1712.02862)\]. This makes them less flexible for applications where CR varies significantly \[[5](http://arxiv.org/abs/2402.12971)\].

Several works have explored the integration of PnP and unrolling methods to combine their strengths. For instance, \[[6](http://arxiv.org/abs/2109.14025)\] introduced a framework that integrates PnP with deep learning-based denoisers, demonstrating improved performance on image restoration tasks. Similarly, \[[7](http://arxiv.org/abs/1611.03679)\] proposed a method that unrolls iterative algorithms into neural networks, allowing for the incorporation of physical models into the learning process. This approach has been successfully applied to various imaging problems, including image deblurring \[[8](http://arxiv.org/abs/1809.04693)\] and magnetic resonance imaging \[[9](http://arxiv.org/abs/1508.02848)\]. The key idea is to unroll the iterations of an optimization algorithm into a neural network, which can then be trained end-to-end \[[10](https://www.semanticscholar.org/paper/b954a94af132294a4a4e2efce15027758a535742)\].

The concept of unrolling has also been extended to other domains, such as compressive sensing and image super-resolution. For example, \[[11](http://arxiv.org/abs/1902.03493)\] proposed a deep unrolling approach for image super-resolution that leverages the half-quadratic splitting algorithm to construct a neural network. This method allows for the incorporation of physical models into the learning process, improving the interpretability and performance of the network \[[12](http://arxiv.org/abs/1704.03488)\]. Similarly, \[[13](http://arxiv.org/abs/2003.10428)\] introduced a deep unfolding network for image super-resolution that combines the flexibility of model-based methods with the efficiency of learning-based approaches \[[14](https://www.semanticscholar.org/paper/34f25a8704614163c4095b3ee2fc969b60de4698)\].

In addition to unrolling, PnP methods have also been enhanced by incorporating more sophisticated denoisers. For example, \[[15](http://arxiv.org/abs/2207.00698)\] introduced a tuning-free PnP proximal algorithm that automatically determines internal parameters such as the penalty parameter and denoising strength. This approach improves the performance of PnP methods on a variety of inverse imaging problems \[[16](http://arxiv.org/abs/2107.11007)\]. Furthermore, \[[17](http://arxiv.org/abs/1612.02177)\] proposed a method that combines PnP with flow matching, allowing for the efficient use of generative models in image restoration tasks \[[18](http://arxiv.org/abs/1910.03193)\].

In summary, both PnP and unrolling approaches have been widely studied and applied to various imaging problems. While PnP methods offer flexibility for varying CRs, they are limited in accuracy and speed. Unrolling methods, on the other hand, offer better accuracy and speed but require fine-tuning when CR changes. Recent works have sought to integrate the strengths of both approaches, leading to more flexible and efficient solutions for imaging inverse problems \[[19](http://arxiv.org/abs/1704.03264)\].

References  
\[[1](http://arxiv.org/abs/1912.10557)\] http://arxiv.org/abs/1912.10557  
\[[2](http://arxiv.org/abs/1502.03167)\] http://arxiv.org/abs/1502.03167  
\[[3](http://arxiv.org/abs/1902.05399)\] http://arxiv.org/abs/1704.03488  
\[[4](http://arxiv.org/abs/1712.02862)\] http://arxiv.org/abs/1902.05399  
\[[5](http://arxiv.org/abs/2402.12971)\] http://arxiv.org/abs/1712.02862  
\[[6](http://arxiv.org/abs/2109.14025)\] http://arxiv.org/abs/1611.03679  
\[[7](http://arxiv.org/abs/1611.03679)\] http://arxiv.org/abs/1809.04693  
\[[8](http://arxiv.org/abs/1809.04693)\] http://arxiv.org/abs/1508.02848  
\[[9](http://arxiv.org/abs/1508.02848)\] http://arxiv.org/abs/2108.06637  
\[[10](https://www.semanticscholar.org/paper/b954a94af132294a4a4e2efce15027758a535742)\] http://arxiv.org/abs/2201.09375  
\[[11](http://arxiv.org/abs/1902.03493)\] http://arxiv.org/abs/2003.10428  
\[[12](http://arxiv.org/abs/1704.03488)\] http://arxiv.org/abs/1705.08041  
\[[13](http://arxiv.org/abs/2003.10428)\] http://arxiv.org/abs/1612.02177  
\[[14](https://www.semanticscholar.org/paper/34f25a8704614163c4095b3ee2fc969b60de4698)\] http://arxiv.org/abs/1704.03264  
\[[15](http://arxiv.org/abs/2207.00698)\] http://arxiv.org/abs/2012.05703  
\[[16](http://arxiv.org/abs/2107.11007)\] http://arxiv.org/abs/2410.02423  
\[[17](http://arxiv.org/abs/1612.02177)\] http://arxiv.org/abs/1709.01809  
\[[18](http://arxiv.org/abs/1910.03193)\] http://arxiv.org/abs/1502.01852  
\[[19](http://arxiv.org/abs/1704.03264)\] http://arxiv.org/abs/2107.11007
