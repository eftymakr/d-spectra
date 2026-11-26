## Related Works

Maximum Inner Product Search (MIPS) has been a focal point in machine learning and information retrieval, particularly in high-dimensional data applications \[[1](http://arxiv.org/abs/1405.5869)\]. Traditional approaches to MIPS often rely solely on inner product (IP) similarity, which can suffer from local optima and redundant computations \[[1](http://arxiv.org/abs/1405.5869)\]. Alternatively, some methods reduce MIPS to Euclidean metric-based nearest neighbor search through space projection, which may lead to topology destruction and information loss \[[1](http://arxiv.org/abs/1405.5869)\]. However, recent studies have shown that there is no inherent binary opposition between IP and Euclidean metrics, and that integrating both can lead to significant performance improvements \[[1](http://arxiv.org/abs/1405.5869)\].

Asymmetric LSH (ALSH) was introduced as a provably sublinear time algorithm for approximate MIPS, leveraging asymmetric transformations to convert the problem into approximate near neighbor search \[[2](http://arxiv.org/abs/1610.03317)\]. This approach was later improved with a different transformation that converted MIPS into cosine similarity search using signed random projections, showing theoretical and empirical superiority \[[6](http://arxiv.org/abs/1410.5410)\]. Similarly, the Norm-Ranging LSH method addressed the issue of long-tailed 2-norm distributions by partitioning datasets and building hash indexes independently, achieving lower query time complexity \[[5](http://arxiv.org/abs/1809.08782)\].

Graph-based methods have also gained traction in MIPS. The inner-product navigable small world graph (ip-NSW) represents a state-of-the-art method, achieving an order of magnitude speedup over baselines by exploiting norm bias in the data \[[3](http://arxiv.org/abs/1909.13459)\]. This norm bias, where large norm items are more likely to be the result of MIPS, is effectively leveraged by ip-NSW through high in-degrees for large norm items \[[3](http://arxiv.org/abs/1909.13459)\]. Further improvements were made with ip-NSW+, which introduced an angular proximity graph to refine search results \[[3](http://arxiv.org/abs/1909.13459)\].

Quantization-based approaches have also been proposed, such as the method that quantizes database vectors into multiple subspaces and approximates inner products as sums of inner products with subspace quantizers \[[8](http://arxiv.org/abs/1509.01469)\]. This avoids the need for higher-dimensional feature space augmentation, offering a more efficient solution \[[8](http://arxiv.org/abs/1509.01469)\].

In addition, the Norm Adjusted Proximity Graph (NAPG) was introduced as a graph-based indexing method that adjusts factors based on sampled data to improve the selection of meaningful data points during graph construction \[[12](https://www.semanticscholar.org/paper/25454f456c514219c9d6eeb42200ebbf378db9ca)\]. This method has shown strong empirical performance in real-world MIPS tasks \[[12](https://www.semanticscholar.org/paper/25454f456c514219c9d6eeb42200ebbf378db9ca)\].

The problem of finding the top-t dot products between two sets of vectors was addressed using diamond sampling, which selects diamonds (four-cycles) in a weighted tripartite representation, focusing on the largest-magnitude entries \[[16](http://arxiv.org/abs/1506.03872)\]. This method was applied to MIPS, showing significant improvements over hashing methods \[[16](http://arxiv.org/abs/1506.03872)\].

Finally, the use of extreme order statistics for dimensionality reduction in MIPS, known as CEOs, was proposed to estimate inner products using a few projections associated with extreme values \[[17](https://www.semanticscholar.org/paper/d204d3848bb76ecca93a0674230303785b82c3b2)\]. This approach provides a sublinear approximate MIPS algorithm with recall guarantees \[[17](https://www.semanticscholar.org/paper/d204d3848bb76ecca93a0674230303785b82c3b2)\].

These diverse methods highlight the ongoing research into improving MIPS performance through various techniques, including hashing, graph-based indexing, quantization, and statistical modeling.

1. \[[1](http://arxiv.org/abs/1405.5869)\] Abstract  
2. \[[2](http://arxiv.org/abs/1610.03317)\] Asymmetric LSH for Sublinear Time Maximum Inner Product Search  
3. \[[3](http://arxiv.org/abs/1909.13459)\] Understanding and Improving Proximity Graph based Maximum Inner Product Search  
4. \[[5](http://arxiv.org/abs/1809.08782)\] Norm-Ranging LSH for Maximum Inner Product Search  
5. \[[6](http://arxiv.org/abs/1410.5410)\] Improved Asymmetric Locality Sensitive Hashing (ALSH) for Maximum Inner Product Search  
6. \[[8](http://arxiv.org/abs/1509.01469)\] Quantization based Fast Inner Product Search  
7. \[[12](https://www.semanticscholar.org/paper/25454f456c514219c9d6eeb42200ebbf378db9ca)\] Norm Adjusted Proximity Graph for Fast Inner Product Retrieval  
8. \[[16](http://arxiv.org/abs/1506.03872)\] Diamond Sampling for Approximate Maximum All-Pairs Dot-Product (MAD) Search  
9. \[[17](https://www.semanticscholar.org/paper/d204d3848bb76ecca93a0674230303785b82c3b2)\] Simple Yet Efficient Algorithms for Maximum Inner Product Search via Extreme Order Statistics
