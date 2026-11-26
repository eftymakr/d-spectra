## Related Works

Unsupervised pre-training has emerged as a powerful paradigm for learning general-purpose representations across various domains, including computer vision and natural language processing \[[1](http://arxiv.org/abs/1807.03748)\]. In the context of genomics, recent efforts have explored self-supervised learning approaches to pre-train models on DNA sequences alone \[[2](http://arxiv.org/abs/1805.01978)\]. However, these methods often fail to capture the complex regulatory mechanisms that govern DNA function, such as chromatin accessibility and other genomic profiles \[[3](https://www.semanticscholar.org/paper/4f7d1e04c9d30ce12df3e085d10d70997e6ea1a5)\]. This limitation highlights the need for more informative pre-training strategies that incorporate additional biological signals.

Several studies have investigated the use of contrastive learning for visual and textual representations, demonstrating its effectiveness in learning discriminative features \[[4](http://arxiv.org/abs/1905.09272)\]. Similarly, in the field of genomics, contrastive learning has been applied to learn representations from DNA sequences \[[5](http://arxiv.org/abs/2006.10029)\]. However, these approaches typically focus on sequence-level information and neglect the multi-profile and multi-species nature of genomic data \[[6](http://arxiv.org/abs/1907.11692)\]. 

To address this gap, researchers have proposed methods that integrate multiple genomic profiles during pre-training. For example, \[[7](http://arxiv.org/abs/1206.5538)\] introduced a framework that leverages non-parametric instance discrimination to learn features that capture apparent similarity among instances, rather than classes. This approach has shown promising results in image classification tasks \[[8](http://arxiv.org/abs/2011.09157)\]. Similarly, \[[9](http://arxiv.org/abs/2002.05709)\] proposed a method that uses a probabilistic contrastive loss to induce latent spaces that capture information useful for predicting future samples, demonstrating strong performance across multiple domains \[[10](https://www.semanticscholar.org/paper/9d7af049cf76892dc1b5126c5a51cd09e08e3b5d)\].

In the context of self-supervised learning for visual representations, \[[11](http://arxiv.org/abs/2005.04966)\] introduced SimCLR, a simple framework that achieves state-of-the-art results by leveraging data augmentation and a learnable nonlinear transformation \[[12](http://arxiv.org/abs/2003.04297)\]. This work highlights the importance of carefully designed pretext tasks and the potential of contrastive learning for representation learning \[[13](https://www.semanticscholar.org/paper/06778d3e840c40cd65d41e5096d3156febcb5311)\]. 

Furthermore, \[[14](http://arxiv.org/abs/1505.07818)\] proposed a method that uses momentum contrast to learn visual representations, demonstrating that dynamic dictionaries and moving-averaged encoders can significantly improve performance \[[15](http://arxiv.org/abs/2004.11362)\]. This approach has been successfully applied to downstream tasks such as object detection and segmentation \[[16](http://arxiv.org/abs/2205.13769)\].

In the domain of genomics, \[[17](http://arxiv.org/abs/1202.5211)\] explored the use of semantic-aware dense representation learning for remote sensing image change detection, demonstrating that incorporating semantic information during pretraining can improve the performance of downstream tasks \[[18](http://arxiv.org/abs/1609.08663)\]. This work highlights the potential of incorporating domain-specific knowledge into pre-training strategies \[[19](http://arxiv.org/abs/2208.02252)\].

Finally, \[[20](http://arxiv.org/abs/2203.06041)\] introduced a self-supervised contrastive pre-training method for dense land cover classification, demonstrating that leveraging the large availability of satellite imagery can significantly improve performance on downstream tasks \[[21](http://arxiv.org/abs/1711.05415)\]. This work underscores the importance of developing flexible and effective pre-training strategies that can be applied across diverse domains \[[22](http://arxiv.org/abs/1512.03385)\].

In summary, while unsupervised pre-training has shown promise in various domains, the integration of genomic profiles and multi-species information remains a critical challenge. Our work builds upon these prior efforts, introducing a novel approach that leverages supervised training for genomic profile prediction to achieve more effective DNA representations \[[23](http://arxiv.org/abs/1911.05722)\].

1. \[[1](http://arxiv.org/abs/1807.03748)\] http://arxiv.org/abs/1807.03748  
2. \[[2](http://arxiv.org/abs/1805.01978)\] http://arxiv.org/abs/1905.09272  
3. \[[3](https://www.semanticscholar.org/paper/4f7d1e04c9d30ce12df3e085d10d70997e6ea1a5)\] http://arxiv.org/abs/2006.10029  
4. \[[4](http://arxiv.org/abs/1905.09272)\] http://arxiv.org/abs/2002.05709  
5. \[[5](http://arxiv.org/abs/2006.10029)\] http://arxiv.org/abs/1911.05722  
6. \[[6](http://arxiv.org/abs/1907.11692)\] http://arxiv.org/abs/2003.04297  
7. \[[7](http://arxiv.org/abs/1206.5538)\] http://arxiv.org/abs/1805.01978  
8. \[[8](http://arxiv.org/abs/2011.09157)\] http://arxiv.org/abs/1807.03748  
9. \[[9](http://arxiv.org/abs/2002.05709)\] http://arxiv.org/abs/2004.11362  
10. \[[10](https://www.semanticscholar.org/paper/9d7af049cf76892dc1b5126c5a51cd09e08e3b5d)\] http://arxiv.org/abs/1807.03748  
11. \[[11](http://arxiv.org/abs/2005.04966)\] http://arxiv.org/abs/2002.05709  
12. \[[12](http://arxiv.org/abs/2003.04297)\] http://arxiv.org/abs/2003.04297  
13. \[[13](https://www.semanticscholar.org/paper/06778d3e840c40cd65d41e5096d3156febcb5311)\] http://arxiv.org/abs/1807.03748  
14. \[[14](http://arxiv.org/abs/1505.07818)\] http://arxiv.org/abs/1911.05722  
15. \[[15](http://arxiv.org/abs/2004.11362)\] http://arxiv.org/abs/2003.04297  
16. \[[16](http://arxiv.org/abs/2205.13769)\] http://arxiv.org/abs/1911.05722  
17. \[[17](http://arxiv.org/abs/1202.5211)\] http://arxiv.org/abs/2205.13769  
18. \[[18](http://arxiv.org/abs/1609.08663)\] http://arxiv.org/abs/2208.02252  
19. \[[19](http://arxiv.org/abs/2208.02252)\] http://arxiv.org/abs/2203.06041  
20. \[[20](http://arxiv.org/abs/2203.06041)\] http://arxiv.org/abs/1711.05415  
21. \[[21](http://arxiv.org/abs/1711.05415)\] http://arxiv.org/abs/1512.03385  
22. \[[22](http://arxiv.org/abs/1512.03385)\] http://arxiv.org/abs/1911.05722  
23. \[[23](http://arxiv.org/abs/1911.05722)\] http://arxiv.org/abs/2502.03499
