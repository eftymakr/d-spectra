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
## Research papers
### Outline
- [Efficient Indexing and Retrieval Strategies [5 papers]](#category-efficient-indexing-and-retrieval-strategies)
- [Pre-trained Language Model Utilization [6 papers]](#category-pre-trained-language-model-utilization)
- [Synthetic Query Generation Techniques [1 papers]](#category-synthetic-query-generation-techniques)
- [Query-Table Semantic Alignment Challenges [1 papers]](#category-query-table-semantic-alignment-challenges)
- [Differentiable Search Index Frameworks [3 papers]](#category-differentiable-search-index-frameworks)

### <a id='category-efficient-indexing-and-retrieval-strategies'></a>Efficient Indexing and Retrieval Strategies: 5 papers found.
The category "Efficient Indexing and Retrieval Strategies" encompasses a range of approaches aimed at improving the performance and scalability of data retrieval systems. Data lakes, as repositories of raw data, face challenges in defining clear functions and technologies, highlighting the need for robust indexing and retrieval mechanisms \[[1](http://arxiv.org/abs/2106.09592)\]. In parallel, generative retrieval (GR) has emerged as a promising technique, where language models directly predict document identifiers (DocIDs) to enhance retrieval accuracy \[[13](http://arxiv.org/abs/2402.01176)\]. However, GR models typically assume static document collections, which limits their applicability in dynamic environments where new documents are continuously added \[[14](http://arxiv.org/abs/2308.14968)\]. To address this, recent work has introduced continual learning frameworks, such as CLEVER, which enable incremental indexing of new documents while preserving query performance \[[14](http://arxiv.org/abs/2308.14968)\]. Additionally, methods like CorpusLM integrate generative retrieval with closed-book generation and retrieval-augmented generation (RAG) to improve the end-to-end effectiveness of knowledge-intensive tasks \[[13](http://arxiv.org/abs/2402.01176)\]. These advancements underscore the growing focus on efficient indexing and retrieval strategies that balance accuracy, scalability, and adaptability in modern data systems.
|    | reference                                                                                                               |   date | key idea/summary                                                                                                                                                                                                                                             |
|----|-------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Data Lakes: A Survey of Functions and Systems](http://arxiv.org/abs/2106.09592)                                        |    nan | This survey provides a comprehensive overview of data lakes, their architectures, systems, and challenges, aiming to serve as a technical reference for designing and implementing data lakes.                                                               |
|  1 | [CorpusLM: Towards a Unified Language Model on Corpus for
  Knowledge-Intensive Tasks](http://arxiv.org/abs/2402.01176) |    nan | CorpusLM is a unified language model that improves knowledge-intensive tasks by integrating generative retrieval, closed-book generation, and RAG through a unified decoding process, achieving superior performance in both retrieval and downstream tasks. |
|  2 | [Continual Learning for Generative Retrieval over Dynamic Corpora](http://arxiv.org/abs/2308.14968)                     |    nan | The paper introduces CLEVER, a novel model for continual learning in generative retrieval, addressing the challenge of dynamically updating document collections while maintaining retrieval performance.                                                    |
|  3 | [(JOSIE:) Overlap Set Similarity Search for Finding Joinable Tables in Data Lakes]()                                    |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                    |
|  4 | [(DSI++:) Updating Transformer Memory with New Documents]()                                                             |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                    |
### <a id='category-pre-trained-language-model-utilization'></a>Pre-trained Language Model Utilization: 6 papers found.
The category "Pre-trained Language Model Utilization" encompasses a range of approaches that leverage pre-trained language models (PLMs) to enhance table discovery, retrieval, and question-answering tasks. These methods often focus on improving semantic alignment between natural language queries and structured data, such as tables, by utilizing PLMs for encoding and representation. For instance, Deepjoin employs a pre-trained language model to embed columns into vectors, enabling efficient and accurate joinable table discovery by measuring similarity in the vector space \[[1](http://arxiv.org/abs/2106.09592)\]. Similarly, Starmie introduces a contrastive learning method to train column encoders from PLMs in an unsupervised manner, capturing rich semantic information and achieving high performance in table union search \[[2](http://arxiv.org/abs/2212.07588)\]. The TAPAS framework extends BERT's architecture to encode tables directly, allowing for question answering without generating logical forms, and achieves state-of-the-art results on semantic parsing tasks \[[4](http://arxiv.org/abs/2301.03560)\]. Additionally, the GTR framework represents tables as multi-granular graphs and uses a Graph Transformer to capture both content and layout structures, enhancing generalizability and performance on complex tables \[[5](http://arxiv.org/abs/2103.12011)\]. These approaches highlight the versatility of PLMs in handling structured data, from improving join accuracy to enabling end-to-end question-answering over tables. Furthermore, methods like the one described in \[[6](http://arxiv.org/abs/2004.02349)\] explore how to effectively encode table content while considering structural constraints, demonstrating the ongoing efforts to integrate PLMs into table-related tasks. The use of PLMs in these contexts underscores their potential to overcome limitations of traditional methods, such as error accumulation and insufficient query-table interaction, by enabling more robust and semantically aligned representations.
|    | reference                                                                                                                                       |   date | key idea/summary                                                                                                                                                                                                                                                                           |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [DeepJoin: Joinable Table Discovery with Pre-trained Language Models](http://arxiv.org/abs/2212.07588)                                          |    nan | Deepjoin is a deep learning model that enables accurate and efficient joinable table discovery in data lakes by using pre-trained language models and contextualization techniques to handle both equi- and semantic joins.                                                                |
|  1 | [Semantics-aware Dataset Discovery from Data Lakes with Contextualized
  Column-based Representation Learning](http://arxiv.org/abs/2210.01922) |    nan | Starmie is an end-to-end framework for dataset discovery from data lakes, using contrastive learning and HNSW indexing to improve the effectiveness and performance of table union search.                                                                                                 |
|  2 | [Open Domain Question Answering over Tables via Dense Retrieval](http://arxiv.org/abs/2103.12011)                                               |    nan | This work introduces a retriever specifically designed for open-domain QA over tables, improving retrieval and end-to-end QA results compared to a BERT-based retriever.                                                                                                                   |
|  3 | [TAPAS: Weakly Supervised Table Parsing via Pre-training](http://arxiv.org/abs/2004.02349)                                                      |    nan | TAPAS is a novel approach for answering natural language questions over tables that avoids generating logical forms, instead directly predicting denotations by selecting table cells and applying aggregation operators, achieving state-of-the-art results on semantic parsing datasets. |
|  4 | [Retrieving Complex Tables with Multi-Granular Graph Representation
  Learning](http://arxiv.org/abs/2105.01736)                                |    nan | The paper introduces Graph-based Table Retrieval (GTR), a novel framework for natural language table retrieval that uses multi-granular graph representation and a Graph Transformer model to effectively handle complex table layouts and diverse query intents.                          |
|  5 | [Table Search Using a Deep Contextualized Language Model](http://arxiv.org/abs/2005.09207)                                                      |    nan | The paper proposes an approach that integrates features from prior literature with BERT for ad hoc table retrieval, achieving significant improvements over previous methods and BERT baselines.                                                                                           |
### <a id='category-synthetic-query-generation-techniques'></a>Synthetic Query Generation Techniques: 1 papers found.
Context: 
	Document 1: [Category]: «Synthetic Query Generation Techniques»
[_citation_number]: «4»
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

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2210.01922)\]. Further details \[[6](http://arxiv.org/abs/2004.02349)\]\[[7](http://arxiv.org/abs/2105.01736)\]\[[8](http://arxiv.org/abs/1802.06159)\]\[[9](http://arxiv.org/abs/2005.09207)\]\[[10](http://arxiv.org/abs/2202.06991)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2210.01922)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2212.07588)\]\[[7](http://arxiv.org/abs/2105.01736)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Synthetic query generation techniques aim to overcome the limitations of traditional keyword-based search systems by enabling users to interact with data through natural language questions \[[4](http://arxiv.org/abs/2301.03560)\]. These techniques are particularly important in the context of data discovery systems, where the ability to handle complex and semantically rich queries is essential for improving user experience and query accuracy \[[4](http://arxiv.org/abs/2301.03560)\]. Current approaches often rely on expensive training data, which limits their scalability and practical deployment \[[4](http://arxiv.org/abs/2301.03560)\]. To address this, researchers have proposed self-supervised methods that generate synthetic queries and train models without human intervention, thereby reducing the dependency on costly annotated datasets \[[4](http://arxiv.org/abs/2301.03560)\]. These methods also focus on designing effective table representation strategies and relevance models that can work with synthetically generated questions \[[4](http://arxiv.org/abs/2301.03560)\]. The integration of these components into a unified system, such as Solo, demonstrates the potential of synthetic query generation in advancing learned discovery systems \[[4](http://arxiv.org/abs/2301.03560)\].
|    | reference                                                                                                                 |   date | key idea/summary                                                                                                                                                                                                           |
|----|---------------------------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Solo: Data Discovery Using Natural Language Questions Via A
  Self-Supervised Approach](http://arxiv.org/abs/2301.03560) |    nan | The paper introduces a self-supervised approach to train learned data discovery systems without human intervention, leading to the development of the Solo system that outperforms state-of-the-art methods on benchmarks. |
### <a id='category-query-table-semantic-alignment-challenges'></a>Query-Table Semantic Alignment Challenges: 1 papers found.
Context: 
	Document 1: [Category]: «Query-Table Semantic Alignment Challenges»
[_citation_number]: «8»
[Snippet]: «We introduce and address the problem of ad hoc table retrieval: answering a keyword query with a ranked list of tables. This task is not only interesting on its own account, but is also being used as a core component in many other table-based information access scenarios, such as table completion or table mining. The main novel contribution of this work is a method for performing semantic matching between queries and tables. Specifically, we (i) represent queries and tables in multiple semantic spaces (both discrete sparse and continuous dense vector representations) and (ii) introduce various similarity measures for matching those semantic representations. We consider all possible combinations of semantic representations and similarity measures and use these as features in a supervised learning model. Using a purpose-built test collection based on Wikipedia tables, we demonstrate significant and substantial improvements over a state-of-the-art baseline.»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2210.01922)\]. Further details \[[6](http://arxiv.org/abs/2004.02349)\]\[[7](http://arxiv.org/abs/2105.01736)\]\[[8](http://arxiv.org/abs/1802.06159)\]\[[9](http://arxiv.org/abs/2005.09207)\]\[[10](http://arxiv.org/abs/2202.06991)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from large table repositories based on NL queries. While current deep-learning-based methods using the traditional dense vector search pipeline, i.e., representation-index-search, achieve remarkable accuracy, they face several limitations that impede further performance improvements: (i) the errors accumulated during the table representation and indexing phases affect the subsequent search accuracy; and (ii) insufficient query-table interaction hinders effective semantic alignment, impeding accuracy improvements. In this paper, we propose a novel framework Birdie, using a differentiable search index. It unifies the indexing and search into a single encoder-decoder language model, thus getting rid of error accumulations. Birdie first assigns each table a prefix-aware identifier and leverages a large language model-based query generator to create synthetic queries for each table. It then encodes the mapping between synthetic queries/tables and their corresponding table identifiers into the parameters of an encoder-decoder language model, enabling deep query-table interactions. During search, the trained model directly generates table identifiers for a given query. To accommodate the continual indexing of dynamic tables, we introduce an index update strategy via parameter isolation, which mitigates the issue of catastrophic forgetting. Extensive experiments demonstrate that Birdie outperforms state-of-the-art dense methods by 16.8% in accuracy, and reduces forgetting by over 90% compared to other continual learning approaches.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2210.01922)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2212.07588)\]\[[7](http://arxiv.org/abs/2105.01736)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
The category "Query-Table Semantic Alignment Challenges" addresses the difficulties in aligning natural language queries with tabular data, a critical task in information retrieval \[[8](http://arxiv.org/abs/1802.06159)\]. This problem is particularly relevant in scenarios such as table completion and table mining, where accurate semantic matching is essential for effective data access \[[8](http://arxiv.org/abs/1802.06159)\]. Existing approaches often rely on traditional dense vector search pipelines, which involve representation, indexing, and search stages, but these methods face limitations such as error accumulation during the indexing phase and insufficient interaction between queries and tables, which hinder semantic alignment \[[8](http://arxiv.org/abs/1802.06159)\]. The challenge lies in developing methods that can accurately represent both queries and tables in multiple semantic spaces, including discrete sparse and continuous dense vector representations, and then apply appropriate similarity measures to match these representations \[[8](http://arxiv.org/abs/1802.06159)\]. The work introduces a supervised learning model that considers all combinations of semantic representations and similarity measures, leading to significant improvements over existing baselines \[[8](http://arxiv.org/abs/1802.06159)\]. This highlights the ongoing need for more sophisticated alignment techniques that can enhance the accuracy and robustness of table retrieval systems.
|    | reference                                                                           |   date | key idea/summary                                                                                                                                                                       |
|----|-------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Ad Hoc Table Retrieval using Semantic Similarity](http://arxiv.org/abs/1802.06159) |    nan | The paper introduces a method for semantic matching between keyword queries and tables, using multiple semantic spaces and similarity measures to improve table retrieval performance. |
### <a id='category-differentiable-search-index-frameworks'></a>Differentiable Search Index Frameworks: 3 papers found.
Context: 
	Document 1: [Category]: «Differentiable Search Index Frameworks»
[_citation_number]: «10»
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

	Document 2: [Category]: «Differentiable Search Index Frameworks»
[_citation_number]: «11»
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

	Document 3: [Category]: «Differentiable Search Index Frameworks»
[_citation_number]: «12»
[Snippet]: «The Differentiable Search Index (DSI) is an emerging paradigm for information
retrieval. Unlike traditional retrieval architectures where index and retrieval
are two different and separate components, DSI uses a single transformer model
to perform both indexing and retrieval.
  In this paper, we identify and tackle an important issue of current DSI
models: the data distribution mismatch that occurs between the DSI indexing and
retrieval processes. Specifically, we argue that, at indexing, current DSI
methods learn to build connections between the text of long documents and the
identifier of the documents, but then retrieval of document identifiers is
based on queries that are commonly much shorter than the indexed documents.
This problem is further exacerbated when using DSI for cross-lingual retrieval,
where document text and query text are in different languages.
  To address this fundamental problem of current DSI models, we propose a
simple yet effective indexing framework for DSI, called DSI-QG. When indexing,
DSI-QG represents documents with a number of potentially relevant queries
generated by a query generation model and re-ranked and filtered by a
cross-encoder ranker. The presence of these queries at indexing allows the DSI
models to connect a document identifier to a set of queries, hence mitigating
data distribution mismatches present between the indexing and the retrieval
phases. Empirical results on popular mono-lingual and cross-lingual passage
retrieval datasets show that DSI-QG significantly outperforms the original DSI
model.»


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
by 16.8% in accuracy, and reduces forgetting by over 90% compared to other
continual learning approaches.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2210.01922)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2212.07588)\]\[[7](http://arxiv.org/abs/2105.01736)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Differentiable Search Index (DSI) frameworks represent a significant advancement in information retrieval by unifying indexing and retrieval into a single model, eliminating the need for separate components \[[10](http://arxiv.org/abs/2202.06991)\]. This paradigm enables models to directly map queries to document identifiers using only their parameters, thereby simplifying the retrieval process \[[10](http://arxiv.org/abs/2202.06991)\]. However, existing DSI models face challenges related to data distribution mismatches between indexing and retrieval phases, particularly when queries are shorter than indexed documents or when cross-lingual retrieval is required \[[12](http://arxiv.org/abs/2206.10128)\]. To address these issues, researchers have proposed improvements such as DSI-QG, which generates relevant queries during indexing to better align with retrieval queries \[[12](http://arxiv.org/abs/2206.10128)\]. Additionally, other approaches like the Neural Corpus Indexer (NCI) have introduced novel architectures, such as prefix-aware weight-adaptive decoders, to enhance recall performance \[[11](http://arxiv.org/abs/2206.02743)\]. These developments highlight the ongoing efforts to improve the robustness and effectiveness of differentiable search index frameworks, particularly in handling complex retrieval tasks and dynamic indexing scenarios.
|    | reference                                                                                                                                  |   date | key idea/summary                                                                                                                                                                                                                                                  |
|----|--------------------------------------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Transformer Memory as a Differentiable Search Index](http://arxiv.org/abs/2202.06991)                                                     |    nan | The paper introduces the Differentiable Search Index (DSI), a novel paradigm that uses a single Transformer model to directly answer queries by encoding all corpus information into its parameters, significantly simplifying the information retrieval process. |
|  1 | [A Neural Corpus Indexer for Document Retrieval](http://arxiv.org/abs/2206.02743)                                                          |    nan | The paper introduces Neural Corpus Indexer (NCI), an end-to-end deep neural network that improves recall performance in document retrieval by unifying training and indexing stages with a prefix-aware weight-adaptive decoder architecture.                     |
|  2 | [Bridging the Gap Between Indexing and Retrieval for Differentiable
  Search Index with Query Generation](http://arxiv.org/abs/2206.10128) |    nan | DSI-QG is an indexing framework for Differentiable Search Index (DSI) models that addresses data distribution mismatches by generating and using relevant queries during indexing to improve retrieval performance.                                               |
