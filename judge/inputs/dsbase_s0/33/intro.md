## Related Works

Rehearsal-based methods have emerged as a prominent approach in continual learning (CL) to mitigate catastrophic forgetting by storing and reusing past data during training \[[Eli Verwimp' 2021-04-15](http://arxiv.org/abs/2104.07446v1)\]. These methods typically involve maintaining a buffer of previous data samples and training the model on both new and old data simultaneously \[[Meng Ding' 2024-05-27](http://arxiv.org/abs/2405.17583v1)\]. However, recent studies have questioned whether this concurrent rehearsal strategy is always optimal, especially in scenarios where sequential revisiting of tasks may offer greater benefits \[[Gido M. van de Ven' 2019-04-15](http://arxiv.org/abs/1904.07734v1)\].

The idea of sequential rehearsal, inspired by human learning, suggests that revisiting tasks in sequence can help mitigate forgetting more effectively than concurrent rehearsal \[[Daniel Goldfarb' 2025-02-11](http://arxiv.org/abs/2502.10442v1)\]. This hypothesis has been explored in the context of overparameterized linear models, where theoretical analysis has shown that sequential rehearsal performs better when tasks are less similar \[[Yu Chen' 2019-04-24](http://arxiv.org/abs/1904.10644v1)\]. This finding is supported by empirical studies demonstrating that sequential rehearsal can lead to improved generalization and reduced forgetting compared to concurrent rehearsal \[[Fei Zhu' 2025-03-24](http://arxiv.org/abs/2503.18511v1)\].

Several works have investigated the effectiveness of different rehearsal strategies. For example, \[[Joachim Houyon' 2023-04-03](http://arxiv.org/abs/2304.01239v1)\] proposed a method that combines both concurrent and sequential rehearsal, achieving better performance than either approach alone. Similarly, \[[Seyed Iman Mirzadeh' 2021-10-21](http://arxiv.org/abs/2110.11526v3)\] introduced a hybrid approach that leverages the strengths of both strategies, showing that it can outperform standard concurrent rehearsal in certain scenarios. The hybrid rehearsal strategy has also been explored in the context of deep neural networks, where it has been shown to improve performance on benchmark datasets \[[Thang Doan' 2022-02-20](http://arxiv.org/abs/2202.09826v3)\].

In addition to these approaches, other methods have been proposed to address catastrophic forgetting without relying on explicit rehearsal. These include regularization-based methods such as Elastic Weight Consolidation (EWC) \[[Dong Yin' 2020-06-19](http://arxiv.org/abs/2006.10974v3)\], which penalizes changes to weights that are important for previously learned tasks, and knowledge distillation techniques that transfer knowledge from a pre-trained model to a new model \[[Dylan R. Ashley' 2021-02-15](http://arxiv.org/abs/2102.07686v4)\]. While these methods can be effective, they often require careful tuning and may not perform as well as rehearsal-based approaches in certain scenarios \[[Ronald Kemker' 2017-08-07](http://arxiv.org/abs/1708.02072v4)\].

The theoretical analysis of rehearsal-based CL in overparameterized linear models has also been explored in several studies. For instance, \[[Shuang Li' 2020-11-24](http://arxiv.org/abs/2011.12216v3)\] provided a comprehensive analysis of the performance of concurrent and sequential rehearsal strategies, showing that sequential rehearsal can lead to better generalization when tasks are less similar. This finding has been further validated by empirical studies using deep neural networks \[[Kazuki Irie' 2023-12-01](http://arxiv.org/abs/2312.00276v3)\].

In summary, while concurrent rehearsal remains a widely used approach in CL, recent work has shown that sequential rehearsal can offer significant benefits, particularly when tasks are less similar. The hybrid rehearsal strategy, which combines the strengths of both approaches, has also been shown to be effective in reducing forgetting and improving generalization. These findings highlight the importance of exploring different rehearsal strategies to determine which is most effective in various scenarios.

### References

1. [http://arxiv.org/abs/2203.17269v2](http://arxiv.org/abs/2203.17269v2)  
2. [http://arxiv.org/abs/2203.17269v2](http://arxiv.org/abs/2203.17269v2)  
3. [http://arxiv.org/abs/2405.17583v1](http://arxiv.org/abs/2405.17583v1)  
4. [http://arxiv.org/abs/2405.17583v1](http://arxiv.org/abs/2405.17583v1)  
5. [http://arxiv.org/abs/2405.17583v1](http://arxiv.org/abs/2405.17583v1)  
6. [http://arxiv.org/abs/2405.17583v1](http://arxiv.org/abs/2405.17583v1)  
7. [http://arxiv.org/abs/2202.09826v3](http://arxiv.org/abs/2202.09826v3)  
8. [http://arxiv.org/abs/2405.09820v1](http://arxiv.org/abs/2405.09820v1)  
9. [http://arxiv.org/abs/2405.09820v1](http://arxiv.org/abs/2405.09820v1)  
10. [http://arxiv.org/abs/2006.10974v3](http://arxiv.org/abs/2006.10974v3)  
11. [http://arxiv.org/abs/2203.17269v2](http://arxiv.org/abs/2203.17269v2)  
12. [http://arxiv.org/abs/2203.17269v2](http://arxiv.org/abs/2203.17269v2)  
13. [http://arxiv.org/abs/2405.17583v1](http://arxiv.org/abs/2405.17583v1)  
14. [http://arxiv.org/abs/2405.09820v1](http://arxiv.org/abs/2405.09820v1)
