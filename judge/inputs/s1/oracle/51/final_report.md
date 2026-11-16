## Related Works

Federated Online Learning to Rank (FOLTR) has emerged as a privacy-preserving approach to ranking tasks, where models are trained across decentralized data sources without sharing raw user data \[[10](http://arxiv.org/abs/2401.13410)\]. This paradigm aligns with increasing data privacy concerns and regulatory frameworks such as the General Data Protection Regulation (GDPR), which introduces the "right to be forgotten" \[[10](http://arxiv.org/abs/2401.13410)\]. This right necessitates that users can request the removal of their data contributions from learned models, prompting the development of unlearning methods in federated learning \[[6](http://arxiv.org/abs/2203.07320)\]. 

Unlearning in federated settings is particularly challenging due to the distributed nature of training, where each client trains a local model on their private data and only shares model updates with a central server \[[3](http://arxiv.org/abs/2307.01565)\]. Existing unlearning methods often rely on retraining the global model from scratch or require access to historical parameter updates \[[7](http://arxiv.org/abs/2207.05521)\]. However, these approaches are computationally expensive and may not be feasible in real-time or resource-constrained environments \[[8](http://arxiv.org/abs/2210.10958)\]. 

Recent work has explored efficient unlearning strategies that eliminate a client's contribution without retraining the entire model. For example, \[[7](http://arxiv.org/abs/2207.05521)\] proposes a method that performs local unlearning at the client level and uses the locally unlearned model as initialization for a few rounds of federated learning. This approach avoids the need for global access to data or stored parameter updates, making it more practical for deployment. Similarly, \[[8](http://arxiv.org/abs/2210.10958)\] introduces a method for federated recommendation systems that enables users to remove their contributions by rolling back historical parameter updates and recalibrating the model. This method is inspired by transaction rollback mechanisms in database systems and is designed to be efficient on resource-constrained devices \[[8](http://arxiv.org/abs/2210.10958)\].

In the context of FOLTR, \[[10](http://arxiv.org/abs/2401.13410)\] investigates the effectiveness of unlearning strategies that remove a client's contribution without compromising the global ranker's performance. The paper introduces a method where the client performs a poisoning attack to measure the impact of its contribution, and the unlearning process is evaluated by checking if the attack's effect is reduced \[[10](http://arxiv.org/abs/2401.13410)\]. This approach allows for a verifiable assessment of unlearning success without retraining from scratch \[[10](http://arxiv.org/abs/2401.13410)\].

Additionally, \[[3](http://arxiv.org/abs/2307.01565)\] discusses the challenges of non-IID data in federated learning and how it affects the performance of FOLTR systems. Non-IID data distributions can lead to biased model updates and degrade the effectiveness of federated learning approaches \[[3](http://arxiv.org/abs/2307.01565)\]. This highlights the importance of robust unlearning methods that can handle such data distribution challenges \[[3](http://arxiv.org/abs/2307.01565)\].

Finally, \[[9](http://arxiv.org/abs/2302.02069)\]
## Research papers
### Outline
- [Model Initialization and Retraining [2 papers]](#category-model-initialization-and-retraining)
- [Non-IID Data Challenges in Federated Learning [1 papers]](#category-non-iid-data-challenges-in-federated-learning)
- [Federated Learning and Privacy Preservation [5 papers]](#category-federated-learning-and-privacy-preservation)
- [Unlearning in Federated Settings [6 papers]](#category-unlearning-in-federated-settings)
- [Client-Level Unlearning Methods [1 papers]](#category-client-level-unlearning-methods)

### <a id='category-model-initialization-and-retraining'></a>Model Initialization and Retraining: 2 papers found.
Context: 
	Document 1: [Category]: «Model Initialization and Retraining»
[Snippet]: «Online Learning to Rank (OLTR) methods optimize rankers based on user
interactions. State-of-the-art OLTR methods are built specifically for linear
models. Their approaches do not extend well to non-linear models such as neural
networks. We introduce an entirely novel approach to OLTR that constructs a
weighted differentiable pairwise loss after each interaction: Pairwise
Differentiable Gradient Descent (PDGD). PDGD breaks away from the traditional
approach that relies on interleaving or multileaving and extensive sampling of
models to estimate gradients. Instead, its gradient is based on inferring
preferences between document pairs from user clicks and can optimize any
differentiable model. We prove that the gradient of PDGD is unbiased w.r.t.
user document pair preferences. Our experiments on the largest publicly
available Learning to Rank (LTR) datasets show considerable and significant
improvements under all levels of interaction noise. PDGD outperforms existing
OLTR methods both in terms of learning speed as well as final convergence.
Furthermore, unlike previous OLTR methods, PDGD also allows for non-linear
models to be optimized effectively. Our results show that using a neural
network leads to even better performance at convergence than a linear model. In
summary, PDGD is an efficient and unbiased OLTR approach that provides a better
user experience than previously possible.»
[_citation_number]: «1»

	Document 2: [Category]: «Model Initialization and Retraining»
[Snippet]: «Existing online learning to rank (OL2R) solutions are limited to linear
models, which are incompetent to capture possible non-linear relations between
queries and documents. In this work, to unleash the power of representation
learning in OL2R, we propose to directly learn a neural ranking model from
users' implicit feedback (e.g., clicks) collected on the fly. We focus on
RankNet and LambdaRank, due to their great empirical success and wide adoption
in offline settings, and control the notorious explore-exploit trade-off based
on the convergence analysis of neural networks using neural tangent kernel.
Specifically, in each round of result serving, exploration is only performed on
document pairs where the predicted rank order between the two documents is
uncertain; otherwise, the ranker's predicted order will be followed in result
ranking. We prove that under standard assumptions our OL2R
|    | reference                                                                                            |   date | key idea/summary                                                                                                                                                                                                                                                 |
|----|------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Differentiable Unbiased Online Learning to Rank](http://arxiv.org/abs/1809.08415)                   |    nan | PDGD is an efficient and unbiased Online Learning to Rank approach that enables the optimization of differentiable models, including neural networks, by directly inferring user preferences from clicks and achieving better performance than existing methods. |
|  1 | [Learning Neural Ranking Models Online from Implicit User Feedback](http://arxiv.org/abs/2201.06658) |    nan | This work proposes a neural ranking model for online learning to rank (OL2R) that leverages users' implicit feedback and addresses the explore-exploit trade-off, achieving a logarithmic regret bound.                                                          |
### <a id='category-non-iid-data-challenges-in-federated-learning'></a>Non-IID Data Challenges in Federated Learning: 1 papers found.
Context: 
	Document 1: [Category]: «Non-IID Data Challenges in Federated Learning»
[Snippet]: «In this perspective paper we study the effect of non independent and
identically distributed (non-IID) data on federated online learning to rank
(FOLTR) and chart directions for future work in this new and largely unexplored
research area of Information Retrieval. In the FOLTR process, clients
participate in a federation to jointly create an effective ranker from the
implicit click signal originating in each client, without the need to share
data (documents, queries, clicks). A well-known factor that affects the
performance of federated learning systems, and that poses serious challenges to
these approaches, is that there may be some type of bias in the way data is
distributed across clients. While FOLTR systems are on their own rights a type
of federated learning system, the presence and effect of non-IID data in FOLTR
has not been studied. To this aim, we first enumerate possible data
distribution settings that may showcase data bias across clients and thus give
rise to the non-IID problem. Then, we study the impact of each setting on the
performance of the current state-of-the-art FOLTR approach, the Federated
Pairwise Differentiable Gradient Descent (FPDGD), and we highlight which data
distributions may pose a problem for FOLTR methods. We also explore how common
approaches proposed in the federated learning literature address non-IID issues
in FOLTR. This allows us to unveil new research gaps that, we argue, future
research in FOLTR should consider. This is an important contribution to the
current state of FOLTR field because, for FOLTR systems to be deployed, the
factors affecting their performance, including the impact of non-IID data, need
to be thoroughly understood.»
[_citation_number]: «2»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-19T07:23:46+00:00. Mention them in a separate, numbered reference list at the end and use the reference
|    | reference                                                                                         |   date | key idea/summary                                                                                                                                                                                                                              |
|----|---------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Is Non-IID Data a Threat in Federated Online Learning to Rank?](http://arxiv.org/abs/2204.09272) |    nan | This paper explores the impact of non-IID data on federated online learning to rank (FOLTR) and identifies research gaps, emphasizing the need to understand how data distribution affects FOLTR performance for effective system deployment. |
### <a id='category-federated-learning-and-privacy-preservation'></a>Federated Learning and Privacy Preservation: 5 papers found.
Context: 
	Document 1: [Category]: «Federated Learning and Privacy Preservation»
[Snippet]: «Federated online learning to rank (FOLTR) aims to preserve user privacy by not sharing their searchable data and search interactions, while guaranteeing high search effectiveness, especially in contexts where individual users have scarce training data and interactions. For this, FOLTR trains learning to rank models in an online manner -- i.e. by exploiting users' interactions with the search systems (queries, clicks), rather than labels -- and federatively -- i.e. by not aggregating interaction data in a central server for training purposes, but by training instances of a model on each user device on their own private data, and then sharing the model updates, not the data, across a set of users that have formed the federation. Existing FOLTR methods build upon advances in federated learning. While federated learning methods have been shown effective at training machine learning models in a distributed way without the need of data sharing, they can be susceptible to attacks that target either the system's security or its overall effectiveness. In this paper, we consider attacks on FOLTR systems that aim to compromise their search effectiveness. Within this scope, we experiment with and analyse data and model poisoning attack methods to showcase their impact on FOLTR search effectiveness. We also explore the effectiveness of defense methods designed to counteract attacks on FOLTR systems. We contribute an understanding of the effect of attack and defense methods for FOLTR systems, as well as identifying the key factors influencing their effectiveness.»
[_citation_number]: «3»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-19T07:23:46+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2307.01565)\]. Further details \[[6](http://arxiv.org/abs/2203.07320)\]\[[7](http://arxiv.org/abs/2207.05521)\]\[[8](http://arxiv.org/abs/2210.10958)\]\[[9](http://arxiv.org/abs/2302.02069)\]\[[10](http://arxiv.org/abs/2401.13410)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section.
|    | reference                                                                                                                                         |   date | key idea/summary                                                                                                                                                                                                                              |
|----|---------------------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [An Analysis of Untargeted Poisoning Attack and Defense Methods for
  Federated Online Learning to Rank Systems](http://arxiv.org/abs/2307.01565) |    nan | This paper explores attacks and defense mechanisms for Federated Online Learning to Rank (FOLTR) systems, focusing on maintaining search effectiveness while preserving user privacy through decentralized model training and update sharing. |
|  1 | [Federated online learning to rank with evolution strategies]()                                                                                   |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                     |
|  2 | [Federated online learning to rank with evolution strategies: a reproducibility study]()                                                          |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                     |
|  3 | [Effective and privacy-preserving federated online learning to rank]()                                                                            |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                     |
|  4 | [Manipulating the Byzantine: Optimizing Model Poisoning Attacks and
                  Defenses for Federated Learning]()                          |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                     |
### <a id='category-unlearning-in-federated-settings'></a>Unlearning in Federated Settings: 6 papers found.
The category "Unlearning in Federated Settings" explores the challenges and solutions for enabling models to forget specific data contributions in federated learning (FL) systems, driven by privacy regulations like the "right to be forgotten." Existing unlearning methods in centralized machine learning cannot be directly applied to FL due to its distributed nature and lack of full data access \[[6](http://arxiv.org/abs/2203.07320)\]. To address this, researchers have proposed federated unlearning approaches that aim to remove a client's influence from the global model without requiring full data access or storing historical parameter updates \[[7](http://arxiv.org/abs/2207.05521)\]. One method involves local unlearning at the client followed by a few rounds of federated learning to obtain the unlearned global model, achieving comparable performance to retraining from scratch while being more efficient \[[3](http://arxiv.org/abs/2307.01565)\]. Another approach, inspired by transaction rollback mechanisms, uses historical parameter updates to roll back and recalibrate the model, though storing these updates on resource-constrained devices remains a challenge \[[8](http://arxiv.org/abs/2210.10958)\]. Additionally, some methods leverage knowledge distillation to restore model performance after unlearning, without relying on client participation \[[1](http://arxiv.org/abs/1809.08415)\]. These strategies are evaluated using diverse metrics, including the effectiveness of unlearning and the impact on model utility, with experiments conducted on real-world datasets \[[6](http://arxiv.org/abs/2203.07320)\]\[[7](http://arxiv.org/abs/2207.05521)\]\[[8](http://arxiv.org/abs/2210.10958)\]. The need for rigorous evaluation frameworks has also been emphasized, as current practices often rely on single metrics, leading to potential biases in assessing unlearning success \[[10](http://arxiv.org/abs/2401.13410)\]. Overall, the field is advancing with a focus on balancing data privacy, model performance, and system efficiency in federated settings.
|    | reference                                                                                                                            |   date | key idea/summary                                                                                                                                                                                                                                                                                                       |
|----|--------------------------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Federated Unlearning with Knowledge Distillation](http://arxiv.org/abs/2201.09441)                                                  |    nan | The paper proposes a novel federated unlearning method that allows FL models to forget specific client data contributions without requiring client participation or data access, using historical updates and knowledge distillation.                                                                                  |
|  1 | [The Right to be Forgotten in Federated Learning: An Efficient
  Realization with Rapid Retraining](http://arxiv.org/abs/2203.07320) |    nan | This paper addresses the challenge of machine unlearning in Federated Learning systems, proposing a rapid retraining approach that allows data holders to efficiently erase data samples from a trained model while keeping training data locally.                                                                     |
|  2 | [Federated Unlearning: How to Efficiently Erase a Client in FL?](http://arxiv.org/abs/2207.05521)                                    |    nan | This paper proposes an efficient federated unlearning method that allows erasing a client's influence from a global model by performing local unlearning and retraining with remaining clients, achieving comparable performance to retraining from scratch without requiring global data access or parameter history. |
|  3 | [Federated Unlearning for On-Device Recommendation](http://arxiv.org/abs/2210.10958)                                                 |    nan | The paper introduces FRU, an efficient unlearning method for federated recommendation systems that enables users to remove their contribution from the training process, enhancing privacy and system robustness.                                                                                                      |
|  4 | [Heterogeneous Federated Knowledge Graph Embedding Learning and
  Unlearning](http://arxiv.org/abs/2302.02069)                       |    nan | FedLU is a novel federated learning framework for heterogeneous knowledge graph embedding that addresses data heterogeneity and knowledge forgetting through mutual knowledge distillation and an unlearning method based on cognitive neuroscience.                                                                   |
|  5 | [How to Forget Clients in Federated Online Learning to Rank?](http://arxiv.org/abs/2401.13410)                                       |    nan | This paper proposes an efficient unlearning method for Federated Online Learning to Rank systems, allowing clients to remove their contributions without retraining the global model, validated through experiments on multiple datasets.                                                                              |
### <a id='category-client-level-unlearning-methods'></a>Client-Level Unlearning Methods: 1 papers found.
Context: 
	Document 1: [Category]: «Client-Level Unlearning Methods»
[Snippet]: «»
[_citation_number]: «14»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-19T07:23:46+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2307.01565)\]. Further details \[[6](http://arxiv.org/abs/2203.07320)\]\[[7](http://arxiv.org/abs/2207.05521)\]\[[8](http://arxiv.org/abs/2210.10958)\]\[[9](http://arxiv.org/abs/2302.02069)\]\[[10](http://arxiv.org/abs/2401.13410)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: This paper reports on findings from a comparative study on the effectiveness
and efficiency of federated unlearning strategies within Federated Online
Learning to Rank (FOLTR), with specific attention to systematically analysing
the unlearning capabilities of methods in a verifiable manner.
  Federated approaches to ranking of search results have recently garnered
attention to address users privacy concerns. In FOLTR, privacy is safeguarded
by collaboratively training ranking models across decentralized data sources,
preserving individual user data while optimizing search results based on
implicit feedback, such as clicks.
  Recent legislation introduced across numerous countries is establishing the
so called "the right to be forgotten", according to which services based on
machine learning models like those in FOLTR should provide capabilities that
allow users to remove their own data from those used to train models. This has
sparked the development of unlearning methods, along with evaluation practices
to measure whether unlearning of a user data successfully occurred. Current
evaluation practices are however often controversial, necessitating the use of
multiple metrics for a more comprehensive assessment -- but previous proposals
of unlearning methods only used single evaluation metrics.
  This paper addresses this limitation: our study rigorously assesses the
effectiveness of unlearning strategies in managing both under-unlearning and
over-unlearning scenarios using adapted, and newly proposed evaluation metrics.
Thanks to our detailed analysis, we uncover the strengths and limitations
|    | reference                                                                                  |   date | key idea/summary                                                                                          |
|----|--------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------|
|  0 | [Federaser: Enabling efficient client-level data removal from federated learning models]() |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
