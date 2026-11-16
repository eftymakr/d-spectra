## Related Works

Fairness in recommendation systems has gained significant attention due to its implications on both users and item producers. Prior work has identified a trade-off between ranking accuracy and item fairness, with fairness considerations often leading to a decline in user-side accuracy \[[10](http://arxiv.org/abs/2104.09024)\]. This trade-off is analogous to the dynamics of economic transactions, where item-side fairness constraints can be likened to a commodity tax on suppliers, ultimately translating into a cost passed on to consumers \[[1](http://arxiv.org/abs/2205.13619)\]. Similarly, the accuracy-fairness trade-off in re-ranking is governed by the elasticity of utility between item groups, a concept borrowed from economics \[[1](http://arxiv.org/abs/2205.13619)\]. This insight highlights the limitations of current fair re-ranking evaluations, which often rely solely on a single fairness metric, thereby hindering a comprehensive assessment of fair re-ranking algorithms \[[1](http://arxiv.org/abs/2205.13619)\].

Several approaches have been proposed to address fairness in recommendation systems. FairRec \[[11](http://arxiv.org/abs/2201.01180)\] investigates fairness in two-sided platforms, ensuring that both customers and producers receive fair exposure. The algorithm guarantees Maximin Share (MMS) of exposure for most producers and Envy-Free up to One item (EF1) fairness for every customer. While effective, FairRec incurs a marginal loss in overall recommendation quality \[[11](http://arxiv.org/abs/2201.01180)\]. Similarly, CPFair \[[9](http://arxiv.org/abs/2204.08085)\] introduces an optimization-based re-ranking approach that integrates fairness constraints from both consumer and producer sides, demonstrating that fairness can be improved without reducing overall recommendation quality \[[9](http://arxiv.org/abs/2204.08085)\].

FairDiverse \[[2](http://arxiv.org/abs/2502.11883)\] presents a comprehensive toolkit for evaluating fairness and diversity-aware algorithms in information retrieval. It supports the evaluation of 28 fairness and diversity algorithms across 16 base models, covering search and recommendation tasks. This toolkit enables standardized evaluation and comparison of different fairness-aware methods \[[2](http://arxiv.org/abs/2502.11883)\]. The concept of fairness in recommendation has also been explored through the lens of multi-stakeholder systems, where the interests of multiple parties must be considered \[[4](http://arxiv.org/abs/1907.13158)\].

In the context of fair re-ranking, Tax-rank \[[5](http://arxiv.org/abs/2404.17826)\] introduces a new method that leverages a taxation perspective to redistribute ranking slots more equitably. The method ensures continuity and controllability over accuracy loss, offering a superior tax policy for fair re-ranking. Experimental results show that Tax-rank outperforms state-of-the-art baselines in terms of effectiveness and efficiency \[[5](http://arxiv.org/abs/2404.17826)\]. Another approach, VerFair \[[7](http://arxiv.org/abs/2204.03046)\], focuses on exposure fairness in ranking services, proposing a novel algorithm that balances exposure fairness and ranking performance more effectively than existing methods \[[7](http://arxiv.org/abs/2204.03046)\].

In summary, the field of fair re-ranking and recommendation systems has seen a variety of approaches, each
## Research papers
### Outline
- [Exposure Fairness in Recommendation Systems [8 papers]](#category-exposure-fairness-in-recommendation-systems)
- [Standardization of Fairness Evaluation [1 papers]](#category-standardization-of-fairness-evaluation)
- [Multi-Stakeholder Fairness Considerations [5 papers]](#category-multi-stakeholder-fairness-considerations)
- [Taxation-Based Fairness Approaches [2 papers]](#category-taxation-based-fairness-approaches)
- [Fairness Trade-offs in Ranking Systems [1 papers]](#category-fairness-trade-offs-in-ranking-systems)

### <a id='category-exposure-fairness-in-recommendation-systems'></a>Exposure Fairness in Recommendation Systems: 8 papers found.
Context: 
	Document 1: [Category]: «Exposure Fairness in Recommendation Systems»
[Snippet]: «As one of the most pervasive applications of machine learning, recommender
systems are playing an important role on assisting human decision making. The
satisfaction of users and the interests of platforms are closely related to the
quality of the generated recommendation results. However, as a highly
data-driven system, recommender system could be affected by data or algorithmic
bias and thus generate unfair results, which could weaken the reliance of the
systems. As a result, it is crucial to address the potential unfairness
problems in recommendation settings. Recently, there has been growing attention
on fairness considerations in recommender systems with more and more literature
on approaches to promote fairness in recommendation. However, the studies are
rather fragmented and lack a systematic organization, thus making it difficult
to penetrate for new researchers to the domain. This motivates us to provide a
systematic survey of existing works on fairness in recommendation. This survey
focuses on the foundations for fairness in recommendation literature. It first
presents a brief introduction about fairness in basic machine learning tasks
such as classification and ranking in order to provide a general overview of
fairness research, as well as introduce the more complex situations and
challenges that need to be considered when studying fairness in recommender
systems. After that, the survey will introduce fairness in recommendation with
a focus on the taxonomies of current fairness definitions, the typical
techniques for improving fairness, as well as the datasets for fairness studies
in recommendation. The survey also talks about the challenges and opportunities
in fairness research with the hope of promoting the fair recommendation
research area and beyond.»
[_citation_number]: «1»

	Document 2: [Category]: «Exposure Fairness in Recommendation Systems»
[Snippet]: «Conventional Learning-to-Rank (LTR) methods optimize the utility of the
rankings to the users, but they are oblivious to their impact on the ranked
items. However, there has been a growing understanding that the latter is
important to consider for a wide range of ranking applications (e.g. online
marketplaces, job placement, admissions). To address this need, we propose a
general LTR framework that can optimize a wide range of utility metrics (e.g.
NDCG) while satisfying fairness of exposure constraints with respect to the
items. This framework expands the class of learnable ranking functions to
stochastic
|    | reference                                                                                            |   date | key idea/summary                                                                                                                                                                                                                                              |
|----|------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Fairness in Recommendation: Foundations, Methods and Applications](http://arxiv.org/abs/2205.13619) |    nan | This survey provides a systematic overview of fairness considerations in recommender systems, covering foundational concepts, taxonomies of fairness definitions, techniques for improving fairness, datasets, and challenges and opportunities in the field. |
|  1 | [Policy Learning for Fairness in Ranking](http://arxiv.org/abs/1902.04056)                           |    nan | The paper proposes a fair Learning-to-Rank (LTR) framework that optimizes utility metrics like NDCG while ensuring fairness of exposure constraints, using a policy-gradient approach called Fair-PG-Rank.                                                    |
|  2 | [Vertical Allocation-based Fair Exposure Amortizing in Ranking](http://arxiv.org/abs/2204.03046)     |    nan | The paper introduces VerFair, a novel algorithm that balances exposure fairness and ranking performance by leveraging consumer prior knowledge, outperforming existing methods in fairness-performance trade-offs.                                            |
|  3 | [Optimizing generalized Gini indices for fairness in rankings](http://arxiv.org/abs/2204.06521)      |    nan | This paper introduces a fairness-aware recommender system using generalized Gini welfare functions to promote equality among items and users, achieving better trade-offs than existing methods through non-smooth optimization techniques.                   |
|  4 | [Towards Fair Recommendation in Two-Sided Platforms](http://arxiv.org/abs/2201.01180)                |    nan | The paper introduces FairRec, an algorithm that ensures fairness in recommendation systems by balancing exposure for producers and customer satisfaction, while maintaining acceptable recommendation quality.                                                |
|  5 | [A Survey of Research on Fair Recommender Systems]()                                                 |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                     |
|  6 | [P-MMF: Provider Max-min Fairness Re-ranking in Recommender System]()                                |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                     |
|  7 | [Fairness Constraints: A Flexible Approach for Fair Classification]()                                |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                     |
### <a id='category-standardization-of-fairness-evaluation'></a>Standardization of Fairness Evaluation: 1 papers found.
Context: 
	Document 1: [Category]: «Standardization of Fairness Evaluation»
[Snippet]: «In modern information retrieval (IR). achieving more than just accuracy is
essential to sustaining a healthy ecosystem, especially when addressing
fairness and diversity considerations. To meet these needs, various datasets,
algorithms, and evaluation frameworks have been introduced. However, these
algorithms are often tested across diverse metrics, datasets, and experimental
setups, leading to inconsistencies and difficulties in direct comparisons. This
highlights the need for a comprehensive IR toolkit that enables standardized
evaluation of fairness- and diversity-aware algorithms across different IR
tasks. To address this challenge, we present FairDiverse, an open-source and
standardized toolkit. FairDiverse offers a framework for integrating fair and
diverse methods, including pre-processing, in-processing, and post-processing
techniques, at different stages of the IR pipeline. The toolkit supports the
evaluation of 28 fairness and diversity algorithms across 16 base models,
covering two core IR tasks (search and recommendation) thereby establishing a
comprehensive benchmark. Moreover, FairDiverse is highly extensible, providing
multiple APIs that empower IR researchers to swiftly develop and evaluate their
own fairness and diversity aware models, while ensuring fair comparisons with
existing baselines. The project is open-sourced and available on
https://github.com/XuChen0427/FairDiverse.»
[_citation_number]: «2»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-21T09:41:08+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2002.10764)\]. Further details \[[6](http://arxiv.org/abs/1902.04056)\]\[[7](http://arxiv.org/abs/2204.03046)\]\[[8](http://arxiv.org/abs/2204.06521)\]\[[9](http://arxiv.org/abs/2204.08085)\]\[[10](http://arxiv.org/abs/2104.09024)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Fairness is an increasingly important factor in re-ranking tasks. Prior work
has
|    | reference                                                                                                                       |   date | key idea/summary                                                                                                                                                                                                         |
|----|---------------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [FairDiverse: A Comprehensive Toolkit for Fair and Diverse Information
  Retrieval Algorithms](http://arxiv.org/abs/2502.11883) |    nan | FairDiverse is an open-source toolkit designed to standardize the evaluation of fairness- and diversity-aware algorithms in information retrieval, supporting multiple IR tasks and providing a comprehensive benchmark. |
### <a id='category-multi-stakeholder-fairness-considerations'></a>Multi-Stakeholder Fairness Considerations: 5 papers found.
Context: 
	Document 1: [Category]: «Multi-Stakeholder Fairness Considerations»
[Snippet]: «We investigate the problem of fair recommendation in the context of two-sided
online platforms, comprising customers on one side and producers on the other.
Traditionally, recommendation services in these platforms have focused on
maximizing customer satisfaction by tailoring the results according to the
personalized preferences of individual customers. However, our investigation
reveals that such customer-centric design may lead to unfair distribution of
exposure among the producers, which may adversely impact their well-being. On
the other hand, a producer-centric design might become unfair to the customers.
Thus, we consider fairness issues that span both customers and producers. Our
approach involves a novel mapping of the fair recommendation problem to a
constrained version of the problem of fairly allocating indivisible goods. Our
proposed FairRec algorithm guarantees at least Maximin Share (MMS) of exposure
for most of the producers and Envy-Free up to One item (EF1) fairness for every
customer. Extensive evaluations over multiple real-world datasets show the
effectiveness of FairRec in ensuring two-sided fairness while incurring a
marginal loss in the overall recommendation quality.»
[_citation_number]: «3»

	Document 2: [Category]: «Multi-Stakeholder Fairness Considerations»
[Snippet]: «There is growing research interest in recommendation as a multi-stakeholder
problem, one where the interests of multiple parties should be taken into
account. This category subsumes some existing well-established areas of
recommendation research including reciprocal and group recommendation, but a
detailed taxonomy of different classes of multi-stakeholder recommender systems
is still lacking. Fairness-aware recommendation has also grown as a research
area, but its close connection with multi-stakeholder recommendation is not
always recognized. In this paper, we define the most commonly observed classes
of multi-stakeholder recommender systems and discuss how different fairness
concerns may come into play in such systems.»
[_citation_number]: «4»

	Document 3: [Category]: «Multi-Stakeholder Fairness Considerations»
[Snippet]: «Recently, there has been a rising awareness that when machine learning (ML)
algorithms are used to automate choices, they may treat/affect individuals
unfairly, with legal, ethical, or economic consequences. Recommender systems
are prominent examples of such ML systems
|    | reference                                                                                                                    |   date | key idea/summary                                                                                                                                                                                                                                                                          |
|----|------------------------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [FairRec: Two-Sided Fairness for Personalized Recommendations in
  Two-Sided Platforms](http://arxiv.org/abs/2002.10764)     |    nan | The paper introduces FairRec, an algorithm that ensures fair recommendation in two-sided platforms by balancing exposure fairness for producers and satisfaction fairness for customers, achieving MMS for producers and EF1 for customers with minimal impact on recommendation quality. |
|  1 | [Multi-stakeholder Recommendation and its Connection to Multi-sided
  Fairness](http://arxiv.org/abs/1907.13158)             |    nan | The paper defines common classes of multi-stakeholder recommender systems and explores how fairness concerns intersect with these systems.                                                                                                                                                |
|  2 | [CPFair: Personalized Consumer and Producer Fairness Re-ranking for
  Recommender Systems](http://arxiv.org/abs/2204.08085)  |    nan | This work introduces an optimization-based re-ranking approach that integrates fairness constraints from both consumer and producer sides in recommender systems, improving fairness without compromising recommendation quality.                                                         |
|  3 | [TFROM: A Two-sided Fairness-Aware Recommendation Model for Both
  Customers and Providers](http://arxiv.org/abs/2104.09024) |    nan | This paper introduces a two-sided fairness-aware recommendation model (TFROM) that addresses fairness for both customers and providers, ensuring better fairness while maintaining personalization, validated through experiments on real-world datasets.                                 |
|  4 | [Multistakeholder Recommendation: Survey and Research Directions]()                                                          |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                 |
### <a id='category-taxation-based-fairness-approaches'></a>Taxation-Based Fairness Approaches: 2 papers found.
Context: 
	Document 1: [Category]: «Taxation-Based Fairness Approaches»
[Snippet]: «Fair re-ranking aims to redistribute ranking slots among items more equitably to ensure responsibility and ethics. The exploration of redistribution problems has a long history in economics, offering valuable insights for conceptualizing fair re-ranking as a taxation process. Such a formulation provides us with a fresh perspective to re-examine fair re-ranking and inspire the development of new methods. From a taxation perspective, we theoretically demonstrate that most previous fair re-ranking methods can be reformulated as an item-level tax policy. Ideally, a good tax policy should be effective and conveniently controllable to adjust ranking resources. However, both empirical and theoretical analyses indicate that the previous item-level tax policy cannot meet two ideal controllable requirements: (1) continuity, ensuring minor changes in tax rates result in small accuracy and fairness shifts; (2) controllability over accuracy loss, ensuring precise estimation of the accuracy loss under a specific tax rate. To overcome these challenges, we introduce a new fair re-ranking method named Tax-rank, which levies taxes based on the difference in utility between two items. Then, we efficiently optimize such an objective by utilizing the Sinkhorn algorithm in optimal transport. Upon a comprehensive analysis, Our model Tax-rank offers a superior tax policy for fair re-ranking, theoretically demonstrating both continuity and controllability over accuracy loss. Experimental results show that Tax-rank outperforms all state-of-the-art baselines in terms of effectiveness and efficiency on recommendation and advertising tasks.»
[_citation_number]: «5»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-21T09:41:08+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2002.10764)\]. Further details \[[6](http://arxiv.org/abs/1902.04056)\]\[[7](http://arxiv.org/abs/2204.03046)\]\[[8](http://arxiv.org/abs/2204.06521)\]\[[9](http://arxiv.org/abs/2204.08085)\]\[[10](http://arxiv.org/abs/2104.09024)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract
|    | reference                                                                     |   date | key idea/summary                                                                                                                                                                                                                |
|----|-------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [A Taxation Perspective for Fair Re-ranking](http://arxiv.org/abs/2404.17826) |    nan | Tax-rank is a new fair re-ranking method that reformulates fair re-ranking as a taxation process, ensuring continuity and controllability over accuracy loss, and outperforms existing methods in effectiveness and efficiency. |
|  1 | [The Distribution and Redistribution of Income]()                             |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                       |
### <a id='category-fairness-trade-offs-in-ranking-systems'></a>Fairness Trade-offs in Ranking Systems: 1 papers found.
Context: 
	Document 1: [Category]: «Fairness Trade-offs in Ranking Systems»
[Snippet]: «Rankings have become the primary interface in two-sided online markets. Many have noted that the rankings not only affect the satisfaction of the users (e.g., customers, listeners, employers, travelers), but that the position in the ranking allocates exposure -- and thus economic opportunity -- to the ranked items (e.g., articles, products, songs, job seekers, restaurants, hotels). This has raised questions of fairness to the items, and most existing works have addressed fairness by explicitly linking item exposure to item relevance. However, we argue that any particular choice of such a link function may be difficult to defend, and we show that the resulting rankings can still be unfair. To avoid these shortcomings, we develop a new axiomatic approach that is rooted in principles of fair division. This not only avoids the need to choose a link function, but also more meaningfully quantifies the impact on the items beyond exposure. Our axioms of envy-freeness and dominance over uniform ranking postulate that for a fair ranking policy every item should prefer their own rank allocation over that of any other item, and that no item should be actively disadvantaged by the rankings. To compute ranking policies that are fair according to these axioms, we propose a new ranking objective related to the Nash Social Welfare. We show that the solution has guarantees regarding its envy-freeness, its dominance over uniform rankings for every item, and its Pareto optimality. In contrast, we show that conventional exposure-based fairness can produce large amounts of envy and have a highly disparate impact on the items. Beyond these theoretical results, we illustrate empirically how our framework controls the trade-off between impact-based individual item fairness and user utility.»
[_citation_number]: «12»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-21T09:41:08+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2002.10764)\]. Further details \[[6](http://arxiv.org/abs/1902.04056)\]\[[7](http://arxiv.org/abs/2204.03046)\]\[[8](http://arxiv.org/abs/2204.06521)\][9
|    | reference                                                                                                       |   date | key idea/summary                                                                                                                                                                                           |
|----|-----------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Fair Ranking as Fair Division: Impact-Based Individual Fairness in
  Ranking](http://arxiv.org/abs/2206.07247) |    nan | The paper introduces an axiomatic approach to ranking fairness based on principles of fair division, avoiding the need for a link function and ensuring envy-freeness and dominance over uniform rankings. |
