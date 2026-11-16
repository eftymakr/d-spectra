## Related Works

Table discovery and semantic parsing over structured data have seen significant advancements in recent years. Early approaches focused on retrieving tables based on keyword matching or query tables, often requiring manual filtering of results \[[1](http://arxiv.org/abs/1508.00305)\]. This limitation has motivated the development of more sophisticated methods that integrate natural language (NL) requirements into the search process. The proposed task of NL-conditional table discovery (nlcTD) builds upon these efforts by combining a query table with NL conditions to refine search results \[[1](http://arxiv.org/abs/1508.00305)\].

Semantic parsing over semi-structured tables has been a key area of research, with a focus on improving both the breadth of knowledge sources and the depth of logical compositionality \[[2](http://arxiv.org/abs/2005.08314)\]. This work introduced a new task of answering complex questions on Wikipedia tables using question-answer pairs as supervision, leading to the creation of a large-scale dataset of 22,0033 questions \[[2](http://arxiv.org/abs/2005.08314)\]. The challenge of handling open-ended relations and combinatorial logical forms has been addressed through logical-form driven parsing algorithms guided by strong typing constraints \[[2](http://arxiv.org/abs/2005.08314)\].

Recent work has also explored pretrained language models for joint understanding of textual and tabular data. TaBERT, a pretrained model trained on 26 million tables and their English contexts, has shown competitive performance on semantic parsing benchmarks like WikiTableQuestions and text-to-SQL datasets like Spider \[[3](https://www.semanticscholar.org/paper/bff7592f28354b3be632f4bf678b622f765a2b8d)\]. This model is particularly suited for tasks requiring reasoning over both free-form NL questions and structured tabular data \[[3](https://www.semanticscholar.org/paper/bff7592f28354b3be632f4bf678b622f765a2b8d)\].

In the realm of table detection and recognition, TableBank has emerged as a valuable benchmark dataset. It contains 417K high-quality labeled tables and is built using novel weak supervision from Word and LaTeX documents \[[4](https://www.semanticscholar.org/paper/9f7a62139dfd09bfad667691332bd55e31736887)\]. This dataset enables the development of strong baselines using state-of-the-art models, addressing the challenge of generalization on real-world applications \[[4](https://www.semanticscholar.org/paper/9f7a62139dfd09bfad667691332bd55e31736887)\].

The nlcTables dataset presented in this paper extends the scope of table discovery by incorporating diverse NL conditions, including NL-only, union, join, and fuzzy conditions \[[1](http://arxiv.org/abs/1508.00305)\]. It includes 627 queries, 22,080 candidate tables, and 21,200 relevance annotations, providing a comprehensive benchmark for evaluating advanced techniques in nlcTD. The evaluation of six state-of-the-art methods on nlcTables reveals substantial performance gaps, underscoring the need for further research \[[1](http://arxiv.org/abs/1508.00305)\].

These works collectively highlight the growing interest in integrating NL understanding with structured data processing, paving the way for more effective and user-friendly table discovery systems. The proposed nlcTD task and nlcTables dataset represent a significant
## Research papers
### Outline
- [Semantic Parsing Over Semi-Structured Tables [1 papers]](#category-semantic-parsing-over-semi-structured-tables)
- [Pretrained Language Models for Text-Table Understanding [1 papers]](#category-pretrained-language-models-for-text-table-understanding)
- [Table Detection and Recognition Benchmarks [2 papers]](#category-table-detection-and-recognition-benchmarks)
- [Weakly Supervised Dataset Construction Techniques [1 papers]](#category-weakly-supervised-dataset-construction-techniques)

### <a id='category-semantic-parsing-over-semi-structured-tables'></a>Semantic Parsing Over Semi-Structured Tables: 1 papers found.
Context: 
	Document 1: [Category]: «Semantic Parsing Over Semi-Structured Tables»
[Snippet]: «Two important aspects of semantic parsing for question answering are the breadth of the knowledge source and the depth of logical compositionality. While existing work trades off one aspect for another, this paper simultaneously makes progress on both fronts through a new task: answering complex questions on semi-structured tables using question-answer pairs as supervision. The central challenge arises from two compounding factors: the broader domain results in an open-ended set of relations, and the deeper compositionality results in a combinatorial explosion in the space of logical forms. We propose a logical-form driven parsing algorithm guided by strong typing constraints and show that it obtains significant improvements over natural baselines. For evaluation, we created a new dataset of 22,033 complex questions on Wikipedia tables, which is made publicly available.»
[_citation_number]: «1»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-22T12:44:59+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](https://www.semanticscholar.org/paper/bff7592f28354b3be632f4bf678b622f765a2b8d)\]. Further details .) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: With the growing abundance of repositories containing tabular data, discovering relevant tables for in-depth analysis remains a challenging task. Existing table discovery methods primarily retrieve desired tables based on a query table or several vague keywords, leaving users to manually filter large result sets. To address this limitation, we propose a new task: NL-conditional table discovery (nlcTD), where users combine a query table with natural language (NL) requirements to refine search results. To advance research in this area, we present nlcTables, a comprehensive benchmark dataset comprising 627 diverse queries spanning NL-only, union, join, and fuzzy conditions, 22,080
|    | reference                                                                                   | date     | key idea/summary                                                                                                                                                                                                                                                                     |
|----|---------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Compositional Semantic Parsing on Semi-Structured Tables](http://arxiv.org/abs/1508.00305) | 08/03/15 | This paper addresses the challenges of semantic parsing by proposing a logical-form driven parsing algorithm that improves both the breadth of knowledge sources and the depth of logical compositionality through a new task involving complex questions on semi-structured tables. |
### <a id='category-pretrained-language-models-for-text-table-understanding'></a>Pretrained Language Models for Text-Table Understanding: 1 papers found.
Context: 
	Document 1: [Category]: «Pretrained Language Models for Text-Table Understanding»
[Snippet]: «Recent years have witnessed the burgeoning of pretrained language models (LMs) for text-based natural language (NL) understanding tasks. Such models are typically trained on free-form NL text, hence may not be suitable for tasks like semantic parsing over structured data, which require reasoning over both free-form NL questions and structured tabular data (e.g., database tables). In this paper we present TaBERT, a pretrained LM that jointly learns representations for NL sentences and (semi-)structured tables. TaBERT is trained on a large corpus of 26 million tables and their English contexts. In experiments, neural semantic parsers using TaBERT as feature representation layers achieve new best results on the challenging weakly-supervised semantic parsing benchmark WikiTableQuestions, while performing competitively on the text-to-SQL dataset Spider.»
[_citation_number]: «2»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-22T12:44:59+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](https://www.semanticscholar.org/paper/bff7592f28354b3be632f4bf678b622f765a2b8d)\]. Further details .) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: With the growing abundance of repositories containing tabular data,
discovering relevant tables for in-depth analysis remains a challenging task.
Existing table discovery methods primarily retrieve desired tables based on a
query table or several vague keywords, leaving users to manually filter large
result sets. To address this limitation, we propose a new task: NL-conditional
table discovery (nlcTD), where users combine a query table with natural
language (NL) requirements to refine search results. To advance research in
this area, we present nlcTables, a comprehensive benchmark dataset comprising
627 diverse queries spanning NL-only, union, join, and
|    | reference                                                                                                  | date     | key idea/summary                                                                                                                                                                              |
|----|------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [TaBERT: Pretraining for Joint Understanding of Textual and Tabular Data](http://arxiv.org/abs/2005.08314) | 05/01/20 | TaBERT is a pretrained language model that jointly learns representations for natural language sentences and structured tables, achieving state-of-the-art results in semantic parsing tasks. |
### <a id='category-table-detection-and-recognition-benchmarks'></a>Table Detection and Recognition Benchmarks: 2 papers found.
Context: 
	Document 1: [Category]: «Table Detection and Recognition Benchmarks»
[Snippet]: «»
[_citation_number]: «3»

	Document 2: [Category]: «Table Detection and Recognition Benchmarks»
[Snippet]: «»
[_citation_number]: «4»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-22T12:44:59+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](https://www.semanticscholar.org/paper/bff7592f28354b3be632f4bf678b622f765a2b8d)\]. Further details .) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: With the growing abundance of repositories containing tabular data,
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
The paragraph should summarize the key themes that relate to the
|    | reference                                                                                                                                                          | date     | key idea/summary                                                                                          |
|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------|
|  0 | [An open approach towards the benchmarking of table structure recognition systems](https://www.semanticscholar.org/paper/bff7592f28354b3be632f4bf678b622f765a2b8d) | 06/09/10 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
|  1 | [Dataset, Ground-Truth and Performance Metrics for Table Detection Evaluation](https://www.semanticscholar.org/paper/9f7a62139dfd09bfad667691332bd55e31736887)     | 03/27/12 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
### <a id='category-weakly-supervised-dataset-construction-techniques'></a>Weakly Supervised Dataset Construction Techniques: 1 papers found.
Context: 
	Document 1: [Category]: «Weakly Supervised Dataset Construction Techniques»
[Snippet]: «We present TableBank, a new image-based table detection and recognition dataset built with novel weak supervision from Word and Latex documents on the internet. Existing research for image-based table detection and recognition usually fine-tunes pre-trained models on out-of-domain data with a few thousand human-labeled examples, which is difficult to generalize on real-world applications. With TableBank that contains 417K high quality labeled tables, we build several strong baselines using state-of-the-art models with deep neural networks. We make TableBank publicly available and hope it will empower more deep learning approaches in the table detection and recognition task. The dataset and models can be downloaded from https://github.com/doc-analysis/TableBank.»
[_citation_number]: «5»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-22T12:44:59+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](https://www.semanticscholar.org/paper/bff7592f28354b3be632f4bf678b622f765a2b8d)\]. Further details .) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: With the growing abundance of repositories containing tabular data,
discovering relevant tables for in-depth analysis remains a challenging task.
Existing table discovery methods primarily retrieve desired tables based on a
query table or several vague keywords, leaving users to manually filter large
result sets. To address this limitation, we propose a new task: NL-conditional
table discovery (nlcTD), where users combine a query table with natural
language (NL) requirements to refine search results. To advance research in
this area, we present nlcTables, a comprehensive benchmark dataset comprising
627 diverse queries spanning NL-only, union, join, and fuzzy conditions, 22,080
candidate tables, and 21,
|    | reference                                                                                                     | date     | key idea/summary                                                                                                                                                                                    |
|----|---------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [TableBank: Table Benchmark for Image-based Table Detection and Recognition](http://arxiv.org/abs/1903.01949) | 03/05/19 | TableBank is a new image-based table detection and recognition dataset with 417K high-quality labeled tables, designed to improve generalization and support deep learning approaches in this task. |
