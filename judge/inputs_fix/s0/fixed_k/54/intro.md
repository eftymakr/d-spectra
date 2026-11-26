## Related Works

Collaborative filtering (CF) has been a cornerstone in recommendation systems, with recent advancements leveraging graph-based models to better capture user-item interactions \[[1](http://arxiv.org/abs/2401.12590)\]. Early CF methods, such as matrix factorization, relied on explicit user-item ratings, while later approaches incorporated deep learning and graph neural networks (GNNs) to model complex relationships \[[2](http://arxiv.org/abs/2007.03383)\]. Graph Convolutional Networks (GCNs) have emerged as a powerful tool for CF, enabling the aggregation of neighborhood information to generate more informative embeddings \[[3](http://arxiv.org/abs/2001.00267)\]. However, these models often suffer from issues such as over-smoothing and limited expressiveness due to their linear or fixed-frequency filtering mechanisms \[[4](http://arxiv.org/abs/1905.08108)\].

Several works have attempted to address these limitations. For instance, NGCF integrates user-item interactions directly into the embedding process by propagating embeddings on the bipartite graph, thereby capturing high-order connectivity \[[5](http://arxiv.org/abs/2311.03316)\]. Similarly, Multi-GCCF explicitly incorporates multiple graphs (user-user, item-item, and user-item) to model richer interaction patterns \[[6](http://arxiv.org/abs/2307.04384)\]. RGCF improves upon traditional GCN-based models by introducing a refined graph convolution structure and a fine-tuned normalization to better encode popularity features \[[7](http://arxiv.org/abs/2406.13996)\]. These methods, however, still rely on linear or fixed-frequency filters, which may not fully exploit the spectrum of graph signals \[[8](http://arxiv.org/abs/2001.10167)\].

To overcome these limitations, researchers have explored more flexible graph filters. PolyCF proposes a polynomial-based graph signal filter that captures spectral features across multiple eigenspaces, enabling the recovery of missing interactions \[[9](http://arxiv.org/abs/1911.10699)\]. The work in \[[10](http://arxiv.org/abs/2203.14748)\] further extends this idea by designing universal IIR graph filters using Butterworth, Chebyshev, and elliptic functions, achieving more accurate frequency responses than traditional polynomial-based filters \[[11](http://arxiv.org/abs/2107.04755)\]. AutoGCN introduces an automatic graph convolutional filter that dynamically adjusts its bandwidth, capturing both low and high-frequency components of graph signals \[[12](http://arxiv.org/abs/2004.14734)\]. These methods highlight the importance of spectral filtering in improving the expressiveness and robustness of CF models.

Despite these advancements, many existing models still face challenges in handling large-scale and sparse data. For example, the work in \[[13](http://arxiv.org/abs/2501.16888)\] introduces a residual network structure to alleviate over-smoothing in GCN-based CF models, while \[[14](http://arxiv.org/abs/2404.05962)\] proposes a linear residual GCN to improve scalability and efficiency. Additionally, \[[15](http://arxiv.org/abs/2412.01376)\] investigates the use of graph filters with adaptive propagation, allowing each node to independently decide the number of communication steps, thereby improving model performance \[[16](http://arxiv.org/abs/2412.01378)\]. These approaches demonstrate the potential of adaptive and flexible graph filtering in enhancing CF performance.

In summary, while existing methods have made significant strides in modeling user-item interactions using graph-based approaches, there remains a need for more expressive and adaptive graph filters that can better capture the full spectrum of graph signals. Our proposed ChebyCF framework builds on these insights by leveraging Chebyshev interpolation and ideal pass filters to achieve more accurate and flexible graph spectral filtering \[[17](http://arxiv.org/abs/1811.10435)\].

### References

1. \[[1](http://arxiv.org/abs/2401.12590)\] http://arxiv.org/abs/2401.12590  
2. \[[2](http://arxiv.org/abs/2007.03383)\] http://arxiv.org/abs/2007.03383  
3. \[[3](http://arxiv.org/abs/2001.00267)\] http://arxiv.org/abs/2001.00267  
4. \[[4](http://arxiv.org/abs/1905.08108)\] http://arxiv.org/abs/1905.08108  
5. \[[5](http://arxiv.org/abs/2311.03316)\] http://arxiv.org/abs/2311.03316  
6. \[[6](http://arxiv.org/abs/2307.04384)\] http://arxiv.org/abs/2307.04384  
7. \[[7](http://arxiv.org/abs/2406.13996)\] http://arxiv.org/abs/2406.13996  
8. \[[8](http://arxiv.org/abs/2001.10167)\] http://arxiv.org/abs/2001.10167  
9. \[[9](http://arxiv.org/abs/1911.10699)\] http://arxiv.org/abs/1911.10699  
10. \[[10](http://arxiv.org/abs/2203.14748)\] http://arxiv.org/abs/2203.14748  
11. \[[11](http://arxiv.org/abs/2107.04755)\] http://arxiv.org/abs/2107.04755  
12. \[[12](http://arxiv.org/abs/2004.14734)\] http://arxiv.org/abs/2004.14734  
13. \[[13](http://arxiv.org/abs/2501.16888)\] http://arxiv.org/abs/2501.16888  
14. \[[14](http://arxiv.org/abs/2404.05962)\] http://arxiv.org/abs/2404.05962  
15. \[[15](http://arxiv.org/abs/2412.01376)\] http://arxiv.org/abs/2412.01376  
16. \[[16](http://arxiv.org/abs/2412.01378)\] http://arxiv.org/abs/2412.01378  
17. \[[17](http://arxiv.org/abs/1811.10435)\] http://arxiv.org/abs/1811.10435
