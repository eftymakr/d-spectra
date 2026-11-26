## Related Works

Cross-domain sequential recommendation (CDSR) has gained significant attention in recent years due to its ability to alleviate data sparsity and cold-start problems by leveraging user interactions across multiple domains \[[1](https://www.semanticscholar.org/paper/a8f2764a76772ab957b31f5d7bb88527d46fbdc8)\]. Traditional approaches often rely on self-attention mechanisms, such as SASRec and BERT4Rec, to model sequential dependencies \[[8](http://arxiv.org/abs/1808.09781)\]. However, these models typically incorporate domain-specific modules to enhance cross-domain learning, which may not fully exploit the inherent capabilities of the self-attention mechanism \[[1](https://www.semanticscholar.org/paper/a8f2764a76772ab957b31f5d7bb88527d46fbdc8)\]. 

Several studies have explored the use of self-attention in sequential recommendation. For instance, LightSANs introduces a low-rank decomposed self-attention mechanism that reduces computational complexity while maintaining performance \[[25](https://www.semanticscholar.org/paper/d3f51870f4da5dd9c2a08a55cfa8a380b8d49208)\]. Similarly, TiSASRec incorporates time interval awareness to better model the temporal dynamics of user interactions \[[6](https://www.semanticscholar.org/paper/9c7a455b1e48d01a99e58e884a6c1acb75074ad0)\]. These works highlight the importance of modeling both the order and timing of interactions in sequential recommendation. 

In the context of cross-domain learning, a number of frameworks have been proposed. For example, DDTCDR employs a dual learning mechanism to transfer knowledge between domains, improving recommendation accuracy by capturing bidirectional latent relations \[[12](http://arxiv.org/abs/1910.05189)\]. Similarly, DREAM introduces a decoupled representation approach that enables simultaneous learning of single- and cross-domain user preferences \[[16](https://www.semanticscholar.org/paper/96bfe33a2503e960153a934e10be91da4d8b13a6)\]. These methods often rely on explicit domain adaptation strategies, which can be computationally intensive and may lead to negative transfer if not carefully managed \[[1](https://www.semanticscholar.org/paper/a8f2764a76772ab957b31f5d7bb88527d46fbdc8)\].

Recent work has also focused on improving the efficiency and effectiveness of cross-domain models. For instance, LSAN proposes a lightweight self-attentive network that reduces memory usage while maintaining high accuracy \[[2](http://arxiv.org/abs/2108.11333)\]. Additionally, the introduction of contrastive learning techniques, such as in CL4SRec, has shown promise in improving user representation learning by leveraging self-supervision signals from user behavior sequences \[[1](https://www.semanticscholar.org/paper/a8f2764a76772ab957b31f5d7bb88527d46fbdc8)\]. These approaches highlight the growing interest in combining self-attention with advanced learning strategies to enhance cross-domain performance.

Moreover, the problem of data sparsity and cold-starts has been addressed through various means. For example, ASReP augments short sequences by generating pseudo-prior items, which helps improve performance for sparse datasets \[[5](http://arxiv.org/abs/2105.00522)\]. Similarly, the use of graph neural networks in C2DSR allows for the modeling of inter-sequence item relationships, further enhancing the accuracy of cross-domain recommendations \[[3](http://arxiv.org/abs/2304.03891)\]. These methods demonstrate the importance of incorporating diverse modeling strategies to address the challenges inherent in cross-domain sequential recommendation.

In summary, while existing CDSR frameworks have made significant progress, there remains a need for more efficient and effective approaches that can fully leverage the self-attention mechanism while addressing the limitations of current methods. Our proposed AutoCDSR framework aims to fill this gap by enhancing the self-attention module to achieve better cross-domain learning \[[1](https://www.semanticscholar.org/paper/a8f2764a76772ab957b31f5d7bb88527d46fbdc8)\].

### References

1. \[[1](https://www.semanticscholar.org/paper/a8f2764a76772ab957b31f5d7bb88527d46fbdc8)\] https://www.semanticscholar.org/paper/a8f2764a76772ab957b31f5d7bb88527d46fbdc8  
2. \[[2](http://arxiv.org/abs/2108.11333)\] http://arxiv.org/abs/2108.11333  
3. \[[3](http://arxiv.org/abs/2304.03891)\] http://arxiv.org/abs/2304.03891  
4. \[[4](https://www.semanticscholar.org/paper/63555b4f363ee72dd8d49d8deca68760542c0cd2)\] https://www.semanticscholar.org/paper/63555b4f363ee72dd8d49d8deca68760542c0cd2  
5. \[[5](http://arxiv.org/abs/2105.00522)\] http://arxiv.org/abs/2105.00522  
6. \[[6](https://www.semanticscholar.org/paper/9c7a455b1e48d01a99e58e884a6c1acb75074ad0)\] https://www.semanticscholar.org/paper/9c7a455b1e48d01a99e58e884a6c1acb75074ad0  
7. \[[7](http://arxiv.org/abs/2209.10163)\] http://arxiv.org/abs/2209.10163  
8. \[[8](http://arxiv.org/abs/1808.09781)\] http://arxiv.org/abs/1808.09781  
9. \[[9](http://arxiv.org/abs/2312.10325)\] http://arxiv.org/abs/2312.10325  
10. \[[10](http://arxiv.org/abs/2311.04760)\] http://arxiv.org/abs/2311.04760  
11. \[[11](https://www.semanticscholar.org/paper/5aed438fecf702ead9c0cddfa9a80bd00cff0138)\] https://www.semanticscholar.org/paper/5aed438fecf702ead9c0cddfa9a80bd00cff0138  
12. \[[12](http://arxiv.org/abs/1910.05189)\] http://arxiv.org/abs/1910.05189  
13. \[[13](http://arxiv.org/abs/2311.04590)\] http://arxiv.org/abs/2311.04590  
14. \[[14](http://arxiv.org/abs/2103.03578)\] http://arxiv.org/abs/2103.03578  
15. \[[15](http://arxiv.org/abs/2106.02768)\] http://arxiv.org/abs/2106.02768  
16. \[[16](https://www.semanticscholar.org/paper/96bfe33a2503e960153a934e10be91da4d8b13a6)\] https://www.semanticscholar.org/paper/96bfe33a2503e960153a934e10be91da4d8b13a6  
17. \[[17](http://arxiv.org/abs/2401.04971)\] http://arxiv.org/abs/2401.04971  
18. \[[18](https://www.semanticscholar.org/paper/2b031c7170c9dccbe506f3d3a1d6104f65e835ae)\] https://www.semanticscholar.org/paper/2b031c7170c9dccbe506f3d3a1d6104f65e835ae  
19. \[[19](https://www.semanticscholar.org/paper/6dd0605f7de7581c69b4acf0ab78000748a09f3e)\] https://www.semanticscholar.org/paper/6dd0605f7de7581c69b4acf0ab78000748a09f3e  
20. \[[20](http://arxiv.org/abs/1812.02646)\] http://arxiv.org/abs/1812.02646  
21. \[[21](http://arxiv.org/abs/2407.11245)\] http://arxiv.org/abs/2407.11245  
22. \[[22](http://arxiv.org/abs/1711.04725)\] http://arxiv.org/abs/1711.04725  
23. \[[23](http://arxiv.org/abs/1804.06769)\] http://arxiv.org/abs/1804.06769  
24. \[[24](http://arxiv.org/abs/2405.12473)\] http://arxiv.org/abs/2405.12473  
25. \[[25](https://www.semanticscholar.org/paper/d3f51870f4da5dd9c2a08a55cfa8a380b8d49208)\] https://www.semanticscholar.org/paper/d3f51870f4da5dd9c2a08a55cfa8a380b8d49208  
26. \[[26](http://arxiv.org/abs/2108.07976)\] http://arxiv.org/abs/2108.07976  
27. \[[27](http://arxiv.org/abs/1911.06478)\] http://arxiv.org/abs/1911.06478  
28. \[[28](http://arxiv.org/abs/2206.08050)\] http://arxiv.org/abs/2206.08050  
29. \[[29](http://arxiv.org/abs/1802.08452)\] http://arxiv.org/abs/1802.08452  
30. \[[30](https://www.semanticscholar.org/paper/27670ed18e96550c674e022e284fc5356a7458c2)\] https://www.semanticscholar.org/paper/27670ed18e96550c674e022e284fc5356a7458c2
