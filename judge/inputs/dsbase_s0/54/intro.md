## Related Works

Graph Convolutional Networks (GCNs) have become a cornerstone in collaborative filtering (CF) for recommendation systems, leveraging the structural information of user-item interaction graphs to capture complex preference patterns \[[Yifang Qin' 2024-01-23](http://arxiv.org/abs/2401.12590v2)\]. However, existing GCN-based approaches face significant limitations. One major issue is the embedding layer, which often results in a latent space with limited capacity, thereby neglecting locally observed but potentially valuable preference patterns \[[Wenqi Fan' 2021-08-12](http://arxiv.org/abs/2108.05552v2)\]. Another limitation is the neighborhood aggregation mechanism, which is typically limited in its ability to leverage diverse preference patterns in a fine-grained manner \[[Pang Li' 2024-12-02](http://arxiv.org/abs/2412.01378v1)\].

Several studies have attempted to address these challenges. For instance, \[[Zonghan Wu' 2021-07-10](http://arxiv.org/abs/2107.04755v3)\] introduces a residual network structure specifically designed for CF with user-item interaction modeling, which alleviates the over-smoothing problem in graph convolution aggregation operations with sparse user-item interaction data. Similarly, \[[Yihong Wu' 2024-06-20](http://arxiv.org/abs/2406.13996v2)\] proposes a linear model for CF that is easy to train, scale to large datasets, and yield better efficiency and effectiveness on real datasets. These works highlight the importance of addressing over-smoothing and improving the expressiveness of the model.

The use of graph spectral filtering has also been explored in the context of recommendation systems. \[[Kang Liu' 2020-07-07](http://arxiv.org/abs/2007.03383v2)\] presents a novel graph convolutional neural network (GCN) using GraphBio as the graph filter, which is analytically defined and requires no training. This approach optimizes the graph spectrum via data training while maintaining interpretability. Additionally, \[[Xiang Wang' 2019-05-20](http://arxiv.org/abs/1905.08108v2)\] introduces a method for graph-based collaborative filtering using linear residual graph convolutional networks, which improves recommendation performance by learning more evenly distributed user and item representations.

Another key area of research is the use of Chebyshev polynomials for graph filtering. \[[Kathrin Glau' 2016-11-26](http://arxiv.org/abs/1611.08706v1)\] discusses the application of Chebyshev polynomials in graph signal processing, emphasizing their ability to efficiently approximate non-linear filters. \[[Zirui Ge' 2022-03-28](http://arxiv.org/abs/2203.14748v1)\] extends this idea by proposing a method for graph-based image denoising using Chebyshev and conjugate gradient filters, demonstrating improved performance over existing polynomial graph filters. These studies provide a foundation for the use of Chebyshev interpolation in graph-based recommendation systems.

In addition, \[[Shoujin Wang' 2021-05-13](http://arxiv.org/abs/2105.06339v1)\] presents a method for graph-based collaborative filtering using linear residual graph convolutional networks, which improves recommendation performance by learning more evenly distributed user and item representations. This work is closely related to our approach, as it also addresses the limitations of traditional GCN-based methods.

References:

1. [Document 4]  
2. [Document 11]  
3. [Document 22]  
4. [Document 17]  
5. [Document 6]  
6. [Document 9]  
7. [Document 15]  
8. [Document 20]  
9. [Document 23]  
10. [Document 15]
