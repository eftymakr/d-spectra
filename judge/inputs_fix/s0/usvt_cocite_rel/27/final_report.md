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
## Research papers
### Outline
- [Differentiable Search Index (DSI) Models [4 papers]](#category-differentiable-search-index-(dsi)-models)
- [Autoregressive Search Engine Approaches [1 papers]](#category-autoregressive-search-engine-approaches)
- [Continual Learning and Catastrophic Forgetting [1 papers]](#category-continual-learning-and-catastrophic-forgetting)
- [Efficient Data Structures for Retrieval [1 papers]](#category-efficient-data-structures-for-retrieval)
- [Evaluation Benchmarks and Performance Metrics [1 papers]](#category-evaluation-benchmarks-and-performance-metrics)
- [Traditional Retrieval Pipelines and Their Limitations [1 papers]](#category-traditional-retrieval-pipelines-and-their-limitations)
- [Semantic Similarity in Table Retrieval [3 papers]](#category-semantic-similarity-in-table-retrieval)
- [Pre-training and Fine-tuning Strategies [3 papers]](#category-pre-training-and-fine-tuning-strategies)

### <a id='category-differentiable-search-index-(dsi)-models'></a>Differentiable Search Index (DSI) Models: 4 papers found.
Differentiable Search Index (DSI) models represent a novel paradigm in information retrieval, where a single transformer model is used for both indexing and retrieval, eliminating the need for separate index-building and search stages \[[2](http://arxiv.org/abs/2202.06991)\]. This approach directly maps queries to document identifiers, leveraging the model's parameters to encode all necessary information about the corpus \[[2](http://arxiv.org/abs/2202.06991)\]. However, existing DSI models face challenges such as data distribution mismatches between indexing and retrieval, particularly when dealing with cross-lingual scenarios \[[1](http://arxiv.org/abs/2206.10128)\]. To address these issues, researchers have proposed enhancements like DSI-QG, which introduces query generation during indexing to better align with retrieval queries \[[1](http://arxiv.org/abs/2206.10128)\]. Similarly, the Neural Corpus Indexer (NCI) improves recall performance by integrating query generation, semantic document identifiers, and consistency-based regularization \[[3](http://arxiv.org/abs/2206.02743)\]. Additionally, the Semantic-Enhanced DSI (SE-DSI) model draws inspiration from cognitive psychology, using elaborative descriptions and rehearsal strategies to enhance document memorization and semantic alignment \[[4](http://arxiv.org/abs/2204.10628)\]. These advancements highlight the ongoing efforts to refine DSI models, ensuring they can effectively handle complex retrieval tasks while maintaining robustness and adaptability.
|    | reference                                                                                                                                | date     | key idea/summary                                                                                                                                                                                                                                                                                       |
|----|------------------------------------------------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Bridging the Gap Between Indexing and Retrieval for Differentiable Search Index with Query Generation](http://arxiv.org/abs/2206.10128) | 06/21/22 | DSI-QG is a novel indexing framework for Differentiable Search Index (DSI) that addresses data distribution mismatches by generating and using relevant queries during indexing to improve retrieval performance.                                                                                      |
|  1 | [Transformer Memory as a Differentiable Search Index](http://arxiv.org/abs/2202.06991)                                                   | 02/14/22 | The paper introduces the Differentiable Search Index (DSI), a novel paradigm that uses a single Transformer model to directly answer queries by encoding all corpus information into its parameters, significantly simplifying the information retrieval process and outperforming existing baselines. |
|  2 | [A Neural Corpus Indexer for Document Retrieval](http://arxiv.org/abs/2206.02743)                                                        | 06/06/22 | The paper introduces Neural Corpus Indexer (NCI), an end-to-end deep neural network that improves recall performance in document retrieval by unifying training and indexing stages with a prefix-aware weight-adaptive decoder and tailored techniques.                                               |
|  3 | [Semantic-Enhanced Differentiable Search Index Inspired by Learning Strategies](http://arxiv.org/abs/2305.15115)                         | 05/24/23 | The Semantic-Enhanced DSI model (SE-DSI) improves document retrieval by incorporating cognitive psychology-inspired strategies, using elaborative descriptions and semantic features to enhance document memorization and retrieval performance.                                                       |
### <a id='category-autoregressive-search-engine-approaches'></a>Autoregressive Search Engine Approaches: 1 papers found.
Context: 
	Document 1: [_citation_number]: «4»
[Snippet]: «Knowledge-intensive language tasks require NLP systems to both provide the correct answer and retrieve supporting evidence for it in a given corpus. Autoregressive language models are emerging as the de-facto standard for generating answers, with newer and more powerful systems emerging at an astonishing pace. In this paper we argue that all this (and future) progress can be directly applied to the retrieval problem with minimal intervention to the models' architecture. Previous work has explored ways to partition the search space into hierarchical structures and retrieve documents by autoregressively generating their unique identifier. In this work we propose an alternative that doesn't force any structure in the search space: using all ngrams in a passage as its possible identifiers. This setup allows us to use an autoregressive model to generate and score distinctive ngrams, that are then mapped to full passages through an efficient data structure. Empirically, we show this not only outperforms prior autoregressive approaches but also leads to an average improvement of at least 10 points over more established retrieval solutions for passage-level retrieval on the KILT benchmark, establishing new state-of-the-art downstream performance on some datasets, while using a considerably lighter memory footprint than competing systems. Code and pre-trained models at https://github.com/facebookresearch/SEAL.»
[Category]: «Autoregressive Search Engine Approaches»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2206.02743)\]. Further details \[[6](http://arxiv.org/abs/2004.12832)\]\[[7](http://arxiv.org/abs/2305.15115)\]\[[8](https://www.semanticscholar.org/paper/d69c0ed04ecc852e8c921900d3e7967f74f81263)\]\[[9](http://arxiv.org/abs/2004.04906)\]\[[10](http://arxiv.org/abs/1802.06159)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from
large table repositories based on NL queries. While current deep-learning-based
methods using the traditional dense vector search pipeline, i.e.,
representation-index-search, achieve remarkable accuracy, they face several
limitations that impede further performance improvements: (i) the errors
accumulated during the table representation and indexing phases affect the
subsequent search accuracy; and (ii) insufficient query-table interaction
hinders effective semantic alignment, impeding accuracy improvements. In this
paper, we propose a novel framework Birdie, using a differentiable search
index. It unifies the indexing and search into a single encoder-decoder
language model, thus getting rid of error accumulations. Birdie first assigns
each table a prefix-aware identifier and leverages a large language model-based
query generator to create synthetic queries for each table. It then encodes the
mapping between synthetic queries/tables and their corresponding table
identifiers into the parameters of an encoder-decoder language model, enabling
deep query-table interactions. During search, the trained model directly
generates table identifiers for a given query. To accommodate the continual
indexing of dynamic tables, we introduce an index update strategy via parameter
isolation, which mitigates the issue of catastrophic forgetting. Extensive
experiments demonstrate that Birdie outperforms state-of-the-art dense methods
by 16.8% in accuracy, and reduces forgetting by over 90% compared to other
continual learning approaches.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2206.02743)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2202.06991)\]\[[7](http://arxiv.org/abs/2305.15115)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Autoregressive search engine approaches have gained traction for their ability to generate and score distinctive identifiers for documents, enabling more accurate retrieval. These methods leverage autoregressive language models to directly generate identifiers, such as ngrams, from passages, which are then mapped to full documents using efficient data structures \[[4](http://arxiv.org/abs/2204.10628)\]. This approach differs from traditional hierarchical search methods that partition the search space into structured segments, as it avoids imposing such constraints \[[4](http://arxiv.org/abs/2204.10628)\]. By using all ngrams as potential identifiers, the model can capture a richer set of features, leading to improved performance on tasks like passage-level retrieval \[[4](http://arxiv.org/abs/2204.10628)\]. Empirical results show that this method outperforms prior autoregressive approaches and achieves an average improvement of at least 10 points over established retrieval solutions on the KILT benchmark \[[4](http://arxiv.org/abs/2204.10628)\]. Additionally, this setup offers a lighter memory footprint compared to competing systems, making it a promising direction for future research in information retrieval.
|    | reference                                                                                                       | date     | key idea/summary                                                                                                                                                                                    |
|----|-----------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Autoregressive Search Engines: Generating Substrings as Document Identifiers](http://arxiv.org/abs/2204.10628) | 04/22/22 | The paper proposes an autoregressive approach for passage-level retrieval that uses all ngrams in a passage as identifiers, achieving state-of-the-art performance with a lighter memory footprint. |
### <a id='category-continual-learning-and-catastrophic-forgetting'></a>Continual Learning and Catastrophic Forgetting: 1 papers found.
Context: 
	Document 1: [_citation_number]: «5»
[Snippet]: «Differentiable Search Indices (DSIs) encode a corpus of documents in model parameters and use the same model to answer user queries directly. Despite the strong performance of DSI models, deploying them in situations where the corpus changes over time is computationally expensive because reindexing the corpus requires re-training the model. In this work, we introduce DSI++, a continual learning challenge for DSI to incrementally index new documents while being able to answer queries related to both previously and newly indexed documents. Across different model scales and document identifier representations, we show that continual indexing of new documents leads to considerable forgetting of previously indexed documents. We also hypothesize and verify that the model experiences forgetting events during training, leading to unstable learning. To mitigate these issues, we investigate two approaches. The first focuses on modifying the training dynamics. Flatter minima implicitly alleviate forgetting, so we optimize for flatter loss basins and show that the model stably memorizes more documents ($+12\%$). Next, we introduce a generative memory to sample pseudo-queries for documents and supplement them during continual indexing to prevent forgetting for the retrieval task. Extensive experiments on novel continual indexing benchmarks based on Natural Questions (NQ) and MS MARCO demonstrate that our proposed solution mitigates forgetting significantly. Concretely, it improves the average Hits@10 by $+21.1\%$ over competitive baselines for NQ and requires $6$ times fewer model updates compared to re-training the DSI model for incrementally indexing five corpora in a sequence.»
[Category]: «Continual Learning and Catastrophic Forgetting»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2206.02743)\]. Further details \[[6](http://arxiv.org/abs/2004.12832)\]\[[7](http://arxiv.org/abs/2305.15115)\]\[[8](https://www.semanticscholar.org/paper/d69c0ed04ecc852e8c921900d3e7967f74f81263)\]\[[9](http://arxiv.org/abs/2004.04906)\]\[[10](http://arxiv.org/abs/1802.06159)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from
large table repositories based on NL queries. While current deep-learning-based
methods using the traditional dense vector search pipeline, i.e.,
representation-index-search, achieve remarkable accuracy, they face several
limitations that impede further performance improvements: (i) the errors
accumulated during the table representation and indexing phases affect the
subsequent search accuracy; and (ii) insufficient query-table interaction
hinders effective semantic alignment, impeding accuracy improvements. In this
paper, we propose a novel framework Birdie, using a differentiable search
index. It unifies the indexing and search into a single encoder-decoder
language model, thus getting rid of error accumulations. Birdie first assigns
each table a prefix-aware identifier and leverages a large language model-based
query generator to create synthetic queries for each table. It then encodes the
mapping between synthetic queries/tables and their corresponding table
identifiers into the parameters of an encoder-decoder language model, enabling
deep query-table interactions. During search, the trained model directly
generates table identifiers for a given query. To accommodate the continual
indexing of dynamic tables, we introduce an index update strategy via parameter
isolation, which mitigates the issue of catastrophic forgetting. Extensive
experiments demonstrate that Birdie outperforms state-of-the-art dense methods
by 16.8% in accuracy, and reduces forgetting by over 90% compared to other
continual learning approaches.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2206.02743)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2202.06991)\]\[[7](http://arxiv.org/abs/2305.15115)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Continual learning and catastrophic forgetting are critical challenges in differentiable search indices (DSIs), where models must adapt to incremental updates in the corpus without losing previously learned information \[[5](http://arxiv.org/abs/2212.09744)\]. DSIs encode documents directly into model parameters, allowing direct query answering, but retraining is required when the corpus evolves, leading to high computational costs \[[5](http://arxiv.org/abs/2212.09744)\]. This issue is exacerbated by the phenomenon of forgetting, where continual indexing of new documents causes degradation in performance on previously indexed data \[[5](http://arxiv.org/abs/2212.09744)\]. The problem is further compounded by unstable learning dynamics, as models may experience forgetting events during training, leading to inconsistent memorization \[[5](http://arxiv.org/abs/2212.09744)\]. To address these challenges, researchers have explored strategies such as optimizing for flatter loss basins to stabilize learning and reduce forgetting \[[5](http://arxiv.org/abs/2212.09744)\]. Additionally, generative memory techniques have been proposed to mitigate forgetting by supplementing training with pseudo-queries, enhancing retrieval performance \[[5](http://arxiv.org/abs/2212.09744)\]. These approaches highlight the need for continual learning mechanisms that balance model updates with retention of prior knowledge, ensuring robustness in dynamic indexing scenarios.
|    | reference                                                                                | date     | key idea/summary                                                                                                                                                                                                                                                                           |
|----|------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [DSI++: Updating Transformer Memory with New Documents](http://arxiv.org/abs/2212.09744) | 12/19/22 | DSI++ addresses the issue of forgetting in continual learning for differentiable search indices by introducing methods to optimize for flatter minima and using a generative memory to prevent forgetting, significantly improving retrieval performance and reducing computational costs. |
### <a id='category-efficient-data-structures-for-retrieval'></a>Efficient Data Structures for Retrieval: 1 papers found.
Context: 
	Document 1: \[[6](http://arxiv.org/abs/2004.12832)\] «Recent progress in Natural Language Understanding (NLU) is driving fast-paced advances in Information Retrieval (IR), largely owed to fine-tuning deep language models (LMs) for document ranking. While remarkably effective, the ranking models based on these LMs increase computational cost by orders of magnitude over prior approaches, particularly as they must feed each query-document pair through a massive neural network to compute a single relevance score. To tackle this, we present ColBERT, a novel ranking model that adapts deep LMs (in particular, BERT) for efficient retrieval. ColBERT introduces a late interaction architecture that independently encodes the query and the document using BERT and then employs a cheap yet powerful interaction step that models their fine-grained similarity. By delaying and yet retaining this fine-granular interaction, ColBERT can leverage the expressiveness of deep LMs while simultaneously gaining the ability to pre-compute document representations offline, considerably speeding up query processing. Crucially, ColBERT's pruning-friendly interaction mechanism enables leveraging vector-similarity indexes for end-to-end retrieval directly from millions of documents. We extensively evaluate ColBERT using two recent passage search datasets. Results show that ColBERT's effectiveness is competitive with existing BERT-based models (and outperforms every non-BERT baseline), while executing two orders-of-magnitude faster and requiring up to four orders-of-magnitude fewer FLOPs per query.»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2206.02743)\]. Further details \[[6](http://arxiv.org/abs/2004.12832)\]\[[7](http://arxiv.org/abs/2305.15115)\]\[[8](https://www.semanticscholar.org/paper/d69c0ed04ecc852e8c921900d3e7967f74f81263)\]\[[9](http://arxiv.org/abs/2004.04906)\]\[[10](http://arxiv.org/abs/1802.06159)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from
large table repositories based on NL queries. While current deep-learning-based
methods using the traditional dense vector search pipeline, i.e.,
representation-index-search, achieve remarkable accuracy, they face several
limitations that impede further performance improvements: (i) the errors
accumulated during the table representation and indexing phases affect the
subsequent search accuracy; and (ii) insufficient query-table interaction
hinders effective semantic alignment, impeding accuracy improvements. In this
paper, we propose a novel framework Birdie, using a differentiable search
index. It unifies the indexing and search into a single encoder-decoder
language model, thus getting rid of error accumulations. Birdie first assigns
each table a prefix-aware identifier and leverages a large language model-based
query generator to create synthetic queries for each table. It then encodes the
mapping between synthetic queries/tables and their corresponding table
identifiers into the parameters of an encoder-decoder language model, enabling
deep query-table interactions. During search, the trained model directly
generates table identifiers for a given query. To accommodate the continual
indexing of dynamic tables, we introduce an index update strategy via parameter
isolation, which mitigates the issue of catastrophic forgetting. Extensive
experiments demonstrate that Birdie outperforms state-of-the-art dense methods
by 16.8% in accuracy, and reduces forgetting by over 90% compared to other
continual learning approaches.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2206.02743)\]. Further details \[[6](http://arxiv.org/abs/2004.12832)\]\[[7](http://arxiv.org/abs/2305.15115)\]\[[8](https://www.semanticscholar.org/paper/d69c0ed04ecc852e8c921900d3e7967f74f81263)\]\[[9](http://arxiv.org/abs/2004.04906)\]\[[10](http://arxiv.org/abs/1802.06159)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Efforts to improve the efficiency of information retrieval systems have led to the development of novel architectures that reduce computational overhead while maintaining high performance. One such approach is ColBERT, which introduces a late interaction mechanism that independently encodes queries and documents using deep language models like BERT, followed by a cost-effective interaction step that captures fine-grained similarity \[[6](http://arxiv.org/abs/2004.12832)\]. This design allows for pre-computation of document representations, significantly speeding up query processing. Additionally, the pruning-friendly interaction mechanism enables the use of vector-similarity indexes for efficient retrieval from large document collections. These innovations address the limitations of traditional dense vector search pipelines, which often suffer from error accumulation during representation and indexing, as well as insufficient query-document interaction that hinders semantic alignment \[[6](http://arxiv.org/abs/2004.12832)\].
|    | reference                                                                                                                        | date     | key idea/summary                                                                                                                                                                                                     |
|----|----------------------------------------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](http://arxiv.org/abs/2004.12832) | 04/27/20 | ColBERT is an efficient ranking model that leverages deep language models like BERT for information retrieval by using a late interaction architecture to reduce computational cost while maintaining effectiveness. |
### <a id='category-evaluation-benchmarks-and-performance-metrics'></a>Evaluation Benchmarks and Performance Metrics: 1 papers found.
Context: 
	Document 1: \[[8](https://www.semanticscholar.org/paper/d69c0ed04ecc852e8c921900d3e7967f74f81263)\] «Pyserini is a Python toolkit for reproducible information retrieval research with sparse and dense representations. It aims to provide effective, reproducible, and easy-to-use first-stage retrieval in a multi-stage ranking architecture. Our toolkit is self-contained as a standard Python package and comes with queries, relevance judgments, pre-built indexes, and evaluation scripts for many commonly used IR test collections. We aim to support, out of the box, the entire research lifecycle of efforts aimed at improving ranking with modern neural approaches. In particular, Pyserini supports sparse retrieval (e.g., BM25 scoring using bag-of-words representations), dense retrieval (e.g., nearest-neighbor search on transformer-encoded representations), as well as hybrid retrieval that integrates both approaches. This paper provides an overview of toolkit features and presents empirical results that illustrate its effectiveness on two popular ranking tasks. Around this toolkit, our group has built a culture of reproducibility through shared norms and tools that enable rigorous automated testing.»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2206.02743)\]. Further details \[[6](http://arxiv.org/abs/2004.12832)\]\[[7](http://arxiv.org/abs/2305.15115)\]\[[8](https://www.semanticscholar.org/paper/d69c0ed04ecc852e8c921900d3e7967f74f81263)\]\[[9](http://arxiv.org/abs/2004.04906)\]\[[10](http://arxiv.org/abs/1802.06159)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from
large table repositories based on NL queries. While current deep-learning-based
methods using the traditional dense vector search pipeline, i.e.,
representation-index-search, achieve remarkable accuracy, they face several
limitations that impede further performance improvements: (i) the errors
accumulated during the table representation and indexing phases affect the
subsequent search accuracy; and (ii) insufficient query-table interaction
hinders effective semantic alignment, impeding accuracy improvements. In this
paper, we propose a novel framework Birdie, using a differentiable search
index. It unifies the indexing and search into a single encoder-decoder
language model, thus getting rid of error accumulations. Birdie first assigns
each table a prefix-aware identifier and leverages a large language model-based
query generator to create synthetic queries for each table. It then encodes the
mapping between synthetic queries/tables and their corresponding table
identifiers into the parameters of an encoder-decoder language model, enabling
deep query-table interactions. During search, the trained model directly
generates table identifiers for a given query. To accommodate the continual
indexing of dynamic tables, we introduce an index update strategy via parameter
isolation, which mitigates the issue of catastrophic forgetting. Extensive
experiments demonstrate that Birdie outperforms state-of-the-art dense methods
by 16.8% in accuracy, and reduces forgetting by over 90% compared to other
continual learning approaches.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2206.02743)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2202.06991)\]\[[7](http://arxiv.org/abs/2305.15115)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer:
The Pyserini toolkit \[[8](https://www.semanticscholar.org/paper/d69c0ed04ecc852e8c921900d3e7967f74f81263)\] is designed to support reproducible information retrieval research by integrating both sparse and dense retrieval methods within a unified framework. It provides researchers with a comprehensive environment for conducting experiments, including pre-built indexes, evaluation scripts, and relevance judgments for widely used IR test collections. This toolkit emphasizes the importance of reproducibility and ease of use, enabling researchers to focus on advancing ranking techniques with modern neural approaches. By supporting both sparse retrieval (e.g., BM25) and dense retrieval (e.g., transformer-encoded nearest-neighbor search), Pyserini addresses the need for flexible and robust retrieval strategies. The toolkit also facilitates hybrid retrieval, which combines the strengths of both approaches, thereby enhancing the effectiveness of multi-stage ranking architectures. The emphasis on reproducibility through shared norms and automated testing tools further strengthens the toolkit’s utility in academic and industrial research settings.
|    | reference                                                                                                                                                                                          | date     | key idea/summary                                                                                                                                                                                                                               |
|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Pyserini: A Python Toolkit for Reproducible Information Retrieval Research with Sparse and Dense Representations](https://www.semanticscholar.org/paper/d69c0ed04ecc852e8c921900d3e7967f74f81263) | 07/11/21 | Pyserini is a Python toolkit designed for reproducible information retrieval research, supporting both sparse and dense retrieval methods, hybrid approaches, and the entire research lifecycle with pre-built resources and evaluation tools. |
### <a id='category-traditional-retrieval-pipelines-and-their-limitations'></a>Traditional Retrieval Pipelines and Their Limitations: 1 papers found.
Context: 
	Document 1: [_citation_number]: «9»
[Snippet]: «Open-domain question answering relies on efficient passage retrieval to select candidate contexts, where traditional sparse vector space models, such as TF-IDF or BM25, are the de facto method. In this work, we show that retrieval can be practically implemented using dense representations alone, where embeddings are learned from a small number of questions and passages by a simple dual-encoder framework. When evaluated on a wide range of open-domain QA datasets, our dense retriever outperforms a strong Lucene-BM25 system largely by 9%-19% absolute in terms of top-20 passage retrieval accuracy, and helps our end-to-end QA system establish new state-of-the-art on multiple open-domain QA benchmarks.»
[Category]: «Traditional Retrieval Pipelines and Their Limitations»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2206.02743)\]. Further details \[[6](http://arxiv.org/abs/2004.12832)\]\[[7](http://arxiv.org/abs/2305.15115)\]\[[8](https://www.semanticscholar.org/paper/d69c0ed04ecc852e8c921900d3e7967f74f81263)\]\[[9](http://arxiv.org/abs/2004.04906)\]\[[10](http://arxiv.org/abs/1802.06159)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from
large table repositories based on NL queries. While current deep-learning-based
methods using the traditional dense vector search pipeline, i.e.,
representation-index-search, achieve remarkable accuracy, they face several
limitations that impede further performance improvements: (i) the errors
accumulated during the table representation and indexing phases affect the
subsequent search accuracy; and (ii) insufficient query-table interaction
hinders effective semantic alignment, impeding accuracy improvements. In this
paper, we propose a novel framework Birdie, using a differentiable search
index. It unifies the indexing and search into a single encoder-decoder
language model, thus getting rid of error accumulations. Birdie first assigns
each table a prefix-aware identifier and leverages a large language model-based
query generator to create synthetic queries for each table. It then encodes the
mapping between synthetic queries/tables and their corresponding table
identifiers into the parameters of an encoder-decoder language model, enabling
deep query-table interactions. During search, the trained model directly
generates table identifiers for a given query. To accommodate the continual
indexing of dynamic tables, we introduce an index update strategy via parameter
isolation, which mitigates the issue of catastrophic forgetting. Extensive
experiments demonstrate that Birdie outperforms state-of-the-art dense methods
by 16.8% in accuracy, and reduces forgetting by over 90% compared to other
continual learning approaches.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2206.02743)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2202.06991)\]\[[7](http://arxiv.org/abs/2305.15115)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Traditional retrieval pipelines, such as those based on sparse vector space models like TF-IDF or BM25, have long been the de facto standard for passage retrieval in open-domain question answering \[[9](http://arxiv.org/abs/2004.04906)\]. These methods rely on precomputed indices and typically involve separate stages for representation, indexing, and search, which can introduce error accumulation and limit semantic alignment between queries and documents \[[9](http://arxiv.org/abs/2004.04906)\]. Recent work has shown that dense representations, learned through dual-encoder frameworks, can achieve competitive performance and even outperform traditional systems by a significant margin \[[9](http://arxiv.org/abs/2004.04906)\]. This shift toward dense retrieval highlights the limitations of sparse methods, particularly in terms of their inability to capture complex semantic relationships effectively. The transition to dense representations also enables more flexible and accurate matching between queries and candidate passages, as demonstrated by improved top-20 passage retrieval accuracy \[[9](http://arxiv.org/abs/2004.04906)\]. However, the reliance on precomputed indices and the separation of indexing from search continue to pose challenges for further performance improvements.
|    | reference                                                                                     | date     | key idea/summary                                                                                                                                                                                                               |
|----|-----------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Dense Passage Retrieval for Open-Domain Question Answering](http://arxiv.org/abs/2004.04906) | 04/10/20 | This work demonstrates that dense representations can effectively replace traditional sparse methods like TF-IDF or BM25 for open-domain question answering, achieving significant improvements in passage retrieval accuracy. |
### <a id='category-semantic-similarity-in-table-retrieval'></a>Semantic Similarity in Table Retrieval: 3 papers found.
Context: 
	Document 1: [_citation_number]: «10»
[Snippet]: «We introduce and address the problem of ad hoc table retrieval: answering a keyword query with a ranked list of tables. This task is not only interesting on its own account, but is also being used as a core component in many other table-based information access scenarios, such as table completion or table mining. The main novel contribution of this work is a method for performing semantic matching between queries and tables. Specifically, we (i) represent queries and tables in multiple semantic spaces (both discrete sparse and continuous dense vector representations) and (ii) introduce various similarity measures for matching those semantic representations. We consider all possible combinations of semantic representations and similarity measures and use these as features in a supervised learning model. Using a purpose-built test collection based on Wikipedia tables, we demonstrate significant and substantial improvements over a state-of-the-art baseline.»
[Category]: «Semantic Similarity in Table Retrieval»

	Document 2: [_citation_number]: «13»
[Snippet]: «We present the design of a structured search engine which returns a multi-column table in response to a query consisting of keywords describing each of its columns. We answer such queries by exploiting the millions of tables on the Web because these are much richer sources of structured knowledge than free-format text. However, a corpus of tables harvested from arbitrary HTML web pages presents huge challenges of diversity and redundancy not seen in centrally edited knowledge bases. We concentrate on one concrete task in this paper. Given a set of Web tables T1,..., Tn, and a query Q with q sets of keywords Q1,..., Qq, decide for each Ti if it is relevant to Q and if so, identify the mapping between the columns of Ti and query columns. We represent this task as a graphical model that jointly maps all tables by incorporating diverse sources of clues spanning matches in different parts of the table, corpus-wide co-occurrence statistics, and content overlap across table columns. We define a novel query segmentation model for matching keywords to table columns, and a robust mechanism of exploiting content overlap across table columns. We design efficient inference algorithms based on bipartite matching and constrained graph cuts to solve the joint labeling task. Experiments on a workload of 59 queries over a 25 million web table corpus shows significant boost in accuracy over baseline IR methods.»
[Category]: «Semantic Similarity in Table Retrieval»

	Document 3: [_citation_number]: «15»
[Snippet]: «Tables contain valuable knowledge in a structured form. We employ neural language modeling approaches to embed tabular data into vector spaces. Specifically, we consider different table elements, such caption, column headings, and cells, for training word and entity embeddings. These embeddings are then utilized in three particular table-related tasks, row population, column population, and table retrieval, by incorporating them into existing retrieval models as additional semantic similarity signals. Evaluation results show that table embeddings can significantly improve upon the performance of state-of-the-art baselines.»
[Category]: «Semantic Similarity in Table Retrieval»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2206.02743)\]. Further details \[[6](http://arxiv.org/abs/2004.12832)\]\[[7](http://arxiv.org/abs/2305.15115)\]\[[8](https://www.semanticscholar.org/paper/d69c0ed04ecc852e8c921900d3e7967f74f81263)\]\[[9](http://arxiv.org/abs/2004.04906)\]\[[10](http://arxiv.org/abs/1802.06159)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from
large table repositories based on NL queries. While current deep-learning-based
methods using the traditional dense vector search pipeline, i.e.,
representation-index-search, achieve remarkable accuracy, they face several
limitations that impede further performance improvements: (i) the errors
accumulated during the table representation and indexing phases affect the
subsequent search accuracy; and (ii) insufficient query-table interaction
hinders effective semantic alignment, impeding accuracy improvements. In this
paper, we propose a novel framework Birdie, using a differentiable search
index. It unifies the indexing and search into a single encoder-decoder
language model, thus getting rid of error accumulations. Birdie first assigns
each table a prefix-aware identifier and leverages a large language model-based
query generator to create synthetic queries for each table. It then encodes the
mapping between synthetic queries/tables and their corresponding table
identifiers into the parameters of an encoder-decoder language model, enabling
deep query-table interactions. During search, the trained model directly
generates table identifiers for a given query. To accommodate the continual
indexing of dynamic tables, we introduce an index update strategy via parameter
isolation, which mitigates the issue of catastrophic forgetting. Extensive
experiments demonstrate that Birdie outperforms state-of-the-art dense methods
by 16.8% in accuracy, and reduces forgetting by over 90% compared to other
continual learning approaches.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2206.02743)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2202.06991)\]\[[7](http://arxiv.org/abs/2305.15115)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
The semantic similarity in table retrieval has been a focal point in recent research, with multiple approaches aiming to enhance the accuracy of matching queries to relevant tables. Existing methods often rely on semantic representations, such as discrete sparse and continuous dense vector embeddings, to capture the meaning of both queries and tables \[[10](http://arxiv.org/abs/1802.06159)\]. These representations are combined with various similarity measures to improve retrieval performance, as demonstrated in experiments using a purpose-built test collection \[[10](http://arxiv.org/abs/1802.06159)\]. Additionally, structured search engines have been developed to handle multi-column tables by leveraging graphical models that incorporate diverse clues, including matches in different parts of the table, corpus-wide co-occurrence statistics, and content overlap across columns \[[13](http://arxiv.org/abs/1207.0132)\]. These models enable efficient inference through bipartite matching and constrained graph cuts, leading to significant improvements over traditional IR methods \[[13](http://arxiv.org/abs/1207.0132)\]. Furthermore, neural language modeling approaches have been applied to embed tabular data into vector spaces, allowing for the use of word and entity embeddings in tasks like row population, column population, and table retrieval \[[15](http://arxiv.org/abs/1906.00041)\]. These embeddings serve as additional semantic similarity signals, enhancing the performance of existing retrieval models \[[15](http://arxiv.org/abs/1906.00041)\]. Overall, these studies highlight the importance of semantic alignment and the integration of diverse sources of information to improve table retrieval accuracy.
|    | reference                                                                                                          | date     | key idea/summary                                                                                                                                                                                          |
|----|--------------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Ad Hoc Table Retrieval using Semantic Similarity](http://arxiv.org/abs/1802.06159)                                | 02/16/18 | The paper introduces a method for semantic matching between keyword queries and tables, using multiple semantic representations and similarity measures to improve table retrieval performance.           |
|  1 | [Answering Table Queries on the Web using Column Keywords](http://arxiv.org/abs/1207.0132)                         | 06/01/12 | The paper introduces a structured search engine that returns multi-column tables in response to keyword-based queries by leveraging Web tables and advanced graphical models for accurate column mapping. |
|  2 | [Table2Vec: Neural Word and Entity Embeddings for Table Population and Retrieval](http://arxiv.org/abs/1906.00041) | 05/31/19 | The paper proposes using neural language modeling to embed tabular data into vector spaces, improving performance in table-related tasks through semantic similarity signals.                             |
### <a id='category-pre-training-and-fine-tuning-strategies'></a>Pre-training and Fine-tuning Strategies: 3 papers found.
Context: 
	Document 1: [_citation_number]: «11»
[Snippet]: «The advent of deep neural networks pre-trained via language modeling tasks has spurred a number of successful applications in natural language processing. This work explores one such popular model, BERT, in the context of document ranking. We propose two variants, called monoBERT and duoBERT, that formulate the ranking problem as pointwise and pairwise classification, respectively. These two models are arranged in a multi-stage ranking architecture to form an end-to-end search system. One major advantage of this design is the ability to trade off quality against latency by controlling the admission of candidates into each pipeline stage, and by doing so, we are able to find operating points that offer a good balance between these two competing metrics. On two large-scale datasets, MS MARCO and TREC CAR, experiments show that our model produces results that are either at or comparable to the state of the art. Ablation studies show the contributions of each component and characterize the latency/quality tradeoff space.»
[Category]: «Pre-training and Fine-tuning Strategies»

	Document 2: [_citation_number]: «12»
[Snippet]: «Knowledge-intensive language tasks (KILT) usually require a large body of information to provide correct answers. A popular paradigm to solve this problem is to combine a search system with a machine reader, where the former retrieves supporting evidences and the latter examines them to produce answers. Recently, the reader component has witnessed significant advances with the help of large-scale pre-trained generative models. Meanwhile most existing solutions in the search component rely on the traditional "index-retrieve-then-rank'' pipeline, which suffers from large memory footprint and difficulty in end-to-end optimization. Inspired by recent efforts in constructing model-based IR models, we propose to replace the traditional multi-step search pipeline with a novel single-step generative model, which can dramatically simplify the search process and be optimized in an end-to-end manner. We show that a strong generative retrieval model can be learned with a set of adequately designed pre-training tasks, and be adopted to improve a variety of downstream KILT tasks with further fine-tuning. We name the pre-trained generative retrieval model as CorpusBrain as all information about the corpus is encoded in its parameters without the need of constructing additional index. Empirical results show that CorpusBrain can significantly outperform strong baselines for the retrieval task on the KILT benchmark and establish new state-of-the-art downstream performances. We also show that CorpusBrain works well under zero- and low-resource settings.»
[Category]: «Pre-training and Fine-tuning Strategies»

	Document 3: [_citation_number]: «14»
[Snippet]: «Pretrained contextualized language models such as BERT have achieved impressive results on various natural language processing benchmarks. Benefiting from multiple pretraining tasks and large scale training corpora, pretrained models can capture complex syntactic word relations. In this paper, we use the deep contextualized language model BERT for the task of ad hoc table retrieval. We investigate how to encode table content considering the table structure and input length limit of BERT. We also propose an approach that incorporates features from prior literature on table retrieval and jointly trains them with BERT. In experiments on public datasets, we show that our best approach can outperform the previous state-of-the-art method and BERT baselines with a large margin under different evaluation metrics.»
[Category]: «Pre-training and Fine-tuning Strategies»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2206.02743)\]. Further details \[[6](http://arxiv.org/abs/2004.12832)\]\[[7](http://arxiv.org/abs/2305.15115)\]\[[8](https://www.semanticscholar.org/paper/d69c0ed04ecc852e8c921900d3e7967f74f81263)\]\[[9](http://arxiv.org/abs/2004.04906)\]\[[10](http://arxiv.org/abs/1802.06159)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from
large table repositories based on NL queries. While current deep-learning-based
methods using the traditional dense vector search pipeline, i.e.,
representation-index-search, achieve remarkable accuracy, they face several
limitations that impede further performance improvements: (i) the errors
accumulated during the table representation and indexing phases affect the
subsequent search accuracy; and (ii) insufficient query-table interaction
hinders effective semantic alignment, impeding accuracy improvements. In this
paper, we propose a novel framework Birdie, using a differentiable search
index. It unifies the indexing and search into a single encoder-decoder
language model, thus getting rid of error accumulations. Birdie first assigns
each table a prefix-aware identifier and leverages a large language model-based
query generator to create synthetic queries for each table. It then encodes the
mapping between synthetic queries/tables and their corresponding table
identifiers into the parameters of an encoder-decoder language model, enabling
deep query-table interactions. During search, the trained model directly
generates table identifiers for a given query. To accommodate the continual
indexing of dynamic tables, we introduce an index update strategy via parameter
isolation, which mitigates the issue of catastrophic forgetting. Extensive
experiments demonstrate that Birdie outperforms state-of-the-art dense methods
by 16.8% in accuracy, and reduces forgetting by over 90% compared to other
continual learning approaches.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2206.02743)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2202.06991)\]\[[7](http://arxiv.org/abs/2305.15115)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer:  
Recent advances in pre-training and fine-tuning strategies have significantly enhanced the performance of language models in various NLP tasks \[[11](http://arxiv.org/abs/1910.14424)\]. Pretrained contextualized models like BERT have demonstrated impressive results by capturing complex syntactic and semantic relationships through extensive pretraining on large corpora \[[14](http://arxiv.org/abs/2005.09207)\]. These models are often fine-tuned for specific tasks, such as document ranking, where they are adapted to handle pointwise and pairwise classification \[[11](http://arxiv.org/abs/1910.14424)\]. Additionally, efforts have been made to integrate search systems with machine readers, leveraging large-scale pre-trained generative models to improve knowledge-intensive tasks \[[12](http://arxiv.org/abs/2208.07652)\]. The traditional "index-retrieve-then-rank" pipeline, however, suffers from limitations such as high memory usage and difficulty in end-to-end optimization, prompting the development of novel generative retrieval models that simplify the search process \[[12](http://arxiv.org/abs/2208.07652)\]. These strategies highlight the importance of pre-training and fine-tuning in achieving state-of-the-art results while addressing challenges like error accumulation and semantic alignment \[[11](http://arxiv.org/abs/1910.14424)\]\[[12](http://arxiv.org/abs/2208.07652)\]\[[14](http://arxiv.org/abs/2005.09207)\].
|    | reference                                                                                                                     | date     | key idea/summary                                                                                                                                                                                                                     |
|----|-------------------------------------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Multi-Stage Document Ranking with BERT](http://arxiv.org/abs/1910.14424)                                                     | 10/31/19 | This work introduces monoBERT and duoBERT variants of BERT for document ranking, achieving state-of-the-art results on large-scale datasets while enabling a balance between quality and latency through a multi-stage architecture. |
|  1 | [CorpusBrain: Pre-train a Generative Retrieval Model for Knowledge-Intensive Language Tasks](http://arxiv.org/abs/2208.07652) | 08/16/22 | CorpusBrain is a pre-trained generative retrieval model that replaces traditional search pipelines, enabling end-to-end optimization and significant performance improvements on knowledge-intensive language tasks.                 |
|  2 | [Table Search Using a Deep Contextualized Language Model](http://arxiv.org/abs/2005.09207)                                    | 05/19/20 | The paper proposes an approach that enhances ad hoc table retrieval using BERT by incorporating structural features and joint training, achieving better performance than previous methods.                                          |
