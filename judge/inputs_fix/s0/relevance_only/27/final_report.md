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
## Research papers
### Outline
- [Semantic Table Retrieval with Multiple Spaces [3 papers]](#category-semantic-table-retrieval-with-multiple-spaces)
- [Multi-Task Distillation for Retrieval Quality [1 papers]](#category-multi-task-distillation-for-retrieval-quality)
- [Benchmark Datasets for NL-Driven Table Discovery [2 papers]](#category-benchmark-datasets-for-nl-driven-table-discovery)
- [Differentiable Search Index Frameworks [5 papers]](#category-differentiable-search-index-frameworks)
- [Query Generation for Indexing [1 papers]](#category-query-generation-for-indexing)
- [Query-Table Semantic Alignment [2 papers]](#category-query-table-semantic-alignment)
- [Catastrophic Forgetting Mitigation Techniques [1 papers]](#category-catastrophic-forgetting-mitigation-techniques)

### <a id='category-semantic-table-retrieval-with-multiple-spaces'></a>Semantic Table Retrieval with Multiple Spaces: 3 papers found.
Context: 
	Document 1: [Category]: «Semantic Table Retrieval with Multiple Spaces»
[Snippet]: «Pretrained contextualized language models such as BERT have achieved impressive results on various natural language processing benchmarks. Benefiting from multiple pretraining tasks and large scale training corpora, pretrained models can capture complex syntactic word relations. In this paper, we use the deep contextualized language model BERT for the task of ad hoc table retrieval. We investigate how to encode table content considering the table structure and input length limit of BERT. We also propose an approach that incorporates features from prior literature on table retrieval and jointly trains them with BERT. In experiments on public datasets, we show that our best approach can outperform the previous state-of-the-art method and BERT baselines with a large margin under different evaluation metrics.»
[_citation_number]: «1»

	Document 2: [Category]: «Semantic Table Retrieval with Multiple Spaces»
[Snippet]: «Tables on the Web contain a vast amount of knowledge in a structured form. To tap into this valuable resource, we address the problem of table retrieval: answering an information need with a ranked list of tables. We investigate this problem in two different variants, based on how the information need is expressed: as a keyword query or as an existing table ("query-by-table"). The main novel contribution of this work is a semantic table retrieval framework for matching information needs (keyword or table queries) against tables. Specifically, we (i) represent queries and tables in multiple semantic spaces (both discrete sparse and continuous dense vector representations) and (ii) introduce various similarity measures for matching those semantic representations. We consider all possible combinations of semantic representations and similarity measures and use these as features in a supervised learning model. Using two purpose-built test collections based on Wikipedia tables, we demonstrate significant and substantial improvements over state-of-the-art baselines.»
[_citation_number]: «14»

	Document 3: [Category]: «Semantic Table Retrieval with Multiple Spaces»
[Snippet]: «We introduce and address the problem of ad hoc table retrieval: answering a keyword query with a ranked list of tables. This task is not only interesting on its own account, but is also being used as a core component in many other table-based information access scenarios, such as table completion or table mining. The main novel contribution of this work is a method for performing semantic matching between queries and tables. Specifically, we (i) represent queries and tables in multiple semantic spaces (both discrete sparse and continuous dense vector representations) and (ii) introduce various similarity measures for matching those semantic representations. We consider all possible combinations of semantic representations and similarity measures and use these as features in a supervised learning model. Using a purpose-built test collection based on Wikipedia tables, we demonstrate significant and substantial improvements over a state-of-the-art baseline.»
[_citation_number]: «15»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2504.15849)\]. Further details \[[6](http://arxiv.org/abs/2404.12237)\]\[[7](http://arxiv.org/abs/2307.10323)\]\[[8](http://arxiv.org/abs/2502.02788)\]\[[9](http://arxiv.org/abs/1512.00965)\]\[[10](http://arxiv.org/abs/2209.09207)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2504.15849)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2305.02073)\]\[[7](http://arxiv.org/abs/2307.10323)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The semantic table retrieval task, which involves matching information needs against tables, has been extensively studied with a focus on improving semantic alignment and representation. Prior work has explored the use of multiple semantic spaces, including both discrete sparse and continuous dense vector representations, to better capture the meaning of queries and tables \[[14](http://arxiv.org/abs/2105.06365)\]. These representations are often combined with various similarity measures to enhance retrieval accuracy \[[15](http://arxiv.org/abs/1802.06159)\]. Additionally, the integration of pretrained models like BERT has shown promise in capturing complex syntactic relationships and improving retrieval performance \[[1](http://arxiv.org/abs/2005.09207)\]. However, traditional methods often suffer from error accumulation during representation and indexing, as well as limited query-table interaction, which hinders semantic alignment \[[1](http://arxiv.org/abs/2005.09207)\]. Recent approaches have attempted to address these challenges by proposing novel frameworks that unify indexing and search processes, enabling more effective and accurate retrieval.
|    | reference                                                                                   | date     | key idea/summary                                                                                                                                                                                                                                                                |
|----|---------------------------------------------------------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Table Search Using a Deep Contextualized Language Model](http://arxiv.org/abs/2005.09207)  | 05/19/20 | The paper proposes an approach that enhances ad hoc table retrieval by leveraging the BERT model with structured table encoding and joint training of features from prior literature, achieving significant performance improvements over existing methods.                     |
|  1 | [Semantic Table Retrieval using Keyword and Table Queries](http://arxiv.org/abs/2105.06365) | 05/13/21 | This work presents a semantic table retrieval framework that improves the matching of information needs, whether keyword-based or table-based, against structured web tables by using multiple semantic representations and similarity measures in a supervised learning model. |
|  2 | [Ad Hoc Table Retrieval using Semantic Similarity](http://arxiv.org/abs/1802.06159)         | 02/16/18 | The paper introduces a method for semantic matching between keyword queries and tables, using multiple semantic representations and similarity measures to improve table retrieval performance.                                                                                 |
### <a id='category-multi-task-distillation-for-retrieval-quality'></a>Multi-Task Distillation for Retrieval Quality: 1 papers found.
Context: 
	Document 1: [Category]: «Multi-Task Distillation for Retrieval Quality»
[Snippet]: «The Differentiable Search Index (DSI) is a novel information retrieval (IR) framework that utilizes a differentiable function to generate a sorted list of document identifiers in response to a given query. However, due to the black-box nature of the end-to-end neural architecture, it remains to be understood to what extent DSI possesses the basic indexing and retrieval abilities. To mitigate this gap, in this study, we define and examine three important abilities that a functioning IR framework should possess, namely, exclusivity, completeness, and relevance ordering. Our analytical experimentation shows that while DSI demonstrates proficiency in memorizing the unidirectional mapping from pseudo queries to document identifiers, it falls short in distinguishing relevant documents from random ones, thereby negatively impacting its retrieval effectiveness. To address this issue, we propose a multi-task distillation approach to enhance the retrieval quality without altering the structure of the model and successfully endow it with improved indexing abilities. Through experiments conducted on various datasets, we demonstrate that our proposed method outperforms previous DSI baselines.»
[_citation_number]: «2»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2504.15849)\]. Further details \[[6](http://arxiv.org/abs/2404.12237)\]\[[7](http://arxiv.org/abs/2307.10323)\]\[[8](http://arxiv.org/abs/2502.02788)\]\[[9](http://arxiv.org/abs/1512.00965)\]\[[10](http://arxiv.org/abs/2209.09207)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2504.15849)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2305.02073)\]\[[7](http://arxiv.org/abs/2307.10323)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
The Differentiable Search Index (DSI) represents a significant advancement in information retrieval (IR) by integrating differentiable functions to generate document identifiers based on queries \[[2](http://arxiv.org/abs/2305.02073)\]. This framework aims to unify indexing and retrieval processes, reducing error accumulation that typically occurs in traditional pipelines \[[2](http://arxiv.org/abs/2305.02073)\]. However, the black-box nature of DSI poses challenges in assessing its indexing and retrieval capabilities, prompting researchers to evaluate fundamental IR properties such as exclusivity, completeness, and relevance ordering \[[2](http://arxiv.org/abs/2305.02073)\]. While DSI excels in memorizing mappings from pseudo queries to document identifiers, it struggles with distinguishing relevant documents from irrelevant ones, which limits its retrieval effectiveness \[[2](http://arxiv.org/abs/2305.02073)\]. To address these limitations, a multi-task distillation approach has been proposed to enhance retrieval quality without altering the model structure \[[2](http://arxiv.org/abs/2305.02073)\]. This method demonstrates improved indexing abilities and outperforms previous DSI baselines across various datasets \[[2](http://arxiv.org/abs/2305.02073)\].
|    | reference                                                                                     | date     | key idea/summary                                                                                                                                                                                                                                                                                             |
|----|-----------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Understanding Differential Search Index for Text Retrieval](http://arxiv.org/abs/2305.02073) | 05/03/23 | The Differentiable Search Index (DSI) is a novel information retrieval framework that, while effective in memorizing query-document mappings, lacks in distinguishing relevant documents from random ones, and the study proposes a multi-task distillation approach to enhance its retrieval effectiveness. |
### <a id='category-benchmark-datasets-for-nl-driven-table-discovery'></a>Benchmark Datasets for NL-Driven Table Discovery: 2 papers found.
Context: 
	Document 1: [Category]: «Benchmark Datasets for NL-Driven Table Discovery»
[Snippet]: «With the growing abundance of repositories containing tabular data, discovering relevant tables for in-depth analysis remains a challenging task. Existing table discovery methods primarily retrieve desired tables based on a query table or several vague keywords, leaving users to manually filter large result sets. To address this limitation, we propose a new task: NL-conditional table discovery (nlcTD), where users combine a query table with natural language (NL) requirements to refine search results. To advance research in this area, we present nlcTables, a comprehensive benchmark dataset comprising 627 diverse queries spanning NL-only, union, join, and fuzzy conditions, 22,080 candidate tables, and 21,200 relevance annotations. Our evaluation of six state-of-the-art table discovery methods on nlcTables reveals substantial performance gaps, highlighting the need for advanced techniques to tackle this challenging nlcTD scenario. The dataset, construction framework, and baseline implementations are publicly available at https://github.com/SuDIS-ZJU/nlcTables to foster future research.»
[_citation_number]: «3»

	Document 2: [Category]: «Benchmark Datasets for NL-Driven Table Discovery»
[Snippet]: «Recent deep learning approaches in table detection achieved outstanding performance and proved to be effective in identifying document layouts. Currently, available table detection benchmarks have many limitations, including the lack of samples diversity, simple table structure, the lack of training cases, and samples quality. In this paper, we introduce a diverse large-scale dataset for table detection with more than seven thousand samples containing a wide variety of table structures collected from many diverse sources. In addition to that, we also present baseline results using a convolutional neural network-based method to detect table structure in documents. Experimental results show the superiority of applying convolutional deep learning methods over classical computer vision-based methods. The introduction of this diverse table detection dataset will enable the community to develop high throughput deep learning methods for understanding document layout and tabular data processing. Dataset is available at: 1. https://www.kaggle.com/datasets/mrinalim/stdw-dataset 2. https://huggingface.co/datasets/n3011/STDW»
[_citation_number]: «10»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2504.15849)\]. Further details \[[6](http://arxiv.org/abs/2404.12237)\]\[[7](http://arxiv.org/abs/2307.10323)\]\[[8](http://arxiv.org/abs/2502.02788)\]\[[9](http://arxiv.org/abs/1512.00965)\]\[[10](http://arxiv.org/abs/2209.09207)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2504.15849)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2305.02073)\]\[[7](http://arxiv.org/abs/2307.10323)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The field of NL-driven table discovery has seen significant advancements, particularly with the introduction of benchmark datasets designed to address the challenges of retrieving relevant tables from large repositories. These datasets aim to improve the accuracy and efficiency of table discovery by incorporating natural language (NL) queries and complex conditions. For instance, the nlcTables dataset \[[3](http://arxiv.org/abs/2504.15849)\] introduces a comprehensive benchmark with 627 diverse queries, covering NL-only, union, join, and fuzzy conditions, alongside 22,280 candidate tables and 21,200 relevance annotations. This dataset highlights the need for more sophisticated methods that can handle the nuances of NL queries and reduce the manual filtering burden on users. Similarly, the STDW dataset \[[10](http://arxiv.org/abs/2209.09207)\] provides a large-scale, diverse collection of over 7,000 table samples with varied structures, addressing limitations in existing benchmarks such as lack of diversity and poor sample quality. These datasets are crucial for evaluating and improving deep learning methods, which have shown promise in table detection but still face challenges in semantic alignment and error accumulation during representation and indexing \[[3](http://arxiv.org/abs/2504.15849)\]. The availability of such benchmarks, along with baseline implementations and evaluation frameworks, fosters further research into advanced techniques for NL-driven table discovery.
|    | reference                                                                                                             | date     | key idea/summary                                                                                                                                                                                                                                                       |
|----|-----------------------------------------------------------------------------------------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [nlcTables: A Dataset for Marrying Natural Language Conditions with Table Discovery](http://arxiv.org/abs/2504.15849) | 04/22/25 | The paper introduces NL-conditional table discovery (nlcTD) and presents nlcTables, a benchmark dataset to evaluate table discovery methods that combine natural language requirements with query tables.                                                              |
|  1 | [Table Detection in the Wild: A Novel Diverse Table Detection Dataset and Method](http://arxiv.org/abs/2209.09207)    | 08/31/22 | This paper introduces a diverse large-scale table detection dataset with over 7,000 samples and presents baseline results using a convolutional neural network-based method, demonstrating the superiority of deep learning over classical computer vision approaches. |
### <a id='category-differentiable-search-index-frameworks'></a>Differentiable Search Index Frameworks: 5 papers found.
Differentiable Search Index (DSI) frameworks have emerged as a novel paradigm for document retrieval, integrating indexing and search into a unified neural model \[[4](http://arxiv.org/abs/2305.15115)\]. These models encode document identifiers and semantic associations directly into their parameters, enabling direct query-to-document mapping without traditional index-retrieval pipelines \[[6](http://arxiv.org/abs/2404.12237)\]. Recent works such as SE-DSI \[[4](http://arxiv.org/abs/2305.15115)\] and De-DSI \[[6](http://arxiv.org/abs/2404.12237)\] have advanced this approach by incorporating cognitive psychology-inspired strategies, such as elaborative descriptions for document identifiers and rehearsal strategies for semantic feature selection. Additionally, IncDSI \[[7](http://arxiv.org/abs/2307.10323)\] addresses the challenge of incremental updates, allowing real-time addition of new documents with minimal parameter changes, while DSI variants like the one proposed in \[[8](http://arxiv.org/abs/2502.02788)\] focus on balancing relevance and diversity during training. These frameworks also demonstrate scalability and efficiency, with De-DSI employing ensemble models and beam search for decentralized retrieval \[[6](http://arxiv.org/abs/2404.12237)\]. Furthermore, learned static indexes \[[12](http://arxiv.org/abs/2107.09480)\] explore space-time trade-offs, offering insights into optimizing search performance with minimal additional space. These developments highlight the growing interest in DSI as a flexible and powerful alternative to traditional retrieval systems.
|    | reference                                                                                                        | date     | key idea/summary                                                                                                                                                                                                                                    |
|----|------------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Semantic-Enhanced Differentiable Search Index Inspired by Learning Strategies](http://arxiv.org/abs/2305.15115) | 05/24/23 | The Semantic-Enhanced DSI model (SE-DSI) improves document retrieval by incorporating cognitive psychology-inspired strategies, using elaborative descriptions and semantic features to enhance document memorization and retrieval performance.    |
|  1 | [De-DSI: Decentralised Differentiable Search Index](http://arxiv.org/abs/2404.12237)                             | 04/18/24 | De-DSI is a decentralized framework that combines large language models with a differentiable search index to efficiently retrieve documents using query-docid pairs, enabling scalability and multimedia retrieval without direct document access. |
|  2 | [IncDSI: Incrementally Updatable Document Retrieval](http://arxiv.org/abs/2307.10323)                            | 07/19/23 | IncDSI is a method that allows real-time addition of new documents to a Differentiable Search Index without retraining the model, enabling dynamic updates to document retrieval systems.                                                           |
|  3 | [Inducing Diversity in Differentiable Search Indexing](http://arxiv.org/abs/2502.02788)                          | 02/05/25 | Differentiable Search Indexing (DSI) is enhanced by balancing relevance and diversity during training, achieving both without significant relevance loss and eliminating the need for post-processing diversity steps.                              |
|  4 | [Learned Sorted Table Search and Static Indexes in Small Model Space](http://arxiv.org/abs/2107.09480)           | 07/19/21 | This paper introduces new machine learning models for learned indexes that improve binary search speed with minimal additional space, demonstrating efficient time-space trade-offs.                                                                |
### <a id='category-query-generation-for-indexing'></a>Query Generation for Indexing: 1 papers found.
Context: 
	Document 1: [Category]: «Query Generation for Indexing»
[Snippet]: «The Differentiable Search Index (DSI) is an emerging paradigm for information retrieval. Unlike traditional retrieval architectures where index and retrieval are two different and separate components, DSI uses a single transformer model to perform both indexing and retrieval. In this paper, we identify and tackle an important issue of current DSI models: the data distribution mismatch that occurs between the DSI indexing and retrieval processes. Specifically, we argue that, at indexing, current DSI methods learn to build connections between the text of long documents and the identifier of the documents, but then retrieval of document identifiers is based on queries that are commonly much shorter than the indexed documents. This problem is further exacerbated when using DSI for cross-lingual retrieval, where document text and query text are in different languages. To address this fundamental problem of current DSI models, we propose a simple yet effective indexing framework for DSI, called DSI-QG. When indexing, DSI-QG represents documents with a number of potentially relevant queries generated by a query generation model and re-ranked and filtered by a cross-encoder ranker. The presence of these queries at indexing allows the DSI models to connect a document identifier to a set of queries, hence mitigating data distribution mismatches present between the indexing and the retrieval phases. Empirical results on popular mono-lingual and cross-lingual passage retrieval datasets show that DSI-QG significantly outperforms the original DSI model.»
[_citation_number]: «5»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2504.15849)\]. Further details \[[6](http://arxiv.org/abs/2404.12237)\]\[[7](http://arxiv.org/abs/2307.10323)\]\[[8](http://arxiv.org/abs/2502.02788)\]\[[9](http://arxiv.org/abs/1512.00965)\]\[[10](http://arxiv.org/abs/2209.09207)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from
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
isolation, which mitigizes the issue of catastrophic forgetting. Extensive
experiments demonstrate that Birdie outperforms state-of-the-art dense methods
by 16.8% in accuracy, and reduces forgetting by over 90% compared to other
continual learning approaches.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2504.15849)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2305.02073)\]\[[7](http://arxiv.org/abs/2307.10323)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer:  
The Differentiable Search Index (DSI) represents a paradigm shift in information retrieval by integrating indexing and retrieval into a single transformer model, thereby eliminating the traditional separation between these components \[[5](http://arxiv.org/abs/2206.10128)\]. This approach addresses key limitations of conventional systems, such as the data distribution mismatch between indexing and retrieval phases, where indexed documents are typically longer than the queries used during retrieval \[[5](http://arxiv.org/abs/2206.10128)\]. This mismatch is particularly pronounced in cross-lingual retrieval scenarios, where document and query texts are in different languages \[[5](http://arxiv.org/abs/2206.10128)\]. To mitigate these issues, the DSI-QG framework was introduced, which generates potentially relevant queries during the indexing phase using a query generation model, followed by re-ranking and filtering via a cross-encoder ranker \[[5](http://arxiv.org/abs/2206.10128)\]. By incorporating these queries into the indexing process, DSI-QG enables the model to better align with the query distribution during retrieval, thus improving retrieval performance \[[5](http://arxiv.org/abs/2206.10128)\]. Empirical evaluations on both mono-lingual and cross-lingual datasets have demonstrated that DSI-QG significantly outperforms the original DSI model, highlighting its effectiveness in addressing the fundamental challenges of DSI systems \[[5](http://arxiv.org/abs/2206.10128)\].
|    | reference                                                                                                                                | date     | key idea/summary                                                                                                                                                                                                  |
|----|------------------------------------------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Bridging the Gap Between Indexing and Retrieval for Differentiable Search Index with Query Generation](http://arxiv.org/abs/2206.10128) | 06/21/22 | DSI-QG is a novel indexing framework for Differentiable Search Index (DSI) that addresses data distribution mismatches by generating and using relevant queries during indexing to improve retrieval performance. |
### <a id='category-query-table-semantic-alignment'></a>Query-Table Semantic Alignment: 2 papers found.
Context: 
	Document 1: [Category]: «Query-Table Semantic Alignment»
[Snippet]: «We proposed Neural Enquirer as a neural network architecture to execute a natural language (NL) query on a knowledge-base (KB) for answers. Basically, Neural Enquirer finds the distributed representation of a query and then executes it on knowledge-base tables to obtain the answer as one of the values in the tables. Unlike similar efforts in end-to-end training of semantic parsers, Neural Enquirer is fully "neuralized": it not only gives distributional representation of the query and the knowledge-base, but also realizes the execution of compositional queries as a series of differentiable operations, with intermediate results (consisting of annotations of the tables at different levels) saved on multiple layers of memory. Neural Enquirer can be trained with gradient descent, with which not only the parameters of the controlling components and semantic parsing component, but also the embeddings of the tables and query words can be learned from scratch. The training can be done in an end-to-end fashion, but it can take stronger guidance, e.g., the step-by-step supervision for complicated queries, and benefit from it. Neural Enquirer is one step towards building neural network systems which seek to understand language by executing it on real-world. Our experiments show that Neural Enquirer can learn to execute fairly complicated NL queries on tables with rich structures.»
[_citation_number]: «9»

	Document 2: [Category]: «Query-Table Semantic Alignment»
[Snippet]: «Database systems have to cater to the growing demands of the information age. The growth of the new age information retrieval powerhouses like search engines has thrown a challenge to the data management community to come up with novel mechanisms for feeding information to end users. The burgeoning use of natural language query interfaces compels system designers to present meaningful and customised information. Conventional query languages like SQL do not cater to these requirements due to syntax oriented design. Providing a semantic cover over these systems was the aim of latent table discovery focusing on semantically connecting unrelated tables that were not syntactically related by design and document the discovered knowledge. This paper throws a new direction towards improving the semantic capabilities of database systems by introducing a concept driven framework over the latent table discovery method.»
[_citation_number]: «11»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2504.15849)\]. Further details \[[6](http://arxiv.org/abs/2404.12237)\]\[[7](http://arxiv.org/abs/2307.10323)\]\[[8](http://arxiv.org/abs/2502.02788)\]\[[9](http://arxiv.org/abs/1512.00965)\]\[[10](http://arxiv.org/abs/2209.09207)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2504.15849)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2305.02073)\]\[[7](http://arxiv.org/abs/2307.10323)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The category of Query-Table Semantic Alignment focuses on improving the alignment between natural language queries and structured data tables, enabling more accurate and semantically meaningful interactions. Existing approaches often rely on traditional dense vector search pipelines, which suffer from error accumulation during representation and indexing, as well as limited query-table interaction that hinders semantic alignment \[[9](http://arxiv.org/abs/1512.00965)\]. To address these challenges, researchers have proposed frameworks that integrate neural architectures for both indexing and search, allowing for end-to-end learning and better alignment \[[11](http://arxiv.org/abs/1208.4016)\]. For instance, Neural Enquirer employs a neural network to generate distributed representations of queries and execute them on knowledge-base tables, achieving compositional query execution through differentiable operations \[[9](http://arxiv.org/abs/1512.00965)\]. Similarly, recent work emphasizes the need for concept-driven frameworks that enhance semantic connections between unrelated tables, moving beyond syntactic alignment \[[11](http://arxiv.org/abs/1208.4016)\]. These efforts highlight the growing interest in developing more robust and flexible systems for natural language-driven table discovery and query execution.
|    | reference                                                                             | date     | key idea/summary                                                                                                                                                                                                                                                      |
|----|---------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Neural Enquirer: Learning to Query Tables](http://arxiv.org/abs/1512.00965)          | 12/03/15 | Neural Enquirer is a neural network architecture that executes natural language queries on knowledge-base tables by using distributed representations and differentiable operations, enabling end-to-end training with gradient descent and step-by-step supervision. |
|  1 | [Concept driven framework for Latent Table Discovery](http://arxiv.org/abs/1208.4016) | 08/20/12 | This paper introduces a concept-driven framework to enhance the semantic capabilities of database systems by improving upon latent table discovery methods.                                                                                                           |
### <a id='category-catastrophic-forgetting-mitigation-techniques'></a>Catastrophic Forgetting Mitigation Techniques: 1 papers found.
Context: 
	Document 1: [Category]: «Catastrophic Forgetting Mitigation Techniques»
[Snippet]: «Differentiable Search Indices (DSIs) encode a corpus of documents in model parameters and use the same model to answer user queries directly. Despite the strong performance of DSI models, deploying them in situations where the corpus changes over time is computationally expensive because reindexing the corpus requires re-training the model. In this work, we introduce DSI++, a continual learning challenge for DSI to incrementally index new documents while being able to answer queries related to both previously and newly indexed documents. Across different model scales and document identifier representations, we show that continual indexing of new documents leads to considerable forgetting of previously indexed documents. We also hypothesize and verify that the model experiences forgetting events during training, leading to unstable learning. To mitigate these issues, we investigate two approaches. The first focuses on modifying the training dynamics. Flatter minima implicitly alleviate forgetting, so we optimize for flatter loss basins and show that the model stably memorizes more documents ($+12\%$). Next, we introduce a generative memory to sample pseudo-queries for documents and supplement them during continual indexing to prevent forgetting for the retrieval task. Extensive experiments on novel continual indexing benchmarks based on Natural Questions (NQ) and MS MARCO demonstrate that our proposed solution mitigates forgetting significantly. Concretely, it improves the average Hits@10 by $+21.1\%$ over competitive baselines for NQ and requires $6$ times fewer model updates compared to re-training the DSI model for incrementally indexing five corpora in a sequence.»
[_citation_number]: «13»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-30T03:30:21+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2504.15849)\]. Further details \[[6](http://arxiv.org/abs/2404.12237)\]\[[7](http://arxiv.org/abs/2307.10323)\]\[[8](http://arxiv.org/abs/2502.02788)\]\[[9](http://arxiv.org/abs/1512.00965)\]\[[10](http://arxiv.org/abs/2209.09207)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Natural language (NL)-driven table discovery identifies relevant tables from
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2504.15849)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2305.02073)\]\[[7](http://arxiv.org/abs/2307.10323)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The mitigation of catastrophic forgetting in continual learning has been a critical area of research, particularly in the context of differentiable search indices (DSIs). DSIs encode a corpus of documents directly into model parameters and use the same model to answer queries, but they face challenges when the corpus evolves over time, as reindexing requires full retraining and leads to significant forgetting of previously indexed documents \[[13](http://arxiv.org/abs/2212.09744)\]. To address this, researchers have explored methods to optimize training dynamics, such as promoting flatter minima in the loss landscape, which helps stabilize learning and improve memorization of prior data \[[13](http://arxiv.org/abs/2212.09744)\]. Additionally, generative memory techniques have been introduced to simulate pseudo-queries for previously indexed documents, preventing forgetting during continual indexing \[[13](http://arxiv.org/abs/2212.09744)\]. These approaches demonstrate that mitigating forgetting is essential for maintaining performance in dynamic environments, as evidenced by improvements in retrieval accuracy and reduced computational overhead \[[13](http://arxiv.org/abs/2212.09744)\].
|    | reference                                                                                | date     | key idea/summary                                                                                                                                                                                                                                                                           |
|----|------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [DSI++: Updating Transformer Memory with New Documents](http://arxiv.org/abs/2212.09744) | 12/19/22 | DSI++ addresses the issue of forgetting in continual learning for differentiable search indices by introducing methods to optimize for flatter minima and using a generative memory to prevent forgetting, significantly improving retrieval performance and reducing computational costs. |
