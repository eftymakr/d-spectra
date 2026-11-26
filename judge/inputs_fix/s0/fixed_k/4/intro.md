## Related Works

The field of in-context learning (ICL) has seen significant advancements, particularly in the context of large language models (LLMs) and their ability to leverage annotated corpora for task execution \[[1](http://arxiv.org/abs/2110.10456)\]. However, the reliance on high-quality demonstrations has exposed critical limitations when dealing with noisy annotations. Existing approaches often assume that noisy samples yield higher perplexity than clean ones, using local perplexity rankings to detect anomalies \[[2](http://arxiv.org/abs/2012.11854)\]. This assumption, however, becomes invalid under high noise ratios, where many demonstrations are flawed, leading to unreliable detection \[[3](http://arxiv.org/abs/2406.16966)\].

Several studies have addressed the issue of noisy annotations in deep learning models. For instance, \[[4](http://arxiv.org/abs/2207.13316)\] explores the challenges of training models with noisy labels, emphasizing the need for robust methods to correct such errors. Similarly, \[[5](http://arxiv.org/abs/2312.12275)\] proposes a framework for mitigating noisy supervision by generating synthetic samples with soft labels, which helps in improving generalization performance. These approaches, while effective in some settings, often fail to account for the complex interplay between annotation quality and model behavior \[[6](http://arxiv.org/abs/2212.01189)\].

In the context of object detection, \[[7](http://arxiv.org/abs/1407.5155)\] highlights the importance of correcting noisy annotations, particularly in large-scale datasets obtained through cloud sourcing. Their work demonstrates that entangled noises in class labels and bounding boxes can significantly degrade model performance, necessitating methods to decouple and correct these errors \[[8](http://arxiv.org/abs/2401.14360)\]. This aligns with the broader challenge of handling noisy annotations in various NLP and vision tasks \[[9](http://arxiv.org/abs/1809.04019)\].

The problem of label noise has also been studied in the context of reinforcement learning, where \[[10](http://arxiv.org/abs/2410.09365)\] introduces a novel data acquisition approach to enable in-context learning from noisy data. This work shows that synthetic noise injection can be used to generate learning histories, reducing the reliance on optimal policy generation \[[11](http://arxiv.org/abs/2305.10736)\]. These findings are relevant to the broader discussion on handling noisy annotations in ICL settings \[[12](http://arxiv.org/abs/2106.07704)\].

In addition, \[[13](http://arxiv.org/abs/2412.04727)\] proposes a method for robust image denoising by translating unknown real-world noise into Gaussian noise, enabling the use of pre-trained denoising networks. This approach is particularly relevant to the generalization challenges faced by models trained on noisy data \[[14](http://arxiv.org/abs/1911.05241)\].

The importance of annotation quality in downstream tasks has also been highlighted in the context of named entity recognition, where \[[15](http://arxiv.org/abs/2408.15204)\] demonstrates the brittleness of standard models to capitalization errors. Their approach, based on data augmentation, allows models to learn how to handle such noise without sacrificing performance on well-formed text \[[16](http://arxiv.org/abs/2004.10283)\].

Finally, \[[17](http://arxiv.org/abs/2103.06413)\] explores the use of LLM annotations in computational social science, emphasizing the need for confidence-driven inference to ensure validity while reducing the reliance on human annotations. This work provides insights into the broader implications of using noisy annotations in downstream tasks .

---

**References**  
\[[1](http://arxiv.org/abs/2110.10456)\] http://arxiv.org/abs/2110.10456  
\[[2](http://arxiv.org/abs/2012.11854)\] http://arxiv.org/abs/2012.11854  
\[[3](http://arxiv.org/abs/2406.16966)\] http://arxiv.org/abs/2406.16966  
\[[4](http://arxiv.org/abs/2207.13316)\] http://arxiv.org/abs/2207.13316  
\[[5](http://arxiv.org/abs/2312.12275)\] http://arxiv.org/abs/2212.01189  
\[[6](http://arxiv.org/abs/2212.01189)\] http://arxiv.org/abs/2401.14360  
\[[7](http://arxiv.org/abs/1407.5155)\] http://arxiv.org/abs/1407.5155  
\[[8](http://arxiv.org/abs/2401.14360)\] http://arxiv.org/abs/1809.04019  
\[[9](http://arxiv.org/abs/1809.04019)\] http://arxiv.org/abs/2410.09365  
\[[10](http://arxiv.org/abs/2410.09365)\] http://arxiv.org/abs/2312.12275  
\[[11](http://arxiv.org/abs/2305.10736)\] http://arxiv.org/abs/2106.07704  
\[[12](http://arxiv.org/abs/2106.07704)\] http://arxiv.org/abs/2412.04727  
\[[13](http://arxiv.org/abs/2412.04727)\] http://arxiv.org/abs/1911.05241  
\[[14](http://arxiv.org/abs/1911.05241)\] http://arxiv.org/abs/2408.15204  
\[[15](http://arxiv.org/abs/2408.15204)\] http://arxiv.org/abs/2004.10283  
\[[16](http://arxiv.org/abs/2004.10283)\] http://arxiv.org/abs/2103.06413  
\[[17](http://arxiv.org/abs/2103.06413)\] http://arxiv.org/abs/2406.16966  
 http://arxiv.org/abs/2408.15204
