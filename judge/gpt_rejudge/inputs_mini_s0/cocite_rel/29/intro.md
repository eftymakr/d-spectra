## Related Works

Maximum Inner Product Search (MIPS) is a fundamental problem in machine learning and information retrieval, especially for high-dimensional data. Traditional approaches often rely on inner product (IP) similarity directly, which can suffer from issues such as local optima and redundant computations \[[1405.5869](http://arxiv.org/abs/1405.5869)\]. To address these challenges, some methods reduce MIPS to Nearest Neighbor Search (NNS) under Euclidean or cosine similarity metrics by projecting or transforming the original space. However, such reductions often cause topology distortion and information loss, limiting search quality \[[1410.5410](http://arxiv.org/abs/1410.5410)\]\[[https://www.semanticscholar.org/paper/d8aad5d9c2c336c550ca9621b73c7688f184d50b](https://www.semanticscholar.org/paper/d8aad5d9c2c336c550ca9621b73c7688f184d50b)\].

### Hashing-Based Approaches

Locality Sensitive Hashing (LSH) was extended to MIPS through asymmetric transformations, leading to the Asymmetric LSH (ALSH) framework. ALSH converts MIPS into approximate nearest neighbor problems under L2 or cosine similarity, enabling sublinear time search with theoretical guarantees \[[1405.5869](http://arxiv.org/abs/1405.5869)\]\[[1410.5410](http://arxiv.org/abs/1410.5410)\]. Later improvements, such as H2-ALSH, introduced homocentric hypersphere partitioning and query normalization to reduce distortion errors and improve accuracy and efficiency \[[https://www.semanticscholar.org/paper/865488b467250ceb85bb59d35b8d4fb4f10ae421](https://www.semanticscholar.org/paper/865488b467250ceb85bb59d35b8d4fb4f10ae421)\]. Norm-Ranging LSH further refined hashing by partitioning datasets based on norm distribution to mitigate normalization issues from long-tail norms, achieving better query efficiency than SIMPLE-LSH \[[1809.08782](http://arxiv.org/abs/1809.08782)\]. Quantization-based methods also approximate inner products by decomposing vectors into subspaces and learning codebooks that minimize quantization error, yielding significant speedups and accuracy gains \[[1509.01469](http://arxiv.org/abs/1509.01469)\].

### Graph-Based Methods

Graph-based indices have emerged as a powerful paradigm for MIPS, often outperforming hashing and quantization techniques in practice. The inner-product navigable small world graph (ip-NSW) exploits a norm bias inherent in MIPS whereby items with larger norms dominate search results; this property is harnessed by graph construction and traversal to avoid redundant exploration of low-norm nodes, achieving order-of-magnitude speedups \[[1909.13459](http://arxiv.org/abs/1909.13459)\]. Building on ip-NSW, ip-NSW+ introduces an additional angular proximity graph to guide candidate selection, further enhancing robustness and search quality across diverse data distributions \[[1909.13459](http://arxiv.org/abs/1909.13459)\]\[[1202.6101](http://arxiv.org/abs/1202.6101)\]. Norm Adjusted Proximity Graph (NAPG) refines graph connectivity by adjusting edges based on sampled norm statistics, improving the meaningfulness of neighborhood relations and thus search efficiency \[[https://www.semanticscholar.org/paper/25454f456c514219c9d6eeb42200ebbf378db9ca](https://www.semanticscholar.org/paper/25454f456c514219c9d6eeb42200ebbf378db9ca)\]. Reinforcement learning-based routing on proximity graphs has also been explored to automatically optimize search paths without relying solely on ground truth labels, showing competitive results \[[2201.09290](http://arxiv.org/abs/2201.09290)\].

### Branch-and-Bound and Tree-Based Algorithms

Cone trees and dual-tree algorithms provide efficient branch-and-bound strategies for exact or approximate MIPS by exploiting inner product bounds. These tree structures enable pruning large portions of the search space and yield substantial query time improvements over brute-force methods, sometimes by several orders of magnitude \[[1202.6101](http://arxiv.org/abs/1202.6101)\].

### Sampling and Statistical Methods

Sampling-based algorithms like Diamond Sampling avoid exhaustive computation of all pairwise dot products by probabilistically focusing on pairs with large inner products, resulting in significant speedups and improved quality over hashing methods \[[1506.03872](http://arxiv.org/abs/1506.03872)\]. Extreme order statistics have also been leveraged via dimensionality reduction methods such as CEOs and its variants, which select projections associated with extreme query values to efficiently approximate MIPS with high recall and sublinear search times \[[https://www.semanticscholar.org/paper/d204d3848bb76ecca93a0674230303785b82c3b2](https://www.semanticscholar.org/paper/d204d3848bb76ecca93a0674230303785b82c3b2)\].

### Hardware-Efficient and Exact Methods

While approximate methods dominate, exact MIPS remains important. Hardware-optimized brute-force techniques based on blocked matrix multiplication (BMM) have been shown to outperform many indexing methods on certain datasets \[[https://www.semanticscholar.org/paper/0b2790c2c1e23e5535421696e1ec763bbc651bbd](https://www.semanticscholar.org/paper/0b2790c2c1e23e5535421696e1ec763bbc651bbd)\]. Hybrid approaches like MAX-IMUS combine efficient pruning with hardware acceleration, and data-dependent optimizers like OPTIMUS select the best solver online to maximize performance across diverse inputs \[[https://www.semanticscholar.org/paper/0b2790c2c1e23e5535421696e1ec763bbc651bbd](https://www.semanticscholar.org/paper/0b2790c2c1e23e5535421696e1ec763bbc651bbd)\].

### Integration of Inner Product and Euclidean Metrics

The theoretical and empirical unification of IP and Euclidean metrics has gained attention. The norm bias observed in MIPS suggests that Euclidean-based proximity information can guide inner product search effectively. For example, ip-NSW+ leverages both inner product and angular proximity graphs to exploit complementary metric properties \[[1909.13459](http://arxiv.org/abs/1909.13459)\]. Recent works argue against a strict dichotomy between IP and Euclidean metrics, advocating hybrid designs that dynamically switch or blend metrics depending on data topology \[[2201.09290](http://arxiv.org/abs/2201.09290)\]. These insights motivate novel indexing structures like the Metric-Amphibious Graph (MAG) and associated Adaptive Navigation with Metric Switch (ANMS) search algorithm, which adaptively toggle between metrics to optimize performance based on statistical indicators capturing data topology \[[2104.04406](http://arxiv.org/abs/2104.04406)\]\[[https://www.semanticscholar.org/paper/2040c5de2344b9b14f1bbfff372f708639cca739](https://www.semanticscholar.org/paper/2040c5de2344b9b14f1bbfff372f708639cca739)\].

### Summary

Overall, the literature reveals a rich ecosystem of MIPS approaches spanning hashing, graph-based search, tree structures, sampling, and hardware acceleration. Key themes include overcoming the non-metric nature of inner product similarity, mitigating norm-related biases, and leveraging multiple complementary metric spaces to enhance search efficiency and accuracy. Graph-based methods, particularly those integrating inner product and Euclidean perspectives, currently represent the state-of-the-art in balancing scalability, adaptability, and search speed \[[1909.13459](http://arxiv.org/abs/1909.13459)\]\[[https://www.semanticscholar.org/paper/25454f456c514219c9d6eeb42200ebbf378db9ca](https://www.semanticscholar.org/paper/25454f456c514219c9d6eeb42200ebbf378db9ca)\]\[[2201.09290](http://arxiv.org/abs/2201.09290)\]\[[2104.04406](http://arxiv.org/abs/2104.04406)\].

### References

1. Asymmetric LSH (ALSH) for Sublinear Time Maximum Inner Product Search (http://arxiv.org/abs/1405.5869)  
2. A Greedy Approach for Budgeted Maximum Inner Product Search (http://arxiv.org/abs/1610.03317)  
3. Accurate and Fast Asymmetric Locality-Sensitive Hashing Scheme for Maximum Inner Product Search (https://www.semanticscholar.org/paper/865488b467250ceb85bb59d35b8d4fb4f10ae421)  
4. Understanding and Improving Proximity Graph based Maximum Inner Product Search (http://arxiv.org/abs/1909.13459)  
5. Norm-Ranging LSH for Maximum Inner Product Search (http://arxiv.org/abs/1809.08782)  
6. Maximum inner-product search using cone trees (http://arxiv.org/abs/1202.6101)  
7. Diamond Sampling for Approximate Maximum All-Pairs Dot-Product (MAD) Search (http://arxiv.org/abs/1506.03872)  
8. Improved Asymmetric Locality Sensitive Hashing (ALSH) for Maximum Inner Product Search (http://arxiv.org/abs/1410.5410)  
9. Norm Adjusted Proximity Graph for Fast Inner Product Retrieval (https://www.semanticscholar.org/paper/25454f456c514219c9d6eeb42200ebbf378db9ca)  
10. To Index or Not to Index: Optimizing Exact Maximum Inner Product Search (https://www.semanticscholar.org/paper/0b2790c2c1e23e5535421696e1ec763bbc651bbd)  
11. ProMIPS: Efficient High-Dimensional c-Approximate Maximum Inner Product Search with a Lightweight Index (http://arxiv.org/abs/2104.04406)  
13. Reinforcement Routing on Proximity Graph for Efficient Recommendation (http://arxiv.org/abs/2201.09290)  
14. Simple Yet Efficient Algorithms for Maximum Inner Product Search via Extreme Order Statistics (https://www.semanticscholar.org/paper/d204d3848bb76ecca93a0674230303785b82c3b2)  
16. Speeding up the Xbox recommender system using a euclidean transformation for inner-product spaces (https://www.semanticscholar.org/paper/d8aad5d9c2c336c550ca9621b73c7688f184d50b)  
18. Quantization based Fast Inner Product Search (http://arxiv.org/abs/1509.01469)