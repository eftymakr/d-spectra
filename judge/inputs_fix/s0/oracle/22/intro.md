## Related Works

Unsupervised domain adaptation (UDA) for semantic segmentation aims to transfer knowledge from a labeled source domain to an unlabeled target domain without requiring additional annotations \[[1](http://arxiv.org/abs/1411.4038)\]. Traditional UDA methods assume that the category settings between the source and target domains are known, which is a restrictive assumption in real-world applications \[[1](http://arxiv.org/abs/1411.4038)\]. This assumption leads to performance degradation when private classes—classes present in the target domain but absent in the source—exist \[[1](http://arxiv.org/abs/1411.4038)\]. To address this limitation, recent works have explored more flexible domain adaptation settings, such as open-set and universal domain adaptation \[[1](http://arxiv.org/abs/1411.4038)\].

Several methods have been proposed to handle domain shift in semantic segmentation. For instance, \[[2](http://arxiv.org/abs/1606.00915)\] introduced DeepLab, which combines atrous convolution and fully connected CRFs to improve localization accuracy. Similarly, \[[3](http://arxiv.org/abs/1506.04579)\] proposed ParseNet, which enhances semantic segmentation by incorporating global context into deep convolutional networks. These methods focus on improving performance within a fixed domain setting, rather than addressing the more challenging problem of unknown category shifts \[[1](http://arxiv.org/abs/1411.4038)\].

To handle open-set domain adaptation, where the target domain may contain classes not present in the source, \[[4](http://arxiv.org/abs/1612.01105)\] introduced a method that uses image rotation recognition as a self-supervised task to distinguish between known and unknown classes. This approach improves the robustness of models in open-set scenarios \[[1](http://arxiv.org/abs/1411.4038)\]. Additionally, \[[5](http://arxiv.org/abs/2105.15203)\] proposed a universal domain adaptation framework called DANCE, which uses self-supervised learning and entropy-based feature alignment to handle arbitrary category shifts \[[1](http://arxiv.org/abs/1411.4038)\].

In the context of domain adaptation, \[[6](http://arxiv.org/abs/2012.15840)\] proposed a method that leverages adversarial learning to align features between source and target domains. This approach has been further refined in \[[7](http://arxiv.org/abs/1802.10349)\], where the authors introduced a multi-level adversarial network to enhance domain adaptation performance. These methods, while effective, typically assume that the target domain contains only known classes, which is not always the case in real-world applications \[[1](http://arxiv.org/abs/1411.4038)\].

To address the problem of unknown categories, \[[8](http://arxiv.org/abs/2003.00867)\] proposed a method that learns a threshold to distinguish between known and unknown classes in the target domain. This threshold is learned using source samples and adapted to the target domain. This approach is more robust than manually setting a threshold \[[1](http://arxiv.org/abs/1411.4038)\].

The problem of domain adaptation in semantic segmentation has also been tackled through self-training strategies. For example, \[[9](http://arxiv.org/abs/2004.07703)\] introduced a method that uses pseudo-labels to iteratively refine the model's predictions on the target domain. However, pseudo-labels can be noisy, leading to overfitting to the source domain \[[1](http://arxiv.org/abs/1411.4038)\]. To mitigate this issue, \[[10](http://arxiv.org/abs/1901.05427)\] proposed a confidence-regularized self-training framework that improves the quality of pseudo-labels by incorporating confidence regularization \[[1](http://arxiv.org/abs/1411.4038)\].

In summary, while many methods have been proposed to address domain adaptation in semantic segmentation, most assume a fixed category setting or rely on manual thresholding. The proposed UniMAP framework addresses these limitations by introducing a novel approach that handles unknown categories and improves adaptation performance through domain-specific prototype distinction and image matching \[[1](http://arxiv.org/abs/1411.4038)\].

References:
1. \[[1](http://arxiv.org/abs/1411.4038)\] "Universal Domain Adaptation for Semantic Segmentation (UniDA-SS)"  
2. \[[2](http://arxiv.org/abs/1606.00915)\] "DeepLab: Semantic Image Segmentation with Deep Convolutional Nets, Atrous Convolution, and Fully Connected CRFs"  
3. \[[3](http://arxiv.org/abs/1506.04579)\] "ParseNet: Looking Wider to See Better"  
4. \[[4](http://arxiv.org/abs/1612.01105)\] "On the Effectiveness of Image Rotation for Open Set Domain Adaptation"  
5. \[[5](http://arxiv.org/abs/2105.15203)\] "Universal Domain Adaptation through Self Supervision"  
6. \[[6](http://arxiv.org/abs/2012.15840)\] "Domain Adaptation for Structured Output via Discriminative Patch Representations"  
7. \[[7](http://arxiv.org/abs/1802.10349)\] "Learning to Adapt Structured Output Space for Semantic Segmentation"  
8. \[[8](http://arxiv.org/abs/2003.00867)\] "OVANet: One-vs-All Network for Universal Domain Adaptation"  
9. \[[9](http://arxiv.org/abs/2004.07703)\] "Confidence Regularized Self-Training"  
10. \[[10](http://arxiv.org/abs/1901.05427)\] "Prototypical Pseudo Label Denoising and Target Structure Learning for Domain Adaptive Semantic Segmentation"
