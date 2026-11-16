## Related Works

Table discovery and semantic parsing have seen significant advancements in recent years, driven by the increasing availability of structured and tabular data. Early approaches primarily focused on retrieving tables based on queries or keywords, often resulting in large, unfiltered result sets that required manual filtering \[[6](http://arxiv.org/abs/1508.00305)\]. This limitation has motivated new research directions, including the introduction of natural language (NL)-conditional table discovery (nlcTD), where users combine a query table with NL requirements to refine search results \[[1](http://arxiv.org/abs/2005.08314)\]. The nlcTables dataset, introduced to address this challenge, includes 627 diverse queries and 22,080 candidate tables, providing a comprehensive benchmark for evaluating new methods \[[1](http://arxiv.org/abs/2005.08314)\].

Pretrained language models have also played a crucial role in improving semantic parsing and understanding of structured data. For instance, TaBERT was developed to jointly learn representations for natural language sentences and (semi-)structured tables, enabling better performance on tasks like semantic parsing and text-to-SQL \[[2](https://www.semanticscholar.org/paper/9d6931dd0ba9e492b0ceab00268ca4be62ef663a)\]. This model was trained on a large corpus of 26 million tables and their English contexts, leading to state-of-the-art results on the WikiTableQuestions benchmark \[[2](https://www.semanticscholar.org/paper/9d6931dd0ba9e492b0ceab00268ca4be62ef663a)\]. Similarly, the Unified Text-to-Text Transformer framework has demonstrated the effectiveness of transfer learning in NLP, achieving strong results across various tasks by converting them into a unified text-to-text format \[[5](http://arxiv.org/abs/1910.10683)\]. These models highlight the importance of leveraging both textual and tabular data for improved understanding and reasoning.

Semantic parsing over structured data has also been explored in the context of semi-structured tables. A notable work in this area is the introduction of a new task: answering complex questions on semi-structured tables using question-answer pairs as supervision \[[6](http://arxiv.org/abs/1508.00305)\]. This approach addresses the challenges of open-ended relations and combinatorial complexity in logical forms, achieving significant improvements over natural baselines \[[6](http://arxiv.org/abs/1508.00305)\]. The dataset created for this task includes 22,033 complex questions, offering a valuable resource for future research \[[6](http://arxiv.org/abs/1508.00305)\].

In addition, deep learning methods have been applied to the detection and structure recognition of tables in document images, further advancing the field of table processing \[[4](https://www.semanticscholar.org/paper/f8bead3ae810cd3f7427d3004e45b4158da9b744)\]. These methods typically involve convolutional neural networks and attention mechanisms to accurately identify and parse table structures from scanned documents \[[4](https://www.semanticscholar.org/paper/f8bead3ae810cd3f7427d3004e45b4158da9b744)\]. Such advancements underscore the growing interest in integrating deep learning techniques with traditional table processing tasks.

Overall, the recent developments in table discovery, semantic parsing, and deep learning for structured data highlight the need for more sophisticated models and benchmarks. The nlcTables dataset and related works provide a solid foundation for future research in
## Research papers
### Outline
- [Pretrained Language Models for Structured Data [1 papers]](#category-pretrained-language-models-for-structured-data)
- [Deep Learning for Table Detection [2 papers]](#category-deep-learning-for-table-detection)
- [Dataset Construction and Benchmarking [1 papers]](#category-dataset-construction-and-benchmarking)
- [Unified Text-to-Text Transformers [1 papers]](#category-unified-text-to-text-transformers)
- [Semi-Structured Table Question Answering [1 papers]](#category-semi-structured-table-question-answering)

### <a id='category-pretrained-language-models-for-structured-data'></a>Pretrained Language Models for Structured Data: 1 papers found.
Context: 
	Document 1: [Snippet]: «Recent years have witnessed the burgeoning of pretrained language models (LMs) for text-based natural language (NL) understanding tasks. Such models are typically trained on free-form NL text, hence may not be suitable for tasks like semantic parsing over structured data, which require reasoning over both free-form NL questions and structured tabular data (e.g., database tables). In this paper we present TaBERT, a pretrained LM that jointly learns representations for NL sentences and (semi-)structured tables. TaBERT is trained on a large corpus of 26 million tables and their English contexts. In experiments, neural semantic parsers using TaBERT as feature representation layers achieve new best results on the challenging weakly-supervised semantic parsing benchmark WikiTableQuestions, while performing competitively on the text-to-SQL dataset Spider.»
[_citation_number]: «1»
[Category]: «Pretrained Language Models for Structured Data»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-22T12:44:59+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](https://www.semanticscholar.org/paper/bff7592f28354b3be632f4bf678b622f765a2b8d)\]. Further details \[[6](http://arxiv.org/abs/1508.00305)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: With the growing abundance of repositories containing tabular data,
discovering relevant tables for in-depth analysis remains a challenging task.
Existing table discovery methods primarily retrieve desired tables based on a
query table or several vague keywords, leaving users to manually filter large
result sets. To address this limitation, we propose a new task: NL-conditional
table discovery (nlcTD), where users combine a query table with natural
language (NL) requirements to refine search results. To advance research in
this area, we present nlcTables, a comprehensive benchmark dataset comprising
627 diverse queries spanning NL-only, union, join,
|    | reference                                                                                                  | date     | key idea/summary                                                                                                                                                                              |
|----|------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [TaBERT: Pretraining for Joint Understanding of Textual and Tabular Data](http://arxiv.org/abs/2005.08314) | 05/01/20 | TaBERT is a pretrained language model that jointly learns representations for natural language sentences and structured tables, achieving state-of-the-art results in semantic parsing tasks. |
### <a id='category-deep-learning-for-table-detection'></a>Deep Learning for Table Detection: 2 papers found.
Context: 
	Document 1: [Snippet]: «»
[_citation_number]: «2»
[Category]: «Deep Learning for Table Detection»

	Document 2: [Snippet]: «»
[_citation_number]: «4»
[Category]: «Deep Learning for Table Detection»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-22T12:44:59+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](https://www.semanticscholar.org/paper/bff7592f28354b3be632f4bf678b622f765a2b8d)\]. Further details \[[6](http://arxiv.org/abs/1508.00305)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: With the growing abundance of repositories containing tabular data,
discovering relevant tables for in-depth analysis remains a challenging task.
Existing table discovery methods primarily retrieve desired tables based on a
query table or several vague keywords, leaving users to manually filter large
result sets. To address this limitation, we propose a new task: NL-conditional
table discovery (nlcTD), where users combine a query table with natural
language (NL) requirements to refine search results. To advance research in
this area, we present nlcTables, a comprehensive benchmark dataset comprising
627 diverse queries spanning NL-only, union, join, and fuzzy conditions, 22,080
candidate tables, and 21,200 relevance annotations. Our evaluation of six
state-of-the-art table discovery methods on nlcTables reveals substantial
performance gaps, highlighting the need for advanced techniques to tackle this
challenging nlcTD scenario. The dataset, construction framework, and baseline
implementations are publicly available at
https://github.com/SuDIS-ZJU/nlcTables to foster future research.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category,
|    | reference                                                                                                                                                                       | date     | key idea/summary                                                                                          |
|----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------|
|  0 | [Table Detection Using Deep Learning](https://www.semanticscholar.org/paper/9d6931dd0ba9e492b0ceab00268ca4be62ef663a)                                                           | 11/01/17 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
|  1 | [DeepDeSRT: Deep Learning for Detection and Structure Recognition of Tables in Document Images](https://www.semanticscholar.org/paper/f8bead3ae810cd3f7427d3004e45b4158da9b744) | 11/01/17 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
### <a id='category-dataset-construction-and-benchmarking'></a>Dataset Construction and Benchmarking: 1 papers found.
Context: 
	Document 1: [Snippet]: «»
[_citation_number]: «3»
[Category]: «Dataset Construction and Benchmarking»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-22T12:44:59+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](https://www.semanticscholar.org/paper/bff7592f28354b3be632f4bf678b622f765a2b8d)\]. Further details \[[6](http://arxiv.org/abs/1508.00305)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: With the growing abundance of repositories containing tabular data,
discovering relevant tables for in-depth analysis remains a challenging task.
Existing table discovery methods primarily retrieve desired tables based on a
query table or several vague keywords, leaving users to manually filter large
result sets. To address this limitation, we propose a new task: NL-conditional
table discovery (nlcTD), where users combine a query table with natural
language (NL) requirements to refine search results. To advance research in
this area, we present nlcTables, a comprehensive benchmark dataset comprising
627 diverse queries spanning NL-only, union, join, and fuzzy conditions, 22,080
candidate tables, and 21,200 relevance annotations. Our evaluation of six
state-of-the-art table discovery methods on nlcTables reveals substantial
performance gaps, highlighting the need for advanced techniques to tackle this
challenging nlcTD scenario. The dataset, construction framework, and baseline
implementations are publicly available at
https://github.com/SuDIS-ZJU/nlcTables to foster future research.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the
|    | reference                                                                                                                                                          | date     | key idea/summary                                                                                          |
|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------|
|  0 | [An open approach towards the benchmarking of table structure recognition systems](https://www.semanticscholar.org/paper/bff7592f28354b3be632f4bf678b622f765a2b8d) | 06/09/10 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
### <a id='category-unified-text-to-text-transformers'></a>Unified Text-to-Text Transformers: 1 papers found.
Context: 
	Document 1: [Snippet]: «Transfer learning, where a model is first pre-trained on a data-rich task before being fine-tuned on a downstream task, has emerged as a powerful technique in natural language processing (NLP). The effectiveness of transfer learning has given rise to a diversity of approaches, methodology, and practice. In this paper, we explore the landscape of transfer learning techniques for NLP by introducing a unified framework that converts every language problem into a text-to-text format. Our systematic study compares pre-training objectives, architectures, unlabeled datasets, transfer approaches, and other factors on dozens of language understanding tasks. By combining the insights from our exploration with scale and our new "Colossal Clean Crawled Corpus", we achieve state-of-the-art results on many benchmarks covering summarization, question answering, text classification, and more. To facilitate future work on transfer learning for NLP, we release our dataset, pre-trained models, and code.»
[_citation_number]: «5»
[Category]: «Unified Text-to-Text Transformers»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-22T12:44:59+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](https://www.semanticscholar.org/paper/bff7592f28354b3be632f4bf678b622f765a2b8d)\]. Further details \[[6](http://arxiv.org/abs/1508.00305)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: With the growing abundance of repositories containing tabular data,
discovering relevant tables for in-depth analysis remains a challenging task.
Existing table discovery methods primarily retrieve desired tables based on a
query table or several vague keywords, leaving users to manually filter large
result sets. To address this limitation, we propose a new task: NL-conditional
table discovery (nlcTD), where users combine a query table with natural
language (NL) requirements to refine search results. To advance research in
this area, we present n
|    | reference                                                                                                            | date     | key idea/summary                                                                                                                                                                                                         |
|----|----------------------------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](http://arxiv.org/abs/1910.10683) | 10/23/19 | This paper introduces a unified framework for transfer learning in NLP, converting language problems into text-to-text format, and achieves state-of-the-art results using a large-scale dataset and pre-trained models. |
### <a id='category-semi-structured-table-question-answering'></a>Semi-Structured Table Question Answering: 1 papers found.
Context: 
	Document 1: [Snippet]: «Two important aspects of semantic parsing for question answering are the breadth of the knowledge source and the depth of logical compositionality. While existing work trades off one aspect for another, this paper simultaneously makes progress on both fronts through a new task: answering complex questions on semi-structured tables using question-answer pairs as supervision. The central challenge arises from two compounding factors: the broader domain results in an open-ended set of relations, and the deeper compositionality results in a combinatorial explosion in the space of logical forms. We propose a logical-form driven parsing algorithm guided by strong typing constraints and show that it obtains significant improvements over natural baselines. For evaluation, we created a new dataset of 22,033 complex questions on Wikipedia tables, which is made publicly available.»
[_citation_number]: «6»
[Category]: «Semi-Structured Table Question Answering»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-22T12:44:59+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](https://www.semanticscholar.org/paper/bff7592f28354b3be632f4bf678b622f765a2b8d)\]. Further details \[[6](http://arxiv.org/abs/1508.00305)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: With the growing abundance of repositories containing tabular data,
discovering relevant tables for in-depth analysis remains a challenging task.
Existing table discovery methods primarily retrieve desired tables based on a
query table or several vague keywords, leaving users to manually filter large
result sets. To address this limitation, we propose a new task: NL-conditional
table discovery (nlcTD), where users combine a query table with natural
language (NL) requirements to refine search results. To advance research in
this area, we present nlcTables, a comprehensive benchmark dataset comprising
627 diverse queries spanning NL-only, union, join, and fuzzy conditions
|    | reference                                                                                   | date     | key idea/summary                                                                                                                                                                                                                                                                     |
|----|---------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Compositional Semantic Parsing on Semi-Structured Tables](http://arxiv.org/abs/1508.00305) | 08/03/15 | This paper addresses the challenges of semantic parsing by proposing a logical-form driven parsing algorithm that improves both the breadth of knowledge sources and the depth of logical compositionality through a new task involving complex questions on semi-structured tables. |
