## Related Works

Conversational Recommender Systems (CRSs) have emerged as a promising approach to dynamically capture user preferences through multi-turn interactions \[[1](http://arxiv.org/abs/2002.09102)\]. Traditional recommender systems often rely on static models that estimate user preferences based on past behavior, which limits their ability to adapt to dynamic user needs \[[4](http://arxiv.org/abs/2101.09459)\]. In contrast, CRSs enable systems to actively engage with users by asking questions about item attributes and recommending items in real-time \[[1](http://arxiv.org/abs/2002.09102)\]. This interactive approach allows for more accurate preference elicitation and personalized recommendations \[[1](http://arxiv.org/abs/2002.09102)\].

Several studies have explored the challenges of conversational recommendation, particularly in understanding user preferences from natural language interactions. For instance, the Estimation-Action-Reflection (EAR) framework was introduced to address three key problems in CRSs: determining what questions to ask, when to recommend items, and how to adapt to user feedback \[[1](http://arxiv.org/abs/2002.09102)\]. The framework consists of three stages—Estimation, Action, and Reflection—to better converse with users \[[1](http://arxiv.org/abs/2002.09102)\]. However, existing methods often struggle with effectively integrating conversation and recommendation components, leading to suboptimal performance \[[6](http://arxiv.org/abs/2105.09710)\].

To improve the interaction process, the Conversational Path Reasoning (CPR) framework was proposed, which models conversational recommendation as an interactive path reasoning problem on a graph \[[2](http://arxiv.org/abs/2007.00194)\]. CPR leverages the graph structure to prune irrelevant attributes and improve the chances of hitting user-preferred attributes \[[2](http://arxiv.org/abs/2007.00194)\]. This approach has shown significant improvements over state-of-the-art methods like EAR and CRM \[[2](http://arxiv.org/abs/2007.00194)\]. Additionally, the Knowledge Graph based Semantic Fusion approach enhances CRSs by incorporating both word-oriented and entity-oriented knowledge graphs to align semantic representations \[[3](http://arxiv.org/abs/2007.04032)\]. This helps bridge the semantic gap between natural language and item-level preferences \[[3](http://arxiv.org/abs/2007.04032)\].

The development of conversational recommendation systems has also been influenced by reinforcement learning (RL) techniques. The Unified Conversational Recommendation Policy Learning via Graph-based Reinforcement Learning method integrates conversation and recommendation components into a unified policy learning task \[[6](http://arxiv.org/abs/2105.09710)\]. This approach enables the system to learn when to ask for attributes or recommend items, improving scalability and stability \[[6](http://arxiv.org/abs/2105.09710)\]. Moreover, the SAUR paradigm, which involves System Ask – User Respond, has been proposed to formalize conversational search and recommendation frameworks \[[5](https://www.semanticscholar.org/paper/3ae5bef6b0c8317603a2deab2527383580904fd8)\]. This paradigm allows systems to ask questions to clarify user needs and provide personalized recommendations during the conversation \[[5](https://www.semanticscholar.org/paper/3ae5bef6b0c8317603a2deab2527383580904fd8)\].

To evaluate the effectiveness of conversational recommenders, user simulation techniques have been introduced. The UserSimCRS toolkit enables automatic evaluation by simulating user interactions and generating realistic responses \[[16](http://arxiv.org/abs/2301.05544)\]. This approach helps overcome the limitations of human evaluation, which is time-consuming and resource-intensive \[[13](http://arxiv.org/abs/2006.08732)\]. Furthermore, the Q&R framework, which combines question generation and recommendation, has been proposed to improve the accuracy of recommendations by incorporating user feedback \[[14](https://www.semanticscholar.org/paper/2610b45131f31a7c58b0cd6a8fce21c02ba014be)\].

In summary, the field of conversational recommendation has seen significant advancements, with various approaches addressing the challenges of preference elicitation, dialogue understanding, and recommendation accuracy. However, there remains a need for more robust evaluation methods and scalable frameworks to support real-world deployment \[[4](http://arxiv.org/abs/2101.09459)\].

References:
1. \[[1](http://arxiv.org/abs/2002.09102)\] Estimation-Action-Reflection: Towards Deep Interaction Between Conversational and Recommender Systems
2. \[[2](http://arxiv.org/abs/2007.00194)\] Interactive Path Reasoning on Graph for Conversational Recommendation
3. \[[3](http://arxiv.org/abs/2007.04032)\] Improving Conversational Recommender Systems via Knowledge Graph based Semantic Fusion
4. \[[4](http://arxiv.org/abs/2101.09459)\] Advances and Challenges in Conversational Recommender Systems: A Survey
5. \[[5](https://www.semanticscholar.org/paper/3ae5bef6b0c8317603a2deab2527383580904fd8)\] Towards Conversational Search and Recommendation: System Ask, User Respond
6. \[[6](http://arxiv.org/abs/2105.09710)\] Unified Conversational Recommendation Policy Learning via Graph-based Reinforcement Learning
7. \[[7](http://arxiv.org/abs/2004.00646)\] A Survey on Conversational Recommender Systems
8. \[[8](http://arxiv.org/abs/2010.04125)\] Towards Topic-Guided Conversational Recommender System
9. \[[9](http://arxiv.org/abs/1806.03277)\] Conversational Recommender System
10. \[[10](http://arxiv.org/abs/2105.04774)\] Learning to Ask Appropriate Questions in Conversational Recommendation
11. \[[11](https://www.semanticscholar.org/paper/33e0fe2d4cf01b16da89ab0c180cdcbf37b3be17)\] Adapting User Preference to Online Feedback in Multi-round Conversational Recommendation
12. \[[12](http://arxiv.org/abs/2005.14255)\] Towards Question-based Recommender Systems
13. \[[13](http://arxiv.org/abs/2006.08732)\] Evaluating Conversational Recommender Systems via User Simulation
14. \[[14](https://www.semanticscholar.org/paper/2610b45131f31a7c58b0cd6a8fce21c02ba014be)\] Q&R: A Two-Stage Approach toward Interactive Recommendation
15. \[[15](https://www.semanticscholar.org/paper/be0edbe07823c69a4e6fc1e194a35910655885e4)\] Leading Conversational Search by Suggesting Useful Questions
16. \[[16](http://arxiv.org/abs/2301.05544)\] UserSimCRS: A User Simulation Toolkit for Evaluating Conversational Recommender Systems
## Research papers
### Outline
- [Reinforcement Learning in CRSs [2 papers]](#category-reinforcement-learning-in-crss)
- [User Preference Elicitation Techniques [3 papers]](#category-user-preference-elicitation-techniques)
- [Knowledge Graph Integration [2 papers]](#category-knowledge-graph-integration)
- [Conversational Recommender Systems Overview [4 papers]](#category-conversational-recommender-systems-overview)
- [Graph-Based Reinforcement Learning [1 papers]](#category-graph-based-reinforcement-learning)
- [Dialogue Understanding in CRSs [1 papers]](#category-dialogue-understanding-in-crss)
- [Evaluation Methods for CRSs [2 papers]](#category-evaluation-methods-for-crss)
- [User Simulation Toolkits [1 papers]](#category-user-simulation-toolkits)

### <a id='category-reinforcement-learning-in-crss'></a>Reinforcement Learning in CRSs: 2 papers found.
Context: 
	Document 1: [Category]: «Reinforcement Learning in CRSs»
[Snippet]: «Recommender systems are embracing conversational technologies to obtain user preferences dynamically, and to overcome inherent limitations of their static models. A successful Conversational Recommender System (CRS) requires proper handling of interactions between conversation and recommendation. We argue that three fundamental problems need to be solved: 1) what questions to ask regarding item attributes, 2) when to recommend items, and 3) how to adapt to the users' online feedback. To the best of our knowledge, there lacks a unified framework that addresses these problems. In this work, we fill this missing interaction framework gap by proposing a new CRS framework named Estimation"Action" Reflection, or EAR, which consists of three stages to better converse with users. (1) Estimation, which builds predictive models to estimate user preference on both items and item attributes; (2) Action, which learns a dialogue policy to determine whether to ask attributes or recommend items, based on Estimation stage and conversation history; and (3) Reflection, which updates the recommender model when a user rejects the recommendations made by the Action stage. We present two conversation scenarios on binary and enumerated questions, and conduct extensive experiments on two datasets from Yelp and LastFM, for each scenario, respectively. Our experiments demonstrate significant improvements over the state-of-the-art method CRM , corresponding to fewer conversation turns and a higher level of recommendation hits.»
[_citation_number]: «1»

	Document 2: [Category]: «Reinforcement Learning in CRSs»
[Snippet]: «A personalized conversational sales agent could have much commercial potential. E-commerce companies such as Amazon, eBay, JD, Alibaba etc. are piloting such kind of agents with their users. However, the research on this topic is very limited and existing solutions are either based on single round adhoc search engine or traditional multi round dialog system. They usually only utilize user inputs in the current session, ignoring users' long term preferences. On the other hand, it is well known that sales conversion rate can be greatly improved based on recommender systems, which learn user preferences based on past purchasing behavior and optimize business oriented metrics such as conversion rate or expected revenue. In this work, we propose to integrate research in dialog systems and recommender systems into a novel and unified deep reinforcement learning framework to build a personalized conversational recommendation agent that optimizes a per session based utility function. In particular, we propose to represent a user conversation history as a semi-structured user query with facet-value pairs. This query is generated and updated by belief tracker that analyzes natural language utterances of user at each step. We propose a set of machine actions tailored for recommendation agents and train a deep policy network to decide which action (i.e. asking for the value of a facet or making a recommendation) the agent should take at each step. We train a personalized recommendation model that uses both the user's past ratings and user query collected in the current conversational session when making rating predictions and generating recommendations. Such a conversational system often tries to collect user preferences by asking questions. Once enough user preference is collected, it makes personalized recommendations to the user. We perform both simulation experiments and real online user studies to demonstrate the effectiveness of the proposed framework.»
[_citation_number]: «9»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-29T06:37:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2007.04032)\]. Further details \[[6](http://arxiv.org/abs/2105.09710)\]\[[7](http://arxiv.org/abs/2004.00646)\]\[[8](http://arxiv.org/abs/2010.04125)\]\[[9](http://arxiv.org/abs/1806.03277)\]\[[10](http://arxiv.org/abs/2105.04774)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Conversational recommendation systems (CRSs) use multi-turn interaction to
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2007.04032)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2007.00194)\]\[[7](http://arxiv.org/abs/2004.00646)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Reinforcement learning in conversational recommender systems (CRSs) has gained significant attention for its ability to dynamically capture user preferences through multi-turn interactions \[[1](http://arxiv.org/abs/2002.09102)\]. A key challenge lies in determining when to ask questions about item attributes versus when to recommend items, as well as how to adapt to user feedback in real-time \[[1](http://arxiv.org/abs/2002.09102)\]. Existing approaches often rely on single-round ad-hoc search engines or traditional dialogue systems, which fail to leverage long-term user preferences and may degrade the user experience due to frequent interactions \[[9](http://arxiv.org/abs/1806.03277)\]. To address these limitations, researchers have proposed frameworks that integrate dialog systems with recommender systems using deep reinforcement learning \[[9](http://arxiv.org/abs/1806.03277)\]. For instance, one study introduces a three-stage framework—Estimation, Action, and Reflection—to better align conversation and recommendation processes \[[1](http://arxiv.org/abs/2002.09102)\]. The Estimation stage builds predictive models for user preferences, while the Action stage learns a dialogue policy to decide whether to ask questions or make recommendations based on conversation history \[[1](http://arxiv.org/abs/2002.09102)\]. The Reflection stage updates the model when users reject recommendations, ensuring continuous adaptation \[[1](http://arxiv.org/abs/2002.09102)\]. Another work focuses on developing a personalized conversational recommendation agent that optimizes a session-based utility function, incorporating both past ratings and current session data to improve recommendation accuracy \[[9](http://arxiv.org/abs/1806.03277)\]. These approaches highlight the growing interest in combining reinforcement learning with conversational dynamics to enhance CRS performance.
|    | reference                                                                                                                                | date     | key idea/summary                                                                                                                                                                                                                                                                                      |
|----|------------------------------------------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Estimation-Action-Reflection: Towards Deep Interaction Between Conversational and Recommender Systems](http://arxiv.org/abs/2002.09102) | 01/20/20 | The paper introduces a new Conversational Recommender System (CRS) framework named EAR, which addresses three fundamental problems in conversational recommendations through three stages: Estimation, Action, and Reflection, leading to improved performance over existing methods.                 |
|  1 | [Conversational Recommender System](http://arxiv.org/abs/1806.03277)                                                                     | 06/08/18 | This work proposes a unified deep reinforcement learning framework that integrates dialog systems and recommender systems to create a personalized conversational recommendation agent, which optimizes per session utility by leveraging both user's past behavior and current conversation history. |
### <a id='category-user-preference-elicitation-techniques'></a>User Preference Elicitation Techniques: 3 papers found.
Context: 
	Document 1: [Category]: «User Preference Elicitation Techniques»
[Snippet]: «Traditional recommendation systems estimate user preference on items from past interaction history, thus suffering from the limitations of obtaining fine-grained and dynamic user preference. Conversational recommendation system (CRS) brings revolutions to those limitations by enabling the system to directly ask users about their preferred attributes on items. However, existing CRS methods do not make full use of such advantage --- they only use the attribute feedback in rather implicit ways such as updating the latent user representation. In this paper, we propose Conversational Path Reasoning (CPR), a generic framework that models conversational recommendation as an interactive path reasoning problem on a graph. It walks through the attribute vertices by following user feedback, utilizing the user preferred attributes in an explicit way. By leveraging on the graph structure, CPR is able to prune off many irrelevant candidate attributes, leading to a better chance of hitting user-preferred attributes. To demonstrate how CPR works, we propose a simple yet effective instantiation named SCPR (Simple CPR). We perform empirical studies on the multi-round conversational recommendation scenario, the most realistic CRS setting so far that considers multiple rounds of asking attributes and recommending items. Through extensive experiments on two datasets Yelp and LastFM, we validate the effectiveness of our SCPR, which significantly outperforms the state-of-the-art CRS methods EAR and CRM. In particular, we find that the more attributes there are, the more advantages our method can achieve.»
[_citation_number]: «2»

	Document 2: [Category]: «User Preference Elicitation Techniques»
[Snippet]: «This paper concerns user preference estimation in multi-round conversational recommender systems (CRS), which interacts with users by asking questions about attributes and recommending items multiple times in one conversation. Multi-round CRS such as EAR have been proposed in which the user's online feedback at both attribute level and item level can be utilized to estimate user preference and make recommendations. Though preliminary success has been shown, existing user preference models in CRS usually use the online feedback information as independent features or training instances, overlooking the relation between attribute-level and item-level feedback signals. The relation can be used to more precisely identify the reasons (e.g., some certain attributes) that trigger the rejection of an item, leading to more fine-grained utilization of the feedback information. To address aforementioned issue, this paper proposes a novel preference estimation model tailored for multi-round CRS, called Feedback-guided Preference Adaptation Network (FPAN). In FPAN, two gating modules are designed to respectively adapt the original user embedding and item-level feedback, both according to the online attribute-level feedback. The gating modules utilize the fine-grained attribute-level feedback to revise the user embedding and coarse-grained item-level feedback, achieving more accurate user preference estimation by considering the relation between feedback. Experimental results on two benchmarks showed that FPAN outperformed the state-of-the-art user preference models in CRS, and the multi-round CRS can also be enhanced by using FPAN as its recommender component.»
[_citation_number]: «11»

	Document 3: [Category]: «User Preference Elicitation Techniques»
[Snippet]: «Conversational and question-based recommender systems have gained increasing attention in recent years, with users enabled to converse with the system and better control recommendations. Nevertheless, research in the field is still limited, compared to traditional recommender systems. In this work, we propose a novel Question-based recommendation method, Qrec, to assist users to find items interactively, by answering automatically constructed and algorithmically chosen questions. Previous conversational recommender systems ask users to express their preferences over items or item facets. Our model, instead, asks users to express their preferences over descriptive item features. The model is first trained offline by a novel matrix factorization algorithm, and then iteratively updates the user and item latent factors online by a closed-form solution based on the user answers. Meanwhile, our model infers the underlying user belief and preferences over items to learn an optimal question-asking strategy by using Generalized Binary Search, so as to ask a sequence of questions to the user. Our experimental results demonstrate that our proposed matrix factorization model outperforms the traditional Probabilistic Matrix Factorization model. Further, our proposed Qrec model can greatly improve the performance of state-of-the-art baselines, and it is also effective in the case of cold-start user and item recommendations.»
[_citation_number]: «12»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-29T06:37:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2007.04032)\]. Further details \[[6](http://arxiv.org/abs/2105.09710)\]\[[7](http://arxiv.org/abs/2004.00646)\]\[[8](http://arxiv.org/abs/2010.04125)\]\[[9](http://arxiv.org/abs/1806.03277)\]\[[10](http://arxiv.org/abs/2105.04774)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Conversational recommendation systems (CRSs) use multi-turn interaction to
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2007.04032)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2007.00194)\]\[[7](http://arxiv.org/abs/2004.00646)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Conversational recommendation systems (CRSs) have emerged as a promising approach to better capture user preferences through multi-turn interactions \[[1](http://arxiv.org/abs/2002.09102)\]. Traditional recommendation systems often rely on historical data to estimate user preferences, which can be limited in capturing fine-grained and dynamic preferences \[[2](http://arxiv.org/abs/2007.00194)\]. In contrast, CRSs directly engage users to elicit preferences on item attributes, enabling more accurate and personalized recommendations \[[1](http://arxiv.org/abs/2002.09102)\]. However, existing methods often fail to fully leverage this advantage, as they implicitly use attribute feedback, such as updating latent user representations, rather than explicitly incorporating user preferences \[[2](http://arxiv.org/abs/2007.00194)\]. To address this, recent works have proposed frameworks that model conversational recommendation as an interactive path reasoning problem on a graph, allowing systems to walk through attribute vertices based on user feedback \[[2](http://arxiv.org/abs/2007.00194)\]. For example, the Conversational Path Reasoning (CPR) framework explicitly utilizes user-preferred attributes by leveraging the graph structure to prune irrelevant candidates, leading to more accurate recommendations \[[2](http://arxiv.org/abs/2007.00194)\]. Similarly, the Feedback-guided Preference Adaptation Network (FPAN) focuses on integrating attribute-level and item-level feedback signals to improve user preference estimation, achieving more precise identification of reasons behind item rejections \[[11](https://www.semanticscholar.org/paper/33e0fe2d4cf01b16da89ab0c180cdcbf37b3be17)\]. Additionally, the Qrec model introduces a question-based approach, where users express preferences over item features rather than items themselves, leading to more efficient and effective recommendations \[[12](http://arxiv.org/abs/2005.14255)\]. These approaches highlight the ongoing efforts to enhance user preference elicitation in CRSs by leveraging explicit feedback and sophisticated modeling techniques.
|    | reference                                                                                                                                                                  | date     | key idea/summary                                                                                                                                                                                                                                                           |
|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Interactive Path Reasoning on Graph for Conversational Recommendation](http://arxiv.org/abs/2007.00194)                                                                   | 07/01/20 | The paper introduces Conversational Path Reasoning (CPR), a framework that models conversational recommendation as an interactive path reasoning problem on a graph, enabling more effective and explicit utilization of user feedback to improve recommendation accuracy. |
|  1 | [Adapting User Preference to Online Feedback in Multi-round Conversational Recommendation](https://www.semanticscholar.org/paper/33e0fe2d4cf01b16da89ab0c180cdcbf37b3be17) | 03/08/21 | This paper introduces FPAN, a novel preference estimation model for multi-round conversational recommender systems that leverages the relationship between attribute-level and item-level feedback to improve user preference estimation and recommendation accuracy.      |
|  2 | [Towards Question-based Recommender Systems](http://arxiv.org/abs/2005.14255)                                                                                              | 05/28/20 | The paper introduces Qrec, a novel question-based recommendation method that improves interactive recommendation by inferring user preferences through descriptive item features and using a closed-form solution for online updates.                                      |
### <a id='category-knowledge-graph-integration'></a>Knowledge Graph Integration: 2 papers found.
Context: 
	Document 1: [Category]: «Knowledge Graph Integration»
[Snippet]: «Conversational recommender systems (CRS) aim to recommend high-quality items to users through interactive conversations. Although several efforts have been made for CRS, two major issues still remain to be solved. First, the conversation data itself lacks of sufficient contextual information for accurately understanding users' preference. Second, there is a semantic gap between natural language expression and item-level user preference. To address these issues, we incorporate both word-oriented and entity-oriented knowledge graphs~(KG) to enhance the data representations in CRSs, and adopt Mutual Information Maximization to align the word-level and entity-level semantic spaces. Based on the aligned semantic representations, we further develop a KG-enhanced recommender component for making accurate recommendations, and a KG-enhanced dialog component that can generate informative keywords or entities in the response text. Extensive experiments have demonstrated the effectiveness of our approach in yielding better performance on both recommendation and conversation tasks.»
[_citation_number]: «3»

	Document 2: [Category]: «Knowledge Graph Integration»
[Snippet]: «Conversational recommender systems (CRSs) have revolutionized the conventional recommendation paradigm by embracing dialogue agents to dynamically capture the fine-grained user preference. In a typical conversational recommendation scenario, a CRS firstly generates questions to let the user clarify her/his demands and then makes suitable recommendations. Hence, the ability to generate suitable clarifying questions is the key to timely tracing users' dynamic preferences and achieving successful recommendations. However, existing CRSs fall short in asking high-quality questions because: (1) system-generated responses heavily depends on the performance of the dialogue policy agent, which has to be trained with huge conversation corpus to cover all circumstances; and (2) current CRSs cannot fully utilize the learned latent user profiles for generating appropriate and personalized responses. To mitigate these issues, we propose the Knowledge-Based Question Generation System (KBQG), a novel framework for conversational recommendation. Distinct from previous conversational recommender systems, KBQG models a user's preference in a finer granularity by identifying the most relevant relations from a structured knowledge graph (KG). Conditioned on the varied importance of different relations, the generated clarifying questions could perform better in impelling users to provide more details on their preferences. Finially, accurate recommendations can be generated in fewer conversational turns. Furthermore, the proposed KBQG outperforms all baselines in our experiments on two real-world datasets.»
[_citation_number]: «10»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-29T06:37:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2007.04032)\]. Further details \[[6](http://arxiv.org/abs/2105.09710)\]\[[7](http://arxiv.org/abs/2004.00646)\]\[[8](http://arxiv.org/abs/2010.04125)\]\[[9](http://arxiv.org/abs/1806.03277)\]\[[10](http://arxiv.org/abs/2105.04774)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Conversational recommendation systems (CRSs) use multi-turn interaction to
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2007.04032)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2007.00194)\]\[[7](http://arxiv.org/abs/2004.00646)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Knowledge graph integration has emerged as a promising approach to enhance conversational recommender systems (CRSs) by addressing the challenges of understanding user preferences and bridging the semantic gap between natural language and item-level preferences \[[3](http://arxiv.org/abs/2007.04032)\]. By incorporating both word-oriented and entity-oriented knowledge graphs (KGs), researchers have aimed to enrich data representations and align semantic spaces for more accurate recommendations \[[3](http://arxiv.org/abs/2007.04032)\]. Additionally, the integration of KGs enables the generation of more informative and personalized dialog components, such as clarifying questions that help users articulate their preferences more effectively \[[10](http://arxiv.org/abs/2105.04774)\]. These approaches not only improve the quality of recommendations but also enhance the conversational experience by leveraging structured knowledge to refine user profiles and guide interactions more precisely.
|    | reference                                                                                                                 | date     | key idea/summary                                                                                                                                                                                                                                             |
|----|---------------------------------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Improving Conversational Recommender Systems via Knowledge Graph based Semantic Fusion](http://arxiv.org/abs/2007.04032) | 07/06/20 | The paper proposes a conversational recommender system that integrates word-oriented and entity-oriented knowledge graphs with mutual information maximization to improve both recommendation accuracy and conversational quality.                           |
|  1 | [Learning to Ask Appropriate Questions in Conversational Recommendation](http://arxiv.org/abs/2105.04774)                 | 05/11/21 | KBQG is a novel framework for conversational recommendation that improves the quality of clarifying questions by leveraging a structured knowledge graph to model user preferences more accurately, leading to more efficient and effective recommendations. |
### <a id='category-conversational-recommender-systems-overview'></a>Conversational Recommender Systems Overview: 4 papers found.
Context: 
	Document 1: [Category]: «Conversational Recommender Systems Overview»
[Snippet]: «Recommender systems exploit interaction history to estimate user preference, having been heavily used in a wide range of industry applications. However, static recommendation models are difficult to answer two important questions well due to inherent shortcomings: (a) What exactly does a user like? (b) Why does a user like an item? The shortcomings are due to the way that static models learn user preference, i.e., without explicit instructions and active feedback from users. The recent rise of conversational recommender systems (CRSs) changes this situation fundamentally. In a CRS, users and the system can dynamically communicate through natural language interactions, which provide unprecedented opportunities to explicitly obtain the exact preference of users. Considerable efforts, spread across disparate settings and applications, have been put into developing CRSs. Existing models, technologies, and evaluation methods for CRSs are far from mature. In this paper, we provide a systematic review of the techniques used in current CRSs. We summarize the key challenges of developing CRSs in five directions: (1) Question-based user preference elicitation. (2) Multi-turn conversational recommendation strategies. (3) Dialogue understanding and generation. (4) Exploitation-exploration trade-offs. (5) Evaluation and user simulation. These research directions involve multiple research fields like information retrieval (IR), natural language processing (NLP), and human-computer interaction (HCI). Based on these research directions, we discuss some future challenges and opportunities. We provide a road map for researchers from multiple communities to get started in this area. We hope this survey can help to identify and address challenges in CRSs and inspire future research.»
[_citation_number]: «4»

	Document 2: [Category]: «Conversational Recommender Systems Overview»
[Snippet]: «Conversational search and recommendation based on user-system dialogs exhibit major differences from conventional search and recommendation tasks in that 1) the user and system can interact for multiple semantically coherent rounds on a task through natural language dialog, and 2) it becomes possible for the system to understand the user needs or to help users clarify their needs by asking appropriate questions from the users directly. We believe the ability to ask questions so as to actively clarify the user needs is one of the most important advantages of conversational search and recommendation. In this paper, we propose and evaluate a unified conversational search/recommendation framework, in an attempt to make the research problem doable under a standard formalization. Specifically, we propose a System Ask -- User Respond (SAUR) paradigm for conversational search, define the major components of the paradigm, and design a unified implementation of the framework for product search and recommendation in e-commerce. To accomplish this, we propose the Multi-Memory Network (MMN) architecture, which can be trained based on large-scale collections of user reviews in e-commerce. The system is capable of asking aspect-based questions in the right order so as to understand the user needs, while (personalized) search is conducted during the conversation, and results are provided when the system feels confident. Experiments on real-world user purchasing data verified the advantages of conversational search and recommendation against conventional search and recommendation algorithms in terms of standard evaluation measures such as NDCG.»
[_citation_number]: «5»

	Document 3: [Category]: «Conversational Recommender Systems Overview»
[Snippet]: «Recommender systems are software applications that help users to find items of interest in situations of information overload. Current research often assumes a one-shot interaction paradigm, where the users’ preferences are estimated based on past observed behavior and where the presentation of a ranked list of suggestions is the main, one-directional form of user interaction. Conversational recommender systems (CRS) take a different approach and support a richer set of interactions. These interactions can, for example, help to improve the preference elicitation process or allow the user to ask questions about the recommendations and to give feedback. The interest in CRS has significantly increased in the past few years. This development is mainly due to the significant progress in the area of natural language processing, the emergence of new voice-controlled home assistants, and the increased use of chatbot technology. With this article, we provide a detailed survey of existing approaches to conversational recommendation. We categorize these approaches in various dimensions, e.g., in terms of the supported user intents or the knowledge they use in the background. Moreover, we discuss technological approaches, review how CRS are evaluated, and finally identify a number of gaps that deserve more research in the future.»
[_citation_number]: «7»

	Document 4: [Category]: «Conversational Recommender Systems Overview»
[Snippet]: «Recommendation systems, prevalent in many applications, aim to surface to users the right content at the right time. Recently, researchers have aspired to develop conversational systems that offer seamless interactions with users, more effectively eliciting user preferences and offering better recommendations. Taking a step towards this goal, this paper explores the two stages of a single round of conversation with a user: which question to ask the user, and how to use their feedback to respond with a more accurate recommendation. Following these two stages, first, we detail an RNN-based model for generating topics a user might be interested in, and then extend a state-of-the-art RNN-based video recommender to incorporate the user's selected topic. We describe our proposed system Q&R, i.e., Question & Recommendation, and the surrogate tasks we utilize to bootstrap data for training our models. We evaluate different components of Q&R on live traffic in various applications within YouTube: User Onboarding, Homepage Recommendation, and Notifications. Our results demonstrate that our approach improves upon state-of-the-art recommendation models, including RNNs, and makes these applications more useful, such as a >1% increase in video notifications opened. Further, our design choices can be useful to practitioners wanting to transition to more conversational recommendation systems.»
[_citation_number]: «14»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-29T06:37:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2007.04032)\]. Further details \[[6](http://arxiv.org/abs/2105.09710)\]\[[7](http://arxiv.org/abs/2004.00646)\]\[[8](http://arxiv.org/abs/2010.04125)\]\[[9](http://arxiv.org/abs/1806.03277)\]\[[10](http://arxiv.org/abs/2105.04774)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Conversational recommendation systems (CRSs) use multi-turn interaction to
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2007.04032)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2007.00194)\]\[[7](http://arxiv.org/abs/2004.00646)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: Conversational recommender systems (CRSs) have emerged as a promising approach to address the limitations of traditional recommendation systems by enabling dynamic, multi-turn interactions between users and the system \[[1](http://arxiv.org/abs/2002.09102)\]. These systems allow for more accurate preference elicitation by engaging users in natural language dialogues, which can help clarify their needs and provide richer feedback \[[2](http://arxiv.org/abs/2007.00194)\]. Unlike static models that rely solely on historical data, CRSs leverage real-time interactions to refine recommendations iteratively \[[3](http://arxiv.org/abs/2007.04032)\]. This shift is driven by advancements in natural language processing and the increasing demand for personalized, interactive experiences in applications such as e-commerce and content recommendation \[[4](http://arxiv.org/abs/2101.09459)\]. Existing research highlights key challenges in CRS development, including question-based preference elicitation, multi-turn dialogue strategies, and the integration of dialogue understanding with recommendation algorithms \[[5](https://www.semanticscholar.org/paper/3ae5bef6b0c8317603a2deab2527383580904fd8)\]. Additionally, the use of simulated users for automated testing and evaluation has gained traction, as it enables the assessment of CRS performance without requiring extensive user involvement \[[6](http://arxiv.org/abs/2105.09710)\]. The proposed GRSU model, for instance, introduces a generative reward framework that allows for automatic interaction and feedback, improving the system’s ability to capture complex user preferences \[[7](http://arxiv.org/abs/2004.00646)\]. These approaches collectively emphasize the importance of interactive, context-aware mechanisms in enhancing recommendation accuracy and user satisfaction \[[8](http://arxiv.org/abs/2010.04125)\].
|    | reference                                                                                                                                                    | date     | key idea/summary                                                                                                                                                                                                                                                                                    |
|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Advances and Challenges in Conversational Recommender Systems: A Survey](http://arxiv.org/abs/2101.09459)                                                   | 01/23/21 | This paper provides a systematic review of conversational recommender systems (CRSs), highlighting key challenges and future directions in user preference elicitation, dialogue understanding, and evaluation methods.                                                                             |
|  1 | [Towards Conversational Search and Recommendation: System Ask, User Respond](https://www.semanticscholar.org/paper/3ae5bef6b0c8317603a2deab2527383580904fd8) | 10/17/18 | The paper introduces a unified conversational search and recommendation framework using the SAUR paradigm and the Multi-Memory Network (MMN) architecture, demonstrating its effectiveness through experiments on real-world e-commerce data.                                                       |
|  2 | [A Survey on Conversational Recommender Systems](http://arxiv.org/abs/2004.00646)                                                                            | 04/01/20 | Conversational recommender systems (CRS) enable richer user interactions compared to traditional recommenders, leveraging advancements in natural language processing and chatbot technology, and this article provides a comprehensive survey of existing approaches and identifies research gaps. |
|  3 | [Q&R: A Two-Stage Approach toward Interactive Recommendation](https://www.semanticscholar.org/paper/2610b45131f31a7c58b0cd6a8fce21c02ba014be)                | 07/19/18 | This paper introduces a conversational recommendation system called Q&R, which improves recommendation accuracy by incorporating user feedback through a two-stage process of generating relevant questions and refining recommendations based on user responses.                                   |
### <a id='category-graph-based-reinforcement-learning'></a>Graph-Based Reinforcement Learning: 1 papers found.
Context: 
	Document 1: [Category]: «Graph-Based Reinforcement Learning»
[Snippet]: «Conversational recommender systems (CRS) enable the traditional recommender systems to explicitly acquire user preferences towards items and attributes through interactive conversations. Reinforcement learning (RL) is widely adopted to learn conversational recommendation policies to decide what attributes to ask, which items to recommend, and when to ask or recommend, at each conversation turn. However, existing methods mainly target at solving one or two of these three decision-making problems in CRS with separated conversation and recommendation components, which restrict the scalability and generality of CRS and fall short of preserving a stable training procedure. In the light of these challenges, we propose to formulate these three decision-making problems in CRS as a unified policy learning task. In order to systematically integrate conversation and recommendation components, we develop a dynamic weighted graph based RL method to learn a policy to select the action at each conversation turn, either asking an attribute or recommending items. Further, to deal with the sample efficiency issue, we propose two action selection strategies for reducing the candidate action space according to the preference and entropy information. Experimental results on two benchmark CRS datasets and a real-world E-Commerce application show that the proposed method not only significantly outperforms state-of-the-art methods but also enhances the scalability and stability of CRS.»
[_citation_number]: «6»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-29T06:37:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2007.04032)\]. Further details \[[6](http://arxiv.org/abs/2105.09710)\]\[[7](http://arxiv.org/abs/2004.00646)\]\[[8](http://arxiv.org/abs/2010.04125)\]\[[9](http://arxiv.org/abs/1806.03277)\]\[[10](http://arxiv.org/abs/2105.04774)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Conversational recommendation systems (CRSs) use multi-turn interaction to
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2007.04032)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2007.00194)\]\[[7](http://arxiv.org/abs/2004.00646)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer:  
Graph-based reinforcement learning has emerged as a promising approach for conversational recommender systems (CRSs), where the goal is to dynamically interact with users to capture their preferences and provide personalized recommendations \[[6](http://arxiv.org/abs/2105.09710)\]. Traditional methods often address only one or two of the key decision-making tasks—such as attribute questioning, item recommendation, or timing of interaction—leading to limited scalability and unstable training procedures \[[6](http://arxiv.org/abs/2105.09710)\]. To overcome these limitations, recent work has focused on unifying these tasks into a single policy learning framework, enabling more coherent and efficient conversational interactions \[[6](http://arxiv.org/abs/2105.09710)\]. A key innovation in this area is the use of dynamic weighted graphs to model the interplay between conversation and recommendation components, allowing the system to select the most appropriate action—either asking for an attribute or recommending an item—at each turn \[[6](http://arxiv.org/abs/2105.09710)\]. Additionally, strategies such as action selection based on preference and entropy information have been introduced to improve sample efficiency and reduce the complexity of the action space \[[6](http://arxiv.org/abs/2105.09710)\]. These advancements highlight the potential of graph-based reinforcement learning to enhance the performance, stability, and generalizability of CRSs in real-world applications.
|    | reference                                                                                                                       | date     | key idea/summary                                                                                                                                                                                                                                                                                      |
|----|---------------------------------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Unified Conversational Recommendation Policy Learning via Graph-based Reinforcement Learning](http://arxiv.org/abs/2105.09710) | 05/20/21 | The paper proposes a unified reinforcement learning approach for conversational recommender systems that integrates conversation and recommendation components, improving scalability, stability, and sample efficiency through dynamic weighted graph-based methods and action selection strategies. |
### <a id='category-dialogue-understanding-in-crss'></a>Dialogue Understanding in CRSs: 1 papers found.
Context: 
	Document 1: [Category]: «Dialogue Understanding in CRSs»
[Snippet]: «Conversational recommender systems (CRS) aim to recommend high-quality items to users through interactive conversations. To develop an effective CRS, the support of high-quality datasets is essential. Existing CRS datasets mainly focus on immediate requests from users, while lack proactive guidance to the recommendation scenario. In this paper, we contribute a new CRS dataset named TG-ReDial (Recommendation through Topic-Guided Dialog). Our dataset has two major features. First, it incorporates topic threads to enforce natural semantic transitions towards the recommendation scenario. Second, it is created in a semi-automatic way, hence human annotation is more reasonable and controllable. Based on TG-ReDial, we present the task of topic-guided conversational recommendation, and propose an effective approach to this task. Extensive experiments have demonstrated the effectiveness of our approach on three sub-tasks, namely topic prediction, item recommendation and response generation. TG-ReDial is available at bluehttps://github.com/RUCAIBox/TG-ReDial.»
[_citation_number]: «8»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-29T06:37:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2007.04032)\]. Further details \[[6](http://arxiv.org/abs/2105.09710)\]\[[7](http://arxiv.org/abs/2004.00646)\]\[[8](http://arxiv.org/abs/2010.04125)\]\[[9](http://arxiv.org/abs/1806.03277)\]\[[10](http://arxiv.org/abs/2105.04774)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Conversational recommendation systems (CRSs) use multi-turn interaction to
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2007.04032)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2007.00194)\]\[[7](http://arxiv.org/abs/2004.00646)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The field of dialogue understanding in conversational recommender systems (CRSs) has seen significant advancements, particularly in the development of high-quality datasets that support more natural and proactive interaction scenarios \[[8](http://arxiv.org/abs/2010.04125)\]. Traditional CRS datasets often focus on immediate user requests, which limits their ability to capture complex user preferences and guide recommendations effectively \[[8](http://arxiv.org/abs/2010.04125)\]. In response, recent work has introduced datasets like TG-ReDial, which incorporate topic threads to enable more natural semantic transitions toward the recommendation scenario \[[8](http://arxiv.org/abs/2010.04125)\]. This approach not only enhances the realism of dialogues but also allows for more structured and guided interactions, improving the system's ability to understand and respond to user intent \[[8](http://arxiv.org/abs/2010.04125)\]. Additionally, the semi-automatic creation of such datasets ensures that human annotations are more reasonable and controllable, leading to better alignment with real-world conversational dynamics \[[8](http://arxiv.org/abs/2010.04125)\]. These innovations are critical for advancing the capabilities of CRSs, as they enable more accurate and personalized recommendations through multi-turn interactions.
|    | reference                                                                                 | date     | key idea/summary                                                                                                                                                                                           |
|----|-------------------------------------------------------------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Towards Topic-Guided Conversational Recommender System](http://arxiv.org/abs/2010.04125) | 10/08/20 | TG-ReDial is a new conversational recommender systems dataset that incorporates topic threads for natural semantic transitions and is created in a semi-automatic way to improve human annotation quality. |
### <a id='category-evaluation-methods-for-crss'></a>Evaluation Methods for CRSs: 2 papers found.
Context: 
	Document 1: [Category]: «Evaluation Methods for CRSs»
[Snippet]: «Conversational information access is an emerging research area. Currently, human evaluation is used for end-to-end system evaluation, which is both very time and resource intensive at scale, and thus becomes a bottleneck of progress. As an alternative, we propose automated evaluation by means of simulating users. Our user simulator aims to generate responses that a real human would give by considering both individual preferences and the general flow of interaction with the system. We evaluate our simulation approach on an item recommendation task by comparing three existing conversational recommender systems. We show that preference modeling and task-specific interaction models both contribute to more realistic simulations, and can help achieve high correlation between automatic evaluation measures and manual human assessments.»
[_citation_number]: «13»

	Document 2: [Category]: «Evaluation Methods for CRSs»
[Snippet]: «This paper studies a new scenario in conversational search, conversational question suggestion, which leads search engine users to more engaging experiences by suggesting interesting, informative, and useful follow-up questions. We first establish a novel evaluation metric, usefulness, which goes beyond relevance and measures whether the suggestions provide valuable information for the next step of a user’s journey, and construct a public benchmark for useful question suggestion. Then we develop two suggestion systems, a BERT based ranker and a GPT-2 based generator, both trained with novel weak supervision signals that convey past users’ search behaviors in search sessions. The weak supervision signals help ground the suggestions to users’ information-seeking trajectories: we identify more coherent and informative sessions using encodings, and then weakly supervise our models to imitate how users transition to the next state of search. Our offline experiments demonstrate the crucial role our “next-turn” inductive training plays in improving usefulness over a strong online system. Our online A/B test in Bing shows that our more useful question suggestions receive 8% more user clicks than the previous system.»
[_citation_number]: «15»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-29T06:37:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2007.04032)\]. Further details \[[6](http://arxiv.org/abs/2105.09710)\]\[[7](http://arxiv.org/abs/2004.00646)\]\[[8](http://arxiv.org/abs/2010.04125)\]\[[9](http://arxiv.org/abs/1806.03277)\]\[[10](http://arxiv.org/abs/2105.04774)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Conversational recommendation systems (CRSs) use multi-turn interaction to
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2007.04032)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2007.00194)\]\[[7](http://arxiv.org/abs/2004.00646)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The evaluation of conversational recommendation systems (CRSs) has seen significant advancements, particularly in the development of automated evaluation methods that reduce the reliance on costly human assessments. Researchers have proposed user simulators that generate responses mimicking human behavior, incorporating both individual preferences and the flow of interaction \[[13](http://arxiv.org/abs/2006.08732)\]. These simulators are designed to provide more realistic feedback, enhancing the correlation between automated metrics and human judgments. Additionally, novel evaluation metrics such as "usefulness" have been introduced to capture the value of suggestions in conversational contexts, moving beyond traditional relevance measures \[[15](https://www.semanticscholar.org/paper/be0edbe07823c69a4e6fc1e194a35910655885e4)\]. These metrics are supported by public benchmarks and are validated through both offline experiments and real-world A/B tests, demonstrating their effectiveness in improving user engagement and interaction quality.
|    | reference                                                                                                                                      | date     | key idea/summary                                                                                                                                                                                                                                                                                                                                                        |
|----|------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Evaluating Conversational Recommender Systems via User Simulation](http://arxiv.org/abs/2006.08732)                                           | 06/15/20 | The paper proposes an automated evaluation method for conversational information access systems using a user simulator that generates realistic responses by considering individual preferences and interaction flow, showing that preference modeling and task-specific interaction models improve the correlation between automatic evaluation and human assessments. |
|  1 | [Leading Conversational Search by Suggesting Useful Questions](https://www.semanticscholar.org/paper/be0edbe07823c69a4e6fc1e194a35910655885e4) | 04/19/20 | This paper introduces a new conversational search scenario, conversational question suggestion, and develops systems to provide more useful follow-up questions by leveraging weak supervision signals from user search behavior.                                                                                                                                       |
### <a id='category-user-simulation-toolkits'></a>User Simulation Toolkits: 1 papers found.
Context: 
	Document 1: [Category]: «User Simulation Toolkits»
[Snippet]: «We present an extensible user simulation toolkit to facilitate automatic evaluation of conversational recommender systems. It builds on an established agenda-based approach and extends it with several novel elements, including user satisfaction prediction, persona and context modeling, and conditional natural language generation. We showcase the toolkit with a pre-existing movie recommender system and demonstrate its ability to simulate dialogues that mimic real conversations, while requiring only a handful of manually annotated dialogues as training data.»
[_citation_number]: «16»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-29T06:37:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2007.04032)\]. Further details \[[6](http://arxiv.org/abs/2105.09710)\]\[[7](http://arxiv.org/abs/2004.00646)\]\[[8](http://arxiv.org/abs/2010.04125)\]\[[9](http://arxiv.org/abs/1806.03277)\]\[[10](http://arxiv.org/abs/2105.04774)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Conversational recommendation systems (CRSs) use multi-turn interaction to
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2007.04032)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2007.00194)\]\[[7](http://arxiv.org/abs/2004.00646)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The category of "User Simulation Toolkits" focuses on the development of tools that enable the automatic evaluation of conversational recommender systems (CRSs) by simulating realistic user interactions \[[16](http://arxiv.org/abs/2301.05544)\]. These toolkits often build on established approaches, such as agenda-based models, and introduce novel elements like user satisfaction prediction, persona and context modeling, and conditional natural language generation to enhance the realism and effectiveness of simulated dialogues \[[16](http://arxiv.org/abs/2301.05544)\]. The ability to generate dialogues that closely mimic real conversations is crucial for evaluating CRSs without requiring extensive user involvement, which can degrade the user experience \[[16](http://arxiv.org/abs/2301.05544)\]. By requiring only a small amount of manually annotated data for training, these toolkits offer a practical solution for testing and improving CRSs in a controlled environment.
|    | reference                                                                                                                  | date     | key idea/summary                                                                                                                                                                                                                     |
|----|----------------------------------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [UserSimCRS: A User Simulation Toolkit for Evaluating Conversational Recommender Systems](http://arxiv.org/abs/2301.05544) | 01/13/23 | The paper introduces an extensible user simulation toolkit for evaluating conversational recommender systems, incorporating user satisfaction prediction, persona and context modeling, and conditional natural language generation. |
