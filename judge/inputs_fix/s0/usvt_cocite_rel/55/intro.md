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
