## Related Works

Long-tailed recognition remains a challenging problem in visual recognition due to the skewed class distribution in real-world datasets \[[1](http://arxiv.org/abs/1910.09217)\]. Many existing methods have attempted to address this issue by either balancing the data, the loss, or the classifier \[[2](http://arxiv.org/abs/2107.12028)\]. For instance, class-balancing strategies such as loss re-weighting, data re-sampling, or transfer learning from head to tail classes have been widely explored \[[1](http://arxiv.org/abs/1910.09217)\]. However, these approaches often follow a joint learning scheme of representation and classification, which may not be optimal for long-tailed data \[[1](http://arxiv.org/abs/1910.09217)\].

Recent work has focused on contrastive learning as a promising approach to improve representation learning for long-tailed recognition. Supervised contrastive learning (SCL) has shown significant performance gains by pulling samples from the same class together and pushing apart samples from different classes in the embedding space \[[16](http://arxiv.org/abs/2004.11362)\]. However, SCL tends to bias toward high-frequency classes, increasing the difficulty of imbalanced learning \[[2](http://arxiv.org/abs/2107.12028)\]. This bias is exacerbated by the long-tailed distribution of real-world data, where a few majority classes dominate the training process \[[4](http://arxiv.org/abs/2111.13998)\].

To address this issue, several methods have been proposed. Parametric Contrastive Learning (PaCo) introduces class-wise learnable centers to rebalance the optimization process and adaptively enhance the intensity of pushing samples toward their corresponding centers \[[2](http://arxiv.org/abs/2107.12028)\]. Balanced Contrastive Learning (BCL) further improves upon SCL by introducing class-averaging and class-complement strategies to ensure a regular simplex formation in the embedding space \[[3](http://arxiv.org/abs/2207.09052)\]. Targeted Supervised Contrastive Learning (TSC) improves the uniformity of the feature distribution on the hypersphere by generating targets uniformly distributed on a hypersphere and aligning features with these targets \[[4](http://arxiv.org/abs/2111.13998)\].

In addition to contrastive learning, other approaches have explored the use of class-balanced losses and weight balancing techniques. The Class-Balanced Loss based on the effective number of samples has been proposed to re-balance the loss by considering the impact of sample overlap \[[19](http://arxiv.org/abs/1901.05555)\]. Weight balancing techniques such as L2-normalization, weight decay, and MaxNorm have also been investigated to reduce the bias of models toward common classes \[[9](http://arxiv.org/abs/2203.14197)\]. These methods aim to improve the generalization of models on tail classes while maintaining performance on head classes \[[9](http://arxiv.org/abs/2203.14197)\].

Furthermore, methods such as BBN and ResLT have focused on decoupling representation learning and classifier learning to improve performance on long-tailed data \[[1](http://arxiv.org/abs/1910.09217)\]. BBN introduces a bilateral-branch network with a cumulative learning strategy to simultaneously handle representation and classifier learning \[[1](http://arxiv.org/abs/1910.09217)\]. ResLT proposes a residual learning approach that preserves specific capacity for low-frequency classes \[[14](http://arxiv.org/abs/2101.10633)\].

In summary, while many approaches have been proposed to address the long-tailed recognition problem, the challenge remains in achieving a balance between representation learning and classifier learning while maintaining performance on both head and tail classes. Our proposed Aligned Contrastive Learning (ACL) algorithm builds upon these prior works by addressing the underlying issues of gradient conflicts and imbalanced attraction and repulsion gradients in SCL \[[1](http://arxiv.org/abs/1910.09217)\].

1. Decoupling Representation and Classifier for Long-Tailed Recognition \[[1](http://arxiv.org/abs/1910.09217)\]  
2. Parametric Contrastive Learning for Long-Tailed Recognition \[[2](http://arxiv.org/abs/2107.12028)\]  
3. Balanced Contrastive Learning for Long-Tailed Visual Recognition \[[3](http://arxiv.org/abs/2207.09052)\]  
4. Targeted Supervised Contrastive Learning for Long-Tailed Recognition \[[4](http://arxiv.org/abs/2111.13998)\]  
5. Large-Scale Long-Tailed Recognition in an Open World \[[5](http://arxiv.org/abs/1904.05160)\]  
6. A Simple Framework for Contrastive Learning of Visual Representations \[[6](http://arxiv.org/abs/2002.05709)\]  
7. BBN: Bilateral-Branch Network With Cumulative Learning for Long-Tailed Visual Recognition \[[7](http://arxiv.org/abs/1912.02413)\]  
8. Contrastive Learning based Hybrid Networks for Long-Tailed Image Classification \[[8](http://arxiv.org/abs/2103.14267)\]  
9. Long-Tailed Recognition via Weight Balancing \[[9](http://arxiv.org/abs/2203.14197)\]  
10. Long-tailed Recognition by Routing Diverse Distribution-Aware Experts \[[10](http://arxiv.org/abs/2010.01809)\]  
11. Distribution Alignment: A Unified Framework for Long-tail Visual Recognition \[[11](http://arxiv.org/abs/2103.16370)\]  
12. Balanced Meta-Softmax for Long-Tailed Visual Recognition \[[12](http://arxiv.org/abs/2007.10740)\]  
13. Improving Calibration for Long-Tailed Recognition \[[13](http://arxiv.org/abs/2104.00466)\]  
14. ResLT: Residual Learning for Long-Tailed Recognition \[[14](http://arxiv.org/abs/2101.10633)\]  
15. Long-tail learning via logit adjustment \[[15](http://arxiv.org/abs/2007.07314)\]  
16. Supervised Contrastive Learning \[[16](http://arxiv.org/abs/2004.11362)\]  
17. Self-Supervised Aggregation of Diverse Experts for Test-Agnostic Long-Tailed Recognition \[[17](http://arxiv.org/abs/2107.09249)\]  
18. Disentangling Label Distribution for Long-tailed Visual Recognition \[[18](http://arxiv.org/abs/2012.00321)\]  
19. Class-Balanced Loss Based on Effective Number of Samples \[[19](http://arxiv.org/abs/1901.05555)\]  
20. Prototypical Contrastive Learning of Unsupervised Representations \[[20](http://arxiv.org/abs/2005.04966)\]  
21. Deep Long-Tailed Learning: A Survey \[[21](http://arxiv.org/abs/2110.04596)\]  
22. Learning Imbalanced Datasets with Label-Distribution-Aware Margin Loss \[[22](http://arxiv.org/abs/1906.07413)\]  
23. Momentum Contrast for Unsupervised Visual Representation Learning \[[23](http://arxiv.org/abs/1911.05722)\]  
24. Unequal-Training for Deep Face Recognition With Long-Tailed Noisy Data \[[24](https://www.semanticscholar.org/paper/e2e5093f8164b3c3bb5ac0d223c2100e9f334f6c)\]  
25. Exploring Classification Equilibrium in Long-Tailed Object Detection \[[25](http://arxiv.org/abs/2108.07507)\]  
26. Distributional Robustness Loss for Long-tail Learning \[[26](http://arxiv.org/abs/2104.03066)\]
