## Related Works

Fairness in re-ranking has garnered significant attention in recent years, with a growing body of research addressing the trade-off between ranking accuracy and fairness \[[1' 2024-04-27](http://arxiv.org/abs/2404.17826v1)\]. Early work on fairness-aware re-ranking focused on balancing accuracy and fairness by incorporating fairness constraints into the ranking objective \[[2' 2018-09-09](http://arxiv.org/abs/1809.02921v2)\]. However, these approaches often treated fairness and accuracy as conflicting objectives without considering the nuanced relationship between them \[[3' 2024-05-25](http://arxiv.org/abs/2405.16120v2)\]. More recent studies have explored the economic analogy between re-ranking and tax transfer processes, suggesting that fairness considerations in re-ranking can be modeled as a cost passed on to users, similar to commodity taxes \[[4' 2022-04-17](http://arxiv.org/abs/2204.08085v1)\]. This analogy has led to the introduction of elasticity-based frameworks for evaluating the fairness-accuracy trade-off in re-ranking \[[5' 2023-06-02](http://arxiv.org/abs/2306.01417v1)\].

Several approaches have been proposed to ensure fairness in recommendation systems, particularly from the perspective of providers or consumers \[[6' 2020-05-21](http://arxiv.org/abs/2005.12974v1)\]. For example, the work by \[[7' 2024-09-21](http://arxiv.org/abs/2409.14078v1)\] introduced a fairness-aware re-ranking algorithm that balances accuracy and provider-side fairness by incorporating user tolerance for diversity. Similarly, \[[8' 2021-11-17](http://arxiv.org/abs/2111.08878v3)\] proposed a method that integrates fairness constraints from both consumer and producer sides, aiming to improve fairness without sacrificing recommendation quality. These approaches highlight the importance of multi-faceted fairness considerations in re-ranking tasks \[[9' 2017-06-30](http://arxiv.org/abs/1706.10208v1)\].

The concept of elasticity has been used to formalize the trade-off between fairness and accuracy in re-ranking. In particular, the elasticity of utility between item groups has been proposed as a measure to quantify how changes in fairness affect accuracy \[[10' 2020-01-21](http://arxiv.org/abs/2001.09784v1)\]. This idea has inspired the development of new evaluation frameworks, such as the Elastic Fairness Curve (EF-Curve), which enables a comparative analysis of algorithm performance across different elasticity levels \[[11' 2023-03-12](http://arxiv.org/abs/2303.06660v1)\]. The EF-Curve provides a more comprehensive assessment of fair re-ranking algorithms by considering the trade-off between fairness and accuracy in a structured manner \[[12' 2021-03-01](http://arxiv.org/abs/2103.01335v1)\].

In addition to elasticity-based approaches, several studies have explored alternative fairness metrics and optimization strategies for fair re-ranking. For instance, \[[13' 2022-06-05](http://arxiv.org/abs/2206.02237v1)\] proposed a method based on max-min fairness to ensure that the worst-performing providers receive adequate exposure, while \[[14' 2024-05-07](http://arxiv.org/abs/2405.04034v1)\] introduced a fairness-aware re-ranking model that balances user preferences with provider fairness in an online setting. These methods demonstrate the diversity of approaches to fairness in re-ranking, each with its own trade-offs and assumptions \[[15' 2022-02-08](http://arxiv.org/abs/2202.03586v2)\].

The challenge of ensuring fairness in re-ranking is further complicated by the need to account for fluctuating user traffic and varying fairness requirements \[[16' 2023-10-15](http://arxiv.org/abs/2310.13007v6)\]. Some studies have addressed this by introducing dynamic fairness-aware re-ranking approaches that adapt to changing conditions \[[17' 2021-10-04](http://arxiv.org/abs/2110.01641v1)\]. These methods often rely on economic-inspired principles, such as the Talmud rule, to ensure long-term fairness while maintaining short-term accuracy \[[18' 2023-06-10](http://arxiv.org/abs/2306.06542v1)\].

Overall, the field of fair re-ranking has evolved from simple fairness constraints to more sophisticated models that incorporate economic principles, multi-faceted fairness considerations, and dynamic adaptation to changing conditions \[[19' 2019-02-26](http://arxiv.org/abs/1902.11162v2)\].

References:

1. \[[1' 2024-04-27](http://arxiv.org/abs/2404.17826v1)\] http://arxiv.org/abs/2404.17826v1  
2. \[[2' 2018-09-09](http://arxiv.org/abs/1809.02921v2)\] http://arxiv.org/abs/1809.02921v2  
3. \[[3' 2024-05-25](http://arxiv.org/abs/2405.16120v2)\] http://arxiv.org/abs/2405.16120v2  
4. \[[4' 2022-04-17](http://arxiv.org/abs/2204.08085v1)\] http://arxiv.org/abs/2204.08085v1  
5. \[[5' 2023-06-02](http://arxiv.org/abs/2306.01417v1)\] http://arxiv.org/abs/2005.12974v1  
6. \[[6' 2020-05-21](http://arxiv.org/abs/2005.12974v1)\] http://arxiv.org/abs/2303.06660v1  
7. \[[7' 2024-09-21](http://arxiv.org/abs/2409.14078v1)\] http://arxiv.org/abs/2111.08878v3  
8. \[[8' 2021-11-17](http://arxiv.org/abs/2111.08878v3)\] http://arxiv.org/abs/2206.02237v1  
9. \[[9' 2017-06-30](http://arxiv.org/abs/1706.10208v1)\] http://arxiv.org/abs/2409.14078v1  
10. \[[10' 2020-01-21](http://arxiv.org/abs/2001.09784v1)\] http://arxiv.org/abs/2103.01335v1  
11. \[[11' 2023-03-12](http://arxiv.org/abs/2303.06660v1)\] http://arxiv.org/abs/2306.06542v1  
12. \[[12' 2021-03-01](http://arxiv.org/abs/2103.01335v1)\] http://arxiv.org/abs/2110.01641v1  
13. \[[13' 2022-06-05](http://arxiv.org/abs/2206.02237v1)\] http://arxiv.org/abs/2306.06542v1  
14. \[[14' 2024-05-07](http://arxiv.org/abs/2405.04034v1)\] http://arxiv.org/abs/2306.06542v1  
15. \[[15' 2022-02-08](http://arxiv.org/abs/2202.03586v2)\] http://arxiv.org/abs/2306.06542v1  
16. \[[16' 2023-10-15](http://arxiv.org/abs/2310.13007v6)\] http://arxiv.org/abs/2306.06542v1  
17. \[[17' 2021-10-04](http://arxiv.org/abs/2110.01641v1)\] http://arxiv.org/abs/2306.06542v1  
18. \[[18' 2023-06-10](http://arxiv.org/abs/2306.06542v1)\] http://arxiv.org/abs/2306.06542v1  
19. \[[19' 2019-02-26](http://arxiv.org/abs/1902.11162v2)\] http://arxiv.org/abs/2306.06542v1
