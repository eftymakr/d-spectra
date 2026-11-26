## Related Works

Rehearsal-based methods have been widely studied in continual learning (CL) as a means to mitigate catastrophic forgetting by revisiting past data alongside new data \[[1](http://arxiv.org/abs/2104.07446)\]. These approaches typically store a subset of previously seen data in a memory buffer and use it during training to maintain performance on old tasks \[[2](http://arxiv.org/abs/2302.05836)\]. However, the optimality of concurrent rehearsal, where past and new data are trained together, has not been thoroughly evaluated. Recent work has explored alternative strategies, such as sequential rehearsal, where new data is trained first, followed by revisiting past data sequentially \[[3](http://arxiv.org/abs/2203.14544)\]. This approach is inspired by human learning, where revisiting tasks helps reinforce memory \[[4](http://arxiv.org/abs/1812.02464)\]. 

The effectiveness of rehearsal strategies has been analyzed in various contexts. For instance, \[[5](http://arxiv.org/abs/2103.07492)\] highlights that models trained sequentially with rehearsal may remain in a low-loss region but risk overfitting on their sample memory, which can harm generalization. Similarly, \[[6](http://arxiv.org/abs/2312.00276)\] shows that rehearsal-based methods often require careful memory management to maintain performance, and the choice of memory selection can significantly impact results. This aligns with findings in \[[7](http://arxiv.org/abs/2405.04101)\], which suggests that uniform sampling in a class-balanced manner is effective, but better sample selection policies remain elusive. 

In the context of deep learning, several works have explored the use of rehearsal with different mechanisms. For example, \[[8](http://arxiv.org/abs/2403.01244)\] introduces a dual memory system that separates continual learning from reinforcement learning, while \[[9](http://arxiv.org/abs/2203.17269)\] proposes a pseudo-rehearsal system that generates synthetic instances to avoid the need for storing raw data. These methods aim to reduce memory overhead while maintaining performance. However, they often rely on additional storage or computational resources, which can limit scalability \[[10](http://arxiv.org/abs/1810.10612)\]. 

Theoretical analysis of rehearsal-based CL has also been explored. \[[11](http://arxiv.org/abs/2406.09384)\] provides a theoretical framework for understanding forgetting in linear regression models, showing that task similarity and step size significantly affect forgetting. This aligns with findings in \[[12](http://arxiv.org/abs/2308.13646)\], which demonstrates that the arrangement of tasks in a sequence, particularly those with larger eigenvalues in their population data covariance matrices, can increase forgetting. These insights are further supported by \[[13](http://arxiv.org/abs/2405.17583)\], which shows that overparameterization can mitigate forgetting in linear models. 

Recent work has also examined the role of consistency regularization in rehearsal-based methods. \[[14](http://arxiv.org/abs/2202.09826)\] suggests that consistency in predictions of soft-targets can help preserve information about previous tasks, while \[[15](http://arxiv.org/abs/2408.16939)\] explores how consistency regularization can be cast as a self-supervised pretext task to improve performance. These approaches highlight the importance of maintaining consistency across tasks to reduce forgetting. 

In addition, \[[16](http://arxiv.org/abs/2505.21942)\] proposes a memoryless method that combines self-organizing maps with standard supervised networks to adaptively cluster inputs into task contexts, reducing the need for explicit memory buffers. This aligns with the idea of using task-agnostic semantic memory for cross-task knowledge consolidation \[[17](http://arxiv.org/abs/1904.09330)\]. 

Overall, the literature on rehearsal-based CL highlights the importance of memory management, task similarity, and consistency regularization in mitigating catastrophic forgetting. While concurrent rehearsal remains a popular strategy, recent work suggests that sequential rehearsal may offer advantages in certain scenarios, particularly when tasks are less similar \[[18](http://arxiv.org/abs/2006.10974)\].

1. \[[1](http://arxiv.org/abs/2104.07446)\] http://arxiv.org/abs/2104.07446  
2. \[[2](http://arxiv.org/abs/2302.05836)\] http://arxiv.org/abs/2103.07492  
3. \[[3](http://arxiv.org/abs/2203.14544)\] http://arxiv.org/abs/2302.05836  
4. \[[4](http://arxiv.org/abs/1812.02464)\] http://arxiv.org/abs/2203.17269  
5. \[[5](http://arxiv.org/abs/2103.07492)\] http://arxiv.org/abs/2104.07446  
6. \[[6](http://arxiv.org/abs/2312.00276)\] http://arxiv.org/abs/2203.14544  
7. \[[7](http://arxiv.org/abs/2405.04101)\] http://arxiv.org/abs/2203.14544  
8. \[[8](http://arxiv.org/abs/2403.01244)\] http://arxiv.org/abs/1812.02464  
9. \[[9](http://arxiv.org/abs/2203.17269)\] http://arxiv.org/abs/2403.01244  
10. \[[10](http://arxiv.org/abs/1810.10612)\] http://arxiv.org/abs/2203.17269  
11. \[[11](http://arxiv.org/abs/2406.09384)\] http://arxiv.org/abs/2405.17583  
12. \[[12](http://arxiv.org/abs/2308.13646)\] http://arxiv.org/abs/2405.17583  
13. \[[13](http://arxiv.org/abs/2405.17583)\] http://arxiv.org/abs/2408.16939  
14. \[[14](http://arxiv.org/abs/2202.09826)\] http://arxiv.org/abs/2207.04998  
15. \[[15](http://arxiv.org/abs/2408.16939)\] http://arxiv.org/abs/2207.04998  
16. \[[16](http://arxiv.org/abs/2505.21942)\] http://arxiv.org/abs/1904.09330  
17. \[[17](http://arxiv.org/abs/1904.09330)\] http://arxiv.org/abs/2006.10974  
18. \[[18](http://arxiv.org/abs/2006.10974)\] http://arxiv.org/abs/2203.17269
