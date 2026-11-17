## Related Works

Generative retrieval (GR) has emerged as a transformative paradigm in information retrieval (IR), shifting from the traditional index-retrieve-then-rank pipeline to directly generating document identifiers (docids) for queries using sequence-to-sequence models \[[https://www.semanticscholar.org/paper/5beaeee1e27007bd12967480bb9c379cebd15e6e](https://www.semanticscholar.org/paper/5beaeee1e27007bd12967480bb9c379cebd15e6e)\]\[[2404.14851](http://arxiv.org/abs/2404.14851)\]. This approach leverages the parametric capacity of neural networks to memorize and retrieve documents end-to-end, eliminating explicit indexing. Early GR models primarily used fixed or static docids, such as titles or clustering-based numeric codes, which often limited semantic expressiveness and model adaptability \[[https://www.semanticscholar.org/paper/6682a3679a17d090830635f1c420126d20eae54a](https://www.semanticscholar.org/paper/6682a3679a17d090830635f1c420126d20eae54a)\]\[[2304.04171](http://arxiv.org/abs/2304.04171)\]\[[2305.13859](http://arxiv.org/abs/2305.13859)\]. 

### Docid Design and Semantic Alignment

Docid design is a critical factor influencing GR performance. Text-based docids, including n-grams, synthetic queries, or title-based identifiers, offer strong semantic alignment with pretrained language models, facilitating better generalization, especially for unseen documents \[[https://www.semanticscholar.org/paper/6682a3679a17d090830635f1c420126d20eae54a](https://www.semanticscholar.org/paper/6682a3679a17d090830635f1c420126d20eae54a)\]\[[2304.04171](http://arxiv.org/abs/2304.04171)\]\[[2305.13859](http://arxiv.org/abs/2305.13859)\]. Techniques such as GenRet employ discrete autoencoding to learn semantic docids end-to-end, achieving superior retrieval effectiveness by capturing document semantics more faithfully \[[2304.04171](http://arxiv.org/abs/2304.04171)\]. Additionally, frameworks like NOVO optimize docids as sets of unique n-grams, allowing for interpretable and learnable identifiers that enhance semantic and lexical diversity \[[https://www.semanticscholar.org/paper/6682a3679a17d090830635f1c420126d20eae54a](https://www.semanticscholar.org/paper/6682a3679a17d090830635f1c420126d20eae54a)\]. Contrastingly, numeric-based docids, though computationally efficient, tend to overfit initial document sets and exhibit decreased performance when applied to dynamic corpora with evolving document collections \[[2305.18952](http://arxiv.org/abs/2305.18952)\]\[[2311.09134](http://arxiv.org/abs/2311.09134)\].

### Generative Retrieval in Dynamic Corpora

Most GR research has focused on static corpora, which do not reflect real-world scenarios where document collections are dynamic and continuously updated. Recent studies explicitly address this gap by evaluating GR models on dynamic corpora. For instance, CLEVER introduces a continual learning framework that incrementally updates document representations using an adaptive quantization technique and memory-augmented learning, enabling GR models to incorporate new documents without forgetting prior knowledge \[[2308.14968](http://arxiv.org/abs/2308.14968)\]. Empirical results demonstrate that text-based docids outperform numeric-based ones in dynamic settings due to their semantic granularity and lexical richness, which helps maintain retrieval quality as the corpus evolves \[[2305.18952](http://arxiv.org/abs/2305.18952)\]\[[2308.14968](http://arxiv.org/abs/2308.14968)\].

Moreover, few-shot indexing approaches have been proposed to reduce training overhead and improve adaptability by employing large language models (LLMs) to generate docids without extensive retraining \[[2408.02152](http://arxiv.org/abs/2408.02152)\]. This method achieves competitive performance on dynamic corpora by leveraging pretrained knowledge and constraining retrieval to a preconstructed docid bank, thus blending efficiency with semantic relevance.

### Optimization and Ranking Strategies

Optimization techniques tailored for GR have evolved to address token-level misalignment and ranking effectiveness. Direct Document Relevance Optimization (DDRO) aligns token generation with document-level relevance through pairwise ranking, outperforming reinforcement learning-based approaches while simplifying training complexity \[[2504.05181](http://arxiv.org/abs/2504.05181)\]. Similarly, listwise generative retrieval models refine ranking by treating docid generation as a sequential prediction problem, optimizing the relevance of the entire returned document list rather than individual docids independently \[[2403.12499](http://arxiv.org/abs/2403.12499)\]. These methods improve retrieval accuracy by better modeling dependencies among documents in ranked lists.

### Addressing Docid Generation Challenges

Token-by-token generation of docids in GR faces challenges such as error propagation and limited context during decoding. Term-Set Generation (TSGen) addresses this by representing docids as permutation-invariant sets of terms, enabling flexible decoding orders and reducing the risk of pruning relevant tokens prematurely \[[2305.13859](http://arxiv.org/abs/2305.13859)\]. This approach enhances robustness and scalability, crucial for large-scale and dynamic retrieval scenarios.

Other innovative approaches include Translational Generative Retrieval, which models documents as distributions over potential queries to capture multi-topic semantics, and CorpusLM, which unifies GR with downstream knowledge-intensive tasks by integrating docid generation with retrieval-augmented generation techniques \[[2402.01176](http://arxiv.org/abs/2402.01176)\]\[[https://www.semanticscholar.org/paper/c0877659a3af5c0da6b1e69589787fdbbbaaf39a](https://www.semanticscholar.org/paper/c0877659a3af5c0da6b1e69589787fdbbbaaf39a)\]. These methods aim to enrich document representations and improve retrieval quality beyond straightforward docid generation.

### Summary

In summary, recent advances in generative retrieval highlight the importance of semantic, fine-grained, and interpretable docid designs to improve generalization and robustness, especially in dynamic corpora where documents continuously evolve. Text-based docids demonstrate superior adaptability and retrieval effectiveness compared to numeric-based counterparts, which, despite their efficiency, suffer from overfitting and performance degradation in changing environments \[[2305.18952](http://arxiv.org/abs/2305.18952)\]\[[2308.14968](http://arxiv.org/abs/2308.14968)\]\[[2304.04171](http://arxiv.org/abs/2304.04171)\]. Continual learning mechanisms and few-shot indexing strategies further enhance GR applicability to dynamic settings by enabling incremental updates without full retraining \[[2308.14968](http://arxiv.org/abs/2308.14968)\]\[[2408.02152](http://arxiv.org/abs/2408.02152)\]. Optimization methods focusing on document-level relevance and listwise ranking have also contributed to improved retrieval accuracy \[[2504.05181](http://arxiv.org/abs/2504.05181)\]\[[2403.12499](http://arxiv.org/abs/2403.12499)\]. Finally, novel decoding frameworks like TSGen and translational retrieval models tackle inherent challenges in docid generation, paving the way for more resilient and scalable GR systems \[[https://www.semanticscholar.org/paper/c0877659a3af5c0da6b1e69589787fdbbbaaf39a](https://www.semanticscholar.org/paper/c0877659a3af5c0da6b1e69589787fdbbbaaf39a)\]\[[2305.13859](http://arxiv.org/abs/2305.13859)\].

### References

1. http://arxiv.org/abs/2305.18952v5  
2. http://arxiv.org/abs/2308.14968v2  
3. http://arxiv.org/abs/2308.14968v2  
4. http://arxiv.org/abs/6682a3679a17d090830635f1c420126d20eae54a  
6. http://arxiv.org/abs/2304.04171v1  
7. http://arxiv.org/abs/2504.05181  
10. http://arxiv.org/abs/2408.02152  
11. http://arxiv.org/abs/2403.12499  
12. http://arxiv.org/abs/2402.01176  
14. https://www.semanticscholar.org/paper/c0877659a3af5c0da6b1e69589787fdbbbaaf39a  
15. http://arxiv.org/abs/2404.14851  
16. http://arxiv.org/abs/2311.09134  
17. http://arxiv.org/abs/2305.13859