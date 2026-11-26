## Related Works

Cross-Domain Sequential Recommendation (CDSR) has attracted significant attention due to its ability to alleviate data sparsity and cold-start issues by leveraging user interactions across multiple domains \[[1](https://www.semanticscholar.org/paper/f3b7672aaab5b65e1eb66aee6f3a5b95fb0c304f)\]. Traditional approaches often rely on overlapping users to transfer knowledge between domains, which limits their applicability in scenarios with limited overlap \[[2](http://arxiv.org/abs/2401.04971)\]. For instance, methods like EMCDR \[[1](https://www.semanticscholar.org/paper/f3b7672aaab5b65e1eb66aee6f3a5b95fb0c304f)\] and Dual Metric Learning \[[8](http://arxiv.org/abs/2104.08490)\] attempt to address this by utilizing overlapping users and item-level information, but they often struggle with sparse or non-overlapping data \[[3](http://arxiv.org/abs/2304.03891)\]. 

The transition complexity in CDSR arises from the challenge of modeling complex sequential patterns from mixed behavior sequences \[[4](http://arxiv.org/abs/1706.03205)\]. Existing works such as C2DSR \[[3](http://arxiv.org/abs/2304.03891)\] and DDGHM \[[5](http://arxiv.org/abs/2209.10163)\] attempt to capture both intra- and inter-sequence relationships, yet they often fail to effectively integrate cross-domain information due to the lack of semantic alignment \[[6](http://arxiv.org/abs/2406.03085)\]. This is further exacerbated by the limitations of traditional models that rely on ID-based item representations, making it difficult to align items with similar meanings across domains \[[7](http://arxiv.org/abs/2311.04760)\].

Recent advances have explored the use of Large Language Models (LLMs) to enhance CDSR by capturing semantic relationships and user preferences \[[8](http://arxiv.org/abs/2104.08490)\]. For example, LLM-Rec \[[9](http://arxiv.org/abs/2311.04590)\] integrates multi-domain user behaviors and item titles to generate semantically rich representations, improving recommendation accuracy across domains. However, LLMs also face challenges in handling large item repositories and sequential collaborative signals, leading to potential hallucination and unreliable outputs \[[10](http://arxiv.org/abs/2206.08050)\]. To mitigate these issues, LLMCDSR \[[11](http://arxiv.org/abs/2106.02768)\] introduces a framework that leverages LLMs to predict pseudo items within single-domain interactions, enhancing cross-domain modeling while addressing reliability concerns.

Additionally, methods like CA-CDSR \[[12](https://www.semanticscholar.org/paper/6bceab2405e4bbd4dadc16e8b946aa12dbddefc7)\] focus on aligning item representations across domains to improve sequential modeling, while DREAM \[[13](https://www.semanticscholar.org/paper/44ecd5740798b8d90818fde07ea5bfceee22b83b)\] proposes a decoupled representation approach that simultaneously learns single- and cross-domain user preferences. These approaches highlight the importance of semantic alignment and efficient knowledge transfer in CDSR. However, they often lack scalability and robustness in real-world scenarios with sparse or non-overlapping data \[[14](https://www.semanticscholar.org/paper/96bfe33a2503e960153a934e10be91da4d8b13a6)\].

To address these challenges, the proposed LLM4CDSR model introduces a tri-thread framework that integrates a unified representation module, a trainable adapter with contrastive regularization, and a hierarchical LLMs profiling module. This approach enables more effective semantic alignment and cross-domain preference modeling, as demonstrated through extensive experiments on three public datasets \[[15](http://arxiv.org/abs/2305.19860)\].

---

References  
\[[1](https://www.semanticscholar.org/paper/f3b7672aaab5b65e1eb66aee6f3a5b95fb0c304f)\] Semi-Supervised Learning for Cross-Domain Recommendation to Cold-Start Users  
\[[2](http://arxiv.org/abs/2401.04971)\] Dual Metric Learning for Effective and Efficient Cross-Domain Recommendations  
\[[3](http://arxiv.org/abs/2304.03891)\] Contrastive Cross-Domain Sequential Recommendation  
\[[4](http://arxiv.org/abs/1706.03205)\] Cross-Domain Sequential Recommendation (CDSR) aims to predict future interactions based on user's historical sequential interactions from multiple domains  
\[[5](http://arxiv.org/abs/2209.10163)\] DDGHM: Dual Dynamic Graph with Hybrid Metric Training for Cross-Domain Sequential Recommendation  
\[[6](http://arxiv.org/abs/2406.03085)\] Exploring User Retrieval Integration towards Large Language Models for Cross-Domain Sequential Recommendation  
\[[7](http://arxiv.org/abs/2311.04760)\] One Model for All: Large Language Models Are Domain-Agnostic Recommendation Systems  
\[[8](http://arxiv.org/abs/2104.08490)\] A survey on large language models for recommendation  
\[[9](http://arxiv.org/abs/2311.04590)\] One Model for All: Large Language Models Are Domain-Agnostic Recommendation Systems  
\[[10](http://arxiv.org/abs/2206.08050)\] Learning Partially Aligned Item Representation for Cross-Domain Sequential Recommendation  
\[[11](http://arxiv.org/abs/2106.02768)\] LLMCDSR: Enhancing Cross-Domain Sequential Recommendation with Large Language Models  
\[[12](https://www.semanticscholar.org/paper/6bceab2405e4bbd4dadc16e8b946aa12dbddefc7)\] Learning Partially Aligned Item Representation for Cross-Domain Sequential Recommendation  
\[[13](https://www.semanticscholar.org/paper/44ecd5740798b8d90818fde07ea5bfceee22b83b)\] DREAM: Decoupled Representation via Extraction Attention Module and Supervised Contrastive Learning for Cross-Domain Sequential Recommender  
\[[14](https://www.semanticscholar.org/paper/96bfe33a2503e960153a934e10be91da4d8b13a6)\] Transfer Learning via Contextual Invariants for One-to-Many Cross-Domain Recommendation  
\[[15](http://arxiv.org/abs/2305.19860)\] Cross-Domain Sequential Recommendation (CDSR) aims to predict users’ preferences based on historical sequential interactions across multiple domains
