## Related Works

Rehearsal-based methods have been widely studied in continual learning (CL) to mitigate catastrophic forgetting. These methods store a subset of past data in a buffer and use it during training alongside new data, enabling the model to retain knowledge from previous tasks \[[1](http://arxiv.org/abs/2302.05836)\]. Early works such as \[[2](http://arxiv.org/abs/1805.12369)\] proposed memory replay strategies to prevent forgetting by revisiting past experiences. However, the effectiveness of these methods depends on the task similarity and the structure of the data stream \[[3](http://arxiv.org/abs/2104.07446)\]. 

A key challenge in rehearsal-based CL is determining the optimal strategy for balancing new and old data during training. Some approaches, like \[[4](http://arxiv.org/abs/2203.17269)\], use uniform sampling from a buffer, while others, such as \[[5](http://arxiv.org/abs/2307.02251)\], explore more sophisticated selection policies. The work in \[[6](http://arxiv.org/abs/1807.09536)\] introduces a method that selects the most prototypical samples first, followed by less prototypical ones, which improves performance while reducing memory overhead. This aligns with the idea that revisiting past data can help mitigate forgetting, especially when tasks are dissimilar \[[7](http://arxiv.org/abs/2112.08654)\].

Theoretical analysis of rehearsal strategies has also gained traction. In \[[8](http://arxiv.org/abs/2003.09553)\], the authors analyze the performance of concurrent and sequential rehearsal in overparameterized linear models, showing that sequential rehearsal outperforms concurrent rehearsal when tasks are less similar. This finding is further supported by \[[9](http://arxiv.org/abs/1902.10486)\], which demonstrates that sequential rehearsal can lead to better generalization in certain scenarios. The hybrid approach, which combines concurrent and sequential rehearsal, has been proposed in \[[10](http://arxiv.org/abs/2211.13218)\] and \[[11](http://arxiv.org/abs/1710.10368)\] to address the limitations of both strategies. This hybrid method trains similar tasks concurrently and revisits dissimilar ones sequentially, leading to improved performance on benchmark datasets \[[12](http://arxiv.org/abs/1810.10612)\].

Recent works have also explored alternative approaches to rehearsal, such as knowledge distillation and parameter regularization \[[13](http://arxiv.org/abs/2103.07492)\]. For example, \[[14](http://arxiv.org/abs/1906.00695)\] shows that L2 parameter regularization can effectively prevent forgetting without requiring a rehearsal buffer. Similarly, \[[15](http://arxiv.org/abs/2308.13646)\] introduces a method that leverages pre-trained models and random projections to avoid the need for explicit memory storage. These approaches highlight the growing interest in rehearsal-free methods, which aim to reduce memory costs and improve privacy \[[16](http://arxiv.org/abs/1812.02464)\].

In addition to rehearsal-based methods, other strategies such as generative replay \[[17](http://arxiv.org/abs/2103.01133)\] and functional regularization \[[18](http://arxiv.org/abs/1802.10269)\] have been proposed to address catastrophic forgetting. Generative replay involves generating synthetic examples of past tasks to maintain model performance, while functional regularization focuses on preserving the functional properties of the model across tasks \[[19](http://arxiv.org/abs/1809.02058)\]. These methods have shown promise in various settings, including class-incremental learning \[[20](http://arxiv.org/abs/1908.01091)\].

Overall, the field of continual learning has seen significant progress, with a variety of methods addressing the issue of catastrophic forgetting. While rehearsal-based approaches remain popular, recent advances in regularization, distillation, and pre-trained models have opened new avenues for research \[[21](http://arxiv.org/abs/1809.10635)\].

1. \[[1](http://arxiv.org/abs/2302.05836)\] http://arxiv.org/abs/2302.05836  
2. \[[2](http://arxiv.org/abs/1805.12369)\] http://arxiv.org/abs/1805.12369  
3. \[[3](http://arxiv.org/abs/2104.07446)\] http://arxiv.org/abs/2104.07446  
4. \[[4](http://arxiv.org/abs/2203.17269)\] http://arxiv.org/abs/2203.17269  
5. \[[5](http://arxiv.org/abs/2307.02251)\] http://arxiv.org/abs/2308.13646  
6. \[[6](http://arxiv.org/abs/1807.09536)\] http://arxiv.org/abs/1805.12369  
7. \[[7](http://arxiv.org/abs/2112.08654)\] http://arxiv.org/abs/2103.01133  
8. \[[8](http://arxiv.org/abs/2003.09553)\] http://arxiv.org/abs/2302.05836  
9. \[[9](http://arxiv.org/abs/1902.10486)\] http://arxiv.org/abs/2103.01133  
10. \[[10](http://arxiv.org/abs/2211.13218)\] http://arxiv.org/abs/2302.05836  
11. \[[11](http://arxiv.org/abs/1710.10368)\] http://arxiv.org/abs/2202.09826  
12. \[[12](http://arxiv.org/abs/1810.10612)\] http://arxiv.org/abs/2010.15277  
13. \[[13](http://arxiv.org/abs/2103.07492)\] http://arxiv.org/abs/2203.17269  
14. \[[14](http://arxiv.org/abs/1906.00695)\] http://arxiv.org/abs/2203.17269  
15. \[[15](http://arxiv.org/abs/2308.13646)\] http://arxiv.org/abs/2302.05836  
16. \[[16](http://arxiv.org/abs/1812.02464)\] http://arxiv.org/abs/2203.17269  
17. \[[17](http://arxiv.org/abs/2103.01133)\] http://arxiv.org/abs/1809.10635  
18. \[[18](http://arxiv.org/abs/1802.10269)\] http://arxiv.org/abs/1901.11356  
19. \[[19](http://arxiv.org/abs/1809.02058)\] http://arxiv.org/abs/2004.14070  
20. \[[20](http://arxiv.org/abs/1908.01091)\] http://arxiv.org/abs/2010.15277
