## Related Works

Recent advances in sequential recommendation have focused on modeling user behavior through attention mechanisms and recurrent structures. However, most existing models struggle to effectively capture both temporal dynamics and diverse interaction patterns, particularly in the presence of variable-length sequences \[[1' 2020-01-29](http://arxiv.org/abs/2002.00741v1)\]. This challenge has motivated the development of more sophisticated architectures that integrate attention with state-space modeling or mixture-of-experts (MoE) frameworks \[[2' 2024-04-22](http://arxiv.org/abs/2404.13878v2)\]. 

Several works have explored the use of attention mechanisms to model sequential interactions. For instance, \[[1' 2020-01-29](http://arxiv.org/abs/2002.00741v1)\] introduces a contextualized temporal attention mechanism that dynamically weighs historical actions based on both their content and timing, improving the modeling of user behavior over time. Similarly, \[[8' 2020-12-06](http://arxiv.org/abs/2012.03323v3)\] proposes a knowledge-aware attentive sequential recommendation model (KATRec) that leverages item relationships from a knowledge graph to enhance user preference modeling. These approaches highlight the importance of incorporating both temporal and side information for more accurate recommendations \[[8' 2020-12-06](http://arxiv.org/abs/2012.03323v3)\].

Efforts to improve computational efficiency in sequential recommendation have also led to the development of lightweight models. For example, \[[4' 2023-10-03](http://arxiv.org/abs/2310.02367v2)\] introduces Linear Recurrent Units (LRURec), which offer fast inference and incremental processing by decomposing linear recurrence operations. This model is particularly useful for real-time applications where computational resources are limited. Additionally, \[[11' 2024-02-22](http://arxiv.org/abs/2402.14800v2)\] proposes efficient expert pruning and skipping techniques for MoE models, reducing model size and inference time while maintaining performance. These methods demonstrate the potential of MoE frameworks for scalable recommendation systems \[[11' 2024-02-22](http://arxiv.org/abs/2402.14800v2)\].

The integration of MoE with attention mechanisms has also been explored. \[[6' 2024-10-23](http://arxiv.org/abs/2410.17954v2)\] introduces a sequence-level MoE framework that adaptively routes different behavioral patterns to specialized experts, enabling the model to handle both focused browsing and diverse exploration. This approach aligns with the idea of using MoE to capture heterogeneous user preferences \[[6' 2024-10-23](http://arxiv.org/abs/2410.17954v2)\]. Furthermore, \[[14' 2024-11-12](http://arxiv.org/abs/2411.07569v1)\] proposes a supernet-based model design that allows for automated exploration of architecture and hardware co-design strategies, enhancing the flexibility of recommendation models \[[14' 2024-11-12](http://arxiv.org/abs/2411.07569v1)\].

In addition to attention and MoE, some works have focused on incorporating metadata and contextual information. For example, \[[5' 2021-09-22](http://arxiv.org/abs/2109.11059v2)\] introduces a two-tower model that separately learns user and item representations, leveraging metadata such as text descriptions and cover-art images to improve recommendations for cold-start items. This approach demonstrates the value of combining explicit metadata with sequential behavior for more personalized recommendations \[[5' 2021-09-22](http://arxiv.org/abs/2109.11059v2)\].

Finally, \[[15' 2023-05-22](http://arxiv.org/abs/2305.12976v1)\] explores the use of graph-based models to incorporate textual content and high-order user-item interactions, improving the performance of top-N recommendation. This work highlights the importance of integrating both textual and structural information for more accurate modeling of user preferences \[[15' 2023-05-22](http://arxiv.org/abs/2305.12976v1)\].

These related works collectively emphasize the need for models that can effectively capture diverse user behaviors, handle variable-length sequences, and incorporate both temporal and contextual information. The proposed STAR-Rec model addresses these challenges by combining preference-aware attention with state-space modeling and a sequence-level MoE framework, offering a more flexible and efficient approach to sequential recommendation.

References:  
\[[1' 2020-01-29](http://arxiv.org/abs/2002.00741v1)\] Déjà vu: A Contextualized Temporal Attention Mechanism for Sequential Recommendation  
\[[2' 2024-04-22](http://arxiv.org/abs/2404.13878v2)\] Linear Recurrent Units for Sequential Recommendation  
\[[3' 2025-03-05](http://arxiv.org/abs/2503.03213v1)\] Convergence Rates for Softmax Gating Mixture of Experts  
\[[4' 2023-10-03](http://arxiv.org/abs/2310.02367v2)\] Linear Recurrent Units for Sequential Recommendation  
\[[5' 2021-09-22](http://arxiv.org/abs/2109.11059v2)\] Exploring Heterogeneous Metadata for Video Recommendation with Two-tower Model  
\[[6' 2024-10-23](http://arxiv.org/abs/2410.17954v2)\] ExpertFlow: Efficient Mixture-of-Experts Inference via Predictive Expert Caching and Token Scheduling  
\[[7' 2018-06-21](http://arxiv.org/abs/1806.08200v1)\] Mixtures of Experts Models  
\[[8' 2020-12-06](http://arxiv.org/abs/2012.03323v3)\] KATRec: Knowledge Aware aTtentive Sequential Recommendations  
\[[9' 2020-02-12](http://arxiv.org/abs/2002.05063v1)\] A Bayesian Approach to Conversational Recommendation Systems  
\[[10' 2022-09-14](http://arxiv.org/abs/2209.11801v1)\] Solutions to preference manipulation in recommender systems require knowledge of meta-preferences  
\[[11' 2024-02-22](http://arxiv.org/abs/2402.14800v2)\] Not All Experts are Equal: Efficient Expert Pruning and Skipping for Mixture-of-Experts Large Language Models  
\[[12' 2022-10-04](http://arxiv.org/abs/2210.01942v1)\] IGNiteR: News Recommendation in Microblogging Applications (Extended Version)  
\[[13' 2010-02-05](http://arxiv.org/abs/1002.1150v1)\] Finding Sequential Patterns from Large Sequence Data  
\[[14' 2024-11-12](http://arxiv.org/abs/2411.07569v1)\] Towards Automated Model Design on Recommender Systems  
\[[15' 2023-05-22](http://arxiv.org/abs/2305.12976v1)\] Attentive Graph-based Text-aware Preference Modeling for Top-N Recommendation
