## Related Works

Natural language-driven table discovery has emerged as a critical task in modern data lake management, enabling users to identify relevant tables based on semantic queries \[[2](http://arxiv.org/abs/2212.07588)\]. Traditional approaches rely on a dense vector search pipeline, which involves representation, indexing, and search stages \[[9](http://arxiv.org/abs/2005.09207)\]. However, these methods face limitations such as error accumulation during representation and indexing, and insufficient query-table interaction that hinders semantic alignment \[[1](http://arxiv.org/abs/2106.09592)\]. 

Several studies have explored alternative methods to improve the accuracy and efficiency of table discovery. For instance, DeepJoin leverages pre-trained language models (PLMs) to enable accurate and efficient joinable table discovery by embedding columns into vectors and using approximate nearest neighbor search algorithms \[[2](http://arxiv.org/abs/2212.07588)\]. This approach supports both equi-joins and semantic joins, demonstrating high precision and performance \[[2](http://arxiv.org/abs/2212.07588)\]. Similarly, Starmie introduces a contrastive learning method to train column encoders from pre-trained language models, capturing rich contextual semantic information and improving table union search effectiveness \[[3](http://arxiv.org/abs/2210.01922)\]. It also employs the HNSW index to accelerate query processing, achieving significant performance gains \[[3](http://arxiv.org/abs/2210.01922)\].

Other works focus on natural language table retrieval (NLTR), where the goal is to retrieve semantically relevant tables based on natural language queries. Ad hoc table retrieval using semantic similarity has been explored, where queries and tables are represented in multiple semantic spaces and compared using various similarity measures \[[8](http://arxiv.org/abs/1802.06159)\]. This approach has shown substantial improvements over state-of-the-art baselines \[[8](http://arxiv.org/abs/1802.06159)\]. Similarly, the use of BERT for ad hoc table retrieval has been investigated, with methods that encode table content while considering the table structure and input length constraints \[[9](http://arxiv.org/abs/2005.09207)\]. These approaches have demonstrated strong performance, often outperforming previous methods \[[9](http://arxiv.org/abs/2005.09207)\].

Recent advancements in differentiable search indexes have also contributed to this field. The Differentiable Search Index (DSI) paradigm allows a single Transformer model to perform both indexing and retrieval, simplifying the retrieval process \[[10](http://arxiv.org/abs/2202.06991)\]. However, DSI models face challenges related to data distribution mismatches between indexing and retrieval phases, particularly in cross-lingual settings \[[12](http://arxiv.org/abs/2206.10128)\]. To address this, DSI-QG introduces an indexing framework that generates relevant queries during indexing, improving the alignment between indexed documents and retrieval queries \[[12](http://arxiv.org/abs/2206.10128)\].

In addition, generative retrieval (GR) has been proposed as a method for directly predicting document identifiers based on a parametric model, offering superior performance in retrieval tasks \[[13](http://arxiv.org/abs/2402.01176)\]. However, GR models often struggle with dynamic corpora, where new documents are continuously added \[[14](http://arxiv.org/abs/2308.14968)\]. To address this, CLE
## Research papers
### Outline
- [Performance Evaluation Metrics [1 papers]](#category-performance-evaluation-metrics)
- [Pre-trained Language Models in Table Retrieval [5 papers]](#category-pre-trained-language-models-in-table-retrieval)
- [Contrastive Learning for Table Encoding [1 papers]](#category-contrastive-learning-for-table-encoding)
- [Query-Table Interaction [1 papers]](#category-query-table-interaction)
- [Table Discovery Methods [1 papers]](#category-table-discovery-methods)
- [Differentiable Search Index Frameworks [5 papers]](#category-differentiable-search-index-frameworks)
- [Continual Learning in Dynamic Environments [1 papers]](#category-continual-learning-in-dynamic-environments)
- [Approximate Nearest Neighbor Search [1 papers]](#category-approximate-nearest-neighbor-search)

### <a id='category-performance-evaluation-metrics'></a>Performance Evaluation Metrics: 1 papers found.
Context: 
	Document 1: [Category]: «Performance Evaluation Metrics»
[Snippet]: «Data lakes are becoming increasingly prevalent for big data management and
data analytics. In contrast to traditional 'schema-on-write' approaches such as
data warehouses, data lakes are repositories storing raw data in its original
formats and providing a common access interface. Despite the strong interest
raised from both academia and industry, there is a large body of ambiguity
regarding the definition, functions and available technologies for data lakes.
A complete, coherent picture of data lake challenges and solutions is still
missing. This survey reviews the development, architectures, and systems of
data lakes. We provide a comprehensive overview of research questions for
designing and building data lakes. We classify the existing approaches and
systems based on their provided functions for data lakes, which makes this
survey a useful technical reference for designing, implementing and deploying
data lakes. We hope that the thorough comparison of existing solutions and the
discussion of open research challenges in this survey will motivate the future
development of data lake research and practice.»
[_citation_number]: «1»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2210.01922)\]. Further details \[[6](http://arxiv.org/abs/2004.02349)\]\[[7](http://arxiv.org/abs/2105.01736)\]\[[8](http://arxiv.org/abs/1802.06159)\]\[[9](http://arxiv.org/abs/2005.09207)\]\[[10](http://arxiv.org/abs/2202.06991)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from
large table repositories based on NL queries. While current deep-learning-based
methods using the traditional dense vector search pipeline, i.e.,
representation-index-search, achieve remarkable accuracy, they face several
limitations that impede further performance improvements: (i) the errors
accumulated during the table representation and indexing phases affect the
subsequent search accuracy; and (ii) insufficient query-table interaction

|    | reference                                                                        |   date | key idea/summary                                                                                                                                                                               |
|----|----------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Data Lakes: A Survey of Functions and Systems](http://arxiv.org/abs/2106.09592) |    nan | This survey provides a comprehensive overview of data lakes, their architectures, systems, and challenges, aiming to serve as a technical reference for designing and implementing data lakes. |
### <a id='category-pre-trained-language-models-in-table-retrieval'></a>Pre-trained Language Models in Table Retrieval: 5 papers found.
Context: 
	Document 1: [Category]: «Pre-trained Language Models in Table Retrieval»
[Snippet]: «Due to the usefulness in data enrichment for data analysis tasks, joinable
table discovery has become an important operation in data lake management.
Existing approaches target equi-joins, the most common way of combining tables
for creating a unified view, or semantic joins, which tolerate misspellings and
different formats to deliver more join results. They are either exact solutions
whose running time is linear in the sizes of query column and target table
repository or approximate solutions lacking precision. In this paper, we
propose Deepjoin, a deep learning model for accurate and efficient joinable
table discovery. Our solution is an embedding-based retrieval, which employs a
pre-trained language model (PLM) and is designed as one framework serving both
equi- and semantic joins. We propose a set of contextualization options to
transform column contents to a text sequence. The PLM reads the sequence and is
fine-tuned to embed columns to vectors such that columns are expected to be
joinable if they are close to each other in the vector space. Since the output
of the PLM is fixed in length, the subsequent search procedure becomes
independent of the column size. With a state-of-the-art approximate nearest
neighbor search algorithm, the search time is logarithmic in the repository
size. To train the model, we devise the techniques for preparing training data
as well as data augmentation. The experiments on real datasets demonstrate that
by training on a small subset of a corpus, Deepjoin generalizes to large
datasets and its precision consistently outperforms other approximate
solutions'. Deepjoin is even more accurate than an exact solution to semantic
joins when evaluated with labels from experts. Moreover, when equipped with a
GPU, Deepjoin is up to two orders of magnitude faster than existing solutions.»
[_citation_number]: «2»

	Document 2: [Category]: «Pre-trained Language Models in Table Retrieval»
[Snippet]: «Recent advances in open-domain QA have led to strong models based on dense
retrieval, but only focused on retrieving textual passages. In this work, we
tackle open-domain QA over tables for the first time, and show that retrieval
can be improved by a retriever designed to handle tabular context. We present
an effective pre-training procedure for our retriever and improve retrieval
quality with mined hard negatives.
|    | reference                                                                                                        |   date | key idea/summary                                                                                                                                                                                                                                                                           |
|----|------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [DeepJoin: Joinable Table Discovery with Pre-trained Language Models](http://arxiv.org/abs/2212.07588)           |    nan | Deepjoin is a deep learning model that enables accurate and efficient joinable table discovery in data lakes by using pre-trained language models and contextualization techniques to handle both equi- and semantic joins.                                                                |
|  1 | [Open Domain Question Answering over Tables via Dense Retrieval](http://arxiv.org/abs/2103.12011)                |    nan | This work introduces a retriever specifically designed for open-domain QA over tables, improving retrieval and end-to-end QA results compared to a BERT-based retriever.                                                                                                                   |
|  2 | [TAPAS: Weakly Supervised Table Parsing via Pre-training](http://arxiv.org/abs/2004.02349)                       |    nan | TAPAS is a novel approach for answering natural language questions over tables that avoids generating logical forms, instead directly predicting denotations by selecting table cells and applying aggregation operators, achieving state-of-the-art results on semantic parsing datasets. |
|  3 | [Retrieving Complex Tables with Multi-Granular Graph Representation
  Learning](http://arxiv.org/abs/2105.01736) |    nan | The paper introduces Graph-based Table Retrieval (GTR), a novel framework for natural language table retrieval that uses multi-granular graph representation and a Graph Transformer model to effectively handle complex table layouts and diverse query intents.                          |
|  4 | [Table Search Using a Deep Contextualized Language Model](http://arxiv.org/abs/2005.09207)                       |    nan | The paper proposes an approach that integrates features from prior literature with BERT for ad hoc table retrieval, achieving significant improvements over previous methods and BERT baselines.                                                                                           |
### <a id='category-contrastive-learning-for-table-encoding'></a>Contrastive Learning for Table Encoding: 1 papers found.
Context: 
	Document 1: [Category]: «Contrastive Learning for Table Encoding»
[Snippet]: «Dataset discovery from data lakes is essential in many real application
scenarios. In this paper, we propose Starmie, an end-to-end framework for
dataset discovery from data lakes (with table union search as the main use
case). Our proposed framework features a contrastive learning method to train
column encoders from pre-trained language models in a fully unsupervised
manner. The column encoder of Starmie captures the rich contextual semantic
information within tables by leveraging a contrastive multi-column pre-training
strategy. We utilize the cosine similarity between column embedding vectors as
the column unionability score and propose a filter-and-verification framework
that allows exploring a variety of design choices to compute the unionability
score between two tables accordingly. Empirical evaluation results on real
table benchmark datasets show that Starmie outperforms the best-known solutions
in the effectiveness of table union search by 6.8 in MAP and recall. Moreover,
Starmie is the first to employ the HNSW (Hierarchical Navigable Small World)
index for accelerate query processing of table union search which provides a
3,000X performance gain over the linear scan baseline and a 400X performance
gain over an LSH index (the state-of-the-art solution for data lake indexing).»
[_citation_number]: «3»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2210.01922)\]. Further details \[[6](http://arxiv.org/abs/2004.02349)\]\[[7](http://arxiv.org/abs/2105.01736)\]\[[8](http://arxiv.org/abs/1802.06159)\]\[[9](http://arxiv.org/abs/2005.09207)\]\[[10](http://arxiv.org/abs/2202.06991)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from
large table repositories based on NL
|    | reference                                                                                                                                       |   date | key idea/summary                                                                                                                                                                           |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Semantics-aware Dataset Discovery from Data Lakes with Contextualized
  Column-based Representation Learning](http://arxiv.org/abs/2210.01922) |    nan | Starmie is an end-to-end framework for dataset discovery from data lakes, using contrastive learning and HNSW indexing to improve the effectiveness and performance of table union search. |
### <a id='category-query-table-interaction'></a>Query-Table Interaction: 1 papers found.
Context: 
	Document 1: [Category]: «Query-Table Interaction»
[Snippet]: «Most deployed data discovery systems, such as Google Datasets, and open data
portals only support keyword search. Keyword search is geared towards general
audiences but limits the types of queries the systems can answer. We propose a
new system that lets users write natural language questions directly. A major
barrier to using this learned data discovery system is it needs
expensive-to-collect training data, thus limiting its utility. In this paper,
we introduce a self-supervised approach to assemble training datasets and train
learned discovery systems without human intervention. It requires addressing
several challenges, including the design of self-supervised strategies for data
discovery, table representation strategies to feed to the models, and relevance
models that work well with the synthetically generated questions. We combine
all the above contributions into a system, Solo, that solves the problem end to
end. The evaluation results demonstrate the new techniques outperform
state-of-the-art approaches on well-known benchmarks. All in all, the technique
is a stepping stone towards building learned discovery systems. The code is
open-sourced at https://github.com/TheDataStation/solo»
[_citation_number]: «4»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2210.01922)\]. Further details \[[6](http://arxiv.org/abs/2004.02349)\]\[[7](http://arxiv.org/abs/2105.01736)\]\[[8](http://arxiv.org/abs/1802.06159)\]\[[9](http://arxiv.org/abs/2005.09207)\]\[[10](http://arxiv.org/abs/2202.06991)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from
large table repositories based on NL queries. While current deep-learning-based
methods using the traditional dense vector search pipeline, i.e.,
representation-index-search, achieve remarkable accuracy, they face several
limitations that impede further
|    | reference                                                                                                                 |   date | key idea/summary                                                                                                                                                                                                           |
|----|---------------------------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Solo: Data Discovery Using Natural Language Questions Via A
  Self-Supervised Approach](http://arxiv.org/abs/2301.03560) |    nan | The paper introduces a self-supervised approach to train learned data discovery systems without human intervention, leading to the development of the Solo system that outperforms state-of-the-art methods on benchmarks. |
### <a id='category-table-discovery-methods'></a>Table Discovery Methods: 1 papers found.
Context: 
	Document 1: [Category]: «Table Discovery Methods»
[Snippet]: «We introduce and address the problem of ad hoc table retrieval: answering a keyword query with a ranked list of tables. This task is not only interesting on its own account, but is also being used as a core component in many other table-based information access scenarios, such as table completion or table mining. The main novel contribution of this work is a method for performing semantic matching between queries and tables. Specifically, we (i) represent queries and tables in multiple semantic spaces (both discrete sparse and continuous dense vector representations) and (ii) introduce various similarity measures for matching those semantic representations. We consider all possible combinations of semantic representations and similarity measures and use these as features in a supervised learning model. Using a purpose-built test collection based on Wikipedia tables, we demonstrate significant and substantial improvements over a state-of-the-art baseline.»
[_citation_number]: «8»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2210.01922)\]. Further details \[[6](http://arxiv.org/abs/2004.02349)\]\[[7](http://arxiv.org/abs/2105.01736)\]\[[8](http://arxiv.org/abs/1802.06159)\]\[[9](http://arxiv.org/abs/2005.09207)\]\[[10](http://arxiv.org/abs/2202.06991)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from large table repositories based on NL queries. While current deep-learning-based methods using the traditional dense vector search pipeline, i.e., representation-index-search, achieve remarkable accuracy, they face several limitations that impede further performance improvements: (i) the errors accumulated during the table representation and indexing phases affect the subsequent search accuracy; and (ii) insufficient query-table interaction hinders effective semantic alignment, impeding accuracy improvements. In this paper, we propose a novel framework Birdie, using a differentiable search index. It unifies the indexing and search into a single encoder-decoder language
|    | reference                                                                           |   date | key idea/summary                                                                                                                                                                       |
|----|-------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Ad Hoc Table Retrieval using Semantic Similarity](http://arxiv.org/abs/1802.06159) |    nan | The paper introduces a method for semantic matching between keyword queries and tables, using multiple semantic spaces and similarity measures to improve table retrieval performance. |
### <a id='category-differentiable-search-index-frameworks'></a>Differentiable Search Index Frameworks: 5 papers found.
Context: 
	Document 1: [Category]: «Differentiable Search Index Frameworks»
[Snippet]: «In this paper, we demonstrate that information retrieval can be accomplished
with a single Transformer, in which all information about the corpus is encoded
in the parameters of the model. To this end, we introduce the Differentiable
Search Index (DSI), a new paradigm that learns a text-to-text model that maps
string queries directly to relevant docids; in other words, a DSI model answers
queries directly using only its parameters, dramatically simplifying the whole
retrieval process. We study variations in how documents and their identifiers
are represented, variations in training procedures, and the interplay between
models and corpus sizes. Experiments demonstrate that given appropriate design
choices, DSI significantly outperforms strong baselines such as dual encoder
models. Moreover, DSI demonstrates strong generalization capabilities,
outperforming a BM25 baseline in a zero-shot setup.»
[_citation_number]: «10»

	Document 2: [Category]: «Differentiable Search Index Frameworks»
[Snippet]: «Current state-of-the-art document retrieval solutions mainly follow an
index-retrieve paradigm, where the index is hard to be directly optimized for
the final retrieval target. In this paper, we aim to show that an end-to-end
deep neural network unifying training and indexing stages can significantly
improve the recall performance of traditional methods. To this end, we propose
Neural Corpus Indexer (NCI), a sequence-to-sequence network that generates
relevant document identifiers directly for a designated query. To optimize the
recall performance of NCI, we invent a prefix-aware weight-adaptive decoder
architecture, and leverage tailored techniques including query generation,
semantic document identifiers, and consistency-based regularization. Empirical
studies demonstrated the superiority of NCI on two commonly used academic
benchmarks, achieving +21.4% and +16.8% relative enhancement for Recall@1 on
NQ320k dataset and R-Precision on TriviaQA dataset, respectively, compared to
the best baseline method.»
[_citation_number]: «11»

	Document 3: [Category]: «Differentiable Search Index Frameworks»
[Snippet]: «The Differentiable Search Index (DSI) is an emerging paradigm for information
retrieval. Unlike traditional retrieval architectures where index and retrieval
are two different and separate components, DSI uses a
|    | reference                                                                                                                                  |   date | key idea/summary                                                                                                                                                                                                                                                  |
|----|--------------------------------------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Transformer Memory as a Differentiable Search Index](http://arxiv.org/abs/2202.06991)                                                     |    nan | The paper introduces the Differentiable Search Index (DSI), a novel paradigm that uses a single Transformer model to directly answer queries by encoding all corpus information into its parameters, significantly simplifying the information retrieval process. |
|  1 | [A Neural Corpus Indexer for Document Retrieval](http://arxiv.org/abs/2206.02743)                                                          |    nan | The paper introduces Neural Corpus Indexer (NCI), an end-to-end deep neural network that improves recall performance in document retrieval by unifying training and indexing stages with a prefix-aware weight-adaptive decoder architecture.                     |
|  2 | [Bridging the Gap Between Indexing and Retrieval for Differentiable
  Search Index with Query Generation](http://arxiv.org/abs/2206.10128) |    nan | DSI-QG is an indexing framework for Differentiable Search Index (DSI) models that addresses data distribution mismatches by generating and using relevant queries during indexing to improve retrieval performance.                                               |
|  3 | [CorpusLM: Towards a Unified Language Model on Corpus for
  Knowledge-Intensive Tasks](http://arxiv.org/abs/2402.01176)                    |    nan | CorpusLM is a unified language model that improves knowledge-intensive tasks by integrating generative retrieval, closed-book generation, and RAG through a unified decoding process, achieving superior performance in both retrieval and downstream tasks.      |
|  4 | [(DSI++:) Updating Transformer Memory with New Documents]()                                                                                |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                         |
### <a id='category-continual-learning-in-dynamic-environments'></a>Continual Learning in Dynamic Environments: 1 papers found.
Context: 
	Document 1: [Category]: «Continual Learning in Dynamic Environments»
[Snippet]: «Generative retrieval (GR) directly predicts the identifiers of relevant documents (i.e., docids) based on a parametric model. It has achieved solid performance on many ad-hoc retrieval tasks. So far, these tasks have assumed a static document collection. In many practical scenarios, however, document collections are dynamic, where new documents are continuously added to the corpus. The ability to incrementally index new documents while preserving the ability to answer queries with both previously and newly indexed relevant documents is vital to applying GR models. In this paper, we address this practical continual learning problem for GR. We put forward a novel Continual-LEarner for generatiVE Retrieval (CLEVER) model and make two major contributions to continual learning for GR: (i) To encode new documents into docids with low computational cost, we present Incremental Product Quantization, which updates a partial quantization codebook according to two adaptive thresholds; and (ii) To memorize new documents for querying without forgetting previous knowledge, we propose a memory-augmented learning mechanism, to form meaningful connections between old and new documents. Empirical results demonstrate the effectiveness and efficiency of the proposed model.»
[_citation_number]: «14»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2210.01922)\]. Further details \[[6](http://arxiv.org/abs/2004.02349)\]\[[7](http://arxiv.org/abs/2105.01736)\]\[[8](http://arxiv.org/abs/1802.06159)\]\[[9](http://arxiv.org/abs/2005.09207)\]\[[10](http://arxiv.org/abs/2202.06991)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from
large table repositories based on NL queries. While current deep-learning-based
methods using the traditional dense vector search pipeline, i.e.,
representation-index-search, achieve remarkable accuracy, they
|    | reference                                                                                           |   date | key idea/summary                                                                                                                                                                                          |
|----|-----------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Continual Learning for Generative Retrieval over Dynamic Corpora](http://arxiv.org/abs/2308.14968) |    nan | The paper introduces CLEVER, a novel model for continual learning in generative retrieval, addressing the challenge of dynamically updating document collections while maintaining retrieval performance. |
### <a id='category-approximate-nearest-neighbor-search'></a>Approximate Nearest Neighbor Search: 1 papers found.
Context: 
	Document 1: [Category]: «Approximate Nearest Neighbor Search»
[Snippet]: «»
[_citation_number]: «15»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2210.01922)\]. Further details \[[6](http://arxiv.org/abs/2004.02349)\]\[[7](http://arxiv.org/abs/2105.01736)\]\[[8](http://arxiv.org/abs/1802.06159)\]\[[9](http://arxiv.org/abs/2005.09207)\]\[[10](http://arxiv.org/abs/2202.06991)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from
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
by 16
|    | reference                                                                            |   date | key idea/summary                                                                                          |
|----|--------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------|
|  0 | [(JOSIE:) Overlap Set Similarity Search for Finding Joinable Tables in Data Lakes]() |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
