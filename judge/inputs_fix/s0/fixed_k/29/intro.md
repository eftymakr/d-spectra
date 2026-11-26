## Related Works

Maximum Inner Product Search (MIPS) has been extensively studied in recent years due to its critical role in machine learning and information retrieval, especially in high-dimensional settings \[[1](http://arxiv.org/abs/2503.06882)\]. Traditional approaches to MIPS either rely solely on inner product similarity, which can lead to local optima and redundant computations \[[1](http://arxiv.org/abs/2503.06882)\], or reduce the problem to Euclidean Nearest Neighbor Search (NNS) through space projection, which often results in topology distortion and information loss \[[1](http://arxiv.org/abs/2503.06882)\]. While these paradigms have been explored separately, recent work suggests that the dichotomy between inner product and Euclidean metrics is not inherent and that integrating both can enhance MIPS performance \[[1](http://arxiv.org/abs/2503.06882)\].

Several methods have been proposed to address MIPS. For instance, the ip-NSW algorithm, an advanced graph-based approach, achieves significant speedup over existing baselines by leveraging the norm bias in the MIPS problem \[[3](http://arxiv.org/abs/1909.13459)\]. It effectively avoids unnecessary computations on small norm vectors by focusing on large norm items \[[3](http://arxiv.org/abs/1909.13459)\]. Building on this, ip-NSW+ further improves performance by introducing an angular proximity graph to refine the search process \[[3](http://arxiv.org/abs/1909.13459)\]. Similarly, the BanditMIPS algorithm presents a randomized approach with complexity independent of dimensionality, offering a 20× speedup on real-world datasets \[[4](http://arxiv.org/abs/2212.07551)\].

Another line of research explores budgeted MIPS, where the goal is to find the best approximate top-k results under a computational budget. The Greedy-MIPS algorithm, which balances search efficiency and quality, outperforms naive approaches by 200× on large-scale datasets \[[2](http://arxiv.org/abs/1610.03317)\]. Additionally, wedge sampling has been proposed as a method for budgeted top-k MIPS, demonstrating competitive performance compared to diamond sampling \[[6](http://arxiv.org/abs/1908.08656)\]. These approaches highlight the growing interest in adaptive and efficient MIPS algorithms that can handle large-scale and high-dimensional data.

In the realm of approximate MIPS, quantization-based methods have also been explored. For example, the proposed quantization approach for MIPS uses multiple subspaces to approximate inner products, avoiding the need for higher-dimensional feature space augmentation \[[7](http://arxiv.org/abs/1509.01469)\]. This method has shown superior performance on datasets arising from deep neural networks \[[7](http://arxiv.org/abs/1509.01469)\]. Furthermore, clustering-based approaches, such as those using spherical $k$-means, have been introduced to address approximate MIPS by efficiently partitioning data and reducing the search space \[[10](http://arxiv.org/abs/1507.05910)\].

The problem of reverse MIPS, where the goal is to find users who would be interested in a given item, has also been studied. Simpfer, an exact algorithm for reverse MIPS, uses a lightweight index to filter user vectors efficiently, achieving speedups of up to 8000× compared to baselines \[[13](http://arxiv.org/abs/2110.07131)\]. This demonstrates the versatility of MIPS in recommendation systems and e-commerce applications.

Finally, the integration of graph-based indexing and search strategies has shown promise in enhancing MIPS performance. The introduction of the Metric-Amphibious Graph (MAG) and Adaptive Navigation with Metric Switch (ANMS) algorithm is a direct extension of these ideas, aiming to combine the strengths of inner product and Euclidean metrics \[[1](http://arxiv.org/abs/2503.06882)\].

### References

1. \[[1](http://arxiv.org/abs/2503.06882)\] Maximum Inner Product is Query-Scaled Nearest Neighbor [http://arxiv.org/abs/2503.06882]  
2. \[[2](http://arxiv.org/abs/1610.03317)\] A Greedy Approach for Budgeted Maximum Inner Product Search [http://arxiv.org/abs/1610.03317]  
3. \[[3](http://arxiv.org/abs/1909.13459)\] Understanding and Improving Proximity Graph based Maximum Inner Product Search [http://arxiv.org/abs/1909.13459]  
4. \[[4](http://arxiv.org/abs/2212.07551)\] Faster Maximum Inner Product Search in High Dimensions [http://arxiv.org/abs/2212.07551]  
5. \[[5](http://arxiv.org/abs/2309.09013)\] Bridging Dense and Sparse Maximum Inner Product Search [http://arxiv.org/abs/2309.09013]  
6. \[[6](http://arxiv.org/abs/1908.08656)\] Revisiting Wedge Sampling for Budgeted Maximum Inner Product Search [http://arxiv.org/abs/1908.08656]  
7. \[[7](http://arxiv.org/abs/1509.01469)\] Quantization based Fast Inner Product Search [http://arxiv.org/abs/1509.01469]  
8. \[[8](http://arxiv.org/abs/2402.13858)\] Diversity-Aware k-Maximum Inner Product Search Revisited [http://arxiv.org/abs/2402.13858]  
9. \[[9](http://arxiv.org/abs/2104.04406)\] ProMIPS: Efficient High-Dimensional c-Approximate Maximum Inner Product Search with a Lightweight Index [http://arxiv.org/abs/2104.04406]  
10. \[[10](http://arxiv.org/abs/1507.05910)\] Clustering is Efficient for Approximate Maximum Inner Product Search [http://arxiv.org/abs/1507.05910]  
11. \[[11](http://arxiv.org/abs/1405.5869)\] Asymmetric LSH (ALSH) for Sublinear Time Maximum Inner Product Search (MIPS) [http://arxiv.org/abs/1405.5869]  
12. \[[12](http://arxiv.org/abs/1812.06360)\] A Bandit Approach to Maximum Inner Product Search [http://arxiv.org/abs/1812.06360]  
13. \[[13](http://arxiv.org/abs/2110.07131)\] Reverse Maximum Inner Product Search: How to efficiently find users who would like to buy my item? [http://arxiv.org/abs/2110.07131]  
14. \[[14](http://arxiv.org/abs/1410.5410)\] Improved Asymmetric Locality Sensitive Hashing (ALSH) for Maximum Inner Product Search (MIPS) [http://arxiv.org/abs/1410.5410]  
15. \[[15](http://arxiv.org/abs/2012.11098)\] Sublinear Maximum Inner Product Search using Concomitants of Extreme Order Statistics [http://arxiv.org/abs/2012.11098]  
16. \[[16](http://arxiv.org/abs/1809.08782)\] Norm-Ranging LSH for Maximum Inner Product Search [http://arxiv.org/abs/1809.08782]  
17. \[[17](http://arxiv.org/abs/2301.10622)\] An Approximate Algorithm for Maximum Inner Product Search over Streaming Sparse Vectors [http://arxiv.org/abs/2301.10622]  
18. \[[18](http://arxiv.org/abs/2405.12207)\] Optimistic Query Routing in Clustering-based Approximate Maximum Inner Product Search [http://arxiv.org/abs/2405.12207]  
19. \[[19](http://arxiv.org/abs/2309.00472)\] General and Practical Tuning Method for Off-the-Shelf Graph-Based Index: SISAP Indexing Challenge Report by Team UTokyo [http://arxiv.org/abs/2309.00472]
