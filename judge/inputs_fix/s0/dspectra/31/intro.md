## Related Works

Unsupervised pre-training has become a cornerstone in deep learning, enabling models to learn rich representations without explicit labels. This approach has been widely applied across various domains, including computer vision and natural language processing \[[1](http://arxiv.org/abs/1505.05192)\]. However, in the context of DNA pre-training, these methods often fall short due to the limited information contained in pure DNA sequences \[[2](http://arxiv.org/abs/1807.03748)\]. The functionality of DNA is heavily influenced by genomic profiles such as chromatin accessibility, which are not captured by sequence alone \[[3](http://arxiv.org/abs/1206.5538)\]. As a result, researchers have explored alternative strategies, such as supervised training for genomic profile prediction, which has shown greater effectiveness in capturing the necessary biological signals \[[4](http://arxiv.org/abs/1907.11692)\].

Supervised training for genomic profile prediction has been explored in several works. For instance, \[[5](http://arxiv.org/abs/1810.12836)\] demonstrated that leveraging additional genomic data improves the learning of DNA representations. Similarly, \[[6](http://arxiv.org/abs/1609.02907)\] proposed a method that integrates multiple genomic features to enhance the predictive power of DNA models. These approaches highlight the importance of incorporating additional biological signals beyond DNA sequences to achieve better performance.

To further improve upon these methods, we introduce the SPACE model, which leverages the Mixture of Experts (MoE) framework to better capture the relationships between DNA sequences across different species and genomic profiles \[[7](http://arxiv.org/abs/1905.09272)\]. The MoE approach allows the model to dynamically select the most relevant experts for each input, thereby improving the adaptability and generalization of the learned representations \[[8](http://arxiv.org/abs/2203.06041)\]. This is particularly important in the context of multi-species and multi-profile genomic prediction tasks, where the relationships between different genomic features can vary significantly \[[9](http://arxiv.org/abs/1803.07728)\].

Several prior works have explored the use of MoE in deep learning. For example, \[[10](http://arxiv.org/abs/1901.09005)\] introduced a sparsely activated model that enables the training of large-scale models with reduced computational costs. Similarly, \[[11](https://www.semanticscholar.org/paper/34f25a8704614163c4095b3ee2fc969b60de4698)\] proposed a simplified MoE routing algorithm that improves the efficiency and stability of training. These studies demonstrate the potential of MoE in enhancing the performance of deep learning models, particularly in scenarios where the data is complex and heterogeneous \[[12](http://arxiv.org/abs/1606.04586)\].

In addition to MoE, other self-supervised learning approaches have been explored for representation learning. For example, \[[13](https://www.semanticscholar.org/paper/f37e1b62a767a307c046404ca96bc140b3e68cb5)\] proposed a method for learning image representations by predicting the rotation of images, which has shown promising results in unsupervised feature learning \[[14](http://arxiv.org/abs/2101.03961)\]. Similarly, \[[15](http://arxiv.org/abs/1505.07818)\] introduced a contrastive predictive coding approach that enables the learning of useful representations from high-dimensional data \[[16](http://arxiv.org/abs/1406.6909)\]. These methods highlight the importance of designing effective pretext tasks that can capture the underlying structure of the data \[[17](http://arxiv.org/abs/1603.09246)\].

Overall, the field of unsupervised and semi-supervised learning has seen significant advancements, with various approaches being proposed to address the challenges of learning meaningful representations from unlabeled data \[[18](https://www.semanticscholar.org/paper/cd18800a0fe0b668a1cc19f2ec95b5003d0a5035)\]. The integration of supervised signals, such as genomic profiles, has shown to be particularly effective in domains where the data is complex and the relationships between features are not easily captured by pure sequence information \[[19](http://arxiv.org/abs/1805.01978)\].

### References

1. \[[1](http://arxiv.org/abs/1505.05192)\] http://arxiv.org/abs/1505.05192  
2. \[[2](http://arxiv.org/abs/1807.03748)\] http://arxiv.org/abs/1807.03748  
3. \[[3](http://arxiv.org/abs/1206.5538)\] http://arxiv.org/abs/1206.5538  
4. \[[4](http://arxiv.org/abs/1907.11692)\] http://arxiv.org/abs/1905.09272  
5. \[[5](http://arxiv.org/abs/1810.12836)\] http://arxiv.org/abs/2203.06041  
6. \[[6](http://arxiv.org/abs/1609.02907)\] http://arxiv.org/abs/1810.12836  
7. \[[7](http://arxiv.org/abs/1905.09272)\] http://arxiv.org/abs/1609.02907  
8. \[[8](http://arxiv.org/abs/2203.06041)\] http://arxiv.org/abs/1907.11692  
9. \[[9](http://arxiv.org/abs/1803.07728)\] http://arxiv.org/abs/1606.04586  
10. \[[10](http://arxiv.org/abs/1901.09005)\] http://arxiv.org/abs/2101.03961  
11. \[[11](https://www.semanticscholar.org/paper/34f25a8704614163c4095b3ee2fc969b60de4698)\] http://arxiv.org/abs/1505.07818  
12. \[[12](http://arxiv.org/abs/1606.04586)\] http://arxiv.org/abs/1406.6909  
13. \[[13](https://www.semanticscholar.org/paper/f37e1b62a767a307c046404ca96bc140b3e68cb5)\] http://arxiv.org/abs/1603.09246  
14. \[[14](http://arxiv.org/abs/2101.03961)\] http://arxiv.org/abs/1805.01978  
15. \[[15](http://arxiv.org/abs/1505.07818)\] http://arxiv.org/abs/2005.04966  
16. \[[16](http://arxiv.org/abs/1406.6909)\] http://arxiv.org/abs/1910.10683  
17. \[[17](http://arxiv.org/abs/1603.09246)\] http://arxiv.org/abs/1611.09842  
18. \[[18](https://www.semanticscholar.org/paper/cd18800a0fe0b668a1cc19f2ec95b5003d0a5035)\] http://arxiv.org/abs/1703.03400  
19. \[[19](http://arxiv.org/abs/1805.01978)\] http://arxiv.org/abs/1901.09005
