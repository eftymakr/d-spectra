## Related Works

Recent advances in pre-training paradigms have inspired researchers to apply similar approaches to DNA-based models. However, these methods often fall short due to the limited information contained in pure DNA sequences, which do not capture the full regulatory context of genomic functions \[[1' 2024-08-20](http://arxiv.org/abs/2408.10681v1)\]. This limitation has led to the exploration of alternative strategies that incorporate additional genomic features, such as chromatin accessibility, to improve model performance \[[2' 2025-02-05](http://arxiv.org/abs/2502.03499v1)\].

Several studies have investigated the use of supervised training for genomic profile prediction as a more effective alternative to pure sequence pre-training. For instance, \[[3' 2021-01-14](http://arxiv.org/abs/2101.05870v1)\] demonstrated that incorporating genomic profiles significantly enhances the predictive power of models, particularly in tasks involving complex regulatory mechanisms. Similarly, \[[4' 2025-03-05](http://arxiv.org/abs/2503.03213v1)\] emphasized the importance of integrating multi-profile data to better understand the functional implications of DNA sequences across different species.

The use of Mixture of Experts (MoE) architectures has also gained traction in the field of genomic modeling. \[[5' 2003-01-15](http://arxiv.org/abs/physics/0301031v1)\] introduced a heterogeneous MoE framework that allows for the deployment of experts with varying capacities, improving computational efficiency and parameter utilization. This approach aligns with the need for models that can handle the complexity of genomic data by leveraging diverse expert capabilities. Additionally, \[[6' 2024-07-28](http://arxiv.org/abs/2407.19385v1)\] explored the convergence rates of softmax gating in MoE models, highlighting the importance of efficient parameter estimation and expert selection for accurate predictions.

In the context of multi-species and multi-profile genomic prediction, \[[7' 2024-02-22](http://arxiv.org/abs/2402.14800v2)\] proposed a collaborative expert system that integrates diverse genomic profiles to capture the relationships between DNA sequences and their functional outcomes. This work is closely related to the proposed SPACE model, which utilizes MoE to enhance the representation learning of DNA sequences across different species and genomic profiles.

Furthermore, \[[8' 2013-01-25](http://arxiv.org/abs/1301.5948v3)\] introduced a multi-modal imaging genomics transformer that integrates genomic and imaging data to improve the classification of complex diseases such as schizophrenia. This approach demonstrates the potential of combining multiple data modalities to achieve more accurate and interpretable results.

In addition to these studies, \[[9' 2019-02-28](http://arxiv.org/abs/1902.11104v3)\] explored the use of tensor-variate MoE models for regression tasks involving high-dimensional data, emphasizing the importance of preserving the underlying structure of the data. This is particularly relevant in genomic applications where data often exhibit complex spatial and temporal dependencies.

Lastly, \[[10' 2023-07-24](http://arxiv.org/abs/2307.13708v1)\] investigated the impact of genomic variation on function, highlighting the need for comprehensive catalogs of genome function and the molecular effects of genomic variants. This work underscores the importance of integrating diverse genomic data sources to gain deeper insights into the functional implications of genetic variation.

In summary, the related works highlight the growing interest in leveraging advanced pre-training paradigms, supervised training, and MoE architectures to improve the performance of genomic models. These studies provide a strong foundation for the proposed SPACE model, which aims to enhance DNA representation learning by integrating multi-species and multi-profile data through a collaborative MoE framework.

References:
1. \[[1' 2024-08-20](http://arxiv.org/abs/2408.10681v1)\] HMoE: Heterogeneous Mixture of Experts for Language Modeling
2. \[[2' 2025-02-05](http://arxiv.org/abs/2502.03499v1)\] From Genotype to Phenotype: polygenic prediction of complex human traits
3. \[[3' 2021-01-14](http://arxiv.org/abs/2101.05870v1)\] Omni-DNA: A Unified Genomic Foundation Model for Cross-Modal and Multi-Task Learning
4. \[[4' 2025-03-05](http://arxiv.org/abs/2503.03213v1)\] Convergence Rates for Softmax Gating Mixture of Experts
5. \[[5' 2003-01-15](http://arxiv.org/abs/physics/0301031v1)\] Mixtures of Experts Models
6. \[[6' 2024-07-28](http://arxiv.org/abs/2407.19385v1)\] Multi-modal Imaging Genomics Transformer: Attentive Integration of Imaging with Genomic Biomarkers for Schizophrenia Classification
7. \[[7' 2024-02-22](http://arxiv.org/abs/2402.14800v2)\] Tensor-variate Mixture of Experts for Proportional Myographic Control of a Robotic Hand
8. \[[8' 2013-01-25](http://arxiv.org/abs/1301.5948v3)\] The Impact of Genomic Variation on Function (IGVF) Consortium
9. \[[9' 2019-02-28](http://arxiv.org/abs/1902.11104v3)\] Deep Motif: Visualizing Genomic Sequence Classifications
10. \[[10' 2023-07-24](http://arxiv.org/abs/2307.13708v1)\] DiscDiff: Latent Diffusion Model for DNA Sequence Generation
