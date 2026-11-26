## Related Works

Neural retrieval methods using transformer-based pre-trained language models have significantly advanced multilingual and cross-lingual retrieval \[[1](http://arxiv.org/abs/2503.18570)\]. However, their effectiveness for low-resource, morphologically rich languages such as Amharic remains underexplored due to data scarcity and suboptimal tokenization \[[2](http://arxiv.org/abs/2207.00785)\]. This challenge is echoed in the broader field of low-resource language processing, where the lack of training data and the complexity of morphological structures pose significant hurdles \[[3](http://arxiv.org/abs/2503.18485)\]. 

Several studies have explored the use of transformer-based models for Amharic. For instance, \[[4](http://arxiv.org/abs/2403.06354)\] investigates the fine-tuning of OpenAI's Whisper model for Amharic, highlighting the importance of dataset composition and normalization of homophones to improve Word Error Rate (WER) and BLEU scores. Similarly, \[[5](http://arxiv.org/abs/2212.10448)\] discusses the challenges of named entity recognition in Amharic, emphasizing the need for large annotated datasets and the use of transfer learning techniques like RoBERTa to achieve state-of-the-art results. 

In the context of dense retrieval, \[[6](http://arxiv.org/abs/2412.12997)\] presents a study on the effectiveness of dense retrieval models for Amharic, comparing them with sparse retrieval approaches. The work highlights the importance of tailored training datasets and the challenges of adapting models to morphologically rich languages. Furthermore, \[[7](http://arxiv.org/abs/2408.11942)\] explores the use of multilingual BERT for cross-lingual retrieval, demonstrating the potential of multilingual models in improving retrieval performance across languages. 

The limitations of cross-lingual dense passage retrieval for extremely low-resource languages such as Amharic and Khmer are also discussed in \[[8](http://arxiv.org/abs/2201.08471)\]. The study finds that while models like mDPR show promise, the results remain modest, indicating the need for better data and evaluation strategies. This aligns with the findings of \[[9](http://arxiv.org/abs/2307.10814)\], which highlights the challenges of cross-lingual dense retrieval and the importance of language-specific adaptations. 

To address these challenges, \[[10](http://arxiv.org/abs/2501.05260)\] introduces the use of parameter-efficient transfer learning techniques, such as adapters, for cross-language dense retrieval. The study shows that adapter-enhanced models outperform fine-tuned models in cross-lingual settings. This is further supported by \[[11](http://arxiv.org/abs/2108.06279)\], which compares single and multiple representation approaches in dense retrieval, showing that multiple representations are more effective for certain retrieval tasks. 

In addition, \[[12](http://arxiv.org/abs/2211.14876)\] provides a comprehensive survey of dense retrieval methods based on pretrained language models, emphasizing the role of these models in improving semantic representation and relevance modeling. The work also highlights the importance of training strategies and data augmentation for low-resource languages. 

The use of transfer learning and multilingual models for low-resource languages is also explored in \[[13](http://arxiv.org/abs/2010.10469)\], where the authors propose a method to fine-tune mBERT-based models for Amharic QA tasks using translations from other languages. The results show that cross-lingual fine-tuning can improve performance, although there are limitations when translating across language families. 

In summary, the body of work on Amharic and other low-resource languages highlights the challenges of data scarcity, morphological complexity, and the need for language-specific adaptations. The proposed methods in this paper build on these findings, introducing Amharic-specific dense retrieval models based on pre-trained BERT and RoBERTa backbones, achieving significant improvements over existing multilingual baselines. 

References:  
\[[1](http://arxiv.org/abs/2503.18570)\] http://arxiv.org/abs/2201.08471  
\[[2](http://arxiv.org/abs/2207.00785)\] http://arxiv.org/abs/2503.18570  
\[[3](http://arxiv.org/abs/2503.18485)\] http://arxiv.org/abs/2001.03324  
\[[4](http://arxiv.org/abs/2403.06354)\] http://arxiv.org/abs/2503.18485  
\[[5](http://arxiv.org/abs/2212.10448)\] http://arxiv.org/abs/2207.00785  
\[[6](http://arxiv.org/abs/2412.12997)\] http://arxiv.org/abs/2408.11942  
\[[7](http://arxiv.org/abs/2408.11942)\] http://arxiv.org/abs/2212.10448  
\[[8](http://arxiv.org/abs/2201.08471)\] http://arxiv.org/abs/2408.11942  
\[[9](http://arxiv.org/abs/2307.10814)\] http://arxiv.org/abs/2201.08471  
\[[10](http://arxiv.org/abs/2501.05260)\] http://arxiv.org/abs/2212.10448  
\[[11](http://arxiv.org/abs/2108.06279)\] http://arxiv.org/abs/2108.06279  
\[[12](http://arxiv.org/abs/2211.14876)\] http://arxiv.org/abs/2211.14876  
\[[13](http://arxiv.org/abs/2010.10469)\] http://arxiv.org/abs/2204.05814
