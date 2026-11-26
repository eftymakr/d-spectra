## Related Works

Long-tailed recognition has been a focal point in recent visual recognition research due to the inherent class imbalance in real-world data \[[1' 2022-07-19](http://arxiv.org/abs/2207.09052v3)\]. This imbalance leads to poor generalization for minority classes, as models tend to prioritize majority classes during training \[[2' 2021-11-27](http://arxiv.org/abs/2111.13998v2)\]. Several approaches have been proposed to address this issue, including data augmentation, loss function modification, and contrastive learning techniques \[[3' 2024-08-01](http://arxiv.org/abs/2408.00483v1)\].

Contrastive learning has emerged as a powerful method for representation learning, particularly in the context of long-tailed recognition \[[4' 2024-03-10](http://arxiv.org/abs/2403.06151v1)\]. Supervised Contrastive Learning (SCL) has shown promising results, but it suffers from issues such as gradient conflicts and imbalanced attraction and repulsion gradients between positive and negative pairs \[[5' 2024-06-04](http://arxiv.org/abs/2406.02223v1)\]. These issues are exacerbated in long-tailed distributions, where the number of samples per class is highly imbalanced \[[6' 2022-12-21](http://arxiv.org/abs/2212.11187v1)\]. To mitigate these problems, researchers have proposed various improvements, such as class-averaging and class-complement strategies to balance the gradient contributions of negative classes \[[7' 2022-11-22](http://arxiv.org/abs/2211.11938v1)\].

Decoupled Contrastive Learning (DSCL) addresses the imbalanced intra-category distance by decoupling the training objective and optimizing the relations of positives toward different objectives \[[8' 2023-09-28](http://arxiv.org/abs/2309.16135v1)\]. This approach also introduces a patch-based self-distillation mechanism to transfer knowledge from head to tail classes, improving the under-representation of tail classes \[[9' 2023-12-05](http://arxiv.org/abs/2312.02517v1)\]. Similarly, Targeted Supervised Contrastive Learning (TSC) improves the uniformity of the feature distribution on the hypersphere by generating targets uniformly distributed on a hypersphere and forcing features of different classes to converge to these targets \[[10' 2021-01-16](http://arxiv.org/abs/2101.06480v1)\].

Another approach, Balanced Contrastive Learning (BCL), introduces class-averaging and class-complement strategies to form a regular simplex, which is ideal for representation learning \[[11' 2023-09-13](http://arxiv.org/abs/2309.07186v1)\]. This method enhances the performance of long-tailed visual recognition by improving the feature representation and class boundaries \[[12' 2024-03-11](http://arxiv.org/abs/2403.06726v2)\]. Additionally, Probabilistic Contrastive Learning (ProCo) estimates the data distribution of samples from each class in the feature space and samples contrastive pairs accordingly, addressing the challenge of constructing contrastive pairs in imbalanced data \[[13' 2020-09-28](http://arxiv.org/abs/2009.12991v5)\].

Theoretical analysis of learning dynamics under class imbalance has also contributed to understanding the challenges in long-tailed recognition \[[14' 2022-07-01](http://arxiv.org/abs/2207.00391v4)\]. This analysis reveals that class imbalance affects the convergence of learning dynamics, particularly with gradient-based optimizers \[[15' 2020-07-23](http://arxiv.org/abs/2007.12229v2)\]. To mitigate these issues, methods such as data augmentation and class uncertainty measures have been proposed to improve the performance of models on imbalanced datasets \[[16' 2023-11-23](http://arxiv.org/abs/2311.14090v2)\].

In summary, the field of long-tailed recognition has seen significant advancements through the integration of contrastive learning with various strategies to address class imbalance. These approaches aim to improve the generalization of models on minority classes and enhance the overall performance of visual recognition systems \[[17' 2020-01-15](http://arxiv.org/abs/2001.05571v2)\].

### References

1. \[[1' 2022-07-19](http://arxiv.org/abs/2207.09052v3)\] http://arxiv.org/abs/2207.09052v3  
2. \[[2' 2021-11-27](http://arxiv.org/abs/2111.13998v2)\] http://arxiv.org/abs/2111.13998v2  
3. \[[3' 2024-08-01](http://arxiv.org/abs/2408.00483v1)\] http://arxiv.org/abs/2403.06151v1  
4. \[[4' 2024-03-10](http://arxiv.org/abs/2403.06151v1)\] http://arxiv.org/abs/2212.11187v1  
5. \[[5' 2024-06-04](http://arxiv.org/abs/2406.02223v1)\] http://arxiv.org/abs/2211.11938v1  
6. \[[6' 2022-12-21](http://arxiv.org/abs/2212.11187v1)\] http://arxiv.org/abs/2309.16135v1  
7. \[[7' 2022-11-22](http://arxiv.org/abs/2211.11938v1)\] http://arxiv.org/abs/2309.07186v1  
8. \[[8' 2023-09-28](http://arxiv.org/abs/2309.16135v1)\] http://arxiv.org/abs/2403.06726v2  
9. \[[9' 2023-12-05](http://arxiv.org/abs/2312.02517v1)\] http://arxiv.org/abs/2009.12991v5  
10. \[[10' 2021-01-16](http://arxiv.org/abs/2101.06480v1)\] http://arxiv.org/abs/2207.00391v4  
11. \[[11' 2023-09-13](http://arxiv.org/abs/2309.07186v1)\] http://arxiv.org/abs/2007.12229v2  
12. \[[12' 2024-03-11](http://arxiv.org/abs/2403.06726v2)\] http://arxiv.org/abs/2311.14090v2  
13. \[[13' 2020-09-28](http://arxiv.org/abs/2009.12991v5)\] http://arxiv.org/abs/2001.05571v2  
14. \[[14' 2022-07-01](http://arxiv.org/abs/2207.00391v4)\] http://arxiv.org/abs/2402.19449v2  
15. \[[15' 2020-07-23](http://arxiv.org/abs/2007.12229v2)\] http://arxiv.org/abs/2008.05524v1  
16. \[[16' 2023-11-23](http://arxiv.org/abs/2311.14090v2)\] http://arxiv.org/abs/2302.09195v5  
17. \[[17' 2020-01-15](http://arxiv.org/abs/2001.05571v2)\] http://arxiv.org/abs/1909.02410v3
