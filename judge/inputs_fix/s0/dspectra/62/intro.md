## Related Works

Generative retrieval has emerged as a promising paradigm that replaces traditional search index data structures with a single large-scale neural network, enabling improved efficiency and seamless integration with generative large language models \[[11](http://arxiv.org/abs/2311.09134)\]. This approach directly generates document identifiers through corpus-specific constrained decoding, offering a unified end-to-end framework for retrieval \[[11](http://arxiv.org/abs/2311.09134)\]. However, the generalization capabilities of generative retrieval on out-of-distribution corpora remain a critical challenge \[[11](http://arxiv.org/abs/2311.09134)\].

Several works have explored the effectiveness of generative retrieval on large-scale corpora. For instance, the Differentiable Search Index has been popularized for its ability to encode an entire document corpus within a single Transformer model \[[13](http://arxiv.org/abs/2501.11034)\]. This paradigm has been evaluated on document corpora of up to 100k in size, but scaling to millions of passages remains an unsolved challenge \[[3](http://arxiv.org/abs/2305.11841)\]. Recent studies have shown that generative retrieval is competitive with state-of-the-art dual encoders on small corpora, but scaling to larger datasets requires careful consideration of synthetic queries and compute costs \[[3](http://arxiv.org/abs/2305.11841)\].

The use of beam search in generative retrieval has also been extensively studied. While beam search is the go-to method for decoding auto-regressive models, it is agnostic to end metrics and may not optimize for the desired ranking objective \[[8](http://arxiv.org/abs/2104.05336)\]. This limitation has motivated the development of alternative decoding strategies, such as Monte-Carlo Tree Search (MCTS), which can be more metric-driven \[[8](http://arxiv.org/abs/2104.05336)\]. Additionally, Diverse Beam Search (DBS) has been proposed to generate a list of diverse outputs by optimizing for a diversity-augmented objective, leading to better top-1 solutions with minimal computational overhead \[[4](http://arxiv.org/abs/1610.02424)\].

In the context of retrieval-augmented generation (RAG), several studies have explored how to integrate retrieval with generation to improve performance on knowledge-intensive tasks. For example, RAG models combine pre-trained parametric and non-parametric memory, using a dense vector index of Wikipedia for retrieval \[[5](http://arxiv.org/abs/2005.11401)\]. These models have been shown to outperform parametric seq2seq models and task-specific retrieve-and-extract architectures \[[5](http://arxiv.org/abs/2005.11401)\]. Similarly, the CorpusBrain model replaces the traditional "index-retrieve-then-rank" pipeline with a single-step generative model, enabling end-to-end optimization and significantly improving retrieval performance on the KILT benchmark \[[6](http://arxiv.org/abs/2208.07652)\].

Moreover, the use of contrastive learning for unsupervised dense retrieval has shown promising results, outperforming BM25 on 11 out of 15 datasets for the Recall@100 metric \[[10](http://arxiv.org/abs/2112.09118)\]. This approach enables strong performance in various retrieval settings, even when training data is scarce \[[10](http://arxiv.org/abs/2112.09118)\]. Additionally, the coCondenser model, which introduces an unsupervised corpus-level contrastive loss, has demonstrated comparable performance to RocketQA using simple small batch fine-tuning \[[7](http://arxiv.org/abs/2108.05540)\].

In summary, while generative retrieval offers a promising alternative to traditional retrieval methods, several challenges remain, including the generalization of constrained auto-regressive generation and the effectiveness of beam search in capturing the desired ranking objective. These challenges are the focus of this paper.

References:  
\[[1](http://arxiv.org/abs/2404.07220)\] Blended RAG: Improving RAG (Retriever-Augmented Generation) Accuracy with Semantic Search and Hybrid Query-Based Retrievers  
\[[2](http://arxiv.org/abs/2204.10628)\] Autoregressive Search Engines: Generating Substrings as Document Identifiers  
\[[3](http://arxiv.org/abs/2305.11841)\] How Does Generative Retrieval Scale to Millions of Passages?  
\[[4](http://arxiv.org/abs/1610.02424)\] Diverse Beam Search: Decoding Diverse Solutions from Neural Sequence Models  
\[[5](http://arxiv.org/abs/2005.11401)\] Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks  
\[[6](http://arxiv.org/abs/2208.07652)\] CorpusBrain: Pre-train a Generative Retrieval Model for Knowledge-Intensive Language Tasks  
\[[7](http://arxiv.org/abs/2108.05540)\] Unsupervised Corpus Aware Language Model Pre-training for Dense Passage Retrieval  
\[[8](http://arxiv.org/abs/2104.05336)\] Machine Translation Decoding beyond Beam Search  
\[[9](http://arxiv.org/abs/2306.15222)\] Learning to Rank in Generative Retrieval  
\[[10](http://arxiv.org/abs/2112.09118)\] Unsupervised Dense Information Retrieval with Contrastive Learning  
\[[11](http://arxiv.org/abs/2311.09134)\] Scalable and Effective Generative Information Retrieval
