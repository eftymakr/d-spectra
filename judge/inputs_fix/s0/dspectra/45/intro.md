## Related Works

Opinion mining has gained significant traction in recent years due to the increasing availability of user-generated content, particularly in app reviews \[[19](https://www.semanticscholar.org/paper/695886bf2b7bf90e98e98f630b26dabcdbe78247)\]. While most studies focus on sentiment polarity classification (positive, negative, neutral), the analysis of fine-grained emotions in app reviews remains underexplored \[[1](http://arxiv.org/abs/2005.00547)\]. This gap is addressed in this work by adapting Plutchik’s emotion taxonomy to the context of app reviews and developing a structured annotation framework \[[1](http://arxiv.org/abs/2005.00547)\]. 

Several studies have explored sentiment analysis in app reviews, highlighting the importance of user feedback for improving software quality and user satisfaction \[[7](http://arxiv.org/abs/1505.04657)\]. For instance, the MARK framework proposes a keyword-based approach for semi-automated review analysis, enabling developers to filter and summarize relevant user opinions \[[7](http://arxiv.org/abs/1505.04657)\]. Similarly, the AR-Miner framework leverages active learning to reduce the human effort required for app review classification while maintaining classification accuracy \[[12](https://www.semanticscholar.org/paper/ff921a209cc9e1c2120669d3d81e627ca5e53572)\]. These approaches demonstrate the potential of automated methods in analyzing app reviews but often lack the granularity needed for emotion detection.

Fine-grained emotion detection has been extensively studied in social media and other domains, with datasets such as GoEmotions providing a large-scale manually annotated corpus for 27 emotion categories \[[1](http://arxiv.org/abs/2005.00547)\]. This dataset has been used to evaluate the performance of BERT-based models, achieving an average F1-score of 0.46 \[[1](http://arxiv.org/abs/2005.00547)\]. Similarly, the Sentiment Treebank introduces a resource for sentiment compositionality, with models achieving up to 85.4% accuracy in single-sentence classification \[[13](https://www.semanticscholar.org/paper/687bac2d3320083eb4530bf18bb8f8f721477600)\]. These datasets and models provide a foundation for emotion detection but are not specifically tailored to app reviews.

The PO-EMO dataset extends the scope of emotion analysis to poetry, focusing on aesthetic emotions elicited in the reader rather than what is expressed in the text \[[5](http://arxiv.org/abs/2003.07723)\]. This approach highlights the importance of considering the emotional response of the audience, which is relevant to the analysis of app reviews. However, such datasets are not commonly used in app review analysis due to their domain-specific nature.

Recent studies have also explored the use of large language models (LLMs) for sentiment analysis, demonstrating their potential in few-shot learning scenarios \[[20](http://arxiv.org/abs/2305.15005)\]. However, these models often struggle with complex tasks requiring deeper understanding or structured sentiment information. This limitation underscores the need for hybrid approaches combining human annotation with automated methods \[[20](http://arxiv.org/abs/2305.15005)\].

In summary, while there is a rich body of work on sentiment analysis and emotion detection, the specific challenges of fine-grained emotion classification in app reviews remain underexplored. This work contributes to the field by providing a structured annotation framework, an annotated dataset, and insights into the feasibility of automating emotion annotation using LLMs \[[1](http://arxiv.org/abs/2005.00547)\].

### References

1. GoEmotions: A Dataset of Fine-Grained Emotions [http://arxiv.org/abs/2005.00547]  
2. Training language models to follow instructions with human feedback [http://arxiv.org/abs/2203.02155]  
3. On the Emotion of Users in App Reviews [http://arxiv.org/abs/1703.02256]  
4. Sentiment Analysis and Opinion Mining [https://www.semanticscholar.org/paper/33c95f4d13958e65e676a9cd64bd4d8df0fdb44d]  
5. PO-EMO: Conceptualization, Annotation, and Modeling of Aesthetic Emotions in German and English Poetry [http://arxiv.org/abs/2003.07723]  
6. Mining User Opinions in Mobile App Reviews: A Keyword-Based Approach (T) [http://arxiv.org/abs/1505.04657]  
7. App Review Analysis Via Active Learning: Reducing Supervision Effort without Compromising Classification Accuracy [https://www.semanticscholar.org/paper/3d1db23a8aa2eeb0cf3be91446d0296abecb8dc3]  
8. A Feature-Oriented Sentiment Rating for Mobile App Reviews [https://www.semanticscholar.org/paper/6fe8d8d604e8e19dc6ed738c8e58b7351aeeed515c]  
9. CROWDSOURCING A WORD–EMOTION ASSOCIATION LEXICON [http://arxiv.org/abs/1308.6297]  
10. AR-miner: mining informative reviews for developers from mobile app marketplace [https://www.semanticscholar.org/paper/ff921a209cc9e1c2120669d3d81e627ca5e53572]  
11. Recursive Deep Models for Semantic Compositionality Over a Sentiment Treebank [https://www.semanticscholar.org/paper/687bac2d3320083eb4530bf18bb8f8f721477600]  
12. SENTIWORDNET: A Publicly Available Lexical Resource for Opinion Mining [https://www.semanticscholar.org/paper/96761dc3d8adaeff44eb9c07501eb3109802ee4b]  
13. How Do Users Like This Feature? A Fine Grained Sentiment Analysis of App Reviews [https://www.semanticscholar.org/paper/030ea3f854d688659500a949eac095cdba087682]  
14. Thumbs up? Sentiment Classification using Machine Learning Techniques [https://www.semanticscholar.org/paper/12d0353ce8b41b7e5409e5a4a611110aee33c7bc]  
15. On the automatic classification of app reviews [https://www.semanticscholar.org/paper/c32ed8d14de92c4a8d8cfbeac7d04e99431887cf]  
16. EmoNet: Fine-Grained Emotion Detection with Gated Recurrent Neural Networks [https://www.semanticscholar.org/paper/6a6f1b8ef3eefaf8027a76134859b44886a5f795]  
17. Analysing app reviews for software engineering: a systematic literature review [https://www.semanticscholar.org/paper/695886bf2b7bf90e98e98f630b26dabcdbe78247]  
18. Sentiment Analysis in the Era of Large Language Models: A Reality Check [http://arxiv.org/abs/2305.15005]  
19. Thumbs Up or Thumbs Down? Semantic Orientation Applied to Unsupervised Classification of Reviews [https://www.semanticscholar.org/paper/9e7c7853a16a378cc24a082153b282257a9675b7]  
20. The Impact of Annotation Guidelines and Annotated Data on Extracting App Features from App Reviews [http://arxiv.org/abs/1810.05187]  
21. Listening to Users' Voice: Automatic Summarization of Helpful App Reviews [http://arxiv.org/abs/2210.06235]
