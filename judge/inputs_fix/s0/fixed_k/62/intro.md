## Related Works

Generative retrieval has emerged as a promising paradigm that replaces traditional search index data structures with a single large-scale neural network, enabling end-to-end optimization toward a unified retrieval objective \[[14](http://arxiv.org/abs/2504.05181)\]. This approach directly generates document identifiers (docids) through corpus-specific constrained decoding, offering improved efficiency and seamless integration with generative large language models \[[14](http://arxiv.org/abs/2504.05181)\]. However, constrained auto-regressive generation faces inherent limitations, particularly in terms of constraint satisfaction and beam search optimization \[[14](http://arxiv.org/abs/2504.05181)\].

Several works have explored constrained decoding for controlled text generation. For instance, Discrete Auto-regressive Biasing (DAB) introduces a joint distribution over the generated sequence and an auxiliary bias sequence, leveraging gradient-based discrete MCMC for efficient sampling \[[1](http://arxiv.org/abs/2502.03685)\]. This method improves constraint satisfaction while maintaining fluency, making it relevant to the challenges of generative retrieval. Similarly, the work on Nonparametric Decoding (Np Decoding) enhances generative retrieval by using nonparametric contextualized vocab embeddings, allowing models to utilize both parametric and nonparametric spaces \[[4](http://arxiv.org/abs/2210.02068)\].

Beam search, a widely used decoding method in machine translation, has been criticized for its inability to optimize for end metrics beyond model likelihood \[[3](http://arxiv.org/abs/2104.05336)\]. This limitation is particularly relevant in generative retrieval, where the goal is to generate relevant docids. Monte Carlo Tree Search (MCTS) has been proposed as a more powerful metric-driven search technique, showing competitiveness in various metrics \[[3](http://arxiv.org/abs/2104.05336)\]. Additionally, the work on PAG (Planning Ahead in Generative Retrieval) introduces a simultaneous decoding approach that guides autoregressive generation of docids through set-based and sequential identifiers, achieving significant improvements in performance and speed \[[6](http://arxiv.org/abs/2404.14600)\].

In the context of retrieval-augmented generation (RAG), several challenges remain, such as the non-monotonic utility of retrieved chunks and the lack of adaptability to different query characteristics \[[5](http://arxiv.org/abs/2411.00744)\]. CARROT addresses these issues by employing an MCTS-based strategy to find optimal chunk combinations and introducing a configuration agent to predict optimal settings for each query domain \[[5](http://arxiv.org/abs/2411.00744)\]. These advancements are crucial for improving the generalization capabilities of generative retrieval on out-of-distribution corpora.

Moreover, diverse beam search (DBS) has been proposed to generate a list of diverse outputs by optimizing for a diversity-augmented objective, outperforming traditional beam search in terms of both computational efficiency and retrieval performance \[[8](http://arxiv.org/abs/1610.02424)\]. This method is particularly relevant for generative retrieval, where diversity in generated docids can improve coverage and relevance.

In summary, while generative retrieval offers significant advantages over traditional search paradigms, it faces challenges in constrained decoding and beam search optimization. Recent advances in MCTS, nonparametric decoding, and diverse beam search provide promising directions for improving the generalization and robustness of generative retrieval systems.

### References

1. \[[1](http://arxiv.org/abs/2502.03685)\] Controlled LLM Decoding via Discrete Auto-regressive Biasing [http://arxiv.org/abs/2502.03685]
2. \[[2](http://arxiv.org/abs/2408.02152)\] Generative Retrieval with Few-shot Indexing [http://arxiv.org/abs/2408.02152]
3. \[[3](http://arxiv.org/abs/2104.05336)\] Machine Translation Decoding beyond Beam Search [http://arxiv.org/abs/2104.05336]
4. \[[4](http://arxiv.org/abs/2210.02068)\] Nonparametric Decoding for Generative Retrieval [http://arxiv.org/abs/2210.02068]
5. \[[5](http://arxiv.org/abs/2411.00744)\] CARROT: A Learned Cost-Constrained Retrieval Optimization System for RAG [http://arxiv.org/abs/2411.00744]
6. \[[6](http://arxiv.org/abs/2404.14600)\] Planning Ahead in Generative Retrieval: Guiding Autoregressive Generation through Simultaneous Decoding [http://arxiv.org/abs/2404.14600]
7. \[[7](http://arxiv.org/abs/2404.07220)\] Blended RAG: Improving RAG (Retriever-Augmented Generation) Accuracy with Semantic Search and Hybrid Query-Based Retrievers [http://arxiv.org/abs/2404.07220]
8. \[[8](http://arxiv.org/abs/1610.02424)\] Diverse Beam Search: Decoding Diverse Solutions from Neural Sequence Models [http://arxiv.org/abs/1610.02424]
9. \[[9](http://arxiv.org/abs/2401.06761)\] APAR: LLMs Can Do Auto-Parallel Auto-Regressive Decoding [http://arxiv.org/abs/2401.06761]
10. \[[10](http://arxiv.org/abs/2404.08137)\] Generative Information Retrieval Evaluation [http://arxiv.org/abs/2404.08137]
11. \[[11](http://arxiv.org/abs/2010.10789)\] ProphetNet-Ads: A Looking Ahead Strategy for Generative Retrieval Models in Sponsored Search Engine [http://arxiv.org/abs/2010.10789]
12. \[[12](http://arxiv.org/abs/2406.18960)\] A Surprisingly Simple yet Effective Multi-Query Rewriting Method for Conversational Passage Retrieval [http://arxiv.org/abs/2406.18960]
13. \[[13](http://arxiv.org/abs/1909.09485)\] BSDAR: Beam Search Decoding with Attention Reward in Neural Keyphrase Generation [http://arxiv.org/abs/1909.09485]
14. \[[14](http://arxiv.org/abs/2504.05181)\] Lightweight and Direct Document Relevance Optimization for Generative Information Retrieval [http://arxiv.org/abs/2504.05181]
