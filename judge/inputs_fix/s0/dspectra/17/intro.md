## Related Works

Semi-supervised learning (SSL) has emerged as a powerful paradigm for improving model performance by leveraging unlabeled data when labeled data is scarce \[[1](http://arxiv.org/abs/2205.07246)\]. Traditional SSL methods, such as FixMatch \[[15](http://arxiv.org/abs/2001.07685)\], assume that both labeled and unlabeled data share the same class distribution \[[1](http://arxiv.org/abs/2205.07246)\]. However, this assumption is often violated in real-world scenarios, where unlabeled data may contain out-of-distribution (OOD) samples, i.e., outliers, that do not belong to any of the known classes \[[26](http://arxiv.org/abs/2412.18256)\]. These outliers are typically treated as noise, which can significantly degrade the performance of SSL models \[[1](http://arxiv.org/abs/2205.07246)\]. 

To address this issue, several open-set SSL methods have been proposed. For example, OpenMatch \[[9](http://arxiv.org/abs/2105.14148)\] introduces a novel framework that combines FixMatch with novelty detection based on one-vs-all (OVA) classifiers. This allows the model to distinguish between inliers and outliers. Similarly, IOMatch \[[5](http://arxiv.org/abs/2308.13168)\] proposes a framework that jointly utilizes inliers and outliers, even when it is difficult to distinguish between them. This approach avoids the performance degradation caused by unreliable outlier detection when labeled data is scarce \[[5](http://arxiv.org/abs/2308.13168)\]. 

Another line of research focuses on improving the robustness of SSL in the presence of class imbalance. For instance, CReST \[[10](http://arxiv.org/abs/2102.09559)\] introduces a class-rebalancing self-training framework that improves existing SSL methods on class-imbalanced data. This is achieved by iteratively expanding the labeled set with pseudo-labeled samples from the unlabeled set, with a focus on minority classes \[[10](http://arxiv.org/abs/2102.09559)\]. Similarly, ABC \[[22](http://arxiv.org/abs/2110.10368)\] proposes an auxiliary balanced classifier to mitigate class imbalance by introducing a single-layer classifier that is trained with a class-balanced loss \[[22](http://arxiv.org/abs/2110.10368)\]. 

Additionally, methods like FreeMatch \[[1](http://arxiv.org/abs/2205.07246)\] and Dash \[[8](http://arxiv.org/abs/2109.00650)\] have been developed to dynamically adjust confidence thresholds during training, which helps in better utilization of unlabeled data. FreeMatch, in particular, introduces a self-adaptive class fairness regularization penalty to encourage diverse predictions during the early training stage \[[1](http://arxiv.org/abs/2205.07246)\]. 

Moreover, contrastive learning has been explored for SSL, with methods like SimCLR \[[29](http://arxiv.org/abs/2002.05709)\] showing that contrastive learning can lead to better visual representations by leveraging data augmentations and learnable transformations \[[29](http://arxiv.org/abs/2002.05709)\]. Contrastive regularization has also been used to improve SSL performance by encouraging features of confident pseudo-labels to aggregate within the same cluster while pushing away features from different clusters \[[17](http://arxiv.org/abs/2201.06247)\]. 

In summary, while traditional SSL methods assume a balanced class distribution, recent advances have addressed the challenges posed by open-set scenarios and class imbalance. These methods either focus on outlier detection, class rebalancing, or dynamic thresholding to improve robustness and performance in more realistic settings \[[1](http://arxiv.org/abs/2205.07246)\]\[[5](http://arxiv.org/abs/2308.13168)\]\[[8](http://arxiv.org/abs/2109.00650)\]\[[9](http://arxiv.org/abs/2105.14148)\]\[[10](http://arxiv.org/abs/2102.09559)\]\[[17](http://arxiv.org/abs/2201.06247)\]\[[22](http://arxiv.org/abs/2110.10368)\]\[[29](http://arxiv.org/abs/2002.05709)\]. 

References  
\[[1](http://arxiv.org/abs/2205.07246)\] FreeMatch: Self-adaptive Thresholding for Semi-supervised Learning  
\[[2](http://arxiv.org/abs/2203.02261)\] Class-Aware Contrastive Semi-Supervised Learning  
\[[3](http://arxiv.org/abs/2107.08943)\] OpenCoS: Contrastive Semi-supervised Learning for Handling Open-set Unlabeled Data  
\[[4](http://arxiv.org/abs/2002.06815)\] Class-Imbalanced Semi-Supervised Learning  
\[[5](http://arxiv.org/abs/2308.13168)\] IOMatch: Simplifying Open-Set Semi-Supervised Learning with Joint Inliers and Outliers Utilization  
\[[6](http://arxiv.org/abs/2007.08844)\] Distribution Aligning Refinery of Pseudo-label for Imbalanced Semi-supervised Learning  
\[[7](http://arxiv.org/abs/2007.11330)\] Multi-Task Curriculum Framework for Open-Set Semi-Supervised Learning  
\[[8](http://arxiv.org/abs/2109.00650)\] Dash: Semi-Supervised Learning with Dynamic Thresholding  
\[[9](http://arxiv.org/abs/2105.14148)\] OpenMatch: Open-set Consistency Regularization for Semi-supervised Learning with Outliers  
\[[10](http://arxiv.org/abs/2102.09559)\] CReST: A Class-Rebalancing Self-Training Framework for Imbalanced Semi-Supervised Learning  
\[[11](http://arxiv.org/abs/2303.11066)\] Boosting Semi-Supervised Learning by Exploiting All Unlabeled Data  
\[[12](http://arxiv.org/abs/2311.10572)\] SSB: Simple but Strong Baseline for Boosting Performance of Open-Set Semi-Supervised Learning  
\[[13](https://www.semanticscholar.org/paper/f3df804a7eef204b0c4fc4b81166dec9b4abc073)\] Semi-Supervised Learning under Class Distribution Mismatch  
\[[14](http://arxiv.org/abs/2101.06329)\] In Defense of Pseudo-Labeling: An Uncertainty-Aware Pseudo-label Selection Framework for Semi-Supervised Learning  
\[[15](http://arxiv.org/abs/2001.07685)\] FixMatch: Simplifying Semi-Supervised Learning with Consistency and Confidence  
\[[16](http://arxiv.org/abs/2108.05617)\] Trash to Treasure: Harvesting OOD Data with Cross-Modal Matching for Open-Set Semi-Supervised Learning  
\[[17](http://arxiv.org/abs/2201.06247)\] Contrastive Regularization for Semi-Supervised Learning  
\[[18](http://arxiv.org/abs/2207.13856)\] Imbalanced Semi-supervised Learning with Bias Adaptive Classifier  
\[[19](http://arxiv.org/abs/2208.07204)\] USB: A Unified Semi-supervised Learning Benchmark  
\[[20](http://arxiv.org/abs/2112.04564)\] CoSSL: Co-Learning of Representation and Classifier for Imbalanced Semi-Supervised Learning  
\[[21](https://www.semanticscholar.org/paper/9e4376e0572de32236e408469ffb2173d89eaab5)\] SAFER-STUDENT for Safe Deep Semi-Supervised Learning With Unseen-Class Unlabeled Data  
\[[22](http://arxiv.org/abs/2110.10368)\] ABC: Auxiliary Balanced Classifier for Class-imbalanced Semi-supervised Learning  
\[[23](http://arxiv.org/abs/2303.12091)\] Adaptive Negative Evidential Deep Learning for Open-set Semi-supervised Learning  
\[[24](http://arxiv.org/abs/1606.04586)\] Regularization With Stochastic Transformations and Perturbations for Deep Semi-Supervised Learning  
\[[25](http://arxiv.org/abs/1711.09325)\] Training Confidence-calibrated Classifiers for Detecting Out-of-Distribution Samples  
\[[26](http://arxiv.org/abs/2412.18256)\] Robust semi-supervised learning in open environments  
\[[27](http://arxiv.org/abs/2310.16412)\] FlatMatch: Bridging Labeled Data and Unlabeled Data with Cross-Sharpness for Semi-Supervised Learning  
\[[28](http://arxiv.org/abs/2211.11086)\] An Embarrassingly Simple Baseline for Imbalanced Semi-Supervised Learning  
\[[29](http://arxiv.org/abs/2002.05709)\] A Simple Framework for Contrastive Learning of Visual Representations
