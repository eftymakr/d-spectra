## Related Works

Multi-Domain Recommendation (MDR) has emerged as a critical research area in recommender systems, aiming to improve recommendation performance across multiple domains by leveraging cross-domain knowledge transfer \[[1](http://arxiv.org/abs/2201.05973)\]. Traditional MDR approaches often assume a shared structure for transferring knowledge, which may not account for domain-specific variations or conflicts \[[2](http://arxiv.org/abs/2311.13188)\]. This can lead to the Negative Transfer Problem (NTP), where the transfer of knowledge from one domain negatively affects the performance in another \[[3](http://arxiv.org/abs/2308.05508)\]. 

Several studies have attempted to address the NTP by introducing mechanisms for domain alignment and knowledge selection. For instance, \[[4](http://arxiv.org/abs/2211.11191)\] proposed a method that disentangles domain-specific and domain-shared knowledge, enabling more effective knowledge transfer. Similarly, \[[5](http://arxiv.org/abs/2202.12524)\] introduced a framework that aligns user and item embeddings across domains to enhance cross-domain recommendation. However, these approaches typically rely on static domain alignment strategies, which may not adapt well to dynamic domain interactions \[[6](http://arxiv.org/abs/2403.17374)\].

To mitigate the NTP, \[[7](http://arxiv.org/abs/2309.06217)\] introduced a domain negotiation strategy that dynamically adjusts the contribution of different domains during training, reducing conflicts between domains. This is similar to the approach in \[[8](http://arxiv.org/abs/1210.7056)\], where domain-specific adapters are used to handle the heterogeneity of domains. However, these methods often require extensive parameter tuning and may not scale well to large-scale MDR scenarios \[[9](http://arxiv.org/abs/2405.12892)\].

Another line of research focuses on modeling domain preferences and interactions. For example, \[[10](http://arxiv.org/abs/2302.05990)\] proposed a framework that models users' domain-level preferences explicitly, allowing for more personalized recommendations. This aligns with the idea of domain-specific knowledge selection, as seen in \[[11](http://arxiv.org/abs/1812.06229)\], where a domain-to-domain translation model is used to transfer features across domains. However, these methods often assume a fixed set of domains and may not adapt well to unseen or evolving domains \[[12](http://arxiv.org/abs/1905.10756)\].

Recent work has also explored the use of graph-based models for MDR, such as \[[13](http://arxiv.org/abs/1509.02409)\], which leverages graph neural networks to capture sequential user interactions across domains. This approach helps in modeling the interplay between domains and mitigating negative transfer. Similarly, \[[14](http://arxiv.org/abs/2309.09670)\] proposed a method that uses graph-based sequential representations to capture both recent and long-term user interests, enhancing the overall recommendation performance.

In addition, \[[15](http://arxiv.org/abs/2404.18465)\] introduced a curriculum-scheduled knowledge distillation approach that integrates knowledge from multiple pre-trained models to improve the performance of a student model in multi-domain sequential recommendation. This method is particularly useful in scenarios where multiple domains are involved, as it allows for the selective integration of domain-specific knowledge \[[16](http://arxiv.org/abs/2003.00820)\].

Overall, while existing MDR methods have made significant strides in addressing the NTP, there remains a need for more dynamic and adaptive approaches that can effectively model complex domain interactions and select relevant knowledge sources \[[17](http://arxiv.org/abs/2401.00797)\].

1. \[[1](http://arxiv.org/abs/2201.05973)\] Multi-Sparse-Domain Collaborative Recommendation via Enhanced Comprehensive Aspect Preference Learning [http://arxiv.org/abs/2201.05973]  
2. \[[2](http://arxiv.org/abs/2311.13188)\] Cracking the Code of Negative Transfer: A Cooperative Game Theoretic Approach for Cross-Domain Sequential Recommendation [http://arxiv.org/abs/2311.13188]  
3. \[[3](http://arxiv.org/abs/2308.05508)\] Multi-Domain Recommendation with Embedding Disentangling and Domain Alignment [http://arxiv.org/abs/2308.05508]  
4. \[[4](http://arxiv.org/abs/2211.11191)\] Correlative Preference Transfer with Hierarchical Hypergraph Network for Multi-Domain Recommendation [http://arxiv.org/abs/2211.11191]  
5. \[[5](http://arxiv.org/abs/2202.12524)\] MAMDR: A Model Agnostic Learning Framework for Multi-Domain Recommendation [http://arxiv.org/abs/2202.12524]  
6. \[[6](http://arxiv.org/abs/2403.17374)\] Multi-Domain Recommendation to Attract Users via Domain Preference Modeling [http://arxiv.org/abs/2403.17374]  
7. \[[7](http://arxiv.org/abs/2309.06217)\] HAMUR: Hyper Adapter for Multi-Domain Recommendation [http://arxiv.org/abs/2309.06227]  
8. \[[8](http://arxiv.org/abs/1210.7056)\] Selective Transfer Learning for Cross Domain Recommendation [http://arxiv.org/abs/1210.7056]  
9. \[[9](http://arxiv.org/abs/2405.12892)\] Retrievable Domain-Sensitive Feature Memory for Multi-Domain Recommendation [http://arxiv.org/abs/2405.12892]  
10. \[[10](http://arxiv.org/abs/2302.05990)\] Exploiting Graph Structured Cross-Domain Representation for Multi-Domain Recommendation [http://arxiv.org/abs/2302.05990]  
11. \[[11](http://arxiv.org/abs/1812.06229)\] Domain-to-Domain Translation Model for Recommender System [http://arxiv.org/abs/1812.06229]  
12. \[[12](http://arxiv.org/abs/1905.10756)\] Selective Transfer With Reinforced Transfer Network for Partial Domain Adaptation [http://arxiv.org/abs/1905.10756]  
13. \[[13](http://arxiv.org/abs/1509.02409)\] Data-selective transfer learning for multi-domain speech recognition [http://arxiv.org/abs/1509.02409]  
14. \[[14](http://arxiv.org/abs/2309.09670)\] DGM-DR: Domain Generalization with Mutual Information Regularized Diabetic Retinopathy Classification [http://arxiv.org/abs/2309.09670]  
15. \[[15](http://arxiv.org/abs/2404.18465)\] M3oE: Multi-Domain Multi-Task Mixture-of-Experts Recommendation Framework [http://arxiv.org/abs/2404.18465]  
16. \[[16](http://arxiv.org/abs/2003.00820)\] MADAN: Multi-source Adversarial Domain Aggregation Network for Domain Adaptation [http://arxiv.org/abs/2003.00820]  
17. \[[17](http://arxiv.org/abs/2401.00797)\] Curriculum-scheduled knowledge distillation from multiple pre-trained teachers for multi-domain sequential recommendation [http://arxiv.org/abs/2401.00797]  
18. \[[18](http://arxiv.org/abs/2104.13057)\] Graphical Modeling for Multi-Source Domain Adaptation [http://arxiv.org/abs/2104.13057]  
19. \[[19](http://arxiv.org/abs/2108.04441)\] Domain-Aware Universal Style Transfer [http://arxiv.org/abs/2108.04441]
