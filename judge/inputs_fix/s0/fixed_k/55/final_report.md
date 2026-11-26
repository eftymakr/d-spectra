## Related Works

Conversational recommendation systems (CRSs) have gained significant attention for their ability to engage users in multi-turn dialogues to infer preferences and provide personalized recommendations \[[16](http://arxiv.org/abs/1806.03277)\]. However, capturing user preferences from conversations remains a fundamental challenge due to the complexity and multifaceted nature of user intent \[[1](http://arxiv.org/abs/2304.13874)\]. Existing approaches often rely on handcrafted reward functions or fail to effectively model the dynamic and evolving nature of user preferences \[[2](http://arxiv.org/abs/2310.20109)\]. Additionally, frequent user involvement can degrade the user experience, making automated interaction a critical area of research \[[1](http://arxiv.org/abs/2304.13874)\].

To address these limitations, several studies have explored the use of simulated users to enable automatic interaction with CRSs. For instance, \[[1](http://arxiv.org/abs/2304.13874)\] proposes a user simulator-based framework for multi-turn interactions with mixed-initiative CS systems, demonstrating that user feedback can significantly improve retrieval performance. Similarly, \[[13](http://arxiv.org/abs/2412.06949)\] introduces a dataset that links Reddit conversations with MovieLens interactions to enrich item representations and improve recommendation accuracy. These works highlight the importance of incorporating both conversational and collaborative signals for better performance.

In the context of reward learning, \[[15](http://arxiv.org/abs/1708.04378)\] proposes a method to learn user reward functions directly from interaction traces, which can be used to improve the personalization and effectiveness of recommendation systems. This aligns with the idea of using generative reward models to simulate user feedback, as proposed in our work. Furthermore, \[[12](http://arxiv.org/abs/2112.05197)\] introduces a framework that allows users to critique recommendations with natural language justifications, enhancing the interactivity and trustworthiness of conversational systems.

To improve the efficiency and effectiveness of conversational recommendation, \[[14](http://arxiv.org/abs/2112.08140)\] proposes a model that leverages item metadata and semantic alignment with dialog context to generate high-quality recommendations. This approach reduces the reliance on knowledge graphs and simplifies the engineering process. Additionally, \[[10](http://arxiv.org/abs/2412.02415)\] introduces a Transformer-based sequential conversational recommendation method that models sequential dependencies in dialogues, improving the accuracy of recommendations.

The use of reinforcement learning (RL) in conversational recommendation has also been explored. \[[4](http://arxiv.org/abs/2105.09710)\] proposes a unified policy learning task that integrates conversation and recommendation components, enhancing scalability and stability. Similarly, \[[7](http://arxiv.org/abs/2310.14609)\] introduces a long short-term feedback architecture that connects recommendation and conversation modules, enabling more natural and effective interactions.

In summary, the field of conversational recommendation has seen significant advancements, including the use of simulated users, reward learning, and reinforcement learning frameworks. These approaches aim to improve the accuracy, efficiency, and user experience of CRSs. Our work builds on these contributions by introducing a generative reward model based simulated user (GRSU) that enables automatic and efficient interaction with CRSs.

1. \[[1](http://arxiv.org/abs/2304.13874)\] Exploiting Simulated User Feedback for Conversational Search: Ranking, Rewriting, and Beyond  
2. \[[2](http://arxiv.org/abs/2310.20109)\] Multi-Objective Intrinsic Reward Learning for Conversational Recommender Systems  
3. \[[4](http://arxiv.org/abs/2105.09710)\] Unified Conversational Recommendation Policy Learning via Graph-based Reinforcement Learning  
4. \[[7](http://arxiv.org/abs/2310.14609)\] Long Short-Term Planning for Conversational Recommendation Systems  
5. \[[10](http://arxiv.org/abs/2412.02415)\] Knowledge-Enhanced Conversational Recommendation via Transformer-Based Sequential Modeling  
6. \[[12](http://arxiv.org/abs/2112.05197)\] Self-Supervised Bot Play for Conversational Recommendation with Justifications  
7. \[[13](http://arxiv.org/abs/2412.06949)\] Bridging Conversational and Collaborative Signals for Conversational Recommendation  
8. \[[14](http://arxiv.org/abs/2112.08140)\] Improving Conversational Recommendation Systems' Quality with Context-Aware Item Meta Information  
9. \[[15](http://arxiv.org/abs/1708.04378)\] Towards Learning Reward Functions from User Interactions  
10. \[[16](http://arxiv.org/abs/1806.03277)\] Conversational Recommender System
## Research papers
### Outline
- [Reward Learning and User Feedback Modeling [3 papers]](#category-reward-learning-and-user-feedback-modeling)
- [Challenges in Capturing User Preferences [2 papers]](#category-challenges-in-capturing-user-preferences)
- [Reinforcement Learning in Conversational Systems [2 papers]](#category-reinforcement-learning-in-conversational-systems)
- [Integration of Conversational and Collaborative Signals [3 papers]](#category-integration-of-conversational-and-collaborative-signals)
- [Evaluation and Transferability of Proposed Methods [1 papers]](#category-evaluation-and-transferability-of-proposed-methods)
- [Conversational Recommendation Systems Overview [2 papers]](#category-conversational-recommendation-systems-overview)
- [Use of Transformer Models in Sequential Recommendations [2 papers]](#category-use-of-transformer-models-in-sequential-recommendations)
- [Self-Supervised Learning for Bot Play [1 papers]](#category-self-supervised-learning-for-bot-play)

### <a id='category-reward-learning-and-user-feedback-modeling'></a>Reward Learning and User Feedback Modeling: 3 papers found.
Context: 
	Document 1: [Snippet]: «This research aims to explore various methods for assessing user feedback in mixed-initiative conversational search (CS ) systems. While CS systems enjoy profuse advancements across multiple aspects, recent research fails to successfully incorporate feedback from the users. One of the main reasons for that is the lack of system-user conversational interaction data. To this end, we propose a user simulator-based framework for multi-turn interactions with a variety of mixed-initiative CS systems. Specifically, we develop a user simulator, dubbed ConvSim, that, once initialized with an information need description, is capable of providing feedback to system's responses, as well as answering potential clarifying questions. Our experiments on a wide variety of state-of-the-art passage retrieval and neural re-ranking models show that effective utilization of user feedback can lead to 16% retrieval performance increase in terms of nDCG@3. Moreover, we observe consistent improvements as the number of feedback rounds increases (35% relative improvement in terms of nDCG@3 after three rounds). This points to a research gap in the development of specific feedback processing modules and opens a potential for significant advancements in CS. To support further research in the topic, we release over 30 000 transcripts of system-simulator interactions based on well-established CS datasets.»
[_citation_number]: «1»
[Category]: «Reward Learning and User Feedback Modeling»

	Document 2: [Snippet]: «Conversational Recommender Systems (CRS) actively elicit user preferences to generate adaptive recommendations. Mainstream reinforcement learning-based CRS solutions heavily rely on handcrafted reward functions, which may not be aligned with user intent in CRS tasks. Therefore, the design of task-specific rewards is critical to facilitate CRS policy learning, which remains largely under-explored in the literature. In this work, we propose a novel approach to address this challenge by learning intrinsic rewards from interactions with users. Specifically, we formulate intrinsic reward learning as a multi-objective bi-level optimization problem. The inner level optimizes the CRS policy augmented by the learned intrinsic rewards, while the outer level drives the intrinsic rewards to optimize two CRS-specific objectives: maximizing the success rate and minimizing the number of turns to reach a successful recommendation in conversations. To evaluate the effectiveness of our approach, we conduct extensive experiments on three public CRS benchmarks. The results show that our algorithm significantly improves CRS performance by exploiting informative learned intrinsic rewards.»
[_citation_number]: «2»
[Category]: «Reward Learning and User Feedback Modeling»

	Document 3: [Snippet]: «In the physical world, people have dynamic preferences, e.g., the same situation can lead to satisfaction for some humans and to frustration for others. Personalization is called for. The same observation holds for online behavior with interactive systems. It is natural to represent the behavior of users who are engaging with interactive systems such as a search engine or a recommender system, as a sequence of actions where each next action depends on the current situation and the user reward of taking a particular action. By and large, current online evaluation metrics for interactive systems such as search engines or recommender systems, are static and do not reflect differences in user behavior. They rarely capture or model the reward experienced by a user while interacting with an interactive system. We argue that knowing a user's reward function is essential for an interactive system as both for learning and evaluation. We propose to learn users' reward functions directly from observed interaction traces. In particular, we present how users' reward functions can be uncovered directly using inverse reinforcement learning techniques. We also show how to incorporate user features into the learning process. Our main contribution is a novel and dynamic approach to restore a user's reward function. We present an analytic approach to this problem and complement it with initial experiments using the interaction logs of a cultural heritage institution that demonstrate the feasibility of the approach by uncovering different reward functions for different user groups.»
[_citation_number]: «15»
[Category]: «Reward Learning and User Feedback Modeling»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-29T06:37:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2503.00999)\]. Further details \[[6](http://arxiv.org/abs/2112.11775)\]\[[7](http://arxiv.org/abs/2310.14609)\]\[[8](http://arxiv.org/abs/2111.13463)\]\[[9](http://arxiv.org/abs/1107.0029)\]\[[10](http://arxiv.org/abs/2412.02415)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Conversational recommendation systems (CRSs) use multi-turn interaction to
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
tasks and employ beam search for the interaction process. On top of this, we
propose an efficient candidate ranking method to improve the recommendation
results derived from interaction. Extensive experiments on public datasets
demonstrate the effectiveness, efficiency, and transferability of our approach.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2503.00999)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2310.20109)\]\[[7](http://arxiv.org/abs/2310.14609)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Reward learning and user feedback modeling have been increasingly recognized as critical components in the development of conversational systems, particularly in conversational recommender systems (CRSs) and mixed-initiative conversational search (CS) systems \[[1](http://arxiv.org/abs/2304.13874)\]. Recent studies highlight the limitations of handcrafted reward functions, which may not align with user intent, and emphasize the need for learning intrinsic rewards from user interactions \[[2](http://arxiv.org/abs/2310.20109)\]. This approach allows systems to adapt to dynamic user preferences, as users may have varying satisfaction levels based on the same situation \[[15](http://arxiv.org/abs/1708.04378)\]. For instance, in CRSs, the design of task-specific rewards is crucial for policy learning, yet it remains underexplored \[[2](http://arxiv.org/abs/2310.20109)\]. Similarly, in CS systems, the lack of conversational interaction data hinders the incorporation of user feedback, leading to suboptimal performance \[[1](http://arxiv.org/abs/2304.13874)\]. To address these challenges, researchers have proposed user simulators that generate realistic feedback, enabling multi-turn interactions and improving recommendation accuracy \[[1](http://arxiv.org/abs/2304.13874)\]. These simulators, such as ConvSim, provide both coarse-grained and fine-grained feedback, enhancing the system's ability to capture intricate user preferences \[[1](http://arxiv.org/abs/2304.13874)\]. Additionally, methods like inverse reinforcement learning are employed to uncover user reward functions directly from interaction traces, offering a dynamic and personalized approach \[[15](http://arxiv.org/abs/1708.04378)\]. Overall, these works underscore the importance of integrating user feedback into the reward learning framework to improve the effectiveness and efficiency of conversational systems.
|    | reference                                                                                                                       | date     | key idea/summary                                                                                                                                                                                                                                                |
|----|---------------------------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Exploiting Simulated User Feedback for Conversational Search: Ranking, Rewriting, and Beyond](http://arxiv.org/abs/2304.13874) | 04/26/23 | This research introduces a user simulator-based framework, ConvSim, to effectively incorporate user feedback in mixed-initiative conversational search systems, leading to significant improvements in retrieval performance.                                   |
|  1 | [Multi-Objective Intrinsic Reward Learning for Conversational Recommender Systems](http://arxiv.org/abs/2310.20109)             | 10/31/23 | This work proposes a novel approach to improve Conversational Recommender Systems by learning intrinsic rewards from user interactions, formulated as a multi-objective bi-level optimization problem to maximize success rate and minimize conversation turns. |
|  2 | [Towards Learning Reward Functions from User Interactions](http://arxiv.org/abs/1708.04378)                                     | 08/15/17 | The paper proposes a dynamic approach to uncover users' reward functions from interaction traces using inverse reinforcement learning, enabling more personalized and accurate evaluation of interactive systems.                                               |
### <a id='category-challenges-in-capturing-user-preferences'></a>Challenges in Capturing User Preferences: 2 papers found.
Context: 
	Document 1: [Snippet]: «Conversational Recommender Systems (CRSs) have become increasingly popular as a powerful tool for providing personalized recommendation experiences. By directly engaging with users in a conversational manner to learn their current and fine-grained preferences, a CRS can quickly derive recommendations that are relevant and justifiable. However, existing conversational recommendation systems (CRSs) typically rely on a centralized training and deployment process, which involves collecting and storing explicitly-communicated user preferences in a centralized repository. These fine-grained user preferences are completely human-interpretable and can easily be used to infer sensitive information (e.g., financial status, political stands, and health information) about the user, if leaked or breached. To address the user privacy concerns in CRS, we first define a set of privacy protection guidelines for preserving user privacy under the conversational recommendation setting. Based on these guidelines, we propose a novel federated conversational recommendation framework that effectively reduces the risk of exposing user privacy by (i) de-centralizing both the historical interests estimation stage and the interactive preference elicitation stage and (ii) strictly bounding privacy leakage by enforcing user-level differential privacy with meticulously selected privacy budgets. Through extensive experiments, we show that the proposed framework not only satisfies these user privacy protection guidelines, but also enables the system to achieve competitive recommendation performance even when compared to the state-of-the-art non-private conversational recommendation approach.»
[_citation_number]: «3»
[Category]: «Challenges in Capturing User Preferences»

	Document 2: [Snippet]: «Conversational recommendation system (CRS) is able to obtain fine-grained and dynamic user preferences based on interactive dialogue. Previous CRS assumes that the user has a clear target item, which often deviates from the real scenario, that is for many users who resort to CRS, they might not have a clear idea about what they really like. Specifically, the user may have a clear single preference for some attribute types (e.g. brand) of items, while for other attribute types (e.g. color), the user may have multiple preferences or even no clear preferences, which leads to multiple acceptable attribute instances (e.g. black and red) of one attribute type. Therefore, the users could show their preferences over items under multiple combinations of attribute instances rather than a single item with unique combination of all attribute instances. As a result, we first propose a more realistic conversational recommendation learning setting, namely Multi-Interest Multi-round Conversational Recommendation (MIMCR), where users may have multiple interests in attribute instance combinations and accept multiple items with partially overlapped combinations of attribute instances. To effectively cope with the new CRS learning setting, in this paper, we propose a novel learning framework, namely Multiple Choice questions based Multi-Interest Policy Learning (MCMIPL). In order to obtain user preferences more efficiently, the agent generates multiple choice questions rather than binary yes/no ones on specific attribute instance. Furthermore, we propose a union set strategy to select candidate items instead of existing intersection set strategy in order to overcome over-filtering items during the conversation. Finally, we design a Multi-Interest Policy Learning (MIPL) module, which utilizes captured multiple interests of the user to decide next action, either asking attribute instances or recommending items. Extensive experimental results on four datasets demonstrate the superiority of our method for the proposed MIMCR setting.»
[_citation_number]: «6»
[Category]: «Challenges in Capturing User Preferences»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-29T06:37:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2503.00999)\]. Further details \[[6](http://arxiv.org/abs/2112.11775)\]\[[7](http://arxiv.org/abs/2310.14609)\]\[[8](http://arxiv.org/abs/2111.13463)\]\[[9](http://arxiv.org/abs/1107.0029)\]\[[10](http://arxiv.org/abs/2412.02415)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Conversational recommendation systems (CRSs) use multi-turn interaction to
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
tasks and employ beam search for the interaction process. On top of this, we
propose an efficient candidate ranking method to improve the recommendation
results derived from interaction. Extensive experiments on public datasets
demonstrate the effectiveness, efficiency, and transferability of our approach.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2503.00999)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2310.20109)\]\[[7](http://arxiv.org/abs/2310.14609)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
The challenge of capturing user preferences in conversational recommendation systems (CRSs) is a central issue in the field, as highlighted by multiple studies \[[3](http://arxiv.org/abs/2503.00999)\]. Traditional CRSs often assume users have a clear target item, which is not always the case in real-world scenarios \[[6](http://arxiv.org/abs/2112.11775)\]. Users may exhibit complex and multifaceted preferences, with clear preferences for certain attributes and uncertainty about others, leading to multiple acceptable attribute combinations \[[6](http://arxiv.org/abs/2112.11775)\]. This complexity necessitates more realistic models that can handle multiple interests and partial overlaps in user preferences \[[6](http://arxiv.org/abs/2112.11775)\]. Additionally, privacy concerns arise due to the collection and storage of fine-grained user preferences, which can expose sensitive information if breached \[[3](http://arxiv.org/abs/2503.00999)\]. To address these issues, researchers have proposed frameworks that decentralize preference elicitation and enforce differential privacy to protect user data \[[3](http://arxiv.org/abs/2503.00999)\]. These advancements highlight the evolving nature of CRSs, aiming to balance accuracy, user experience, and privacy protection.
|    | reference                                                                                                                           | date     | key idea/summary                                                                                                                                                                                                                                                                         |
|----|-------------------------------------------------------------------------------------------------------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Federated Conversational Recommender System](http://arxiv.org/abs/2503.00999)                                                      | 03/02/25 | The paper proposes a federated conversational recommendation framework to enhance user privacy by decentralizing preference elicitation and enforcing differential privacy, while maintaining competitive recommendation performance.                                                    |
|  1 | [Multiple Choice Questions based Multi-Interest Policy Learning for Conversational Recommendation](http://arxiv.org/abs/2112.11775) | 12/22/21 | The paper introduces a new conversational recommendation setting called MIMCR, where users have multiple interests in attribute combinations, and proposes a framework called MCMIPL to efficiently capture user preferences through multiple-choice questions and a union set strategy. |
### <a id='category-reinforcement-learning-in-conversational-systems'></a>Reinforcement Learning in Conversational Systems: 2 papers found.
Context: 
	Document 1: [Snippet]: «Conversational recommender systems (CRS) enable the traditional recommender systems to explicitly acquire user preferences towards items and attributes through interactive conversations. Reinforcement learning (RL) is widely adopted to learn conversational recommendation policies to decide what attributes to ask, which items to recommend, and when to ask or recommend, at each conversation turn. However, existing methods mainly target at solving one or two of these three decision-making problems in CRS with separated conversation and recommendation components, which restrict the scalability and generality of CRS and fall short of preserving a stable training procedure. In the light of these challenges, we propose to formulate these three decision-making problems in CRS as a unified policy learning task. In order to systematically integrate conversation and recommendation components, we develop a dynamic weighted graph based RL method to learn a policy to select the action at each conversation turn, either asking an attribute or recommending items. Further, to deal with the sample efficiency issue, we propose two action selection strategies for reducing the candidate action space according to the preference and entropy information. Experimental results on two benchmark CRS datasets and a real-world E-Commerce application show that the proposed method not only significantly outperforms state-of-the-art methods but also enhances the scalability and stability of CRS.»
[_citation_number]: «4»
[Category]: «Reinforcement Learning in Conversational Systems»

	Document 2: [Snippet]: «A personalized conversational sales agent could have much commercial potential. E-commerce companies such as Amazon, eBay, JD, Alibaba etc. are piloting such kind of agents with their users. However, the research on this topic is very limited and existing solutions are either based on single round adhoc search engine or traditional multi round dialog system. They usually only utilize user inputs in the current session, ignoring users' long term preferences. On the other hand, it is well known that sales conversion rate can be greatly improved based on recommender systems, which learn user preferences based on past purchasing behavior and optimize business oriented metrics such as conversion rate or expected revenue. In this work, we propose to integrate research in dialog systems and recommender systems into a novel and unified deep reinforcement learning framework to build a personalized conversational recommendation agent that optimizes a per session based utility function. In particular, we propose to represent a user conversation history as a semi-structured user query with facet-value pairs. This query is generated and updated by belief tracker that analyzes natural language utterances of user at each step. We propose a set of machine actions tailored for recommendation agents and train a deep policy network to decide which action (i.e. asking for the value of a facet or making a recommendation) the agent should take at each step. We train a personalized recommendation model that uses both the user's past ratings and user query collected in the current conversational session when making rating predictions and generating recommendations. Such a conversational system often tries to collect user preferences by asking questions. Once enough user preference is collected, it makes personalized recommendations to the user. We perform both simulation experiments and real online user studies to demonstrate the effectiveness of the proposed framework.»
[_citation_number]: «16»
[Category]: «Reinforcement Learning in Conversational Systems»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-29T06:37:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2503.00999)\]. Further details \[[6](http://arxiv.org/abs/2112.11775)\]\[[7](http://arxiv.org/abs/2310.14609)\]\[[8](http://arxiv.org/abs/2111.13463)\]\[[9](http://arxiv.org/abs/1107.0029)\]\[[10](http://arxiv.org/abs/2412.02415)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Conversational recommendation systems (CRSs) use multi-turn interaction to
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
tasks and employ beam search for the interaction process. On top of this, we
propose an efficient candidate ranking method to improve the recommendation
results derived from interaction. Extensive experiments on public datasets
demonstrate the effectiveness, efficiency, and transferability of our approach.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2503.00999)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2310.20109)\]\[[7](http://arxiv.org/abs/2310.14609)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer:  
Reinforcement learning (RL) has been increasingly applied to conversational recommendation systems (CRSs) to address the challenges of dynamically acquiring user preferences and generating personalized recommendations \[[4](http://arxiv.org/abs/2105.09710)\]. Existing methods often focus on solving one or two of the key decision-making problems—such as asking for attributes or recommending items—using separate components, which limits scalability and training stability \[[4](http://arxiv.org/abs/2105.09710)\]. To overcome these limitations, researchers have proposed unified policy learning frameworks that integrate conversation and recommendation modules, enabling more efficient and effective policy learning \[[4](http://arxiv.org/abs/2105.09710)\]. For instance, some approaches use dynamic weighted graph-based RL to model the interaction process, allowing the system to select actions (e.g., asking questions or recommending items) based on user feedback and contextual information \[[4](http://arxiv.org/abs/2105.09710)\]. Additionally, strategies such as action selection based on preference and entropy information have been introduced to improve sample efficiency and reduce the candidate action space \[[4](http://arxiv.org/abs/2105.09710)\]. These advancements align with broader efforts to combine dialog systems and recommender systems, as seen in works that integrate deep reinforcement learning to build personalized conversational agents capable of optimizing session-based utility functions \[[16](http://arxiv.org/abs/1806.03277)\]. Such frameworks often rely on belief tracking to update user queries and generate tailored actions, such as asking for attribute values or making recommendations, based on the conversation history \[[16](http://arxiv.org/abs/1806.03277)\]. Overall, these studies highlight the potential of RL in enhancing the performance and adaptability of CRSs through unified and efficient policy learning mechanisms.
|    | reference                                                                                                                       | date     | key idea/summary                                                                                                                                                                                                                                                                                      |
|----|---------------------------------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Unified Conversational Recommendation Policy Learning via Graph-based Reinforcement Learning](http://arxiv.org/abs/2105.09710) | 05/20/21 | The paper proposes a unified reinforcement learning approach for conversational recommender systems that integrates conversation and recommendation components, improving scalability, stability, and sample efficiency through dynamic weighted graph-based methods and action selection strategies. |
|  1 | [Conversational Recommender System](http://arxiv.org/abs/1806.03277)                                                            | 06/08/18 | This work proposes a unified deep reinforcement learning framework that integrates dialog systems and recommender systems to create a personalized conversational recommendation agent, which optimizes per session utility by leveraging both user's past behavior and current conversation history. |
### <a id='category-integration-of-conversational-and-collaborative-signals'></a>Integration of Conversational and Collaborative Signals: 3 papers found.
The category "Integration of Conversational and Collaborative Signals" focuses on the challenges and solutions in conversational recommendation systems (CRSs) that aim to better integrate conversational interactions with collaborative filtering techniques to improve recommendation accuracy and user engagement. Existing CRSs often struggle with capturing user preferences effectively due to limited interaction or insufficient collaborative signals, leading to inaccurate recommendations and poor user experience \[[1](http://arxiv.org/abs/2304.13874)\]. To address these issues, researchers have proposed various approaches, such as knowledge graph-based models that dynamically update user-item and item-attribute relationships during dialogue to enhance recommendation quality \[[2](http://arxiv.org/abs/2310.20109)\]. Another approach involves designing novel architectures that allow for more seamless interaction between conversational and recommendation modules, such as the long short-term feedback architecture, which connects long-term recommendation goals with short-term conversational feedback \[[3](http://arxiv.org/abs/2503.00999)\]. Additionally, there is growing interest in leveraging large language models (LLMs) and collaborative datasets to enrich item representations and align recommendations with collaborative filtering embeddings, as demonstrated by the Reddit-ML32M dataset and associated frameworks \[[4](http://arxiv.org/abs/2105.09710)\]. These studies highlight the importance of integrating conversational and collaborative signals to achieve more accurate and personalized recommendations while maintaining a natural and engaging user experience.
|    | reference                                                                                                              | date     | key idea/summary                                                                                                                                                                                                                                                                |
|----|------------------------------------------------------------------------------------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Leveraging Knowledge Graph Embedding for Effective Conversational Recommendation](http://arxiv.org/abs/2408.01342)    | 08/02/24 | KG-CRS is a knowledge graph-based conversational recommender system that improves recommendation performance by dynamically integrating user-item and item-attribute graphs, enabling better learning of user preferences through interactions.                                 |
|  1 | [Long Short-Term Planning for Conversational Recommendation Systems](http://arxiv.org/abs/2310.14609)                  | 10/23/23 | This paper introduces a novel long short-term feedback architecture for Conversational Recommendation Systems (CRS) to enhance interaction between the conversational and recommendation modules by aligning short-term user preferences with long-term recommendation targets. |
|  2 | [Bridging Conversational and Collaborative Signals for Conversational Recommendation](http://arxiv.org/abs/2412.06949) | 12/09/24 | The paper introduces a framework that combines conversational recommendation systems with collaborative filtering by leveraging a new dataset, Reddit-ML32M, to improve recommendation accuracy through aligned LLM-generated recommendations and CF embeddings.                |
### <a id='category-evaluation-and-transferability-of-proposed-methods'></a>Evaluation and Transferability of Proposed Methods: 1 papers found.
Context: 
	Document 1: [Snippet]: «A key distinguishing feature of conversational recommender systems over traditional recommender systems is their ability to elicit user preferences using natural language. Currently, the predominant approach to preference elicitation is to ask questions directly about items or item attributes. Users searching for recommendations may not have deep knowledge of the available options in a given domain. As such, they might not be aware of key attributes or desirable values for them. However, in many settings, talking about the planned use of items does not present any difficulties, even for those that are new to a domain. In this article, we propose a novel approach to preference elicitation by asking implicit questions based on item usage. As one of the main contributions of this work, we develop a multi-stage data annotation protocol using crowdsourcing, to create a high-quality labeled training dataset. Another main contribution is the development of four models for the question generation task: two template-based baseline models and two neural text-to-text models. The template-based models use heuristically extracted common patterns found in the training data, while the neural models use the training data to learn to generate questions automatically. Using common metrics from machine translation for automatic evaluation, we show that our approaches are effective in generating elicitation questions, even with limited training data. We further employ human evaluation for comparing the generated questions using both pointwise and pairwise evaluation designs. We find that the human evaluation results are consistent with the automatic ones, allowing us to draw conclusions about the quality of the generated questions with certainty. Finally, we provide a detailed analysis of cases where the models show their limitations.»
[_citation_number]: «8»
[Category]: «Evaluation and Transferability of Proposed Methods»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-29T06:37:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2503.00999)\]. Further details \[[6](http://arxiv.org/abs/2112.11775)\]\[[7](http://arxiv.org/abs/2310.14609)\]\[[8](http://arxiv.org/abs/2111.13463)\]\[[9](http://arxiv.org/abs/1107.0029)\]\[[10](http://arxiv.org/abs/2412.02415)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Conversational recommendation systems (CRSs) use multi-turn interaction to
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
tasks and employ beam search for the interaction process. On top of this, we
propose an efficient candidate ranking method to improve the recommendation
results derived from interaction. Extensive experiments on public datasets
demonstrate the effectiveness, efficiency, and transferability of our approach.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2503.00999)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2310.20109)\]\[[7](http://arxiv.org/abs/2310.14609)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The evaluation and transferability of proposed methods in conversational recommender systems (CRSs) have been a focal point in recent research. A key challenge lies in accurately capturing user preferences through multi-turn interactions, which requires robust evaluation metrics and the ability to generalize across different domains \[[8](http://arxiv.org/abs/2111.13463)\]. Existing approaches often rely on direct question-asking methods to elicit preferences, but these can be limited by users’ lack of domain knowledge \[[8](http://arxiv.org/abs/2111.13463)\]. To address this, researchers have proposed novel methods that generate implicit questions based on item usage, leveraging both template-based and neural models to improve question quality \[[8](http://arxiv.org/abs/2111.13463)\]. These models are evaluated using automatic metrics from machine translation and human evaluation, ensuring consistency in results \[[8](http://arxiv.org/abs/2111.13463)\]. Additionally, the transferability of these methods is examined through extensive experiments on public datasets, demonstrating their effectiveness and efficiency \[[8](http://arxiv.org/abs/2111.13463)\]. The integration of feedback mechanisms, such as generative item scoring and attribute-based critique, further enhances the system's ability to adapt to diverse user needs \[[8](http://arxiv.org/abs/2111.13463)\]. Overall, these studies highlight the importance of combining automated evaluation with human judgment to ensure the reliability and generalizability of CRSs \[[8](http://arxiv.org/abs/2111.13463)\].
|    | reference                                                                                                                              | date     | key idea/summary                                                                                                                                                                                                                        |
|----|----------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Generating Usage-related Questions for Preference Elicitation in Conversational Recommender Systems](http://arxiv.org/abs/2111.13463) | 11/26/21 | This paper proposes a novel approach to preference elicitation in conversational recommender systems by generating implicit questions based on item usage, and evaluates the effectiveness of different models for question generation. |
### <a id='category-conversational-recommendation-systems-overview'></a>Conversational Recommendation Systems Overview: 2 papers found.
Context: 
	Document 1: [Snippet]: «Searching for and making decisions about information is becoming increasingly difficult as the amount of information and number of choices increases. Recommendation systems help users find items of interest of a particular type, such as movies or restaurants, but are still somewhat awkward to use. Our solution is to take advantage of the complementary strengths of personalized recommendation systems and dialogue systems, creating personalized aides. We present a system - the ADAPTIVE PLACE ADVISOR - that treats item selection as an interactive, conversational process, with the program inquiring about item attributes and the user responding. Individual, long-term user preferences are unobtrusively obtained in the course of normal recommendation dialogues and used to direct future conversations with the same user. We present a novel user model that influences both item search and the questions asked during a conversation. We demonstrate the effectiveness of our system in significantly reducing the time and number of interactions required to find a satisfactory item, as compared to a control group of users interacting with a non-adaptive version of the system.»
[_citation_number]: «9»
[Category]: «Conversational Recommendation Systems Overview»

	Document 2: [Snippet]: «Growing attention has been paid in Conversational Recommendation System (CRS), which works as a conversation-based and recommendation task-oriented tool to provide items of interest and explore user preference. However, existing work in CRS fails to explicitly show the reasoning logic to users and the whole CRS still remains a black box. Therefore we propose a novel end-to-end framework named Explanation Generation for Conversational Recommendation (EGCR) based on generating explanations for conversational agents to explain why they make the action. EGCR incorporates user reviews to enhance the item representation and increase the informativeness of the whole conversation. To the best of our knowledge, this is the first framework for explainable conversational recommendation on real-world datasets. Moreover, we evaluate EGCR on one benchmark conversational recommendation datasets and achieve better performance on both recommendation accuracy and conversation quality than other state-of-the art models. Finally, extensive experiments demonstrate that generated explanations are not only having high quality and explainability, but also making CRS more trustworthy. We will make our code available to contribute to the CRS community»
[_citation_number]: «11»
[Category]: «Conversational Recommendation Systems Overview»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-29T06:37:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2503.00999)\]. Further details \[[6](http://arxiv.org/abs/2112.11775)\]\[[7](http://arxiv.org/abs/2310.14609)\]\[[8](http://arxiv.org/abs/2111.13463)\]\[[9](http://arxiv.org/abs/1107.0029)\]\[[10](http://arxiv.org/abs/2412.02415)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Conversational recommendation systems (CRSs) use multi-turn interaction to
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
tasks and employ beam search for the interaction process. On top of this, we
propose an efficient candidate ranking method to improve the recommendation
results derived from interaction. Extensive experiments on public datasets
demonstrate the effectiveness, efficiency, and transferability of our approach.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2503.00999)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2310.20109)\]\[[7](http://arxiv.org/abs/2310.14609)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Conversational recommendation systems (CRSs) aim to provide personalized recommendations through multi-turn interactions, but they face challenges in accurately capturing user preferences \[[9](http://arxiv.org/abs/1107.0029)\]. Existing systems often struggle with complex and multifaceted user preferences, even with access to external knowledge \[[9](http://arxiv.org/abs/1107.0029)\]. To address these challenges, researchers have proposed various approaches, such as the ADAPTIVE PLACE ADVISOR, which treats item selection as an interactive, conversational process \[[9](http://arxiv.org/abs/1107.0029)\]. This system uses a novel user model to influence both item search and the questions asked during a conversation, significantly reducing the time and number of interactions required to find a satisfactory item \[[9](http://arxiv.org/abs/1107.0029)\]. Additionally, the EGCR framework introduces explainable conversational recommendation by generating explanations for the actions of conversational agents, enhancing transparency and trust \[[11](http://arxiv.org/abs/2208.08035)\]. These works highlight the importance of integrating dialogue systems with recommendation systems to improve user experience and recommendation accuracy \[[9](http://arxiv.org/abs/1107.0029)\]\[[11](http://arxiv.org/abs/2208.08035)\].
|    | reference                                                                                         | date     | key idea/summary                                                                                                                                                                                                                          |
|----|---------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [A Personalized System for Conversational Recommendations](http://arxiv.org/abs/1107.0029)        | 06/30/11 | The ADAPTIVE PLACE ADVISOR system improves item selection by combining personalized recommendation systems with dialogue systems, using long-term user preferences to reduce interaction time and enhance the conversational experience.  |
|  1 | [EGCR: Explanation Generation for Conversational Recommendation](http://arxiv.org/abs/2208.08035) | 08/17/22 | The paper introduces EGCR, an end-to-end framework for explainable conversational recommendation that enhances item representation using user reviews and generates high-quality explanations to improve trustworthiness and performance. |
### <a id='category-use-of-transformer-models-in-sequential-recommendations'></a>Use of Transformer Models in Sequential Recommendations: 2 papers found.
In the category of "Use of Transformer Models in Sequential Recommendations," recent research has focused on leveraging Transformer-based architectures to model sequential dependencies in conversational recommendation systems (CRSs) \[[10](http://arxiv.org/abs/2412.02415)\]. These systems often involve interactions where users discuss items and their related entities, such as directors or genres, creating complex sequential patterns \[[10](http://arxiv.org/abs/2412.02415)\]. Traditional approaches have largely overlooked these dependencies, leading to suboptimal recommendations \[[10](http://arxiv.org/abs/2412.02415)\]. To address this, the TSCR model was introduced, utilizing a Transformer to capture sequential relationships between items and their attributes within conversations \[[10](http://arxiv.org/abs/2412.02415)\]. This model constructs user sequences by incorporating both mentioned items and their associated entities, then employs a Cloze task to predict the next recommended item \[[10](http://arxiv.org/abs/2412.02415)\]. Furthermore, TSCRKG, an enhanced version of TSCR, integrates knowledge graphs to improve recommendation performance by leveraging multi-hop paths in the graph \[[10](http://arxiv.org/abs/2412.02415)\]. Similarly, another study proposed a pre-trained language model (PLM) combined with an item metadata encoder to align item embeddings with semantic information in the dialog context, enhancing recommendation accuracy without relying on knowledge graphs \[[14](http://arxiv.org/abs/2112.08140)\]. These approaches highlight the growing interest in using Transformer models to better understand and model user preferences in sequential recommendation tasks \[[10](http://arxiv.org/abs/2412.02415)\]\[[14](http://arxiv.org/abs/2112.08140)\].
|    | reference                                                                                                                            | date     | key idea/summary                                                                                                                                                                                                                                                                |
|----|--------------------------------------------------------------------------------------------------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Knowledge-Enhanced Conversational Recommendation via Transformer-Based Sequential Modeling](http://arxiv.org/abs/2412.02415)        | 07/12/24 | The paper introduces TSCR, a Transformer-based sequential conversational recommendation method that models sequential dependencies in conversations, and enhances it with a knowledge graph to improve recommendation performance.                                              |
|  1 | [Improving Conversational Recommendation Systems' Quality with Context-Aware Item Meta Information](http://arxiv.org/abs/2112.08140) | 12/15/21 | The paper proposes a conversational recommendation system that uses a pre-trained language model and an item metadata encoder to generate accurate recommendations and responses without relying on knowledge graphs, achieving state-of-the-art results on benchmark datasets. |
### <a id='category-self-supervised-learning-for-bot-play'></a>Self-Supervised Learning for Bot Play: 1 papers found.
Context: 
	Document 1: [Snippet]: «Conversational recommender systems offer the promise of interactive, engaging ways for users to find items they enjoy. We seek to improve conversational recommendation via three dimensions: 1) We aim to mimic a common mode of human interaction for recommendation: experts justify their suggestions, a seeker explains why they don't like the item, and both parties iterate through the dialog to find a suitable item. 2) We leverage ideas from conversational critiquing to allow users to flexibly interact with natural language justifications by critiquing subjective aspects. 3) We adapt conversational recommendation to a wider range of domains where crowd-sourced ground truth dialogs are not available. We develop a new two-part framework for training conversational recommender systems. First, we train a recommender system to jointly suggest items and justify its reasoning with subjective aspects. We then fine-tune this model to incorporate iterative user feedback via self-supervised bot-play. Experiments on three real-world datasets demonstrate that our system can be applied to different recommendation models across diverse domains to achieve superior performance in conversational recommendation compared to state-of-the-art methods. We also evaluate our model on human users, showing that systems trained under our framework provide more useful, helpful, and knowledgeable recommendations in warm- and cold-start settings.»
[_citation_number]: «12»
[Category]: «Self-Supervised Learning for Bot Play»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-29T06:37:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2503.00999)\]. Further details \[[6](http://arxiv.org/abs/2112.11775)\]\[[7](http://arxiv.org/abs/2310.14609)\]\[[8](http://arxiv.org/abs/2111.13463)\]\[[9](http://arxiv.org/abs/1107.0029)\]\[[10](http://arxiv.org/abs/2412.02415)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Conversational recommendation systems (CRSs) use multi-turn interaction to
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
tasks and employ beam search for the interaction process. On top of this, we
propose an efficient candidate ranking method to improve the recommendation
results derived from interaction. Extensive experiments on public datasets
demonstrate the effectiveness, efficiency, and transferability of our approach.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2503.00999)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2310.20109)\]\[[7](http://arxiv.org/abs/2310.14609)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Self-Supervised Learning for Bot Play has emerged as a promising approach to enhance conversational recommender systems (CRSs) by enabling more natural and effective user interactions. This category focuses on training models to simulate human-like dialogue through iterative feedback mechanisms, where the system learns from user critiques and adjusts its recommendations accordingly \[[12](http://arxiv.org/abs/2112.05197)\]. The key idea is to use self-supervised learning to allow the system to generate responses based on user input without requiring explicit human supervision. This approach is particularly useful in scenarios where crowd-sourced dialog data is limited, as it enables the model to adapt to diverse domains and user preferences \[[12](http://arxiv.org/abs/2112.05197)\]. By incorporating bot-play, or simulated interactions, the system can refine its recommendations through continuous learning, improving both accuracy and user satisfaction. This method aligns with broader efforts in conversational AI to create more engaging and personalized experiences, leveraging the power of self-supervised learning to bridge the gap between automated systems and human-like interaction.
|    | reference                                                                                                         | date     | key idea/summary                                                                                                                                                                                                                               |
|----|-------------------------------------------------------------------------------------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Self-Supervised Bot Play for Conversational Recommendation with Justifications](http://arxiv.org/abs/2112.05197) | 12/09/21 | This paper introduces a framework for conversational recommender systems that improves recommendations through iterative user feedback, natural language justifications, and adaptation to diverse domains without crowd-sourced ground truth. |
