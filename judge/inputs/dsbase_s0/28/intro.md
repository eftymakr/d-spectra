## Related Works

Active learning (AL) has been extensively studied for reducing annotation costs by selecting the most informative samples for labeling \[[Tatjana Legler' 2024-08-18](http://arxiv.org/abs/2408.09545v2)\]. However, AL methods often suffer from limited data diversity and annotation budget, especially in large-scale distributed settings \[[Sannara Ek' 2022-07-17](http://arxiv.org/abs/2207.08187v1)\]. Federated Active Learning (FAL) extends AL to distributed environments by enabling collaborative data selection and model training while preserving data privacy \[[Fuxun Yu' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\]. Despite these advancements, existing FAL approaches typically neglect the heterogeneity of data distributions across clients and the associated fluctuations in global and local model parameters, which can degrade model accuracy \[[Gergely D. Németh' 2025-04-15](http://arxiv.org/abs/2504.11216v2)\].

Several works have explored federated learning (FL) for handling heterogeneous data. FedDiverse addresses data heterogeneity by proposing a client selection algorithm that promotes collaboration between clients with complementary data distributions \[[Neta Shoham' 2019-10-17](http://arxiv.org/abs/1910.07796v1)\]. Similarly, FedFN introduces feature normalization to alleviate data heterogeneity in FL, improving model performance by reducing feature representation degradation \[[Chaoyang He' 2019-10-11](http://arxiv.org/abs/1910.04956v2)\]. These methods focus on improving model convergence and performance in non-IID settings but do not directly address the challenge of identifying informative samples in FAL.

Client adaptation techniques have also been proposed to enhance model performance in FL. For instance, Client Adaptation improves FL performance by introducing client-specific conditioning, which is particularly beneficial when data distributions differ significantly across clients \[[Lixuan Yang' 2020-11-12](http://arxiv.org/abs/2011.06393v1)\]. Additionally, FedCompass addresses client imbalance by using a computing power-aware scheduler to adaptively assign training tasks to clients, improving convergence and accuracy \[[Christopher Briggs' 2020-04-24](http://arxiv.org/abs/2004.11794v2)\]. These approaches aim to optimize FL performance but do not incorporate active learning strategies for sample selection.

In the realm of personalized FL, WAFFLE introduces a weighted averaging approach that leverages stochastic control variates to improve convergence \[[Laura Rieger' 2020-07-09](http://arxiv.org/abs/2007.04806v1)\]. FedCor proposes a correlation-based client selection strategy to enhance FL convergence by considering loss correlations between clients \[[Deepesh Data' 2020-06-22](http://arxiv.org/abs/2006.13041v2)\]. These methods focus on improving model personalization and convergence but do not integrate active learning for data selection.

The integration of active learning into FL is a relatively new area. FedCor addresses the issue of client-wise data heterogeneity by proposing a correlation-based selection strategy \[[Deepesh Data' 2020-06-22](http://arxiv.org/abs/2006.13041v2)\]. Similarly, FedMD uses model distillation to enable personalized FL, allowing each client to maintain its own model while contributing to a global model \[[Davide Cacciarelli' 2023-02-17](http://arxiv.org/abs/2302.08893v4)\]. These methods highlight the potential of combining active learning with FL to improve model performance and data efficiency.

In summary, while existing FL and FAL methods have made significant strides in addressing data heterogeneity, model personalization, and communication efficiency, there remains a gap in effectively selecting informative samples for annotation in FAL. CHASe addresses this gap by focusing on identifying samples with high epistemic variations, which are critical for improving model accuracy and efficiency in FAL \[[Tianyi Chen' 2020-07-12](http://arxiv.org/abs/2007.06081v1)\].

### References

1. \[[Tatjana Legler' 2024-08-18](http://arxiv.org/abs/2408.09545v2)\] [Document 1](http://arxiv.org/abs/2207.02337v1)  
2. \[[Sannara Ek' 2022-07-17](http://arxiv.org/abs/2207.08187v1)\] [Document 2](http://arxiv.org/abs/2504.11216v2)  
3. \[[Fuxun Yu' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\] [Document 3](http://arxiv.org/abs/2007.06081v1)  
4. \[[Gergely D. Németh' 2025-04-15](http://arxiv.org/abs/2504.11216v2)\] [Document 4](http://arxiv.org/abs/2007.04806v1)  
5. \[[Neta Shoham' 2019-10-17](http://arxiv.org/abs/1910.07796v1)\] [Document 5](http://arxiv.org/abs/2010.13723v3)  
6. \[[Chaoyang He' 2019-10-11](http://arxiv.org/abs/1910.04956v2)\] [Document 6](http://arxiv.org/abs/2112.09429v2)  
7. \[[Lixuan Yang' 2020-11-12](http://arxiv.org/abs/2011.06393v1)\] [Document 7](http://arxiv.org/abs/1910.09933v2)  
8. \[[Christopher Briggs' 2020-04-24](http://arxiv.org/abs/2004.11794v2)\] [Document 8](http://arxiv.org/abs/2008.06767v2)  
9. \[[Laura Rieger' 2020-07-09](http://arxiv.org/abs/2007.04806v1)\] [Document 9](http://arxiv.org/abs/2006.12097v3)  
10. \[[Deepesh Data' 2020-06-22](http://arxiv.org/abs/2006.13041v2)\] [Document 10](http://arxiv.org/abs/1910.04956v2)  
11. \[[Davide Cacciarelli' 2023-02-17](http://arxiv.org/abs/2302.08893v4)\] [Document 11](http://arxiv.org/abs/2308.00155v1)  
12. \[[Tianyi Chen' 2020-07-12](http://arxiv.org/abs/2007.06081v1)\] [Document 12](http://arxiv.org/abs/2206.05507v1)
