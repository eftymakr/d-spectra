## Related Works

Table discovery has emerged as a critical task in data management, especially with the proliferation of data lakes and repositories containing vast amounts of tabular data. Existing approaches primarily rely on keyword-based or query table-based retrieval, often leading to large result sets that require manual filtering \[[12](http://arxiv.org/abs/1802.06159)\]. This limitation highlights the need for more sophisticated methods that can incorporate natural language (NL) requirements to refine search results, a challenge that our proposed task, NL-conditional table discovery (nlcTD), aims to address \[[1](http://arxiv.org/abs/2105.01736)\].

Several works have explored table retrieval and union search, focusing on improving the accuracy and efficiency of these tasks. For instance, **StruBERT** introduces a structure-aware BERT model that fuses textual and structural information of tables to produce context-aware representations \[[2](http://arxiv.org/abs/2203.14278)\]. This model is used in an end-to-end neural ranking model to solve keyword- and content-based table retrieval and table similarity tasks. Similarly, **SANTOS** improves union search by considering semantic relationships between columns, leveraging both existing knowledge bases and synthesized knowledge from data lakes \[[5](http://arxiv.org/abs/2209.13589)\]. These methods demonstrate the importance of integrating structural and semantic information for more accurate table discovery.

In the realm of data lakes, **Dataset Discovery in Data Lakes** proposes a hash-based indexing approach to measure relatedness between tables based on their features, enabling efficient retrieval of relevant datasets \[[4](http://arxiv.org/abs/2011.10427)\]. This approach is further enhanced by **Starmie**, which employs contrastive learning to train column encoders from pre-trained language models, capturing rich contextual semantic information \[[6](http://arxiv.org/abs/2210.01922)\]. Starmie also introduces a filter-and-verification framework to compute unionability scores, significantly improving the effectiveness of table union search.

Efforts to enable semantic joins in data lakes have also been explored. **PEXESO** uses high-dimensional vector representations of textual values to identify joinable tables based on similarity predicates, addressing the limitations of equi-join approaches \[[8](http://arxiv.org/abs/2010.13273)\]. **DeepJoin** further advances this by using pre-trained language models (PLMs) to embed columns into a vector space, allowing for both equi- and semantic joins with high accuracy and efficiency \[[9](http://arxiv.org/abs/2212.07588)\]. These methods highlight the potential of leveraging semantic and structural information to improve joinability and relatedness between tables.

In addition, **TURL** presents a framework for table understanding through representation learning, pre-training on relational Web tables to capture semantics and knowledge from large-scale unlabeled data \[[7](http://arxiv.org/abs/2006.14806)\]. This approach is complemented by **ARDA**, which automates relational data augmentation for machine learning, enhancing predictive performance by enriching datasets with relevant attributes \[[10](http://arxiv.org/abs/2003.09758)\]. These systems demonstrate the importance of integrating semantic and structural information for effective data discovery and augmentation.

Finally, **LakeBench** provides a benchmark for discovering joinable and unionable tables in data lakes, offering a standardized evaluation framework for comparing different approaches \[[17]()\]. These benchmarks are essential for advancing research in table discovery and ensuring that new methods are evaluated against well-defined criteria.

1. \[[12](http://arxiv.org/abs/1802.06159)\]  
2. \[[2](http://arxiv.org/abs/2203.14278)\]  
3. \[[5](http://arxiv.org/abs/2209.13589)\]  
4. \[[4](http://arxiv.org/abs/2011.10427)\]  
5. \[[6](http://arxiv.org/abs/2210.01922)\]  
6. \[[8](http://arxiv.org/abs/2010.13273)\]  
7. \[[9](http://arxiv.org/abs/2212.07588)\]  
8. \[[7](http://arxiv.org/abs/2006.14806)\]  
9. \[[10](http://arxiv.org/abs/2003.09758)\]  
10. \[[17]()\]
