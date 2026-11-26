## Related Works

Fairness in re-ranking has garnered significant attention as recommender systems increasingly influence critical domains such as employment and housing \[[1](http://arxiv.org/abs/2005.12974)\]. Prior work has identified a trade-off between ranking accuracy and item fairness, highlighting the need for a more nuanced understanding of these interactions \[[2](http://arxiv.org/abs/1704.06840)\]. This trade-off is often framed in terms of a cost passed on to users, similar to economic principles where commodity taxes on suppliers translate into user-side costs \[[3](http://arxiv.org/abs/1703.09207)\]. The concept of elasticity, which quantifies how changes in one variable affect another, has been proposed as a framework to analyze the fairness-accuracy trade-off in re-ranking \[[4](http://arxiv.org/abs/1507.05259)\].

Several approaches have been proposed to address fairness in ranking. For instance, \[[5](http://arxiv.org/abs/1505.05723)\] introduces a re-ranking method that learns individual preferences across multiple fairness dimensions, enhancing provider fairness while maintaining recommendation accuracy. This approach is particularly relevant as it considers fairness from both user and provider perspectives \[[5](http://arxiv.org/abs/1505.05723)\]. Similarly, \[[6](http://arxiv.org/abs/2404.17826)\] presents a taxation perspective for fair re-ranking, reformulating previous methods as item-level tax policies. However, these policies often lack continuity and controllability, which are critical for practical implementation \[[6](http://arxiv.org/abs/2404.17826)\].

Another line of work focuses on fairness-aware re-ranking algorithms that balance accuracy and provider-side fairness. The Fairness-Aware Re-ranking (FAR) algorithm \[[7](http://arxiv.org/abs/1809.02921)\] iteratively generates rankings by trading off between accuracy and provider coverage, while also incorporating personalized user tolerance for diversity. This approach demonstrates that fairness can be improved with minimal accuracy loss, and it accounts for individual user preferences \[[7](http://arxiv.org/abs/1809.02921)\]. Additionally, \[[8](http://arxiv.org/abs/1609.05807)\] explores the concept of fairness of exposure in rankings, proposing a framework that allows for fairness constraints based on exposure allocation. This work highlights the importance of fairness not only for users but also for the items being ranked \[[8](http://arxiv.org/abs/1609.05807)\].

The trade-off between accuracy and fairness is also a central theme in fairness-aware classification. \[[9](http://arxiv.org/abs/1805.01788)\] introduces a confidence-based approach to balance fairness and accuracy, proposing a method to shift decision boundaries for protected groups while maintaining high accuracy. This method allows for a transparent quantification of the trade-off between bias and error \[[9](http://arxiv.org/abs/1805.01788)\]. Similarly, \[[10](http://arxiv.org/abs/1809.03577)\] presents a convex framework for fair regression, introducing fairness regularizers that span from group fairness to individual fairness. This framework enables the computation of the efficient frontier of accuracy-fairness trade-offs \[[10](http://arxiv.org/abs/1809.03577)\].

In the context of recommendation systems, \[[11](http://arxiv.org/abs/1601.05764)\] explores fairness in re-ranking through pairwise comparisons, proposing a new regularizer to improve fairness during model training. This approach is based on randomized experiments and provides a tractable means to reason about fairness in rankings \[[11](http://arxiv.org/abs/1601.05764)\]. Additionally, \[[12](http://arxiv.org/abs/1802.07281)\] discusses the fairness of exposure in rankings, emphasizing the responsibility of ranking systems to both users and items \[[12](http://arxiv.org/abs/1802.07281)\].

Finally, \[[13](http://arxiv.org/abs/2005.14713)\] introduces a learning-to-rank approach that enforces merit-based fairness guarantees for groups of items, ensuring amortized group fairness while learning the ranking function from implicit feedback data \[[13](http://arxiv.org/abs/2005.14713)\]. These works collectively highlight the complexity of fairness in re-ranking and the need for frameworks that balance accuracy, fairness, and user preferences.

1. \[[1](http://arxiv.org/abs/2005.12974)\] http://arxiv.org/abs/2005.12974  
2. \[[2](http://arxiv.org/abs/1704.06840)\] http://arxiv.org/abs/1704.06840  
3. \[[3](http://arxiv.org/abs/1703.09207)\] http://arxiv.org/abs/2404.17826  
4. \[[4](http://arxiv.org/abs/1507.05259)\] http://arxiv.org/abs/2404.17826  
5. \[[5](http://arxiv.org/abs/1505.05723)\] http://arxiv.org/abs/1809.02921  
6. \[[6](http://arxiv.org/abs/2404.17826)\] http://arxiv.org/abs/2404.17826  
7. \[[7](http://arxiv.org/abs/1809.02921)\] http://arxiv.org/abs/1809.02921  
8. \[[8](http://arxiv.org/abs/1609.05807)\] http://arxiv.org/abs/1802.07281  
9. \[[9](http://arxiv.org/abs/1805.01788)\] http://arxiv.org/abs/1601.05764  
10. \[[10](http://arxiv.org/abs/1809.03577)\] http://arxiv.org/abs/1706.02409  
11. \[[11](http://arxiv.org/abs/1601.05764)\] http://arxiv.org/abs/1903.00780  
12. \[[12](http://arxiv.org/abs/1802.07281)\] http://arxiv.org/abs/1802.07281  
13. \[[13](http://arxiv.org/abs/2005.14713)\] http://arxiv.org/abs/2005.14713
