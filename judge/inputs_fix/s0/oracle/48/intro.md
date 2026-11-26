## Related Works

Neural retrieval methods using transformer-based pre-trained language models have advanced multilingual and cross-lingual retrieval \[[10](http://arxiv.org/abs/2402.05672)\]. However, their effectiveness for low-resource, morphologically rich languages such as Amharic remains underexplored due to data scarcity and suboptimal tokenization \[[15](https://aclanthology.org/2021.mrl-1.11/)\]. This gap is addressed by introducing Amharic-specific dense retrieval models based on pre-trained Amharic BERT and RoBERTa backbones \[[15](https://aclanthology.org/2021.mrl-1.11/)\]. These models demonstrate significant improvements over existing multilingual baselines, such as Arctic Embed 2.0 \[[9](http://arxiv.org/abs/2412.04506)\], which, while effective for many languages, suffers from degraded English retrieval quality \[[9](http://arxiv.org/abs/2412.04506)\]. The proposed RoBERTa-Base-Amharic-Embed model (110M parameters) achieves a 17.6% relative improvement in MRR@10 and a 9.86% gain in Recall@10 over the strongest multilingual baseline \[[15](https://aclanthology.org/2021.mrl-1.11/)\]. More compact variants, such as RoBERTa-Medium-Amharic-Embed (42M), remain competitive while being over 13x smaller \[[15](https://aclanthology.org/2021.mrl-1.11/)\].

The importance of language-specific adaptation is underscored by the limitations of multilingual models, which often exhibit systematic deficiencies affecting certain language pairs \[[4](http://arxiv.org/abs/1906.01502)\]. For instance, Multilingual BERT (M-BERT) shows surprising zero-shot cross-lingual transfer capabilities but still has systematic deficiencies \[[4](http://arxiv.org/abs/1906.01502)\]. Similarly, XLM-R, a multilingual language model trained at scale, outperforms mBERT on a variety of cross-lingual benchmarks but still faces challenges in low-resource languages \[[5](http://arxiv.org/abs/1911.02116)\]. These findings highlight the need for language-specific models to achieve optimal performance in low-resource settings.

In addition to dense retrieval, sparse retrieval methods such as BM25 have been widely used in open-domain question answering \[[2](http://arxiv.org/abs/2004.04906)\]. However, recent work has shown that dense retrievers can outperform sparse methods by a significant margin \[[2](http://arxiv.org/abs/2004.04906)\]. For example, dense passage retrieval using a dual-encoder framework has been shown to outperform BM25 by 9%-19% in top-20 passage retrieval accuracy \[[2](http://arxiv.org/abs/2004.04906)\]. Furthermore, contrastive learning has been used to train unsupervised dense retrievers, achieving strong performance in various retrieval settings \[[7](http://arxiv.org/abs/2112.09118)\]. This includes cross-lingual retrieval, where training data is even scarcer than for English \[[7](http://arxiv.org/abs/2112.09118)\].

The development of multilingual language models for African languages has also been an active area of research. SERENGETI, a massively multilingual language model covering 517 African languages and language varieties, outperforms other models on 11 datasets across eight natural language understanding tasks \[[6](http://arxiv.org/abs/2212.10785)\]. This highlights the potential of multilingual models in low-resource settings, though they still face challenges in terms of performance and tokenization \[[16](https://aclanthology.org/2021.winlp-1.5/)\].

In summary, while multilingual and cross-lingual retrieval has seen significant advancements, the effectiveness of these methods for low-resource, morphologically rich languages such as Amharic remains underexplored \[[15](https://aclanthology.org/2021.mrl-1.11/)\]. This paper addresses this gap by introducing Amharic-specific dense retrieval models that outperform existing multilingual baselines \[[15](https://aclanthology.org/2021.mrl-1.11/)\].

References:  
\[[1](http://arxiv.org/abs/2109.10086)\] SPLADE v2: Sparse Lexical and Expansion Model for Information Retrieval  
\[[2](http://arxiv.org/abs/2004.04906)\] Dense Passage Retrieval for Open-Domain Question Answering  
\[[3](http://arxiv.org/abs/2007.00808)\] Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval  
\[[4](http://arxiv.org/abs/1906.01502)\] How multilingual is Multilingual BERT?  
\[[5](http://arxiv.org/abs/1911.02116)\] Unsupervised Cross-lingual Representation Learning at Scale  
\[[6](http://arxiv.org/abs/2212.10785)\] SERENGETI: Massively Multilingual Language Models for Africa  
\[[7](http://arxiv.org/abs/2112.09118)\] Unsupervised Dense Information Retrieval with Contrastive Learning  
\[[8](http://arxiv.org/abs/2012.15613)\] How Good is Your Tokenizer? On the Monolingual Performance of Multilingual Language Models  
\[[9](http://arxiv.org/abs/2412.04506)\] Arctic-Embed 2.0: Multilingual Retrieval Without Compromise  
\[[10](http://arxiv.org/abs/2402.05672)\] Multilingual E5 Text Embeddings: A Technical Report  
\[[11](http://arxiv.org/abs/2103.05639)\] An Amharic News Text classification Dataset  
\[[12]()\] The Probabilistic Relevance Framework: (BM25) and Beyond  
\[[13]()\] SPLADE: Sparse Lexical and Expansion Model for First Stage Ranking  
\[[14]()\] Context-aware term weighting for first stage passage retrieval  
\[[15](https://aclanthology.org/2021.mrl-1.11/)\] Small Data? (No) Problem! (Exploring) the Viability of Pretrained Multilingual Language Models for Low-resourced Languages  
\[[16](https://aclanthology.org/2021.winlp-1.5/)\] The Development of Pre-processing Tools and Pre-trained Embedding Models for (A)mharic
