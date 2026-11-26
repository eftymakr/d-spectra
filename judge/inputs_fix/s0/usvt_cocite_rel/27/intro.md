## Related Works

Recent advancements in information retrieval have led to the development of various approaches for document and table retrieval. Traditional methods often rely on a separate indexing and retrieval pipeline, which can introduce error accumulation during the indexing phase and limit effective semantic alignment between queries and documents \[[14](http://arxiv.org/abs/2005.09207)\]. This limitation is particularly evident in dense vector search pipelines, where representation, indexing, and search are distinct stages \[[15](http://arxiv.org/abs/1906.00041)\]. These pipelines typically suffer from performance degradation due to the inability to directly optimize for the final retrieval target \[[3](http://arxiv.org/abs/2206.02743)\].

To address these limitations, differentiable search index (DSI) models have emerged as a promising alternative. DSI models unify indexing and retrieval within a single transformer model, allowing direct mapping of queries to document identifiers \[[2](http://arxiv.org/abs/2202.06991)\]. This approach eliminates the need for separate indexing and retrieval stages, thereby reducing error accumulation \[[1](http://arxiv.org/abs/2206.10128)\]. However, early DSI models faced challenges with data distribution mismatches between indexing and retrieval phases, especially in cross-lingual settings \[[1](http://arxiv.org/abs/2206.10128)\]. To mitigate this, DSI-QG was proposed, which generates relevant queries during indexing and re-ranks them using a cross-encoder ranker, improving alignment between queries and documents \[[1](http://arxiv.org/abs/2206.10128)\].

Similarly, the Neural Corpus Indexer (NCI) aims to unify training and indexing stages by using a sequence-to-sequence network that generates document identifiers directly for a given query \[[3](http://arxiv.org/abs/2206.02743)\]. NCI employs a prefix-aware weight-adaptive decoder and incorporates techniques such as query generation and semantic document identifiers to enhance recall performance \[[3](http://arxiv.org/abs/2206.02743)\]. This aligns with the idea of generating synthetic queries to improve query-document alignment, as seen in Birdie \[[1](http://arxiv.org/abs/2206.10128)\].

Autoregressive search engines have also been explored for document retrieval, where models generate and score distinctive ngrams as document identifiers \[[4](http://arxiv.org/abs/2204.10628)\]. This approach allows for efficient retrieval by mapping ngrams to full passages using an efficient data structure. It has been shown to outperform prior autoregressive methods and established retrieval solutions, achieving significant improvements on the KILT benchmark \[[4](http://arxiv.org/abs/2204.10628)\].

Continual learning in DSI models remains a challenge, as retraining the model for incremental indexing leads to forgetting of previously indexed documents \[[5](http://arxiv.org/abs/2212.09744)\]. DSI++ was introduced to address this issue by incorporating a generative memory that samples pseudo-queries during continual indexing, thereby preventing forgetting \[[5](http://arxiv.org/abs/2212.09744)\]. This is similar to the index update strategy in Birdie, which uses parameter isolation to mitigate catastrophic forgetting \[[1](http://arxiv.org/abs/2206.10128)\].

In the context of table retrieval, semantic similarity and contextualized language models have been leveraged to improve matching between queries and tables \[[10](http://arxiv.org/abs/1802.06159)\]. These approaches often involve encoding tables and queries into semantic spaces and using similarity measures to rank relevant tables \[[10](http://arxiv.org/abs/1802.06159)\]. This is closely related to the deep query-table interactions in Birdie, which are enabled by the encoder-decoder language model \[[1](http://arxiv.org/abs/2206.10128)\].

In summary, while traditional retrieval methods face limitations in error accumulation and semantic alignment, recent advances in differentiable search indices and autoregressive models have shown promising results. The proposed Birdie framework builds upon these advancements by unifying indexing and search within a single model and introducing strategies to mitigate forgetting during continual indexing.

1. \[[1](http://arxiv.org/abs/2206.10128)\] DSI-QG: Bridging the Gap Between Indexing and Retrieval for Differentiable Search Index with Query Generation  
2. \[[2](http://arxiv.org/abs/2202.06991)\] Transformer Memory as a Differentiable Search Index  
3. \[[3](http://arxiv.org/abs/2206.02743)\] A Neural Corpus Indexer for Document Retrieval  
4. \[[4](http://arxiv.org/abs/2204.10628)\] Autoregressive Search Engines: Generating Substrings as Document Identifiers  
5. \[[5](http://arxiv.org/abs/2212.09744)\] DSI++: Updating Transformer Memory with New Documents  
6. \[[6](http://arxiv.org/abs/2004.12832)\] ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT  
7. \[[7](http://arxiv.org/abs/2305.15115)\] Semantic-Enhanced Differentiable Search Index Inspired by Learning Strategies  
8. \[[8](https://www.semanticscholar.org/paper/d69c0ed04ecc852e8c921900d3e7967f74f81263)\] Pyserini: A Python Toolkit for Reproducible Information Retrieval Research with Sparse and Dense Representations  
9. \[[9](http://arxiv.org/abs/2004.04906)\] Dense Passage Retrieval for Open-Domain Question Answering  
10. \[[10](http://arxiv.org/abs/1802.06159)\] Ad Hoc Table Retrieval using Semantic Similarity  
11. \[[11](http://arxiv.org/abs/1910.14424)\] Multi-Stage Document Ranking with BERT  
12. \[[12](http://arxiv.org/abs/2208.07652)\] CorpusBrain: Pre-train a Generative Retrieval Model for Knowledge-Intensive Language Tasks  
13. \[[13](http://arxiv.org/abs/1207.0132)\] Answering Table Queries on the Web using Column Keywords  
14. \[[14](http://arxiv.org/abs/2005.09207)\] Table Search Using a Deep Contextualized Language Model  
15. \[[15](http://arxiv.org/abs/1906.00041)\] Table2Vec: Neural Word and Entity Embeddings for Table Population and Retrieval
