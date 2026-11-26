## Related Works

Natural language-driven table discovery has emerged as a critical task in modern data lake management, enabling users to identify relevant tables based on semantic queries \[[2](http://arxiv.org/abs/2212.07588)\]. Traditional approaches rely on a dense vector search pipeline, which involves representation, indexing, and search stages \[[9](http://arxiv.org/abs/2005.09207)\]. However, these methods face limitations such as error accumulation during representation and indexing, and insufficient query-table interaction that hinders semantic alignment \[[1](http://arxiv.org/abs/2106.09592)\]. 

Several studies have explored alternative methods to improve the accuracy and efficiency of table discovery. For instance, DeepJoin proposes a deep learning model that uses pre-trained language models (PLMs) to perform embedding-based retrieval for both equi- and semantic joins \[[2](http://arxiv.org/abs/2212.07588)\]. This approach leverages contextualization options to transform column contents into text sequences, allowing the PLM to fine-tune embeddings for joinable columns \[[2](http://arxiv.org/abs/2212.07588)\]. While DeepJoin improves precision, it still relies on a traditional indexing mechanism, which can introduce errors during the search phase \[[2](http://arxiv.org/abs/2212.07588)\].

Starmie introduces a framework that uses contextualized column-based representation learning to enhance dataset discovery from data lakes \[[3](http://arxiv.org/abs/2210.01922)\]. It employs a contrastive learning method to train column encoders from pre-trained language models, capturing rich semantic information \[[3](http://arxiv.org/abs/2210.01922)\]. The framework also utilizes cosine similarity between column embeddings to compute unionability scores and incorporates a filter-and-verification mechanism for efficient search \[[3](http://arxiv.org/abs/2210.01922)\]. Starmie outperforms existing solutions in effectiveness and performance, particularly with the use of the HNSW index for faster query processing \[[3](http://arxiv.org/abs/2210.01922)\].

Solo proposes a self-supervised approach to enable natural language question answering over data lakes without requiring expensive training data \[[4](http://arxiv.org/abs/2301.03560)\]. It combines techniques for data discovery, table representation, and relevance modeling into a single system, demonstrating improvements over state-of-the-art approaches on well-known benchmarks \[[4](http://arxiv.org/abs/2301.03560)\]. This work highlights the potential of self-supervised learning in building learned discovery systems \[[4](http://arxiv.org/abs/2301.03560)\].

TAPAS addresses the challenge of answering natural language questions over tables without generating logical forms \[[6](http://arxiv.org/abs/2004.02349)\]. It trains from weak supervision and predicts denotations by selecting table cells and applying aggregation operators \[[6](http://arxiv.org/abs/2004.02349)\]. TAPAS extends BERT’s architecture to encode tables and achieves state-of-the-art results on semantic parsing tasks \[[6](http://arxiv.org/abs/2004.02349)\].

Ad Hoc Table Retrieval using Semantic Similarity introduces a method for semantic matching between queries and tables by representing them in multiple semantic spaces and using various similarity measures \[[8](http://arxiv.org/abs/1802.06159)\]. This approach significantly improves retrieval performance over state-of-the-art baselines \[[8](http://arxiv.org/abs/1802.06159)\].

Table Search Using a Deep Contextualized Language Model investigates how to encode table content using BERT, considering table structure and input length constraints \[[9](http://arxiv.org/abs/2005.09207)\]. It also integrates features from prior literature and jointly trains them with BERT, achieving superior performance on public datasets \[[9](http://arxiv.org/abs/2005.09207)\].

Transformer Memory as a Differentiable Search Index introduces the Differentiable Search Index (DSI), a paradigm where a single Transformer model encodes all information about the corpus \[[10](http://arxiv.org/abs/2202.06991)\]. This approach simplifies the retrieval process and demonstrates strong generalization capabilities \[[10](http://arxiv.org/abs/2202.06991)\].

These works collectively highlight the evolving landscape of table discovery and retrieval, emphasizing the need for more robust and efficient methods that address the limitations of traditional approaches \[[2](http://arxiv.org/abs/2212.07588)\]\[[3](http://arxiv.org/abs/2210.01922)\]\[[4](http://arxiv.org/abs/2301.03560)\]\[[6](http://arxiv.org/abs/2004.02349)\]\[[8](http://arxiv.org/abs/1802.06159)\]\[[9](http://arxiv.org/abs/2005.09207)\]\[[10](http://arxiv.org/abs/2202.06991)\]. 

References  
\[[1](http://arxiv.org/abs/2106.09592)\] The paper abstract  
\[[2](http://arxiv.org/abs/2212.07588)\] DeepJoin: Joinable Table Discovery with Pre-trained Language Models  
\[[3](http://arxiv.org/abs/2210.01922)\] Semantics-aware Dataset Discovery from Data Lakes with Contextualized Column-based Representation Learning  
\[[4](http://arxiv.org/abs/2301.03560)\] Solo: Data Discovery Using Natural Language Questions Via A Self-Supervised Approach  
\[[6](http://arxiv.org/abs/2004.02349)\] TAPAS: Weakly Supervised Table Parsing via Pre-training  
\[[8](http://arxiv.org/abs/1802.06159)\] Ad Hoc Table Retrieval using Semantic Similarity  
\[[9](http://arxiv.org/abs/2005.09207)\] Table Search Using a Deep Contextualized Language Model  
\[[10](http://arxiv.org/abs/2202.06991)\] Transformer Memory as a Differentiable Search Index
