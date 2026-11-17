## Related Works

Rehearsal-based methods are among the most successful strategies to mitigate catastrophic forgetting in continual learning (CL) by storing and replaying samples from previously seen tasks alongside new data during training \[[2104.07446](http://arxiv.org/abs/2104.07446)\]\[[2302.05836](http://arxiv.org/abs/2302.05836)\]. These methods typically employ a buffer to maintain a subset of past data, which is interleaved with current task data in a concurrent manner. While effective, rehearsal strategies face challenges related to memory constraints, overfitting to the rehearsal buffer, and generalization limitations \[[2104.07446](http://arxiv.org/abs/2104.07446)\]\[[2207.04998](http://arxiv.org/abs/2207.04998)\]. Efforts to optimize rehearsal include advanced sample selection policies such as GRASP, which prioritizes prototypical examples to improve efficiency without additional memory overhead \[[2308.13646](http://arxiv.org/abs/2308.13646)\], and gradient-matching coresets that select samples to best approximate the gradient induced by the entire data distribution \[[2203.14544](http://arxiv.org/abs/2203.14544)\].

Inspired by human learning mechanisms, where sequential revisiting of tasks is common, recent work has begun to explore sequential rehearsal strategies. These approaches revisit previously learned tasks in a sequence rather than concurrently mixing old and new data, potentially reducing interference and improving retention, especially when tasks are dissimilar \[[2104.07446](http://arxiv.org/abs/2104.07446)\]\[[2103.07492](http://arxiv.org/abs/2103.07492)\]\[[2405.17583](http://arxiv.org/abs/2405.17583)\]. Theoretical foundations have been developed primarily in overparameterized linear models, which provide explicit characterizations of forgetting and generalization errors under different rehearsal regimes. These analyses reveal that sequential rehearsal can outperform concurrent rehearsal particularly when the similarity between tasks is low, as it mitigates cross-task interference more effectively \[[2103.07492](http://arxiv.org/abs/2103.07492)\]\[[2405.17583](http://arxiv.org/abs/2405.17583)\]\[[2502.10442](http://arxiv.org/abs/2502.10442)\].

Hybrid rehearsal methods that combine concurrent training for similar tasks and sequential rehearsal for dissimilar ones have been proposed to capitalize on the advantages of both strategies. Such hybrid approaches have shown promise in both theoretical analyses and empirical evaluations on deep neural networks, demonstrating superior performance over purely concurrent rehearsal \[[2104.07446](http://arxiv.org/abs/2104.07446)\]\[[2403.01244](http://arxiv.org/abs/2403.01244)\]\[[2202.09826](http://arxiv.org/abs/2202.09826)\]. Moreover, ensemble methods and routing networks that allocate different model components to subsets of tasks have also been explored to reduce forgetting by minimizing interference through structural separation \[[2202.09826](http://arxiv.org/abs/2202.09826)\]\[[2009.04381](http://arxiv.org/abs/2009.04381)\].

Beyond rehearsal, alternative approaches to continual learning include regularization-based methods like Elastic Weight Consolidation (EWC) and knowledge distillation techniques that preserve previously learned knowledge without explicit data replay \[[1810.10612](http://arxiv.org/abs/1810.10612)\]\[[2006.10974](http://arxiv.org/abs/2006.10974)\]\[[2203.17269](http://arxiv.org/abs/2203.17269)\]. While these methods offer benefits such as privacy preservation and reduced memory demands, they often require careful tuning and may not match rehearsal-based methods in scenarios involving class-incremental learning or long task sequences \[[2203.17269](http://arxiv.org/abs/2203.17269)\]\[[1904.07734](http://arxiv.org/abs/1904.07734)\]. Recent advances in parameter-efficient fine-tuning methods have also been adapted for rehearsal-free continual learning, achieving competitive results by leveraging pretrained models and lightweight adaptation mechanisms \[[2406.09384](http://arxiv.org/abs/2406.09384)\].

Theoretical studies have further deepened the understanding of factors influencing forgetting and generalization in CL. For instance, the role of overparameterization has been shown to be critical in reducing forgetting, as larger model capacity allows for better retention of sequential tasks \[[2502.10442](http://arxiv.org/abs/2502.10442)\]\[[2110.11526](http://arxiv.org/abs/2110.11526)\]\[[2408.16939](http://arxiv.org/abs/2408.16939)\]. The order and similarity of tasks also significantly affect forgetting dynamics, with task sequences arranged by eigenvalue spectra impacting the extent of catastrophic forgetting \[[2405.17583](http://arxiv.org/abs/2405.17583)\]\[[2010.04003](http://arxiv.org/abs/2010.04003)\]. Additionally, consistency regularization methods have been proposed to improve rehearsal efficacy by enforcing stability in model predictions, thereby enhancing robustness and reducing forgetting \[[2207.04998](http://arxiv.org/abs/2207.04998)\].

In reinforcement learning and large language models, pseudo-rehearsal and self-synthesized rehearsal approaches have been introduced to address the limitations of storing raw data, generating synthetic samples that serve as proxies for past experience and facilitating continual adaptation without explicit data storage \[[1812.02464](http://arxiv.org/abs/1812.02464)\]\[[2403.01244](http://arxiv.org/abs/2403.01244)\]. These methods demonstrate that rehearsal can be effectively approximated through generative models, expanding the applicability of continual learning in privacy-sensitive or data-scarce environments.

Overall, the landscape of rehearsal-based continual learning is evolving from conventional concurrent replay towards more nuanced strategies that consider task similarity, sequential revisiting, and hybrid methods. This shift is supported by a growing body of theoretical and empirical work that clarifies when and why sequential or hybrid rehearsal may be preferable, thus informing the design of more efficient and generalizable continual learning algorithms \[[2104.07446](http://arxiv.org/abs/2104.07446)\]\[[2103.07492](http://arxiv.org/abs/2103.07492)\]\[[2405.17583](http://arxiv.org/abs/2405.17583)\]\[[2202.09826](http://arxiv.org/abs/2202.09826)\]\[[2408.16939](http://arxiv.org/abs/2408.16939)\].

### References

1. http://arxiv.org/abs/2104.07446  
2. http://arxiv.org/abs/2203.14544  
3. http://arxiv.org/abs/2203.14544  
4. http://arxiv.org/abs/1812.02464  
5. http://arxiv.org/abs/2405.17583  
8. http://arxiv.org/abs/2405.09820  
9. http://arxiv.org/abs/2203.17269  
10. http://arxiv.org/abs/2006.10974  
11. http://arxiv.org/abs/2406.09384  
12. http://arxiv.org/abs/2308.13646  
13. http://arxiv.org/abs/2405.17583  
14. http://arxiv.org/abs/2202.09826  
15. http://arxiv.org/abs/2408.16939  
19. http://arxiv.org/abs/2006.10974  
21. http://arxiv.org/abs/1904.07734  
24. http://arxiv.org/abs/2502.10442  
25. http://arxiv.org/abs/2110.11526  
26. http://arxiv.org/abs/2207.04998  
28. http://arxiv.org/abs/2009.04381  
29. http://arxiv.org/abs/2010.04003  
