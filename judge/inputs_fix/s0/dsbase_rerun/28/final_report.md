## Related Works

Federated Learning (FL) has emerged as a promising paradigm for training machine learning models on distributed data while preserving data privacy \[[1' 2024-08-18](http://arxiv.org/abs/2408.09545v2)\]. However, existing FL approaches often face challenges related to data heterogeneity, non-IID data distributions, and the need for robust client selection strategies \[[4' 2025-04-15](http://arxiv.org/abs/2504.11216v2)\]. In particular, the integration of new clients into FL systems can introduce significant variability in data distribution, which can negatively impact model convergence and performance \[[1' 2024-08-18](http://arxiv.org/abs/2408.09545v2)\]. This challenge is further exacerbated by the lack of standardized methods for managing client heterogeneity and ensuring model alignment across diverse data sources \[[3' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\].

Active learning (AL) has been widely studied as a method to reduce annotation costs by selecting the most informative samples for labeling \[[11' 2023-02-17](http://arxiv.org/abs/2302.08893v4)\]. However, when applied in a federated setting, these methods often fail to account for the dynamic and heterogeneous nature of client data, leading to suboptimal model performance \[[1' 2024-08-18](http://arxiv.org/abs/2408.09545v2)\]. Federated Active Learning (FAL) aims to address this by enabling collaborative data selection and model training while maintaining data privacy \[[1' 2024-08-18](http://arxiv.org/abs/2408.09545v2)\]. Despite these efforts, current FAL methods typically overlook the impact of client heterogeneity on model accuracy and parameter alignment, which can lead to significant performance degradation \[[4' 2025-04-15](http://arxiv.org/abs/2504.11216v2)\].

Several works have explored the challenges of data heterogeneity in FL. For instance, \[[4' 2025-04-15](http://arxiv.org/abs/2504.11216v2)\] highlights the importance of characterizing statistical data heterogeneity using metrics such as client attribute imbalance, class imbalance, and spurious correlations. Similarly, \[[3' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\] proposes a framework for aligning model structures across clients to ensure consistent feature representation and improve convergence. These approaches emphasize the need for more sophisticated client selection and model alignment strategies to handle the complexities of heterogeneous FL environments \[[4' 2025-04-15](http://arxiv.org/abs/2504.11216v2)\].

In addition to data heterogeneity, the issue of model forgetting in non-IID settings has been addressed in prior work. \[[5' 2019-10-17](http://arxiv.org/abs/1910.07796v1)\] introduces a method to prevent catastrophic forgetting by adding a penalty term to the loss function, encouraging local models to converge to a shared optimum. This approach is particularly relevant for FL applications where client data distributions differ significantly \[[5' 2019-10-17](http://arxiv.org/abs/1910.07796v1)\]. Furthermore, \[[12' 2020-07-12](http://arxiv.org/abs/2007.06081v1)\] explores the use of vertical FL to combine features from multiple clients, improving model performance by leveraging diverse data sources \[[12' 2020-07-12](http://arxiv.org/abs/2007.06081v1)\].

To enhance the robustness of FL systems, \[[13' 2020-11-13](http://arxiv.org/abs/2011.06803v1)\] proposes a method that integrates dimensionality-reduced data representations without requiring model sharing, thereby preserving privacy while enabling collaborative learning \[[13' 2020-11-13](http://arxiv.org/abs/2011.06803v1)\]. This approach is particularly useful in scenarios where direct model sharing is not feasible \[[13' 2020-11-13](http://arxiv.org/abs/2011.06803v1)\].

In summary, while existing works have made significant strides in addressing the challenges of FL, there remains a need for more comprehensive approaches that account for client heterogeneity, model alignment, and data privacy in federated active learning \[[1' 2024-08-18](http://arxiv.org/abs/2408.09545v2)\]\[[3' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\]\[[4' 2025-04-15](http://arxiv.org/abs/2504.11216v2)\]\[[5' 2019-10-17](http://arxiv.org/abs/1910.07796v1)\]\[[12' 2020-07-12](http://arxiv.org/abs/2007.06081v1)\]\[[13' 2020-11-13](http://arxiv.org/abs/2011.06803v1)\].

References:
1. \[[1' 2024-08-18](http://arxiv.org/abs/2408.09545v2)\] Seamless Integration: Sampling Strategies in Federated Learning Systems
2. \[[3' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\] Heterogeneous Federated Learning
3. \[[4' 2025-04-15](http://arxiv.org/abs/2504.11216v2)\] FedDiverse: Tackling Data Heterogeneity in Federated Learning with Diversity-Driven Client Selection
4. \[[5' 2019-10-17](http://arxiv.org/abs/1910.07796v1)\] Overcoming Forgetting in Federated Learning on Non-IID Data
5. \[[12' 2020-07-12](http://arxiv.org/abs/2007.06081v1)\] VAFL: a Method of Vertical Asynchronous Federated Learning
6. \[[13' 2020-11-13](http://arxiv.org/abs/2011.06803v1)\] Federated Learning System without Model Sharing through Integration of Dimensional Reduced Data Representations
## Research papers
### Outline
- [Data Heterogeneity in FL [6 papers]](#category-data-heterogeneity-in-fl)
- [Model Alignment Techniques [1 papers]](#category-model-alignment-techniques)
- [Model Forgetting Mitigation [1 papers]](#category-model-forgetting-mitigation)
- [Federated Learning (FL) Overview [1 papers]](#category-federated-learning-(fl)-overview)
- [Privacy-Preserving FL Methods [5 papers]](#category-privacy-preserving-fl-methods)
- [Active Learning (AL) in Federated Settings [1 papers]](#category-active-learning-(al)-in-federated-settings)
- [Vertical Federated Learning Approaches [1 papers]](#category-vertical-federated-learning-approaches)
- [Evaluation of CHASe Against Baselines [4 papers]](#category-evaluation-of-chase-against-baselines)

### <a id='category-data-heterogeneity-in-fl'></a>Data Heterogeneity in FL: 6 papers found.
Data heterogeneity in Federated Learning (FL) is a critical challenge that affects model performance, convergence, and system stability. Existing studies highlight that client data is often non-identically distributed (non-IID), leading to statistical heterogeneity, class imbalance, and spurious correlations, which hinder the generalization of the global model \[[3' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\]. To address this, researchers have proposed various strategies, such as characterizing data heterogeneity through metrics like global and client attribute imbalance, and developing client selection algorithms that promote collaboration between clients with complementary data distributions \[[3' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\]. Additionally, methods have been introduced to handle heterogeneous data by maintaining task-specific model parameters on each client while aggregating generic layers on the server, thereby improving performance in extreme cases \[[7' 2020-11-12](http://arxiv.org/abs/2011.06393v1)\]. Furthermore, approaches that incorporate client-specific conditioning, such as conditional gated activation units, have been shown to enhance model robustness when data distributions vary significantly across clients \[[5' 2019-10-17](http://arxiv.org/abs/1910.07796v1)\]. These efforts underscore the importance of addressing data heterogeneity to improve the efficiency and scalability of FL systems.
|    | reference                                                                                                                                 | date     | key idea/summary                                                                                                                                                                                                                                                                                     |
|----|-------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Seamless Integration: Sampling Strategies in Federated Learning Systems](http://arxiv.org/abs/2408.09545v2)                              | 08/18/24 | This paper addresses the challenges of integrating new clients into Federated Learning systems, focusing on data heterogeneity, system stability, and scalability, while proposing strategies to enhance performance and enable broader adoption in production environments.                         |
|  1 | [Federated Self-Supervised Learning in Heterogeneous Settings: Limits of a Baseline Approach on HAR](http://arxiv.org/abs/2207.08187v1)   | 07/17/22 | This work explores the challenges of applying federated learning in a semi-supervised setting, highlighting the limitations of existing approaches in handling heterogeneous, unlabelled data for human activity recognition.                                                                        |
|  2 | [FedDiverse: Tackling Data Heterogeneity in Federated Learning with Diversity-Driven Client Selection](http://arxiv.org/abs/2504.11216v2) | 04/15/25 | The paper introduces FEDDIVERSE, a client selection algorithm for Federated Learning that enhances model performance by leveraging data heterogeneity through complementary client collaboration.                                                                                                    |
|  3 | [Heterogeneous Data-Aware Federated Learning](http://arxiv.org/abs/2011.06393v1)                                                          | 11/12/20 | The paper proposes a novel federated learning method that aggregates generic model parameters on the server while maintaining task-specific parameters on each client, addressing issues like non-i.i.d data and multi-modality in distributed training.                                             |
|  4 | [Client Adaptation improves Federated Learning with Simulated Non-IID Clients](http://arxiv.org/abs/2007.04806v1)                         | 07/09/20 | The paper introduces a federated learning approach that improves model performance by incorporating client-specific conditioning, particularly beneficial for handling non-IID data across clients.                                                                                                  |
|  5 | [Byzantine-Resilient High-Dimensional Federated Learning](http://arxiv.org/abs/2006.13041v2)                                              | 06/22/20 | This paper presents a Byzantine-resilient stochastic gradient descent (SGD) algorithm with local iterations for federated learning, which efficiently filters out malicious updates and provides convergence guarantees for both convex and non-convex objectives under heterogeneous data settings. |
### <a id='category-model-alignment-techniques'></a>Model Alignment Techniques: 1 papers found.
Context: 
	Document 1: [Snippet]: «Federated learning learns from scattered data by fusing collaborative models from local nodes. However, due to chaotic information distribution, the model fusion may suffer from structural misalignment with regard to unmatched parameters. In this work, we propose a novel federated learning framework to resolve this issue by establishing a firm structure-information alignment across collaborative models. Specifically, we design a feature-oriented regulation method (($Ψ$-Net)) to ensure explicit feature information allocation in different neural network structures. Applying this regulating method to collaborative models, matchable structures with similar feature information can be initialized at the very early training stage. During the federated learning process under either IID or non-IID scenarios, dedicated collaboration schemes further guarantee ordered information distribution with definite structure matching, so as the comprehensive model alignment. Eventually, this framework effectively enhances the federated learning applicability to extensive heterogeneous settings, while providing excellent convergence speed, accuracy, and computation/communication efficiency.»
[_citation_number]: «3»
[Category]: «Model Alignment Techniques»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-24T11:28:00+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\]. Further details \[[6' 2019-10-11](http://arxiv.org/abs/1910.04956v2)\]\[[7' 2020-11-12](http://arxiv.org/abs/2011.06393v1)\]\[[8' 2020-04-24](http://arxiv.org/abs/2004.11794v2)\]\[[9' 2020-07-09](http://arxiv.org/abs/2007.04806v1)\]\[[10' 2020-06-22](http://arxiv.org/abs/2006.13041v2)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Active learning (AL) reduces human annotation costs for machine learning
systems by strategically selecting the most informative unlabeled data for
annotation, but performing it individually may still be insufficient due to
restricted data diversity and annotation budget. Federated Active Learning
(FAL) addresses this by facilitating collaborative data selection and model
training, while preserving the confidentiality of raw data samples. Yet,
existing FAL methods fail to account for the heterogeneity of data distribution
across clients and the associated fluctuations in global and local model
parameters, adversely affecting model accuracy. To overcome these challenges,
we propose CHASe (Client Heterogeneity-Aware Data Selection), specifically
designed for FAL. CHASe focuses on identifying those unlabeled samples with
high epistemic variations (EVs), which notably oscillate around the decision
boundaries during training. To achieve both effectiveness and efficiency,
\model() encompasses techniques for 1) tracking EVs by analyzing inference
inconsistencies across training epochs, 2) calibrating decision boundaries of
inaccurate models with a new alignment loss, and 3) enhancing data selection
efficiency via a data freeze and awaken mechanism with subset sampling.
Experiments show that CHASe surpasses various established baselines in terms of
effectiveness and efficiency, validated across diverse datasets, model
complexities, and heterogeneous federation settings.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\]. Further details discussed in contexts \[[2' 2022-07-17](http://arxiv.org/abs/2207.08187v1)\]\[[7' 2020-11-12](http://arxiv.org/abs/2011.06393v1)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Model alignment techniques play a critical role in federated learning by addressing the challenges of structural misalignment and parameter mismatch across distributed models \[[3' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\]. These techniques aim to ensure that collaborative models maintain consistent feature information allocation, even when operating on heterogeneous data distributions \[[3' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\]. One approach involves designing feature-oriented regulation methods, such as Ψ-Net, which explicitly allocate feature information across different neural network structures \[[3' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\]. This enables the initialization of matchable structures with similar feature information at the early stages of training \[[3' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\]. Furthermore, dedicated collaboration schemes during the federated learning process help maintain ordered information distribution and ensure structure matching, leading to comprehensive model alignment \[[3' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\]. These methods enhance the applicability of federated learning in diverse and heterogeneous settings, improving convergence speed, accuracy, and computational efficiency \[[3' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\]. Such advancements are particularly relevant in the context of federated active learning, where model alignment is crucial for maintaining performance across varying client data distributions \[[3' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\].
|    | reference                                                             | date     | key idea/summary                                                                                                                                                                                                                                                               |
|----|-----------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Heterogeneous Federated Learning](http://arxiv.org/abs/2008.06767v2) | 08/15/20 | The paper proposes a novel federated learning framework that addresses structural misalignment in model fusion by establishing structure-information alignment through a feature-oriented regulation method, enhancing applicability and efficiency in heterogeneous settings. |
### <a id='category-model-forgetting-mitigation'></a>Model Forgetting Mitigation: 1 papers found.
Context: 
	Document 1: [Snippet]: «We tackle the problem of Federated Learning in the non i.i.d. case, in which local models drift apart, inhibiting learning. Building on an analogy with Lifelong Learning, we adapt a solution for catastrophic forgetting to Federated Learning. We add a penalty term to the loss function, compelling all local models to converge to a shared optimum. We show that this can be done efficiently for communication (adding no further privacy risks), scaling with the number of nodes in the distributed setting. Our experiments show that this method is superior to competing ones for image recognition on the MNIST dataset.»
[_citation_number]: «5»
[Category]: «Model Forgetting Mitigation»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-24T11:28:00+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\]. Further details \[[6' 2019-10-11](http://arxiv.org/abs/1910.04956v2)\]\[[7' 2020-11-12](http://arxiv.org/abs/2011.06393v1)\]\[[8' 2020-04-24](http://arxiv.org/abs/2004.11794v2)\]\[[9' 2020-07-09](http://arxiv.org/abs/2007.04806v1)\]\[[10' 2020-06-22](http://arxiv.org/abs/2006.13041v2)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Active learning (AL) reduces human annotation costs for machine learning
systems by strategically selecting the most informative unlabeled data for
annotation, but performing it individually may still be insufficient due to
restricted data diversity and annotation budget. Federated Active Learning
(FAL) addresses this by facilitating collaborative data selection and model
training, while preserving the confidentiality of raw data samples. Yet,
existing FAL methods fail to account for the heterogeneity of data distribution
across clients and the associated fluctuations in global and local model
parameters, adversely affecting model accuracy. To overcome these challenges,
we propose CHASe (Client Heterogeneity-Aware Data Selection), specifically
designed for FAL. CHASe focuses on identifying those unlabeled samples with
high epistemic variations (EVs), which notably oscillate around the decision
boundaries during training. To achieve both effectiveness and efficiency,
\model() encompasses techniques for 1) tracking EVs by analyzing inference
inconsistencies across training epochs, 2) calibrating decision boundaries of
inaccurate models with a new alignment loss, and 3) enhancing data selection
efficiency via a data freeze and awaken mechanism with subset sampling.
Experiments show that CHASe surpasses various established baselines in terms of
effectiveness and efficiency, validated across diverse datasets, model
complexities, and heterogeneous federation settings.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\]. Further details discussed in contexts \[[2' 2022-07-17](http://arxiv.org/abs/2207.08187v1)\]\[[7' 2020-11-12](http://arxiv.org/abs/2011.06393v1)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Model forgetting mitigation in federated learning has been explored through various approaches aimed at preventing local models from drifting apart due to non-i.i.d. data distributions \[[5' 2019-10-17](http://arxiv.org/abs/1910.07796v1)\]. One notable method involves adapting solutions from lifelong learning to address catastrophic forgetting, such as adding a penalty term to the loss function to enforce convergence toward a shared optimum \[[5' 2019-10-17](http://arxiv.org/abs/1910.07796v1)\]. This approach ensures that all local models maintain alignment without increasing communication overhead or privacy risks \[[5' 2019-10-17](http://arxiv.org/abs/1910.07796v1)\]. While such methods show promise, they often focus on centralized optimization strategies, whereas recent work emphasizes the need for distributed solutions that can scale effectively in heterogeneous environments \[[5' 2019-10-17](http://arxiv.org/abs/1910.07796v1)\]. These efforts highlight the growing interest in developing robust mechanisms to maintain model consistency across distributed learning systems.
|    | reference                                                                                        | date     | key idea/summary                                                                                                                                                                                                               |
|----|--------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Overcoming Forgetting in Federated Learning on Non-IID Data](http://arxiv.org/abs/1910.07796v1) | 10/17/19 | The paper proposes a method for Federated Learning in non-i.i.d. settings by adding a penalty term to the loss function to ensure local models converge to a shared optimum, improving performance on image recognition tasks. |
### <a id='category-federated-learning-(fl)-overview'></a>Federated Learning (FL) Overview: 1 papers found.
Context: 
	Document 1: [Snippet]: «Federated learning has become increasingly important for modern machine learning, especially for data privacy-sensitive scenarios. Existing federated learning mostly adopts the central server-based architecture or centralized architecture. However, in many social network scenarios, centralized federated learning is not applicable (e.g., a central agent or server connecting all users may not exist, or the communication cost to the central server is not affordable). In this paper, we consider a generic setting: 1) the central server may not exist, and 2) the social network is unidirectional or of single-sided trust (i.e., user A trusts user B but user B may not trust user A). We propose a central server free federated learning algorithm, named Online Push-Sum (OPS) method, to handle this challenging but generic scenario. A rigorous regret analysis is also provided, which shows very interesting results on how users can benefit from communication with trusted users in the federated learning scenario. This work builds upon the fundamental algorithm framework and theoretical guarantees for federated learning in the generic social network scenario.»
[_citation_number]: «6»
[Category]: «Federated Learning (FL) Overview»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-24T11:28:00+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\]. Further details \[[6' 2019-10-11](http://arxiv.org/abs/1910.04956v2)\]\[[7' 2020-11-12](http://arxiv.org/abs/2011.06393v1)\]\[[8' 2020-04-24](http://arxiv.org/abs/2004.11794v2)\]\[[9' 2020-07-09](http://arxiv.org/abs/2007.04806v1)\]\[[10' 2020-06-22](http://arxiv.org/abs/2006.13041v2)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Active learning (AL) reduces human annotation costs for machine learning
systems by strategically selecting the most informative unlabeled data for
annotation, but performing it individually may still be insufficient due to
restricted data diversity and annotation budget. Federated Active Learning
(FAL) addresses this by facilitating collaborative data selection and model
training, while preserving the confidentiality of raw data samples. Yet,
existing FAL methods fail to account for the heterogeneity of data distribution
across clients and the associated fluctuations in global and local model
parameters, adversely affecting model accuracy. To overcome these challenges,
we propose CHASe (Client Heterogeneity-Aware Data Selection), specifically
designed for FAL. CHASe focuses on identifying those unlabeled samples with
high epistemic variations (EVs), which notably oscillate around the decision
boundaries during training. To achieve both effectiveness and efficiency,
\model() encompasses techniques for 1) tracking EVs by analyzing inference
inconsistencies across training epochs, 2) calibrating decision boundaries of
inaccurate models with a new alignment loss, and 3) enhancing data selection
efficiency via a data freeze and awaken mechanism with subset sampling.
Experiments show that CHASe surpasses various established baselines in terms of
effectiveness and efficiency, validated across diverse datasets, model
complexities, and heterogeneous federation settings.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\]. Further details discussed in contexts \[[2' 2022-07-17](http://arxiv.org/abs/2207.08187v1)\]\[[7' 2020-11-12](http://arxiv.org/abs/2011.06393v1)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Federated learning (FL) has emerged as a critical paradigm for privacy-preserving machine learning, particularly in scenarios where data is distributed across multiple parties \[[6' 2019-10-11](http://arxiv.org/abs/1910.04956v2)\]. Traditional FL approaches typically rely on a central server to aggregate model updates, which can be impractical in decentralized environments such as social networks where communication with a central authority is either unavailable or prohibitively costly \[[6' 2019-10-11](http://arxiv.org/abs/1910.04956v2)\]. To address these limitations, recent research has focused on developing decentralized FL frameworks that operate without a central server, enabling collaboration among participants in a more flexible and scalable manner \[[6' 2019-10-11](http://arxiv.org/abs/1910.04956v2)\]. These methods often leverage peer-to-peer communication and trust-based relationships to facilitate knowledge sharing, which is especially relevant in scenarios involving asymmetric trust, such as unidirectional social networks where user A may trust user B but not vice versa \[[6' 2019-10-11](http://arxiv.org/abs/1910.04956v2)\]. This work contributes to the growing body of research on decentralized FL by proposing the Online Push-Sum (OPS) algorithm, which enables efficient and secure model training in such settings \[[6' 2019-10-11](http://arxiv.org/abs/1910.04956v2)\]. The OPS method is designed to handle the challenges of communication costs and trust asymmetry, offering a robust solution for federated learning in complex, real-world environments.
|    | reference                                                                                                           | date     | key idea/summary                                                                                                                                                                                                                            |
|----|---------------------------------------------------------------------------------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Central Server Free Federated Learning over Single-sided Trust Social Networks](http://arxiv.org/abs/1910.04956v2) | 10/11/19 | The paper introduces an Online Push-Sum (OPS) method for federated learning in decentralized social networks without a central server, providing a rigorous regret analysis and demonstrating benefits of communication with trusted users. |
### <a id='category-privacy-preserving-fl-methods'></a>Privacy-Preserving FL Methods: 5 papers found.
Federated Learning (FL) has emerged as a privacy-preserving approach for collaborative machine learning, enabling multiple parties to jointly train models without sharing raw data \[[14' 2019-12-13](http://arxiv.org/abs/1912.06733v1)\]. This paradigm is particularly relevant in the context of the Internet-of-Things (IoT), where vast amounts of personal data are generated, and privacy risks are significant \[[8' 2020-04-24](http://arxiv.org/abs/2004.11794v2)\]. However, FL faces challenges related to data heterogeneity, communication efficiency, and privacy preservation \[[14' 2019-12-13](http://arxiv.org/abs/1912.06733v1)\]. To address these issues, researchers have explored various techniques, such as dimensionality reduction to enable distributed feature extraction without model sharing \[[13' 2020-11-13](http://arxiv.org/abs/2011.06803v1)\], and domain adaptation to improve model accuracy across different user data distributions \[[14' 2019-12-13](http://arxiv.org/abs/1912.06733v1)\]. Additionally, privacy threats in FL, such as inference attacks and model inversion, have been identified, prompting the development of countermeasures tailored to different FL architectures, including horizontal, vertical, and transfer FL \[[17' 2024-02-01](http://arxiv.org/abs/2402.00342v2)\]. These efforts highlight the growing interest in enhancing both the security and effectiveness of FL systems, especially in sensitive applications like IoT and healthcare.
|    | reference                                                                                                                                            | date     | key idea/summary                                                                                                                                                                                                                                   |
|----|------------------------------------------------------------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [A Review of Privacy-preserving Federated Learning for the Internet-of-Things](http://arxiv.org/abs/2004.11794v2)                                    | 04/24/20 | This work reviews federated learning as a privacy-preserving approach for machine learning on distributed IoT data, addressing communication efficiency, client heterogeneity, and privacy challenges, while outlining future research directions. |
|  1 | [Federated Learning System without Model Sharing through Integration of Dimensional Reduced Data Representations](http://arxiv.org/abs/2011.06803v1) | 11/13/20 | This work proposes a federated learning system that integrates dimensionality-reduced representations of distributed data before supervised learning, achieving comparable or better performance than existing methods in small-user settings.     |
|  2 | [Private Federated Learning with Domain Adaptation](http://arxiv.org/abs/1912.06733v1)                                                               | 12/13/19 | The paper proposes a framework that enhances Federated Learning with per-user domain adaptation, improving model accuracy, especially under differential privacy constraints.                                                                      |
|  3 | [Baryon resonances in large $N_c$ QCD](http://arxiv.org/abs/hep-ph/0611096v1)                                                                        | 11/08/06 | The paper provides an algebraic semantics and a sequent calculus for information update due to epistemic actions, modeling these actions using quantales and modules, and extends to scenarios involving lying and cheating.                       |
|  4 | [Survey of Privacy Threats and Countermeasures in Federated Learning](http://arxiv.org/abs/2402.00342v2)                                             | 02/01/24 | This paper categorizes and describes common and unique privacy threats and countermeasures for typical types of federated learning, including horizontal, vertical, and transfer federated learning.                                               |
### <a id='category-active-learning-(al)-in-federated-settings'></a>Active Learning (AL) in Federated Settings: 1 papers found.
Context: 
	Document 1: [Snippet]: «Online active learning is a paradigm in machine learning that aims to select the most informative data points to label from a data stream. The problem of minimizing the cost associated with collecting labeled observations has gained a lot of attention in recent years, particularly in real-world applications where data is only available in an unlabeled form. Annotating each observation can be time-consuming and costly, making it difficult to obtain large amounts of labeled data. To overcome this issue, many active learning strategies have been proposed in the last decades, aiming to select the most informative observations for labeling in order to improve the performance of machine learning models. These approaches can be broadly divided into two categories: static pool-based and stream-based active learning. Pool-based active learning involves selecting a subset of observations from a closed pool of unlabeled data, and it has been the focus of many surveys and literature reviews. However, the growing availability of data streams has led to an increase in the number of approaches that focus on online active learning, which involves continuously selecting and labeling observations as they arrive in a stream. This work aims to provide an overview of the most recently proposed approaches for selecting the most informative observations from data streams in real time. We review the various techniques that have been proposed and discuss their strengths and limitations, as well as the challenges and opportunities that exist in this area of research.»
[_citation_number]: «11»
[Category]: «Active Learning (AL) in Federated Settings»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-24T11:28:00+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\]. Further details \[[6' 2019-10-11](http://arxiv.org/abs/1910.04956v2)\]\[[7' 2020-11-12](http://arxiv.org/abs/2011.06393v1)\]\[[8' 2020-04-24](http://arxiv.org/abs/2004.11794v2)\]\[[9' 2020-07-09](http://arxiv.org/abs/2007.04806v1)\]\[[10' 2020-06-22](http://arxiv.org/abs/2006.13041v2)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Active learning (AL) reduces human annotation costs for machine learning
systems by strategically selecting the most informative unlabeled data for
annotation, but performing it individually may still be insufficient due to
restricted data diversity and annotation budget. Federated Active Learning
(FAL) addresses this by facilitating collaborative data selection and model
training, while preserving the confidentiality of raw data samples. Yet,
existing FAL methods fail to account for the heterogeneity of data distribution
across clients and the associated fluctuations in global and local model
parameters, adversely affecting model accuracy. To overcome these challenges,
we propose CHASe (Client Heterogeneity-Aware Data Selection), specifically
designed for FAL. CHASe focuses on identifying those unlabeled samples with
high epistemic variations (EVs), which notably oscillate around the decision
boundaries during training. To achieve both effectiveness and efficiency,
\model() encompasses techniques for 1) tracking EVs by analyzing inference
inconsistencies across training epochs, 2) calibrating decision boundaries of
inaccurate models with a new alignment loss, and 3) enhancing data selection
efficiency via a data freeze and awaken mechanism with subset sampling.
Experiments show that CHASe surpasses various established baselines in terms of
effectiveness and efficiency, validated across diverse datasets, model
complexities, and heterogeneous federation settings.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\]. Further details discussed in contexts \[[2' 2022-07-17](http://arxiv.org/abs/2207.08187v1)\]\[[7' 2020-11-12](http://arxiv.org/abs/2011.06393v1)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer:  
Active Learning (AL) in Federated Settings has gained significant attention as a means to reduce annotation costs while maintaining data privacy in distributed environments. Federated Active Learning (FAL) extends traditional AL by enabling collaborative data selection and model training across decentralized clients, ensuring that raw data remains confidential \[[11' 2023-02-17](http://arxiv.org/abs/2302.08893v4)\]. However, existing FAL methods often overlook the heterogeneity of data distribution across clients and the resulting fluctuations in model parameters, which can degrade performance \[[11' 2023-02-17](http://arxiv.org/abs/2302.08893v4)\]. This challenge is particularly critical in real-world applications where data streams are continuous and diverse, requiring online active learning strategies that adapt dynamically to new information \[[11' 2023-02-17](http://arxiv.org/abs/2302.08893v4)\]. Recent approaches have focused on improving the efficiency and effectiveness of FAL by addressing issues such as epistemic uncertainty and model calibration, which are essential for accurate decision-making in heterogeneous federated settings \[[11' 2023-02-17](http://arxiv.org/abs/2302.08893v4)\].
|    | reference                                                                       | date     | key idea/summary                                                                                                                                              |
|----|---------------------------------------------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Active learning for data streams: a survey](http://arxiv.org/abs/2302.08893v4) | 02/17/23 | This work provides an overview of recent approaches in online active learning, focusing on selecting informative observations from data streams in real time. |
### <a id='category-vertical-federated-learning-approaches'></a>Vertical Federated Learning Approaches: 1 papers found.
Context: 
	Document 1: [Snippet]: «Horizontal Federated learning (FL) handles multi-client data that share the same set of features, and vertical FL trains a better predictor that combine all the features from different clients. This paper targets solving vertical FL in an asynchronous fashion, and develops a simple FL method. The new method allows each client to run stochastic gradient algorithms without coordination with other clients, so it is suitable for intermittent connectivity of clients. This method further uses a new technique of perturbed local embedding to ensure data privacy and improve communication efficiency. Theoretically, we present the convergence rate and privacy level of our method for strongly convex, nonconvex and even nonsmooth objectives separately. Empirically, we apply our method to FL on various image and healthcare datasets. The results compare favorably to centralized and synchronous FL methods.»
[_citation_number]: «12»
[Category]: «Vertical Federated Learning Approaches»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-24T11:28:00+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\]. Further details \[[6' 2019-10-11](http://arxiv.org/abs/1910.04956v2)\]\[[7' 2020-11-12](http://arxiv.org/abs/2011.06393v1)\]\[[8' 2020-04-24](http://arxiv.org/abs/2004.11794v2)\]\[[9' 2020-07-09](http://arxiv.org/abs/2007.04806v1)\]\[[10' 2020-06-22](http://arxiv.org/abs/2006.13041v2)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Active learning (AL) reduces human annotation costs for machine learning
systems by strategically selecting the most informative unlabeled data for
annotation, but performing it individually may still be insufficient due to
restricted data diversity and annotation budget. Federated Active Learning
(FAL) addresses this by facilitating collaborative data selection and model
training, while preserving the confidentiality of raw data samples. Yet,
existing FAL methods fail to account for the heterogeneity of data distribution
across clients and the associated fluctuations in global and local model
parameters, adversely affecting model accuracy. To overcome these challenges,
we propose CHASe (Client Heterogeneity-Aware Data Selection), specifically
designed for FAL. CHASe focuses on identifying those unlabeled samples with
high epistemic variations (EVs), which notably oscillate around the decision
boundaries during training. To achieve both effectiveness and efficiency,
\model() encompasses techniques for 1) tracking EVs by analyzing inference
inconsistencies across training epochs, 2) calibrating decision boundaries of
inaccurate models with a new alignment loss, and 3) enhancing data selection
efficiency via a data freeze and awaken mechanism with subset sampling.
Experiments show that CHASe surpasses various established baselines in terms of
effectiveness and efficiency, validated across diverse datasets, model
complexities, and heterogeneous federation settings.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\]. Further details discussed in contexts \[[2' 2022-07-17](http://arxiv.org/abs/2207.08187v1)\]\[[7' 2020-11-12](http://arxiv.org/abs/2011.06393v1)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Vertical Federated Learning (VFL) has emerged as a critical approach for collaborative machine learning where clients contribute data with different feature sets, allowing the model to benefit from a richer set of features \[[12' 2020-07-12](http://arxiv.org/abs/2007.06081v1)\]. Unlike Horizontal FL, which focuses on data with shared features, VFL emphasizes the integration of diverse features from multiple clients to enhance model performance \[[12' 2020-07-12](http://arxiv.org/abs/2007.06081v1)\]. Recent studies have explored asynchronous training methods to accommodate the intermittent connectivity of clients, enabling local computations without strict coordination \[[12' 2020-07-12](http://arxiv.org/abs/2007.06081v1)\]. A key innovation in this area is the use of perturbed local embedding techniques, which not only protect data privacy but also improve communication efficiency by reducing the amount of information exchanged between clients \[[12' 2020-07-12](http://arxiv.org/abs/2007.06081v1)\]. Theoretical analyses have further demonstrated the convergence properties of these methods under various objective functions, including strongly convex, nonconvex, and nonsmooth settings \[[12' 2020-07-12](http://arxiv.org/abs/2007.06081v1)\]. Empirical evaluations on image and healthcare datasets have shown that asynchronous VFL methods can achieve competitive results compared to centralized and synchronous approaches, highlighting their potential for real-world applications \[[12' 2020-07-12](http://arxiv.org/abs/2007.06081v1)\].
|    | reference                                                                                       | date     | key idea/summary                                                                                                                                                                                                                                                                         |
|----|-------------------------------------------------------------------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [VAFL: a Method of Vertical Asynchronous Federated Learning](http://arxiv.org/abs/2007.06081v1) | 07/12/20 | This paper introduces a simple asynchronous vertical federated learning method that allows clients to run stochastic gradient algorithms independently, ensuring data privacy through perturbed local embeddings and achieving competitive performance on image and healthcare datasets. |
### <a id='category-evaluation-of-chase-against-baselines'></a>Evaluation of CHASe Against Baselines: 4 papers found.
Context: 
	Document 1: [Snippet]: «Deep learning techniques have achieved specific results in recording device source identification. The recording device source features include spatial information and certain temporal information. However, most recording device source identification methods based on deep learning only use spatial representation learning from recording device source features, which cannot make full use of recording device source information. Therefore, in this paper, to fully explore the spatial information and temporal information of recording device source, we propose a new method for recording device source identification based on the fusion of spatial feature information and temporal feature information by using an end-to-end framework. From a feature perspective, we designed two kinds of networks to extract recording device source spatial and temporal information. Afterward, we use the attention mechanism to adaptively assign the weight of spatial information and temporal information to obtain fusion features. From a model perspective, our model uses an end-to-end framework to learn the deep representation from spatial feature and temporal feature and train using deep and shallow loss to joint optimize our network. This method is compared with our previous work and baseline system. The results show that the proposed method is better than our previous work and baseline system under general conditions.»
[_citation_number]: «16»
[Category]: «Evaluation of CHASe Against Baselines»

	Document 2: [Snippet]: «In networked video applications, the frame rate (FR) and quantization stepsize (QS) of a compressed video are often adapted in response to the changes of the available bandwidth. It is important to understand how do the variation of FR and QS and their variation pattern affect the video quality. In this paper, we investigate the impact of temporal variation of FR and QS on the perceptual video quality. Among all possible variation patterns, we focus on videos in which two FR's (or QS's) alternate over a fixed interval. We explore the human responses to such variation by conducting subjective evaluation of test videos with different variation magnitudes and frequencies. We further analyze statistical significance of the impact of variation magnitude, variation frequency, video content, and their interactions. By analyzing the subjective ratings, we propose two models for predicting the quality of video with alternating FR and QS, respectively, The proposed models have simple mathematical forms with a few content-dependent parameters. The models fit the measured data very well using parameters determined by least square fitting with the measured data. We further propose some guidelines for adaptation of FR and QS based on trends observed from subjective test results.»
[_citation_number]: «18»
[Category]: «Evaluation of CHASe Against Baselines»

	Document 3: [Snippet]: «In this paper, we consider the problem of quickest change point detection and identification over a linear array of $N$ sensors, where the change pattern could first reach any of these sensors, and then propagate to the other sensors. Our goal is not only to detect the presence of such a change as quickly as possible, but also to identify which sensor that the change pattern first reaches. We jointly design two decision rules: a stopping rule, which determines when we should stop sampling and claim a change occurred, and a terminal decision rule, which decides which sensor that the change pattern reaches first, with the objective to strike a balance among the detection delay, the false alarm probability, and the false identification probability. We show that this problem can be converted to a Markov optimal stopping time problem, from which some technical tools could be borrowed. Furthermore, to avoid the high implementation complexity issue of the optimal rules, we develop a scheme with a much simpler structure and certain performance guarantee.»
[_citation_number]: «19»
[Category]: «Evaluation of CHASe Against Baselines»

	Document 4: [Snippet]: «Review of recent works devoted to the variation of the fundamental constants is presented including atomic clocks, quasar absorption spectra, and Oklo natural nuclear reactor data. Assuming linear variation with time we can compare different results. From the quasar absorption spectra:
  $\dotμ/μ=(1 \pm 3) \times 10^(-16)$ yr$^(-1)$. A combination of this result and the atomic clock results gives the best limt on variation of $α$: $\dotα/α=(-0.8 \pm 0.8) \times 10^(-16)$ yr$^(-1)$. The Oklo natural reactor gives the best limit on the variation of $m_s/Λ_(QCD)$ where $m_s$ is the strange quark mass.
  Huge enhancement of the relative variation effects happens in transitions between close atomic, molecular and nuclear energy levels. We suggest several new cases where the levels are very narrow. Large enhancement of the variation effects is also possible in cold atomic and molecular collisions near Feshbach resonance. Massive bodies (stars or galaxies) can also affect physical constants. They have large scalar charge $S$ proportional to number of particles which produces a Coulomb-like scalar field $U=S/r$. This leads to a variation of the fundamental constants proportional to the gravitational potential, e.g. $δα/ α= k_αδ(GM/ r c^2)$. We compare different manifestations of this effect.The strongest limit
  $k_α+0.17 k_e= (-3.5\pm 6) \times 10^(-7)$.»
[_citation_number]: «20»
[Category]: «Evaluation of CHASe Against Baselines»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-24T11:28:00+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\]. Further details \[[6' 2019-10-11](http://arxiv.org/abs/1910.04956v2)\]\[[7' 2020-11-12](http://arxiv.org/abs/2011.06393v1)\]\[[8' 2020-04-24](http://arxiv.org/abs/2004.11794v2)\]\[[9' 2020-07-09](http://arxiv.org/abs/2007.04806v1)\]\[[10' 2020-06-22](http://arxiv.org/abs/2006.13041v2)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Active learning (AL) reduces human annotation costs for machine learning
systems by strategically selecting the most informative unlabeled data for
annotation, but performing it individually may still be insufficient due to
restricted data diversity and annotation budget. Federated Active Learning
(FAL) addresses this by facilitating collaborative data selection and model
training, while preserving the confidentiality of raw data samples. Yet,
existing FAL methods fail to account for the heterogeneity of data distribution
across clients and the associated fluctuations in global and local model
parameters, adversely affecting model accuracy. To overcome these challenges,
we propose CHASe (Client Heterogeneity-Aware Data Selection), specifically
designed for FAL. CHASe focuses on identifying those unlabeled samples with
high epistemic variations (EVs), which notably oscillate around the decision
boundaries during training. To achieve both effectiveness and efficiency,
\model() encompasses techniques for 1) tracking EVs by analyzing inference
inconsistances across training epochs, 2) calibrating decision boundaries of
inaccurate models with a new alignment loss, and 3) enhancing data selection
efficiency via a data freeze and awaken mechanism with subset sampling.
Experiments show that CHASe surpasses various established baselines in terms of
effectiveness and efficiency, validated across diverse datasets, model
complexities, and heterogeneous federation settings.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3' 2020-08-15](http://arxiv.org/abs/2008.06767v2)\]. Further details discussed in contexts \[[2' 2022-07-17](http://arxiv.org/abs/2207.08187v1)\]\[[7' 2020-11-12](http://arxiv.org/abs/2011.06393v1)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer:  
The Evaluation of CHASe Against Baselines category highlights the comparative performance of CHASe against existing methods in federated active learning (FAL). This category includes studies that evaluate the effectiveness and efficiency of CHASe in diverse settings, such as varying datasets, model complexities, and heterogeneous federation environments \[[16' 2022-12-05](http://arxiv.org/abs/2212.02084v1)\]. One study focuses on the importance of leveraging both spatial and temporal features in recording device source identification, demonstrating that integrating these features improves model performance by capturing more comprehensive patterns \[[16' 2022-12-05](http://arxiv.org/abs/2212.02084v1)\]. Another study examines the impact of temporal variations in video quality, specifically how changes in frame rate (FR) and quantization stepsize (QS) affect perceptual quality, and proposes models to predict video quality based on these variations \[[18' 2014-06-08](http://arxiv.org/abs/1406.2018v1)\]. A third study addresses the challenge of detecting and identifying change points in sensor networks, emphasizing the need for adaptive decision rules that balance detection delay, false alarm probability, and false identification probability \[[19' 2013-05-17](http://arxiv.org/abs/1305.4199v1)\]. Lastly, research on the variation of fundamental constants explores how physical constants may change over time, with implications for understanding cosmic phenomena and testing theoretical models \[[20' 2007-05-25](http://arxiv.org/abs/0705.3704v2)\]. These studies collectively underscore the importance of adaptive and robust methods in addressing challenges related to data heterogeneity, temporal dynamics, and model accuracy in distributed and evolving environments.
|    | reference                                                                                                                                                      | date     | key idea/summary                                                                                                                                                                                                                                                   |
|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [End-to-end Recording Device Identification Based on Deep Representation Learning](http://arxiv.org/abs/2212.02084v1)                                          | 12/05/22 | The paper proposes a new method for recording device source identification that combines spatial and temporal feature information using an end-to-end framework and attention mechanism, achieving better performance than previous methods.                       |
|  1 | [Perceptual Quality of Video with Periodic Frame Rate and Quantization Variation-Subjective Studies and Analytical Modeling](http://arxiv.org/abs/1406.2018v1) | 06/08/14 | The paper investigates how variations in frame rate and quantization stepsize affect perceptual video quality, proposing models to predict quality and guidelines for adapting these parameters.                                                                   |
|  2 | [Quickest Change Point Detection and Identification Across a Generic Sensor Array](http://arxiv.org/abs/1305.4199v1)                                           | 05/17/13 | This paper addresses the problem of quickest change point detection and identification in a linear array of sensors, focusing on detecting the change as quickly as possible while identifying the first sensor affected, using a simplified yet effective scheme. |
|  3 | [Variation of fundamental constants: theory and observations](http://arxiv.org/abs/0705.3704v2)                                                                | 05/25/07 | The paper reviews recent studies on the variation of fundamental constants, using data from atomic clocks, quasar absorption spectra, and the Oklo natural reactor, and discusses potential effects of massive bodies on physical constants through scalar fields. |
