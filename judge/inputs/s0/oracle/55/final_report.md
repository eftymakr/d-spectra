## Related Works

Conversational recommendation systems (CRSs) have gained significant attention due to their ability to interact with users and capture nuanced preferences through multi-turn dialogues \[[1](http://arxiv.org/abs/2007.00194)\]. However, effectively understanding user preferences remains a fundamental challenge, especially when preferences are multifaceted and complex \[[1](http://arxiv.org/abs/2007.00194)\]. Traditional recommendation systems often rely on static user-item interactions and struggle to adapt to dynamic preferences \[[1](http://arxiv.org/abs/2007.00194)\]. In contrast, CRSs enable direct interaction with users, allowing for more accurate preference modeling \[[1](http://arxiv.org/abs/2007.00194)\]. Nevertheless, frequent user involvement can degrade the user experience, necessitating automated solutions for interaction \[[1](http://arxiv.org/abs/2007.00194)\].

To address this, several approaches have been proposed. For instance, \[[2](http://arxiv.org/abs/2005.12979)\] introduces a conversational recommendation framework that unifies attributes and items in the same arm space, enabling seamless exploration-exploitation (EE) trade-offs via Thompson Sampling. This method improves recommendation effectiveness by considering both attributes and items simultaneously, rather than separately \[[2](http://arxiv.org/abs/2005.12979)\]. Similarly, \[[3](http://arxiv.org/abs/2307.11650)\] proposes a framework that addresses the long-tail problem in CRSs by simulating and utilizing balanced datasets, ensuring diverse recommendations even for rarely mentioned items \[[3](http://arxiv.org/abs/2307.11650)\]. This is particularly important as existing datasets often suffer from long-tail issues, leading to over-recommendation of frequent items \[[3](http://arxiv.org/abs/2307.11650)\].

Another key challenge in CRSs is the need for efficient and effective interaction strategies. \[[4](http://arxiv.org/abs/2110.14168)\] introduces a method for conversational recommendation that leverages multi-armed bandit approaches, allowing for real-time personalization of cold-start users by interactively exploring preferences \[[4](http://arxiv.org/abs/2110.14168)\]. However, these methods often model recommendation actions homogeneously, limiting their ability to incorporate interpretable attribute feedback \[[4](http://arxiv.org/abs/2110.14168)\]. In contrast, \[[5](http://arxiv.org/abs/2410.12832)\] proposes a framework that explicitly models user feedback on attributes, leading to more accurate preference capture \[[5](http://arxiv.org/abs/2410.12832)\].

Recent work has also focused on improving the efficiency and effectiveness of CRSs through automated interaction. \[[6](http://arxiv.org/abs/2408.15240)\] introduces a simulated user based on generative reward models, enabling automatic multi-turn interaction with CRSs. This approach allows for the generation of synthetic feedback, which can be used to refine recommendations without requiring frequent user involvement \[[6](http://arxiv.org/abs/2408.15240)\]. The simulated user is designed to provide both coarse-grained and fine-grained feedback, enhancing the accuracy of preference modeling \[[6](http://arxiv.org/abs/2408.15240)\]. Furthermore, \[[7]()\] proposes a method that integrates reward-guided search with beam search to balance effectiveness and efficiency during interaction \[[7]()\].

In addition, \[[8]()\] explores the use of large language models (LLMs) as conversational recommenders, leveraging their ability to generate natural language responses and understand complex user preferences
## Research papers
### Outline
- [Attribute-Based Feedback Modeling [1 papers]](#category-attribute-based-feedback-modeling)
- [Efficient Interaction Strategies [1 papers]](#category-efficient-interaction-strategies)
- [Dataset Long-Tail Problem Addressal [2 papers]](#category-dataset-long-tail-problem-addressal)
- [Large Language Models in CRSs [7 papers]](#category-large-language-models-in-crss)
- [Simulated User Approaches for Automation [1 papers]](#category-simulated-user-approaches-for-automation)

### <a id='category-attribute-based-feedback-modeling'></a>Attribute-Based Feedback Modeling: 1 papers found.
Context: 
	Document 1: [Snippet]: «Traditional recommendation systems estimate user preference on items from past interaction history, thus suffering from the limitations of obtaining fine-grained and dynamic user preference. Conversational recommendation system (CRS) brings revolutions to those limitations by enabling the system to directly ask users about their preferred attributes on items. However, existing CRS methods do not make full use of such advantage -- they only use the attribute feedback in rather implicit ways such as updating the latent user representation. In this paper, we propose Conversational Path Reasoning (CPR), a generic framework that models conversational recommendation as an interactive path reasoning problem on a graph. It walks through the attribute vertices by following user feedback, utilizing the user preferred attributes in an explicit way. By leveraging on the graph structure, CPR is able to prune off many irrelevant candidate attributes, leading to better chance of hitting user preferred attributes. To demonstrate how CPR works, we propose a simple yet effective instantiation named SCPR (Simple CPR). We perform empirical studies on the multi-round conversational recommendation scenario, the most realistic CRS setting so far that considers multiple rounds of asking attributes and recommending items. Through extensive experiments on two datasets Yelp and LastFM, we validate the effectiveness of our SCPR, which significantly outperforms the state-of-the-art CRS methods EAR (arXiv:2002.09102) and CRM (arXiv:1806.03277). In particular, we find that the more attributes there are, the more advantages our method can achieve.»
[Category]: «Attribute-Based Feedback Modeling»
[_citation_number]: «1»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-29T06:37:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2307.11650)\]. Further details \[[6](http://arxiv.org/abs/2408.15240)\]\[[7]()\]\[[8]()\]\[[9]()\]\[[10]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed
|    | reference                                                                                                |   date | key idea/summary                                                                                                                                                                                                                                                           |
|----|----------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Interactive Path Reasoning on Graph for Conversational Recommendation](http://arxiv.org/abs/2007.00194) |    nan | The paper introduces Conversational Path Reasoning (CPR), a framework that models conversational recommendation as an interactive path reasoning problem on a graph, enabling more effective and explicit utilization of user feedback to improve recommendation accuracy. |
### <a id='category-efficient-interaction-strategies'></a>Efficient Interaction Strategies: 1 papers found.
Context: 
	Document 1: [Snippet]: «Static recommendation methods like collaborative filtering suffer from the inherent limitation of performing real-time personalization for cold-start users. Online recommendation, e.g., multi-armed bandit approach, addresses this limitation by interactively exploring user preference online and pursuing the exploration-exploitation (EE) trade-off. However, existing bandit-based methods model recommendation actions homogeneously. Specifically, they only consider the items as the arms, being incapable of handling the item attributes, which naturally provide interpretable information of user's current demands and can effectively filter out undesired items. In this work, we consider the conversational recommendation for cold-start users, where a system can both ask the attributes from and recommend items to a user interactively. This important scenario was studied in a recent work. However, it employs a hand-crafted function to decide when to ask attributes or make recommendations. Such separate modeling of attributes and items makes the effectiveness of the system highly rely on the choice of the hand-crafted function, thus introducing fragility to the system. To address this limitation, we seamlessly unify attributes and items in the same arm space and achieve their EE trade-offs automatically using the framework of Thompson Sampling. Our Conversational Thompson Sampling (ConTS) model holistically solves all questions in conversational recommendation by choosing the arm with the maximal reward to play. Extensive experiments on three benchmark datasets show that ConTS outperforms the state-of-the-art methods Conversational UCB (ConUCB) and Estimation-Action-Reflection model in both metrics of success rate and average number of conversation turns.»
[Category]: «Efficient Interaction Strategies»
[_citation_number]: «2»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-29T06:37:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2307.11650)\]. Further details \[[6](http://arxiv.org/abs/2408.15240)\]\[[7]()\]\[[8]()\]\[[9]()\]\[[10]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use
|    | reference                                                                                                                         |   date | key idea/summary                                                                                                                                                                                                                    |
|----|-----------------------------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Seamlessly Unifying Attributes and Items: Conversational Recommendation
  for Cold-Start Users](http://arxiv.org/abs/2005.12979) |    nan | ConTS improves conversational recommendation for cold-start users by integrating item and attribute exploration-exploitation through Thompson Sampling, outperforming existing methods in success rate and conversation efficiency. |
### <a id='category-dataset-long-tail-problem-addressal'></a>Dataset Long-Tail Problem Addressal: 2 papers found.
Context: 
	Document 1: [Snippet]: «Conversational recommender systems (CRS) aim to provide the recommendation
service via natural language conversations. To develop an effective CRS,
high-quality CRS datasets are very crucial. However, existing CRS datasets
suffer from the long-tail issue, \ie a large proportion of items are rarely (or
even never) mentioned in the conversations, which are called long-tail items.
As a result, the CRSs trained on these datasets tend to recommend frequent
items, and the diversity of the recommended items would be largely reduced,
making users easier to get bored.
  To address this issue, this paper presents \textbf(LOT-CRS), a novel
framework that focuses on simulating and utilizing a balanced CRS dataset (\ie
covering all the items evenly) for improving \textbf(LO)ng-\textbf(T)ail
recommendation performance of CRSs. In our approach, we design two pre-training
tasks to enhance the understanding of simulated conversation for long-tail
items, and adopt retrieval-augmented fine-tuning with label smoothness strategy
to further improve the recommendation of long-tail items. Extensive experiments
on two public CRS datasets have demonstrated the effectiveness and
extensibility of our approach, especially on long-tail recommendation.»
[Category]: «Dataset Long-Tail Problem Addressal»
[_citation_number]: «3»

	Document 2: [Snippet]: «State-of-the-art language models can match human performance on many tasks,
but they still struggle to robustly perform multi-step mathematical reasoning.
To diagnose the failures of current models and support research, we introduce
GSM8K, a dataset of 8.5K high quality linguistically diverse grade school math
word problems. We find that even the largest transformer models fail to achieve
high test performance, despite the conceptual simplicity of this problem
distribution. To increase performance, we propose training verifiers to judge
the correctness of model completions. At test time, we generate many candidate
solutions and select the one ranked highest by the verifier. We demonstrate
that verification significantly improves performance on GSM8K, and we provide
strong empirical evidence that verification scales more effectively with
increased data than a finetuning baseline.»
[Category]: «Dataset Long-Tail Problem Addressal»
[_citation_number]: «4»


Instruction:  You are writing a single subsection of a larger report answering the user's query:
|    | reference                                                                                                  |   date | key idea/summary                                                                                                                                                                                                                     |
|----|------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Alleviating the Long-Tail Problem in Conversational Recommender Systems](http://arxiv.org/abs/2307.11650) |    nan | LOT-CRS is a novel framework designed to improve long-tail recommendation performance in conversational recommender systems by simulating balanced datasets and incorporating retrieval-augmented fine-tuning with label smoothness. |
|  1 | [Training Verifiers to Solve Math Word Problems](http://arxiv.org/abs/2110.14168)                          |    nan | GSM8K is a dataset designed to evaluate and improve the performance of language models in multi-step mathematical reasoning, showing that verification methods significantly enhance model performance.                              |
### <a id='category-large-language-models-in-crss'></a>Large Language Models in CRSs: 7 papers found.
Context: 
	Document 1: [Snippet]: «Reinforcement Learning from Human Feedback (RLHF) has greatly improved the performance of modern Large Language Models (LLMs). The RLHF process is resource-intensive and technically challenging, generally requiring a large collection of human preference labels over model-generated outputs. Reinforcement Learning from AI Feedback (RLAIF) addresses this data collection challenge by leveraging synthetic preferences generated by an LLM. However, recent work has shown that synthetic preferences labels may not align well with human preference judgments. To address this, we propose a hybrid approach that unifies RLHF and RLAIF methodologies. We introduce GenRM, an iterative algorithm that trains an LLM on self-generated reasoning traces, leading to synthetic preference labels matching human preference judgments. Empirically, we show that zero-shot LLM-based judgments under-perform compared to Bradley-Terry reward models on in-distribution tasks (between 9-36%). In contrast, GenRM achieves in-distribution accuracy comparable to Bradley-Terry models, while significantly outperforming them on out-of-distribution tasks (between 10-45%). Moreover, GenRM surpasses the performance of using LLMs as judges on both in-distribution (by 9-31%) and out-of-distribution tasks (by 2-6%). Our results show that combining the strengths of RLHF and RLAIF offers a promising approach for improving the quality of synthetic preference labels.»
[Category]: «Large Language Models in CRSs»
[_citation_number]: «5»

	Document 2: [Snippet]: «Verifiers or reward models are often used to enhance the reasoning performance of large language models (LLMs). A common approach is the Best-of-N method, where N candidate solutions generated by the LLM are ranked by a verifier, and the best one is selected. While LLM-based verifiers are typically trained as discriminative classifiers to score solutions, they do not utilize the text generation capabilities of pretrained LLMs. To overcome this limitation, we instead propose training verifiers using the ubiquitous next-token prediction objective, jointly on verification and solution generation. Compared to standard verifiers, such generative verifiers (GenRM) can benefit from several advantages of LLMs: they integrate seamlessly with instruction tuning, enable chain-of-thought reasoning, and can utilize additional test-time compute via majority voting for better verification. We demonstrate that GenRM outperforms discriminative, DPO verifiers, and LLM-as-a-Judge
|    | reference                                                                                                 |   date | key idea/summary                                                                                                                                                                                                                                                                                         |
|----|-----------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Generative Reward Models](http://arxiv.org/abs/2410.12832)                                               |    nan | GenRM is a hybrid approach combining RLHF and RLAIF that improves the quality of synthetic preference labels by training LLMs on self-generated reasoning traces, achieving better performance than both human judgments and Bradley-Terry models on both in-distribution and out-of-distribution tasks. |
|  1 | [Generative Verifiers: Reward Modeling as Next-Token Prediction](http://arxiv.org/abs/2408.15240)         |    nan | The paper introduces generative verifiers (GenRM) trained using next-token prediction, which outperform discriminative verifiers by integrating LLMs' generation capabilities, leading to significant performance gains in Best-of-N methods on various tasks.                                           |
|  2 | [Estimation-action-reflection: Towards deep interaction between conversational and recommender systems]() |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                                |
|  3 | [Towards unified conversational recommender systems via knowledge-enhanced prompt learning]()             |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                                |
|  4 | [Broadening the view: Demonstration-augmented prompt learning for conversational recommendation]()        |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                                |
|  5 | [Large language models as zero-shot conversational recommenders]()                                        |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                                |
|  6 | [Unleashing the Retrieval Potential of Large Language Models in Conversational Recommender Systems]()     |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                                |
### <a id='category-simulated-user-approaches-for-automation'></a>Simulated User Approaches for Automation: 1 papers found.
Context: 
	Document 1: [Snippet]: «»
[Category]: «Simulated User Approaches for Automation»
[_citation_number]: «9»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-29T06:37:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2307.11650)\]. Further details \[[6](http://arxiv.org/abs/2408.15240)\]\[[7]()\]\[[8]()\]\[[9]()\]\[[10]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Conversational recommendation systems (CRSs) use multi-turn interaction to
capture user preferences and provide personalized recommendations. A
fundamental challenge in CRSs lies in effectively understanding user
preferences from conversations. User preferences can be multifaceted and
complex, posing significant challenges for accurate recommendations even with
access to abundant external knowledge. While interaction with users can clarify
their true preferences, frequent user involvement can lead to a degraded user
experience.
  To address this problem, we propose a generative reward model based simulated
user, named GRSU, for automatic interaction with CRSs. The simulated user
provides feedback to the items recommended by CRSs, enabling them to better
capture intricate user preferences through multi-turn interaction. Inspired by
generative reward models, we design two types of feedback actions for the
simulated user: i.e., generative item scoring, which offers coarse-grained
feedback, and attribute-based item critique, which provides fine-grained
feedback. To ensure seamless integration, these feedback actions are unified
into an instruction-based format, allowing the development of a unified
simulated user via instruction tuning on synthesized data. With this simulated
user, automatic multi-turn interaction with CRSs can be effectively conducted.
Furthermore, to strike a balance between effectiveness and efficiency, we draw
inspiration from the paradigm of reward-guided search in complex reasoning
tasks and employ beam search for
|    | reference                                                                              |   date | key idea/summary                                                                                          |
|----|----------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------|
|  0 | [Improving conversational recommendation systems via counterfactual data simulation]() |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
