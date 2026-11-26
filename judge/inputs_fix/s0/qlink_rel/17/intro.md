## Related Works

Semi-supervised learning (SSL) has emerged as a powerful paradigm for improving model performance when labeled data is scarce. Traditional SSL methods assume that labeled and unlabeled data share the same class distribution \[[1](https://www.semanticscholar.org/paper/f3df804a7eef204b0c4fc4b81166dec9b4abc073)\]. However, this assumption is often violated in practice, as unlabeled data may contain out-of-distribution (OOD) samples, or outliers, which can significantly degrade model performance \[[2](http://arxiv.org/abs/2001.07685)\]. Several recent works have addressed this challenge by focusing on open-set SSL, where the presence of OOD samples is explicitly considered \[[3](http://arxiv.org/abs/2007.11330)\].

Early approaches to SSL, such as Temporal Ensembling \[[4](http://arxiv.org/abs/2105.14148)\], utilized self-ensembling to improve consistency across different training epochs. While effective, these methods typically assume that all unlabeled data belongs to the same class distribution as the labeled data \[[5](http://arxiv.org/abs/1905.02249)\]. This limitation becomes critical when unlabeled data contains OOD samples, which are often treated as noise \[[6](http://arxiv.org/abs/2109.00650)\].

To handle open-set scenarios, methods like FixMatch \[[7](http://arxiv.org/abs/2108.05617)\] and MixMatch \[[8](http://arxiv.org/abs/1610.02242)\] have been proposed. FixMatch introduces pseudo-labeling with confidence thresholds, while MixMatch combines pseudo-labeling with mixup augmentation to improve performance. However, these methods still assume that unlabeled data is from the same class distribution as the labeled data \[[9](http://arxiv.org/abs/1606.04586)\]. This assumption is not valid in open-set settings where OOD samples are present \[[10](http://arxiv.org/abs/2205.07246)\].

More recent works have focused on explicitly handling OOD samples. For example, OpenMatch \[[11](http://arxiv.org/abs/2102.03526)\] integrates novelty detection with consistency regularization to identify and reject outliers. Similarly, OpenCoS \[[12](https://www.semanticscholar.org/paper/9e4376e0572de32236e408469ffb2173d89eaab5)\] uses contrastive learning to identify OOD samples in unlabeled data, improving robustness to outliers. These methods demonstrate that OOD detection is essential for robust open-set SSL \[[13](http://arxiv.org/abs/1904.12848)\].

Another line of research, such as CoMatch \[[14](http://arxiv.org/abs/2107.08943)\], has explored contrastive graph regularization to improve pseudo-label quality and model generalization. These methods aim to improve the robustness of SSL to OOD samples by leveraging contrastive learning and graph-based regularization \[[15](http://arxiv.org/abs/2110.08263)\].

The problem of class distribution mismatch between labeled and unlabeled data has also been addressed in works like UASD \[[16](http://arxiv.org/abs/2308.13168)\], which introduces uncertainty-aware self-distillation to avoid error propagation from irrelevant samples. Similarly, the work in \[[17](http://arxiv.org/abs/1704.03976)\] proposes a multi-task curriculum framework that jointly trains an OOD detector and SSL model, improving performance in the presence of OOD samples \[[18](http://arxiv.org/abs/2203.02261)\].

In addition, methods like FreeMatch \[[19](http://arxiv.org/abs/2007.08844)\] and FlexMatch \[[20](http://arxiv.org/abs/2311.10572)\] have introduced adaptive thresholding mechanisms to improve pseudo-labeling accuracy, particularly in scenarios with limited labeled data. These approaches demonstrate the importance of dynamically adjusting thresholds to improve SSL performance in open-set settings \[[21](https://www.semanticscholar.org/paper/67f8f7fd1b8fea0214b032f94209650a73afece6)\].

Finally, methods such as SSB \[[22](http://arxiv.org/abs/2011.13529)\] and IOMatch \[[23](https://www.semanticscholar.org/paper/3448e3c55cf3b1f25aab4719eb094a95dbe7f05e)\] have explored the joint utilization of inliers and outliers in open-set SSL. These methods demonstrate that leveraging both types of data can improve performance, even when distinguishing between them is challenging \[[24](http://arxiv.org/abs/2011.11183)\].

In summary, while traditional SSL methods assume a closed-set scenario, recent works have focused on open-set SSL, where OOD samples are explicitly considered. These methods employ a variety of techniques, including OOD detection, pseudo-labeling, and contrastive learning, to improve robustness in the presence of outliers \[[25](http://arxiv.org/abs/2208.07204)\].

References  
\[[1](https://www.semanticscholar.org/paper/f3df804a7eef204b0c4fc4b81166dec9b4abc073)\] https://www.semanticscholar.org/paper/f3df804a7eef204b0c4fc4b81166dec9b4abc073  
\[[2](http://arxiv.org/abs/2001.07685)\] https://www.semanticscholar.org/paper/9e4376e0572de32236e408469ffb2173d89eaab5  
\[[3](http://arxiv.org/abs/2007.11330)\] https://www.semanticscholar.org/paper/67f8f7fd1b8fea0214b032f94209650a73afece6  
\[[4](http://arxiv.org/abs/2105.14148)\] http://arxiv.org/abs/1610.02242  
\[[5](http://arxiv.org/abs/1905.02249)\] http://arxiv.org/abs/1606.04586  
\[[6](http://arxiv.org/abs/2109.00650)\] http://arxiv.org/abs/1904.12848  
\[[7](http://arxiv.org/abs/2108.05617)\] http://arxiv.org/abs/2001.07685  
\[[8](http://arxiv.org/abs/1610.02242)\] http://arxiv.org/abs/1905.02249  
\[[9](http://arxiv.org/abs/1606.04586)\] http://arxiv.org/abs/2007.11330  
\[[10](http://arxiv.org/abs/2205.07246)\] http://arxiv.org/abs/2105.14148  
\[[11](http://arxiv.org/abs/2102.03526)\] http://arxiv.org/abs/2107.08943  
\[[12](https://www.semanticscholar.org/paper/9e4376e0572de32236e408469ffb2173d89eaab5)\] http://arxiv.org/abs/2110.08263  
\[[13](http://arxiv.org/abs/1904.12848)\] http://arxiv.org/abs/2203.02261  
\[[14](http://arxiv.org/abs/2107.08943)\] http://arxiv.org/abs/2007.08844  
\[[15](http://arxiv.org/abs/2110.08263)\] http://arxiv.org/abs/2311.10572  
\[[16](http://arxiv.org/abs/2308.13168)\] http://arxiv.org/abs/2011.13529  
\[[17](http://arxiv.org/abs/1704.03976)\] http://arxiv.org/abs/2308.13168  
\[[18](http://arxiv.org/abs/2203.02261)\] http://arxiv.org/abs/2203.02261  
\[[19](http://arxiv.org/abs/2007.08844)\] http://arxiv.org/abs/2110.08263  
\[[20](http://arxiv.org/abs/2311.10572)\] http://arxiv.org/abs/2102.03526  
\[[21](https://www.semanticscholar.org/paper/67f8f7fd1b8fea0214b032f94209650a73afece6)\] http://arxiv.org/abs/2203.02261  
\[[22](http://arxiv.org/abs/2011.13529)\] http://arxiv.org/abs/2308.13168  
\[[23](https://www.semanticscholar.org/paper/3448e3c55cf3b1f25aab4719eb094a95dbe7f05e)\] http://arxiv.org/abs/2108.05617  
\[[24](http://arxiv.org/abs/2011.11183)\] http://arxiv.org/abs/2107.08943  
\[[25](http://arxiv.org/abs/2208.07204)\] http://arxiv.org/abs/2208.07204
