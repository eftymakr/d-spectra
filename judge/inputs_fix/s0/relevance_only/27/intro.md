## Related Works

Recent advancements in table retrieval have focused on leveraging deep learning techniques to improve the accuracy and efficiency of identifying relevant tables based on natural language queries. Traditional approaches often rely on a representation-index-search pipeline, where tables are represented as dense vectors, indexed, and then searched using these vectors \[[14](http://arxiv.org/abs/2105.06365)\]. However, these methods face significant limitations, including error accumulation during the indexing phase and insufficient interaction between queries and tables, which hinders semantic alignment \[[1](http://arxiv.org/abs/2005.09207)\]. 

Several studies have explored alternative approaches to address these limitations. For instance, \[[14](http://arxiv.org/abs/2105.06365)\] introduced a semantic table retrieval framework that represents queries and tables in multiple semantic spaces and uses various similarity measures to improve matching. This work demonstrated significant improvements over existing baselines by incorporating both discrete and continuous vector representations \[[14](http://arxiv.org/abs/2105.06365)\]. Similarly, \[[15](http://arxiv.org/abs/1802.06159)\] proposed a method for semantic matching between queries and tables, which also considered multiple semantic spaces and similarity measures, leading to better performance on Wikipedia-based test collections \[[15](http://arxiv.org/abs/1802.06159)\].

The Differentiable Search Index (DSI) has emerged as a promising paradigm that unifies indexing and retrieval into a single model, enabling more direct and efficient query-to-table mapping \[[5](http://arxiv.org/abs/2206.10128)\]. DSI models encode all documents into the model parameters and use a sequence-to-sequence architecture to directly map queries to relevant document identifiers \[[5](http://arxiv.org/abs/2206.10128)\]. However, early DSI implementations faced challenges in distinguishing relevant documents from random ones, which affected retrieval effectiveness \[[2](http://arxiv.org/abs/2305.02073)\]. To address this, researchers proposed multi-task distillation approaches to enhance retrieval quality without altering the model structure \[[2](http://arxiv.org/abs/2305.02073)\]. Additionally, the DSI-QG framework was introduced to mitigate data distribution mismatches by generating relevant queries during indexing \[[5](http://arxiv.org/abs/2206.10128)\].

In the context of dynamic table indexing, the IncDSI model enables real-time updates to the retrieval system without retraining the entire model, allowing for incremental addition of new documents with minimal computational overhead \[[7](http://arxiv.org/abs/2307.10323)\]. This is particularly useful for applications requiring continuous updates to the table repository. Furthermore, the DSI++ model was developed to address catastrophic forgetting during continual learning by introducing techniques such as flatter loss basins and generative memory \[[13](http://arxiv.org/abs/2212.09744)\].

The nlcTables dataset was created to support the development of more advanced NL-conditional table discovery methods, providing a comprehensive benchmark with diverse queries and relevance annotations \[[3](http://arxiv.org/abs/2504.15849)\]. This dataset highlights the need for more sophisticated techniques to handle complex NL conditions in table discovery \[[3](http://arxiv.org/abs/2504.15849)\].

In summary, while traditional dense vector-based methods have achieved notable success, recent works such as DSI, IncDSI, and nlcTables have introduced novel approaches that address key limitations in table retrieval, particularly in terms of semantic alignment, error accumulation, and dynamic indexing \[[3](http://arxiv.org/abs/2504.15849)\]\[[5](http://arxiv.org/abs/2206.10128)\]\[[7](http://arxiv.org/abs/2307.10323)\]\[[13](http://arxiv.org/abs/2212.09744)\].

References:  
\[[1](http://arxiv.org/abs/2005.09207)\] http://arxiv.org/abs/2005.09207  
\[[2](http://arxiv.org/abs/2305.02073)\] http://arxiv.org/abs/2305.02073  
\[[3](http://arxiv.org/abs/2504.15849)\] http://arxiv.org/abs/2504.15849  
\[[5](http://arxiv.org/abs/2206.10128)\] http://arxiv.org/abs/2305.15115  
\[[7](http://arxiv.org/abs/2307.10323)\] http://arxiv.org/abs/2307.10323  
\[[13](http://arxiv.org/abs/2212.09744)\] http://arxiv.org/abs/2212.09744  
\[[14](http://arxiv.org/abs/2105.06365)\] http://arxiv.org/abs/2105.06365  
\[[15](http://arxiv.org/abs/1802.06159)\] http://arxiv.org/abs/1802.06159
