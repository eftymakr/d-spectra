## Related Works

Cross-domain sequential recommendation (CDSR) has gained significant attention in recent years due to its ability to alleviate data sparsity and cold-start problems by leveraging user interactions across multiple domains \[[1](https://www.semanticscholar.org/paper/27670ed18e96550c674e022e284fc5356a7458c2)\]. Traditional approaches to CDSR often rely on self-attention mechanisms within transformer-based models, with additional domain-specific components being introduced to enhance performance \[[2](http://arxiv.org/abs/2407.11245)\]. However, these methods typically overlook the potential of the core self-attention module, which is inherently capable of capturing complex correlations among sequential interactions \[[3](http://arxiv.org/abs/2401.04971)\]. 

Several works have attempted to improve CDSR by incorporating domain-aware modules or attention mechanisms tailored for cross-domain settings. For instance, \[[4](https://www.semanticscholar.org/paper/96bfe33a2503e960153a934e10be91da4d8b13a6)\] proposes a shared proxy item encoder to generate universal representations for items across domains, while \[[5](http://arxiv.org/abs/2405.12473)\] introduces a time-interval-aware attention encoder to consider temporal dynamics in sequences. Additionally, \[[6](http://arxiv.org/abs/2311.04760)\] develops a contrastive learning auxiliary task to enhance cross-domain sequence representation by weighting items based on their relevance to the objective domain. These approaches aim to improve performance but often focus on isolated components rather than the holistic enhancement of the self-attention mechanism \[[7](https://www.semanticscholar.org/paper/10715bc315c7c1075b5bf35e603fc08aaf5dff36)\].

More recently, \[[8](https://www.semanticscholar.org/paper/6dd0605f7de7581c69b4acf0ab78000748a09f3e)\] explores cooperative learning between single- and cross-domain sequential recommendation tasks, using an asymmetric cooperative network to evaluate negative transfer and adaptively assign weights to prediction losses. Similarly, \[[9](https://www.semanticscholar.org/paper/11da511e9baafc1dfdf58a287c1ead787c9345bc)\] introduces a decoupled representation framework that simultaneously learns single- and cross-domain user preferences, addressing the limitations of prior methods that transfer knowledge from rich to target domains without considering inter-sequence relationships \[[10](http://arxiv.org/abs/2304.03891)\]. These studies highlight the need for more integrated and effective strategies for cross-domain knowledge transfer.

In parallel, \[[11](https://www.semanticscholar.org/paper/5a653a8060bf9f714866be2823cef71c0fbf9a34)\] investigates the use of graph neural networks (GNNs) combined with attention-aware mechanisms to model cross-domain and target domain user preferences, demonstrating the effectiveness of such approaches in capturing collaborative relationships among inter-sequence items. \[[12](http://arxiv.org/abs/2311.04590)\] further enhances CDSR by proposing a channel-enhanced contrastive learning framework that captures temporal contextual relationships and improves user preference modeling \[[13](http://arxiv.org/abs/2410.13588)\]. These works emphasize the importance of leveraging both intra- and inter-sequence interactions to achieve better performance in cross-domain settings.

The challenge of negative transfer and the need for more robust knowledge transfer mechanisms have also been addressed in several studies. For example, \[[14](https://www.semanticscholar.org/paper/c13603992b90529918bd170e2f7a10858a340d43)\] introduces a multi-agent reinforcement learning framework that optimizes the transfer process by coordinating agents' strategies within each source domain, while \[[15](http://arxiv.org/abs/2209.10163)\] proposes a dual dynamic graph with hybrid metric training to enhance user and item representations by aligning collaborative and contrastive metrics \[[16](http://arxiv.org/abs/2501.19232)\]. These approaches demonstrate the potential of advanced learning strategies to improve cross-domain recommendation performance.

In summary, while many existing works have made progress in CDSR, they often focus on isolated components or specific aspects of the problem, such as domain alignment or temporal modeling. Our work builds on these prior efforts by focusing on the core self-attention mechanism and proposing a novel approach to enhance its performance in cross-domain settings \[[17](https://www.semanticscholar.org/paper/4124740c5376b23d87a1d539051b3f350aeb4326)\].

### References

1. [Document 1]  
2. [Document 2]  
3. [Document 3]  
4. [Document 4]  
5. [Document 5]  
6. [Document 6]  
7. [Document 7]  
8. [Document 8]  
9. [Document 9]  
10. [Document 10]  
11. [Document 11]  
12. [Document 12]  
13. [Document 13]  
14. [Document 14]  
15. [Document 15]  
16. [Document 16]  
17. [Document 17]
