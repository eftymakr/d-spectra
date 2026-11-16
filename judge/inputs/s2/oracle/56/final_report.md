## Related Works

Cross-domain Sequential Recommendation (CDSR) has gained significant attention in recent years due to its ability to leverage user behavior across multiple domains to improve recommendation accuracy. Early approaches primarily focused on single-domain sequential recommendation, where models learned user preferences based on intra-sequence interactions \[[3](http://arxiv.org/abs/2304.03891)\]. However, these methods struggled to generalize across domains, leading to the development of more sophisticated models that incorporate cross-domain information \[[1](http://arxiv.org/abs/2401.04971)\].

A key challenge in CDSR is the overlap dilemma, where existing methods often rely on users with interactions across all domains to learn cross-domain relationships, which limits their practicality \[[1](http://arxiv.org/abs/2401.04971)\]. This issue has been addressed by several recent works that propose methods to capture cross-domain preferences without requiring full domain coverage. For example, the paper by \[[3](http://arxiv.org/abs/2304.03891)\] introduces a framework that integrates intra- and inter-sequence item interactions to jointly learn single- and cross-domain user preferences, thereby improving the modeling of complex transition patterns. Similarly, \[[5](http://arxiv.org/abs/2304.05027)\] presents a framework that jointly models source, target, and mixed behavior sequences to highlight global and target preferences, enhancing the understanding of cross-domain correlations.

Another challenge in CDSR is the transition complexity, which refers to the difficulty of learning complex transition patterns from mixed behavior sequences \[[1](http://arxiv.org/abs/2401.04971)\]. To tackle this, \[[3](http://arxiv.org/abs/2304.03891)\] proposes a method that leverages graph neural networks to mine inter-sequence collaborative relationships and sequential attentive encoders to capture intra-sequence sequential relationships. This dual approach enables the model to better understand the temporal dynamics of user behavior across domains. Additionally, \[[17]()\] introduces a multi-view graph contrastive learning framework that enhances cross-domain representation learning by considering both intra- and inter-domain interactions.

Recent advancements have also explored the integration of large language models (LLMs) into CDSR to address these challenges. LLMs offer powerful representation and reasoning capabilities that can help bridge the gap between items and capture user preferences from a semantic perspective \[[1](http://arxiv.org/abs/2401.04971)\]. For instance, \[[11](http://arxiv.org/abs/2411.14922)\] proposes a framework called GOT4Rec, which utilizes the graph of thoughts (GoT) reasoning strategy to enhance sequential recommendations by leveraging user history for reasoning. This approach allows LLMs to generate more accurate and comprehensive recommendations by considering short-term, long-term, and collaborative information.

Furthermore, \[[12](http://arxiv.org/abs/2305.00447)\] introduces TALLRec, an efficient tuning framework that aligns LLMs with recommendation tasks by fine-tuning them on recommendation data. This method improves the performance of LLMs in recommendation tasks, even with limited datasets. Similarly, \[[13](http://arxiv.org/abs/2406.09215)\] proposes Softmax-D
## Research papers
### Outline
- [Cross-domain Sequential Recommendation (CDSR) Overview [6 papers]](#category-cross-domain-sequential-recommendation-(cdsr)-overview)
- [Overlap Dilemma in CDSR [1 papers]](#category-overlap-dilemma-in-cdsr)
- [Large Language Models (LLMs) in CDSR [9 papers]](#category-large-language-models-(llms)-in-cdsr)
- [Semantic Item Representation via LLMs [2 papers]](#category-semantic-item-representation-via-llms)
- [Graph of Thoughts (GoT) Reasoning in Recommendations [1 papers]](#category-graph-of-thoughts-(got)-reasoning-in-recommendations)
- [Efficient LLM Tuning for Recommendations [1 papers]](#category-efficient-llm-tuning-for-recommendations)
- [Graph Neural Networks in CDSR [2 papers]](#category-graph-neural-networks-in-cdsr)
- [Multi-view Graph Contrastive Learning [1 papers]](#category-multi-view-graph-contrastive-learning)

### <a id='category-cross-domain-sequential-recommendation-(cdsr)-overview'></a>Cross-domain Sequential Recommendation (CDSR) Overview: 6 papers found.
Context: 
	Document 1: [_citation_number]: «1»
[Snippet]: «Cross-domain sequential recommendation (CDSR) shifts the modeling of user
preferences from flat to stereoscopic by integrating and learning interaction
information from multiple domains at different granularities (ranging from
inter-sequence to intra-sequence and from single-domain to cross-domain). In
this survey, we first define the CDSR problem using a four-dimensional tensor
and then analyze its multi-type input representations under multidirectional
dimensionality reductions. Following that, we provide a systematic overview
from both macro and micro views. From a macro view, we abstract the multi-level
fusion structures of various models across domains and discuss their bridges
for fusion. From a micro view, focusing on the existing models, we first
discuss the basic technologies and then explain the auxiliary learning
technologies. Finally, we exhibit the available public datasets and the
representative experimental results as well as provide some insights into
future directions for research in CDSR.»
[Category]: «Cross-domain Sequential Recommendation (CDSR) Overview»

	Document 2: [_citation_number]: «3»
[Snippet]: «Cross-Domain Sequential Recommendation (CDSR) aims to predict future
interactions based on user's historical sequential interactions from multiple
domains. Generally, a key challenge of CDSR is how to mine precise cross-domain
user preference based on the intra-sequence and inter-sequence item
interactions. Existing works first learn single-domain user preference only
with intra-sequence item interactions, and then build a transferring module to
obtain cross-domain user preference. However, such a pipeline and implicit
solution can be severely limited by the bottleneck of the designed transferring
module, and ignores to consider inter-sequence item relationships. In this
paper, we propose C^2DSR to tackle the above problems to capture precise user
preferences. The main idea is to simultaneously leverage the intra- and inter-
sequence item relationships, and jointly learn the single- and cross- domain
user preferences. Specifically, we first utilize a graph neural network to mine
inter-sequence item collaborative relationship, and then exploit sequential
attentive encoder to capture intra-sequence item sequential relationship. Based
on them, we devise two different sequential training objectives to obtain user
single-domain and cross-domain representations. Furthermore, we present a novel
contrastive cross-domain infomax objective to enhance the correlation between
single-
|    | reference                                                                                                                                                   |   date | key idea/summary                                                                                                                                                                                                                                                                              |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [A Survey on Cross-Domain Sequential Recommendation](http://arxiv.org/abs/2401.04971)                                                                       |    nan | Cross-domain sequential recommendation (CDSR) integrates interaction information from multiple domains at various granularities to model user preferences in a stereoscopic manner, with a systematic overview of models, techniques, datasets, and future directions.                        |
|  1 | [Contrastive Cross-Domain Sequential Recommendation](http://arxiv.org/abs/2304.03891)                                                                       |    nan | C^2DSR is a cross-domain sequential recommendation method that simultaneously leverages intra- and inter-sequence item relationships to jointly learn single- and cross-domain user preferences, enhancing the correlation between them through a contrastive cross-domain infomax objective. |
|  2 | [Unbiased and Robust: External Attention-enhanced Graph Contrastive
  Learning for Cross-domain Sequential Recommendation](http://arxiv.org/abs/2310.04633) |    nan | EA-GCL is a novel framework that addresses inter-domain density bias and improves sequential recommendation by integrating external attention mechanisms and self-supervised learning in a graph contrastive learning setting.                                                                |
|  3 | [Triple Sequence Learning for Cross-domain Recommendation](http://arxiv.org/abs/2304.05027)                                                                 |    nan | Tri-CDR is a novel framework for cross-domain recommendation that jointly models source, target, and mixed behavior sequences to enhance user preference modeling by capturing global and target-domain preferences through triple cross-domain attention and contrastive learning.           |
|  4 | [AutoTransfer: Instance transfer for cross-domain recommendations]()                                                                                        |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                     |
|  5 | [$\pi$-net: A parallel information-sharing network for shared-account cross-domain sequential recommendations]()                                            |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                     |
### <a id='category-overlap-dilemma-in-cdsr'></a>Overlap Dilemma in CDSR: 1 papers found.
Context: 
	Document 1: \[[1](http://arxiv.org/abs/2401.04971)\]: «Multi-Domain Recommendation (MDR) has gained significant attention in recent years, which leverages data from multiple domains to enhance their performance concurrently. However, current MDR models are confronted with two limitations. Firstly, the majority of these models adopt an approach that explicitly shares parameters between domains, leading to mutual interference among them. Secondly, due to the distribution differences among domains, the utilization of static parameters in existing methods limits their flexibility to adapt to diverse domains. To address these challenges, we propose a novel model Hyper Adapter for Multi-Domain Recommendation (HAMUR). Specifically, HAMUR consists of two components: (1). Domain-specific adapter, designed as a pluggable module that can be seamlessly integrated into various existing multi-domain backbone models, and (2). Domain-shared hyper-network, which implicitly captures shared information among domains and dynamically generates the parameters for the adapter. We conduct extensive experiments on two public datasets using various backbone networks. The experimental results validate the effectiveness and scalability of the proposed model.»
[Category]: «Overlap Dilemma in CDSR»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-25T14:30:25+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2304.03891)\]. Further details \[[6](http://arxiv.org/abs/2306.05817)\]\[[7](http://arxiv.org/abs/2410.19744)\]\[[8](http://arxiv.org/abs/2409.19925)\]\[[9](http://arxiv.org/abs/2503.12547)\]\[[10](http://arxiv.org/abs/2402.06196)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Cross-domain Sequential Recommendation (CDSR) aims to extract the preference from the user's historical interactions across various domains. Despite some progress in CDSR, two problems set the barrier for further advancements, i.e., overlap dilemma and transition complexity. The former means existing CDSR methods severely rely on users who own interactions on all domains to learn cross-domain item relationships, compromising the practicability. The latter refers to the difficulties in learning the complex transition patterns from the
|    | reference                                                                               |   date | key idea/summary                                                                                                                                                                                                                      |
|----|-----------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [HAMUR: Hyper Adapter for Multi-Domain Recommendation](http://arxiv.org/abs/2309.06217) |    nan | HAMUR is a novel model for Multi-Domain Recommendation that addresses parameter interference and static parameter limitations by using domain-specific adapters and a domain-shared hyper-network to dynamically generate parameters. |
### <a id='category-large-language-models-(llms)-in-cdsr'></a>Large Language Models (LLMs) in CDSR: 9 papers found.
The integration of Large Language Models (LLMs) into Cross-domain Sequential Recommendation (CDSR) has emerged as a promising direction to address the overlap dilemma and transition complexity inherent in existing methods \[[9](http://arxiv.org/abs/2503.12547)\]. Traditional CDSR approaches often rely on users with interactions across all domains, limiting their applicability to real-world scenarios \[[9](http://arxiv.org/abs/2503.12547)\]. LLMs, with their strong semantic understanding and reasoning capabilities, offer a way to bridge items and capture user preferences from a semantic perspective, enabling more effective cross-domain recommendations \[[1](http://arxiv.org/abs/2401.04971)\]. By leveraging LLMs, researchers have proposed frameworks such as LLMSeR, which uses LLMs to generate pseudo-prior items and enhance sequential recommendation through semantic interaction augmentation and adaptive reliability validation \[[3](http://arxiv.org/abs/2304.03891)\]. Additionally, the use of LLMs in CDSR has led to the development of novel training strategies, such as the Softmax-DPO approach, which integrates ranking information into the model to better distinguish preferred items from negatives \[[5](http://arxiv.org/abs/2304.05027)\]. These advancements highlight the potential of LLMs to improve the effectiveness and efficiency of CDSR systems, while also addressing challenges related to data scarcity and model generalization \[[1](http://arxiv.org/abs/2401.04971)\]. The growing body of work in this area underscores the importance of exploring how LLMs can be systematically adapted to the unique requirements of CDSR, including their role in feature engineering, scoring functions, and user interaction \[[1](http://arxiv.org/abs/2401.04971)\].
|    | reference                                                                                                        |   date | key idea/summary                                                                                                                                                                                                                                                                                      |
|----|------------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [How Can Recommender Systems Benefit from Large Language Models: A Survey](http://arxiv.org/abs/2306.05817)      |    nan | This paper presents a comprehensive survey on integrating large language models (LLMs) into recommender systems (RS) by exploring where and how to adapt LLMs across different stages of the recommendation pipeline, while addressing challenges related to efficiency, effectiveness, and ethics.   |
|  1 | [Towards Next-Generation LLM-based Recommender Systems: A Survey and
  Beyond](http://arxiv.org/abs/2410.19744)  |    nan | This survey provides a comprehensive review of recent advances and challenges in LLM-based recommender systems, proposing a novel taxonomy and three-tier structure to enhance the integration of large language models into both academic research and industrial applications.                      |
|  2 | [LLMSeR: Enhancing Sequential Recommendation via LLM-based Data
  Augmentation](http://arxiv.org/abs/2503.12547) |    nan | LLMSeR is an innovative framework that leverages Large Language Models to generate pseudo-prior items for Sequential Recommender Systems, enhancing recommendation accuracy by integrating semantic and collaborative signals while mitigating hallucination through adaptive reliability validation. |
|  3 | [Large Language Models: A Survey](http://arxiv.org/abs/2402.06196)                                               |    nan | This paper provides a comprehensive review of Large Language Models (LLMs), discussing their characteristics, development techniques, datasets, evaluation metrics, and future research directions.                                                                                                   |
|  4 | [On Softmax Direct Preference Optimization for Recommendation](http://arxiv.org/abs/2406.09215)                  |    nan | Softmax-DPO (S-DPO) is a novel approach that integrates ranking information into language models to enhance personalized recommendation performance by effectively leveraging user preference data and optimizing for personalized ranking tasks.                                                     |
|  5 | [Large language models for recommendation: Past, present, and future]()                                          |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                             |
|  6 | [Large language model enhanced recommender systems: Taxonomy, trend, application and future]()                   |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                             |
|  7 | [A Practice-Friendly Two-Stage LLM-Enhanced Paradigm in Sequential Recommendation]()                             |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                             |
|  8 | [Llm-esr: Large language models enhancement for long-tailed sequential recommendation]()                         |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                             |
### <a id='category-semantic-item-representation-via-llms'></a>Semantic Item Representation via LLMs: 2 papers found.
Context: 
	Document 1: [_citation_number]: «8»
[Snippet]: «Sequential Recommender Systems (SRS), which model a user's interaction history to predict the next item of interest, are widely used in various applications. However, existing SRS often struggle with low-popularity items, a challenge known as the long-tail problem. This issue leads to reduced serendipity for users and diminished profits for sellers, ultimately harming the overall system. Large Language Model (LLM) has the ability to capture semantic relationships between items, independent of their popularity, making it a promising solution to this problem. In this paper, we introduce LLMEmb, a novel method leveraging LLM to generate item embeddings that enhance SRS performance. To bridge the gap between general-purpose LLM and the recommendation domain, we propose a Supervised Contrastive Fine-Tuning (SCFT) approach. This approach includes attribute-level data augmentation and a tailored contrastive loss to make LLM more recommendation-friendly. Additionally, we emphasize the importance of integrating collaborative signals into LLM-generated embeddings, for which we propose Recommendation Adaptation Training (RAT). This further refines the embeddings for optimal use in SRS. The LLMEmb-derived embeddings can be seamlessly integrated with any SRS models, underscoring the practical value. Comprehensive experiments conducted on three real-world datasets demonstrate that LLMEmb significantly outperforms existing methods across multiple SRS models. The code for our method is released online https://github.com/Applied-Machine-Learning-Lab/LLMEmb.»
[Category]: «Semantic Item Representation via LLMs»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-25T14:30:25+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2304.03891)\]. Further details \[[6](http://arxiv.org/abs/2306.05817)\]\[[7](http://arxiv.org/abs/2410.19744)\]\[[8](http://arxiv.org/abs/2409.19925)\]\[[9](http://arxiv.org/abs/2503.12547)\]\[[10](http://arxiv.org/abs/2402.06196)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for
|    | reference                                                                                                                         |   date | key idea/summary                                                                                                                                                                                                                                                                           |
|----|-----------------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [LLMEmb: Large Language Model Can Be a Good Embedding Generator for
  Sequential Recommendation](http://arxiv.org/abs/2409.19925) |    nan | LLMEmb is a novel method that leverages Large Language Models to generate item embeddings for Sequential Recommender Systems, addressing the long-tail problem by improving serendipity and performance through supervised contrastive fine-tuning and recommendation adaptation training. |
|  1 | [Enhancing sequential recommendation via llm-based semantic embedding learning]()                                                 |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                  |
### <a id='category-graph-of-thoughts-(got)-reasoning-in-recommendations'></a>Graph of Thoughts (GoT) Reasoning in Recommendations: 1 papers found.
Context: 
	Document 1: [_citation_number]: «11»
[Snippet]: «With their vast open-world knowledge and reasoning abilities, large language
models (LLMs) have become a promising tool for sequential recommendation.
Researchers have explored various methods to harness these capabilities, but
most existing approaches rely on simple input-output prompting, failing to
effectively bridge the gap between LLMs' general knowledge and the specific
needs of recommendation tasks. While reasoning strategies like chain-of-thought
(CoT) have been introduced to enhance performance, they often produce
inaccurate recommendations due to underutilized user preference information and
insufficient reasoning depth. To address these challenges, we propose GOT4Rec,
a novel sequential recommendation method leveraging the graph of thoughts (GoT)
reasoning strategy. Our method focuses on three key types of information in
user histories: short-term interests, long-term interests and collaborative
information from other users. It enables LLMs to reason independently and
generate recommendations, subsequently aggregating results to derive final
items. This method allows LLMs, with enhanced reasoning capabilities, to better
utilize the user sequence information, producing more accurate recommendations
and comprehensive explanations. Extensive experiments on real-world datasets
demonstrate the effectiveness of GOT4Rec, outperforming existing
state-of-the-art baselines with an average improvement of 37.11%. Our code is
available at https://anonymous.4open.science/r/GOT4Rec.»
[Category]: «Graph of Thoughts (GoT) Reasoning in Recommendations»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-25T14:30:25+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2304.03891)\]. Further details \[[6](http://arxiv.org/abs/2306.05817)\]\[[7](http://arxiv.org/abs/2410.19744)\]\[[8](http://arxiv.org/abs/2409.19925)\]\[[9](http://arxiv.org/abs/2503.12547)\]\[[10](http://arxiv.org/abs/2402.06196)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section
|    | reference                                                                                   |   date | key idea/summary                                                                                                                                                                                                       |
|----|---------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [GOT4Rec: Graph of Thoughts for Sequential Recommendation](http://arxiv.org/abs/2411.14922) |    nan | GOT4Rec is a novel sequential recommendation method that leverages graph of thoughts (GoT) reasoning to better utilize user sequence information, improving recommendation accuracy by 37.11% over existing baselines. |
### <a id='category-efficient-llm-tuning-for-recommendations'></a>Efficient LLM Tuning for Recommendations: 1 papers found.
Context: 
	Document 1: [_citation_number]: «12»
[Snippet]: «Large Language Models (LLMs) have demonstrated remarkable performance across
diverse domains, thereby prompting researchers to explore their potential for
use in recommendation systems. Initial attempts have leveraged the exceptional
capabilities of LLMs, such as rich knowledge and strong generalization through
In-context Learning, which involves phrasing the recommendation task as
prompts. Nevertheless, the performance of LLMs in recommendation tasks remains
suboptimal due to a substantial disparity between the training tasks for LLMs
and recommendation tasks, as well as inadequate recommendation data during
pre-training. To bridge the gap, we consider building a Large Recommendation
Language Model by tunning LLMs with recommendation data. To this end, we
propose an efficient and effective Tuning framework for Aligning LLMs with
Recommendation, namely TALLRec. We have demonstrated that the proposed TALLRec
framework can significantly enhance the recommendation capabilities of LLMs in
the movie and book domains, even with a limited dataset of fewer than 100
samples. Additionally, the proposed framework is highly efficient and can be
executed on a single RTX 3090 with LLaMA-7B. Furthermore, the fine-tuned LLM
exhibits robust cross-domain generalization. Our code and data are available at
https://github.com/SAI990323/TALLRec.»
[Category]: «Efficient LLM Tuning for Recommendations»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-25T14:30:25+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2304.03891)\]. Further details \[[6](http://arxiv.org/abs/2306.05817)\]\[[7](http://arxiv.org/abs/2410.19744)\]\[[8](http://arxiv.org/abs/2409.19925)\]\[[9](http://arxiv.org/abs/2503.12547)\]\[[10](http://arxiv.org/abs/2402.06196)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is
|    | reference                                                                                                                                   |   date | key idea/summary                                                                                                                                                                                                           |
|----|---------------------------------------------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [TALLRec: An Effective and Efficient Tuning Framework to Align Large
  Language Model with Recommendation](http://arxiv.org/abs/2305.00447) |    nan | The paper proposes TALLRec, an efficient tuning framework to align Large Language Models (LLMs) with recommendation tasks, significantly improving recommendation performance in movie and book domains with limited data. |
### <a id='category-graph-neural-networks-in-cdsr'></a>Graph Neural Networks in CDSR: 2 papers found.
Context: 
	Document 1: [_citation_number]: «14»
[Snippet]: «»
[Category]: «Graph Neural Networks in CDSR»

	Document 2: [_citation_number]: «16»
[Snippet]: «»
[Category]: «Graph Neural Networks in CDSR»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-25T14:30:25+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2304.03891)\]. Further details \[[6](http://arxiv.org/abs/2306.05817)\]\[[7](http://arxiv.org/abs/2410.19744)\]\[[8](http://arxiv.org/abs/2409.19925)\]\[[9](http://arxiv.org/abs/2503.12547)\]\[[10](http://arxiv.org/abs/2402.06196)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Cross-domain Sequential Recommendation (CDSR) aims to extract the preference
from the user's historical interactions across various domains. Despite some
progress in CDSR, two problems set the barrier for further advancements, i.e.,
overlap dilemma and transition complexity. The former means existing CDSR
methods severely rely on users who own interactions on all domains to learn
cross-domain item relationships, compromising the practicability. The latter
refers to the difficulties in learning the complex transition patterns from the
mixed behavior sequences. With powerful representation and reasoning abilities,
Large Language Models (LLMs) are promising to address these two problems by
bridging the items and capturing the user's preferences from a semantic view.
Therefore, we propose an LLMs Enhanced Cross-domain Sequential Recommendation
model (LLM4CDSR). To obtain the semantic item relationships, we first propose
an LLM-based unified representation module to represent items. Then, a
trainable adapter with contrastive regularization is designed to adapt the CDSR
task. Besides, a hierarchical LLMs profiling module is designed to summarize
user cross-domain preferences. Finally, these two modules are integrated into
the proposed tri-thread framework to derive recommendations. We have conducted
extensive experiments on
|    | reference                                                                             |   date | key idea/summary                                                                                          |
|----|---------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------|
|  0 | [Gromov-wasserstein guided representation learning for cross-domain recommendation]() |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
|  1 | [Graph neural networks in recommender systems: a survey]()                            |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
### <a id='category-multi-view-graph-contrastive-learning'></a>Multi-view Graph Contrastive Learning: 1 papers found.
Context: 
	Document 1: [_citation_number]: «17»
[Snippet]: «»
[Category]: «Multi-view Graph Contrastive Learning»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-25T14:30:25+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2304.03891)\]. Further details \[[6](http://arxiv.org/abs/2306.05817)\]\[[7](http://arxiv.org/abs/2410.19744)\]\[[8](http://arxiv.org/abs/2409.19925)\]\[[9](http://arxiv.org/abs/2503.12547)\]\[[10](http://arxiv.org/abs/2402.06196)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Cross-domain Sequential Recommendation (CDSR) aims to extract the preference
from the user's historical interactions across various domains. Despite some
progress in CDSR, two problems set the barrier for further advancements, i.e.,
overlap dilemma and transition complexity. The former means existing CDSR
methods severely rely on users who own interactions on all domains to learn
cross-domain item relationships, compromising the practicability. The latter
refers to the difficulties in learning the complex transition patterns from the
mixed behavior sequences. With powerful representation and reasoning abilities,
Large Language Models (LLMs) are promising to address these two problems by
bridging the items and capturing the user's preferences from a semantic view.
Therefore, we propose an LLMs Enhanced Cross-domain Sequential Recommendation
model (LLM4CDSR). To obtain the semantic item relationships, we first propose
an LLM-based unified representation module to represent items. Then, a
trainable adapter with contrastive regularization is designed to adapt the CDSR
task. Besides, a hierarchical LLMs profiling module is designed to summarize
user cross-domain preferences. Finally, these two modules are integrated into
the proposed tri-thread framework to derive recommendations. We have conducted
extensive experiments on three public cross-domain datasets, validating the
effectiveness of LLM4CDSR. We have released the code online.
Your job is to write
|    | reference                                                                                        |   date | key idea/summary                                                                                          |
|----|--------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------|
|  0 | [A multi-view graph contrastive learning framework for cross-domain sequential recommendation]() |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
