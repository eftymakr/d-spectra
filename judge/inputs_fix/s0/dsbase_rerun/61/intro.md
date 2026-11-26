## Related Works

Personalized outfit generation has been a focal point in recent fashion technology research, with a growing emphasis on generating compatible and personalized fashion items. Early approaches to outfit recommendation focused on pre-defined outfits or personalized composition based on existing fashion items \[[6' 2022-11-29](http://arxiv.org/abs/2211.16353v1)\]. However, these methods were limited by the reliance on predefined fashion products, which constrained their ability to address diverse user needs \[[2' 2024-02-27](http://arxiv.org/abs/2402.17279v3)\]. To overcome these limitations, recent work has explored AI-generated content for outfit recommendation, enabling personalized outfit generation and recommendation \[[2' 2024-02-27](http://arxiv.org/abs/2402.17279v3)\].

Several studies have introduced generative models for outfit generation, aiming to improve compatibility and personalization. For example, Coherent and Controllable Outfit Generation \[[1' 2019-06-17](http://arxiv.org/abs/1906.07273v2)\] introduced a method that generates outfits whose items match a theme described by a text query. This approach uses text and image embeddings to represent fashion items and learns a multimodal embedding to measure item-query coherence. The method also employs a discriminator to compute compatibility between fashion items, achieving state-of-the-art results in compatibility prediction \[[1' 2019-06-17](http://arxiv.org/abs/1906.07273v2)\].

Diffusion models have also been applied to generative outfit recommendation, with the DiFashion model \[[2' 2024-02-27](http://arxiv.org/abs/2402.17279v3)\] demonstrating high fidelity, compatibility, and personalization in generated outfits. DiFashion enables parallel generation of multiple fashion images and uses Classifier-Free-Guidance to enhance alignment with conditions, leading to superior performance compared to competitive baselines \[[2' 2024-02-27](http://arxiv.org/abs/2402.17279v3)\].

Outfit generation frameworks such as FCBoost-Net \[[3' 2025-02-03](http://arxiv.org/abs/2502.00992v1)\] have focused on synthesizing multiple collocated and diversified outfits by improving compatibility through a novel fashion compatibility booster. This approach was inspired by boosting algorithms, allowing performance to be gradually improved in multiple steps. FCBoost-Net has shown effectiveness in maintaining visual authenticity and diversity while improving fashion compatibility \[[3' 2025-02-03](http://arxiv.org/abs/2502.00992v1)\].

Style-based outfit recommendation has also been explored, with methods such as the one proposed in \[[4' 2022-03-30](http://arxiv.org/abs/2203.16161v1)\] aiming to generate outfits conditional on styles or themes. This work uses a novel style encoder network to render outfit styles in a smooth latent space, enabling more flexible and interpretable style-based recommendations \[[4' 2022-03-30](http://arxiv.org/abs/2203.16161v1)\].

COutfitGAN \[[5' 2025-02-12](http://arxiv.org/abs/2502.08674v1)\] introduces a framework for synthesizing compatible fashion items based on given fashion items, focusing on photo-realistic image generation and compatibility. This model includes a pyramid style extractor, an outfit generator, and a UNet-based real/fake discriminator, achieving superior results in similarity, authenticity, and compatibility measurements \[[5' 2025-02-12](http://arxiv.org/abs/2502.08674v1)\].

In addition to these methods, several studies have focused on outfit completion and recommendation, such as the work on conditional set transformation \[[13' 2023-11-28](http://arxiv.org/abs/2311.16630v1)\] and the Box recommendation framework \[[14' 2024-02-26](http://arxiv.org/abs/2402.16660v1)\]. These approaches aim to generate outfits that match user preferences and budgets, incorporating price-range considerations and shopping budgets into the recommendation process \[[14' 2024-02-26](http://arxiv.org/abs/2402.16660v1)\].

The proposed FashionDPO framework addresses the limitations of existing methods by fine-tuning fashion outfit generation models using direct preference optimization. This approach eliminates the need for task-specific reward functions and leverages multi-expert feedback to ensure comprehensive and objective evaluation of generated outfits \[[26' 2018-06-29](http://arxiv.org/abs/1806.11371v1)\]. The framework has been evaluated on established datasets such as iFashion and Polyvore-U, demonstrating its effectiveness in aligning with users' personalized preferences while adhering to fashion compatibility principles \[[26' 2018-06-29](http://arxiv.org/abs/1806.11371v1)\].

1. Coherent and Controllable Outfit Generation \[[1' 2019-06-17](http://arxiv.org/abs/1906.07273v2)\]
2. Diffusion Models for Generative Outfit Recommendation \[[2' 2024-02-27](http://arxiv.org/abs/2402.17279v3)\]
3. FCBoost-Net: A Generative Network for Synthesizing Multiple Collocated Outfits via Fashion Compatibility Boosting \[[3' 2025-02-03](http://arxiv.org/abs/2502.00992v1)\]
4. Recommendation of Compatible Outfits Conditioned on Style \[[4' 2022-03-30](http://arxiv.org/abs/2203.16161v1)\]
5. COutfitGAN: Learning to Synthesize Compatible Fashion Items Supervised by Silhouette Masks and Fashion Styles \[[5' 2025-02-12](http://arxiv.org/abs/2502.08674v1)\]
6. Outfit Generation and Recommendation -- An Experimental Study \[[6' 2022-11-29](http://arxiv.org/abs/2211.16353v1)\]
7. Learning to Synthesize Compatible Fashion Items Using Semantic Alignment and Collocation Classification: An Outfit Generation Framework \[[7' 2025-02-05](http://arxiv.org/abs/2502.06827v1)\]
8. Outfit Generation and Style Extraction via Bidirectional LSTM and Autoencoder \[[8' 2018-06-29](http://arxiv.org/abs/1807.03133v3)\]
9. Session-based Complementary Fashion Recommendations \[[9' 2019-08-22](http://arxiv.org/abs/1908.08327v1)\]
10. Mining Fashion Outfit Composition Using An End-to-End Deep Learning Approach on Set Data \[[10' 2016-08-10](http://arxiv.org/abs/1608.03016v2)\]
11. Personalised Outfit Recommendation via History-aware Transformers \[[11' 2024-06-29](http://arxiv.org/abs/2407.00289v2)\]
12. Arithmetic Control of LLMs for Diverse User Preferences: Directional Preference Alignment with Multi-Objective Rewards \[[12' 2024-02-28](http://arxiv.org/abs/2402.18571v3)\]
13. Outfit Completion via Conditional Set Transformation \[[13' 2023-11-28](http://arxiv.org/abs/2311.16630v1)\]
14. BOXREC: Recommending a Box of Preferred Outfits in Online Shopping \[[14' 2024-02-26](http://arxiv.org/abs/2402.16660v1)\]
15. Hierarchical Fashion Graph Network for Personalized Outfit Recommendation \[[15' 2020-05-26](http://arxiv.org/abs/2005.12566v1)\]
16. OutfitTransformer: Learning Outfit Representations for Fashion Recommendation \[[16' 2022-04-11](http://arxiv.org/abs/2204.04812v2)\]
17. Fashion Recommendation: Outfit Compatibility using GNN \[[17' 2024-04-28](http://arxiv.org/abs/2404.18040v1)\]
18. Regularizing Reasons for Outfit Evaluation with Gradient Penalty \[[18' 2020-02-02](http://arxiv.org/abs/2002.00460v1)\]
19. Transformer-based Graph Neural Networks for Outfit Generation \[[19' 2023-04-17](http://arxiv.org/abs/2304.08098v1)\]
20. Fashion Outfit Complementary Item Retrieval \[[20' 2019-12-19](http://arxiv.org/abs/1912.08967v2)\]
21. FSPO: Few-Shot Optimization of Synthetic Preferences Personalizes to Real Users \[[21' 2025-02-26](http://arxiv.org/abs/2502.19312v2)\]
22. On Preference Learning Based on Sequential Bayesian Optimization with Pairwise Comparison \[[22' 2021-03-24](http://arxiv.org/abs/2103.13192v3)\]
23. Brand > Logo: Visual Analysis of Fashion Brands \[[23' 2018-10-23](http://arxiv.org/abs/1810.09941v1)\]
24. Optimal design of frame structures with mixed categorical and continuous design variables using the Gumbel-Softmax method \[[24' 2024-12-31](http://arxiv.org/abs/2501.00258v1)\]
25. Generating High-Resolution Fashion Model Images Wearing Custom Outfits \[[25' 2019-08-23](http://arxiv.org/abs/1908.08847v1)\]
26. Personalizing Similar Product Recommendations in Fashion E-commerce \[[26' 2018-06-29](http://arxiv.org/abs/1806.11371v1)\]
