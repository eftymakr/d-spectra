## Related Works

Fact verification has seen significant advancements with the integration of structured knowledge sources such as knowledge graphs (KGs). Early efforts focused on unstructured text corpora, limiting the ability to leverage the rich semantic relationships provided by KGs \[[3](http://arxiv.org/abs/2011.03088)\]. For instance, FEVER introduces a large-scale dataset for fact verification, emphasizing the importance of evidence retrieval and classification \[[1](http://arxiv.org/abs/1803.05355)\]. However, these methods often lack the structured reasoning capabilities that KGs provide \[[3](http://arxiv.org/abs/2011.03088)\]. 

Recent works have explored the use of KGs for fact verification, but most rely on simplistic reasoning strategies. FactKG is a notable dataset that includes various reasoning types, such as one-hop and multi-hop reasoning, and provides a structured framework for evaluating KG-based fact verification \[[8](http://arxiv.org/abs/2305.06590)\]. Despite this, existing methods often fail to effectively integrate KGs with large language models (LLMs), which are known for their strong reasoning abilities \[[3](http://arxiv.org/abs/2011.03088)\]. 

To address these limitations, several approaches have been proposed. VitaminC introduces a benchmark that challenges models to discern subtle factual changes and adapt to evolving evidence \[[2](http://arxiv.org/abs/2103.08541)\]. This dataset emphasizes contrastive evidence pairs, which are critical for robust fact verification. Similarly, HoVer presents a dataset requiring many-hop reasoning across multiple Wikipedia articles, highlighting the complexity of long-range dependencies \[[3](http://arxiv.org/abs/2011.03088)\]. 

The integration of LLMs with KGs has also been explored. RoG proposes a novel method that synergizes LLMs with KGs to enable faithful and interpretable reasoning by leveraging the structural information of KGs \[[9](http://arxiv.org/abs/2310.01061)\]. This approach uses a planning-retrieval-reasoning framework to generate relation paths grounded in KGs, which are then used to retrieve valid reasoning paths for LLMs. 

Additionally, ProgramFC introduces a novel fact-checking model that decomposes complex claims into sub-tasks, using a shared library of specialized functions to guide the verification process \[[6](http://arxiv.org/abs/2305.12744)\]. This model leverages the in-context learning ability of LLMs to generate reasoning programs, making the process both explanatory and data-efficient. 

Another approach, FOLK, uses First-Order-Logic (FOL) to guide knowledge-grounded reasoning, translating claims into FOL clauses and performing reasoning over a set of question-and-answer pairs \[[7](http://arxiv.org/abs/2310.05253)\]. This method provides comprehensive explanations without relying on human-annotated data, enhancing the transparency of the verification process. 

In summary, while existing works have made strides in fact verification, the integration of KGs with LLMs remains a critical challenge. The proposed ClaimPKG framework addresses these challenges by seamlessly integrating LLM reasoning with structured knowledge from KGs, achieving state-of-the-art performance on benchmark datasets \[[3](http://arxiv.org/abs/2011.03088)\].

References:
1. \[[1](http://arxiv.org/abs/1803.05355)\] FEVER: a large-scale dataset for Fact Extraction and VERification [http://arxiv.org/abs/1803.05355]
2. \[[2](http://arxiv.org/abs/2103.08541)\] Get Your Vitamin C! Robust Fact Verification with Contrastive Evidence [http://arxiv.org/abs/2103.08541]
3. \[[3](http://arxiv.org/abs/2011.03088)\] FactKG: Fact Verification via Reasoning on Knowledge Graphs [http://arxiv.org/abs/2305.06590]
4. \[[4](http://arxiv.org/abs/1812.08434)\] Graph Neural Networks: A Review of Methods and Applications [http://arxiv.org/abs/1812.08434]
5. \[[5](http://arxiv.org/abs/2004.02349)\] TAPAS: Weakly Supervised Table Parsing via Pre-training [http://arxiv.org/abs/2004.02349]
6. \[[6](http://arxiv.org/abs/2305.12744)\] Fact-Checking Complex Claims with Program-Guided Reasoning [http://arxiv.org/abs/2305.12744]
7. \[[7](http://arxiv.org/abs/2310.05253)\] Explainable Claim Verification via Knowledge-Grounded Reasoning with Large Language Models [http://arxiv.org/abs/2310.05253]
8. \[[8](http://arxiv.org/abs/2305.06590)\] HoVer: A Dataset for Many-Hop Fact Extraction And Claim Verification [http://arxiv.org/abs/2011.03088]
9. \[[9](http://arxiv.org/abs/2310.01061)\] Reasoning on Graphs: Faithful and Interpretable Large Language Model Reasoning [http://arxiv.org/abs/2310.01061]
## Research papers
### Outline
- [Fact Verification Datasets [4 papers]](#category-fact-verification-datasets)
- [Knowledge-Grounded Reasoning Methods [4 papers]](#category-knowledge-grounded-reasoning-methods)
- [Benchmarking and Comparative Analysis [1 papers]](#category-benchmarking-and-comparative-analysis)
- [Subtask Decomposition in Fact Checking [1 papers]](#category-subtask-decomposition-in-fact-checking)
- [KG Integration in Fact Verification [1 papers]](#category-kg-integration-in-fact-verification)
- [Reasoning Frameworks for LLMs [1 papers]](#category-reasoning-frameworks-for-llms)

### <a id='category-fact-verification-datasets'></a>Fact Verification Datasets: 4 papers found.
Context: 
	Document 1: [Category]: «Fact Verification Datasets»
[_citation_number]: «1»
[Snippet]: «In this paper we introduce a new publicly available dataset for verification
against textual sources, FEVER: Fact Extraction and VERification. It consists
of 185,445 claims generated by altering sentences extracted from Wikipedia and
subsequently verified without knowledge of the sentence they were derived from.
The claims are classified as Supported, Refuted or NotEnoughInfo by annotators
achieving 0.6841 in Fleiss $\kappa$. For the first two classes, the annotators
also recorded the sentence(s) forming the necessary evidence for their
judgment. To characterize the challenge of the dataset presented, we develop a
pipeline approach and compare it to suitably designed oracles. The best
accuracy we achieve on labeling a claim accompanied by the correct evidence is
31.87%, while if we ignore the evidence we achieve 50.91%. Thus we believe that
FEVER is a challenging testbed that will help stimulate progress on claim
verification against textual sources.»

	Document 2: [Category]: «Fact Verification Datasets»
[_citation_number]: «2»
[Snippet]: «Typical fact verification models use retrieved written evidence to verify
claims. Evidence sources, however, often change over time as more information
is gathered and revised. In order to adapt, models must be sensitive to subtle
differences in supporting evidence. We present VitaminC, a benchmark infused
with challenging cases that require fact verification models to discern and
adjust to slight factual changes. We collect over 100,000 Wikipedia revisions
that modify an underlying fact, and leverage these revisions, together with
additional synthetically constructed ones, to create a total of over 400,000
claim-evidence pairs. Unlike previous resources, the examples in VitaminC are
contrastive, i.e., they contain evidence pairs that are nearly identical in
language and content, with the exception that one supports a given claim while
the other does not. We show that training using this design increases
robustness -- improving accuracy by 10% on adversarial fact verification and 6%
on adversarial natural language inference (NLI). Moreover, the structure of
VitaminC leads us to define additional tasks for fact-checking resources:
tagging relevant words in the evidence for verifying the claim, identifying
factual revisions, and providing automatic edits via factually consistent text
generation.»

	Document 3: [Category]: «Fact Verification Datasets»
[_citation_number]: «3»
[Snippet]: «We introduce HoVer (HOppy VERification), a dataset for many-hop evidence
extraction and fact verification. It challenges models to extract facts from
several Wikipedia articles that are relevant to a claim and classify whether
the claim is Supported or Not-Supported by the facts. In HoVer, the claims
require evidence to be extracted from as many as four English Wikipedia
articles and embody reasoning graphs of diverse shapes. Moreover, most of the
3/4-hop claims are written in multiple sentences, which adds to the complexity
of understanding long-range dependency relations such as coreference. We show
that the performance of an existing state-of-the-art semantic-matching model
degrades significantly on our dataset as the number of reasoning hops
increases, hence demonstrating the necessity of many-hop reasoning to achieve
strong results. We hope that the introduction of this challenging dataset and
the accompanying evaluation task will encourage research in many-hop fact
retrieval and information verification. We make the HoVer dataset publicly
available at https://hover-nlp.github.io»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-28T16:34:14+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2011.03088)\]. Further details \[[6](http://arxiv.org/abs/2305.12744)\]\[[7](http://arxiv.org/abs/2310.05253)\]\[[8](http://arxiv.org/abs/2305.06590)\]\[[9](http://arxiv.org/abs/2310.01061)\]\[[10](https://aclanthology.org/2022.acl-long.354/)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Integrating knowledge graphs (KGs) to enhance the reasoning capabilities of
large language models (LLMs) is an emerging research challenge in claim
verification. While KGs provide structured, semantically rich representations
well-suited for reasoning, most existing verification methods rely on
unstructured text corpora, limiting their ability to effectively leverage KGs.
Additionally, despite possessing strong reasoning abilities, modern LLMs
struggle with multi-step modular pipelines and reasoning over KGs without
adaptation. To address these challenges, we propose ClaimPKG, an end-to-end
framework that seamlessly integrates LLM reasoning with structured knowledge
from KGs. Specifically, the main idea of ClaimPKG is to employ a lightweight,
specialized LLM to represent the input claim as pseudo-subgraphs, guiding a
dedicated subgraph retrieval module to identify relevant KG subgraphs. These
retrieved subgraphs are then processed by a general-purpose LLM to produce the
final verdict and justification. Extensive experiments on the FactKG dataset
demonstrate that ClaimPKG achieves state-of-the-art performance, outperforming
strong baselines in this research field by 9%-12% accuracy points across
multiple categories. Furthermore, ClaimPKG exhibits zero-shot generalizability
to unstructured datasets such as HoVer and FEVEROUS, effectively combining
structured knowledge from KGs with LLM reasoning across various LLM backbones.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2011.03088)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2103.08541)\]\[[7](http://arxiv.org/abs/2310.05253)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer:  
Fact verification datasets play a crucial role in advancing the field of claim verification, offering diverse challenges and benchmarks for evaluating model performance. Datasets like FEVER \[[1](http://arxiv.org/abs/1803.05355)\] provide a large-scale, annotated collection of claims derived from Wikipedia, where each claim is classified as Supported, Refuted, or NotEnoughInfo, with evidence sentences recorded for verification. This dataset highlights the complexity of aligning claims with textual evidence, as models struggle to achieve high accuracy even with correct evidence \[[1](http://arxiv.org/abs/1803.05355)\]. Similarly, VitaminC \[[2](http://arxiv.org/abs/2103.08541)\] introduces a benchmark that emphasizes the dynamic nature of evidence, requiring models to adapt to subtle factual changes over time. By leveraging Wikipedia revisions and synthetic data, VitaminC creates contrastive examples that improve model robustness against adversarial scenarios. Meanwhile, HoVer \[[3](http://arxiv.org/abs/2011.03088)\] presents a challenging dataset focused on many-hop reasoning, where claims require evidence from multiple Wikipedia articles, necessitating the ability to handle long-range dependencies and complex reasoning graphs. These datasets collectively underscore the need for models that can effectively integrate structured knowledge and adapt to evolving evidence, paving the way for more sophisticated verification systems.
|    | reference                                                                                                        |   date | key idea/summary                                                                                                                                                                                                            |
|----|------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [FEVER: a large-scale dataset for Fact Extraction and VERification](http://arxiv.org/abs/1803.05355)             |    nan | FEVER is a challenging new dataset for fact verification, containing 185,445 claims verified by annotators with high inter-annotator agreement, designed to advance research in claim verification against textual sources. |
|  1 | [Get Your Vitamin C! Robust Fact Verification with Contrastive Evidence](http://arxiv.org/abs/2103.08541)        |    nan | VitaminC is a benchmark dataset designed to improve fact verification models by challenging them to discern subtle factual changes through contrastive claim-evidence pairs.                                                |
|  2 | [HoVer: A Dataset for Many-Hop Fact Extraction And Claim Verification](http://arxiv.org/abs/2011.03088)          |    nan | HoVer is a challenging dataset for many-hop evidence extraction and fact verification, requiring models to extract relevant facts from multiple Wikipedia articles and classify claims as Supported or Not-Supported.       |
|  3 | [(F)a(VIQ): (FA)ct Verification from Information-seeking Questions](https://aclanthology.org/2022.acl-long.354/) |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                   |
### <a id='category-knowledge-grounded-reasoning-methods'></a>Knowledge-Grounded Reasoning Methods: 4 papers found.
Context: 
	Document 1: [Category]: «Knowledge-Grounded Reasoning Methods»
[_citation_number]: «4»
[Snippet]: «Lots of learning tasks require dealing with graph data which contains rich
relation information among elements. Modeling physics systems, learning
molecular fingerprints, predicting protein interface, and classifying diseases
demand a model to learn from graph inputs. In other domains such as learning
from non-structural data like texts and images, reasoning on extracted
structures (like the dependency trees of sentences and the scene graphs of
images) is an important research topic which also needs graph reasoning models.
Graph neural networks (GNNs) are neural models that capture the dependence of
graphs via message passing between the nodes of graphs. In recent years,
variants of GNNs such as graph convolutional network (GCN), graph attention
network (GAT), graph recurrent network (GRN) have demonstrated ground-breaking
performances on many deep learning tasks. In this survey, we propose a general
design pipeline for GNN models and discuss the variants of each component,
systematically categorize the applications, and propose four open problems for
future research.»

	Document 2: [Category]: «Knowledge-Grounded Reasoning Methods»
[_citation_number]: «7»
[Snippet]: «Claim verification plays a crucial role in combating misinformation. While
existing works on claim verification have shown promising results, a crucial
piece of the puzzle that remains unsolved is to understand how to verify claims
without relying on human-annotated data, which is expensive to create at a
large scale. Additionally, it is important for models to provide comprehensive
explanations that can justify their decisions and assist human fact-checkers.
This paper presents First-Order-Logic-Guided Knowledge-Grounded (FOLK)
Reasoning that can verify complex claims and generate explanations without the
need for annotated evidence using Large Language Models (LLMs). FOLK leverages
the in-context learning ability of LLMs to translate the claim into a
First-Order-Logic (FOL) clause consisting of predicates, each corresponding to
a sub-claim that needs to be verified. Then, FOLK performs FOL-Guided reasoning
over a set of knowledge-grounded question-and-answer pairs to make veracity
predictions and generate explanations to justify its decision-making process.
This process makes our model highly explanatory, providing clear explanations
of its reasoning process in human-readable form. Our experiment results
indicate that FOLK outperforms strong baselines on three datasets encompassing
various claim verification challenges. Our code and data are available.»

	Document 3: [Category]: «Knowledge-Grounded Reasoning Methods»
[_citation_number]: «9»
[Snippet]: «Large language models (LLMs) have demonstrated impressive reasoning abilities
in complex tasks. However, they lack up-to-date knowledge and experience
hallucinations during reasoning, which can lead to incorrect reasoning
processes and diminish their performance and trustworthiness. Knowledge graphs
(KGs), which capture vast amounts of facts in a structured format, offer a
reliable source of knowledge for reasoning. Nevertheless, existing KG-based LLM
reasoning methods only treat KGs as factual knowledge bases and overlook the
importance of their structural information for reasoning. In this paper, we
propose a novel method called reasoning on graphs (RoG) that synergizes LLMs
with KGs to enable faithful and interpretable reasoning. Specifically, we
present a planning-retrieval-reasoning framework, where RoG first generates
relation paths grounded by KGs as faithful plans. These plans are then used to
retrieve valid reasoning paths from the KGs for LLMs to conduct faithful
reasoning. Furthermore, RoG not only distills knowledge from KGs to improve the
reasoning ability of LLMs through training but also allows seamless integration
with any arbitrary LLMs during inference. Extensive experiments on two
benchmark KGQA datasets demonstrate that RoG achieves state-of-the-art
performance on KG reasoning tasks and generates faithful and interpretable
reasoning results.»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-28T16:34:14+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2011.03088)\]. Further details \[[6](http://arxiv.org/abs/2305.12744)\]\[[7](http://arxiv.org/abs/2310.05253)\]\[[8](http://arxiv.org/abs/2305.06590)\]\[[9](http://arxiv.org/abs/2310.01061)\]\[[10](https://aclanthology.org/2022.acl-long.354/)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Integrating knowledge graphs (KGs) to enhance the reasoning capabilities of
large language models (LLMs) is an emerging research challenge in claim
verification. While KGs provide structured, semantically rich representations
well-suited for reasoning, most existing verification methods rely on
unstructured text corpora, limiting their ability to effectively leverage KGs.
Additionally, despite possessing strong reasoning abilities, modern LLMs
struggle with multi-step modular pipelines and reasoning over KGs without
adaptation. To address these challenges, we propose ClaimPKG, an end-to-end
framework that seamlessly integrates LLM reasoning with structured knowledge
from KGs. Specifically, the main idea of ClaimPKG is to employ a lightweight,
specialized LLM to represent the input claim as pseudo-subgraphs, guiding a
dedicated subgraph retrieval module to identify relevant KG subgraphs. These
retrieved subgraphs are then processed by a general-purpose LLM to produce the
final verdict and justification. Extensive experiments on the FactKG dataset
demonstrate that ClaimPKG achieves state-of-the-art performance, outperforming
strong baselines in this research field by 9%-12% accuracy points across
multiple categories. Furthermore, ClaimPKG exhibits zero-shot generalizability
to unstructured datasets such as HoVer and FEVEROUS, effectively combining
structured knowledge from KGs with LLM reasoning across various LLM backbones.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2011.03088)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2103.08541)\]\[[7](http://arxiv.org/abs/2310.05253)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Knowledge-Grounded Reasoning Methods have gained significant attention in recent years, particularly in the context of claim verification and enhancing the reasoning capabilities of large language models (LLMs). These methods leverage structured knowledge from knowledge graphs (KGs) to improve the accuracy and interpretability of reasoning processes \[[3](http://arxiv.org/abs/2011.03088)\]. While traditional approaches often rely on unstructured text corpora, the integration of KGs offers a more semantically rich representation, enabling more effective reasoning \[[3](http://arxiv.org/abs/2011.03088)\]. This is especially important given that LLMs, despite their strong reasoning abilities, often struggle with multi-step pipelines and reasoning over structured data without adaptation \[[3](http://arxiv.org/abs/2011.03088)\]. Recent works such as First-Order-Logic-Guided Knowledge-Grounded (FOLK) Reasoning have demonstrated the potential of using logical frameworks to translate claims into structured clauses, allowing for more transparent and explainable reasoning \[[7](http://arxiv.org/abs/2310.05253)\]. Similarly, the Reasoning on Graphs (RoG) approach has introduced a planning-retrieval-reasoning framework that synergizes LLMs with KGs by generating relation paths and retrieving valid reasoning paths, leading to more faithful and interpretable results \[[9](http://arxiv.org/abs/2310.01061)\]. These developments highlight the growing interest in combining the strengths of LLMs with the structured knowledge of KGs to address the challenges of claim verification and complex reasoning tasks.
|    | reference                                                                                                                                                              |   date | key idea/summary                                                                                                                                                                                                                                  |
|----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Graph Neural Networks: A Review of Methods and Applications](http://arxiv.org/abs/1812.08434)                                                                         |    nan | This survey presents a general design pipeline for graph neural networks (GNNs), discusses their variants, categorizes applications, and identifies four open problems for future research.                                                       |
|  1 | [Explainable Claim Verification via Knowledge-Grounded Reasoning with
  Large Language Models](http://arxiv.org/abs/2310.05253)                                        |    nan | The paper introduces FOLK, a method that uses First-Order-Logic-Guided Knowledge-Grounded Reasoning to verify claims and generate explanations without relying on human-annotated data, leveraging Large Language Models for in-context learning. |
|  2 | [Reasoning on Graphs: Faithful and Interpretable Large Language Model
  Reasoning](http://arxiv.org/abs/2310.01061)                                                    |    nan | The paper introduces RoG, a novel method that synergizes large language models with knowledge graphs to enable faithful and interpretable reasoning by leveraging both the factual and structural information of KGs.                             |
|  3 | [(KG-GPT:) (A) General Framework for Reasoning on Knowledge Graphs
                  Using Large Language Models](https://doi.org/10.18653/v1/2023.findings-emnlp.631) |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                         |
### <a id='category-benchmarking-and-comparative-analysis'></a>Benchmarking and Comparative Analysis: 1 papers found.
Context: 
	Document 1: [Category]: «Benchmarking and Comparative Analysis»
[_citation_number]: «5»
[Snippet]: «Answering natural language questions over tables is usually seen as a semantic parsing task. To alleviate the collection cost of full logical forms, one popular approach focuses on weak supervision consisting of denotations instead of logical forms. However, training semantic parsers from weak supervision poses difficulties, and in addition, the generated logical forms are only used as an intermediate step prior to retrieving the denotation. In this paper, we present TAPAS, an approach to question answering over tables without generating logical forms. TAPAS trains from weak supervision, and predicts the denotation by selecting table cells and optionally applying a corresponding aggregation operator to such selection. TAPAS extends BERT's architecture to encode tables as input, initializes from an effective joint pre-training of text segments and tables crawled from Wikipedia, and is trained end-to-end. We experiment with three different semantic parsing datasets, and find that TAPAS outperforms or rivals semantic parsing models by improving state-of-the-art accuracy on SQA from 55.1 to 67.2 and performing on par with the state-of-the-art on WIKISQL and WIKITQ, but with a simpler model architecture. We additionally find that transfer learning, which is trivial in our setting, from WIKISQL to WIKITQ, yields 48.7 accuracy, 4.2 points above the state-of-the-art.»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-28T16:34:14+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2011.03088)\]. Further details \[[6](http://arxiv.org/abs/2305.12744)\]\[[7](http://arxiv.org/abs/2310.05253)\]\[[8](http://arxiv.org/abs/2305.06590)\]\[[9](http://arxiv.org/abs/2310.01061)\]\[[10](https://aclanthology.org/2022.acl-long.354/)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Integrating knowledge graphs (KGs) to enhance the reasoning capabilities of large language models (LLMs) is an emerging research challenge in claim verification. While KGs provide structured, semantically rich representations well-suited for reasoning, most existing verification methods rely on unstructured text corpora, limiting their ability to effectively leverage KGs. Additionally, despite possessing strong reasoning abilities, modern LLMs struggle with multi-step modular pipelines and reasoning over KGs without adaptation. To address these challenges, we propose ClaimPKG, an end-to-end framework that seamlessly integrates LLM reasoning with structured knowledge from KGs. Specifically, the main idea of ClaimPKG is to employ a lightweight, specialized LLM to represent the input claim as pseudo-subgraphs, guiding a dedicated subgraph retrieval module to identify relevant KG subgraphs. These retrieved subgraphs are then processed by a general-purpose LLM to produce the final verdict and justification. Extensive experiments on the FactKG dataset demonstrate that ClaimPKG achieves state-of-the-art performance, outperforming strong baselines in this research field by 9%-12% accuracy points across multiple categories. Furthermore, ClaimPKG exhibits zero-shot generalizability to unstructured datasets such as HoVer and FEVEROUS, effectively combining structured knowledge from KGs with LLM reasoning across various LLM backbones.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2011.03088)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2103.08541)\]\[[7](http://arxiv.org/abs/2310.05253)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer:  
The category of benchmarking and comparative analysis is central to advancing question answering (QA) systems over structured data, particularly in semantic parsing tasks \[[5](http://arxiv.org/abs/2004.02349)\]. Traditional approaches often rely on generating full logical forms as an intermediate step, which is both costly and complex to collect \[[5](http://arxiv.org/abs/2004.02349)\]. To address these limitations, recent work has shifted toward weak supervision, using denotations instead of logical forms to train models \[[5](http://arxiv.org/abs/2004.02349)\]. This shift is exemplified by TAPAS, which directly predicts denotations by selecting relevant table cells and applying aggregation operators, eliminating the need for explicit logical form generation \[[5](http://arxiv.org/abs/2004.02349)\]. TAPAS leverages a modified BERT architecture to encode tables, pre-trained on a joint corpus of text and tables from Wikipedia, enabling end-to-end training \[[5](http://arxiv.org/abs/2004.02349)\]. Experimental results on datasets such as SQA, WIKISQL, and WIKITQ demonstrate that TAPAS achieves state-of-the-art accuracy, particularly on SQA, where it improves performance from 55.1% to 67.2% \[[5](http://arxiv.org/abs/2004.02349)\]. Additionally, transfer learning between datasets like WIKISQL and WIKITQ shows promising results, achieving 48.7% accuracy, 4.2 points above the previous state-of-the-art \[[5](http://arxiv.org/abs/2004.02349)\]. These findings highlight the potential of weakly supervised models to simplify QA pipelines while maintaining high performance, setting a new benchmark for semantic parsing and table-based QA systems.
|    | reference                                                                                  |   date | key idea/summary                                                                                                                                                                                                                                                                           |
|----|--------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [TAPAS: Weakly Supervised Table Parsing via Pre-training](http://arxiv.org/abs/2004.02349) |    nan | TAPAS is a novel approach for answering natural language questions over tables that avoids generating logical forms, instead directly predicting denotations by selecting table cells and applying aggregation operators, achieving state-of-the-art results on semantic parsing datasets. |
### <a id='category-subtask-decomposition-in-fact-checking'></a>Subtask Decomposition in Fact Checking: 1 papers found.
Context: 
	Document 1: [Category]: «Subtask Decomposition in Fact Checking»
[_citation_number]: «6»
[Snippet]: «Fact-checking real-world claims often requires collecting multiple pieces of
evidence and applying complex multi-step reasoning. In this paper, we present
Program-Guided Fact-Checking (ProgramFC), a novel fact-checking model that
decomposes complex claims into simpler sub-tasks that can be solved using a
shared library of specialized functions. We first leverage the in-context
learning ability of large language models to generate reasoning programs to
guide the verification process. Afterward, we execute the program by delegating
each sub-task to the corresponding sub-task handler. This process makes our
model both explanatory and data-efficient, providing clear explanations of its
reasoning process and requiring minimal training data. We evaluate ProgramFC on
two challenging fact-checking datasets and show that it outperforms seven
fact-checking baselines across different settings of evidence availability,
with explicit output programs that benefit human debugging. Our codes and data
are publicly available at https://github.com/mbzuai-nlp/ProgramFC.»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-28T16:34:14+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2011.03088)\]. Further details \[[6](http://arxiv.org/abs/2305.12744)\]\[[7](http://arxiv.org/abs/2310.05253)\]\[[8](http://arxiv.org/abs/2305.06590)\]\[[9](http://arxiv.org/abs/2310.01061)\]\[[10](https://aclanthology.org/2022.acl-long.354/)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Integrating knowledge graphs (KGs) to enhance the reasoning capabilities of
large language models (LLMs) is an emerging research challenge in claim
verification. While KGs provide structured, semantically rich representations
well-suited for reasoning, most existing verification methods rely on
unstructured text corpora, limiting their ability to effectively leverage KGs.
Additionally, despite possessing strong reasoning abilities, modern LLMs
struggle with multi-step modular pipelines and reasoning over KGs without
adaptation. To address these challenges, we propose ClaimPKG, an end-to-end
framework that seamlessly integrates LLM reasoning with structured knowledge
from KGs. Specifically, the main idea of ClaimPKG is to employ a lightweight,
specialized LLM to represent the input claim as pseudo-subgraphs, guiding a
dedicated subgraph retrieval module to identify relevant KG subgraphs. These
retrieved subgraphs are then processed by a general-purpose LLM to produce the
final verdict and justification. Extensive experiments on the FactKG dataset
demonstrate that ClaimPKG achieves state-of-the-art performance, outperforming
strong baselines in this research field by 9%-12% accuracy points across
multiple categories. Furthermore, ClaimPKG exhibits zero-shot generalizability
to unstructured datasets such as HoVer and FEVEROUS, effectively combining
structured knowledge from KGs with LLM reasoning across various LLM backbones.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2011.03088)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2103.08541)\]\[[7](http://arxiv.org/abs/2310.05253)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer:
Subtask decomposition in fact-checking has emerged as a promising approach to enhance the efficiency and explainability of verification processes \[[6](http://arxiv.org/abs/2305.12744)\]. This method involves breaking down complex claims into simpler, manageable sub-tasks that can be addressed using specialized functions, thereby enabling more structured and transparent reasoning \[[6](http://arxiv.org/abs/2305.12744)\]. By leveraging the in-context learning capabilities of large language models, these models generate reasoning programs that guide the verification process, allowing for the delegation of specific sub-tasks to dedicated handlers \[[6](http://arxiv.org/abs/2305.12744)\]. This modular approach not only improves data efficiency but also facilitates human debugging through explicit output programs \[[6](http://arxiv.org/abs/2305.12744)\]. The integration of such subtask decomposition techniques with knowledge graphs and LLMs, as seen in frameworks like ClaimPKG, highlights the potential for combining structured reasoning with flexible, large-scale language models to address the limitations of traditional fact-checking methods \[[6](http://arxiv.org/abs/2305.12744)\].
|    | reference                                                                                     |   date | key idea/summary                                                                                                                                                                                                                       |
|----|-----------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Fact-Checking Complex Claims with Program-Guided Reasoning](http://arxiv.org/abs/2305.12744) |    nan | Program-Guided Fact-Checking (ProgramFC) is a novel fact-checking model that decomposes complex claims into sub-tasks using specialized functions and in-context learning, improving data efficiency and providing clear explanations. |
### <a id='category-kg-integration-in-fact-verification'></a>KG Integration in Fact Verification: 1 papers found.
Context: 
	Document 1: [Category]: «KG Integration in Fact Verification»
[_citation_number]: «8»
[Snippet]: «In real world applications, knowledge graphs (KG) are widely used in various
domains (e.g. medical applications and dialogue agents). However, for fact
verification, KGs have not been adequately utilized as a knowledge source. KGs
can be a valuable knowledge source in fact verification due to their
reliability and broad applicability. A KG consists of nodes and edges which
makes it clear how concepts are linked together, allowing machines to reason
over chains of topics. However, there are many challenges in understanding how
these machine-readable concepts map to information in text. To enable the
community to better use KGs, we introduce a new dataset, FactKG: Fact
Verification via Reasoning on Knowledge Graphs. It consists of 108k natural
language claims with five types of reasoning: One-hop, Conjunction, Existence,
Multi-hop, and Negation. Furthermore, FactKG contains various linguistic
patterns, including colloquial style claims as well as written style claims to
increase practicality. Lastly, we develop a baseline approach and analyze
FactKG over these reasoning types. We believe FactKG can advance both
reliability and practicality in KG-based fact verification.»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-28T16:34:14+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2011.03088)\]. Further details \[[6](http://arxiv.org/abs/2305.12744)\]\[[7](http://arxiv.org/abs/2310.05253)\]\[[8](http://arxiv.org/abs/2305.06590)\]\[[9](http://arxiv.org/abs/2310.01061)\]\[[10](https://aclanthology.org/2022.acl-long.354/)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Integrating knowledge graphs (KGs) to enhance the reasoning capabilities of
large language models (LLMs) is an emerging research challenge in claim
verification. While KGs provide structured, semantically rich representations
well-suited for reasoning, most existing verification methods rely on
unstructured text corpora, limiting their ability to effectively leverage KGs.
Additionally, despite possessing strong reasoning abilities, modern LLMs
struggle with multi-step modular pipelines and reasoning over KGs without
adaptation. To address these challenges, we propose ClaimPKG, an end-to-end
framework that seamlessly integrates LLM reasoning with structured knowledge
from KGs. Specifically, the main idea of ClaimPKG is to employ a lightweight,
specialized LLM to represent the input claim as pseudo-subgraphs, guiding a
dedicated subgraph retrieval module to identify relevant KG subgraphs. These
retrieved subgraphs are then processed by a general-purpose LLM to produce the
final verdict and justification. Extensive experiments on the FactKG dataset
demonstrate that ClaimPKG achieves state-of-the-art performance, outperforming
strong baselines in this research field by 9%-12% accuracy points across
multiple categories. Furthermore, ClaimPKG exhibits zero-shot generalizability
to unstructured datasets such as HoVer and FEVEROUS, effectively combining
structured knowledge from KGs with LLM reasoning across various LLM backbones.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2011.03088)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2103.08541)\]\[[7](http://arxiv.org/abs/2310.05253)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
The integration of knowledge graphs (KGs) into fact verification has gained increasing attention due to their ability to provide structured, semantically rich representations that facilitate reasoning over complex relationships \[[8](http://arxiv.org/abs/2305.06590)\]. KGs, composed of nodes and edges, enable machines to understand how concepts are interconnected, offering a clear framework for reasoning about chains of topics \[[8](http://arxiv.org/abs/2305.06590)\]. Despite their potential, KGs have not been widely utilized in fact verification tasks, where most approaches rely on unstructured text corpora, limiting their ability to leverage the structured knowledge available in KGs \[[8](http://arxiv.org/abs/2305.06590)\]. To address this gap, recent work has introduced datasets like FactKG, which includes 108k natural language claims with various reasoning types, including one-hop, conjunction, existence, multi-hop, and negation \[[8](http://arxiv.org/abs/2305.06590)\]. These datasets aim to enhance the practicality and reliability of KG-based fact verification by incorporating diverse linguistic patterns, such as colloquial and written styles \[[8](http://arxiv.org/abs/2305.06590)\]. This highlights the growing interest in utilizing KGs for fact verification and the need for frameworks that can effectively bridge the gap between structured knowledge and natural language reasoning.
|    | reference                                                                                      |   date | key idea/summary                                                                                                                                                                                                                                        |
|----|------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [FactKG: Fact Verification via Reasoning on Knowledge Graphs](http://arxiv.org/abs/2305.06590) |    nan | The paper introduces FactKG, a new dataset for fact verification using knowledge graphs, which includes 108k claims with various reasoning types and linguistic patterns, aiming to improve reliability and practicality in KG-based fact verification. |
### <a id='category-reasoning-frameworks-for-llms'></a>Reasoning Frameworks for LLMs: 1 papers found.
Context: 
	Document 1: [Category]: «Reasoning Frameworks for LLMs»
[_citation_number]: «12»
[Snippet]: «»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-28T16:34:14+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2011.03088)\]. Further details \[[6](http://arxiv.org/abs/2305.12744)\]\[[7](http://arxiv.org/abs/2310.05253)\]\[[8](http://arxiv.org/abs/2305.06590)\]\[[9](http://arxiv.org/abs/2310.01061)\]\[[10](https://aclanthology.org/2022.acl-long.354/)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Integrating knowledge graphs (KGs) to enhance the reasoning capabilities of
large language models (LLMs) is an emerging research challenge in claim
verification. While KGs provide structured, semantically rich representations
well-suited for reasoning, most existing verification methods rely on
unstructured text corpora, limiting their ability to effectively leverage KGs.
Additionally, despite possessing strong reasoning abilities, modern LLMs
struggle with multi-step modular pipelines and reasoning over KGs without
adaptation. To address these challenges, we propose ClaimPKG, an end-to-end
framework that seamlessly integrates LLM reasoning with structured knowledge
from KGs. Specifically, the main idea of ClaimPKG is to employ a lightweight,
specialized LLM to represent the input claim as pseudo-subgraphs, guiding a
dedicated subgraph retrieval module to identify relevant KG subgraphs. These
retrieved subgraphs are then processed by a general-purpose LLM to produce the
final verdict and justification. Extensive experiments on the FactKG dataset
demonstrate that ClaimPKG achieves state-of-the-art performance, outperforming
strong baselines in this research field by 9%-12% accuracy points across
multiple categories. Furthermore, ClaimPKG exhibits zero-shot generalizability
to unstructured datasets such as HoVer and FEVEROUS, effectively combining
structured knowledge from KGs with LLM reasoning across various LLM backbones.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2011.03088)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2103.08541)\]\[[7](http://arxiv.org/abs/2310.05253)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer:  
The category "Reasoning Frameworks for LLMs" focuses on the integration of large language models (LLMs) with structured knowledge sources, such as knowledge graphs (KGs), to enhance reasoning capabilities, particularly in claim verification tasks \[[12](https://aclanthology.org/2023.emnlp-main.574/)\]. This area of research addresses the limitations of traditional verification methods that rely on unstructured text corpora, which hinder effective utilization of KGs' semantically rich representations \[[12](https://aclanthology.org/2023.emnlp-main.574/)\]. Recent frameworks, like ClaimPKG, aim to bridge this gap by employing specialized LLMs to generate pseudo-subgraphs from input claims, which are then used to retrieve relevant KG subgraphs \[[12](https://aclanthology.org/2023.emnlp-main.574/)\]. These subgraphs are further processed by general-purpose LLMs to produce final verdicts and justifications, demonstrating the potential of combining structured knowledge with LLM reasoning \[[12](https://aclanthology.org/2023.emnlp-main.574/)\]. Such approaches not only improve accuracy but also enable zero-shot generalizability to unstructured datasets, highlighting the evolving landscape of LLM-based reasoning frameworks \[[12](https://aclanthology.org/2023.emnlp-main.574/)\].
|    | reference                                                                                                                                   |   date | key idea/summary                                                                                          |
|----|---------------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------|
|  0 | [(S)truct(GPT): A General Framework for Large Language Model to Reason over Structured Data](https://aclanthology.org/2023.emnlp-main.574/) |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
