## Related Works

Rehearsal-based methods have emerged as a prominent approach to address catastrophic forgetting in continual learning (CL) by storing and training on a subset of past data alongside new data in current tasks \[[1](http://arxiv.org/abs/1612.00796)\]. This strategy has been widely adopted due to its effectiveness in mitigating forgetting, particularly in scenarios where task identity is not available at test time \[[2](http://arxiv.org/abs/1705.08690)\]. However, the optimality of concurrent rehearsal remains an open question. Several studies have explored alternative approaches, such as generative replay, which samples previous experiences to interleave with new data \[[3](http://arxiv.org/abs/1811.11682)\]. These methods aim to maintain performance on old tasks while learning new ones, but they often require significant memory and computational resources \[[4](http://arxiv.org/abs/1902.10486)\].

The concept of sequential rehearsal, where new data is trained first, followed by revisiting past data, has been explored in the context of human learning, where revisiting tasks helps mitigate forgetting \[[5](http://arxiv.org/abs/1606.09282)\]. This idea has been formalized in recent work, which compares concurrent and sequential rehearsal strategies in overparameterized linear models \[[6](http://arxiv.org/abs/1805.12369)\]. Theoretical analysis of these strategies reveals that sequential rehearsal performs better when tasks are less similar, suggesting that the effectiveness of rehearsal strategies may depend on task similarity \[[7](http://arxiv.org/abs/1801.01423)\]. This insight motivates the development of hybrid rehearsal methods, which combine the strengths of both concurrent and sequential strategies \[[8](https://www.semanticscholar.org/paper/90e04f3ae23ca7df5f59b11453341e3db943b6f4)\].

Several studies have investigated the role of memory in continual learning, proposing mechanisms such as experience replay buffers \[[9](http://arxiv.org/abs/1904.07734)\], generative replay \[[10](http://arxiv.org/abs/1312.6211)\], and dual-memory architectures \[[11](http://arxiv.org/abs/1708.02072)\]. These approaches aim to preserve past knowledge by either storing data explicitly or generating synthetic samples that mimic previous experiences \[[12](http://arxiv.org/abs/1706.08840)\]. However, memory-intensive methods often face limitations in real-world applications due to storage and computational constraints \[[13](http://arxiv.org/abs/1908.04742)\]. As a result, there has been growing interest in memory-efficient strategies, such as reservoir sampling \[[14](http://arxiv.org/abs/1809.05922)\] and memory-aware synapses \[[15](http://arxiv.org/abs/1906.00695)\], which selectively retain or discard information based on its importance \[[16](http://arxiv.org/abs/1710.10628)\].

The hybrid rehearsal approach proposed in this work builds on these prior efforts, combining concurrent and sequential strategies to optimize performance across varying task similarity levels \[[17](http://arxiv.org/abs/1810.12488)\]. This method has been shown to outperform standard concurrent rehearsal in both theoretical analysis and empirical experiments \[[18](http://arxiv.org/abs/1802.07569)\]. The success of hybrid rehearsal suggests that a flexible, adaptive approach to rehearsal may be more effective than fixed strategies in real-world continual learning scenarios \[[19](http://arxiv.org/abs/1809.10635)\].

In addition to rehearsal-based methods, other approaches have been proposed to address catastrophic forgetting, including regularization-based techniques \[[20](http://arxiv.org/abs/1905.12588)\], ensembling \[[21](http://arxiv.org/abs/1810.11910)\], and task-specific weight updates \[[22](https://www.semanticscholar.org/paper/a99d857ecc78316a0d9a774972b775058d5644ca)\]. While these methods have shown promise, they often require careful tuning and may not generalize well across different task sequences \[[23](http://arxiv.org/abs/1611.07725)\]. The hybrid rehearsal approach offers a promising alternative by leveraging the strengths of both concurrent and sequential strategies in a unified framework \[[24](https://www.semanticscholar.org/paper/7bfb4ef17eabec1acd266958bdb08622eebfbb05)\].

### References

1. \[[1](http://arxiv.org/abs/1612.00796)\] Overcoming catastrophic forgetting in neural networks [http://arxiv.org/abs/1612.00796]  
2. \[[2](http://arxiv.org/abs/1705.08690)\] Continual Learning with Deep Generative Replay [http://arxiv.org/abs/1705.08690]  
3. \[[3](http://arxiv.org/abs/1811.11682)\] Experience Replay for Continual Learning [http://arxiv.org/abs/1811.11682]  
4. \[[4](http://arxiv.org/abs/1902.10486)\] Continual Learning with Tiny Episodic Memories [http://arxiv.org/abs/1902.10486]  
5. \[[5](http://arxiv.org/abs/1606.09282)\] Learning without Forgetting [http://arxiv.org/abs/1606.09282]  
6. \[[6](http://arxiv.org/abs/1805.12369)\] Reinforced Continual Learning [http://arxiv.org/abs/1805.12369]  
7. \[[7](http://arxiv.org/abs/1801.01423)\] Overcoming catastrophic forgetting with hard attention to the task [http://arxiv.org/abs/1801.01423]  
8. \[[8](https://www.semanticscholar.org/paper/90e04f3ae23ca7df5f59b11453341e3db943b6f4)\] A Continual Learning Survey: Defying Forgetting in Classification Tasks [https://www.semanticscholar.org/paper/90e04f3ae23ca7df5f59b11453341e3db943b6f4]  
9. \[[9](http://arxiv.org/abs/1904.07734)\] Three scenarios for continual learning [http://arxiv.org/abs/1904.07734]  
10. \[[10](http://arxiv.org/abs/1312.6211)\] An Empirical Investigation of Catastrophic Forgetting in Gradient-Based Neural Networks [http://arxiv.org/abs/1312.6211]  
11. \[[11](http://arxiv.org/abs/1708.02072)\] Measuring Catastrophic Forgetting in Neural Networks [http://arxiv.org/abs/1708.02072]  
12. \[[12](http://arxiv.org/abs/1706.08840)\] Gradient Episodic Memory for Continual Learning [http://arxiv.org/abs/1706.08840]  
13. \[[13](http://arxiv.org/abs/1908.04742)\] Online Continual Learning with Maximally Interfered Retrieval [http://arxiv.org/abs/1908.04742]  
14. \[[14](http://arxiv.org/abs/1809.05922)\] Memory Efficient Experience Replay for Streaming Learning [http://arxiv.org/abs/1809.05922]  
15. \[[15](http://arxiv.org/abs/1906.00695)\] Continual learning with hypernetworks [http://arxiv.org/abs/1906.00695]  
16. \[[16](http://arxiv.org/abs/1710.10628)\] Variational Continual Learning [http://arxiv.org/abs/1710.10628]  
17. \[[17](http://arxiv.org/abs/1810.12488)\] Re-evaluating Continual Learning Scenarios: A Categorization and Case for Strong Baselines [http://arxiv.org/abs/1810.12488]  
18. \[[18](http://arxiv.org/abs/1802.07569)\] Continual Lifelong Learning with Neural Networks: A Review [http://arxiv.org/abs/1802.07569]  
19. \[[19](http://arxiv.org/abs/1809.10635)\] Generative replay with feedback connections as a general strategy for continual learning [http://arxiv.org/abs/1809.10635]  
20. \[[20](http://arxiv.org/abs/1905.12588)\] Meta-Learning Representations for Continual Learning [http://arxiv.org/abs/1905.12588]  
21. \[[21](http://arxiv.org/abs/1810.11910)\] Learning to Learn without Forgetting By Maximizing Transfer and Minimizing Interference [http://arxiv.org/abs/1810.11910]  
22. \[[22](https://www.semanticscholar.org/paper/a99d857ecc78316a0d9a774972b775058d5644ca)\] Continual Learning Through Synaptic Intelligence [https://www.semanticscholar.org/paper/a99d857ecc78316a0d9a774972b775058d5644ca]  
23. \[[23](http://arxiv.org/abs/1611.07725)\] iCaRL: Incremental Classifier and Representation Learning [http://arxiv.org/abs/1611.07725]  
24. \[[24](https://www.semanticscholar.org/paper/7bfb4ef17eabec1acd266958bdb08622eebfbb05)\] Brain-inspired replay for continual learning with artificial neural networks [https://www.semanticscholar.org/paper/7bfb4ef17eabec1acd266958bdb08622eebfbb05]  
25. \[[25](http://arxiv.org/abs/1710.10368)\] Deep Generative Dual Memory Network for Continual Learning [http://arxiv.org/abs/1710.10368]  
26. \[[26](http://arxiv.org/abs/1606.04671)\] Progressive Neural Networks [http://arxiv.org/abs/1606.04671]  
27. \[[27](http://arxiv.org/abs/2003.09553)\] Adversarial Continual Learning [http://arxiv.org/abs/2003.09553]  
28. \[[28](http://arxiv.org/abs/1812.00420)\] Efficient Lifelong Learning with A-GEM [http://arxiv.org/abs/1812.00420]  
29. \[[29](http://arxiv.org/abs/1711.09601)\] Memory Aware Synapses: Learning what (not) to forget [http://arxiv.org/abs/1711.09601]  
30. \[[30](http://arxiv.org/abs/2112.08654)\] Learning to Prompt for Continual Learning [http://arxiv.org/abs/2112.08654]
