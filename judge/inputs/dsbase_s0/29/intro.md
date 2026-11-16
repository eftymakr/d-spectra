## Related Works

Maximum Inner Product Search (MIPS) has been a focal point in machine learning and information retrieval, particularly for high-dimensional data applications. Early approaches to MIPS primarily relied on inner product (IP) similarity, which, while intuitive, often led to issues with local optima and redundant computations \[[Tingyang Chen' 2025-03-10](http://arxiv.org/abs/2503.06882v2)\]. Additionally, some methods attempted to reduce the MIPS problem to the Nearest Neighbor Search (NNS) under the Euclidean metric by using space projections, which introduced topology distortion and information loss \[[Jie Liu' 2019-09-30](http://arxiv.org/abs/1909.13459v2)\]. Despite these divergent paradigms, recent research suggests that there is no inherent binary opposition between IP and Euclidean metrics. Instead, integrating both metrics in the design of indexing and search algorithms can significantly enhance MIPS performance \[[Ninh Pham' 2020-12-21](http://arxiv.org/abs/2012.11098v2)\].

The theoretical and empirical connections between IP and Euclidean metrics have been explored in several studies. For instance, the work by \[[Anshumali Shrivastava' 2014-05-22](http://arxiv.org/abs/1405.5869v1)\] introduced a method called ip-NSW, which leverages the norm bias in the MIPS problem to achieve an order of magnitude speedup over baseline methods. This approach aligns with the idea that different indexing and search strategies can offer distinct advantages depending on the underlying data topology \[[Ruiqi Guo' 2015-09-04](http://arxiv.org/abs/1509.01469v1)\]. Similarly, \[[Mo Tiwari' 2022-12-14](http://arxiv.org/abs/2212.07551v3)\] proposed ip-NSW+, an improvement over ip-NSW that incorporates an additional angular proximity graph to further enhance performance.

Graph-based search has emerged as a promising paradigm for MIPS, offering a balance between accuracy and efficiency. The work by \[[Alex Auvolat' 2015-07-21](http://arxiv.org/abs/1507.05910v3)\] introduced the concept of the inner-product navigable small world graph (ip-NSW), which enables efficient approximate MIPS by leveraging graph traversal. This approach has been further refined in \[[Yang Song' 2021-04-09](http://arxiv.org/abs/2104.04406v1)\], where the authors proposed ip-NSW+ to improve upon the original method by incorporating angular proximity information.

In addition to graph-based methods, several studies have explored the use of hashing techniques for MIPS. The Asymmetric LSH (ALSH) method \[[Chaoyang Wang' 2020-10-04](http://arxiv.org/abs/2010.07027v5)\] was the first to provide a provably sublinear time algorithm for approximate MIPS by transforming the problem into an approximate near neighbor search. This approach was later improved by \[[Sebastian Bruch' 2023-01-25](http://arxiv.org/abs/2301.10622v1)\], who introduced a new transformation that converts the problem into an approximate cosine similarity search, which can be efficiently solved using signed random projections.

Recent advancements have also focused on the integration of both IP and Euclidean metrics in indexing and search algorithms. The work by \[[Naoki Ono' 2023-10-31](http://arxiv.org/abs/2310.20419v1)\] proposed a novel graph-based index called the Metric-Amphibious Graph (MAG) and a corresponding search algorithm, Adaptive Navigation with Metric Switch (ANMS), which dynamically switches between IP and Euclidean metrics based on the data topology. This approach is grounded in the observation that different indexing and search strategies offer distinct advantages for MIPS, depending on the underlying data structure \[[Rui Liu' 2018-12-15](http://arxiv.org/abs/1812.06360v1)\].

To facilitate parameter tuning for optimal performance, \[[Qiang Huang' 2022-11-23](http://arxiv.org/abs/2211.12751v1)\] identified three statistical indicators that capture essential data topology properties and correlate strongly with parameter tuning. These indicators have been instrumental in improving the adaptability and scalability of MIPS algorithms.

### References

1. [Document 1]  
2. [Document 2]  
3. [Document 3]  
4. [Document 4]  
5. [Document 5]  
6. [Document 6]  
7. [Document 7]  
8. [Document 8]  
9. [Document 9]  
10. [Document 10]  
11. [Document 11]  
12. [Document 12]  
13. [Document 13]
