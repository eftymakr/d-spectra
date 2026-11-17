## Related Works

Rehearsal-based methods have become a cornerstone in continual learning (CL) for mitigating catastrophic forgetting by maintaining a buffer of past data samples and jointly training on both new and old data \[[2104.07446](http://arxiv.org/abs/2104.07446)\]\[[1902.10486](http://arxiv.org/abs/1902.10486)\]\[[2308.13646](http://arxiv.org/abs/2308.13646)\]. The dominant approach, concurrent rehearsal, trains on past and new data simultaneously, which has demonstrated strong empirical performance across various benchmarks \[[1805.12369](http://arxiv.org/abs/1805.12369)\]\[[1902.10486](http://arxiv.org/abs/1902.10486)\]. However, this strategy may not always be optimal, especially when task similarity varies.

The concept of sequential rehearsal, inspired by human learning where tasks are revisited in sequence rather than simultaneously, has recently gained attention. Theoretical analysis under overparameterized linear models shows that sequential rehearsal—training first on new data and then revisiting old data—can reduce forgetting and improve generalization when tasks are less similar \[[2302.05836](http://arxiv.org/abs/2302.05836)\]\[[2104.07446](http://arxiv.org/abs/2104.07446)\]. This finer-grained understanding clarifies the interplay between task similarity, rehearsal strategy, and forgetting dynamics, which was previously underexplored in CL literature.

Hybrid rehearsal approaches have been proposed to leverage the benefits of both concurrent and sequential rehearsal by training similar tasks concurrently and dissimilar tasks sequentially \[[2104.07446](http://arxiv.org/abs/2104.07446)\]. This strategy aligns with findings from ensemble and modular methods that combine distinct mechanisms to improve continual performance \[[2202.09826](http://arxiv.org/abs/2202.09826)\]\[[1906.00695](http://arxiv.org/abs/1906.00695)\]. Empirical studies with deep neural networks confirm that hybrid rehearsal outperforms standard concurrent rehearsal, particularly in challenging class-incremental settings \[[2104.07446](http://arxiv.org/abs/2104.07446)\]\[[1902.10486](http://arxiv.org/abs/1902.10486)\].

Beyond rehearsal, several alternative mechanisms have been developed to address catastrophic forgetting. Regularization-based methods, such as Elastic Weight Consolidation (EWC), penalize changes to important weights to preserve past knowledge but often require task identity and careful hyperparameter tuning \[[2211.13218](http://arxiv.org/abs/2211.13218)\]\[[2004.1407](http://arxiv.org/abs/2004.14070)\]. Knowledge distillation approaches transfer knowledge from earlier models or pre-trained networks to maintain performance but may struggle with domain shifts or task dissimilarity \[[2203.17269](http://arxiv.org/abs/2203.17269)\]\[[1710.10368](http://arxiv.org/abs/1710.10368)\]\[[2205.00329](http://arxiv.org/abs/2205.00329)\]. These methods typically underperform rehearsal-based methods when memory buffers are available \[[1708.02072](http://arxiv.org/abs/1708.02072)\].

Rehearsal-free continual learning has been advanced through prompt-based techniques, leveraging pre-trained foundation models and learning small sets of parameters (prompts) to instruct models without storing raw data \[[2112.08654](http://arxiv.org/abs/2112.08654)\]\[[2204.04799](http://arxiv.org/abs/2204.04799)\]\[[2211.13218](http://arxiv.org/abs/2211.13218)\]. These methods demonstrate promising performance, rivaling rehearsal-based approaches under memory constraints, but their efficacy in scenarios with large task heterogeneity remains an open question.

Generative replay techniques use generative models to synthesize past data and avoid storing raw samples, which mitigates privacy and memory issues \[[1710.10368](http://arxiv.org/abs/1710.10368)\]\[[1810.10612](http://arxiv.org/abs/1810.10612)\]\[[1809.02058](http://arxiv.org/abs/1809.02058)\]\[[1809.10635](http://arxiv.org/abs/1809.10635)\]. Although effective, generative replay often requires complex training and can be computationally intensive. Dual-memory architectures inspired by biological memory systems combine fast and slow learning components to reduce forgetting while accommodating new information \[[1710.10368](http://arxiv.org/abs/1710.10368)\]\[[1812.02464](http://arxiv.org/abs/1812.02464)\].

Sample selection policies for rehearsal buffers also directly impact continual learning effectiveness. Recent work on GRASP proposes selecting prototypical samples first and gradually harder examples, outperforming uniform sampling and reducing computational costs \[[2308.13646](http://arxiv.org/abs/2308.13646)\]. Similarly, selective experience replay strategies that match data distributions or maximize coverage have been shown to improve forgetting mitigation \[[1802.10269](http://arxiv.org/abs/1802.10269)\].

Theoretical frameworks continue to evolve to better characterize forgetting and generalization in CL. The Ideal Continual Learner (ICL) framework unifies memory-based, regularization, and expansion methods under a principled theory, offering insights into rehearsal’s impact on generalization \[[2305.00316](http://arxiv.org/abs/2305.00316)\]. Other analyses focus on task sequence properties such as total complexity and heterogeneity, revealing nuanced effects on forgetting that challenge previous assumptions \[[1908.01091](http://arxiv.org/abs/1908.01091)\]. Overparameterization and task ordering have also been shown to influence forgetting dynamics and generalization in both linear and deep models \[[2302.05836](http://arxiv.org/abs/2302.05836)\].

In summary, while concurrent rehearsal remains the standard approach in rehearsal-based CL, recent theoretical and empirical studies highlight the benefits of sequential and hybrid rehearsal strategies, particularly when task similarity is low \[[2302.05836](http://arxiv.org/abs/2302.05836)\]\[[2104.07446](http://arxiv.org/abs/2104.07446)\]. These insights motivate the design of adaptive rehearsal policies that account for task relationships. Moreover, the broader CL landscape includes complementary approaches such as prompt-based rehearsal-free methods, generative replay, regularization, and hybrid architectures, each with distinct trade-offs in memory, computation, and privacy \[[2203.17269](http://arxiv.org/abs/2203.17269)\]\[[2112.08654](http://arxiv.org/abs/2112.08654)\]\[[2211.13218](http://arxiv.org/abs/2211.13218)\]\[[1710.10368](http://arxiv.org/abs/1710.10368)\]\[[2204.04799](http://arxiv.org/abs/2204.04799)\]. The integration of theoretical advances with practical algorithms is driving continual learning toward more robust and efficient lifelong learning systems.

### References

\[[2302.05836](http://arxiv.org/abs/2302.05836)\] http://arxiv.org/abs/2302.05836  
\[[1805.12369](http://arxiv.org/abs/1805.12369)\] http://arxiv.org/abs/1805.12369  
\[[2104.07446](http://arxiv.org/abs/2104.07446)\] http://arxiv.org/abs/2104.07446  
\[[2203.17269](http://arxiv.org/abs/2203.17269)\] http://arxiv.org/abs/2203.17269  
\[[2112.08654](http://arxiv.org/abs/2112.08654)\] http://arxiv.org/abs/2112.08654  
9. http://arxiv.org/abs/1902.10486  
10. http://arxiv.org/abs/2006.10974  
11. http://arxiv.org/abs/2203.17269  
12. http://arxiv.org/abs/1810.10612  
14. http://arxiv.org/abs/1906.00695  
15. http://arxiv.org/abs/2308.13646  
16. http://arxiv.org/abs/1908.01091  
17. http://arxiv.org/abs/2305.00316  
18. http://arxiv.org/abs/1802.10269  
19. http://arxiv.org/abs/1809.02058  
20. http://arxiv.org/abs/2202.09826  
23. http://arxiv.org/abs/2004.14070  
25. http://arxiv.org/abs/1809.10635  
26. http://arxiv.org/abs/2204.04799  
28. http://arxiv.org/abs/1812.02464  
30. http://arxiv.org/abs/2205.00329