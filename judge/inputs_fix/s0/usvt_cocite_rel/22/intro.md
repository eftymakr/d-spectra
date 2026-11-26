## Related Works

Unsupervised domain adaptation (UDA) for semantic segmentation has attracted significant research interest due to the high cost of obtaining pixel-level annotations for real-world data \[[1](http://arxiv.org/abs/2004.07703)\]. Traditional UDA methods assume that the category settings between the source and target domains are known \[[2](http://arxiv.org/abs/1909.13589)\], which is often not the case in real-world scenarios. This assumption leads to performance degradation when private classes exist in the target domain \[[3](http://arxiv.org/abs/2007.08702)\]. Several approaches have been proposed to address this issue, including methods that focus on domain alignment, pseudo-label refinement, and class-level adaptation.

Early works in UDA for semantic segmentation primarily relied on adversarial learning to align the feature distributions between domains \[[4](http://arxiv.org/abs/1904.01886)\]. These methods often assume that the class labels are known and that the target domain contains only classes present in the source domain \[[5](http://arxiv.org/abs/1904.10620)\]. However, this assumption is not always valid, especially in cross-domain scenarios where the target domain may contain new or unseen classes \[[6](http://arxiv.org/abs/2004.05498)\]. To address this, some methods have introduced mechanisms to handle unknown classes, such as using pseudo-labels and entropy minimization \[[7](http://arxiv.org/abs/1809.09478)\]. For example, the Maximum Squares Loss (MSL) was proposed to prevent the training process from being dominated by easy-to-transfer samples in the target domain \[[8](http://arxiv.org/abs/2003.03773)\].

Recent approaches have also focused on improving the quality of pseudo-labels, which are crucial for self-training in UDA \[[9](http://arxiv.org/abs/2008.12197)\]. Methods like Rectifying Pseudo Label Learning via Uncertainty Estimation have been proposed to estimate prediction uncertainty during training and use it to refine pseudo-labels \[[10](http://arxiv.org/abs/1910.13049)\]. Similarly, the Prototypical Pseudo Label Denoising and Target Structure Learning method leverages class prototypes to correct noisy pseudo-labels and align target features \[[11](http://arxiv.org/abs/1802.10349)\]. These approaches highlight the importance of pseudo-label refinement in achieving robust domain adaptation.

Another line of research has focused on category-level adaptation, aiming to align features at the class level rather than globally \[[12](https://www.semanticscholar.org/paper/3f9f801aec1f87ae81524f1928407673805927cb)\]. The Category Anchor-Guided UDA model explicitly enforces category-aware feature alignment to learn shared discriminative features and classifiers \[[13](http://arxiv.org/abs/1612.02649)\]. This approach improves the alignment of features for each class, leading to better performance in cross-domain scenarios \[[14](http://arxiv.org/abs/1901.05427)\].

Additionally, methods like Domain Adaptation via Cross-domain Mixed Sampling (DACS) have been proposed to mix images from the source and target domains along with their labels and pseudo-labels, enabling more effective domain adaptation \[[15](http://arxiv.org/abs/1912.08954)\]. Similarly, the DADA method exploits depth information to improve semantic segmentation performance in the target domain \[[16](http://arxiv.org/abs/2101.10979)\].

In summary, while many UDA methods have been proposed for semantic segmentation, the challenge of handling unknown classes and improving pseudo-label quality remains an active research area. The proposed UniMAP framework addresses these challenges by introducing novel components such as Domain-Specific Prototype-based Distinction and Target-based Image Matching \[[17](http://arxiv.org/abs/1811.12833)\].

### References

1. \[[1](http://arxiv.org/abs/2004.07703)\] http://arxiv.org/abs/1909.13589  
2. \[[2](http://arxiv.org/abs/1909.13589)\] http://arxiv.org/abs/1904.01886  
3. \[[3](http://arxiv.org/abs/2007.08702)\] http://arxiv.org/abs/1904.10620  
4. \[[4](http://arxiv.org/abs/1904.01886)\] http://arxiv.org/abs/1809.09478  
5. \[[5](http://arxiv.org/abs/1904.10620)\] http://arxiv.org/abs/1909.13589  
6. \[[6](http://arxiv.org/abs/2004.05498)\] http://arxiv.org/abs/1904.10620  
7. \[[7](http://arxiv.org/abs/1809.09478)\] http://arxiv.org/abs/1909.13589  
8. \[[8](http://arxiv.org/abs/2003.03773)\] http://arxiv.org/abs/1909.13589  
9. \[[9](http://arxiv.org/abs/2008.12197)\] http://arxiv.org/abs/2003.03773  
10. \[[10](http://arxiv.org/abs/1910.13049)\] http://arxiv.org/abs/2101.10979  
11. \[[11](http://arxiv.org/abs/1802.10349)\] http://arxiv.org/abs/1904.10620  
12. \[[12](https://www.semanticscholar.org/paper/3f9f801aec1f87ae81524f1928407673805927cb)\] http://arxiv.org/abs/1910.13049  
13. \[[13](http://arxiv.org/abs/1612.02649)\] http://arxiv.org/abs/1910.13049  
14. \[[14](http://arxiv.org/abs/1901.05427)\] http://arxiv.org/abs/1901.05427  
15. \[[15](http://arxiv.org/abs/1912.08954)\] http://arxiv.org/abs/2007.08702  
16. \[[16](http://arxiv.org/abs/2101.10979)\] http://arxiv.org/abs/1904.01886  
17. \[[17](http://arxiv.org/abs/1811.12833)\] http://arxiv.org/abs/2003.08040
