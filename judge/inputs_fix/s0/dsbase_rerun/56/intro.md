## Related Works

Cross-domain Sequential Recommendation (CDSR) has gained significant attention in recent years due to its ability to leverage user behavior across multiple domains to improve recommendation performance. Early approaches primarily focused on capturing sequential patterns within a single domain, often neglecting the rich cross-domain interactions that could enhance recommendation accuracy \[[1' 2020-12-01](http://arxiv.org/abs/2012.00485v3)\]. However, the challenge of modeling cross-domain preferences remains a critical issue, especially when user interactions are sparse or non-overlapping across domains \[[2' 2024-06-17](http://arxiv.org/abs/2406.11156v4)\].

A key limitation of existing CDSR methods is the reliance on overlapping users, which restricts their applicability in real-world scenarios where user data is often sparse or entirely non-overlapping \[[3' 2024-12-31](http://arxiv.org/abs/2502.15694v2)\]. This issue, referred to as the "overlap dilemma," limits the ability of models to generalize across domains \[[4' 2023-09-15](http://arxiv.org/abs/2309.08420v7)\]. Additionally, modeling complex transition patterns from mixed behavior sequences remains a significant challenge, as existing methods often fail to capture the nuanced relationships between items and users across domains \[[5' 2025-03-17](http://arxiv.org/abs/2503.13254v1)\].

To address these challenges, several works have explored the integration of advanced models and techniques. For instance, \[[6' 2024-01-10](http://arxiv.org/abs/2401.04971v4)\] proposed a mixed information flow network that considers both behavioral and knowledge transfer to improve cross-domain recommendations. This approach enables the model to dynamically decide when and how to use cross-domain information based on user preferences. Similarly, \[[7' 2025-04-21](http://arxiv.org/abs/2504.15085v5)\] introduced a framework that leverages large language models (LLMs) to enhance sequential recommendation by capturing semantic relationships between items and users. This work demonstrated that LLMs can effectively model complex user preferences and improve recommendation performance, especially in scenarios with limited data.

Another line of research focuses on improving the representation of items and users across domains. For example, \[[8' 2023-11-08](http://arxiv.org/abs/2311.04760v3)\] proposed a method that integrates item image information to better capture visual preferences, while \[[9' 2022-09-21](http://arxiv.org/abs/2209.10163v1)\] introduced a framework that uses frozen CLIP models to generate image and text embeddings, enriching item representations with multimodal data. These approaches highlight the importance of incorporating auxiliary information to enhance the modeling of cross-domain preferences.

Furthermore, \[[10' 2024-10-27](http://arxiv.org/abs/2410.20580v2)\] explored the use of federated learning to address privacy concerns and enable cross-domain knowledge sharing without sharing user data. This work introduced a framework that disentangles domain-specific and domain-shared features, allowing for more effective cross-domain learning while preserving data privacy. Similarly, \[[11' 2023-11-14](http://arxiv.org/abs/2311.08272v1)\] proposed a model that leverages dual dynamic graphs and hybrid metric training to improve the performance of CDSR by capturing both intra- and inter-domain sequential patterns.

In addition to these approaches, \[[12' 2023-11-08](http://arxiv.org/abs/2311.04590v6)\] introduced a contrastive cross-domain infomax objective to enhance the correlation between single- and cross-domain user representations, while \[[13' 2023-04-08](http://arxiv.org/abs/2304.03891v1)\] proposed a framework that models domain and feedback transitions to better capture user preferences across different domains. These works demonstrate the ongoing efforts to address the challenges of CDSR by incorporating advanced modeling techniques and leveraging diverse data sources.

Finally, \[[14' 2024-10-17](http://arxiv.org/abs/2410.13588v1)\] explored the use of automated prompting to address the non-overlapping cross-domain scenario, where no shared entities exist between domains. This work introduced a framework that learns domain-invariant and domain-specific representations to enable effective cross-domain recommendations without relying on shared users or content.

References  
\[[1' 2020-12-01](http://arxiv.org/abs/2012.00485v3)\] http://arxiv.org/abs/2401.04971v4  
\[[2' 2024-06-17](http://arxiv.org/abs/2406.11156v4)\] http://arxiv.org/abs/2502.15694v2  
\[[3' 2024-12-31](http://arxiv.org/abs/2502.15694v2)\] http://arxiv.org/abs/2309.08420v7  
\[[4' 2023-09-15](http://arxiv.org/abs/2309.08420v7)\] http://arxiv.org/abs/2503.13254v1  
\[[5' 2025-03-17](http://arxiv.org/abs/2503.13254v1)\] http://arxiv.org/abs/2311.04760v3  
\[[6' 2024-01-10](http://arxiv.org/abs/2401.04971v4)\] http://arxiv.org/abs/2012.00485v3  
\[[7' 2025-04-21](http://arxiv.org/abs/2504.15085v5)\] http://arxiv.org/abs/2406.11156v4  
\[[8' 2023-11-08](http://arxiv.org/abs/2311.04760v3)\] http://arxiv.org/abs/2502.15694v2  
\[[9' 2022-09-21](http://arxiv.org/abs/2209.10163v1)\] http://arxiv.org/abs/2504.15085v5  
\[[10' 2024-10-27](http://arxiv.org/abs/2410.20580v2)\] http://arxiv.org/abs/2309.08420v7  
\[[11' 2023-11-14](http://arxiv.org/abs/2311.08272v1)\] http://arxiv.org/abs/2209.10163v1  
\[[12' 2023-11-08](http://arxiv.org/abs/2311.04590v6)\] http://arxiv.org/abs/2304.03891v1  
\[[13' 2023-04-08](http://arxiv.org/abs/2304.03891v1)\] http://arxiv.org/abs/2408.08209v2  
\[[14' 2024-10-17](http://arxiv.org/abs/2410.13588v1)\] http://arxiv.org/abs/2304.04218v1
