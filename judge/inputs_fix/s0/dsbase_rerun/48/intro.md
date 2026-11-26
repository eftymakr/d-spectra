## Related Works

Neural retrieval methods using transformer-based pre-trained language models have advanced multilingual and cross-lingual retrieval \[[2' 2021-08-13](http://arxiv.org/abs/2108.06279v2)\]. However, their effectiveness for low-resource, morphologically rich languages such as Amharic remains underexplored due to data scarcity and suboptimal tokenization \[[15' 2025-03-24](http://arxiv.org/abs/2503.18570v1)\]. This challenge is not unique to Amharic; similar issues are observed in other low-resource languages, where tokenization and representation learning are critical for effective retrieval \[[1' 2025-04-14](http://arxiv.org/abs/2504.10335v2)\]. For instance, MorphTok proposes morphology-aware segmentation and Constrained BPE (CBPE) to improve tokenization for Indian languages, achieving a 1.68% reduction in fertility scores while maintaining comparable or improved downstream performance \[[1' 2025-04-14](http://arxiv.org/abs/2504.10335v2)\]. These advancements highlight the importance of language-specific tokenization strategies for robust retrieval in morphologically rich languages.

Dense retrieval has become the new paradigm in passage retrieval, leveraging pretrained language models (PLMs) to learn dense representations of queries and texts \[[4' 2022-11-27](http://arxiv.org/abs/2211.14876v1)\]. This approach enables semantic matching and has been extensively studied, with various architectures and training strategies proposed to improve retrieval effectiveness \[[22' 2022-03-21](http://arxiv.org/abs/2203.11163v2)\]. For example, the work on dense retrieval for low-resource languages, such as Amharic, demonstrates the need for language-specific adaptations and the challenges posed by data scarcity \[[15' 2025-03-24](http://arxiv.org/abs/2503.18570v1)\]. Similarly, the paper on improving the robustness of dense retrievers against typos via multi-positive contrastive learning highlights the importance of handling noisy and variant queries in low-resource settings \[[3' 2024-03-16](http://arxiv.org/abs/2403.10939v1)\].

In the context of multilingual and cross-lingual retrieval, several studies have explored the use of transfer learning and cross-lingual embeddings to address the lack of annotated data in low-resource languages \[[5' 2021-05-12](http://arxiv.org/abs/2105.05996v3)\]. For instance, the paper on multilingual offensive language identification uses cross-lingual contextual embeddings and transfer learning to make predictions in low-resource languages, achieving competitive performance on several datasets \[[5' 2021-05-12](http://arxiv.org/abs/2105.05996v3)\]. These approaches demonstrate the potential of leveraging high-resource language models for low-resource tasks, although challenges remain in adapting these models to specific linguistic and cultural contexts.

The development of language-specific models, such as the RoBERTa-Base-Amharic-Embed model introduced in this work, represents a significant step forward in addressing the unique challenges of low-resource languages \[[15' 2025-03-24](http://arxiv.org/abs/2503.18570v1)\]. This model outperforms existing multilingual baselines, such as Arctic Embed 2.0, in terms of retrieval effectiveness, as measured by MRR@10 and Recall@10 \[[15' 2025-03-24](http://arxiv.org/abs/2503.18570v1)\]. The success of this model underscores the importance of language-specific adaptation and the need for tailored approaches in low-resource settings. Furthermore, the use of late interaction retrieval models, such as the ColBERT-based model, highlights the potential of combining different retrieval strategies to achieve state-of-the-art performance \[[15' 2025-03-24](http://arxiv.org/abs/2503.18570v1)\].

1. \[[1' 2025-04-14](http://arxiv.org/abs/2504.10335v2)\] Document 1  
2. \[[2' 2021-08-13](http://arxiv.org/abs/2108.06279v2)\] Document 2  
3. \[[3' 2024-03-16](http://arxiv.org/abs/2403.10939v1)\] Document 3  
4. \[[4' 2022-11-27](http://arxiv.org/abs/2211.14876v1)\] Document 4  
5. \[[5' 2021-05-12](http://arxiv.org/abs/2105.05996v3)\] Document 5  
6. \[[6' 2021-03-14](http://arxiv.org/abs/2103.08052v2)\] Document 6  
7. \[[7' 2022-04-12](http://arxiv.org/abs/2204.05814v1)\] Document 7  
8. \[[8' 2024-03-31](http://arxiv.org/abs/2404.00684v1)\] Document 8  
9. \[[9' 2020-10-13](http://arxiv.org/abs/2010.06447v2)\] Document 9  
10. \[[10' 2025-01-09](http://arxiv.org/abs/2501.05260v1)\] Document 10  
11. \[[11' 2024-03-22](http://arxiv.org/abs/2404.07220v2)\] Document 11  
12. \[[12' 2024-11-06](http://arxiv.org/abs/2411.04316v1)\] Document 12  
13. \[[13' 2018-11-21](http://arxiv.org/abs/1811.08772v1)\] Document 13  
14. \[[14' 2016-01-18](http://arxiv.org/abs/1601.04605v1)\] Document 14  
15. \[[15' 2025-03-24](http://arxiv.org/abs/2503.18570v1)\] Document 15  
16. \[[16' 2023-04-04](http://arxiv.org/abs/2304.01492v5)\] Document 16  
17. \[[17' 2015-11-18](http://arxiv.org/abs/1511.05800v1)\] Document 17  
18. \[[18' 2024-11-01](http://arxiv.org/abs/2411.00727v2)\] Document 18  
19. \[[19' 2023-07-31](http://arxiv.org/abs/2307.16779v1)\] Document 19  
20. \[[20' 2024-12-13](http://arxiv.org/abs/2412.10008v1)\] Document 20  
21. \[[21' 2022-02-24](http://arxiv.org/abs/2202.12288v1)\] Document 21  
22. \[[22' 2022-03-21](http://arxiv.org/abs/2203.11163v2)\] Document 22  
23. \[[23' 2024-03-20](http://arxiv.org/abs/2403.13468v1)\] Document 23  
24. \[[24' 2018-07-02](http://arxiv.org/abs/1807.00745v2)\] Document 24  
25. \[[25' 2024-12-20](http://arxiv.org/abs/2412.16365v1)\] Document 25  
26. \[[26' 2018-04-21](http://arxiv.org/abs/1804.07878v2)\] Document 26  
27. \[[27' 2023-10-15](http://arxiv.org/abs/2310.09765v2)\] Document 27  
28. \[[28' 2024-07-29](http://arxiv.org/abs/2407.20114v3)\] Document 28  
29. \[[29' 2021-02-23](http://arxiv.org/abs/2102.11903v2)\] Document 29  
30. \[[30' 2024-11-24](http://arxiv.org/abs/2411.15766v1)\] Document 30
