## Related Works

Generative retrieval (GR) has emerged as a promising paradigm in information retrieval (IR), offering an end-to-end approach to document retrieval by generating document identifiers (docids) directly from queries \[[Jiangui Chen' 2023-08-29](http://arxiv.org/abs/2308.14968v2)\]. However, most existing GR models are primarily evaluated on static document collections, and their performance on dynamic corpora, where documents are continuously added or modified, remains underexplored \[[Weiwei Sun' 2023-04-09](http://arxiv.org/abs/2304.04171v1)\]. This section reviews related works that address dynamic retrieval, GR models, and their limitations, providing a foundation for the current study.

Early GR models focused on generating docids based on text-based or numeric-based representations \[[Jiangui Chen' 2023-08-29](http://arxiv.org/abs/2308.14968v2)\]. Text-based docids, such as titles or n-grams, leverage the semantic information of documents, enabling better alignment with pre-trained language models \[[Gustavo Penha' 2021-11-25](http://arxiv.org/abs/2111.13057v3)\]. In contrast, numeric-based docids, often derived from clustering or hashing techniques, offer efficiency but lack semantic richness \[[Gustavo Penha' 2021-11-25](http://arxiv.org/abs/2111.13057v3)\]. Recent works have highlighted the limitations of numeric-based docids in dynamic settings, where models may overfit to the training data and fail to generalize to new documents \[[Weiwei Sun' 2023-04-09](http://arxiv.org/abs/2304.04171v1)\]. For instance, \[[Weiwei Sun' 2023-04-09](http://arxiv.org/abs/2304.04171v1)\] found that numeric-based docids tend to favor the initial document set, leading to poor performance when the corpus evolves.

Several studies have explored the generalization of GR models to unseen documents. \[[Gustavo Penha' 2021-11-25](http://arxiv.org/abs/2111.13057v3)\] proposed a method for learning to tokenize documents into short discrete representations (docids) using a discrete auto-encoding approach, which improved the generalization of GR models. Similarly, \[[Arian Askari' 2024-08-04](http://arxiv.org/abs/2408.02152v3)\] introduced GenRet, a method that learns semantic docids in an end-to-end manner, achieving state-of-the-art performance on benchmark datasets. These works demonstrate the importance of semantic alignment in GR models for dynamic retrieval.

In addition to GR models, there has been growing interest in the performance of retrieval-augmented generation (RAG) systems in dynamic environments \[[Arian Askari' 2024-08-04](http://arxiv.org/abs/2408.02152v3)\]. \[[Arian Askari' 2024-08-04](http://arxiv.org/abs/2408.02152v3)\] proposed CLEVER, a continual learning model for GR that enables incremental indexing of new documents while preserving the ability to answer queries with both previously and newly indexed documents. This work addresses the practical challenge of applying GR models to dynamic corpora.

The limitations of numeric-based docids in dynamic settings have also been studied in the context of generative retrieval. \[[Weiwei Sun' 2023-04-09](http://arxiv.org/abs/2304.04171v1)\] found that numeric-based docids suffer from performance degradation over dynamic corpora due to overfitting on the training set. This aligns with findings from \[[Gustavo Penha' 2021-11-25](http://arxiv.org/abs/2111.13057v3)\], which emphasized the importance of fine-grained docid design for better generalization.

Finally, \[[Arian Askari' 2024-08-04](http://arxiv.org/abs/2408.02152v3)\] proposed Few-Shot GR, a few-shot indexing-based GR framework that eliminates the need for extensive training, allowing for rapid indexing of new documents. This approach has shown superior performance to state-of-the-art GR methods requiring heavy training \[[Arian Askari' 2024-08-04](http://arxiv.org/abs/2408.02152v3)\].

### References

1. http://arxiv.org/abs/2305.18952v5  
2. http://arxiv.org/abs/2308.14968v2  
3. http://arxiv.org/abs/2304.04171v1  
4. http://arxiv.org/abs/2308.14968v2  
5. http://arxiv.org/abs/2408.02152v3  
6. http://arxiv.org/abs/2308.14968v2
