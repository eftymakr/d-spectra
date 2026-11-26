## Related Works

Long-tailed recognition remains a challenging problem in computer vision due to the significant imbalance in class distribution, where a few dominant classes (head classes) dominate the dataset, while many rare classes (tail classes) contain only a few samples \[[1](http://arxiv.org/abs/2312.01753)\]. This imbalance leads to biased feature learning and poor generalization on tail classes \[[17](http://arxiv.org/abs/1910.09217)\]. Several approaches have been proposed to address this issue, primarily focusing on data augmentation, loss reweighting, and contrastive learning strategies \[[20](http://arxiv.org/abs/2110.04596)\].

Contrastive learning has shown promising results in representation learning by pulling positive samples together and pushing negative samples apart \[[1](http://arxiv.org/abs/2312.01753)\]. However, in long-tailed scenarios, supervised contrastive learning (SCL) tends to bias toward high-frequency classes, exacerbating the imbalance \[[10](http://arxiv.org/abs/2107.12028)\]. This bias is attributed to imbalanced attraction and repulsion gradients between positive and negative pairs, which hinder the model's ability to generalize to tail classes \[[1](http://arxiv.org/abs/2312.01753)\]. To address this, researchers have proposed various modifications, such as decoupling the training objectives for head and tail classes \[[2](http://arxiv.org/abs/2403.06151)\], introducing class frequency-based balancing \[[1](http://arxiv.org/abs/2312.01753)\], and enforcing uniformity in feature space distribution \[[13](http://arxiv.org/abs/2111.13998)\].

One line of work focuses on balancing the feature space by adjusting the loss function or data sampling strategy. For instance, Balanced Contrastive Learning (BCL) introduces class-averaging and class-complement techniques to ensure a regular simplex formation in the feature space, which improves the performance of long-tailed recognition \[[7](http://arxiv.org/abs/2207.09052)\]. Similarly, Rebalanced Contrastive Learning (RCL) addresses class imbalance by enforcing intra-class compactness and larger margins for tail classes \[[1](http://arxiv.org/abs/2312.01753)\]. These methods aim to create a more uniform distribution of features across all classes, improving the model's ability to generalize to underrepresented tail classes.

Another approach involves decoupling the representation learning and classifier balancing processes. For example, Decoupled Contrastive Learning for Long-Tailed Recognition introduces a patch-based self-distillation method to transfer knowledge from head to tail classes, improving the representation of rare classes \[[2](http://arxiv.org/abs/2403.06151)\]. Similarly, the Equalization Loss v2 introduces a gradient-driven training mechanism that dynamically rebalances the positive/negative gradients during training \[[21](http://arxiv.org/abs/2012.08548)\]. These methods aim to reduce the imbalance in gradient contributions, leading to more balanced feature learning.

Additionally, some works focus on improving the generalization of models by incorporating saliency masking or generative models to augment the features of tail classes \[[9](http://arxiv.org/abs/2406.02223)\]\[[25](https://www.semanticscholar.org/paper/7c1cb2db2f311bef3cb312394e53c1d54290ab60)\]. These techniques help mitigate the bias introduced by the imbalanced data distribution and improve the model's ability to learn discriminative features for rare classes.

In summary, the long-tailed recognition problem has been extensively studied, with a variety of approaches targeting different aspects of the imbalance, such as loss design, data augmentation, and gradient balancing. These methods have laid the foundation for the development of more robust and generalizable models for long-tailed recognition.

References  
\[[1](http://arxiv.org/abs/2312.01753)\] Long-Tail Learning with Rebalanced Contrastive Loss  
\[[2](http://arxiv.org/abs/2403.06151)\] Decoupled Contrastive Learning for Long-Tailed Recognition  
\[[7](http://arxiv.org/abs/2207.09052)\] Balanced Contrastive Learning for Long-Tailed Visual Recognition  
\[[9](http://arxiv.org/abs/2406.02223)\] SMCL: Saliency Masked Contrastive Learning for Long-Tailed Visual Recognition  
\[[10](http://arxiv.org/abs/2107.12028)\] Parametric Contrastive Learning  
\[[13](http://arxiv.org/abs/2111.13998)\] Targeted Supervised Contrastive Learning for Long-Tailed Recognition  
\[[17](http://arxiv.org/abs/1910.09217)\] Decoupling Representation and Classifier for Long-Tailed Recognition  
\[[20](http://arxiv.org/abs/2110.04596)\] Deep Long-Tailed Learning: A Survey  
\[[21](http://arxiv.org/abs/2012.08548)\] Equalization Loss v2: A New Gradient Balance Approach for Long-tailed Object Detection
