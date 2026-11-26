## Related Works

Personalized outfit generation has been a focal point in recent fashion AI research, with a growing emphasis on generating compatible and personalized fashion items. Early approaches primarily focused on pre-defined outfit recommendation and personalized outfit composition, which were constrained by existing fashion products, limiting their ability to address diverse user needs \[[2](http://arxiv.org/abs/2402.17279)\]. More recently, AI-generated content has enabled the development of Generative Outfit Recommendation (GOR), which aims to generate visually compatible outfits tailored to specific users \[[2](http://arxiv.org/abs/2402.17279)\]. This task requires high fidelity, compatibility, and personalization, which are challenging to achieve simultaneously \[[2](http://arxiv.org/abs/2402.17279)\].

Several studies have explored the use of deep learning models for outfit generation and recommendation. For example, POG (Personalized Outfit Generation) leverages Transformer architecture to connect user preferences with outfit generation, improving compatibility and personalization \[[1](http://arxiv.org/abs/1905.01866)\]. Similarly, OutfitTransformer introduces a framework that uses self-attention mechanisms to learn effective outfit-level representations, enabling compatibility prediction and complementary item retrieval \[[16](http://arxiv.org/abs/2204.04812)\]. The model is trained using a set-wise outfit ranking loss to generate target item embeddings, which are then used to retrieve compatible items \[[16](http://arxiv.org/abs/2204.04812)\].

Another line of research focuses on improving the compatibility and personalization of generated outfits through advanced neural network architectures. For instance, COutfitGAN proposes a framework that includes a pyramid style extractor, an outfit generator, and discriminators to ensure compatibility and realism \[[18](http://arxiv.org/abs/2502.08674)\]. This approach synthesizes photo-realistic images of complementary fashion items, outperforming existing baselines in terms of similarity, authenticity, and compatibility \[[18](http://arxiv.org/abs/2502.08674)\].

The challenge of generating diverse and personalized outfits has also been addressed through the use of multi-modal and transformer-based models. For example, the work by \[[21](http://arxiv.org/abs/2502.06827)\] introduces OutfitGAN, which combines semantic alignment and collocation classification to synthesize compatible fashion items. The model is trained on a large-scale dataset and achieves state-of-the-art results in terms of compatibility and authenticity \[[21](http://arxiv.org/abs/2502.06827)\]. Similarly, the Hierarchical Fashion Graph Network (HFGN) unifies fashion compatibility modeling and personalized outfit recommendation by constructing a hierarchical graph that captures user-outfit and outfit-item relationships \[[23](http://arxiv.org/abs/2005.12566)\].

In addition to compatibility and personalization, recent studies have also focused on improving the interpretability and controllability of outfit generation models. For example, the work by \[[6](http://arxiv.org/abs/1906.07273)\] introduces a method that generates outfits matching a specified theme, using text and image embeddings to measure item-query coherence \[[6](http://arxiv.org/abs/1906.07273)\]. This approach ensures that the generated outfits are both compatible and aligned with user preferences \[[6](http://arxiv.org/abs/1906.07273)\].

Finally, the cold-start problem in outfit recommendation has been addressed through visual preference modeling. This approach leverages feature-weighted clustering to personalize outfit recommendations for new users, outperforming state-of-the-art methods in clothing attribute prediction \[[25](http://arxiv.org/abs/2008.01437)\].

In summary, the field of personalized outfit generation has seen significant advancements, with a focus on improving compatibility, personalization, and interpretability. These works provide a strong foundation for the proposed framework, FashionDPO, which aims to address the limitations of existing methods through direct preference optimization \[[1](http://arxiv.org/abs/1905.01866)\].

### References

1. \[[1](http://arxiv.org/abs/1905.01866)\] POG: Personalized Outfit Generation for Fashion Recommendation at Alibaba iFashion  
2. \[[2](http://arxiv.org/abs/2402.17279)\] Diffusion Models for Generative Outfit Recommendation  
3. \[[3](http://arxiv.org/abs/2211.16353)\] Outfit Generation and Recommendation - An Experimental Study  
4. \[[4](http://arxiv.org/abs/2502.04370)\] DreamDPO: Aligning Text-to-3D Generation with Human Preferences via Direct Preference Optimization  
5. \[[5](http://arxiv.org/abs/1904.00741)\] Fashion Outfit Generation for E-commerce  
6. \[[6](http://arxiv.org/abs/1906.07273)\] Coherent and controllable outfit generation  
7. \[[7](http://arxiv.org/abs/2205.00663)\] An Application to Generate Style Guided Compatible Outfit  
8. \[[8](http://arxiv.org/abs/1807.03133)\] Outfit Generation and Style Extraction via Bidirectional LSTM and Autoencoder  
9. \[[9](http://arxiv.org/abs/2502.00992)\] FCBoost-Net: A Generative Network for Synthesizing Multiple Collocated Outfits via Fashion Compatibility Boosting  
10. \[[10](http://arxiv.org/abs/2409.12150)\] Decoding Style: Efficient Fine-Tuning of LLMs for Image-Guided Outfit Recommendation with Preference  
11. \[[11](http://arxiv.org/abs/2504.09915)\] StePO-Rec: Towards Personalized Outfit Styling Assistant via Knowledge-Guided Multi-Step Reasoning  
12. \[[12](http://arxiv.org/abs/1906.06619)\] Generating Diverse and Informative Natural Language Fashion Feedback  
13. \[[13](http://arxiv.org/abs/2008.01780)\] PAI-BPR: Personalized Outfit Recommendation Scheme with Attribute-wise Interpretability  
14. \[[14](http://arxiv.org/abs/1608.03016)\] Mining Fashion Outfit Composition Using an End-to-End Deep Learning Approach on Set Data  
15. \[[15](http://arxiv.org/abs/2404.13846)\] Filtered Direct Preference Optimization  
16. \[[16](http://arxiv.org/abs/2204.04812)\] OutfitTransformer: Learning Outfit Representations for Fashion Recommendation  
17. \[[17](http://arxiv.org/abs/1806.08977)\] Explainable Outfit Recommendation with Joint Outfit Matching and Comment Generation  
18. \[[18](http://arxiv.org/abs/2502.08674)\] COutfitGAN: Learning to Synthesize Compatible Outfits Supervised by Silhouette Masks and Fashion Styles  
19. \[[19](http://arxiv.org/abs/1804.09979)\] Recommending Outfits from Personal Closet  
20. \[[20](http://arxiv.org/abs/2304.08098)\] Transformer-Based Graph Neural Networks for Outfit Generation  
21. \[[21](http://arxiv.org/abs/2502.06827)\] Learning to Synthesize Compatible Fashion Items Using Semantic Alignment and Collocation Classification: An Outfit Generation Framework  
22. \[[22](http://arxiv.org/abs/2203.16161)\] Recommendation of Compatible Outfits Conditioned on Style  
23. \[[23](http://arxiv.org/abs/2005.12566)\] Hierarchical Fashion Graph Network for Personalized Outfit Recommendation  
24. \[[24](http://arxiv.org/abs/1908.08847)\] Generating High-Resolution Fashion Model Images Wearing Custom Outfits  
25. \[[25](http://arxiv.org/abs/2008.01437)\] Addressing the Cold-Start Problem in Outfit Recommendation Using Visual Preference Modelling  
26. \[[26](http://arxiv.org/abs/2402.05941)\] Character-based Outfit Generation with Vision-augmented Style Extraction via LLMs  
27. \[[27](http://arxiv.org/abs/2005.06584)\] Fashion Recommendation and Compatibility Prediction Using Relational Network
