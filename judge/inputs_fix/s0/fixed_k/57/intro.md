## Related Works

Generative retrieval (GR) has gained significant attention as a promising paradigm in information retrieval (IR), offering end-to-end modeling of retrieval tasks by generating document identifiers (docids) directly from queries \[[4](http://arxiv.org/abs/2304.04171)\]. However, most existing GR models are primarily evaluated on static document collections, with limited studies on their performance in dynamic corpora where document sets evolve continuously \[[1](http://arxiv.org/abs/2305.18952)\]. This section reviews related works that address the challenges of GR in dynamic environments, the design of docids, and the efficiency-performance trade-offs in retrieval systems.

Early works in GR focused on static document collections, assuming a fixed set of documents during training and inference \[[4](http://arxiv.org/abs/2304.04171)\]. However, in practical scenarios, document collections are often dynamic, requiring models to adapt to new documents while preserving retrieval accuracy \[[2](http://arxiv.org/abs/2308.14968)\]. This challenge has led to the development of continual learning approaches for GR, such as the CLEVER model, which enables incremental indexing of new documents while maintaining query performance \[[2](http://arxiv.org/abs/2308.14968)\]. These methods aim to address the limitations of static indexing, which is computationally expensive and less adaptable to evolving corpora \[[3](http://arxiv.org/abs/2408.02152)\].

The design of docids plays a critical role in GR performance. Traditional approaches use fixed rule-based docids, such as document titles or clustered BERT embeddings, which often fail to capture semantic information effectively \[[4](http://arxiv.org/abs/2304.04171)\]. Recent work proposes GenRet, a method that learns to tokenize documents into short discrete representations (docids) using a discrete auto-encoding approach, enabling fully end-to-end modeling of retrieval tasks \[[4](http://arxiv.org/abs/2304.04171)\]. This approach improves semantic alignment and generalization to unseen documents, as observed in experiments on benchmark datasets \[[4](http://arxiv.org/abs/2304.04171)\].

The use of text-based docids has shown superior generalization to unseen documents compared to numeric-based docids, which are more efficient but less effective in dynamic settings \[[1](http://arxiv.org/abs/2305.18952)\]. This is attributed to the fine-grained design of text-based docids, which aligns better with the semantic knowledge of large language models (LLMs) \[[1](http://arxiv.org/abs/2305.18952)\]. In contrast, numeric-based docids tend to overfit to the initial document set, leading to performance degradation in dynamic corpora \[[1](http://arxiv.org/abs/2305.18952)\]. This overfitting issue is further exacerbated by the lack of lexical diversity in numeric-based docids, which limits their adaptability to new documents \[[1](http://arxiv.org/abs/2305.18952)\].

To address these limitations, recent work proposes a multi-docid design that combines the efficiency of numeric-based docids with the effectiveness of text-based docids \[[1](http://arxiv.org/abs/2305.18952)\]. This hybrid approach aims to improve retrieval performance in dynamic environments without requiring additional retraining \[[1](http://arxiv.org/abs/2305.18952)\]. Such strategies are crucial for developing generalized yet efficient GR models suitable for real-world search engines \[[1](http://arxiv.org/abs/2305.18952)\].

Further, the generalization capabilities of generative retrieval on out-of-distribution corpora have been explored, highlighting the importance of addressing constraints and beam search limitations in auto-regressive decoding \[[7](http://arxiv.org/abs/2504.09935)\]. These findings underscore the need for more robust and generalizable GR models, particularly in dynamic settings \[[7](http://arxiv.org/abs/2504.09935)\].

References:

1. \[[1](http://arxiv.org/abs/2305.18952)\] http://arxiv.org/abs/2305.18952  
2. \[[2](http://arxiv.org/abs/2308.14968)\] http://arxiv.org/abs/2308.14968  
3. \[[3](http://arxiv.org/abs/2408.02152)\] http://arxiv.org/abs/2408.02152  
4. \[[4](http://arxiv.org/abs/2304.04171)\] http://arxiv.org/abs/2304.04171  
5. \[[5](http://arxiv.org/abs/2504.05181)\] http://arxiv.org/abs/2504.05181  
6. \[[6](http://arxiv.org/abs/2305.13859)\] http://arxiv.org/abs/2305.13859  
7. \[[7](http://arxiv.org/abs/2504.09935)\] http://arxiv.org/abs/2504.09935
