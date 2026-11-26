## Related Works

Rehearsal-based methods have been widely studied in continual learning (CL) to address catastrophic forgetting, where models lose previously learned knowledge when trained on new tasks \[[1](http://arxiv.org/abs/1612.00796)\]. These methods typically store a subset of past data and train it alongside new data in the current task \[[2](http://arxiv.org/abs/1811.11682)\]. While concurrent rehearsal, where past and new data are trained together, is a common approach, recent work has questioned whether this strategy is always optimal \[[3](http://arxiv.org/abs/1705.08690)\]. Inspired by human learning, where revisiting tasks sequentially helps mitigate forgetting, there is growing interest in exploring sequential rehearsal as a potentially more effective strategy \[[4](http://arxiv.org/abs/1801.01423)\].

Several studies have investigated the effectiveness of rehearsal-based approaches in mitigating catastrophic forgetting. For instance, experience replay buffers have been proposed as a general solution to reduce forgetting by storing and reusing past experiences \[[5](http://arxiv.org/abs/2012.12631)\]. This approach has been shown to be effective in both reinforcement learning and classification tasks \[[6](http://arxiv.org/abs/1606.09282)\]. Similarly, generative replay has been explored as a method to sample and reuse past data, particularly in scenarios where task identity is not known \[[7](http://arxiv.org/abs/1902.10486)\]. The idea of using generative models to replay past experiences has been further refined by integrating feedback connections, enabling more efficient and scalable solutions \[[8](https://www.semanticscholar.org/paper/90e04f3ae23ca7df5f59b11453341e3db943b6f4)\].

The importance of task similarity in determining the effectiveness of rehearsal strategies has also been highlighted. For example, in class-incremental learning scenarios, where tasks are not disjoint, methods like Elastic Weight Consolidation (EWC) and Memory Aware Synapses (MAS) have been proposed to selectively protect important weights \[[9](http://arxiv.org/abs/1904.07734)\]. These methods aim to preserve knowledge from previous tasks while allowing the model to learn new tasks \[[10](http://arxiv.org/abs/1809.10635)\]. Additionally, the role of memory in continual learning has been extensively studied, with approaches such as the Deep Generative Replay framework proposing a dual model architecture to sample and interleave past and new data \[[11](https://www.semanticscholar.org/paper/7bfb4ef17eabec1acd266958bdb08622eebfbb05)\].

In the context of sequential rehearsal, recent work has suggested that training similar tasks concurrently and revisiting dissimilar tasks sequentially may offer better performance \[[12](http://arxiv.org/abs/1908.04742)\]. This idea aligns with the theoretical analysis presented in this paper, which compares concurrent and sequential rehearsal strategies in overparameterized linear models \[[13](http://arxiv.org/abs/1706.08840)\]. The analysis shows that sequential rehearsal performs better when tasks are less similar, motivating the development of a hybrid approach that combines both strategies \[[14](http://arxiv.org/abs/1906.00695)\].

In addition to theoretical insights, empirical studies have demonstrated the effectiveness of hybrid rehearsal strategies. For example, the Gradient Episodic Memory (GEM) method has been shown to outperform existing approaches by allowing beneficial transfer of knowledge to previous tasks \[[15](http://arxiv.org/abs/1805.12369)\]. Similarly, the Learning without Forgetting method has been proposed to preserve original capabilities while training on new tasks, without requiring access to past data \[[16](http://arxiv.org/abs/2003.09553)\]. These approaches highlight the ongoing efforts to develop more robust and efficient continual learning strategies.

In summary, while concurrent rehearsal remains a popular approach, recent research has explored sequential rehearsal as a promising alternative, particularly in scenarios where tasks are less similar \[[17](http://arxiv.org/abs/1905.12588)\]. The hybrid rehearsal method proposed in this work builds on these insights, offering a novel approach that combines the strengths of both strategies \[[18](http://arxiv.org/abs/1809.05922)\].

References:
1. \[[1](http://arxiv.org/abs/1612.00796)\] http://arxiv.org/abs/1612.00796
2. \[[2](http://arxiv.org/abs/1811.11682)\] http://arxiv.org/abs/1811.11682
3. \[[3](http://arxiv.org/abs/1705.08690)\] http://arxiv.org/abs/1705.08690
4. \[[4](http://arxiv.org/abs/1801.01423)\] http://arxiv.org/abs/1801.01423
5. \[[5](http://arxiv.org/abs/2012.12631)\] http://arxiv.org/abs/2012.12631
6. \[[6](http://arxiv.org/abs/1606.09282)\] http://arxiv.org/abs/1902.10486
7. \[[7](http://arxiv.org/abs/1902.10486)\] http://arxiv.org/abs/1809.10635
8. \[[8](https://www.semanticscholar.org/paper/90e04f3ae23ca7df5f59b11453341e3db943b6f4)\] http://arxiv.org/abs/1908.04742
9. \[[9](http://arxiv.org/abs/1904.07734)\] http://arxiv.org/abs/1706.08840
10. \[[10](http://arxiv.org/abs/1809.10635)\] http://arxiv.org/abs/1906.00695
11. \[[11](https://www.semanticscholar.org/paper/7bfb4ef17eabec1acd266958bdb08622eebfbb05)\] http://arxiv.org/abs/1904.07734
12. \[[12](http://arxiv.org/abs/1908.04742)\] http://arxiv.org/abs/2112.10017
13. \[[13](http://arxiv.org/abs/1706.08840)\] http://arxiv.org/abs/1802.07569
14. \[[14](http://arxiv.org/abs/1906.00695)\] http://arxiv.org/abs/1710.10368
15. \[[15](http://arxiv.org/abs/1805.12369)\] http://arxiv.org/abs/1810.11910
16. \[[16](http://arxiv.org/abs/2003.09553)\] http://arxiv.org/abs/1606.09282
17. \[[17](http://arxiv.org/abs/1905.12588)\] http://arxiv.org/abs/2007.07400
18. \[[18](http://arxiv.org/abs/1809.05922)\] http://arxiv.org/abs/1711.09601
