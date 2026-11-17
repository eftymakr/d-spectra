## Related Works

Rehearsal-based methods constitute a cornerstone in continual learning (CL) for addressing catastrophic forgetting by maintaining a memory buffer of past samples and training on both new and stored data concurrently \[[2104.07446v1](http://arxiv.org/abs/2104.07446v1)\]\[[2405.17583v1](http://arxiv.org/abs/2405.17583v1)\]. This concurrent rehearsal strategy has been shown effective across various benchmarks and is widely adopted due to its simplicity and empirical success. However, recent insights suggest that concurrent rehearsal may not always be optimal, particularly concerning how tasks are revisited during training \[[1904.07734v1](http://arxiv.org/abs/1904.07734v1)\]\[[2502.10442v1](http://arxiv.org/abs/2502.10442v1)\].

The concept of sequential rehearsal, inspired by the human learning process where tasks are revisited one after another rather than simultaneously, has gained attention as a potentially superior alternative under certain conditions. Theoretical analyses in overparameterized linear models reveal that sequentially revisiting tasks can reduce forgetting and improve generalization, especially when the tasks exhibit lower similarity in their data distributions \[[2502.10442v1](http://arxiv.org/abs/2502.10442v1)\]\[[1904.10644v1](http://arxiv.org/abs/1904.10644v1)\]\[[2011.12216v3](http://arxiv.org/abs/2011.12216v3)\]. Such findings underscore the importance of task similarity and ordering in continual learning dynamics, with task sequences that group similar tasks concurrently and revisit dissimilar tasks sequentially showing promising results \[[1904.10644v1](http://arxiv.org/abs/1904.10644v1)\]\[[2011.12216v3](http://arxiv.org/abs/2011.12216v3)\].

Complementary to these theoretical advances, empirical studies highlight that rehearsal strategies must be carefully designed to balance memory usage, overfitting, and generalization. For instance, rehearsal can lead to overfitting on the stored samples, limiting generalization performance, motivating the exploration of hybrid approaches that combine concurrent and sequential rehearsal modes \[[2104.07446v1](http://arxiv.org/abs/2104.07446v1)\]\[[2308.13646v2](http://arxiv.org/abs/2308.13646v2)\]. Hybrid rehearsal strategies leverage concurrent training for similar tasks to exploit shared representations while employing sequential revisiting for dissimilar tasks to minimize interference, demonstrating improved performance in deep neural networks \[[2110.11526v3](http://arxiv.org/abs/2110.11526v3)\]\[[2202.09826v3](http://arxiv.org/abs/2202.09826v3)\].

Beyond rehearsal, other methodologies have been proposed to mitigate catastrophic forgetting. Regularization-based approaches such as Elastic Weight Consolidation (EWC) and its variants impose constraints on parameter updates to preserve knowledge of previous tasks, conceptualized as a second-order Taylor approximation of task-specific loss functions \[[2006.10974v3](http://arxiv.org/abs/2006.10974v3)\]\[[1906.06635v1](http://arxiv.org/abs/1906.06635v1)\]. Bayesian continual learning frameworks extend this by maintaining posterior distributions over parameters and employing natural or Stein gradients to incorporate past knowledge effectively \[[1904.10644v1](http://arxiv.org/abs/1904.10644v1)\]\[[2312.17210v1](http://arxiv.org/abs/2312.17210v1)\]. Knowledge distillation and parameter regularization have also been integrated into rehearsal-free continual learning setups, especially with Vision Transformers, showing that parameter regularization can outperform more complex methods like EWC in some cases \[[2203.17269v2](http://arxiv.org/abs/2203.17269v2)\]\[[2203.13167v4](http://arxiv.org/abs/2203.13167v4)\].

Theoretical studies have further deepened understanding of forgetting mechanisms. Analyses of linear regression models trained with stochastic gradient descent reveal how task order, eigenvalue spectra of data covariances, and step sizes influence forgetting and generalization \[[2405.17583v1](http://arxiv.org/abs/2405.17583v1)\]\[[2502.10442v1](http://arxiv.org/abs/2502.10442v1)\]\[[2503.18511v1](http://arxiv.org/abs/2503.18511v1)\]. Overparameterization is identified as a factor that can mitigate forgetting by enlarging the parameter subspace accommodating multiple tasks \[[2502.10442v1](http://arxiv.org/abs/2502.10442v1)\]. Moreover, the Neural Tangent Kernel (NTK) framework has been used to quantify task similarity and its impact on forgetting, guiding algorithmic improvements such as orthogonal gradient descent variants \[[2010.04003v2](http://arxiv.org/abs/2010.04003v2)\].

Model architectural factors also affect forgetting. Wider neural networks tend to forget less catastrophically, possibly due to gradient orthogonality and sparse activations that reduce interference between tasks \[[2110.11526v3](http://arxiv.org/abs/2110.11526v3)\]. Dynamic architectures that conditionally share parameters or expand with new tasks have been proposed to balance plasticity and stability, including pruning and synaptic consolidation mechanisms inspired by biological memory processes \[[1906.06635v1](http://arxiv.org/abs/1906.06635v1)\]\[[1912.09091v3](http://arxiv.org/abs/1912.09091v3)\]\[[2504.10561v2](http://arxiv.org/abs/2504.10561v2)\].

Rehearsal policies themselves have been refined. Techniques like GRASP prioritize prototypical samples for rehearsal to reduce computational overhead while maintaining performance \[[2308.13646v2](http://arxiv.org/abs/2308.13646v2)\]. Brain-inspired methods such as REMIND replay compressed representations rather than raw data to improve efficiency and robustness in online continual learning \[[1910.02509v3](http://arxiv.org/abs/1910.02509v3)\]. Additionally, self-synthesized rehearsal frameworks generate synthetic data from large language models to overcome data availability constraints \[[2403.01244v2](http://arxiv.org/abs/2403.01244v2)\].

Finally, ensemble and multi-backbone models have been explored to improve continual learning performance by leveraging diverse representations, though at an increased computational cost. Recent advances in neural network subspace methods attempt to retain ensemble benefits with single-model efficiency \[[2202.09826v3](http://arxiv.org/abs/2202.09826v3)\]\[[2504.10561v2](http://arxiv.org/abs/2504.10561v2)\].

In summary, the literature on rehearsal in continual learning spans a spectrum from concurrent to sequential and hybrid rehearsal strategies, supported by theoretical and empirical evidence emphasizing task similarity and ordering. These approaches coexist with complementary methods such as regularization, Bayesian inference, architectural modifications, and advanced rehearsal policies. Together, they form a rich landscape for mitigating catastrophic forgetting and improving continual learning performance in diverse settings.

### References

1. [http://arxiv.org/abs/2203.17269v2]  
2. [http://arxiv.org/abs/2203.17269v2]  
3. [http://arxiv.org/abs/2405.17583v1]  
4. [http://arxiv.org/abs/2405.17583v1]  
5. [http://arxiv.org/abs/2405.17583v1]  
6. [http://arxiv.org/abs/2405.17583v1]  
8. [http://arxiv.org/abs/2405.09820v1]  
9. [http://arxiv.org/abs/2405.09820v1]  
10. [http://arxiv.org/abs/2006.10974v3]  
13. [http://arxiv.org/abs/2405.17583v1]  
15. [http://arxiv.org/abs/2312.17210v1]  
16. [http://arxiv.org/abs/1906.06635v1]  
17. [http://arxiv.org/abs/2203.13167v4]  
18. [http://arxiv.org/abs/2203.17269v2]  
19. [http://arxiv.org/abs/2010.04003v2]  
20. [http://arxiv.org/abs/1912.09091v3]  
22. [http://arxiv.org/abs/2403.01244v2]  
25. [http://arxiv.org/abs/2308.13646v2]  
29. [http://arxiv.org/abs/2504.10561v2]  
30. [http://arxiv.org/abs/1910.02509v3]