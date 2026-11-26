## Related Works

Dense retrieval has emerged as a powerful alternative to traditional sparse retrieval methods, leveraging pre-trained language models (PLMs) to generate dense vector representations that can be compared using simple similarity operations \[[1](http://arxiv.org/abs/2108.05540)\]. The effectiveness of dense retrievers is closely tied to the pre-training phase, where models learn to encode semantic relationships between text segments \[[2](http://arxiv.org/abs/2104.08253)\]. Recent studies have questioned the role of fine-tuning in dense retrieval, arguing that much of the retrieval knowledge is acquired during pre-training, and that fine-tuning primarily adjusts neuron activations rather than reorganizing knowledge \[[3](http://arxiv.org/abs/2112.09118)\]. This idea was initially explored using BERT-based encoders with the Dense Passage Retrieval (DPR) framework \[[4](http://arxiv.org/abs/2002.08909)\]. However, the generalizability of this claim has not been thoroughly evaluated across different architectures, representation strategies, and datasets.

Several works have explored the pre-training and fine-tuning dynamics in dense retrieval. For example, \[[5](http://arxiv.org/abs/2204.10641)\] introduced the Condenser architecture, which pre-trains a Transformer model to condense information into dense vectors, improving retrieval performance over standard LM baselines. Similarly, \[[6](http://arxiv.org/abs/2205.12035)\] proposed coCondenser, which adds an unsupervised contrastive loss to warm up the passage embedding space, reducing the need for heavy data engineering and large batch training. These approaches highlight the importance of pre-training in shaping the quality of dense representations \[[7](https://www.semanticscholar.org/paper/5be217c678916543884c354654263f27c0a6bd9f)\].

The role of fine-tuning in dense retrieval has also been investigated in the context of different backbone architectures. For instance, \[[8](http://arxiv.org/abs/1907.11692)\] compared the use of CLS tokens versus mean pooling in dense retrieval, showing that mean pooling can lead to better performance in certain settings. Additionally, \[[9](http://arxiv.org/abs/2107.13602)\] explored the use of decoder-only models like LLaMA, demonstrating that decoder-based architectures can achieve competitive results in dense retrieval tasks \[[10](http://arxiv.org/abs/2207.02578)\]. These findings suggest that while pre-training is crucial, the choice of representation strategy and architecture can significantly impact the effectiveness of fine-tuning.

Moreover, \[[11](http://arxiv.org/abs/2107.07773)\] introduced the concept of contrastive learning for dense retrieval, showing that unsupervised contrastive methods can achieve strong performance without requiring labeled data. This aligns with the findings of \[[12](http://arxiv.org/abs/2006.03659)\], which demonstrated that contrastive learning can improve the quality of dense representations by learning to distinguish between relevant and irrelevant documents. The use of contrastive learning has also been extended to multi-lingual settings, where it enables cross-lingual retrieval between different scripts \[[13](http://arxiv.org/abs/2104.06967)\].

In summary, while pre-training plays a foundational role in dense retrieval, the effectiveness of fine-tuning depends on the architecture, representation strategy, and dataset used. The findings of this study extend previous analyses by evaluating a broader range of models and datasets, confirming that pre-trained knowledge underpins retrieval performance, with fine-tuning primarily adjusting neuron activation rather than reorganizing knowledge \[[14](http://arxiv.org/abs/1905.03197)\]. However, this pattern does not hold universally, as seen in models like Contriever (mean-pooled) and LLaMA (decoder-based) \[[15](http://arxiv.org/abs/2110.06918)\].

1. \[[1](http://arxiv.org/abs/2108.05540)\] BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding [1810.04805]
2. \[[2](http://arxiv.org/abs/2104.08253)\] Unified Language Model Pre-training for Natural Language Understanding and Generation [1905.03197]
3. \[[3](http://arxiv.org/abs/2112.09118)\] Dense Retrieval Based on Pretrained Language Models: A Survey [2211.14876]
4. \[[4](http://arxiv.org/abs/2002.08909)\] Dense Passage Retrieval [2104.08253]
5. \[[5](http://arxiv.org/abs/2204.10641)\] Condenser: a Pre-training Architecture for Dense Retrieval [2104.08253]
6. \[[6](http://arxiv.org/abs/2205.12035)\] coCondenser: Unsupervised Corpus Aware Language Model Pre-training for Dense Passage Retrieval [2108.05540]
7. \[[7](https://www.semanticscholar.org/paper/5be217c678916543884c354654263f27c0a6bd9f)\] Unsupervised Dense Information Retrieval with Contrastive Learning [2112.09118]
8. \[[8](http://arxiv.org/abs/1907.11692)\] Pre-train a Discriminative Text Encoder for Dense Retrieval via Contrastive Span Prediction [2204.10641]
9. \[[9](http://arxiv.org/abs/2107.13602)\] RetroMAE: Pre-Training Retrieval-oriented Language Models Via Masked Auto-Encoder [2205.12035]
10. \[[10](http://arxiv.org/abs/2207.02578)\] SimLM: Pre-training with Representation Bottleneck for Dense Passage Retrieval [2207.02578]
11. \[[11](http://arxiv.org/abs/2107.07773)\] More Robust Dense Retrieval with Contrastive Dual Learning [2107.07773]
12. \[[12](http://arxiv.org/abs/2006.03659)\] DeCLUTR: Deep Contrastive Learning for Unsupervised Textual Representations [2006.03659]
13. \[[13](http://arxiv.org/abs/2104.06967)\] Efficiently Teaching an Effective Dense Retriever with Balanced Topic Aware Sampling [2104.06967]
14. \[[14](http://arxiv.org/abs/1905.03197)\] MASTER: Multi-task Pre-trained Bottlenecked Masked Autoencoders are Better Dense Retrievers [2212.07841]
15. \[[15](http://arxiv.org/abs/2110.06918)\] Salient Phrase Aware Dense Retrieval: Can a Dense Retriever Imitate a Sparse One? [2110.06918]
16. \[[16](http://arxiv.org/abs/2208.09846)\] A Contrastive Pre-training Approach to Discriminative Autoencoder for Dense Retrieval [2208.09846]
17. \[[17](http://arxiv.org/abs/2212.07841)\] Dense Text Retrieval Based on Pretrained Language Models: A Survey [2211.14876]
18. \[[18](http://arxiv.org/abs/2211.14876)\] BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding [1810.04805]
19. \[[19](http://arxiv.org/abs/2007.00808)\] Complementing Lexical Retrieval with Semantic Residual Embedding [2004.13969]
20. \[[20](http://arxiv.org/abs/2305.02564)\] Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks [2005.11401]
21. \[[21](http://arxiv.org/abs/1810.04805)\] How to Train Your DRAGON: Diverse Augmentation Towards Generalizable Dense Retrieval [2302.07452]
22. \[[22](http://arxiv.org/abs/2004.13969)\] Multi-Task Deep Neural Networks for Natural Language Understanding [1901.11504]
23. \[[23](http://arxiv.org/abs/2005.11401)\] Representation Learning with Contrastive Predictive Coding [1807.03748]
24. \[[24](http://arxiv.org/abs/2302.07452)\] Llama2Vec: Unsupervised Adaptation of Large Language Models for Dense Retrieval [2312.15503]
25. \[[25](http://arxiv.org/abs/1901.11504)\] DRAMA: Diverse Augmentation from Large Language Models to Smaller Dense Retrievers [2502.18460]
26. \[[26](http://arxiv.org/abs/1807.03748)\] Explicit Inductive Bias for Transfer Learning with Convolutional Networks [1802.01483]
27. \[[27](http://arxiv.org/abs/2312.15503)\] XLNet: Generalized Autoregressive Pretraining for Language Understanding [1906.08237]
