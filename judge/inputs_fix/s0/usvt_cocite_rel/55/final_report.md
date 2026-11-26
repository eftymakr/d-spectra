## Related Works

Conversational Recommender Systems (CRSs) have emerged as a promising approach to dynamically capture user preferences through multi-turn interactions. Unlike traditional recommender systems that rely on static models and historical data, CRSs enable systems to actively engage users by asking questions about item attributes and recommending items in real-time \[[1](http://arxiv.org/abs/2002.09102)\]. This interactive approach allows for more accurate and personalized recommendations, but it also introduces significant challenges in understanding user preferences, especially when preferences are multifaceted and complex \[[1](http://arxiv.org/abs/2002.09102)\].

Several works have explored the design and implementation of conversational recommendation frameworks. The Estimation-Action-Reflection (EAR) framework, for instance, introduces a three-stage process to better converse with users: (1) Estimation, which builds predictive models to estimate user preference on both items and item attributes; (2) Action, which learns a dialogue policy to determine whether to ask attributes or recommend items, based on Estimation stage and conversation history; and (3) Reflection, which updates the recommender model when a user rejects the recommendations made by the Action stage \[[2](http://arxiv.org/abs/2007.00194)\]. This framework has been evaluated on two datasets from Yelp and LastFM, showing significant improvements over state-of-the-art methods \[[2](http://arxiv.org/abs/2007.00194)\].

Another notable work is the Conversational Path Reasoning (CPR) framework, which models conversational recommendation as an interactive path reasoning problem on a graph. CPR walks through attribute vertices by following user feedback, utilizing the user preferred attributes in an explicit way. This approach enables the system to prune off many irrelevant candidate attributes, leading to a better chance of hitting user-preferred attributes \[[3](http://arxiv.org/abs/2105.09710)\]. The SCPR instantiation of CPR has been shown to significantly outperform existing methods such as EAR and CRM \[[3](http://arxiv.org/abs/2105.09710)\].

The Unified Conversational Recommendation Policy Learning via Graph-based Reinforcement Learning \[[4](https://www.semanticscholar.org/paper/3ae5bef6b0c8317603a2deab2527383580904fd8)\] proposes a unified policy learning task to address the three decision-making problems in CRSs: what attributes to ask, which items to recommend, and when to ask or recommend. This work develops a dynamic weighted graph-based reinforcement learning method to learn a policy to select the action at each conversation turn, either asking an attribute or recommending items \[[4](https://www.semanticscholar.org/paper/3ae5bef6b0c8317603a2deab2527383580904fd8)\]. The method also introduces two action selection strategies to reduce the candidate action space, improving sample efficiency \[[4](https://www.semanticscholar.org/paper/3ae5bef6b0c8317603a2deab2527383580904fd8)\].

The System Ask -- User Respond (SAUR) paradigm \[[5](http://arxiv.org/abs/2101.09459)\] provides a unified framework for conversational search and recommendation, enabling systems to ask questions to clarify user needs and provide recommendations during the conversation. This approach is implemented using the Multi-Memory Network (MMN) architecture, which can be trained based on large-scale collections of user reviews in e-commerce \[[5](http://arxiv.org/abs/2101.09459)\]. The SAUR paradigm has been validated on real-world user purchasing data, showing advantages over conventional search and recommendation algorithms in terms of standard evaluation measures such as NDCG \[[5](http://arxiv.org/abs/2101.09459)\].

The Feedback-guided Preference Adaptation Network (FPAN) \[[9](https://www.semanticscholar.org/paper/33e0fe2d4cf01b16da89ab0c180cdcbf37b3be17)\] addresses the issue of using online feedback in multi-round conversational recommendation by designing two gating modules to adapt the original user embedding and item-level feedback based on attribute-level feedback. This approach improves the accuracy of user preference estimation by considering the relationship between attribute-level and item-level feedback \[[9](https://www.semanticscholar.org/paper/33e0fe2d4cf01b16da89ab0c180cdcbf37b3be17)\].

References:

1. \[[1](http://arxiv.org/abs/2002.09102)\] [Document 1]  
2. \[[2](http://arxiv.org/abs/2007.00194)\] [Document 2]  
3. \[[3](http://arxiv.org/abs/2105.09710)\] [Document 3]  
4. \[[4](https://www.semanticscholar.org/paper/3ae5bef6b0c8317603a2deab2527383580904fd8)\] [Document 4]  
5. \[[5](http://arxiv.org/abs/2101.09459)\] [Document 5]  
6. \[[6](http://arxiv.org/abs/1806.03277)\] [Document 6]  
7. \[[7](http://arxiv.org/abs/2007.04032)\] [Document 7]  
8. \[[8](http://arxiv.org/abs/2010.04125)\] [Document 8]  
9. \[[9](https://www.semanticscholar.org/paper/33e0fe2d4cf01b16da89ab0c180cdcbf37b3be17)\] [Document 9]  
10. \[[10](http://arxiv.org/abs/2112.11775)\] [Document 10]
## Research papers
### Outline
- [Conversational Recommender Systems Frameworks [12 papers]](#category-conversational-recommender-systems-frameworks)
- [Graph-Based Reinforcement Learning for CRSs [1 papers]](#category-graph-based-reinforcement-learning-for-crss)
- [Interactive Feedback Mechanisms in CRSs [1 papers]](#category-interactive-feedback-mechanisms-in-crss)
- [User Preference Estimation Methods [1 papers]](#category-user-preference-estimation-methods)
- [Simulated User Interaction Models [1 papers]](#category-simulated-user-interaction-models)

### <a id='category-conversational-recommender-systems-frameworks'></a>Conversational Recommender Systems Frameworks: 12 papers found.
Conversational recommender systems (CRSs) have emerged as a promising approach to better capture user preferences through interactive dialogue, enabling more accurate and personalized recommendations \[[1](http://arxiv.org/abs/2002.09102)\]. Unlike traditional systems that rely solely on static user-item interactions, CRSs engage users in multi-turn conversations to dynamically elicit preferences, addressing limitations such as the inability to capture fine-grained or dynamic user intent \[[2](http://arxiv.org/abs/2007.00194)\]. This interactive process allows systems to ask targeted questions about item attributes and adapt recommendations based on real-time feedback \[[3](http://arxiv.org/abs/2105.09710)\]. Several frameworks have been proposed to structure this interaction, such as the Estimation-Action-Reflection (EAR) framework, which divides the process into stages: estimating user preferences, deciding when to recommend or ask for more information, and refining the model based on user feedback \[[1](http://arxiv.org/abs/2002.09102)\]. Similarly, the Conversational Path Reasoning (CPR) framework models the interaction as a path-finding problem on a graph, leveraging user feedback to prune irrelevant attributes and improve recommendation accuracy \[[2](http://arxiv.org/abs/2007.00194)\]. The System Ask – User Respond (SAUR) paradigm further emphasizes the importance of active user engagement, enabling systems to ask clarifying questions and provide recommendations in a structured, semantically coherent manner \[[3](http://arxiv.org/abs/2105.09710)\]. Additionally, the integration of knowledge graphs and semantic alignment has been explored to enhance both recommendation and conversation tasks by better capturing user intent and item attributes \[[5](http://arxiv.org/abs/2101.09459)\]. These approaches highlight the growing interest in conversational recommendation, driven by advancements in natural language processing and the increasing demand for more interactive and personalized user experiences \[[8](http://arxiv.org/abs/2010.04125)\].
|    | reference                                                                                                                                                     | date     | key idea/summary                                                                                                                                                                                                                                                                                      |
|----|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Estimation-Action-Reflection: Towards Deep Interaction Between Conversational and Recommender Systems](http://arxiv.org/abs/2002.09102)                      | 01/20/20 | The paper introduces a new Conversational Recommender System (CRS) framework named EAR, which addresses three fundamental problems in conversational recommendations through three stages: Estimation, Action, and Reflection, leading to improved performance over existing methods.                 |
|  1 | [Interactive Path Reasoning on Graph for Conversational Recommendation](http://arxiv.org/abs/2007.00194)                                                      | 07/01/20 | The paper introduces Conversational Path Reasoning (CPR), a framework that models conversational recommendation as an interactive path reasoning problem on a graph, enabling more effective and explicit utilization of user feedback to improve recommendation accuracy.                            |
|  2 | [Towards Conversational Search and Recommendation: System Ask, User Respond](https://www.semanticscholar.org/paper/3ae5bef6b0c8317603a2deab2527383580904fd8)  | 10/17/18 | The paper introduces a unified conversational search and recommendation framework using the SAUR paradigm and the Multi-Memory Network (MMN) architecture, demonstrating its effectiveness through real-world experiments.                                                                            |
|  3 | [Conversational Recommender System](http://arxiv.org/abs/1806.03277)                                                                                          | 06/08/18 | This work proposes a unified deep reinforcement learning framework that integrates dialog systems and recommender systems to create a personalized conversational recommendation agent, which optimizes per session utility by leveraging both user's past behavior and current conversation history. |
|  4 | [Improving Conversational Recommender Systems via Knowledge Graph based Semantic Fusion](http://arxiv.org/abs/2007.04032)                                     | 07/06/20 | The paper proposes a conversational recommender system that integrates word-oriented and entity-oriented knowledge graphs with mutual information maximization to improve both recommendation accuracy and conversational quality.                                                                    |
|  5 | [Towards Topic-Guided Conversational Recommender System](http://arxiv.org/abs/2010.04125)                                                                     | 10/08/20 | TG-ReDial is a new conversational recommender systems dataset that incorporates topic threads for natural semantic transitions and is created in a semi-automatic way to improve human annotation quality.                                                                                            |
|  6 | [Multiple Choice Questions based Multi-Interest Policy Learning for Conversational Recommendation](http://arxiv.org/abs/2112.11775)                           | 12/22/21 | The paper introduces a new conversational recommendation setting called MIMCR, where users have multiple interests in attribute combinations, and proposes a framework called MCMIPL to efficiently capture user preferences through multiple-choice questions and a union set strategy.              |
|  7 | [A Survey on Conversational Recommender Systems](http://arxiv.org/abs/2004.00646)                                                                             | 04/01/20 | Conversational recommender systems (CRS) enable richer user interactions compared to traditional recommenders, leveraging advancements in natural language processing and chatbot technology, and this article provides a comprehensive survey of existing approaches and identifies research gaps.   |
|  8 | [Q&R: A Two-Stage Approach toward Interactive Recommendation](https://www.semanticscholar.org/paper/2610b45131f31a7c58b0cd6a8fce21c02ba014be)                 | 07/19/18 | This paper introduces a conversational recommendation system called Q&R, which improves recommendation accuracy by incorporating user feedback through a two-stage process of generating relevant questions and refining recommendations based on user responses.                                     |
|  9 | [Towards Question-based Recommender Systems](http://arxiv.org/abs/2005.14255)                                                                                 | 05/28/20 | The paper introduces Qrec, a novel question-based recommendation method that improves interactive recommendation by inferring user preferences through descriptive item features and using a closed-form solution for online updates.                                                                 |
| 10 | [Learning to Infer User Implicit Preference in Conversational Recommendation](https://www.semanticscholar.org/paper/0056038b89647afcee84226adf19feb1023a54c0) | 07/06/22 | CRIF is a new conversational recommender system framework that improves user preference estimation by explicitly deducing implicit preferences using attribute-level and item-level feedback, along with a flexible decision strategy based on inverse reinforcement learning.                        |
| 11 | [Seamlessly Unifying Attributes and Items: Conversational Recommendation for Cold-start Users](http://arxiv.org/abs/2005.12979)                               | 05/23/20 | ConTS improves conversational recommendation for cold-start users by unifying item and attribute arms in a Thompson Sampling framework, achieving better performance than existing methods.                                                                                                           |
### <a id='category-graph-based-reinforcement-learning-for-crss'></a>Graph-Based Reinforcement Learning for CRSs: 1 papers found.
Context: 
	Document 1: \[[3](http://arxiv.org/abs/2105.09710)\] «Conversational recommender systems (CRS) enable the traditional recommender systems to explicitly acquire user preferences towards items and attributes through interactive conversations. Reinforcement learning (RL) is widely adopted to learn conversational recommendation policies to decide what attributes to ask, which items to recommend, and when to ask or recommend, at each conversation turn. However, existing methods mainly target at solving one or two of these three decision-making problems in CRS with separated conversation and recommendation components, which restrict the scalability and generality of CRS and fall short of preserving a stable training procedure. In the light of these challenges, we propose to formulate these three decision-making problems in CRS as a unified policy learning task. In order to systematically integrate conversation and recommendation components, we develop a dynamic weighted graph based RL method to learn a policy to select the action at each conversation turn, either asking an attribute or recommending items. Further, to deal with the sample efficiency issue, we propose two action selection strategies for reducing the candidate action space according to the preference and entropy information. Experimental results on two benchmark CRS datasets and a real-world E-Commerce application show that the proposed method not only significantly outperforms state-of-the-art methods but also enhances the scalability and stability of CRS.»
[Category]: «Graph-Based Reinforcement Learning for CRSs»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-29T06:37:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2105.09710)\]. Further details \[[6](http://arxiv.org/abs/1806.03277)\]\[[7](http://arxiv.org/abs/2007.04032)\]\[[8](http://arxiv.org/abs/2010.04125)\]\[[9](https://www.semanticscholar.org/paper/33e0fe2d4cf01b16da89ab0c180cdcbf37b3be17)\]\[[10](http://arxiv.org/abs/2112.11775)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Conversational recommendation systems (CRSs) use multi-turn interaction to
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2105.09710)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2007.00194)\]\[[7](http://arxiv.org/abs/2007.04032)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Graph-based reinforcement learning (RL) has emerged as a promising approach for conversational recommender systems (CRSs), addressing the challenges of integrating conversation and recommendation components \[[3](http://arxiv.org/abs/2105.09710)\]. Traditional methods often tackle only one or two decision-making aspects—such as attribute questioning or item recommendation—leading to limited scalability and unstable training procedures \[[3](http://arxiv.org/abs/2105.09710)\]. To overcome these limitations, recent work proposes a unified policy learning framework that simultaneously addresses these three key decision-making problems \[[3](http://arxiv.org/abs/2105.09710)\]. This approach leverages a dynamic weighted graph-based RL method to learn a policy that selects actions at each conversation turn, either asking for attributes or recommending items \[[3](http://arxiv.org/abs/2105.09710)\]. Furthermore, to enhance sample efficiency, two action selection strategies are introduced, which reduce the candidate action space based on preference and entropy information \[[3](http://arxiv.org/abs/2105.09710)\]. These strategies help maintain a stable training process while improving the overall performance of CRSs. Experimental results on benchmark datasets and real-world E-Commerce applications demonstrate that this method significantly outperforms existing approaches, enhancing both scalability and stability \[[3](http://arxiv.org/abs/2105.09710)\].
|    | reference                                                                                                                       | date     | key idea/summary                                                                                                                                                                                                                                                                                      |
|----|---------------------------------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Unified Conversational Recommendation Policy Learning via Graph-based Reinforcement Learning](http://arxiv.org/abs/2105.09710) | 05/20/21 | The paper proposes a unified reinforcement learning approach for conversational recommender systems that integrates conversation and recommendation components, improving scalability, stability, and sample efficiency through dynamic weighted graph-based methods and action selection strategies. |
### <a id='category-interactive-feedback-mechanisms-in-crss'></a>Interactive Feedback Mechanisms in CRSs: 1 papers found.
Context: 
	Document 1: [_citation_number]: «5»
[Snippet]: «Recommender systems exploit interaction history to estimate user preference, having been heavily used in a wide range of industry applications. However, static recommendation models are difficult to answer two important questions well due to inherent shortcomings: (a) What exactly does a user like? (b) Why does a user like an item? The shortcomings are due to the way that static models learn user preference, i.e., without explicit instructions and active feedback from users. The recent rise of conversational recommender systems (CRSs) changes this situation fundamentally. In a CRS, users and the system can dynamically communicate through natural language interactions, which provide unprecedented opportunities to explicitly obtain the exact preference of users. Considerable efforts, spread across disparate settings and applications, have been put into developing CRSs. Existing models, technologies, and evaluation methods for CRSs are far from mature. In this paper, we provide a systematic review of the techniques used in current CRSs. We summarize the key challenges of developing CRSs in five directions: (1) Question-based user preference elicitation. (2) Multi-turn conversational recommendation strategies. (3) Dialogue understanding and generation. (4) Exploitation-exploration trade-offs. (5) Evaluation and user simulation. These research directions involve multiple research fields like information retrieval (IR), natural language processing (NLP), and human-computer interaction (HCI). Based on these research directions, we discuss some future challenges and opportunities. We provide a road map for researchers from multiple communities to get started in this area. We hope this survey can help to identify and address challenges in CRSs and inspire future research.»
[Category]: «Interactive Feedback Mechanisms in CRSs»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-29T06:37:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2105.09710)\]. Further details \[[6](http://arxiv.org/abs/1806.03277)\]\[[7](http://arxiv.org/abs/2007.04032)\]\[[8](http://arxiv.org/abs/2010.04125)\]\[[9](https://www.semanticscholar.org/paper/33e0fe2d4cf01b16da89ab0c180cdcbf37b3be17)\]\[[10](http://arxiv.org/abs/2112.11775)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Conversational recommendation systems (CRSs) use multi-turn interaction to
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2105.09710)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2007.00194)\]\[[7](http://arxiv.org/abs/2007.04032)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer:  
Interactive feedback mechanisms in conversational recommender systems (CRSs) play a crucial role in capturing user preferences through dynamic, natural language interactions \[[5](http://arxiv.org/abs/2101.09459)\]. Unlike static models that rely on implicit data, CRSs enable users to explicitly express their preferences, addressing the limitations of traditional systems that struggle to determine "what a user likes" and "why they like an item" \[[5](http://arxiv.org/abs/2101.09459)\]. This is particularly important as user preferences are often multifaceted and complex, making accurate recommendations challenging even with access to external knowledge \[[5](http://arxiv.org/abs/2101.09459)\]. To enhance the effectiveness of CRSs, recent research has focused on developing simulated users that provide structured feedback, such as generative item scoring and attribute-based item critique, which offer both coarse-grained and fine-grained insights \[[5](http://arxiv.org/abs/2101.09459)\]. These feedback mechanisms are unified into an instruction-based format, allowing for seamless integration and the development of a unified simulated user through instruction tuning on synthesized data \[[5](http://arxiv.org/abs/2101.09459)\]. This approach enables automatic multi-turn interaction with CRSs, improving the system's ability to capture intricate user preferences while maintaining efficiency \[[5](http://arxiv.org/abs/2101.09459)\].
|    | reference                                                                                                  | date     | key idea/summary                                                                                                                                                                                                        |
|----|------------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Advances and Challenges in Conversational Recommender Systems: A Survey](http://arxiv.org/abs/2101.09459) | 01/23/21 | This paper provides a systematic review of conversational recommender systems (CRSs), highlighting key challenges and future directions in user preference elicitation, dialogue understanding, and evaluation methods. |
### <a id='category-user-preference-estimation-methods'></a>User Preference Estimation Methods: 1 papers found.
Context: 
	Document 1: [_citation_number]: «9»
[Snippet]: «This paper concerns user preference estimation in multi-round conversational recommender systems (CRS), which interacts with users by asking questions about attributes and recommending items multiple times in one conversation. Multi-round CRS such as EAR have been proposed in which the user's online feedback at both attribute level and item level can be utilized to estimate user preference and make recommendations. Though preliminary success has been shown, existing user preference models in CRS usually use the online feedback information as independent features or training instances, overlooking the relation between attribute-level and item-level feedback signals. The relation can be used to more precisely identify the reasons (e.g., some certain attributes) that trigger the rejection of an item, leading to more fine-grained utilization of the feedback information. To address aforementioned issue, this paper proposes a novel preference estimation model tailored for multi-round CRS, called Feedback-guided Preference Adaptation Network (FPAN). In FPAN, two gating modules are designed to respectively adapt the original user embedding and item-level feedback, both according to the online attribute-level feedback. The gating modules utilize the fine-grained attribute-level feedback to revise the user embedding and coarse-grained item-level feedback, achieving more accurate user preference estimation by considering the relation between feedback. Experimental results on two benchmarks showed that FPAN outperformed the state-of-the-art user preference models in CRS, and the multi-round CRS can also be enhanced by using FPAN as its recommender component.»
[Category]: «User Preference Estimation Methods»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-29T06:37:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2105.09710)\]. Further details \[[6](http://arxiv.org/abs/1806.03277)\]\[[7](http://arxiv.org/abs/2007.04032)\]\[[8](http://arxiv.org/abs/2010.04125)\]\[[9](https://www.semanticscholar.org/paper/33e0fe2d4cf01b16da89ab0c180cdcbf37b3be17)\]\[[10](http://arxiv.org/abs/2112.11775)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Conversational recommendation systems (CRSs) use multi-turn interaction to
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2105.09710)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2007.00194)\]\[[7](http://arxiv.org/abs/2007.04032)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
User preference estimation in conversational recommender systems (CRS) has been a focal point of recent research, particularly in multi-round interactions where users provide feedback at both attribute and item levels \[[9](https://www.semanticscholar.org/paper/33e0fe2d4cf01b16da89ab0c180cdcbf37b3be17)\]. Existing models often treat these feedback signals as independent features or training instances, thereby neglecting the interplay between attribute-level and item-level feedback, which can offer deeper insights into user preferences \[[9](https://www.semanticscholar.org/paper/33e0fe2d4cf01b16da89ab0c180cdcbf37b3be17)\]. For instance, attribute-level feedback can reveal specific reasons behind item rejections, while item-level feedback provides a broader view of user satisfaction \[[9](https://www.semanticscholar.org/paper/33e0fe2d4cf01b16da89ab0c180cdcbf37b3be17)\]. To address these limitations, the Feedback-guided Preference Adaptation Network (FPAN) was introduced, which integrates both types of feedback through gating modules that refine user embeddings and item-level feedback based on attribute-level inputs \[[9](https://www.semanticscholar.org/paper/33e0fe2d4cf01b16da89ab0c180cdcbf37b3be17)\]. This approach enables more accurate preference estimation by leveraging the relationship between different feedback types, ultimately enhancing the performance of multi-round CRS systems \[[9](https://www.semanticscholar.org/paper/33e0fe2d4cf01b16da89ab0c180cdcbf37b3be17)\].
|    | reference                                                                                                                                                                  | date     | key idea/summary                                                                                                                                                                                                                                                      |
|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Adapting User Preference to Online Feedback in Multi-round Conversational Recommendation](https://www.semanticscholar.org/paper/33e0fe2d4cf01b16da89ab0c180cdcbf37b3be17) | 03/08/21 | This paper introduces FPAN, a novel preference estimation model for multi-round conversational recommender systems that leverages the relationship between attribute-level and item-level feedback to improve user preference estimation and recommendation accuracy. |
### <a id='category-simulated-user-interaction-models'></a>Simulated User Interaction Models: 1 papers found.
Context: 
	Document 1: [_citation_number]: «14»
[Snippet]: «Conversational information access is an emerging research area. Currently, human evaluation is used for end-to-end system evaluation, which is both very time and resource intensive at scale, and thus becomes a bottleneck of progress. As an alternative, we propose automated evaluation by means of simulating users. Our user simulator aims to generate responses that a real human would give by considering both individual preferences and the general flow of interaction with the system. We evaluate our simulation approach on an item recommendation task by comparing three existing conversational recommender systems. We show that preference modeling and task-specific interaction models both contribute to more realistic simulations, and can help achieve high correlation between automatic evaluation measures and manual human assessments.»
[Category]: «Simulated User Interaction Models»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-29T06:37:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2105.09710)\]. Further details \[[6](http://arxiv.org/abs/1806.03277)\]\[[7](http://arxiv.org/abs/2007.04032)\]\[[8](http://arxiv.org/abs/2010.04125)\]\[[9](https://www.semanticscholar.org/paper/33e0fe2d4cf01b16da89ab0c180cdcbf37b3be17)\]\[[10](http://arxiv.org/abs/2112.11775)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Conversational recommendation systems (CRSs) use multi-turn interaction to
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2105.09710)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2007.00194)\]\[[7](http://arxiv.org/abs/2007.04032)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Simulated user interaction models have gained significant attention in conversational systems, particularly in the context of recommendation tasks. These models aim to replicate human behavior by incorporating both individual preferences and the natural flow of dialogue \[[14](http://arxiv.org/abs/2006.08732)\]. By simulating user responses, they offer an alternative to labor-intensive human evaluations, which are often impractical at scale. Research has shown that integrating preference modeling with task-specific interaction models can enhance the realism of simulated interactions, leading to higher alignment with human assessments \[[14](http://arxiv.org/abs/2006.08732)\]. This approach not only reduces the reliance on manual evaluations but also enables more efficient system testing and refinement. The development of such models is crucial for advancing conversational recommendation systems, as they allow for automated, scalable, and realistic interaction scenarios.
|    | reference                                                                                            | date     | key idea/summary                                                                                                                                                                                                                                                                                                                                                        |
|----|------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Evaluating Conversational Recommender Systems via User Simulation](http://arxiv.org/abs/2006.08732) | 06/15/20 | The paper proposes an automated evaluation method for conversational information access systems using a user simulator that generates realistic responses by considering individual preferences and interaction flow, showing that preference modeling and task-specific interaction models improve the correlation between automatic evaluation and human assessments. |
