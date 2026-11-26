## Related Works

Generative retrieval (GR) has recently gained significant attention as a novel paradigm in information retrieval (IR), offering a direct mapping from queries to relevant document identifiers (docids) without the need for traditional indexing or reranking \[[15](http://arxiv.org/abs/2406.01197)\]. This approach leverages sequence-to-sequence models to generate docids, enabling end-to-end learning of retrieval tasks \[[15](http://arxiv.org/abs/2406.01197)\]. However, most existing GR models are primarily evaluated on static document collections, with limited exploration of their performance in dynamic corpora where documents are continuously added \[[1](http://arxiv.org/abs/2308.14968)\]. This section reviews related works that address the challenges of GR in dynamic settings, docid design, and model efficiency.

Several studies have explored the use of text-based docids in GR, which are often generated as natural language sequences such as titles or n-grams \[[3](https://www.semanticscholar.org/paper/6682a3679a17d090830635f1c420126d20eae54a)\]. These docids benefit from the pre-trained knowledge of language models, allowing for better semantic alignment and fine-grained representation of documents \[[16](http://arxiv.org/abs/2409.18409)\]. In contrast, numeric-based docids, which are typically fixed identifiers assigned during preprocessing, are more efficient but suffer from poor generalization to unseen documents \[[1](http://arxiv.org/abs/2308.14968)\]. This is attributed to their tendency to overfit to the initial document set, leading to suboptimal performance in dynamic environments \[[1](http://arxiv.org/abs/2308.14968)\]. 

The importance of docid design in GR has been highlighted in several works. For instance, \[[3](https://www.semanticscholar.org/paper/6682a3679a17d090830635f1c420126d20eae54a)\] proposes NOVO docids, which are learnable and interpretable n-gram sets that can be optimized during training to capture semantic relationships between documents. Similarly, \[[13](http://arxiv.org/abs/2305.13859)\] introduces Term-Set Generation (TSGen), which uses a set of terms as docids to improve retrieval accuracy by avoiding token pruning errors. These approaches emphasize the need for flexible and semantically rich docid representations that can adapt to evolving document collections.

Efforts to improve the scalability of GR to large-scale corpora have also been explored. \[[10](http://arxiv.org/abs/2305.11841)\] investigates how generative retrieval scales to millions of passages, finding that synthetic queries are crucial for indexing, while existing architectural modifications are often ineffective when considering computational costs. \[[14](http://arxiv.org/abs/2311.09134)\] proposes RIPOR, an optimization framework that enhances the accuracy of relevance estimation during sequential docid generation, achieving significant improvements on standard benchmarks. These studies underscore the challenges of deploying GR in real-world scenarios with large and dynamic document collections.

In addition, \[[7](http://arxiv.org/abs/2408.02152)\] introduces Few-Shot GR, which eliminates the need for extensive training by prompting large language models (LLMs) to generate docids during indexing. This approach reduces training costs and enables rapid adaptation to new documents. \[[17](http://arxiv.org/abs/2310.12455)\] further advances this idea by proposing an end-to-end retrieval paradigm that automatically learns optimal docids for both existing and new documents, demonstrating the potential of fully automated GR systems.

Overall, the literature highlights the trade-offs between efficiency and effectiveness in GR, with text-based docids offering better performance in dynamic settings but at the cost of computational overhead. Future work should focus on hybrid approaches that combine the strengths of both numeric and text-based docids \[[1](http://arxiv.org/abs/2308.14968)\].

### References

1. \[[1](http://arxiv.org/abs/2308.14968)\] Continual Learning for Generative Retrieval over Dynamic Corpora  
2. \[[3](https://www.semanticscholar.org/paper/6682a3679a17d090830635f1c420126d20eae54a)\] NOVO: Learnable and Interpretable Document Identifiers for Model-Based IR  
3. \[[7](http://arxiv.org/abs/2408.02152)\] Generative Retrieval with Few-shot Indexing  
4. \[[10](http://arxiv.org/abs/2305.11841)\] How Does Generative Retrieval Scale to Millions of Passages?  
5. \[[13](http://arxiv.org/abs/2305.13859)\] Generative Retrieval via Term Set Generation  
6. \[[14](http://arxiv.org/abs/2311.09134)\] Scalable and Effective Generative Information Retrieval  
7. \[[15](http://arxiv.org/abs/2406.01197)\] A Survey of Generative Information Retrieval  
8. \[[16](http://arxiv.org/abs/2409.18409)\] Generative Retrieval Meets Multi-Graded Relevance  
9. \[[17](http://arxiv.org/abs/2310.12455)\] Auto Search Indexer for End-to-End Document Retrieval
