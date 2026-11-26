## Related Works

Cross-domain sequential recommendation (CDSR) has gained significant attention in recent years due to its ability to leverage user behavior across multiple domains to improve recommendation performance. Several approaches have been proposed to address the challenges of CDSR, primarily focusing on improving the modeling of cross-domain interactions and mitigating the cold-start problem. Most existing methods rely on self-attention mechanisms within transformer-based architectures, often incorporating domain-specific modules to enhance cross-domain learning \[[1' 2024-05-21](http://arxiv.org/abs/2405.12473v3)\]. However, these approaches typically overlook the potential of the self-attention module itself, which is a core component of the transformer architecture \[[2' 2018-10-10](http://arxiv.org/abs/1810.04650v2)\].

One line of work focuses on improving the self-attention mechanism by introducing domain-aware components or external attention mechanisms to better capture cross-domain dependencies \[[3' 2020-12-01](http://arxiv.org/abs/2012.00485v3)\]. For instance, \[[4' 2023-05-31](http://arxiv.org/abs/2305.19798v2)\] proposes a model that integrates external attention with graph convolution networks to enhance the modeling of cross-domain transitions. Similarly, \[[5' 2024-12-31](http://arxiv.org/abs/2502.15694v2)\] introduces a lightweight external attention-enhanced GCN-based framework that reduces computational complexity while maintaining performance. These methods aim to improve the alignment of user and item representations across domains, but they often require extensive hyperparameter tuning and may not be easily integrated into existing models \[[6' 2023-02-07](http://arxiv.org/abs/2302.03221v1)\].

Another approach to CDSR involves modeling the flow of information between domains, either through behavioral or knowledge transfer \[[7' 2024-08-15](http://arxiv.org/abs/2408.08209v2)\]. For example, \[[8' 2024-10-28](http://arxiv.org/abs/2410.21048v1)\] proposes a mixed information flow network that considers both the flow of behavioral information and the flow of knowledge by incorporating behavior and knowledge transfer units. This approach enables the model to dynamically decide when and how to use cross-domain information based on user preferences. Similarly, \[[9' 2022-09-21](http://arxiv.org/abs/2209.10163v1)\] introduces a dual-channel external attention component to capture cross-domain correlations efficiently. These methods highlight the importance of modeling both intra- and inter-domain interactions, but they often require complex architectures and may not be suitable for real-time applications \[[10' 2022-12-08](http://arxiv.org/abs/2212.04120v1)\].

Recent studies have also explored the use of multi-task learning and multi-objective optimization in CDSR to better balance the trade-offs between different tasks and objectives \[[11' 2023-04-09](http://arxiv.org/abs/2304.04218v1)\]. For example, \[[12' 2023-11-14](http://arxiv.org/abs/2311.08272v1)\] frames multi-task learning as a multi-objective optimization problem and proposes an upper bound for the multi-objective loss that can be optimized efficiently. This approach has been applied to various tasks, including digit classification and scene understanding, demonstrating its effectiveness in handling conflicting objectives \[[13' 2021-08-25](http://arxiv.org/abs/2108.11333v1)\]. In the context of CDSR, such methods could help balance the trade-offs between domain-specific and cross-domain learning, improving overall performance \[[14' 2022-06-16](http://arxiv.org/abs/2206.08050v1)\].

In addition to these methods, some works have focused on improving the efficiency and scalability of CDSR models, particularly in terms of computational complexity and memory usage \[[15' 2023-04-18](http://arxiv.org/abs/2304.09184v3)\]. For instance, \[[16' 2025-04-21](http://arxiv.org/abs/2504.15085v5)\] introduces a lightweight self-attentive network that reduces the number of parameters and computational overhead while maintaining high accuracy. This is particularly important for deploying models on resource-constrained devices or in real-time applications \[[17' 2025-04-29](http://arxiv.org/abs/2504.20859v1)\].

References  
\[[1' 2024-05-21](http://arxiv.org/abs/2405.12473v3)\] http://arxiv.org/abs/2405.12473v3  
\[[2' 2018-10-10](http://arxiv.org/abs/1810.04650v2)\] http://arxiv.org/abs/2405.12473v3  
\[[3' 2020-12-01](http://arxiv.org/abs/2012.00485v3)\] http://arxiv.org/abs/2405.12473v3  
\[[4' 2023-05-31](http://arxiv.org/abs/2305.19798v2)\] http://arxiv.org/abs/2302.03221v1  
\[[5' 2024-12-31](http://arxiv.org/abs/2502.15694v2)\] http://arxiv.org/abs/2302.03221v1  
\[[6' 2023-02-07](http://arxiv.org/abs/2302.03221v1)\] http://arxiv.org/abs/2302.03221v1  
\[[7' 2024-08-15](http://arxiv.org/abs/2408.08209v2)\] http://arxiv.org/abs/2012.00485v3  
\[[8' 2024-10-28](http://arxiv.org/abs/2410.21048v1)\] http://arxiv.org/abs/2012.00485v3  
\[[9' 2022-09-21](http://arxiv.org/abs/2209.10163v1)\] http://arxiv.org/abs/2302.03221v1  
\[[10' 2022-12-08](http://arxiv.org/abs/2212.04120v1)\] http://arxiv.org/abs/2302.03221v1  
\[[11' 2023-04-09](http://arxiv.org/abs/2304.04218v1)\] http://arxiv.org/abs/1810.04650v2  
\[[12' 2023-11-14](http://arxiv.org/abs/2311.08272v1)\] http://arxiv.org/abs/1810.04650v2  
\[[13' 2021-08-25](http://arxiv.org/abs/2108.11333v1)\] http://arxiv.org/abs/1810.04650v2  
\[[14' 2022-06-16](http://arxiv.org/abs/2206.08050v1)\] http://arxiv.org/abs/2302.03221v1  
\[[15' 2023-04-18](http://arxiv.org/abs/2304.09184v3)\] http://arxiv.org/abs/2108.11333v1  
\[[16' 2025-04-21](http://arxiv.org/abs/2504.15085v5)\] http://arxiv.org/abs/2108.11333v1  
\[[17' 2025-04-29](http://arxiv.org/abs/2504.20859v1)\] http://arxiv.org/abs/2108.11333v1
