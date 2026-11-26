## Related Works

Neural retrieval methods using transformer-based pre-trained language models have significantly advanced multilingual and cross-lingual retrieval \[[14](http://arxiv.org/abs/2201.08471)\]. However, their effectiveness for low-resource, morphologically rich languages such as Amharic remains underexplored due to data scarcity and suboptimal tokenization \[[2](http://arxiv.org/abs/2207.00785)\]. This gap is addressed by introducing Amharic-specific dense retrieval models based on pre-trained Amharic BERT and RoBERTa backbones \[[25](http://arxiv.org/abs/2001.03324)\]. These models demonstrate notable improvements over existing multilingual baselines, such as Arctic Embed 2.0 \[[25](http://arxiv.org/abs/2001.03324)\].

The use of pre-trained language models for information retrieval has been extensively studied. For instance, ColBERT \[[8](http://arxiv.org/abs/2004.12832)\] introduces a late interaction architecture that independently encodes the query and document using BERT and then employs a cheap yet powerful interaction step to model their fine-grained similarity. This approach significantly improves retrieval effectiveness while reducing computational costs \[[8](http://arxiv.org/abs/2004.12832)\]. Similarly, ColBERT-X \[[14](http://arxiv.org/abs/2201.08471)\] extends this idea to support cross-language information retrieval by using the XLM-RoBERTa encoder, enabling zero-shot training on the English MS MARCO collection. These models show substantial improvements over traditional lexical CLIR baselines \[[14](http://arxiv.org/abs/2201.08471)\].

Fine-tuning pre-trained models for low-resource languages has also been explored. For example, Whispering in Amharic \[[3](http://arxiv.org/abs/2503.18485)\] explores fine-tuning OpenAI's Whisper automatic speech recognition (ASR) model for Amharic, a low-resource language, to improve transcription accuracy. The study highlights the importance of fine-tuning strategies and dataset composition for improving ASR in low-resource languages \[[3](http://arxiv.org/abs/2503.18485)\]. Similarly, the RoBERTa model \[[6](http://arxiv.org/abs/1907.11692)\] has been used for named entity recognition in Amharic, achieving an F1-score of 93% \[[2](http://arxiv.org/abs/2207.00785)\]. This demonstrates the potential of transfer learning for low-resource languages.

Dense retrieval models have also been applied to other tasks, such as passage re-ranking with BERT \[[19](http://arxiv.org/abs/1901.04085)\], which outperforms previous state-of-the-art results by 27% in MRR@10. Additionally, ColBERTv2 \[[16](http://arxiv.org/abs/2112.01488)\] introduces a lightweight late interaction mechanism that reduces the space footprint of late interaction models by 6–10x while maintaining high retrieval effectiveness.

The challenges of low-resource language retrieval are also addressed in other works. For example, the study on Urdu MS MARCO \[[11](http://arxiv.org/abs/2412.12997)\] introduces the first large-scale Urdu IR dataset and establishes baseline results through zero-shot learning. This work highlights the importance of creating language-specific datasets and adapting models for low-resource languages \[[11](http://arxiv.org/abs/2412.12997)\]. Similarly, the study on Amharic LLaMA and LLaVA \[[4](http://arxiv.org/abs/2403.06354)\] explores training LLaMA-2 to speak Amharic, demonstrating the potential of open-source models for low-resource languages.

In summary, the field of low-resource language retrieval has seen significant advancements through the use of pre-trained language models, fine-tuning strategies, and dense retrieval approaches. These works collectively highlight the importance of language-specific adaptation and the need for more data and better tokenization strategies to improve retrieval effectiveness for morphologically rich languages like Amharic.

References  
\[[1](http://arxiv.org/abs/2503.18570)\] http://arxiv.org/abs/2503.18570  
\[[2](http://arxiv.org/abs/2207.00785)\] http://arxiv.org/abs/2207.00785  
\[[3](http://arxiv.org/abs/2503.18485)\] http://arxiv.org/abs/2503.18485  
\[[4](http://arxiv.org/abs/2403.06354)\] http://arxiv.org/abs/2403.06354  
\[[5](http://arxiv.org/abs/2402.15059)\] http://arxiv.org/abs/2402.15059  
\[[6](http://arxiv.org/abs/1907.11692)\] http://arxiv.org/abs/1907.11692  
\[[7](http://arxiv.org/abs/2007.01852)\] http://arxiv.org/abs/2007.01852  
\[[8](http://arxiv.org/abs/2004.12832)\] http://arxiv.org/abs/2004.12832  
\[[9](http://arxiv.org/abs/2212.10448)\] http://arxiv.org/abs/2212.10448  
\[[10](https://www.semanticscholar.org/paper/8282c6b141c335fc144818f20d86e68800691a01)\] http://arxiv.org/abs/2006.15498  
\[[11](http://arxiv.org/abs/2412.12997)\] http://arxiv.org/abs/2412.12997  
\[[12](http://arxiv.org/abs/2408.11942)\] http://arxiv.org/abs/2408.11942  
\[[13](http://arxiv.org/abs/2006.15498)\] http://arxiv.org/abs/2112.09118  
\[[14](http://arxiv.org/abs/2201.08471)\] http://arxiv.org/abs/2201.08471  
\[[15](http://arxiv.org/abs/2307.10814)\] http://arxiv.org/abs/2307.10814  
\[[16](http://arxiv.org/abs/2112.01488)\] http://arxiv.org/abs/2112.01488  
\[[17](http://arxiv.org/abs/2112.09118)\] http://arxiv.org/abs/2112.09118  
\[[18](http://arxiv.org/abs/1905.09217)\] http://arxiv.org/abs/1905.09217  
\[[19](http://arxiv.org/abs/1901.04085)\] http://arxiv.org/abs/1901.04085  
\[[20](http://arxiv.org/abs/2501.05260)\] http://arxiv.org/abs/2501.05260  
\[[21](http://arxiv.org/abs/2104.08663)\] http://arxiv.org/abs/2104.08663  
\[[22](http://arxiv.org/abs/2108.06279)\] http://arxiv.org/abs/2108.06279  
\[[23](http://arxiv.org/abs/2211.14876)\] http://arxiv.org/abs/2211.14876  
\[[24](http://arxiv.org/abs/2010.10469)\] http://arxiv.org/abs/2010.10469  
\[[25](http://arxiv.org/abs/2001.03324)\] http://arxiv.org/abs/2001.03324  
\[[26](http://arxiv.org/abs/2204.05814)\] http://arxiv.org/abs/2204.05814  
\[[27](http://arxiv.org/abs/2203.11163)\] http://arxiv.org/abs/2203.11163  
\[[28](http://arxiv.org/abs/2307.16779)\] http://arxiv.org/abs/2307.16779  
\[[29](http://arxiv.org/abs/2112.04426)\] http://arxiv.org/abs/2112.04426  
\[[30](http://arxiv.org/abs/2303.03290)\] http://arxiv.org/abs/2303.03290
