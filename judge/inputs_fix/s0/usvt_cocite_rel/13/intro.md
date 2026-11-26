## Related Works

Long-tailed recognition remains a challenging problem in computer vision due to the skewed class distribution in real-world datasets. Several approaches have been proposed to address this issue, primarily focusing on class-balancing strategies, contrastive learning, and decoupling representation and classifier learning. 

Early methods tackled class imbalance by employing re-weighting or re-sampling techniques, such as instance-balanced sampling \[[1](http://arxiv.org/abs/1910.09217)\]. These approaches aimed to mitigate the bias towards majority classes by adjusting the loss function or modifying the training data. However, these methods often led to suboptimal representation learning due to the lack of diversity in the training samples \[[1](http://arxiv.org/abs/1910.09217)\]. 

More recently, contrastive learning has emerged as a promising approach for learning discriminative visual representations. Supervised contrastive learning (SCL) \[[20](http://arxiv.org/abs/2004.11362)\] has shown significant improvements over cross-entropy by pulling together samples from the same class and pushing apart those from different classes. However, SCL struggles with long-tailed data due to the imbalance in gradient contributions from positive and negative pairs \[[20](http://arxiv.org/abs/2004.11362)\]. This issue is further exacerbated by the lack of uniformity in feature distributions for minority classes \[[4](http://arxiv.org/abs/2111.13998)\]. 

To address these limitations, several works have proposed modifications to contrastive learning. Parametric Contrastive Learning (PaCo) \[[3](http://arxiv.org/abs/2107.12028)\] introduces class-wise learnable centers to rebalance the optimization process, improving the representation quality for tail classes. Similarly, Balanced Contrastive Learning (BCL) \[[2](http://arxiv.org/abs/2207.09052)\] addresses the failure of SCL to form a regular simplex by introducing class-averaging and class-complement strategies. These methods aim to improve the uniformity of feature distributions and enhance class separability \[[2](http://arxiv.org/abs/2207.09052)\]. 

Decoupling representation and classifier learning has also been explored as a way to improve long-tailed recognition. The work by \[[1](http://arxiv.org/abs/1910.09217)\] demonstrated that learning high-quality representations is less affected by data imbalance, and that a simple instance-balanced sampling can lead to strong long-tailed recognition performance when combined with an appropriately designed classifier. This idea was further extended in \[[9](http://arxiv.org/abs/1912.02413)\], where a Bilateral-Branch Network (BBN) was proposed to jointly optimize representation and classifier learning, leading to improved performance on benchmark datasets. 

Additionally, the concept of logit adjustment has been introduced to address the bias in classification scores for rare classes \[[15](http://arxiv.org/abs/2007.07314)\]. This approach modifies the logits based on label frequencies, encouraging a larger margin between rare and common classes. Similarly, the Equalization Loss \[[16](http://arxiv.org/abs/2003.05176)\] aims to reduce the gradient bias against rare categories by ignoring gradients for rare classes during training. 

In summary, while contrastive learning has shown great potential for learning robust visual representations, its application to long-tailed data remains challenging. Recent works have attempted to address these issues through various modifications, including class-balancing strategies, decoupling representation and classifier learning, and logit adjustment. These approaches highlight the ongoing efforts to improve long-tailed recognition in real-world scenarios.

References:  
\[[1](http://arxiv.org/abs/1910.09217)\] Decoupling Representation and Classifier for Long-Tailed Recognition  
\[[2](http://arxiv.org/abs/2207.09052)\] Balanced Contrastive Learning for Long-Tailed Visual Recognition  
\[[3](http://arxiv.org/abs/2107.12028)\] Parametric Contrastive Learning  
\[[4](http://arxiv.org/abs/2111.13998)\] Targeted Supervised Contrastive Learning for Long-Tailed Recognition  
\[[15](http://arxiv.org/abs/2007.07314)\] Long-tail learning via logit adjustment  
\[[16](http://arxiv.org/abs/2003.05176)\] Equalization Loss for Long-Tailed Object Recognition  
\[[20](http://arxiv.org/abs/2004.11362)\] Supervised Contrastive Learning
