## Related Works

Table discovery and related tasks have seen significant advancements in recent years, driven by the increasing availability of tabular data in various domains. Existing approaches primarily focus on retrieving tables based on a query table or vague keywords, often leading to large result sets that require manual filtering \[[1' 2024-10-16](http://arxiv.org/abs/2410.12164v2)\]. This limitation highlights the need for more sophisticated methods that can integrate natural language (NL) requirements to refine search results, a challenge that our proposed task, NL-conditional table discovery (nlcTD), aims to address \[[1' 2024-10-16](http://arxiv.org/abs/2410.12164v2)\].

Several works have explored table detection and related tasks. For instance, \[[2' 2022-08-31](http://arxiv.org/abs/2209.09207v2)\] introduces a diverse large-scale dataset for table detection, containing over 7,000 samples with varied table structures collected from multiple sources. This dataset addresses the limitations of previous benchmarks, such as lack of diversity and poor sample quality, and enables the development of high-throughput deep learning methods for document layout understanding and tabular data processing. The use of convolutional neural networks (CNNs) in this work demonstrates superior performance over classical computer vision methods \[[2' 2022-08-31](http://arxiv.org/abs/2209.09207v2)\].

In the realm of table generation and refinement, \[[1' 2024-10-16](http://arxiv.org/abs/2410.12164v2)\] proposes Table-LLM-Specialist, a self-trained fine-tuning paradigm designed for complex table tasks. This method leverages the duality between generative and classification formulations to iteratively generate and validate training data using language models, thereby reducing reliance on expensive human labeling. The approach enables smaller models to achieve high-quality results with reduced latency and cost, and has been successfully integrated into Microsoft Excel for automated table data cleaning \[[1' 2024-10-16](http://arxiv.org/abs/2410.12164v2)\].

The problem of subgroup discovery, which involves identifying subsets of data that stand out with respect to target attributes, has also been explored in the context of tabular data \[[3' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\]. This work introduces robust subgroup discovery, addressing challenges such as statistical robustness and non-redundancy. The proposed method, SSD++, uses a greedy heuristic to find optimal subgroup lists and guarantees the inclusion of the most significant subgroup according to the Minimum Description Length (MDL) principle. Empirical evaluations on 54 datasets show that SSD++ outperforms previous methods in terms of quality and generalization \[[3' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\].

In addition to these efforts, the nlcTables dataset \[[1' 2024-10-16](http://arxiv.org/abs/2410.12164v2)\] provides a comprehensive benchmark for evaluating NL-conditional table discovery methods. It includes 627 diverse queries, 22,080 candidate tables, and 21,200 relevance annotations, enabling researchers to assess the effectiveness of different approaches in refining search results based on natural language conditions. The dataset and baseline implementations are publicly available, fostering further research in this area \[[1' 2024-10-16](http://arxiv.org/abs/2410.12164v2)\].

References  
\[[1' 2024-10-16](http://arxiv.org/abs/2410.12164v2)\] Table-LLM-Specialist: Language Model Specialists for Tables using Iterative Generator-Validator Fine-tuning  
\[[2' 2022-08-31](http://arxiv.org/abs/2209.09207v2)\] Table Detection in the Wild: A Novel Diverse Table Detection Dataset and Method  
\[[3' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\] Robust subgroup discovery
## Research papers
### Outline
- [Model Training and Optimization Strategies [1 papers]](#category-model-training-and-optimization-strategies)
- [Benchmark Datasets for Table Tasks [1 papers]](#category-benchmark-datasets-for-table-tasks)
- [Subgroup Discovery Techniques [1 papers]](#category-subgroup-discovery-techniques)

### <a id='category-model-training-and-optimization-strategies'></a>Model Training and Optimization Strategies: 1 papers found.
Context: 
	Document 1: [Snippet]: «Language models such as GPT and Llama have shown remarkable ability on diverse natural language tasks, yet their performance on complex table tasks (e.g., NL-to-Code and data cleaning) remains suboptimal. Improving performance typically requires task-specific fine-tuning, which depends on expensive human labeling and is prone to overfitting.
  In this work, we propose Table-LLM-Specialist, a self-trained fine-tuning paradigm designed for table tasks. Our key insight is that many table tasks admit two dual formulations: a generative version and a classification version. Leveraging this duality, we introduce a Generator-Validator paradigm that iteratively generates and validates training data using language models, enabling effective fine-tuning without manually labeled data.
  Extensive evaluations on Llama, GPT-3.5, and GPT-4 show that Table-LLM-Specialist achieves (1) strong performance across diverse tasks compared to base models, for example, models fine-tuned on GPT-3.5 often surpass GPT-4 level quality; (2) lower deployment cost by enabling smaller models to reach high quality with reduced latency and cost; and (3) better generalization across multiple benchmarks, due to training on diverse, systematically generated data from real-world tables.
  Our code is available at https://github.com/microsoft/Table-Specialist. Models fine-tuned with Table-LLM-Specialist have been integrated into Microsoft Excel and are deployed in production for automated table data cleaning.»
[_citation_number]: «1»
[Category]: «Model Training and Optimization Strategies»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-24T12:44:59+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\]. Further details .) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: With the growing abundance of repositories containing tabular data,
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\]. Further details discussed in contexts \[[2' 2022-08-31](http://arxiv.org/abs/2209.09207v2)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Recent advancements in model training and optimization strategies have focused on improving the performance of language models on complex table tasks, such as natural language to code translation and data cleaning \[[1' 2024-10-16](http://arxiv.org/abs/2410.12164v2)\]. A key challenge is that traditional fine-tuning approaches rely on expensive human-labeled data and are prone to overfitting \[[1' 2024-10-16](http://arxiv.org/abs/2410.12164v2)\]. To address this, researchers have proposed self-trained fine-tuning paradigms that leverage the dual formulations of table tasks—generative and classification—through a Generator-Validator paradigm \[[1' 2024-10-16](http://arxiv.org/abs/2410.12164v2)\]. This approach enables iterative generation and validation of training data using language models, reducing the need for manual labeling \[[1' 2024-10-16](http://arxiv.org/abs/2410.12164v2)\]. Such strategies have led to significant improvements in performance across diverse tasks, with models fine-tuned on Llama and GPT-3.5 often surpassing GPT-4 in quality \[[1' 2024-10-16](http://arxiv.org/abs/2410.12164v2)\]. Additionally, these methods have demonstrated lower deployment costs by allowing smaller models to achieve high-quality results with reduced latency and cost \[[1' 2024-10-16](http://arxiv.org/abs/2410.12164v2)\]. The success of these approaches highlights the importance of systematic data generation and validation in optimizing model performance for table-related tasks.
|    | reference                                                                                                                                        | date     | key idea/summary                                                                                                                                                                                                                                          |
|----|--------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Table-LLM-Specialist: Language Model Specialists for Tables using Iterative Generator-Validator Fine-tuning](http://arxiv.org/abs/2410.12164v2) | 10/16/24 | Table-LLM-Specialist is a self-trained fine-tuning paradigm for table tasks that uses a Generator-Validator paradigm to iteratively generate and validate training data, achieving strong performance and lower deployment costs without manual labeling. |
### <a id='category-benchmark-datasets-for-table-tasks'></a>Benchmark Datasets for Table Tasks: 1 papers found.
Context: 
	Document 1: [Snippet]: «Recent deep learning approaches in table detection achieved outstanding performance and proved to be effective in identifying document layouts. Currently, available table detection benchmarks have many limitations, including the lack of samples diversity, simple table structure, the lack of training cases, and samples quality. In this paper, we introduce a diverse large-scale dataset for table detection with more than seven thousand samples containing a wide variety of table structures collected from many diverse sources. In addition to that, we also present baseline results using a convolutional neural network-based method to detect table structure in documents. Experimental results show the superiority of applying convolutional deep learning methods over classical computer vision-based methods. The introduction of this diverse table detection dataset will enable the community to develop high throughput deep learning methods for understanding document layout and tabular data processing. Dataset is available at: 1. https://www.kaggle.com/datasets/mrinalim/stdw-dataset 2. https://huggingface.co/datasets/n3011/STDW»
[_citation_number]: «2»
[Category]: «Benchmark Datasets for Table Tasks»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-22T12:44:59+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\]. Further details .) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: With the growing abundance of repositories containing tabular data, discovering relevant tables for in-depth analysis remains a challenging task. Existing table discovery methods primarily retrieve desired tables based on a query table or several vague keywords, leaving users to manually filter large result sets. To address this limitation, we propose a new task: NL-conditional table discovery (nlcTD), where users combine a query table with natural language (NL) requirements to refine search results. To advance research in this area, we present nlcTables, a comprehensive benchmark dataset comprising 627 diverse queries spanning NL-only, union, join, and fuzzy conditions, 22,080 candidate tables, and 21,200 relevance annotations. Our evaluation of six state-of-the-art table discovery methods on nlcTables reveals substantial performance gaps, highlighting the need for advanced techniques to tackle this challenging nlcTD scenario. The dataset, construction framework, and baseline implementations are publicly available at https://github.com/SuDIS-ZJU/nlcTables to foster future research.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\]. Further details discussed in contexts \[[2' 2022-08-31](http://arxiv.org/abs/2209.09207v2)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Recent advancements in table detection have emphasized the importance of diverse and high-quality datasets to improve the performance of deep learning models \[[2' 2022-08-31](http://arxiv.org/abs/2209.09207v2)\]. Existing benchmarks often suffer from limited sample diversity, simplistic table structures, and insufficient training cases, which hinder the development of robust models for document layout understanding \[[2' 2022-08-31](http://arxiv.org/abs/2209.09207v2)\]. To address these limitations, researchers have introduced large-scale datasets containing thousands of diverse table structures collected from various sources \[[2' 2022-08-31](http://arxiv.org/abs/2209.09207v2)\]. These datasets enable the training of convolutional neural networks that outperform classical computer vision techniques in detecting table layouts \[[2' 2022-08-31](http://arxiv.org/abs/2209.09207v2)\]. The availability of such datasets, such as the STDW dataset, has been crucial in advancing the field by providing a comprehensive resource for benchmarking and evaluating new methods \[[2' 2022-08-31](http://arxiv.org/abs/2209.09207v2)\]. Additionally, the integration of natural language processing techniques with table discovery tasks, such as the nlcTD approach, highlights the need for more sophisticated benchmarks that incorporate both structured and unstructured data \[[2' 2022-08-31](http://arxiv.org/abs/2209.09207v2)\]. The development of such datasets not only supports the creation of high-throughput deep learning models but also fosters further research into tabular data processing \[[2' 2022-08-31](http://arxiv.org/abs/2209.09207v2)\].
|    | reference                                                                                                            | date     | key idea/summary                                                                                                                                                                                                                                                       |
|----|----------------------------------------------------------------------------------------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Table Detection in the Wild: A Novel Diverse Table Detection Dataset and Method](http://arxiv.org/abs/2209.09207v2) | 08/31/22 | This paper introduces a diverse large-scale table detection dataset with over 7,000 samples and presents baseline results using a convolutional neural network-based method, demonstrating the superiority of deep learning over classical computer vision approaches. |
### <a id='category-subgroup-discovery-techniques'></a>Subgroup Discovery Techniques: 1 papers found.
Context: 
	Document 1: [Snippet]: «We introduce the problem of robust subgroup discovery, i.e., finding a set of interpretable descriptions of subsets that 1) stand out with respect to one or more target attributes, 2) are statistically robust, and 3) non-redundant. Many attempts have been made to mine either locally robust subgroups or to tackle the pattern explosion, but we are the first to address both challenges at the same time from a global modelling perspective. First, we formulate the broad model class of subgroup lists, i.e., ordered sets of subgroups, for univariate and multivariate targets that can consist of nominal or numeric variables, including traditional top-1 subgroup discovery in its definition. This novel model class allows us to formalise the problem of optimal robust subgroup discovery using the Minimum Description Length (MDL) principle, where we resort to optimal Normalised Maximum Likelihood and Bayesian encodings for nominal and numeric targets, respectively. Second, finding optimal subgroup lists is NP-hard. Therefore, we propose SSD++, a greedy heuristic that finds good subgroup lists and guarantees that the most significant subgroup found according to the MDL criterion is added in each iteration. In fact, the greedy gain is shown to be equivalent to a Bayesian one-sample proportion, multinomial, or t-test between the subgroup and dataset marginal target distributions plus a multiple hypothesis testing penalty. Furthermore, we empirically show on 54 datasets that SSD++ outperforms previous subgroup discovery methods in terms of quality, generalisation on unseen data, and subgroup list size.»
[_citation_number]: «3»
[Category]: «Subgroup Discovery Techniques»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-22T12:44:59+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\]. Further details .) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: With the growing abundance of repositories containing tabular data,
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\]. Further details discussed in contexts \[[2' 2022-08-31](http://arxiv.org/abs/2209.09207v2)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer:  
Subgroup discovery techniques have evolved to address the challenges of identifying meaningful and robust subgroups from large datasets. Recent approaches focus on ensuring subgroups are statistically significant, interpretable, and non-redundant \[[3' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\]. Traditional methods often prioritize either local robustness or tackle the pattern explosion, but few address both simultaneously \[[3' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\]. This has led to the development of novel model classes, such as subgroup lists, which are ordered sets of subgroups that can handle univariate and multivariate targets, including nominal and numeric variables \[[3' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\]. These models are formalized using principles like Minimum Description Length (MDL), which balance model complexity and data fit \[[3' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\]. The computational complexity of finding optimal subgroup lists is NP-hard, prompting the use of heuristic methods like SSD++ \[[3' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\]. This greedy algorithm ensures that the most significant subgroup, according to MDL criteria, is added iteratively, aligning with Bayesian statistical tests and incorporating multiple hypothesis testing penalties \[[3' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\]. Empirical evaluations on diverse datasets demonstrate that such methods outperform existing techniques in terms of subgroup quality, generalization, and list size \[[3' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\]. These advancements highlight the growing need for robust and scalable subgroup discovery frameworks that can handle the increasing complexity of modern data analysis tasks.
|    | reference                                                      | date     | key idea/summary                                                                                                                                                                                          |
|----|----------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Robust subgroup discovery](http://arxiv.org/abs/2103.13686v4) | 03/25/21 | The paper introduces SSD++, a greedy heuristic for robust subgroup discovery that addresses both statistical robustness and non-redundancy, outperforming existing methods in quality and generalization. |
