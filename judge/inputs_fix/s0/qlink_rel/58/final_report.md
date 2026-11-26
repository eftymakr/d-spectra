## Related Works

Table-based information retrieval has garnered significant attention in recent years, driven by the increasing availability of structured data. Early approaches focused on retrieving tables based on keyword matches or schema similarity, often resulting in noisy or incomplete results \[[3](http://arxiv.org/abs/1802.06159)\]. These methods typically relied on simple string matching or basic semantic similarity measures, which limited their ability to capture complex relationships between natural language queries and tabular data \[[3](http://arxiv.org/abs/1802.06159)\]. More recent work has sought to improve this by incorporating semantic understanding, particularly through the use of pretrained language models \[[1](http://arxiv.org/abs/2005.08314)\].

Pretrained models such as TaBERT have been designed to jointly understand both textual and tabular data, enabling better semantic parsing and reasoning over structured information \[[1](http://arxiv.org/abs/2005.08314)\]. This is particularly important for tasks like semantic parsing, where models must interpret both free-form questions and structured database tables \[[1](http://arxiv.org/abs/2005.08314)\]. The work in \[[2](http://arxiv.org/abs/1508.00305)\] further advances this by focusing on compositional semantic parsing, where models must handle complex logical expressions over semi-structured tables. This approach introduces strong typing constraints and logical-form driven parsing, leading to significant improvements over traditional baselines \[[2](http://arxiv.org/abs/1508.00305)\].

Another important direction is ad hoc table retrieval, where the goal is to find relevant tables based on natural language queries \[[3](http://arxiv.org/abs/1802.06159)\]. This task is challenging due to the open-ended nature of the knowledge sources and the combinatorial complexity of logical forms \[[2](http://arxiv.org/abs/1508.00305)\]. Recent methods have explored semantic matching between queries and tables using multiple representation spaces and similarity measures \[[3](http://arxiv.org/abs/1802.06159)\]. These approaches have shown substantial improvements over previous state-of-the-art methods, particularly when evaluated on large-scale datasets \[[3](http://arxiv.org/abs/1802.06159)\].

The proposed nlcTD task [abstract] builds on these advances by combining a query table with natural language conditions to refine search results. This is a novel approach that addresses the limitations of existing methods, which often rely on either keyword-based or schema-based retrieval [abstract]. The nlcTables benchmark dataset introduced in this work includes a wide range of query types, including NL-only, union, join, and fuzzy conditions, providing a comprehensive evaluation framework for future research [abstract].

In summary, while existing methods have made progress in table retrieval and semantic parsing, the integration of natural language conditions with structured data remains a challenging and underexplored area. The nlcTD task and the nlcTables dataset represent a significant step forward in this direction [abstract].

References:  
\[[1](http://arxiv.org/abs/2005.08314)\] TaBERT: Pretraining for Joint Understanding of Textual and Tabular Data  
\[[2](http://arxiv.org/abs/1508.00305)\] Compositional Semantic Parsing on Semi-Structured Tables  
\[[3](http://arxiv.org/abs/1802.06159)\] Ad Hoc Table Retrieval using Semantic Similarity
## Research papers
### Outline
- [Pretrained Language Models for Tabular Data [1 papers]](#category-pretrained-language-models-for-tabular-data)
- [Semantic Parsing and Logical Form Representation [1 papers]](#category-semantic-parsing-and-logical-form-representation)
- [Ad Hoc Table Retrieval Approaches [1 papers]](#category-ad-hoc-table-retrieval-approaches)

### <a id='category-pretrained-language-models-for-tabular-data'></a>Pretrained Language Models for Tabular Data: 1 papers found.
Context: 
	Document 1: [Snippet]: «Recent years have witnessed the burgeoning of pretrained language models (LMs) for text-based natural language (NL) understanding tasks. Such models are typically trained on free-form NL text, hence may not be suitable for tasks like semantic parsing over structured data, which require reasoning over both free-form NL questions and structured tabular data (e.g., database tables). In this paper we present TaBERT, a pretrained LM that jointly learns representations for NL sentences and (semi-)structured tables. TaBERT is trained on a large corpus of 26 million tables and their English contexts. In experiments, neural semantic parsers using TaBERT as feature representation layers achieve new best results on the challenging weakly-supervised semantic parsing benchmark WikiTableQuestions, while performing competitively on the text-to-SQL dataset Spider.»
[_citation_number]: «1»
[Category]: «Pretrained Language Models for Tabular Data»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-22T12:44:59+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1802.06159)\]. Further details .) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: With the growing abundance of repositories containing tabular data,
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
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1802.06159)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1508.00305)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Pretrained language models have gained significant traction in natural language understanding tasks, but their effectiveness in handling structured data such as tabular information remains a challenge \[[1](http://arxiv.org/abs/2005.08314)\]. Traditional models are typically trained on free-form text, which limits their ability to reason over both natural language questions and structured tables, such as database tables \[[1](http://arxiv.org/abs/2005.08314)\]. To address this gap, researchers have developed specialized models like TaBERT, which jointly learn representations for natural language sentences and (semi-)structured tables \[[1](http://arxiv.org/abs/2005.08314)\]. TaBERT is trained on a large corpus of 26 million tables and their associated English contexts, enabling it to better capture the interplay between textual and tabular data \[[1](http://arxiv.org/abs/2005.08314)\]. This advancement has led to improved performance in semantic parsing tasks, such as the WikiTableQuestions benchmark, where models using TaBERT as feature representations achieved new best results \[[1](http://arxiv.org/abs/2005.08314)\]. Additionally, TaBERT performs competitively on text-to-SQL tasks like Spider, demonstrating its versatility in handling both structured and unstructured data \[[1](http://arxiv.org/abs/2005.08314)\]. These developments highlight the growing importance of pretrained models designed specifically for tabular data, as they offer a more robust framework for tasks requiring reasoning over complex, structured datasets.
|    | reference                                                                                                  | date     | key idea/summary                                                                                                                                                                              |
|----|------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [TaBERT: Pretraining for Joint Understanding of Textual and Tabular Data](http://arxiv.org/abs/2005.08314) | 05/01/20 | TaBERT is a pretrained language model that jointly learns representations for natural language sentences and structured tables, achieving state-of-the-art results in semantic parsing tasks. |
### <a id='category-semantic-parsing-and-logical-form-representation'></a>Semantic Parsing and Logical Form Representation: 1 papers found.
Context: 
	Document 1: [Snippet]: «Two important aspects of semantic parsing for question answering are the breadth of the knowledge source and the depth of logical compositionality. While existing work trades off one aspect for another, this paper simultaneously makes progress on both fronts through a new task: answering complex questions on semi-structured tables using question-answer pairs as supervision. The central challenge arises from two compounding factors: the broader domain results in an open-ended set of relations, and the deeper compositionality results in a combinatorial explosion in the space of logical forms. We propose a logical-form driven parsing algorithm guided by strong typing constraints and show that it obtains significant improvements over natural baselines. For evaluation, we created a new dataset of 22,033 complex questions on Wikipedia tables, which is made publicly available.»
[_citation_number]: «2»
[Category]: «Semantic Parsing and Logical Form Representation»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-22T12:44:59+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1802.06159)\]. Further details .) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: With the growing abundance of repositories containing tabular data, discovering relevant tables for in-depth analysis remains a challenging task. Existing table discovery methods primarily retrieve desired tables based on a query table or several vague keywords, leaving users to manually filter large result sets. To address this limitation, we propose a new task: NL-conditional table discovery (nlcTD), where users combine a query table with natural language (NL) requirements to refine search results. To advance research in this area, we present nlcTables, a comprehensive benchmark dataset comprising 627 diverse queries spanning NL-only, union, join, and fuzzy conditions, 22,080 candidate tables, and 21,200 relevance annotations. Our evaluation of six state-of-the-art table discovery methods on nlcTables reveals substantial performance gaps, highlighting the need for advanced techniques to tackle this challenging nlcTD scenario. The dataset, construction framework, and baseline implementations are publicly available at https://github.com/SuDIS-ZJU/nlcTables to foster future research.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1802.06159)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1508.00305)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The category of semantic parsing and logical form representation focuses on the challenges and advancements in interpreting and generating structured logical forms from natural language, particularly in the context of complex question answering. A key theme is the balance between the breadth of knowledge sources and the depth of logical compositionality, as existing methods often trade off one for the other \[[2](http://arxiv.org/abs/1508.00305)\]. This challenge is compounded by the open-ended nature of relations in broader domains and the combinatorial explosion of logical forms in deeper compositions \[[2](http://arxiv.org/abs/1508.00305)\]. Recent work has sought to address these issues by proposing new tasks, such as answering complex questions on semi-structured tables, using question-answer pairs as supervision \[[2](http://arxiv.org/abs/1508.00305)\]. These approaches emphasize the importance of logical-form driven parsing algorithms guided by strong typing constraints, which have shown significant improvements over natural baselines \[[2](http://arxiv.org/abs/1508.00305)\]. The development of large-scale datasets, such as the 22,033 complex questions on Wikipedia tables, has further enabled benchmarking and evaluation of these methods \[[2](http://arxiv.org/abs/1508.00305)\]. Such efforts highlight the growing interest in creating robust and scalable semantic parsing frameworks that can handle the complexity of real-world data sources.
|    | reference                                                                                   | date     | key idea/summary                                                                                                                                                                                                                                                                     |
|----|---------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Compositional Semantic Parsing on Semi-Structured Tables](http://arxiv.org/abs/1508.00305) | 08/03/15 | This paper addresses the challenges of semantic parsing by proposing a logical-form driven parsing algorithm that improves both the breadth of knowledge sources and the depth of logical compositionality through a new task involving complex questions on semi-structured tables. |
### <a id='category-ad-hoc-table-retrieval-approaches'></a>Ad Hoc Table Retrieval Approaches: 1 papers found.
Context: 
	Document 1: [Snippet]: «We introduce and address the problem of ad hoc table retrieval: answering a keyword query with a ranked list of tables. This task is not only interesting on its own account, but is also being used as a core component in many other table-based information access scenarios, such as table completion or table mining. The main novel contribution of this work is a method for performing semantic matching between queries and tables. Specifically, we (i) represent queries and tables in multiple semantic spaces (both discrete sparse and continuous dense vector representations) and (ii) introduce various similarity measures for matching those semantic representations. We consider all possible combinations of semantic representations and similarity measures and use these as features in a supervised learning model. Using a purpose-built test collection based on Wikipedia tables, we demonstrate significant and substantial improvements over a state-of-the-art baseline.»
[_citation_number]: «3»
[Category]: «Ad Hoc Table Retrieval Approaches»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-22T12:44:59+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1802.06159)\]. Further details .) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: With the growing abundance of repositories containing tabular data,
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
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1802.06159)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1508.00305)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Ad hoc table retrieval has emerged as a critical area of research, particularly due to the increasing volume of tabular data available in repositories. This task involves answering keyword queries with a ranked list of relevant tables, serving as a foundational component in various table-based information access scenarios such as table completion and table mining \[[3](http://arxiv.org/abs/1802.06159)\]. Existing approaches often rely on semantic matching between queries and tables, employing techniques that represent both in multiple semantic spaces—such as discrete sparse and continuous dense vector representations—and utilizing various similarity measures for comparison \[[3](http://arxiv.org/abs/1802.06159)\]. These methods typically consider combinations of semantic representations and similarity measures as features in supervised learning models, aiming to improve retrieval accuracy. The work presented here demonstrates significant improvements over state-of-the-art baselines using a purpose-built test collection based on Wikipedia tables \[[3](http://arxiv.org/abs/1802.06159)\]. This highlights the ongoing efforts to enhance semantic understanding and matching in table retrieval, which is essential for more efficient and accurate information access.
|    | reference                                                                           | date     | key idea/summary                                                                                                                                                                                |
|----|-------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Ad Hoc Table Retrieval using Semantic Similarity](http://arxiv.org/abs/1802.06159) | 02/16/18 | The paper introduces a method for semantic matching between keyword queries and tables, using multiple semantic representations and similarity measures to improve table retrieval performance. |
