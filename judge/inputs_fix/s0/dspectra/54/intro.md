## Related Works

Graph-based collaborative filtering has seen significant advancements in recent years, with graph convolutional networks (GCNs) becoming a cornerstone in recommendation systems \[[1](http://arxiv.org/abs/1905.08108)\]. Early works such as Neural Graph Collaborative Filtering (NGCF) \[[1](http://arxiv.org/abs/1905.08108)\] emphasized the importance of integrating user-item interactions into the embedding process by propagating embeddings on the bipartite graph structure. This approach aimed to capture high-order connectivity and explicitly inject collaborative signals into the embedding process. However, subsequent research has highlighted limitations in these methods, particularly in terms of over-smoothing and the inability to model deeper layers due to the non-linear activation functions \[[6](http://arxiv.org/abs/2001.10167)\].

The use of graph convolutional networks in recommendation systems has been further refined by models such as LightGCN \[[3](http://arxiv.org/abs/2002.02126)\], which simplifies the design of GCNs by removing non-linearities and focusing on linear neighborhood aggregation. This approach has shown substantial improvements over NGCF, demonstrating the effectiveness of a simpler model in capturing collaborative signals. Similarly, the Linear Residual Graph Convolutional Network (LR-GCCF) \[[6](http://arxiv.org/abs/2001.10167)\] revisits GCN-based CF models by removing non-linearities and introducing a residual network structure to alleviate the over-smoothing problem, which is crucial for large-scale user-item graphs.

Another important development is the introduction of Multi-Graph Convolution Collaborative Filtering (Multi-GCCF) \[[2](http://arxiv.org/abs/2001.00267)\], which explicitly incorporates multiple graphs—user-user, item-item, and user-item—into the embedding learning process. This model not only captures high-order information from the bipartite graph but also integrates proximal information from user-user and item-item graphs, enhancing the richness of the learned embeddings.

The concept of graph filtering has also been extended to recommendation systems through the introduction of the Graph Trend Filtering Networks (GTN) \[[12](http://arxiv.org/abs/2108.05552)\], which address the issue of unreliable interactions by introducing a principled graph trend collaborative filtering method. This approach captures the adaptive reliability of interactions and improves the robustness of recommendation models against noisy or unreliable user behavior.

In addition, the work on spectral collaborative filtering \[[13](http://arxiv.org/abs/1808.10523)\] explores the use of spectral domain operations to directly perform convolution on the spectral domain of user-item bipartite graphs. This approach leverages the connectivity information hidden in the graph to discover deep connections between users and items, thereby alleviating the cold-start problem.

The effectiveness of graph convolutional networks in recommendation systems has also been studied through the lens of signal processing on graphs \[[21](http://arxiv.org/abs/1211.0053)\], which extends high-dimensional data analysis to irregular domains such as social networks. This field has led to the development of methods that generalize fundamental operations such as filtering to the graph setting, enabling more efficient and effective feature learning.

Finally, the work on Disentangled Graph Collaborative Filtering (DGCF) \[[9](http://arxiv.org/abs/2007.01764)\] introduces a novel approach to disentangle user intents in the embedding process, leading to more interpretable and effective recommendations. This model iteratively refines intent-aware interaction graphs and encourages independence among different intents, resulting in disentangled representations that capture the nuances of user preferences.

These developments highlight the ongoing efforts to improve the robustness, expressiveness, and efficiency of graph-based collaborative filtering models, paving the way for more accurate and personalized recommendation systems.

References  
\[[1](http://arxiv.org/abs/1905.08108)\] Neural Graph Collaborative Filtering  
\[[2](http://arxiv.org/abs/2001.00267)\] Multi-graph Convolution Collaborative Filtering  
\[[3](http://arxiv.org/abs/2002.02126)\] LightGCN: Simplifying and Powering Graph Convolution Network for Recommendation  
\[[6](http://arxiv.org/abs/2001.10167)\] Revisiting Graph based Collaborative Filtering: A Linear Residual Graph Convolutional Network Approach  
\[[9](http://arxiv.org/abs/2007.01764)\] RGCF: Refined graph convolution collaborative filtering with concise and expressive embedding  
\[[12](http://arxiv.org/abs/2108.05552)\] Graph Trend Filtering Networks for Recommendation  
\[[13](http://arxiv.org/abs/1808.10523)\] Spectral collaborative filtering
