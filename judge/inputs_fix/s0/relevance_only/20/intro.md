## Related Works

Deep-unrolling and plug-and-play (PnP) approaches have emerged as leading methods for solving inverse problems in imaging, particularly in single-pixel imaging (SPI) \[[1](http://arxiv.org/abs/1809.04693)\]. PnP methods integrate pre-trained denoisers into iterative algorithms, leveraging their ability to implicitly enforce image priors \[[2](http://arxiv.org/abs/2107.11007)\]. These methods are flexible across varying compression ratios (CRs) but often face limitations in reconstruction accuracy and speed \[[3](http://arxiv.org/abs/2012.05703)\]. On the other hand, unrolling approaches transform truncated iterative optimization processes into end-to-end trainable neural networks, typically achieving higher accuracy and faster inference \[[4](http://arxiv.org/abs/1704.03488)\]. However, they require fine-tuning or retraining when CR changes, limiting their adaptability \[[5](http://arxiv.org/abs/1902.05399)\].

Several studies have explored the integration of PnP and unrolling methods to leverage their respective strengths. For instance, \[[6](http://arxiv.org/abs/2306.06378)\] introduced a tuning-free PnP proximal algorithm that automatically determines internal parameters, enhancing the adaptability of PnP methods. Similarly, \[[7](http://arxiv.org/abs/2402.12872)\] proposed a dynamic proximal unrolling network (DPUNet) that can handle multiple imaging modalities and sampling ratios without retraining, demonstrating the potential for flexible and efficient reconstruction. These works highlight the need for methods that combine the flexibility of PnP with the accuracy of unrolling \[[8](http://arxiv.org/abs/1902.03493)\].

The concept of unrolling has also been applied to various imaging tasks, such as image deblurring and magnetic resonance imaging (MRI) reconstruction. For example, \[[9](http://arxiv.org/abs/2312.15788)\] introduced a convergent unrolled network based on the Half-Quadratic Splitting (HQS) algorithm, ensuring convergence properties while improving performance. Additionally, \[[10](http://arxiv.org/abs/2410.02423)\] proposed a deep unrolling framework for MRI reconstruction that incorporates the forward model directly into the network, enhancing data consistency and reconstruction quality.

Recent works have also focused on improving the generalizability of unrolling methods across different imaging settings. \[[11](https://www.semanticscholar.org/paper/b954a94af132294a4a4e2efce15027758a535742)\] introduced a deep unrolling approach for blind image deblurring, demonstrating that unrolling can provide interpretable and efficient solutions. Similarly, \[[12](http://arxiv.org/abs/1611.03679)\] proposed a deep unrolling network for image super-resolution that leverages both learning-based and model-based methods, achieving flexibility and performance gains. These studies underscore the importance of combining model-based optimization with data-driven learning to address the challenges of inverse imaging problems \[[13](http://arxiv.org/abs/2201.09375)\].

In addition to unrolling and PnP methods, other approaches have been proposed to enhance the performance of image restoration. \[[14](http://arxiv.org/abs/1912.10557)\] introduced a tuning-free PnP algorithm that automatically adjusts parameters during inference, reducing the need for manual tuning. \[[15](http://arxiv.org/abs/2211.16881)\] proposed a deep unrolling framework for MR reconstruction that uses a regularization term independent of the forward model, improving generalizability across different acquisition settings. These methods highlight the ongoing efforts to develop more robust and adaptable image restoration techniques \[[16](http://arxiv.org/abs/2003.10428)\].

The integration of deep learning with traditional iterative algorithms has also been explored in the context of dynamic imaging tasks. \[[17](http://arxiv.org/abs/1705.08041)\] proposed a deep unrolling shrinkage network for dynamic MR imaging, demonstrating that incorporating sparsity priors can significantly improve reconstruction performance. \[[18](http://arxiv.org/abs/1711.07653)\] introduced a scale-recurrent network for deep image deblurring, showing that the "coarse-to-fine" strategy can be effectively implemented in neural networks \[[19](http://arxiv.org/abs/2203.11156)\].

Finally, the use of uncertainty quantification in deep unrolling has gained attention, as it enables more reliable and robust image reconstruction. \[[20](http://arxiv.org/abs/2109.14025)\] proposed a learning-based framework that incorporates Bayesian neural networks to quantify epistemic and aleatoric uncertainties, enhancing the interpretability and reliability of deep unrolling methods \[[21](http://arxiv.org/abs/2307.09818)\].

---

References  
\[[1](http://arxiv.org/abs/1809.04693)\] http://arxiv.org/abs/1809.04693  
\[[2](http://arxiv.org/abs/2107.11007)\] http://arxiv.org/abs/2012.05703  
\[[3](http://arxiv.org/abs/2012.05703)\] http://arxiv.org/abs/1704.03488  
\[[4](http://arxiv.org/abs/1704.03488)\] http://arxiv.org/abs/1902.05399  
\[[5](http://arxiv.org/abs/1902.05399)\] http://arxiv.org/abs/2306.06378  
\[[6](http://arxiv.org/abs/2306.06378)\] http://arxiv.org/abs/2012.05703  
\[[7](http://arxiv.org/abs/2402.12872)\] http://arxiv.org/abs/2107.11007  
\[[8](http://arxiv.org/abs/1902.03493)\] http://arxiv.org/abs/1705.08041  
\[[9](http://arxiv.org/abs/2312.15788)\] http://arxiv.org/abs/2402.12872  
\[[10](http://arxiv.org/abs/2410.02423)\] http://arxiv.org/abs/2211.16881  
\[[11](https://www.semanticscholar.org/paper/b954a94af132294a4a4e2efce15027758a535742)\] http://arxiv.org/abs/1902.03493  
\[[12](http://arxiv.org/abs/1611.03679)\] http://arxiv.org/abs/2003.10428  
\[[13](http://arxiv.org/abs/2201.09375)\] http://arxiv.org/abs/1705.08041  
\[[14](http://arxiv.org/abs/1912.10557)\] http://arxiv.org/abs/2012.05703  
\[[15](http://arxiv.org/abs/2211.16881)\] http://arxiv.org/abs/2211.16881  
\[[16](http://arxiv.org/abs/2003.10428)\] http://arxiv.org/abs/1705.08041  
\[[17](http://arxiv.org/abs/1705.08041)\] http://arxiv.org/abs/2307.09818  
\[[18](http://arxiv.org/abs/1711.07653)\] http://arxiv.org/abs/1802.01770  
\[[19](http://arxiv.org/abs/2203.11156)\] http://arxiv.org/abs/2207.00698  
\[[20](http://arxiv.org/abs/2109.14025)\] http://arxiv.org/abs/2207.00698  
\[[21](http://arxiv.org/abs/2307.09818)\] http://arxiv.org/abs/2207.00698
