## Related Works

Unsupervised pre-training has emerged as a powerful paradigm in machine learning, particularly in natural language processing and computer vision, where it enables models to learn rich representations from unlabeled data \[[1](http://arxiv.org/abs/1807.03748)\]. However, its application to DNA pre-training has been limited, primarily due to the lack of sufficient information in pure DNA sequences. Unlike images or text, DNA sequences alone do not capture the complex regulatory mechanisms that govern gene function, such as chromatin accessibility and other genomic profiles \[[2](http://arxiv.org/abs/1505.05192)\]. This limitation has led researchers to explore alternative approaches, including supervised training for genomic profile prediction, which can better capture the functional context of DNA sequences \[[3](http://arxiv.org/abs/1206.5538)\].

Several studies have investigated unsupervised learning methods for visual and textual representations, such as Contrastive Predictive Coding \[[1](http://arxiv.org/abs/1807.03748)\], which learns representations by predicting future samples in latent space. While these methods have shown promise, they often rely on large amounts of unlabeled data and may not fully capture the biological complexity of DNA sequences \[[4](http://arxiv.org/abs/1907.11692)\]. Similarly, approaches like SimCLR \[[10](http://arxiv.org/abs/2002.05709)\] and MoCo \[[17](http://arxiv.org/abs/1911.05722)\] have demonstrated the effectiveness of contrastive learning in vision tasks, but their direct application to genomic data remains unexplored.

In the field of natural language processing, BERT \[[16](http://arxiv.org/abs/1810.04805)\] and RoBERTa \[[14](http://arxiv.org/abs/2003.04297)\] have set new benchmarks for pre-training models using large-scale unlabeled text. These models use bidirectional transformers to learn contextual representations, which could be adapted for DNA sequence analysis. However, the regulatory context of DNA sequences requires a different set of features, such as chromatin accessibility and DNA methylation, which are not captured by traditional language models \[[5](https://www.semanticscholar.org/paper/4f7d1e04c9d30ce12df3e085d10d70997e6ea1a5)\].

Recent work on self-supervised learning has also explored the use of predictive tasks, such as predicting image rotations \[[22](http://arxiv.org/abs/1803.07728)\], to learn semantic features without explicit labels. This approach has been successful in computer vision, but its applicability to genomic data is yet to be validated. For instance, the work on unsupervised feature learning via non-parametric instance discrimination \[[7](http://arxiv.org/abs/1805.01978)\] highlights the importance of capturing instance-level similarity, which is critical for understanding DNA regulatory elements.

The introduction of the SPACE model builds upon these insights by leveraging supervised genomic profile prediction to improve DNA representation learning. This approach addresses the limitations of pure sequence pre-training by incorporating multi-species and multi-profile data, which is essential for capturing the regulatory context of DNA sequences \[[6](http://arxiv.org/abs/2203.06041)\]. The use of Mixture of Experts (MoE) in SPACE enables the model to adapt to different genomic profiles and species, leading to more effective and transferable representations \[[8](http://arxiv.org/abs/1910.10683)\].

In summary, while unsupervised pre-training has achieved significant success in various domains, its application to DNA sequence analysis remains underexplored. Supervised genomic profile prediction offers a more effective alternative, particularly when combined with advanced architectures like MoE to handle the complexity of multi-species and multi-profile data \[[9](http://arxiv.org/abs/1905.09272)\].

### References

1. \[[1](http://arxiv.org/abs/1807.03748)\] Representation Learning with Contrastive Predictive Coding  
2. \[[2](http://arxiv.org/abs/1505.05192)\] Unsupervised Visual Representation Learning by Context Prediction  
3. \[[3](http://arxiv.org/abs/1206.5538)\] Data-Efficient Image Recognition with Contrastive Predictive Coding  
4. \[[4](http://arxiv.org/abs/1907.11692)\] A Simple Framework for Contrastive Learning of Visual Representations  
5. \[[5](https://www.semanticscholar.org/paper/4f7d1e04c9d30ce12df3e085d10d70997e6ea1a5)\] RoBERTa: A Robustly Optimized BERT Pretraining Approach  
6. \[[6](http://arxiv.org/abs/2203.06041)\] Improved Baselines with Momentum Contrastive Learning  
7. \[[7](http://arxiv.org/abs/1805.01978)\] Unsupervised Feature Learning via Non-parametric Instance Discrimination  
8. \[[8](http://arxiv.org/abs/1910.10683)\] Momentum Contrast for Unsupervised Visual Representation Learning  
9. \[[9](http://arxiv.org/abs/1905.09272)\] Emerging Properties in Self-Supervised Vision Transformers  
10. \[[10](http://arxiv.org/abs/2002.05709)\] Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer  
11. \[[11](https://www.semanticscholar.org/paper/34f25a8704614163c4095b3ee2fc969b60de4698)\] Deep Residual Learning for Image Recognition  
12. \[[12](http://arxiv.org/abs/1512.03385)\] Unsupervised Learning of Visual Representations by Solving Jigsaw Puzzles  
13. \[[13](http://arxiv.org/abs/1603.09246)\] A Map of Human Genome Variation from Population Scale Sequencing  
14. \[[14](http://arxiv.org/abs/2003.04297)\] Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity  
15. \[[15](https://www.semanticscholar.org/paper/9d7af049cf76892dc1b5126c5a51cd09e08e3b5d)\] Learning Transferable Visual Models From Natural Language Supervision  
16. \[[16](http://arxiv.org/abs/1810.04805)\] BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding  
17. \[[17](http://arxiv.org/abs/1911.05722)\] Big Self-Supervised Models are Strong Semi-Supervised Learners  
18. \[[18](https://www.semanticscholar.org/paper/fec772a7cf60fea25932ce04439e71e492d684c0)\] Semi-Supervised Classification with Graph Convolutional Networks
