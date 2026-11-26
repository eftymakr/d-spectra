## Related Works

Personalized outfit generation has been a focal point in recent research, driven by the increasing demand for fashion recommendation systems that can provide both compatibility and personalization \[[1](http://arxiv.org/abs/1905.01866)\]. Early approaches focused on item-level compatibility, often using rule-based systems or simple similarity metrics \[[12](http://arxiv.org/abs/1805.00313)\]. However, these methods lacked the ability to model complex interactions between items and user preferences \[[14](http://arxiv.org/abs/1810.02443)\]. 

Recent works have explored deep learning models to address these challenges. For instance, \[[1](http://arxiv.org/abs/1905.01866)\] proposed a Personalized Outfit Generation (POG) model that connects user preferences with a Transformer architecture, achieving strong performance in both compatibility and personalization metrics. Similarly, \[[15](https://www.semanticscholar.org/paper/762ec45448e915142f355848265d10dd55ab470f)\] introduced OutfitNet, which uses attention-based multiple instance learning to model the compatibility between items and user preferences, showing improved results in fill-in-the-blank and personalized outfit recommendation tasks. 

The importance of style in outfit generation has also been emphasized. \[[2](http://arxiv.org/abs/1807.03133)\] incorporated an unsupervised style extraction module to learn global style information, enabling more flexible and interpretable outfit generation. \[[16](http://arxiv.org/abs/1509.07473)\] further extended this idea by learning a visual compatibility metric from co-occurrence data, which proved effective in generating compatible outfits across categories. 

Compatibility modeling has been another key area of research. \[[13](http://arxiv.org/abs/1712.01262)\] proposed a compatibility family learning framework that embeds items into a latent space and projects queries into compatible prototypes, achieving state-of-the-art performance on multiple datasets. \[[17](http://arxiv.org/abs/1506.04757)\] introduced a Siamese CNN architecture to learn compatibility from user behavior data, demonstrating the effectiveness of cross-category fit learning. 

Personalization in outfit recommendation has also received significant attention. \[[6](https://www.semanticscholar.org/paper/b5f488dd55024f0db2cabb73b055002b5d995be9)\] introduced a framework that uses a two-level attention mechanism to capture user preferences, improving the accuracy of outfit recommendations. \[[24](https://www.semanticscholar.org/paper/30fb5c24cc15eb8cde5e389bf368d65fb96513e4)\] proposed a partitioned embedding network that enables interpretable and customizable outfit composition, addressing the limitations of black-box deep learning models. 

The challenge of generating outfits from user preferences has been tackled using generative models. \[[26](https://www.semanticscholar.org/paper/ca3ad34ff2652cd922c3476514a758674bc7e76b)\] proposed a personalized fashion design framework using generative adversarial training, which generates realistic items that match user preferences. \[[22](http://arxiv.org/abs/1906.07273)\] introduced a method that generates outfits based on text queries, ensuring compatibility and thematic coherence. 

The need for scalable and interpretable models has led to the development of graph-based approaches. \[[19](http://arxiv.org/abs/1905.03703)\] used a graph neural network to model outfit compatibility, showing improved performance in fill-in-the-blank and compatibility prediction tasks. \[[23](http://arxiv.org/abs/1902.08009)\] proposed Node-wise Graph Neural Networks (NGNN) to better capture interactions between items, leading to more accurate compatibility scores. 

In summary, while many approaches have focused on either compatibility or personalization, recent work has sought to unify these aspects, often through deep learning and graph-based models. The proposed framework, FashionDPO, builds on these advances by introducing a novel fine-tuning approach that leverages multi-expert feedback for direct preference optimization \[[1](http://arxiv.org/abs/1905.01866)\].

References:  
\[[1](http://arxiv.org/abs/1905.01866)\] POG: Personalized Outfit Generation for Fashion Recommendation at Alibaba iFashion  
\[[2](http://arxiv.org/abs/1807.03133)\] Outfit Generation and Style Extraction via Bidirectional LSTM and Autoencoder  
\[[3](http://arxiv.org/abs/1608.03016)\] Mining Fashion Outfit Composition Using an End-to-End Deep Learning Approach on Set Data  
\[[4](http://arxiv.org/abs/1803.09196)\] Learning Type-Aware Embeddings for Fashion Compatibility  
\[[5](http://arxiv.org/abs/1904.00741)\] Fashion Outfit Generation for E-commerce  
\[[6](https://www.semanticscholar.org/paper/b5f488dd55024f0db2cabb73b055002b5d995be9)\] $A^3$-FKG: Attentive Attribute-Aware Fashion Knowledge Graph for Outfit Preference Prediction  
\[[7](http://arxiv.org/abs/1908.09493)\] Supporting stylists by recommending fashion style  
\[[8](http://arxiv.org/abs/1711.02231)\] Visually-Aware Fashion Recommendation and Design with Generative Image Models  
\[[9](http://arxiv.org/abs/2005.12566)\] Hierarchical Fashion Graph Network for Personalized Outfit Recommendation  
\[[10](http://arxiv.org/abs/1712.02662)\] Creating Capsule Wardrobes from Fashion Images  
\[[11](http://arxiv.org/abs/1707.05691)\] Learning Fashion Compatibility with Bidirectional LSTMs  
\[[12](http://arxiv.org/abs/1805.00313)\] Neural Compatibility Modeling with Attentive Knowledge Distillation  
\[[13](http://arxiv.org/abs/1712.01262)\] Compatibility Family Learning for Item Recommendation and Generation  
\[[14](http://arxiv.org/abs/1810.02443)\] FashionNet: Personalized Outfit Recommendation with Deep Neural Network  
\[[15](https://www.semanticscholar.org/paper/762ec45448e915142f355848265d10dd55ab470f)\] OutfitNet: Fashion Outfit Recommendation with Attention-Based Multiple Instance Learning  
\[[16](http://arxiv.org/abs/1509.07473)\] Learning Visual Clothing Style with Heterogeneous Dyadic Co-Occurrences  
\[[17](http://arxiv.org/abs/1506.04757)\] Image-Based Recommendations on Styles and Substitutes  
\[[18](http://arxiv.org/abs/1707.03376)\] Learning the Latent “Look”: Unsupervised Discovery of a Style-Coherent Embedding from Fashion Images  
\[[19](http://arxiv.org/abs/1905.03703)\] Learning Fashion Compatibility Across Apparel Categories for Outfit Recommendation  
\[[20](https://www.semanticscholar.org/paper/396b400370ec78275b239ded03c1eba9d073f5eb)\] Personalized Capsule Wardrobe Creation with Garment and User Modeling  
\[[21](http://arxiv.org/abs/1708.04014)\] Style2Vec: Representation Learning for Fashion Items from Style Sets  
\[[22](http://arxiv.org/abs/1906.07273)\] Coherent and controllable outfit generation  
\[[23](http://arxiv.org/abs/1902.08009)\] Dressing as a Whole: Outfit Compatibility Learning Based on Node-wise Graph Neural Networks  
\[[24](https://www.semanticscholar.org/paper/30fb5c24cc15eb8cde5e389bf368d65fb96513e4)\] Interpretable Partitioned Embedding for Customized Multi-item Fashion Outfit Composition  
\[[25](http://arxiv.org/abs/2106.04128)\] Conversational Fashion Image Retrieval via Multiturn Natural Language Feedback  
\[[26](https://www.semanticscholar.org/paper/ca3ad34ff2652cd922c3476514a758674bc7e76b)\] Personalized Fashion Design
