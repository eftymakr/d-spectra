## Related Works

Cross-domain sequential recommendation (CDSR) has emerged as a critical area of research in recommender systems, aiming to predict user behavior across multiple domains by leveraging sequential interactions \[[Mingjia Yin' 2024-05-21](http://arxiv.org/abs/2405.12473v3)\]. Early approaches primarily relied on self-attention mechanisms within the Transformer architecture to capture dependencies between items \[[Ozan Sener' 2018-10-10](http://arxiv.org/abs/1810.04650v2)\]. However, these models often failed to effectively handle cross-domain information, leading to performance degradation due to domain shift \[[Muyang Ma' 2020-12-01](http://arxiv.org/abs/2012.00485v3)\]. To address this, several works have introduced domain-specific modules or components to enhance the self-attention mechanism \[[Yingyi Chen' 2023-05-31](http://arxiv.org/abs/2305.19798v2)\]. For example, \[[Wangyu Wu' 2024-12-31](http://arxiv.org/abs/2502.15694v2)\] proposed a contextualized temporal attention mechanism to weigh historical actions based on both temporal and context information, while \[[Jinyu Zhang' 2023-02-07](http://arxiv.org/abs/2302.03221v1)\] introduced a reinforcement learning module to simulate the evolution of user preferences across domains.

Despite these advancements, existing CDSR frameworks often overlook the core self-attention module, which is inherently capable of learning correlations among behaviors \[[Changshuo Zhang' 2024-08-15](http://arxiv.org/abs/2408.08209v2)\]. This limitation has prompted recent studies to focus on enhancing the self-attention mechanism itself. For instance, \[[Yuli Liu' 2024-10-28](http://arxiv.org/abs/2410.21048v1)\] introduced a lightweight self-attentive network (LSAN) to reduce memory usage while maintaining performance, and \[[Xiaolin Zheng' 2022-09-21](http://arxiv.org/abs/2209.10163v1)\] proposed a mixed information flow network to consider both behavioral and knowledge flows across domains. Additionally, \[[Huiyuan Chen' 2022-12-08](http://arxiv.org/abs/2212.04120v1)\] developed a privacy-preserving cross-domain sequential recommender system (PriCDSR) to protect user privacy while enabling cross-domain recommendations.

To further improve CDSR performance, recent works have explored multi-objective optimization strategies. For example, \[[Lei Guo' 2023-04-09](http://arxiv.org/abs/2304.04218v1)\] introduced a reinforcement learning-enhanced framework to address shared-account cross-domain sequential recommendation, while \[[Guanyu Lin' 2023-11-14](http://arxiv.org/abs/2311.08272v1)\] proposed a mixed attention network to extract both domain-specific and cross-domain information. Moreover, \[[Yang Li' 2021-08-25](http://arxiv.org/abs/2108.11333v1)\] presented a self-attentive sequential recommendation model based on cheap causal convolutions to better capture local context, and \[[Lei Guo' 2022-06-16](http://arxiv.org/abs/2206.08050v1)\] introduced a parallel split-join network to handle shared-account and cross-domain scenarios.

In addition to improving attention mechanisms, some studies have focused on integrating external knowledge or leveraging side information. For instance, \[[Xinyu Du' 2023-04-18](http://arxiv.org/abs/2304.09184v3)\] proposed a model that incorporates item image information to better capture visual preferences, while \[[Wangyu Wu' 2025-04-21](http://arxiv.org/abs/2504.15085v5)\] used a frozen CLIP model to generate image embeddings for cross-domain sequential recommendation. Furthermore, \[[Guy Hadad' 2025-04-29](http://arxiv.org/abs/2504.20859v1)\] explored the use of large language models (LLMs) to bridge items and capture user preferences from a semantic perspective.

Recent works have also addressed the issue of data sparsity and cold-start problems in CDSR. For example, \[[Wenchao Sun' 2019-10-06](http://arxiv.org/abs/1910.02448v4)\] introduced a federated cross-domain sequential recommendation framework (FedDCSR) that preserves data privacy while utilizing knowledge from different domains. Similarly, \[[Shu Chen' 2024-01-10](http://arxiv.org/abs/2401.04971v4)\] proposed a model that leverages automated prompting to handle non-overlapping cross-domain scenarios, and \[[Jinzhao Su' 2024-07-18](http://arxiv.org/abs/2407.13135v1)\] introduced a method that models domain and feedback transitions to improve recommendation accuracy.

In summary, while many existing approaches have focused on augmenting the self-attention mechanism or incorporating domain-specific components, our work introduces a novel approach that enhances the self-attention module directly, treating cross-domain learning as a multi-objective optimization problem \[[Wujiang Xu' 2023-11-08](http://arxiv.org/abs/2311.04590v6)\].

### References

1. [Document 3]  
2. [Document 2]  
3. [Document 1]  
4. [Document 12]  
5. [Document 26]  
6. [Document 20]  
7. [Document 1]  
8. [Document 13]  
9. [Document 3]  
10. [Document 24]  
11. [Document 11]  
12. [Document 12]  
13. [Document 13]  
14. [Document 18]  
15. [Document 5]  
16. [Document 16]  
17. [Document 22]  
18. [Document 18]  
19. [Document 11]  
20. [Document 20]  
21. [Document 21]
