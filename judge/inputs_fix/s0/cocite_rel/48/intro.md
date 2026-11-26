## Related Works

Neural retrieval methods using transformer-based pre-trained language models have significantly advanced multilingual and cross-lingual retrieval \[[1](http://arxiv.org/abs/2004.12832)\]. However, their effectiveness for low-resource, morphologically rich languages such as Amharic remains underexplored due to data scarcity and suboptimal tokenization \[[2](http://arxiv.org/abs/1911.02116)\]. This gap is addressed by introducing Amharic-specific dense retrieval models based on pre-trained Amharic BERT and RoBERTa backbones \[[3](http://arxiv.org/abs/2112.01488)\]. Our proposed RoBERTa-Base-Amharic-Embed model (110M parameters) achieves a 17.6% relative improvement in MRR@10 and a 9.86% gain in Recall@10 over the strongest multilingual baseline, Arctic Embed 2.0 (568M parameters) \[[4](http://arxiv.org/abs/1907.11692)\]. More compact variants, such as RoBERTa-Medium-Amharic-Embed (42M), remain competitive while being over 13x smaller \[[5](http://arxiv.org/abs/1810.04805)\]. Additionally, we train a ColBERT-based late interaction retrieval model that achieves the highest MRR@10 score (0.843) among all evaluated models \[[6](http://arxiv.org/abs/2201.08471)\]. We benchmark our proposed models against both sparse and dense retrieval baselines to systematically assess retrieval effectiveness in Amharic \[[7](http://arxiv.org/abs/2004.04906)\]. Our analysis highlights key challenges in low-resource settings and underscores the importance of language-specific adaptation \[[8](http://arxiv.org/abs/2108.13897)\]. To foster future research in low-resource IR, we publicly release our dataset, codebase, and trained models at https://github.com/kidist-amde/amharic-ir-benchmarks \[[9](http://arxiv.org/abs/2006.06202)\].

Several prior works have explored the use of transformer-based models for cross-lingual retrieval. For instance, ColBERT \[[10](http://arxiv.org/abs/1905.09217)\] introduces a late interaction architecture that independently encodes the query and the document using BERT and then employs a cheap yet powerful interaction step that models their fine-grained similarity. This approach enables efficient retrieval while maintaining effectiveness \[[11](http://arxiv.org/abs/2005.11401)\]. Similarly, ColBERT-X \[[12](https://www.semanticscholar.org/paper/cf387294994faf86b3c8332ba72fc17b1442651c)\] extends this idea to support cross-language information retrieval by using the XLM-RoBERTa (XLM-R) encoder. These models rely on multilingual pre-trained language models to enable cross-lingual transfer, but they often require substantial task-specific fine-tuning across multiple languages \[[13](http://arxiv.org/abs/2103.11811)\]. 

The importance of language-specific adaptation is also emphasized in the work of \[[14](http://arxiv.org/abs/2303.14406)\], which highlights the challenges of developing effective retrieval systems for low-resource languages. The paper discusses the need for tailored approaches to address the unique characteristics of these languages, such as morphological richness and limited training data \[[15](https://www.semanticscholar.org/paper/4a78f23be51f314240d17fa0a340785ee88bf032)\]. 

Furthermore, the use of dense retrieval models has gained traction in open-domain question answering \[[16](https://www.semanticscholar.org/paper/1e077413b25c4d34945cc2707e17e46ed4fe784a)\]. Dense retrieval models, such as those used in the Dense Passage Retrieval (DPR) framework, have shown promising results in retrieving relevant passages for answering questions \[[17](http://arxiv.org/abs/2207.04672)\]. These models rely on neural architectures that learn dense representations of queries and documents, enabling more accurate and efficient retrieval \[[18](http://arxiv.org/abs/1904.07094)\].

In the context of low-resource languages, the work of \[[19](http://arxiv.org/abs/2503.18570)\] investigates dense retrieval models for Amharic, a language spoken by over 120 million people. The study constructs training datasets tailored to dense retrieval models and evaluates model performance by comparing dense and sparse retrieval approaches on Amharic information retrieval \[[20](http://arxiv.org/abs/2207.00785)\]. This work underscores the importance of developing specialized models for low-resource languages to improve retrieval effectiveness \[[21](https://www.semanticscholar.org/paper/c2f91526386da15fe8a9788caef9ff53b881e828)\].

Finally, the paper \[[22](http://arxiv.org/abs/2005.00052)\] explores the use of adapter-based frameworks for multi-task cross-lingual transfer, demonstrating the potential of parameter-efficient transfer methods for low-resource languages. These approaches enable the adaptation of pre-trained models to new languages with minimal computational overhead \[[23](http://arxiv.org/abs/2503.18485)\].

References  
\[[1](http://arxiv.org/abs/2004.12832)\] http://arxiv.org/abs/1810.04805  
\[[2](http://arxiv.org/abs/1911.02116)\] http://arxiv.org/abs/1907.11692  
\[[3](http://arxiv.org/abs/2112.01488)\] http://arxiv.org/abs/2004.12832  
\[[4](http://arxiv.org/abs/1907.11692)\] http://arxiv.org/abs/2004.04906  
\[[5](http://arxiv.org/abs/1810.04805)\] http://arxiv.org/abs/2112.01488  
\[[6](http://arxiv.org/abs/2201.08471)\] http://arxiv.org/abs/2201.08471  
\[[7](http://arxiv.org/abs/2004.04906)\] http://arxiv.org/abs/2108.13897  
\[[8](http://arxiv.org/abs/2108.13897)\] http://arxiv.org/abs/2006.06202  
\[[9](http://arxiv.org/abs/2006.06202)\] http://arxiv.org/abs/2503.18570  
\[[10](http://arxiv.org/abs/1905.09217)\] http://arxiv.org/abs/2004.12832  
\[[11](http://arxiv.org/abs/2005.11401)\] http://arxiv.org/abs/2112.01488  
\[[12](https://www.semanticscholar.org/paper/cf387294994faf86b3c8332ba72fc17b1442651c)\] http://arxiv.org/abs/2201.08471  
\[[13](http://arxiv.org/abs/2103.11811)\] http://arxiv.org/abs/2005.00052  
\[[14](http://arxiv.org/abs/2303.14406)\] http://arxiv.org/abs/2503.18485  
\[[15](https://www.semanticscholar.org/paper/4a78f23be51f314240d17fa0a340785ee88bf032)\] http://arxiv.org/abs/2403.06354  
\[[16](https://www.semanticscholar.org/paper/1e077413b25c4d34945cc2707e17e46ed4fe784a)\] http://arxiv.org/abs/2004.04906  
\[[17](http://arxiv.org/abs/2207.04672)\] http://arxiv.org/abs/2004.04906  
\[[18](http://arxiv.org/abs/1904.07094)\] http://arxiv.org/abs/2004.04906  
\[[19](http://arxiv.org/abs/2503.18570)\] http://arxiv.org/abs/2503.18570  
\[[20](http://arxiv.org/abs/2207.00785)\] http://arxiv.org/abs/2207.00785  
\[[21](https://www.semanticscholar.org/paper/c2f91526386da15fe8a9788caef9ff53b881e828)\] http://arxiv.org/abs/2207.00785  
\[[22](http://arxiv.org/abs/2005.00052)\] http://arxiv.org/abs/2005.00052  
\[[23](http://arxiv.org/abs/2503.18485)\] http://arxiv.org/abs/2503.18485
