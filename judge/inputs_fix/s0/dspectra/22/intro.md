## Related Works

Unsupervised domain adaptation (UDA) for semantic segmentation has attracted significant research interest due to the high cost of obtaining pixel-level annotations for real-world data \[[1](https://www.semanticscholar.org/paper/5f9ce93f82dcd9b0f9ffe4274b81682f40d86253)\]. Traditional UDA methods assume that the category settings between the source and target domains are known, which limits their applicability in real-world scenarios where private classes may exist \[[2](http://arxiv.org/abs/2308.05493)\]. This assumption leads to performance degradation when the target domain contains classes not present in the source domain \[[3](https://www.semanticscholar.org/paper/6518b0e6334c6ffb9b94c551c57ad79c7008cbb5)\]. To address this limitation, several works have explored domain adaptation without prior knowledge of category settings.

One line of research focuses on domain adaptation with no access to source domain data, referred to as source-free domain adaptation \[[4](http://arxiv.org/abs/1910.13049)\]. This is particularly relevant in scenarios where data sharing is restricted due to privacy or intellectual property concerns \[[5](http://arxiv.org/abs/2007.08702)\]. For instance, \[[6](http://arxiv.org/abs/2103.16372)\] proposes a framework that recovers source domain knowledge from a pre-trained model and distills valuable information from the target domain for self-supervised learning. This approach enables adaptation without requiring source domain data, making it suitable for privacy-sensitive applications.

Another approach, called universal domain adaptation (UniDA), aims to adapt models to target domains with unknown label sets \[[7](http://arxiv.org/abs/2111.14887)\]. This is especially important in real-world settings where the target domain may contain classes not present in the source domain. \[[8](http://arxiv.org/abs/2012.12545)\] introduces a novel framework that classifies target samples correctly if they belong to the common label set or marks them as "unknown" otherwise. This approach is designed to handle the additional category gap caused by the difference in label sets between domains.

To improve the generalization of models across domains, several methods focus on aligning features between the source and target domains \[[9](http://arxiv.org/abs/1904.01886)\]. For example, \[[10](https://www.semanticscholar.org/paper/28ef938aaa312d76df988f636e248a6b267b6352)\] proposes a method that leverages the knowledge of dense depth in the source domain to improve the performance of semantic segmentation on the target domain. This approach is particularly effective in scenarios where depth information is available in both domains.

In addition to feature alignment, some methods focus on improving the quality of pseudo-labels generated during self-training \[[11](http://arxiv.org/abs/2211.07609)\]. \[[12](http://arxiv.org/abs/2004.08878)\] introduces an uncertainty-aware consistency regularization method that exploits the latent uncertainty information of the target samples to transfer more meaningful knowledge from the teacher model to the student model. This approach improves the performance of semantic segmentation in cross-domain settings.

Furthermore, \[[13](http://arxiv.org/abs/2110.11062)\] proposes a framework that explicitly models what is unique to each domain to improve the ability to extract domain-invariant features. This is achieved by partitioning image representations into two subspaces: one private to each domain and one shared across domains. This approach is particularly useful in scenarios where the source and target domains have significant differences in their data distributions.

In summary, while traditional UDA methods assume known category settings, recent works have explored more flexible approaches that can handle unknown label sets and private classes. These methods include source-free domain adaptation, universal domain adaptation, and feature alignment techniques that improve the generalization of models across domains.

References  
\[[1](https://www.semanticscholar.org/paper/5f9ce93f82dcd9b0f9ffe4274b81682f40d86253)\] https://www.semanticscholar.org/paper/5f9ce93f82dcd9b0f9ffe4274b81682f40d86253  
\[[2](http://arxiv.org/abs/2308.05493)\] https://www.semanticscholar.org/paper/6518b0e6334c6ffb9b94c551c57ad79c7008cbb5  
\[[3](https://www.semanticscholar.org/paper/6518b0e6334c6ffb9b94c551c57ad79c7008cbb5)\] https://www.semanticscholar.org/paper/92443e8b7ae6c295b271ec36b34da2983b194b21  
\[[4](http://arxiv.org/abs/1910.13049)\] http://arxiv.org/abs/2103.16372  
\[[5](http://arxiv.org/abs/2007.08702)\] http://arxiv.org/abs/2103.16372  
\[[6](http://arxiv.org/abs/2103.16372)\] http://arxiv.org/abs/2103.16372  
\[[7](http://arxiv.org/abs/2111.14887)\] https://www.semanticscholar.org/paper/a2e433da83c6e1eb4f4486c900fdfbf1951c4d30  
\[[8](http://arxiv.org/abs/2012.12545)\] https://www.semanticscholar.org/paper/a2e433da83c6e1eb4f4486c900fdfbf1951c4d30  
\[[9](http://arxiv.org/abs/1904.01886)\] http://arxiv.org/abs/1910.13049  
\[[10](https://www.semanticscholar.org/paper/28ef938aaa312d76df988f636e248a6b267b6352)\] http://arxiv.org/abs/2104.13613  
\[[11](http://arxiv.org/abs/2211.07609)\] http://arxiv.org/abs/2004.08878  
\[[12](http://arxiv.org/abs/2004.08878)\] http://arxiv.org/abs/2004.08878  
\[[13](http://arxiv.org/abs/2110.11062)\] http://arxiv.org/abs/1904.01886
