## Related Works

Recent advances in information retrieval have seen a shift from traditional sparse retrieval methods to dense retrieval frameworks that leverage deep learning models for more accurate and semantically rich representations. Early work on dense retrieval focused on using pre-trained language models like BERT for encoding both queries and documents, enabling more nuanced semantic matching \[[14](http://arxiv.org/abs/1910.14424)\]. This approach has been further refined with models such as ColBERT, which introduces a late interaction mechanism that allows for efficient retrieval by precomputing document representations and using vector similarity indexes \[[8](http://arxiv.org/abs/2004.12832)\]. These models significantly improve retrieval performance compared to traditional methods like BM25, often achieving two orders of magnitude faster query processing \[[8](http://arxiv.org/abs/2004.12832)\].

The problem of table retrieval has also seen significant attention, with methods leveraging deep contextualized language models to encode table content while considering both structure and input constraints \[[6](http://arxiv.org/abs/2005.09207)\]. These models often incorporate features from prior literature and jointly train them with BERT to improve performance on public datasets \[[6](http://arxiv.org/abs/2005.09207)\]. Similarly, semantic table retrieval has been explored using multiple semantic spaces and similarity measures to match queries and tables \[[13](http://arxiv.org/abs/2105.06365)\]. This work demonstrates that using a combination of discrete and continuous representations can lead to substantial improvements over state-of-the-art baselines \[[13](http://arxiv.org/abs/2105.06365)\].

However, these methods often suffer from error accumulation during the indexing and search phases, as well as limited query-table interaction that hinders semantic alignment \[[1](http://arxiv.org/abs/2204.10628)\]. To address these limitations, recent work has introduced differentiable search indices (DSI) that unify indexing and retrieval into a single model, eliminating error accumulation \[[3](http://arxiv.org/abs/2202.06991)\]. DSI models encode a corpus of documents in their parameters and use the same model to answer queries directly, significantly simplifying the retrieval process \[[3](http://arxiv.org/abs/2202.06991)\]. This approach has been further extended with DSI-QG, which generates relevant queries during indexing to mitigate data distribution mismatches between indexing and retrieval \[[5](http://arxiv.org/abs/2206.10128)\].

Continual learning remains a challenge for DSI models, as retraining the model when new documents are added leads to catastrophic forgetting \[[7](http://arxiv.org/abs/2212.09744)\]. To address this, DSI++ introduces a continual learning framework that allows incremental indexing of new documents while maintaining retrieval performance for previously indexed documents \[[7](http://arxiv.org/abs/2212.09744)\]. This work demonstrates that continual indexing can be achieved with minimal model updates, significantly reducing computational costs compared to retraining \[[7](http://arxiv.org/abs/2212.09744)\].

In addition, the use of query generation models to create synthetic queries for each table has been explored to enhance query-table interaction \[[1](http://arxiv.org/abs/2204.10628)\]. This approach, combined with a differentiable search index, allows for more effective semantic alignment during retrieval \[[1](http://arxiv.org/abs/2204.10628)\]. The proposed framework, Birdie, builds upon these ideas by using a prefix-aware identifier for each table and a large language model-based query generator to create synthetic queries, enabling deep query-table interactions \[[1](http://arxiv.org/abs/2204.10628)\]. These techniques are critical for improving accuracy and reducing forgetting in dynamic table retrieval scenarios \[[1](http://arxiv.org/abs/2204.10628)\].

1. \[[1](http://arxiv.org/abs/2204.10628)\] "Natural language (NL)-driven table discovery identifies relevant tables from large table repositories based on NL queries. While current deep-learning-based methods using the traditional dense vector search pipeline, i.e., representation-index-search, achieve remarkable accuracy, they face several limitations that impede further performance improvements: (i) the errors accumulated during the table representation and indexing phases affect the subsequent search accuracy; and (ii) insufficient query-table interaction hinders effective semantic alignment, impeding accuracy improvements. In this paper, we propose a novel framework Birdie, using a differentiable search index. It unifies the indexing and search into a single encoder-decoder language model, thus getting rid of error accumulations. Birdie first assigns each table a prefix-aware identifier and leverages a large language model-based query generator to create synthetic queries for each table. It then encodes the mapping between synthetic queries/tables and their corresponding table identifiers into the parameters of an encoder-decoder language model, enabling deep query-table interactions. During search, the trained model directly generates table identifiers for a given query. To accommodate the continual indexing of dynamic tables, we introduce an index update strategy via parameter isolation, which mitigates the issue of catastrophic forgetting. Extensive experiments demonstrate that Birdie outperforms state-of-the-art dense methods by 16.8% in accuracy, and reduces forgetting by over 90% compared to other continual learning approaches."
2. \[[3](http://arxiv.org/abs/2202.06991)\] "Transformer Memory as a Differentiable Search Index[http://arxiv.org/abs/2202.06991]: In this paper, we demonstrate that information retrieval can be accomplished with a single Transformer, in which all information about the corpus is encoded in the parameters of the model. To this end, we introduce the Differentiable Search Index (DSI), a new paradigm that learns a text-to-text model that maps string queries directly to relevant docids; in other words, a DSI model answers queries directly using only its parameters, dramatically simplifying the whole retrieval process."
3. \[[5](http://arxiv.org/abs/2206.10128)\] "Bridging the Gap Between Indexing and Retrieval for Differentiable Search Index with Query Generation[http://arxiv.org/abs/2206.10128]: The Differentiable Search Index (DSI) is an emerging paradigm for information retrieval. Unlike traditional retrieval architectures where index and retrieval are two different and separate components, DSI uses a single transformer model to perform both indexing and retrieval. In this paper, we identify and tackle an important issue of current DSI models: the data distribution mismatch that occurs between the DSI indexing and retrieval processes."
4. \[[7](http://arxiv.org/abs/2212.09744)\] "DSI++: Updating Transformer Memory with New Documents[http://arxiv.org/abs/2212.09744]: Differentiable Search Indices (DSIs) encode a corpus of documents in model parameters and use the same model to answer user queries directly. Despite the strong performance of DSI models, deploying them in situations where the corpus changes over time is computationally expensive because reindexing the corpus requires re-training the model. In this work, we introduce DSI++, a continual learning challenge for DSI to incrementally index new documents while being able to answer queries related to both previously and newly indexed documents."
5. \[[14](http://arxiv.org/abs/1910.14424)\] "Multi-Stage Document Ranking with BERT[http://arxiv.org/abs/1910.14424]: The advent of deep neural networks pre-trained via language modeling tasks has spurred a number of successful applications in natural language processing. This work explores one such popular model, BERT, in the context of document ranking. We propose two variants, called monoBERT and duoBERT, that formulate the ranking problem as pointwise and pairwise classification, respectively. These two models are arranged in a multi-stage ranking architecture to form an end-to-end search system."
## Research papers
### Outline
- [Integration of Large Language Models [4 papers]](#category-integration-of-large-language-models)
- [Query Generation for Retrieval [1 papers]](#category-query-generation-for-retrieval)
- [Differentiable Search Index (DSI) Frameworks [2 papers]](#category-differentiable-search-index-(dsi)-frameworks)
- [Traditional vs. Dense Retrieval Methods [2 papers]](#category-traditional-vs.-dense-retrieval-methods)
- [Deep Learning in Table Retrieval [3 papers]](#category-deep-learning-in-table-retrieval)
- [Continual Learning in DSI Models [1 papers]](#category-continual-learning-in-dsi-models)
- [Query-Table Interaction and Semantic Alignment [2 papers]](#category-query-table-interaction-and-semantic-alignment)

### <a id='category-integration-of-large-language-models'></a>Integration of Large Language Models: 4 papers found.
Context: 
	Document 1: [Category]: «Integration of Large Language Models»
[Snippet]: «Knowledge-intensive language tasks require NLP systems to both provide the correct answer and retrieve supporting evidence for it in a given corpus. Autoregressive language models are emerging as the de-facto standard for generating answers, with newer and more powerful systems emerging at an astonishing pace. In this paper we argue that all this (and future) progress can be directly applied to the retrieval problem with minimal intervention to the models' architecture. Previous work has explored ways to partition the search space into hierarchical structures and retrieve documents by autoregressively generating their unique identifier. In this work we propose an alternative that doesn't force any structure in the search space: using all ngrams in a passage as its possible identifiers. This setup allows us to use an autoregressive model to generate and score distinctive ngrams, that are then mapped to full passages through an efficient data structure. Empirically, we show this not only outperforms prior autoregressive approaches but also leads to an average improvement of at least 10 points over more established retrieval solutions for passage-level retrieval on the KILT benchmark, establishing new state-of-the-art downstream performance on some datasets, while using a considerably lighter memory footprint than competing systems. Code and pre-trained models at https://github.com/facebookresearch/SEAL.»
[_citation_number]: «1»

	Document 2: [Category]: «Integration of Large Language Models»
[Snippet]: «Recent progress in Natural Language Understanding (NLU) is driving fast-paced advances in Information Retrieval (IR), largely owed to fine-tuning deep language models (LMs) for document ranking. While remarkably effective, the ranking models based on these LMs increase computational cost by orders of magnitude over prior approaches, particularly as they must feed each query-document pair through a massive neural network to compute a single relevance score. To tackle this, we present ColBERT, a novel ranking model that adapts deep LMs (in particular, BERT) for efficient retrieval. ColBERT introduces a late interaction architecture that independently encodes the query and the document using BERT and then employs a cheap yet powerful interaction step that models their fine-grained similarity. By delaying and yet retaining this fine-granular interaction, ColBERT can leverage the expressiveness of deep LMs while simultaneously gaining the ability to pre-compute document representations offline, considerably speeding up query processing. Crucially, ColBERT's pruning-friendly interaction mechanism enables leveraging vector-similarity indexes for end-to-end retrieval directly from millions of documents. We extensively evaluate ColBERT using two recent passage search datasets. Results show that ColBERT's effectiveness is competitive with existing BERT-based models (and outperforms every non-BERT baseline), while executing two orders-of-magnitude faster and requiring up to four orders-of-magnitude fewer FLOPs per query.»
[_citation_number]: «8»

	Document 3: [Category]: «Integration of Large Language Models»
[Snippet]: «The advent of deep neural networks pre-trained via language modeling tasks has spurred a number of successful applications in natural language processing. This work explores one such popular model, BERT, in the context of document ranking. We propose two variants, called monoBERT and duoBERT, that formulate the ranking problem as pointwise and pairwise classification, respectively. These two models are arranged in a multi-stage ranking architecture to form an end-to-end search system. One major advantage of this design is the ability to trade off quality against latency by controlling the admission of candidates into each pipeline stage, and by doing so, we are able to find operating points that offer a good balance between these two competing metrics. On two large-scale datasets, MS MARCO and TREC CAR, experiments show that our model produces results that are either at or comparable to the state of the art. Ablation studies show the contributions of each component and characterize the latency/quality tradeoff space.»
[_citation_number]: «14»

	Document 4: [Category]: «Integration of Large Language Models»
[Snippet]: «Transfer learning, where a model is first pre-trained on a data-rich task before being fine-tuned on a downstream task, has emerged as a powerful technique in natural language processing (NLP). The effectiveness of transfer learning has given rise to a diversity of approaches, methodology, and practice. In this paper, we explore the landscape of transfer learning techniques for NLP by introducing a unified framework that converts every language problem into a text-to-text format. Our systematic study compares pre-training objectives, architectures, unlabeled datasets, transfer approaches, and other factors on dozens of language understanding tasks. By combining the insights from our exploration with scale and our new "Colossal Clean Crawled Corpus", we achieve state-of-the-art results on many benchmarks covering summarization, question answering, text classification, and more. To facilitate future work on transfer learning for NLP, we release our dataset, pre-trained models, and code.»
[_citation_number]: «15»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2202.06991)\]. Further details \[[6](http://arxiv.org/abs/2005.09207)\]\[[7](http://arxiv.org/abs/2212.09744)\]\[[8](http://arxiv.org/abs/2004.12832)\]\[[9](http://arxiv.org/abs/1802.06159)\]\[[10](https://www.semanticscholar.org/paper/373588873bef360e3ecad2e091ac17895eb863af)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2202.06991)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2206.02743)\]\[[7](http://arxiv.org/abs/2212.09744)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Recent advancements in the integration of large language models (LLMs) have significantly impacted information retrieval and document ranking tasks. Autoregressive models have become the de facto standard for generating answers, with newer systems showing rapid progress \[[1](http://arxiv.org/abs/2204.10628)\]. These models are being applied to retrieval problems with minimal architectural changes, allowing for more efficient and effective search strategies \[[1](http://arxiv.org/abs/2204.10628)\]. For instance, approaches that use ngrams as identifiers for passages enable autoregressive models to generate and score distinctive ngrams, which are then mapped to full passages through an efficient data structure, leading to improved performance \[[1](http://arxiv.org/abs/2204.10628)\]. Similarly, ColBERT introduces a late interaction architecture that independently encodes queries and documents using BERT, followed by a cheap yet powerful interaction step that models fine-grained similarity, thereby enhancing retrieval efficiency and accuracy \[[8](http://arxiv.org/abs/2004.12832)\]. Additionally, variants of BERT such as monoBERT and duoBERT have been proposed to address ranking problems through pointwise and pairwise classification, forming multi-stage architectures that balance quality and latency \[[14](http://arxiv.org/abs/1910.14424)\]. These developments highlight the growing trend of leveraging LLMs for more sophisticated and efficient retrieval systems, addressing limitations such as error accumulation and insufficient query-document interaction \[[1](http://arxiv.org/abs/2204.10628)\]\[[8](http://arxiv.org/abs/2004.12832)\]\[[14](http://arxiv.org/abs/1910.14424)\].
|    | reference                                                                                                                        | date     | key idea/summary                                                                                                                                                                                                                     |
|----|----------------------------------------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Autoregressive Search Engines: Generating Substrings as Document Identifiers](http://arxiv.org/abs/2204.10628)                  | 04/22/22 | The paper proposes an autoregressive approach for passage-level retrieval that uses all ngrams in a passage as identifiers, achieving state-of-the-art performance with a lighter memory footprint.                                  |
|  1 | [ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](http://arxiv.org/abs/2004.12832) | 04/27/20 | ColBERT is an efficient ranking model that leverages deep language models like BERT for information retrieval by using a late interaction architecture to reduce computational cost while maintaining effectiveness.                 |
|  2 | [Multi-Stage Document Ranking with BERT](http://arxiv.org/abs/1910.14424)                                                        | 10/31/19 | This work introduces monoBERT and duoBERT variants of BERT for document ranking, achieving state-of-the-art results on large-scale datasets while enabling a balance between quality and latency through a multi-stage architecture. |
|  3 | [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](http://arxiv.org/abs/1910.10683)             | 10/23/19 | This paper introduces a unified framework for transfer learning in NLP, converting language problems into text-to-text format, and achieves state-of-the-art results using a large-scale dataset and pre-trained models.             |
### <a id='category-query-generation-for-retrieval'></a>Query Generation for Retrieval: 1 papers found.
Context: 
	Document 1: [Category]: «Query Generation for Retrieval»
[Snippet]: «Current state-of-the-art document retrieval solutions mainly follow an index-retrieve paradigm, where the index is hard to be directly optimized for the final retrieval target. In this paper, we aim to show that an end-to-end deep neural network unifying training and indexing stages can significantly improve the recall performance of traditional methods. To this end, we propose Neural Corpus Indexer (NCI), a sequence-to-sequence network that generates relevant document identifiers directly for a designated query. To optimize the recall performance of NCI, we invent a prefix-aware weight-adaptive decoder architecture, and leverage tailored techniques including query generation, semantic document identifiers, and consistency-based regularization. Empirical studies demonstrated the superiority of NCI on two commonly used academic benchmarks, achieving +21.4% and +16.8% relative enhancement for Recall@1 on NQ320k dataset and R-Precision on TriviaQA dataset, respectively, compared to the best baseline method.»
[_citation_number]: «2»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2202.06991)\]. Further details \[[6](http://arxiv.org/abs/2005.09207)\]\[[7](http://arxiv.org/abs/2212.09744)\]\[[8](http://arxiv.org/abs/2004.12832)\]\[[9](http://arxiv.org/abs/1802.06159)\]\[[10](https://www.semanticscholar.org/paper/373588873bef360e3ecad2e091ac17895eb863af)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2202.06991)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2206.02743)\]\[[7](http://arxiv.org/abs/2212.09744)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The field of query generation for retrieval has seen significant advancements with the introduction of end-to-end deep learning frameworks that unify training and indexing stages \[[2](http://arxiv.org/abs/2206.02743)\]. Traditional methods rely on an index-retrieve paradigm, where the index is difficult to optimize directly for the final retrieval target \[[2](http://arxiv.org/abs/2206.02743)\]. This limitation has led to suboptimal recall performance due to error accumulation during representation and indexing phases \[[2](http://arxiv.org/abs/2206.02743)\]. To address these challenges, researchers have proposed innovative architectures such as the Neural Corpus Indexer (NCI), which employs a sequence-to-sequence network to generate relevant document identifiers directly for a given query \[[2](http://arxiv.org/abs/2206.02743)\]. This approach leverages a prefix-aware weight-adaptive decoder and incorporates techniques like query generation, semantic document identifiers, and consistency-based regularization to enhance recall performance \[[2](http://arxiv.org/abs/2206.02743)\]. Empirical studies have demonstrated that such methods can achieve substantial improvements, with NCI showing a +21.4% relative enhancement in Recall@1 on the NQ320k dataset and a +16.8% improvement in R-Precision on the TriviaQA dataset compared to existing baselines \[[2](http://arxiv.org/abs/2206.02743)\]. These developments highlight the potential of integrating query generation within retrieval systems to improve both accuracy and robustness.
|    | reference                                                                         | date     | key idea/summary                                                                                                                                                                                                                                         |
|----|-----------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [A Neural Corpus Indexer for Document Retrieval](http://arxiv.org/abs/2206.02743) | 06/06/22 | The paper introduces Neural Corpus Indexer (NCI), an end-to-end deep neural network that improves recall performance in document retrieval by unifying training and indexing stages with a prefix-aware weight-adaptive decoder and tailored techniques. |
### <a id='category-differentiable-search-index-(dsi)-frameworks'></a>Differentiable Search Index (DSI) Frameworks: 2 papers found.
The Differentiable Search Index (DSI) framework represents a significant shift in information retrieval by integrating indexing and retrieval into a single transformer model, eliminating the need for separate components \[[3](http://arxiv.org/abs/2202.06991)\]. This approach allows the model to directly map queries to document identifiers using only its parameters, simplifying the retrieval process and improving efficiency \[[3](http://arxiv.org/abs/2202.06991)\]. However, existing DSI models face challenges due to data distribution mismatches between indexing and retrieval, particularly when dealing with short queries compared to long documents \[[5](http://arxiv.org/abs/2206.10128)\]. To address this, the DSI-QG framework was introduced, which generates relevant queries during indexing to better align with retrieval-phase query characteristics \[[5](http://arxiv.org/abs/2206.10128)\]. This innovation enhances the model's ability to generalize across different scenarios, including cross-lingual retrieval, and has shown superior performance over traditional DSI models \[[5](http://arxiv.org/abs/2206.10128)\]. The core idea of using synthetic queries to improve semantic alignment and reduce error accumulation is also echoed in the Birdie framework, which applies DSI principles to table discovery tasks by generating synthetic queries for each table and encoding their relationships into a single encoder-decoder model \[[1](http://arxiv.org/abs/2204.10628)\]. These advancements highlight the evolving landscape of DSI frameworks, emphasizing the importance of query-document interaction and continuous learning mechanisms to maintain performance in dynamic environments \[[1](http://arxiv.org/abs/2204.10628)\].
|    | reference                                                                                                                                | date     | key idea/summary                                                                                                                                                                                                                                                                                       |
|----|------------------------------------------------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Transformer Memory as a Differentiable Search Index](http://arxiv.org/abs/2202.06991)                                                   | 02/14/22 | The paper introduces the Differentiable Search Index (DSI), a novel paradigm that uses a single Transformer model to directly answer queries by encoding all corpus information into its parameters, significantly simplifying the information retrieval process and outperforming existing baselines. |
|  1 | [Bridging the Gap Between Indexing and Retrieval for Differentiable Search Index with Query Generation](http://arxiv.org/abs/2206.10128) | 06/21/22 | DSI-QG is a novel indexing framework for Differentiable Search Index (DSI) that addresses data distribution mismatches by generating and using relevant queries during indexing to improve retrieval performance.                                                                                      |
### <a id='category-traditional-vs.-dense-retrieval-methods'></a>Traditional vs. Dense Retrieval Methods: 2 papers found.
Context: 
	Document 1: [Category]: «Traditional vs. Dense Retrieval Methods»
[Snippet]: «Pyserini is a Python toolkit for reproducible information retrieval research with sparse and dense representations. It aims to provide effective, reproducible, and easy-to-use first-stage retrieval in a multi-stage ranking architecture. Our toolkit is self-contained as a standard Python package and comes with queries, relevance judgments, pre-built indexes, and evaluation scripts for many commonly used IR test collections. We aim to support, out of the box, the entire research lifecycle of efforts aimed at improving ranking with modern neural approaches. In particular, Pyserini supports sparse retrieval (e.g., BM25 scoring using bag-of-words representations), dense retrieval (e.g., nearest-neighbor search on transformer-encoded representations), as well as hybrid retrieval that integrates both approaches.»
[_citation_number]: «4»

	Document 2: [Category]: «Traditional vs. Dense Retrieval Methods»
[Snippet]: «Open-domain question answering relies on efficient passage retrieval to select candidate contexts, where traditional sparse vector space models, such as TF-IDF or BM25, are the de facto method. In this work, we show that retrieval can be practically implemented using dense representations alone, where embeddings are learned from a small number of questions and passages by a simple dual-encoder framework. When evaluated on a wide range of open-domain QA datasets, our dense retriever outperforms a strong Lucene-BM25 system largely by 9%-19% absolute in terms of top-20 passage retrieval accuracy, and helps our end-to-end QA system establish new state-of-the-art on multiple open-domain QA benchmarks.»
[_citation_number]: «12»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2202.06991)\]. Further details \[[6](http://arxiv.org/abs/2005.09207)\]\[[7](http://arxiv.org/abs/2212.09744)\]\[[8](http://arxiv.org/abs/2004.12832)\]\[[9](http://arxiv.org/abs/1802.06159)\]\[[10](https://www.semanticscholar.org/paper/373588873bef360e3ecad2e091ac17895eb863af)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2202.06991)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2206.02743)\]\[[7](http://arxiv.org/abs/2212.09744)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Recent advancements in information retrieval have highlighted the trade-offs between traditional sparse and dense retrieval methods. Traditional methods, such as BM25 and TF-IDF, remain widely used for their simplicity and efficiency \[[4](https://www.semanticscholar.org/paper/d69c0ed04ecc852e8c921900d3e7967f74f81263)\]. However, dense retrieval methods, which rely on neural embeddings and semantic similarity, have shown significant improvements in accuracy, particularly in open-domain question answering tasks \[[12](http://arxiv.org/abs/2004.04906)\]. These methods often use dual-encoder frameworks to learn embeddings from questions and passages, enabling more effective semantic alignment. While dense retrieval offers superior performance, it also introduces challenges related to error accumulation during indexing and the need for robust query-table interaction. This has led to the development of hybrid approaches and novel architectures that aim to combine the strengths of both methods \[[4](https://www.semanticscholar.org/paper/d69c0ed04ecc852e8c921900d3e7967f74f81263)\].
|    | reference                                                                                                                                                                                          | date     | key idea/summary                                                                                                                                                                                                                               |
|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Pyserini: A Python Toolkit for Reproducible Information Retrieval Research with Sparse and Dense Representations](https://www.semanticscholar.org/paper/d69c0ed04ecc852e8c921900d3e7967f74f81263) | 07/11/21 | Pyserini is a Python toolkit designed for reproducible information retrieval research, supporting both sparse and dense retrieval methods, hybrid approaches, and the entire research lifecycle with pre-built resources and evaluation tools. |
|  1 | [Dense Passage Retrieval for Open-Domain Question Answering](http://arxiv.org/abs/2004.04906)                                                                                                      | 04/10/20 | This work demonstrates that dense representations can effectively replace traditional sparse methods like TF-IDF or BM25 for open-domain question answering, achieving significant improvements in passage retrieval accuracy.                 |
### <a id='category-deep-learning-in-table-retrieval'></a>Deep Learning in Table Retrieval: 3 papers found.
Context: 
	Document 1: [Category]: «Deep Learning in Table Retrieval»
[Snippet]: «Pretrained contextualized language models such as BERT have achieved impressive results on various natural language processing benchmarks. Benefiting from multiple pretraining tasks and large scale training corpora, pretrained models can capture complex syntactic word relations. In this paper, we use the deep contextualized language model BERT for the task of ad hoc table retrieval. We investigate how to encode table content considering the table structure and input length limit of BERT. We also propose an approach that incorporates features from prior literature on table retrieval and jointly trains them with BERT. In experiments on public datasets, we show that our best approach can outperform the previous state-of-the-art method and BERT baselines with a large margin under different evaluation metrics.»
[_citation_number]: «6»

	Document 2: [Category]: «Deep Learning in Table Retrieval»
[Snippet]: «We address the web table retrieval task, aiming to retrieve and rank web tables as whole answers to a given information need. To this end, we formally define web tables as multimodal objects. We then suggest a neural ranking model, termed MTR, which makes a novel use of Gated Multimodal Units (GMUs) to learn a joint-representation of the query and the different table modalities. We further enhance this model with a co-learning approach which utilizes automatically learned query-independent and query-dependent "helper'' labels. We evaluate the proposed solution using both ad hoc queries (WikiTables) and natural language questions (GNQtables). Overall, we demonstrate that our approach surpasses the performance of previously studied state-of-the-art baselines.»
[_citation_number]: «10»

	Document 3: [Category]: «Deep Learning in Table Retrieval»
[Snippet]: «Tables contain valuable knowledge in a structured form. We employ neural language modeling approaches to embed tabular data into vector spaces. Specifically, we consider different table elements, such caption, column headings, and cells, for training word and entity embeddings. These embeddings are then utilized in three particular table-related tasks, row population, column population, and table retrieval, by incorporating them into existing retrieval models as additional semantic similarity signals. Evaluation results show that table embeddings can significantly improve upon the performance of state-of-the-art baselines.»
[_citation_number]: «11»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2202.06991)\]. Further details \[[6](http://arxiv.org/abs/2005.09207)\]\[[7](http://arxiv.org/abs/2212.09744)\]\[[8](http://arxiv.org/abs/2004.12832)\]\[[9](http://arxiv.org/abs/1802.06159)\]\[[10](https://www.semanticscholar.org/paper/373588873bef360e3ecad2e091ac17895eb863af)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2202.06991)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2206.02743)\]\[[7](http://arxiv.org/abs/2212.09744)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer:  
Recent advances in deep learning have significantly enhanced table retrieval tasks by leveraging contextualized language models and multimodal representations. Pretrained models such as BERT have demonstrated strong performance in capturing syntactic and semantic relationships, enabling more accurate encoding of table content \[[6](http://arxiv.org/abs/2005.09207)\]. Researchers have also explored neural language modeling approaches to embed tabular data into vector spaces, incorporating elements like captions, column headings, and cells to train word and entity embeddings that improve retrieval performance \[[11](http://arxiv.org/abs/1906.00041)\]. Additionally, models such as MTR have introduced novel architectures that learn joint representations of queries and tables using Gated Multimodal Units (GMUs), further enhancing semantic alignment and ranking accuracy \[[10](https://www.semanticscholar.org/paper/373588873bef360e3ecad2e091ac17895eb863af)\]. These approaches highlight the growing emphasis on integrating deep learning techniques with structured data to address challenges in natural language-driven table discovery.
|    | reference                                                                                                                            | date     | key idea/summary                                                                                                                                                                                            |
|----|--------------------------------------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Table Search Using a Deep Contextualized Language Model](http://arxiv.org/abs/2005.09207)                                           | 05/19/20 | The paper proposes an approach that enhances ad hoc table retrieval using BERT by incorporating structural features and joint training, achieving better performance than previous methods.                 |
|  1 | [Web Table Retrieval using Multimodal Deep Learning](https://www.semanticscholar.org/paper/373588873bef360e3ecad2e091ac17895eb863af) | 07/25/20 | The paper introduces a neural ranking model called MTR for web table retrieval, which uses Gated Multimodal Units (GMUs) and co-learning with helper labels to improve performance over existing baselines. |
|  2 | [Table2Vec: Neural Word and Entity Embeddings for Table Population and Retrieval](http://arxiv.org/abs/1906.00041)                   | 05/31/19 | The paper proposes using neural language modeling to embed tabular data into vector spaces, improving performance in table-related tasks through semantic similarity signals.                               |
### <a id='category-continual-learning-in-dsi-models'></a>Continual Learning in DSI Models: 1 papers found.
Context: 
	Document 1: [Category]: «Continual Learning in DSI Models»
[Snippet]: «Differentiable Search Indices (DSIs) encode a corpus of documents in model parameters and use the same model to answer user queries directly. Despite the strong performance of DSI models, deploying them in situations where the corpus changes over time is computationally expensive because reindexing the corpus requires re-training the model. In this work, we introduce DSI++, a continual learning challenge for DSI to incrementally index new documents while being able to answer queries related to both previously and newly indexed documents. Across different model scales and document identifier representations, we show that continual indexing of new documents leads to considerable forgetting of previously indexed documents. We also hypothesize and verify that the model experiences forgetting events during training, leading to unstable learning. To mitigate these issues, we investigate two approaches. The first focuses on modifying the training dynamics. Flatter minima implicitly alleviate forgetting, so we optimize for flatter loss basins and show that the model stably memorizes more documents ($+12\%$). Next, we introduce a generative memory to sample pseudo-queries for documents and supplement them during continual indexing to prevent forgetting for the retrieval task. Extensive experiments on novel continual indexing benchmarks based on Natural Questions (NQ) and MS MARCO demonstrate that our proposed solution mitigates forgetting significantly. Concretely, it improves the average Hits@10 by $+21.1\%$ over competitive baselines for NQ and requires $6$ times fewer model updates compared to re-training the DSI model for incrementally indexing five corpora in a sequence.»
[_citation_number]: «7»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2202.06991)\]. Further details \[[6](http://arxiv.org/abs/2005.09207)\]\[[7](http://arxiv.org/abs/2212.09744)\]\[[8](http://arxiv.org/abs/2004.12832)\]\[[9](http://arxiv.org/abs/1802.06159)\]\[[10](https://www.semanticscholar.org/paper/373588873bef360e3ecad2e091ac17895eb863af)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2202.06991)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2206.02743)\]\[[7](http://arxiv.org/abs/2212.09744)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The continual learning challenge in Differentiable Search Index (DSI) models focuses on addressing the issue of catastrophic forgetting when incrementally indexing new documents while maintaining retrieval performance for previously indexed ones \[[7](http://arxiv.org/abs/2212.09744)\]. Traditional DSI models require retraining when the corpus changes, which is computationally expensive \[[7](http://arxiv.org/abs/2212.09744)\]. Recent work, such as DSI++, explores continual learning strategies to enable models to adapt to new data without retraining, thereby improving efficiency and reducing computational overhead \[[7](http://arxiv.org/abs/2212.09744)\]. One approach involves optimizing for flatter loss basins during training, which helps in stabilizing memory of previously indexed documents and improving retrieval accuracy \[[7](http://arxiv.org/abs/2212.09744)\]. Another method introduces a generative memory component that samples pseudo-queries for documents to prevent forgetting during the continual indexing process \[[7](http://arxiv.org/abs/2212.09744)\]. These techniques have shown promising results, with improvements in average Hits@10 scores and reduced model updates compared to retraining approaches \[[7](http://arxiv.org/abs/2212.09744)\]. The challenge remains in balancing the trade-off between maintaining performance on old data and efficiently adapting to new information, which is critical for real-world applications where data is constantly evolving \[[7](http://arxiv.org/abs/2212.09744)\].
|    | reference                                                                                | date     | key idea/summary                                                                                                                                                                                                                                                                           |
|----|------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [DSI++: Updating Transformer Memory with New Documents](http://arxiv.org/abs/2212.09744) | 12/19/22 | DSI++ addresses the issue of forgetting in continual learning for differentiable search indices by introducing methods to optimize for flatter minima and using a generative memory to prevent forgetting, significantly improving retrieval performance and reducing computational costs. |
### <a id='category-query-table-interaction-and-semantic-alignment'></a>Query-Table Interaction and Semantic Alignment: 2 papers found.
Context: 
	Document 1: [Category]: «Query-Table Interaction and Semantic Alignment»
[Snippet]: «We introduce and address the problem of ad hoc table retrieval: answering a keyword query with a ranked list of tables. This task is not only interesting on its own account, but is also being used as a core component in many other table-based information access scenarios, such as table completion or table mining. The main novel contribution of this work is a method for performing semantic matching between queries and tables. Specifically, we (i) represent queries and tables in multiple semantic spaces (both discrete sparse and continuous dense vector representations) and (ii) introduce various similarity measures for matching those semantic representations. We consider all possible combinations of semantic representations and similarity measures and use these as features in a supervised learning model. Using a purpose-built test collection based on Wikipedia tables, we demonstrate significant and substantial improvements over a state-of-the-art baseline.»
[_citation_number]: «9»

	Document 2: [Category]: «Query-Table Interaction and Semantic Alignment»
[Snippet]: «Tables on the Web contain a vast amount of knowledge in a structured form. To tap into this valuable resource, we address the problem of table retrieval: answering an information need with a ranked list of tables. We investigate this problem in two different variants, based on how the information need is expressed: as a keyword query or as an existing table ("query-by-table"). The main novel contribution of this work is a semantic table retrieval framework for matching information needs (keyword or table queries) against tables. Specifically, we (i) represent queries and tables in multiple semantic spaces (both discrete sparse and continuous dense vector representations) and (ii) introduce various similarity measures for matching those semantic representations. We consider all possible combinations of semantic representations and similarity measures and use these as features in a supervised learning model. Using two purpose-built test collections based on Wikipedia tables, we demonstrate significant and substantial improvements over state-of-the-art baselines.»
[_citation_number]: «13»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2202.06991)\]. Further details \[[6](http://arxiv.org/abs/2005.09207)\]\[[7](http://arxiv.org/abs/2212.09744)\]\[[8](http://arxiv.org/abs/2004.12832)\]\[[9](http://arxiv.org/abs/1802.06159)\]\[[10](https://www.semanticscholar.org/paper/373588873bef360e3ecad2e091ac17895eb863af)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2202.06991)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2206.02743)\]\[[7](http://arxiv.org/abs/2212.09744)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The category of Query-Table Interaction and Semantic Alignment focuses on the challenges and advancements in retrieving tables based on natural language queries. This area addresses the problem of ad hoc table retrieval, where the goal is to answer a keyword query with a ranked list of relevant tables \[[9](http://arxiv.org/abs/1802.06159)\]. The task is critical for various applications, including table completion and table mining, as it enables efficient access to structured data \[[9](http://arxiv.org/abs/1802.06159)\]. A key challenge lies in achieving effective semantic alignment between queries and tables, which is essential for accurate retrieval \[[13](http://arxiv.org/abs/2105.06365)\]. To tackle this, recent approaches have explored semantic matching by representing queries and tables in multiple semantic spaces, such as discrete sparse and continuous dense vector representations \[[9](http://arxiv.org/abs/1802.06159)\]. These representations are then compared using various similarity measures to determine relevance \[[9](http://arxiv.org/abs/1802.06159)\]. Additionally, the work investigates different variants of the problem, including keyword-based queries and query-by-table scenarios, where an existing table serves as the query \[[13](http://arxiv.org/abs/2105.06365)\]. The main contribution of these studies is the development of a semantic table retrieval framework that integrates multiple semantic representations and similarity measures into a supervised learning model, leading to significant improvements over existing baselines \[[13](http://arxiv.org/abs/2105.06365)\].
|    | reference                                                                                   | date     | key idea/summary                                                                                                                                                                                                                                                                |
|----|---------------------------------------------------------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Ad Hoc Table Retrieval using Semantic Similarity](http://arxiv.org/abs/1802.06159)         | 02/16/18 | The paper introduces a method for semantic matching between keyword queries and tables, using multiple semantic representations and similarity measures to improve table retrieval performance.                                                                                 |
|  1 | [Semantic Table Retrieval using Keyword and Table Queries](http://arxiv.org/abs/2105.06365) | 05/13/21 | This work presents a semantic table retrieval framework that improves the matching of information needs, whether keyword-based or table-based, against structured web tables by using multiple semantic representations and similarity measures in a supervised learning model. |
