## Related Works

Fine-grained emotion classification in app reviews has received increasing attention in recent years, driven by the need to better understand user sentiment and emotional expression in digital platforms. While sentiment analysis has been extensively studied, focusing primarily on polarity classification (positive, negative, neutral) \[[1](https://www.semanticscholar.org/paper/7d0531aaaa4dbf4033da964289843e7812262702)\], the detection of discrete emotions remains a challenging and underexplored area \[[2](https://www.semanticscholar.org/paper/6a6f1b8ef3eefaf8027a76134859b44886a5f795)\]. This is particularly true in the context of app reviews, where emotional nuances are often expressed in complex and varied ways \[[3](https://www.semanticscholar.org/paper/ff921a209cc9e1c2120669d3d81e627ca5e53572)\].

Several studies have attempted to address the lack of large-scale annotated datasets for emotion detection in natural language. For example, the work of \[[4](https://www.semanticscholar.org/paper/030ea3f854d688659500a949eac095cdba087682)\] highlights the scarcity of datasets for fine-grained emotion detection, especially in the social media domain, and proposes extending existing datasets with emotion annotations. Similarly, \[[5](http://arxiv.org/abs/1505.04657)\] introduces GoEmotions, a large dataset of 58k Reddit comments labeled for 27 emotion categories, demonstrating its utility for transfer learning and benchmarking \[[6](https://www.semanticscholar.org/paper/872352b0a53ab6cbb4420f81df64d215d86c7d9b)\]. However, these datasets are not specifically tailored to app reviews, which often contain domain-specific language and emotional expressions unique to user feedback \[[7](https://www.semanticscholar.org/paper/c32ed8d14de92c4a8d8cfbeac7d04e99431887cf)\].

The challenge of annotating emotions in text has also been explored in the context of app reviews. \[[8](http://arxiv.org/abs/2005.00547)\] discusses the importance of structured annotation frameworks and human-in-the-loop processes for improving the reliability of emotion annotations. This aligns with the findings of \[[9](http://arxiv.org/abs/2205.01996)\], which emphasizes the need for clear annotation guidelines and iterative refinement to capture the complexity of emotional expressions in user-generated content. \[[10](https://www.semanticscholar.org/paper/723f744455914bf1ead6ad267976a1500b7dee4a)\] further highlights the limitations of existing emotion lexicons and the need for more nuanced annotation approaches, especially when dealing with the subtleties of user sentiment in app reviews.

Recent advances in deep learning have enabled more accurate emotion detection, particularly with the use of pre-trained models like BERT \[[11](https://www.semanticscholar.org/paper/695886bf2b7bf90e98e98f630b26dabcdbe78247)\]. \[[12](http://arxiv.org/abs/2305.15005)\] demonstrates that fine-tuning a pre-trained BERT model achieves state-of-the-art results on emotion classification tasks, with an average micro-F1 score of 60.4% on the DENS dataset. This suggests that large language models can be effective for emotion detection, although they still struggle with the fine-grained classification required for app reviews \[[13](https://www.semanticscholar.org/paper/66c8ab0b3b7698cf5333c3f7350a6eaa5302294b)\].

In addition to emotion detection, several studies have focused on the broader task of sentiment analysis in app reviews. \[[14](http://arxiv.org/abs/1910.11769)\] presents a framework for automatically classifying app reviews into positive, negative, or neutral sentiments, using semantic orientation and unsupervised learning techniques. \[[15](https://www.semanticscholar.org/paper/3fb416be9e59b35c7cc91cd11b5b3f3f5491f13a)\] further explores the use of topic modeling and sentiment analysis to extract key features from app reviews, providing developers with actionable insights \[[16](https://www.semanticscholar.org/paper/9e7c7853a16a378cc24a082153b282257a9675b7)\].

Overall, while significant progress has been made in sentiment and emotion analysis, the specific challenges of fine-grained emotion classification in app reviews remain largely unaddressed. This paper contributes to this area by developing a structured annotation framework, an annotated dataset, and insights for improving automated emotion detection pipelines \[[17](http://arxiv.org/abs/1308.6297)\].

### References

1. \[[4](https://www.semanticscholar.org/paper/030ea3f854d688659500a949eac095cdba087682)\]  
2. \[[5](http://arxiv.org/abs/1505.04657)\]  
3. \[[6](https://www.semanticscholar.org/paper/872352b0a53ab6cbb4420f81df64d215d86c7d9b)\]  
4. \[[7](https://www.semanticscholar.org/paper/c32ed8d14de92c4a8d8cfbeac7d04e99431887cf)\]  
5. \[[8](http://arxiv.org/abs/2005.00547)\]  
6. \[[9](http://arxiv.org/abs/2205.01996)\]  
7. \[[10](https://www.semanticscholar.org/paper/723f744455914bf1ead6ad267976a1500b7dee4a)\]  
8. \[[11](https://www.semanticscholar.org/paper/695886bf2b7bf90e98e98f630b26dabcdbe78247)\]  
9. \[[12](http://arxiv.org/abs/2305.15005)\]  
10. \[[13](https://www.semanticscholar.org/paper/66c8ab0b3b7698cf5333c3f7350a6eaa5302294b)\]  
11. \[[14](http://arxiv.org/abs/1910.11769)\]  
12. \[[15](https://www.semanticscholar.org/paper/3fb416be9e59b35c7cc91cd11b5b3f3f5491f13a)\]  
13. \[[16](https://www.semanticscholar.org/paper/9e7c7853a16a378cc24a082153b282257a9675b7)\]  
14. \[[17](http://arxiv.org/abs/1308.6297)\]
