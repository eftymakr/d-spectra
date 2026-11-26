## Related Works

Fairness in re-ranking has gained significant attention in recent years, driven by the increasing awareness of potential biases in recommendation systems \[[1](http://arxiv.org/abs/2204.08085)\]. Early work on fairness in recommendation systems primarily focused on user-side fairness, often neglecting the impact on item-side fairness \[[10](http://arxiv.org/abs/2104.10671)\]. This approach, however, fails to account for the two-sided nature of recommender systems, where both users and items (or producers) are stakeholders \[[1](http://arxiv.org/abs/2204.08085)\]. 

Several studies have attempted to address this gap by proposing fairness-aware recommendation models that consider both sides of the market. For instance, \[[11](http://arxiv.org/abs/2201.01180)\] introduced FairRec, which guarantees exposure fairness for producers while maintaining fairness for customers. Similarly, \[[9](http://arxiv.org/abs/2104.09024)\] proposed TFROM, a two-sided fairness-aware recommendation model that balances the fairness of both users and providers. These approaches highlight the need for a more holistic view of fairness in recommendation systems \[[9](http://arxiv.org/abs/2104.09024)\]\[[11](http://arxiv.org/abs/2201.01180)\].

The concept of fairness in ranking has also been explored in the context of exposure distribution. \[[6](http://arxiv.org/abs/1802.07281)\] introduced a framework for fairness in rankings, emphasizing the importance of exposure allocation to ensure equitable treatment of items. This idea was further expanded in \[[15](http://arxiv.org/abs/2204.03046)\], where the authors proposed VerFair, an algorithm that balances exposure fairness with ranking performance by leveraging prior knowledge of consumer behavior. These works demonstrate that fairness in rankings is not only about treating similar items equally but also about ensuring that all stakeholders receive a fair share of attention and exposure \[[6](http://arxiv.org/abs/1802.07281)\]\[[15](http://arxiv.org/abs/2204.03046)\].

Another important direction in fairness research is the integration of fairness constraints into the ranking process. \[[18](http://arxiv.org/abs/1706.06368)\] introduced FA*IR, a fair top-k ranking algorithm that ensures group fairness by maintaining a minimum proportion of protected candidates in the top-k ranking. This approach has been further extended in \[[1](http://arxiv.org/abs/2204.08085)\], where the authors proposed CPFair, an optimization-based re-ranking approach that integrates fairness constraints from both the consumer and producer sides. These methods highlight the importance of incorporating fairness into the ranking objective function to achieve equitable outcomes \[[1](http://arxiv.org/abs/2204.08085)\]\[[18](http://arxiv.org/abs/1706.06368)\].

In addition to fairness-aware ranking algorithms, there has been growing interest in evaluating fairness in recommendation systems. \[[16](http://arxiv.org/abs/1610.08559)\] proposed fairness measures for ranked outputs, enabling the detection of bias in real-world datasets. These measures have been used to evaluate the fairness of recommendation systems, highlighting the need for comprehensive fairness evaluation frameworks \[[16](http://arxiv.org/abs/1610.08559)\].

Finally, the economic perspective on fairness in re-ranking has been explored in \[[1](http://arxiv.org/abs/2204.08085)\], where the authors drew an analogy between re-ranking and the dynamics of economic transactions. They proposed the concept of elasticity to quantify the trade-off between fairness and accuracy, emphasizing the need for a more nuanced understanding of fairness in recommendation systems \[[1](http://arxiv.org/abs/2204.08085)\].

1. CPFair: Personalized Consumer and Producer Fairness Re-ranking for Recommender Systems [http://arxiv.org/abs/2204.08085]
2. Fairness through awareness [http://arxiv.org/abs/1104.3913]
3. Equity of Attention: Amortizing Individual Fairness in Rankings [http://arxiv.org/abs/1805.01788]
4. FairRec: Two-Sided Fairness for Personalized Recommendations in Two-Sided Platforms [http://arxiv.org/abs/2002.10764]
5. Ranking with Fairness Constraints [http://arxiv.org/abs/1704.06840]
6. Fairness of Exposure in Rankings [http://arxiv.org/abs/1802.07281]
7. P-MMF: Provider Max-min Fairness Re-ranking in Recommender System [http://arxiv.org/abs/2303.06660]
8. A Taxation Perspective for Fair Re-ranking [http://arxiv.org/abs/2404.17826]
9. TFROM: A Two-sided Fairness-Aware Recommendation Model for Both Customers and Providers [http://arxiv.org/abs/2104.09024]
10. User-oriented Fairness in Recommendation [http://arxiv.org/abs/2104.10671]
11. Toward Fair Recommendation in Two-sided Platforms [http://arxiv.org/abs/2201.01180]
12. Controlling Fairness and Bias in Dynamic Learning-to-Rank [http://arxiv.org/abs/2005.14713]
13. Two-sided fairness in rankings via Lorenz dominance [http://arxiv.org/abs/2110.15781]
14. Designing Fair Ranking Schemes [http://arxiv.org/abs/1712.09752]
15. Vertical Allocation-based Fair Exposure Amortizing in Ranking [http://arxiv.org/abs/2204.03046]
16. Measuring Fairness in Ranked Outputs [http://arxiv.org/abs/1610.08559]
17. Multisided Fairness for Recommendation [http://arxiv.org/abs/1707.00093]
18. FA*IR: A Fair Top-k Ranking Algorithm [http://arxiv.org/abs/1706.06368]
19. Beyond Parity: Fairness Objectives for Collaborative Filtering [http://arxiv.org/abs/1705.08804]
