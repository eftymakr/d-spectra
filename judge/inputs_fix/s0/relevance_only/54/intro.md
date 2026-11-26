## Related Works

Collaborative filtering (CF) has been a cornerstone in recommendation systems, leveraging user-item interactions to generate personalized recommendations \[[1](https://www.semanticscholar.org/paper/de2562febbdf3181834648d1fc679e2cb75aa973)\]. Recent advances in graph neural networks (GNNs) have significantly enhanced CF methods by enabling the modeling of high-order interactions through graph convolutional networks (GCNs) \[[2](http://arxiv.org/abs/2401.12590)\]. However, existing GCN-based CF models face several limitations. For instance, many models rely on linear transformations and nonlinear activation functions, which may not be optimal for recommendation tasks \[[3](http://arxiv.org/abs/2406.08827)\]. Moreover, the use of neighborhood aggregation often leads to oversmoothing and fails to capture fine-grained user preferences \[[4](http://arxiv.org/abs/1808.10523)\]. 

Several works have explored the use of graph signal processing (GSP) to improve CF. For example, PolyCF reframes CF as a graph signal processing problem, leveraging polynomial graph filters to capture spectral features across multiple eigenspaces \[[5](http://arxiv.org/abs/2007.03383)\]. Similarly, SpectralCF introduces a new spectral convolution operation to directly process the spectral domain of user-item bipartite graphs, thereby capturing deeper connections between users and items \[[6](http://arxiv.org/abs/2001.00267)\]. These methods highlight the potential of spectral graph filters in CF but often rely on complex training procedures or fail to address the issue of over-smoothing \[[7](http://arxiv.org/abs/1905.08108)\].

The importance of graph filters in recommendation has also been studied in the context of low-pass filtering. LCF proposes a low-pass collaborative filter to remove noise caused by exposure and quantization in observed data, improving the efficiency of graph convolution \[[8](http://arxiv.org/abs/2311.03316)\]. However, most existing methods are limited to low-pass filtering, ignoring the potential of middle and high-frequency components in graph signals \[[9](http://arxiv.org/abs/2307.04384)\]. AutoGCN addresses this by automatically adjusting the bandwidth of graph convolutional filters to capture the full spectrum of graph signals \[[10](https://www.semanticscholar.org/paper/219fd0434ce709f39d37df5452c811e7e9c4c9f9)\].

In addition to spectral graph filters, other approaches have focused on improving the efficiency and effectiveness of graph-based CF. LightGCN simplifies the design of GCN by removing unnecessary nonlinearities and feature transformations, resulting in a more efficient and effective model \[[11](https://www.semanticscholar.org/paper/a194dae103ce4593a8e15ecb1c1385cef3c60004)\]. Similarly, MDGCF enhances graph-based CF by mining neighborhood- and homogeneous-level dependencies to capture richer user-item interactions \[[12](http://arxiv.org/abs/2406.13996)\]. These methods demonstrate the importance of carefully designing graph convolutional layers to avoid over-smoothing and improve the expressiveness of embeddings \[[13](http://arxiv.org/abs/2002.02126)\].

Moreover, the issue of feature leakage in GNN-based recommendation systems has been addressed by EFLEC, which proposes an accurate removal algorithm to prevent label information from leaking into node embeddings \[[14](http://arxiv.org/abs/2006.15516)\]. This is crucial for ensuring the generalization of models in sparse interaction scenarios \[[15](http://arxiv.org/abs/2001.10167)\].

In summary, while many works have explored the use of graph filters in CF, there remains a gap in addressing the limitations of linear transformations, oversmoothing, and feature leakage. Our work, ChebyCF, introduces a novel approach based on graph spectral filtering that effectively overcomes these challenges by utilizing Chebyshev interpolation and an ideal pass filter \[[16](http://arxiv.org/abs/1705.07664)\].

### References

1. \[[1](https://www.semanticscholar.org/paper/de2562febbdf3181834648d1fc679e2cb75aa973)\] [Document 1]  
2. \[[2](http://arxiv.org/abs/2401.12590)\] [Document 2]  
3. \[[3](http://arxiv.org/abs/2406.08827)\] [Document 13]  
4. \[[4](http://arxiv.org/abs/1808.10523)\] [Document 15]  
5. \[[5](http://arxiv.org/abs/2007.03383)\] [Document 1]  
6. \[[6](http://arxiv.org/abs/2001.00267)\] [Document 4]  
7. \[[7](http://arxiv.org/abs/1905.08108)\] [Document 15]  
8. \[[8](http://arxiv.org/abs/2311.03316)\] [Document 14]  
9. \[[9](http://arxiv.org/abs/2307.04384)\] [Document 25]  
10. \[[10](https://www.semanticscholar.org/paper/219fd0434ce709f39d37df5452c811e7e9c4c9f9)\] [Document 25]  
11. \[[11](https://www.semanticscholar.org/paper/a194dae103ce4593a8e15ecb1c1385cef3c60004)\] [Document 13]  
12. \[[12](http://arxiv.org/abs/2406.13996)\] [Document 19]  
13. \[[13](http://arxiv.org/abs/2002.02126)\] [Document 15]  
14. \[[14](http://arxiv.org/abs/2006.15516)\] [Document 23]  
15. \[[15](http://arxiv.org/abs/2001.10167)\] [Document 23]  
16. \[[16](http://arxiv.org/abs/1705.07664)\] [User Abstract]
