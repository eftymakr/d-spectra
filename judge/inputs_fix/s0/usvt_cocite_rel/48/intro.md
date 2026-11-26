## Related Works

Neural retrieval methods using transformer-based pre-trained language models have significantly advanced multilingual and cross-lingual retrieval \[[1](http://arxiv.org/abs/2004.12832)\]. However, their effectiveness for low-resource, morphologically rich languages such as Amharic remains underexplored due to data scarcity and suboptimal tokenization \[[1](http://arxiv.org/abs/2004.12832)\]. This challenge is not unique to Amharic; similar issues have been observed in other low-resource languages, where the lack of parallel data and the complexity of morphological structures hinder the performance of multilingual models \[[25](http://arxiv.org/abs/2301.12566)\]. 

Several approaches have been proposed to address these limitations. For instance, ColBERT introduces a late interaction architecture that independently encodes the query and the document using BERT and then employs a cheap yet powerful interaction step that models their fine-grained similarity \[[1](http://arxiv.org/abs/2004.12832)\]. This approach allows for efficient retrieval while maintaining high effectiveness \[[1](http://arxiv.org/abs/2004.12832)\]. Similarly, ColBERT-X extends this idea to cross-language retrieval by using the XLM-RoBERTa encoder to support cross-language information retrieval \[[5](http://arxiv.org/abs/2201.08471)\]. These models demonstrate that with appropriate adaptations, transformer-based models can be effective for cross-lingual tasks.

The importance of language-specific adaptation is also emphasized by the work on RoBERTa, which shows that careful optimization and training can lead to significant improvements in performance \[[3](http://arxiv.org/abs/1907.11692)\]. RoBERTa is a robustly optimized BERT pretraining approach that has been shown to achieve state-of-the-art results on various benchmarks \[[3](http://arxiv.org/abs/1907.11692)\]. The success of RoBERTa highlights the need for tailored models that can better capture the linguistic nuances of specific languages.

Moreover, the use of dense retrieval models has gained traction due to their ability to outperform traditional sparse retrieval methods \[[7](http://arxiv.org/abs/2004.04906)\]. Dense retrieval models, such as those based on BERT, learn dense representations of queries and documents, enabling more accurate semantic matching \[[7](http://arxiv.org/abs/2004.04906)\]. This has been further enhanced by models like ColBERT, which leverage late interaction to improve retrieval effectiveness while maintaining computational efficiency \[[1](http://arxiv.org/abs/2004.12832)\].

In addition to these models, the development of multilingual models such as XLM-R has also contributed to cross-lingual retrieval \[[2](http://arxiv.org/abs/1911.02116)\]. XLM-R is trained on a large corpus of multilingual data and has shown significant improvements over multilingual BERT on various benchmarks \[[2](http://arxiv.org/abs/1911.02116)\]. These models are particularly effective for low-resource languages, where the lack of training data poses a significant challenge \[[25](http://arxiv.org/abs/2301.12566)\].

Finally, the importance of data quality and training strategies in cross-lingual retrieval is underscored by the work on optimal transport distillation, which aims to improve performance on low-resource languages by transferring knowledge from high-resource languages \[[25](http://arxiv.org/abs/2301.12566)\]. This approach demonstrates that with the right training strategies, even low-resource languages can benefit from cross-lingual retrieval models.

### References

1. ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT [http://arxiv.org/abs/2004.12832]  
2. Unsupervised Cross-lingual Representation Learning at Scale [http://arxiv.org/abs/1911.02116]  
3. RoBERTa: A Robustly Optimized BERT Pretraining Approach [http://arxiv.org/abs/1907.11692]  
5. Transfer Learning Approaches for Building Cross-Language Dense Retrieval Models [http://arxiv.org/abs/2201.08471]  
7. Dense Passage Retrieval for Open-Domain Question Answering [http://arxiv.org/abs/2004.04906]  
25. Improving Cross-lingual Information Retrieval on Low-Resource Languages via Optimal Transport Distillation [http://arxiv.org/abs/2301.12566]
