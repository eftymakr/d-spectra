## Related Works

Conversational recommendation systems (CRSs) have gained significant attention in recent years due to their ability to dynamically capture user preferences through multi-turn interactions \[[1](https://www.semanticscholar.org/paper/3ae5bef6b0c8317603a2deab2527383580904fd8)\]. Traditional recommendation systems often rely on static models that estimate user preferences based on past behavior, limiting their ability to adapt to evolving user needs \[[4](http://arxiv.org/abs/2101.09459)\]. In contrast, CRSs enable more nuanced preference elicitation by engaging users in natural language dialogues, allowing the system to ask clarifying questions and refine recommendations iteratively \[[1](https://www.semanticscholar.org/paper/3ae5bef6b0c8317603a2deab2527383580904fd8)\]. This interactive approach has been shown to improve recommendation accuracy and user satisfaction \[[1](https://www.semanticscholar.org/paper/3ae5bef6b0c8317603a2deab2527383580904fd8)\].

Several studies have explored the challenges of modeling user preferences in conversational settings. For instance, \[[4](http://arxiv.org/abs/2101.09459)\] highlights the limitations of static models in accurately capturing what users like and why, emphasizing the need for dynamic interaction. To address this, \[[1](https://www.semanticscholar.org/paper/3ae5bef6b0c8317603a2deab2527383580904fd8)\] proposes a System Ask -- User Respond (SAUR) paradigm, where the system actively asks questions to clarify user needs, leading to more accurate recommendations. Similarly, \[[3](http://arxiv.org/abs/2002.09102)\] introduces the Estimation-Action-Reflection (EAR) framework, which divides the conversational process into three stages: estimating user preferences, deciding whether to ask or recommend, and reflecting on user feedback to improve future interactions.

The integration of conversational and recommendation components remains a key challenge in CRS development. \[[8](http://arxiv.org/abs/2105.09710)\] proposes a unified policy learning approach using graph-based reinforcement learning to simultaneously decide what to ask and what to recommend, enhancing the scalability and stability of conversational recommendation systems. Additionally, \[[14](http://arxiv.org/abs/2206.09363)\] introduces a knowledge-enhanced prompt learning approach to unify recommendation and conversation subtasks, improving the integration of these components.

User feedback is a critical component in refining CRS performance. \[[11](http://arxiv.org/abs/2304.13874)\] develops a user simulator, ConvSim, to generate realistic user feedback, demonstrating that incorporating multiple rounds of feedback significantly improves retrieval performance. \[[16](https://www.semanticscholar.org/paper/33e0fe2d4cf01b16da89ab0c180cdcbf37b3be17)\] further explores the relationship between attribute-level and item-level feedback, proposing a Feedback-guided Preference Adaptation Network (FPAN) to better utilize user feedback in multi-round conversational recommendation.

To enhance the realism of simulated user interactions, \[[13](http://arxiv.org/abs/2006.08732)\] introduces an automated evaluation framework using user simulations, showing that preference modeling and task-specific interaction models contribute to more accurate system evaluation. Additionally, \[[15](http://arxiv.org/abs/1107.0029)\] presents a personalized conversational recommendation system that adaptively collects user preferences during interactions, improving the efficiency and effectiveness of the recommendation process.

In summary, while existing works have made significant strides in developing conversational recommendation systems, challenges remain in seamlessly integrating conversation and recommendation components, effectively utilizing user feedback, and ensuring realistic user simulations. The proposed GRSU model addresses these challenges by introducing a generative reward model for simulated user interaction, enabling more accurate and efficient preference elicitation \[[1](https://www.semanticscholar.org/paper/3ae5bef6b0c8317603a2deab2527383580904fd8)\].

### References

1. \[[1](https://www.semanticscholar.org/paper/3ae5bef6b0c8317603a2deab2527383580904fd8)\] Towards Conversational Search and Recommendation: System Ask, User Respond  
2. \[[2](http://arxiv.org/abs/2004.00646)\] A Survey on Conversational Recommender Systems  
3. \[[3](http://arxiv.org/abs/2002.09102)\] Estimation-Action-Reflection: Towards Deep Interaction Between Conversational and Recommender Systems  
4. \[[4](http://arxiv.org/abs/2101.09459)\] Advances and Challenges in Conversational Recommender Systems: A Survey  
5. \[[5](http://arxiv.org/abs/2007.00194)\] Interactive Path Reasoning on Graph for Conversational Recommendation  
6. \[[6](http://arxiv.org/abs/2007.04032)\] Improving Conversational Recommender Systems via Knowledge Graph based Semantic Fusion  
7. \[[7](https://www.semanticscholar.org/paper/0056038b89647afcee84226adf19feb1023a54c0)\] Learning to Infer User Implicit Preference in Conversational Recommendation  
8. \[[8](http://arxiv.org/abs/2105.09710)\] Unified Conversational Recommendation Policy Learning via Graph-based Reinforcement Learning  
9. \[[9](https://www.semanticscholar.org/paper/49846c2d069c324d5d3f3b53cb74b13e84b7caeb)\] Variational Reasoning about User Preferences for Conversational Recommendation  
10. \[[10](http://arxiv.org/abs/1806.03277)\] Conversational Recommender System  
11. \[[11](http://arxiv.org/abs/2304.13874)\] Exploiting Simulated User Feedback for Conversational Search: Ranking, Rewriting, and Beyond  
12. \[[12](http://arxiv.org/abs/2010.04125)\] Towards Topic-Guided Conversational Recommender System  
13. \[[13](http://arxiv.org/abs/2006.08732)\] Evaluating Conversational Recommender Systems via User Simulation  
14. \[[14](http://arxiv.org/abs/2206.09363)\] Towards Unified Conversational Recommender Systems via Knowledge-Enhanced Prompt Learning  
15. \[[15](http://arxiv.org/abs/1107.0029)\] A Personalized System for Conversational Recommendations  
16. \[[16](https://www.semanticscholar.org/paper/33e0fe2d4cf01b16da89ab0c180cdcbf37b3be17)\] Adapting User Preference to Online Feedback in Multi-round Conversational Recommendation
