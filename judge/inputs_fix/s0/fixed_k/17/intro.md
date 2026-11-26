## Related Works

Semi-supervised learning (SSL) has emerged as a powerful paradigm for improving model generalization by leveraging unlabeled data alongside a small set of labeled samples \[[1](http://arxiv.org/abs/2311.10572)\]. However, conventional SSL methods assume that both labeled and unlabeled data share the same class distribution, which is often violated in practice due to the presence of outliers—unlabeled data from unknown classes \[[2](http://arxiv.org/abs/2303.12091)\]. These outliers are typically treated as noise, which significantly degrades SSL performance \[[3](http://arxiv.org/abs/2401.07551)\]. To address this challenge, numerous open-set SSL approaches have been proposed, aiming to distinguish inliers from outliers while maintaining classification accuracy on known classes \[[4](http://arxiv.org/abs/2308.13168)\].

Early methods, such as FixMatch, rely on consistency regularization to ensure that predictions on unlabeled data are consistent with pseudo-labels \[[5](http://arxiv.org/abs/2105.14148)\]. However, these methods often fail when the labeled data is insufficient, as they do not account for the presence of outliers \[[6](http://arxiv.org/abs/2107.08943)\]. In contrast, methods like OpenMatch integrate novelty detection with SSL, using one-vs-all (OVA) classifiers to identify inliers and outliers \[[7](http://arxiv.org/abs/2405.06979)\]. While effective, these approaches still struggle with performance degradation in open-set scenarios due to the limited ability to distinguish between inliers and outliers \[[8](http://arxiv.org/abs/2002.06815)\].

More recently, methods such as SSB and ANEDL have introduced novel strategies to enhance open-set SSL performance. SSB utilizes non-linear transformations to separate features for inlier classification and outlier detection, while ANEDL introduces adaptive negative optimization to improve outlier detection \[[9](http://arxiv.org/abs/2301.10127)\]. These methods demonstrate that incorporating uncertainty quantification and pseudo-label refinement can lead to better performance in open-set settings \[[10](http://arxiv.org/abs/2407.05370)\].

The challenge of handling open-set data has also been addressed in the context of object detection, where methods like OSSOD and IOMatch have been proposed to jointly utilize inliers and outliers during training \[[11](http://arxiv.org/abs/2207.13856)\]. IOMatch, for instance, employs a multi-binary classifier to treat all outliers as a single class, enabling the model to learn from both inliers and outliers simultaneously \[[12](http://arxiv.org/abs/2403.10658)\]. This approach has shown promising results, particularly when labeled data is scarce \[[13](http://arxiv.org/abs/2201.09196)\].

In addition to outlier detection, the issue of class imbalance in SSL has also been explored. Methods like SEVAL and the bias adaptive classifier aim to mitigate the effects of class imbalance by refining pseudo-labels and adjusting thresholds during training \[[14](http://arxiv.org/abs/1711.07476)\]. These approaches highlight the importance of addressing both class imbalance and outlier presence in SSL \[[15](http://arxiv.org/abs/2201.06247)\].

Furthermore, the integration of self-supervision and consistency regularization has been explored in methods such as FreeMatch and contrastive regularization. FreeMatch introduces a self-adaptive thresholding mechanism to improve pseudo-labeling accuracy, while contrastive regularization leverages well-clustered features of unlabeled data to enhance model performance \[[16](http://arxiv.org/abs/2305.13802)\].

In summary, while many open-set SSL methods have been proposed, the challenge of robustly distinguishing inliers from outliers remains a key research direction. Our approach, Diversify and Conquer (DAC), addresses this by leveraging prediction disagreements among multiple models with different biases, offering a novel solution to enhance SSL robustness in open-set scenarios \[[17](http://arxiv.org/abs/2503.17057)\].

References  
\[[1](http://arxiv.org/abs/2311.10572)\] http://arxiv.org/abs/2311.10572  
\[[2](http://arxiv.org/abs/2303.12091)\] http://arxiv.org/abs/2303.12091  
\[[3](http://arxiv.org/abs/2401.07551)\] http://arxiv.org/abs/2401.07551  
\[[4](http://arxiv.org/abs/2308.13168)\] http://arxiv.org/abs/2308.13168  
\[[5](http://arxiv.org/abs/2105.14148)\] http://arxiv.org/abs/2105.14148  
\[[6](http://arxiv.org/abs/2107.08943)\] http://arxiv.org/abs/2107.08943  
\[[7](http://arxiv.org/abs/2405.06979)\] http://arxiv.org/abs/2405.06979  
\[[8](http://arxiv.org/abs/2002.06815)\] http://arxiv.org/abs/2002.06815  
\[[9](http://arxiv.org/abs/2301.10127)\] http://arxiv.org/abs/2301.10127  
\[[10](http://arxiv.org/abs/2407.05370)\] http://arxiv.org/abs/2407.05370  
\[[11](http://arxiv.org/abs/2207.13856)\] http://arxiv.org/abs/2207.13856  
\[[12](http://arxiv.org/abs/2403.10658)\] http://arxiv.org/abs/2403.10658  
\[[13](http://arxiv.org/abs/2201.09196)\] http://arxiv.org/abs/2201.09196  
\[[14](http://arxiv.org/abs/1711.07476)\] http://arxiv.org/abs/1711.07476  
\[[15](http://arxiv.org/abs/2201.06247)\] http://arxiv.org/abs/2201.06247  
\[[16](http://arxiv.org/abs/2305.13802)\] http://arxiv.org/abs/2205.07246  
\[[17](http://arxiv.org/abs/2503.17057)\] http://arxiv.org/abs/2504.20862
