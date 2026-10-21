## Related Works

Table discovery has become a critical task in data management, especially with the proliferation of tabular data repositories. Traditional approaches typically rely on query tables or vague keywords to retrieve relevant tables, often leading to an overwhelming number of results that require manual filtering \[[Junjie Xing' 2024-10-16](http://arxiv.org/abs/2410.12164v2)\]. This limitation has motivated the development of more sophisticated methods that incorporate natural language (NL) to refine search results, a concept that aligns with our proposed task of NL-conditional table discovery (nlcTD) \[[Mrinal Haloi' 2022-08-31](http://arxiv.org/abs/2209.09207v2)\]. 

Several recent works have focused on improving table discovery by leveraging semantic and structural information. For instance, \[[Hugo Manuel Proença' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\] introduced a dataset for table detection in the wild, emphasizing the diversity of table structures and the need for robust models. Similarly,  presented a large-scale dataset for bitstream-corrupted video recovery, highlighting the importance of diverse and realistic data for training effective models. These datasets, while not directly related to table discovery, underscore the importance of comprehensive and varied training data in machine learning tasks.

In the realm of table discovery,  introduced a benchmark dataset for table structure recognition, emphasizing the need for consistent and accurate annotations. This work laid the groundwork for more advanced benchmarks that incorporate natural language conditions. Building on this,  proposed a dataset for table-to-text generation, demonstrating the potential of generating descriptive text from tables, which is a related but distinct task. 

The integration of natural language into table discovery has been explored in , where a dataset for table-based question answering was introduced. This work highlighted the challenges of aligning natural language queries with table structures, a key aspect of our nlcTD task. Additionally,  presented a dataset for remote sensing image understanding, emphasizing the need for detailed captions and object references, which can be seen as a parallel to the rich annotations in our nlcTables dataset.

The importance of diverse and realistic data for training models has also been emphasized in , where a dataset for pedestrian attribute recognition was introduced. This work demonstrated the value of incorporating multiple domains and conditions to enhance model performance. Similarly,  introduced a dataset for coral video segmentation, emphasizing the need for dense and accurate annotations, which is crucial for our nlcTables dataset.

In summary, the existing literature highlights the need for comprehensive, diverse, and accurately annotated datasets to advance table discovery, especially when incorporating natural language conditions. Our nlcTables dataset addresses these needs by providing a rich set of queries, candidate tables, and relevance annotations, enabling more effective evaluation of advanced techniques in this challenging area.

References:
1. [Document 3]  
2. [Document 2]  
3. [Document 5]  
4. [Document 4]  
5. [Document 6]  
6. [Document 7]  
7. [Document 8]  
8. [Document 9]  
9. [Document 10]
## Research papers
### Outline
- [Data Diversity and Realism in Training [1 papers]](#category-data-diversity-and-realism-in-training)
- [Benchmark Datasets for Table Tasks [1 papers]](#category-benchmark-datasets-for-table-tasks)
- [Performance Evaluation of Existing Methods [1 papers]](#category-performance-evaluation-of-existing-methods)

### <a id='category-data-diversity-and-realism-in-training'></a>Data Diversity and Realism in Training: 1 papers found.
Context: 
	Document 1: [_citation_number]: «1»
[Category]: «Data Diversity and Realism in Training»
[Snippet]: «Language models such as GPT and Llama have shown remarkable ability on diverse natural language tasks, yet their performance on complex table tasks (e.g., NL-to-Code and data cleaning) remains suboptimal. Improving performance typically requires task-specific fine-tuning, which depends on expensive human labeling and is prone to overfitting.
  In this work, we propose Table-LLM-Specialist, a self-trained fine-tuning paradigm designed for table tasks. Our key insight is that many table tasks admit two dual formulations: a generative version and a classification version. Leveraging this duality, we introduce a Generator-Validator paradigm that iteratively generates and validates training data using language models, enabling effective fine-tuning without manually labeled data.
  Extensive evaluations on Llama, GPT-3.5, and GPT-4 show that Table-LLM-Specialist achieves (1) strong performance across diverse tasks compared to base models, for example, models fine-tuned on GPT-3.5 often surpass GPT-4 level quality; (2) lower deployment cost by enabling smaller models to reach high quality with reduced latency and cost; and (3) better generalization across multiple benchmarks, due to training on diverse, systematically generated data from real-world tables.
  Our code is available at https://github.com/microsoft/Table-Specialist. Models fine-tuned with Table-LLM-Specialist have been integrated into Microsoft Excel and are deployed in production for automated table data cleaning.»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-22T12:44:59+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[Hugo Manuel Proença' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\]. Further details .) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: With the growing abundance of repositories containing tabular data,
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[Hugo Manuel Proença' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\]. Further details discussed in contexts \[[Mrinal Haloi' 2022-08-31](http://arxiv.org/abs/2209.09207v2)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
The category of "Data Diversity and Realism in Training" highlights the importance of using diverse and realistic training data to improve the performance of language models on complex tasks. This is particularly relevant for tasks involving tabular data, where models often struggle with tasks such as natural language to code translation and data cleaning \[[Junjie Xing' 2024-10-16](http://arxiv.org/abs/2410.12164v2)\]. The key insight is that many table-related tasks can be formulated in dual ways—generative and classification—allowing for the development of training paradigms that iteratively generate and validate data using language models \[[Junjie Xing' 2024-10-16](http://arxiv.org/abs/2410.12164v2)\]. This approach enables effective fine-tuning without the need for expensive human-labeled data, thereby improving both performance and cost efficiency \[[Junjie Xing' 2024-10-16](http://arxiv.org/abs/2410.12164v2)\]. Moreover, training on systematically generated data from real-world tables leads to better generalization across multiple benchmarks, as demonstrated by the success of Table-LLM-Specialist in achieving high-quality results with smaller models \[[Junjie Xing' 2024-10-16](http://arxiv.org/abs/2410.12164v2)\]. The use of diverse and realistic data is also critical for tasks like natural language conditional table discovery, where the ability to handle complex queries and conditions is essential \[[Junjie Xing' 2024-10-16](http://arxiv.org/abs/2410.12164v2)\].
|    | reference                                                                                                                                        | date     | key idea/summary                                                                                                                                                                                                                                               |
|----|--------------------------------------------------------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Table-LLM-Specialist: Language Model Specialists for Tables using Iterative Generator-Validator Fine-tuning](http://arxiv.org/abs/2410.12164v2) | 10/16/24 | Table-LLM-Specialist is a self-trained fine-tuning paradigm for table tasks that leverages a Generator-Validator paradigm to iteratively generate and validate training data, achieving strong performance and lower deployment costs without manual labeling. |
### <a id='category-benchmark-datasets-for-table-tasks'></a>Benchmark Datasets for Table Tasks: 1 papers found.
Context: 
	Document 1: [_citation_number]: «2»
[Category]: «Benchmark Datasets for Table Tasks»
[Snippet]: «Recent deep learning approaches in table detection achieved outstanding performance and proved to be effective in identifying document layouts. Currently, available table detection benchmarks have many limitations, including the lack of samples diversity, simple table structure, the lack of training cases, and samples quality. In this paper, we introduce a diverse large-scale dataset for table detection with more than seven thousand samples containing a wide variety of table structures collected from many diverse sources. In addition to that, we also present baseline results using a convolutional neural network-based method to detect table structure in documents. Experimental results show the superiority of applying convolutional deep learning methods over classical computer vision-based methods. The introduction of this diverse table detection dataset will enable the community to develop high throughput deep learning methods for understanding document layout and tabular data processing. Dataset is available at: 1. https://www.kaggle.com/datasets/mrinalim/stdw-dataset 2. https://huggingface.co/datasets/n3011/STDW»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-22T12:44:59+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[Hugo Manuel Proença' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\]. Further details .) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: With the growing abundance of repositories containing tabular data, discovering relevant tables for in-depth analysis remains a challenging task. Existing table discovery methods primarily retrieve desired tables based on a query table or several vague keywords, leaving users to manually filter large result sets. To address this limitation, we propose a new task: NL-conditional table discovery (nlcTD), where users combine a query table with natural language (NL) requirements to refine search results. To advance research in this area, we present nlcTables, a comprehensive benchmark dataset comprising 627 diverse queries spanning NL-only, union, join, and fuzzy conditions, 22,080 candidate tables, and 21,200 relevance annotations. Our evaluation of six state-of-the-art table discovery methods on nlcTables reveals substantial performance gaps, highlighting the need for advanced techniques to tackle this challenging nlcTD scenario. The dataset, construction framework, and baseline implementations are publicly available at https://github.com/SuDIS-ZJU/nlcTables to foster future research.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[Hugo Manuel Proença' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\]. Further details discussed in contexts \[[Mrinal Haloi' 2022-08-31](http://arxiv.org/abs/2209.09207v2)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
The field of table detection has seen significant advancements with the introduction of large-scale, diverse benchmark datasets that address the limitations of earlier approaches. These datasets, such as the STDW dataset \[[Mrinal Haloi' 2022-08-31](http://arxiv.org/abs/2209.09207v2)\], provide a wide variety of table structures collected from multiple sources, offering more than seven thousand samples. This diversity helps improve the generalization of deep learning models, as traditional methods often struggled with sample diversity and quality \[[Mrinal Haloi' 2022-08-31](http://arxiv.org/abs/2209.09207v2)\]. The use of convolutional neural networks (CNNs) has also been shown to outperform classical computer vision techniques in detecting table structures, as demonstrated by baseline results in recent studies \[[Mrinal Haloi' 2022-08-31](http://arxiv.org/abs/2209.09207v2)\]. These datasets are crucial for advancing research in document layout understanding and tabular data processing, as they enable the development of high-throughput deep learning methods that can handle complex and varied table structures. The availability of such datasets on platforms like Kaggle and Hugging Face further supports the community's efforts in this area \[[Mrinal Haloi' 2022-08-31](http://arxiv.org/abs/2209.09207v2)\].
|    | reference                                                                                                            | date     | key idea/summary                                                                                                                                                                                                                                                        |
|----|----------------------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Table Detection in the Wild: A Novel Diverse Table Detection Dataset and Method](http://arxiv.org/abs/2209.09207v2) | 08/31/22 | This paper introduces a diverse large-scale table detection dataset with over seven thousand samples and presents baseline results using a convolutional neural network-based method, demonstrating the superiority of deep learning approaches over classical methods. |
### <a id='category-performance-evaluation-of-existing-methods'></a>Performance Evaluation of Existing Methods: 1 papers found.
Context: 
	Document 1: [_citation_number]: «3»
[Category]: «Performance Evaluation of Existing Methods»
[Snippet]: «We introduce the problem of robust subgroup discovery, i.e., finding a set of interpretable descriptions of subsets that 1) stand out with respect to one or more target attributes, 2) are statistically robust, and 3) non-redundant. Many attempts have been made to mine either locally robust subgroups or to tackle the pattern explosion, but we are the first to address both challenges at the same time from a global modelling perspective. First, we formulate the broad model class of subgroup lists, i.e., ordered sets of subgroups, for univariate and multivariate targets that can consist of nominal or numeric variables, including traditional top-1 subgroup discovery in its definition. This novel model class allows us to formalise the problem of optimal robust subgroup discovery using the Minimum Description Length (MDL) principle, where we resort to optimal Normalised Maximum Likelihood and Bayesian encodings for nominal and numeric targets, respectively. Second, finding optimal subgroup lists is NP-hard. Therefore, we propose SSD++, a greedy heuristic that finds good subgroup lists and guarantees that the most significant subgroup found according to the MDL criterion is added in each iteration. In fact, the greedy gain is shown to be equivalent to a Bayesian one-sample proportion, multinomial, or t-test between the subgroup and dataset marginal target distributions plus a multiple hypothesis testing penalty. Furthermore, we empirically show on 54 datasets that SSD++ outperforms previous subgroup discovery methods in terms of quality, generalisation on unseen data, and subgroup list size.»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-22T12:44:59+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[Hugo Manuel Proença' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\]. Further details .) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: With the growing abundance of repositories containing tabular data,
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[Hugo Manuel Proença' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\]. Further details discussed in contexts \[[Mrinal Haloi' 2022-08-31](http://arxiv.org/abs/2209.09207v2)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
The category "Performance Evaluation of Existing Methods" highlights the challenges and advancements in evaluating subgroup discovery techniques. Existing methods often focus on either local robustness or addressing pattern explosion, but few address both simultaneously \[[Hugo Manuel Proença' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\]. The introduction of subgroup lists as an ordered set of subgroups allows for a more comprehensive evaluation framework, particularly when considering univariate and multivariate targets with nominal or numeric variables \[[Hugo Manuel Proença' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\]. This approach formalizes the problem using the Minimum Description Length (MDL) principle, which enables the use of Normalized Maximum Likelihood and Bayesian encodings tailored to different data types \[[Hugo Manuel Proença' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\]. The NP-hard nature of finding optimal subgroup lists necessitates heuristic approaches like SSD++, which guarantees the inclusion of the most significant subgroup according to the MDL criterion in each iteration \[[Hugo Manuel Proença' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\]. The greedy gain in SSD++ is equivalent to Bayesian statistical tests, such as one-sample proportion, multinomial, or t-tests, combined with multiple hypothesis testing penalties \[[Hugo Manuel Proença' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\]. Empirical evaluations on 54 datasets demonstrate that SSD++ outperforms previous methods in terms of quality, generalization, and subgroup list size \[[Hugo Manuel Proença' 2021-03-25](http://arxiv.org/abs/2103.13686v4)\]. This underscores the importance of holistic evaluation frameworks that balance robustness, interpretability, and scalability in subgroup discovery tasks.
|    | reference                                                      | date     | key idea/summary                                                                                                                                                                                          |
|----|----------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Robust subgroup discovery](http://arxiv.org/abs/2103.13686v4) | 03/25/21 | The paper introduces SSD++, a greedy heuristic for robust subgroup discovery that addresses both statistical robustness and non-redundancy, outperforming existing methods in quality and generalization. |
