## Related Works

Multi-Domain Recommendation (MDR) has emerged as a promising approach to improve recommendation performance by leveraging knowledge transfer across different domains \[[1' 2023-02-12](http://arxiv.org/abs/2302.05990v2)\]. However, existing methods often adopt a single structure to transfer complex domain-shared knowledge, which can lead to the Negative Transfer Problem (NTP) when there is knowledge conflict or poor-quality domains \[[2' 2023-09-12](http://arxiv.org/abs/2309.06217v2)\]. This issue has been recognized in various contexts, including cross-domain sequential recommendation \[[3' 2023-11-22](http://arxiv.org/abs/2311.13188v1)\], where heterogeneous knowledge between dissimilar domains can lead to performance degradation \[[4' 2019-05-26](http://arxiv.org/abs/1905.10756v4)\]. 

Several approaches have been proposed to address the NTP. For instance, the work by \[[5' 2024-05-21](http://arxiv.org/abs/2405.12892v2)\] introduces a cooperative game theory framework to assess the extent of negative transfer and adaptively assign low weights to corresponding prediction losses. This method estimates the marginal contribution of each domain to model performance, offering a principled way to handle domain interactions \[[6' 2023-06-09](http://arxiv.org/abs/2306.06302v2)\]. Similarly, \[[7' 2022-01-04](http://arxiv.org/abs/2201.01002v1)\] proposes a hierarchical contrastive learning approach that incorporates information from coarse-level categories to mitigate negative transfer at the fine-level item level \[[8' 2022-01-15](http://arxiv.org/abs/2201.05867v1)\].

In the realm of domain adaptation, \[[9' 2018-12-15](http://arxiv.org/abs/1812.06229v1)\] presents a model that extracts both homogeneous and divergent features across domains, enabling equal support for all domains. This approach is particularly useful when the source domain is not accessible, as is often the case in real-world applications \[[10' 2025-04-29](http://arxiv.org/abs/2504.20371v3)\]. Additionally, \[[11' 2023-11-03](http://arxiv.org/abs/2311.01831v1)\] introduces a domain-to-domain translation model based on GANs, VAEs, and Cycle-Consistency to capture both similarities and differences among domains \[[12' 2023-06-30](http://arxiv.org/abs/2306.17555v2)\]. This model has shown significant improvements over state-of-the-art methods in multi-domain recommendation tasks \[[13' 2015-09-08](http://arxiv.org/abs/1509.02409v1)\].

Another line of research focuses on improving the adaptability of models to different domains. \[[14' 2024-02-09](http://arxiv.org/abs/2402.06213v2)\] proposes a method that leverages both high-level and pixel-level information for partial domain adaptation, using a reinforced transfer network to filter out outlier source samples \[[15' 2023-03-02](http://arxiv.org/abs/2303.01003v1)\]. This approach enhances the robustness of models in the presence of domain shifts \[[16' 2021-02-24](http://arxiv.org/abs/2102.12225v3)\]. Furthermore, \[[17' 2025-02-12](http://arxiv.org/abs/2502.08139v1)\] explores the use of negative control outcomes to select valid instrumental variables, which is relevant to the broader context of transfer learning and domain adaptation \[[18' 2024-04-26](http://arxiv.org/abs/2404.17450v2)\].

In summary, while existing methods have made progress in modeling cross-domain interactions, they often fail to account for the dynamic and complex nature of domain relationships. The proposed Similar Domain Selection Principle (SDSP) aims to address these limitations by dynamically selecting appropriate domains based on both supervised and unsupervised signals \[[19' 2020-06-17](http://arxiv.org/abs/2006.09807v1)\].

References:  
\[[1' 2023-02-12](http://arxiv.org/abs/2302.05990v2)\] http://arxiv.org/abs/2302.05990v2  
\[[2' 2023-09-12](http://arxiv.org/abs/2309.06217v2)\] http://arxiv.org/abs/2309.06217v2  
\[[3' 2023-11-22](http://arxiv.org/abs/2311.13188v1)\] http://arxiv.org/abs/2311.13188v1  
\[[4' 2019-05-26](http://arxiv.org/abs/1905.10756v4)\] http://arxiv.org/abs/2311.13188v1  
\[[5' 2024-05-21](http://arxiv.org/abs/2405.12892v2)\] http://arxiv.org/abs/2311.13188v1  
\[[6' 2023-06-09](http://arxiv.org/abs/2306.06302v2)\] http://arxiv.org/abs/2311.13188v1  
\[[7' 2022-01-04](http://arxiv.org/abs/2201.01002v1)\] http://arxiv.org/abs/2311.13188v1  
\[[8' 2022-01-15](http://arxiv.org/abs/2201.05867v1)\] http://arxiv.org/abs/2311.13188v1  
\[[9' 2018-12-15](http://arxiv.org/abs/1812.06229v1)\] http://arxiv.org/abs/1812.06229v1  
\[[10' 2025-04-29](http://arxiv.org/abs/2504.20371v3)\] http://arxiv.org/abs/1812.06229v1  
\[[11' 2023-11-03](http://arxiv.org/abs/2311.01831v1)\] http://arxiv.org/abs/2311.01831v1  
\[[12' 2023-06-30](http://arxiv.org/abs/2306.17555v2)\] http://arxiv.org/abs/2311.01831v1  
\[[13' 2015-09-08](http://arxiv.org/abs/1509.02409v1)\] http://arxiv.org/abs/2311.01831v1  
\[[14' 2024-02-09](http://arxiv.org/abs/2402.06213v2)\] http://arxiv.org/abs/1905.10756v4  
\[[15' 2023-03-02](http://arxiv.org/abs/2303.01003v1)\] http://arxiv.org/abs/1905.10756v4  
\[[16' 2021-02-24](http://arxiv.org/abs/2102.12225v3)\] http://arxiv.org/abs/1905.10756v4  
\[[17' 2025-02-12](http://arxiv.org/abs/2502.08139v1)\] http://arxiv.org/abs/2102.12225v3  
\[[18' 2024-04-26](http://arxiv.org/abs/2404.17450v2)\] http://arxiv.org/abs/2102.12225v3  
\[[19' 2020-06-17](http://arxiv.org/abs/2006.09807v1)\] http://arxiv.org/abs/2302.05990v2
