## Related Works

Personalized outfit generation has gained significant attention in recent years due to its potential to enhance user experience in fashion recommendation systems. Prior work has primarily focused on two aspects: outfit compatibility and personalization. Early approaches relied on rule-based systems or simple similarity metrics to recommend compatible fashion items \[[1](http://arxiv.org/abs/1905.01866)\]. However, these methods lacked the ability to capture complex style relationships and user preferences. 

Recent advances in deep learning have enabled more sophisticated models for outfit generation and recommendation. For instance, POG \[[1](http://arxiv.org/abs/1905.01866)\] introduces a Transformer-based model that connects user preferences with outfit generation, improving both compatibility and personalization. Similarly, the work by \[[2](http://arxiv.org/abs/1608.03016)\] proposes a multimodal deep learning system to score outfit candidates based on appearance and metadata, leveraging popularity to supervise the scoring process. These models demonstrate the importance of incorporating both visual and semantic information to enhance recommendation accuracy.

The concept of style extraction and its role in outfit generation has also been explored. \[[3](http://arxiv.org/abs/1807.03133)\] introduces a model that incorporates an unsupervised style extraction module to learn global information from outfits, enabling more flexible and interpretable outfit generation. This approach is particularly useful for generating outfits that align with user preferences while maintaining visual coherence. 

Compatibility between fashion items remains a critical challenge, especially when considering different item types and their stylistic relationships. \[[4](http://arxiv.org/abs/1803.09196)\] presents a method to learn type-aware embeddings that respect item type and jointly model similarity and compatibility. This work improves upon existing methods by achieving better performance in outfit compatibility prediction and fill-in-the-blank tasks. 

In addition to compatibility, the ability to generate visually appealing and personalized outfits has been a key focus. \[[5](http://arxiv.org/abs/1711.02231)\] proposes a generative image model that learns fashion-aware image representations directly, enabling the system to generate new clothing items that align with a user's personal taste. This approach not only improves recommendation accuracy but also allows for creative design and style suggestion. 

Another important aspect is the automatic creation of capsule wardrobes, which involves selecting a minimal set of items that can be mixed and matched to form various outfits. \[[6](http://arxiv.org/abs/1712.02662)\] addresses this by developing submodular objective functions that capture visual compatibility, versatility, and user preferences. This work demonstrates the potential of automated capsule creation to mimic skilled fashionistas while being more scalable. 

Furthermore, the use of neural networks for compatibility modeling has been extensively explored. \[[7](http://arxiv.org/abs/1904.00741)\] introduces a bidirectional LSTM (Bi-LSTM) model that learns compatibility relationships between fashion items by sequentially predicting the next item in an outfit. This approach enables the model to not only recommend items but also predict the compatibility of a given outfit. 

In summary, the field of personalized outfit generation has seen significant advancements, with a growing emphasis on deep learning models that incorporate both visual and semantic information. These models aim to improve compatibility, personalization, and creative design while being scalable and interpretable. Future work may focus on integrating more diverse data sources and improving the interpretability of generated recommendations.

References:
1. POG: Personalized Outfit Generation for Fashion Recommendation at Alibaba iFashion [http://arxiv.org/abs/1905.01866]
2. Mining Fashion Outfit Composition Using an End-to-End Deep Learning Approach on Set Data [http://arxiv.org/abs/1608.03016]
3. Outfit Generation and Style Extraction via Bidirectional LSTM and Autoencoder [http://arxiv.org/abs/1807.03133]
4. Learning Type-Aware Embeddings for Fashion Compatibility [http://arxiv.org/abs/1803.09196]
5. Visually-Aware Fashion Recommendation and Design with Generative Image Models [http://arxiv.org/abs/1711.02231]
6. Creating Capsule Wardrobes from Fashion Images [http://arxiv.org/abs/1712.02662]
7. Learning Fashion Compatibility with Bidirectional LSTMs [http://arxiv.org/abs/1707.05691]
