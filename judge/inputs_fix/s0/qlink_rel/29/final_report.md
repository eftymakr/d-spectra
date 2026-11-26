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
## Research papers
### Outline
- [Hashing and Approximate Search Techniques [10 papers]](#category-hashing-and-approximate-search-techniques)
- [MIPS Fundamentals and Challenges [2 papers]](#category-mips-fundamentals-and-challenges)
- [IP-Based MIPS Approaches [1 papers]](#category-ip-based-mips-approaches)
- [Graph-Based Indexing for MIPS [2 papers]](#category-graph-based-indexing-for-mips)
- [Quantization-Based MIPS Methods [2 papers]](#category-quantization-based-mips-methods)
- [Performance Evaluation and Benchmarks [1 papers]](#category-performance-evaluation-and-benchmarks)
- [Euclidean-Based MIPS Approaches [1 papers]](#category-euclidean-based-mips-approaches)

### <a id='category-hashing-and-approximate-search-techniques'></a>Hashing and Approximate Search Techniques: 10 papers found.
The category "Hashing and Approximate Search Techniques" encompasses several approaches to solving Maximum Inner Product Search (MIPS), which is critical for high-dimensional data applications. Early work introduced the first provably sublinear time algorithm for MIPS, leveraging asymmetric transformations to convert the problem into approximate near neighbor search, enabling efficient hashing schemes \[[1](http://arxiv.org/abs/1405.5869)\]. This idea was further refined with the development of the extended asymmetric LSH (ALSH) framework, which allows for more flexible and accurate hashing for MIPS \[[3](http://arxiv.org/abs/1909.13459)\]. Subsequent research, such as SIMPLE-LSH, improved practical performance but faced challenges with long-tailed distributions, prompting the introduction of NORM-RANGING LSH, which partitions datasets to reduce normalization errors and improve query efficiency \[[5](http://arxiv.org/abs/1809.08782)\]. Another approach, H2-ALSH, introduced a novel transformation and partitioning strategy to minimize distortion error and enhance search accuracy and efficiency \[[11](https://www.semanticscholar.org/paper/865488b467250ceb85bb59d35b8d4fb4f10ae421)\]. Additionally, alternative transformations have been proposed to convert MIPS into cosine similarity search, using signed random projections for improved theoretical guarantees and empirical performance \[[6](http://arxiv.org/abs/1410.5410)\]. Sampling-based methods, such as diamond sampling, have also been explored, offering significant speedups over brute-force computation by focusing on high-magnitude dot products \[[16](http://arxiv.org/abs/1506.03872)\]. Furthermore, dimensionality reduction techniques like CEOs and its variants have been developed, leveraging extreme order statistics to achieve sublinear time complexity with recall guarantees \[[17](https://www.semanticscholar.org/paper/d204d3848bb76ecca93a0674230303785b82c3b2)\]. These methods collectively highlight the ongoing efforts to improve the efficiency, accuracy, and adaptability of MIPS solutions through hashing and approximate search techniques.
|    | reference                                                                                                                                                                         | date     | key idea/summary                                                                                                                                                                                                                                                                                                     |
|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Asymmetric LSH (ALSH) for Sublinear Time Maximum Inner Product Search (MIPS)](http://arxiv.org/abs/1405.5869)                                                                    | 05/22/14 | The paper introduces the first provably sublinear time algorithm for approximate Maximum Inner Product Search (MIPS) using an extended Locality Sensitive Hashing (LSH) framework with asymmetric hashing schemes.                                                                                                   |
|  1 | [Norm-Ranging LSH for Maximum Inner Product Search](http://arxiv.org/abs/1809.08782)                                                                                              | 09/24/18 | NORM-RANGING LSH is a hashing-based algorithm that addresses the performance issues of SIMPLE-LSH by partitioning datasets into sub-datasets and building independent hash indexes, leading to lower query time complexity and improved efficiency in maximum inner product search.                                  |
|  2 | [Improved Asymmetric Locality Sensitive Hashing (ALSH) for Maximum Inner Product Search (MIPS)](http://arxiv.org/abs/1410.5410)                                                   | 10/20/14 | This work introduces a new asymmetric transformation that converts approximate Maximum Inner Product Search (MIPS) into approximate cosine similarity search, enabling efficient solutions using signed random projections, and demonstrates its superiority over previous methods theoretically and experimentally. |
|  3 | [Accurate and Fast Asymmetric Locality-Sensitive Hashing Scheme for Maximum Inner Product Search](https://www.semanticscholar.org/paper/865488b467250ceb85bb59d35b8d4fb4f10ae421) | 07/19/18 | The paper proposes H2-ALSH, a novel Asymmetric LSH scheme for high-dimensional AMIP search, which reduces distortion error and improves search efficiency and accuracy through QNF transformation and homocentric hypersphere partition.                                                                             |
|  4 | [Clustering is Efficient for Approximate Maximum Inner Product Search](https://www.semanticscholar.org/paper/a2e2970dd99b86fd6198c0b756c6cd4d52e34c3b)                            | 07/21/15 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                                            |
|  5 | [A Fast Sampling Algorithm for Maximum Inner Product Search](https://www.semanticscholar.org/paper/8031edc543ca23c9e2b18244feb09558f43897ed)                                      | 04/11/19 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                                            |
|  6 | [Exact and Approximate Maximum Inner Product Search with LEMP](https://www.semanticscholar.org/paper/f2e1ebb12cc3e72a87766442b6f81bd3e58b3bab)                                    | 12/03/16 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                                            |
|  7 | [Diamond Sampling for Approximate Maximum All-Pairs Dot-Product (MAD) Search](http://arxiv.org/abs/1506.03872)                                                                    | 06/11/15 | The paper introduces a sampling-based approach called diamond sampling to efficiently find the top-t dot products between two sets of vectors, significantly improving speed and performance compared to direct computation and existing methods.                                                                    |
|  8 | [Simple Yet Efficient Algorithms for Maximum Inner Product Search via Extreme Order Statistics](https://www.semanticscholar.org/paper/d204d3848bb76ecca93a0674230303785b82c3b2)   | 08/14/21 | CEOS is a novel dimensionality reduction method for approximate maximum inner product search (MIPS) that provides a sublinear algorithm with search recall guarantees, achieving significant speedup over brute-force search on large-scale datasets.                                                                |
|  9 | [Scalable and Sustainable Deep Learning via Randomized Hashing](http://arxiv.org/abs/1602.08194)                                                                                  | 02/26/16 | The paper introduces a novel hashing-based technique to reduce computational costs in deep learning by using sparse gradient updates and efficient node selection, achieving 5% of the original computation with minimal accuracy loss.                                                                              |
### <a id='category-mips-fundamentals-and-challenges'></a>MIPS Fundamentals and Challenges: 2 papers found.
Context: 
	Document 1: [Snippet]: «Maximum Inner Product Search (MIPS) is an important task in many machine learning applications such as the prediction phase of a low-rank matrix factorization model for a recommender system. There have been some works on how to perform MIPS in sub-linear time recently. However, most of them do not have the flexibility to control the trade-off between search efficient and search quality. In this paper, we study the MIPS problem with a computational budget. By carefully studying the problem structure of MIPS, we develop a novel Greedy-MIPS algorithm, which can handle budgeted MIPS by design. While simple and intuitive, Greedy-MIPS yields surprisingly superior performance compared to state-of-the-art approaches. As a specific example, on a candidate set containing half a million vectors of dimension 200, Greedy-MIPS runs 200x faster than the naive approach while yielding search results with the top-5 precision greater than 75\%.»
[_citation_number]: «2»
[Category]: «MIPS Fundamentals and Challenges»

	Document 2: [Snippet]: «The problem of efficiently finding the best match for a query in a given set with respect to the Euclidean distance or the cosine similarity has been extensively studied. However, the closely related problem of efficiently finding the best match with respect to the inner-product has never been explored in the general setting to the best of our knowledge. In this paper we consider this problem and contrast it with the previous problems considered. First, we propose a general branch-and-bound algorithm based on a (single) tree data structure. Subsequently, we present a dual-tree algorithm for the case where there are multiple queries. Our proposed branch-and-bound algorithms are based on novel inner-product bounds. Finally we present a new data structure, the cone tree, for increasing the efficiency of the dual-tree algorithm. We evaluate our proposed algorithms on a variety of data sets from various applications, and exhibit up to five orders of magnitude improvement in query time over the naive search technique in some cases.»
[_citation_number]: «4»
[Category]: «MIPS Fundamentals and Challenges»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-21T05:01:58+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1909.13459)\]. Further details \[[6](http://arxiv.org/abs/1410.5410)\]\[[7](https://www.semanticscholar.org/paper/f2171bc79fb72693f60c8e6b0dd547f7d4f850ac)\]\[[8](http://arxiv.org/abs/1509.01469)\]\[[9](https://www.semanticscholar.org/paper/0b2790c2c1e23e5535421696e1ec763bbc651bbd)\]\[[10](https://www.semanticscholar.org/paper/d8aad5d9c2c336c550ca9621b73c7688f184d50b)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Maximum Inner Product Search (MIPS) is a fundamental challenge in machine
learning and information retrieval, particularly in high-dimensional data
applications. Existing approaches to MIPS either rely solely on Inner Product
(IP) similarity, which faces issues with local optima and redundant
computations, or reduce the MIPS problem to the Nearest Neighbor Search under
the Euclidean metric via space projection, leading to topology destruction and
information loss. Despite the divergence of the two paradigms, we argue that
there is no inherent binary opposition between IP and Euclidean metrics. By
stitching IP and Euclidean in the design of indexing and search algorithms, we
can significantly enhance MIPS performance. Specifically, this paper explores
the theoretical and empirical connections between these two metrics from the
MIPS perspective. Our investigation, grounded in graph-based search, reveals
that different indexing and search strategies offer distinct advantages for
MIPS, depending on the underlying data topology. Building on these insights, we
introduce a novel graph-based index called Metric-Amphibious Graph (MAG) and a
corresponding search algorithm, Adaptive Navigation with Metric Switch (ANMS).
To facilitate parameter tuning for optimal performance, we identify three
statistical indicators that capture essential data topology properties and
correlate strongly with parameter tuning. Extensive experiments on 12
real-world datasets demonstrate that MAG outperforms existing state-of-the-art
methods, achieving up to 4x search speedup while maintaining adaptability and
scalability.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1909.13459)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1610.03317)\]\[[7](https://www.semanticscholar.org/paper/f2171bc79fb72693f60c8e6b0dd547f7d4f850ac)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
The MIPS problem has been a focus of recent research due to its critical role in high-dimensional machine learning applications, such as recommender systems \[[1](http://arxiv.org/abs/1405.5869)\]. Existing approaches often face challenges in balancing search efficiency and quality, with some methods relying solely on inner product similarity, which can lead to local optima and redundant computations \[[2](http://arxiv.org/abs/1610.03317)\], or reducing MIPS to Euclidean nearest neighbor search, which may distort data topology and cause information loss \[[3](http://arxiv.org/abs/1909.13459)\]. Several studies have attempted to address these limitations by proposing novel algorithms, such as branch-and-bound methods based on tree structures and dual-tree algorithms for multiple queries \[[4](http://arxiv.org/abs/1202.6101)\]. These approaches introduce inner-product bounds and data structures like the cone tree to improve query efficiency, achieving up to five orders of magnitude speedup over naive search techniques in certain scenarios \[[4](http://arxiv.org/abs/1202.6101)\]. However, the integration of inner product and Euclidean metrics remains underexplored, despite their potential to enhance MIPS performance through hybrid indexing and search strategies \[[1](http://arxiv.org/abs/1405.5869)\]. The development of methods that can dynamically switch between metrics based on data topology, such as the Metric-Amphibious Graph (MAG) and Adaptive Navigation with Metric Switch (ANMS), represents a significant advancement in this area \[[1](http://arxiv.org/abs/1405.5869)\].
|    | reference                                                                                      | date     | key idea/summary                                                                                                                                                                                                                                                            |
|----|------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [A Greedy Approach for Budgeted Maximum Inner Product Search](http://arxiv.org/abs/1610.03317) | 10/11/16 | The paper introduces a novel Greedy-MIPS algorithm that efficiently solves the Maximum Inner Product Search problem with a computational budget, achieving superior performance compared to existing methods.                                                               |
|  1 | [Maximum inner-product search using cone trees](http://arxiv.org/abs/1202.6101)                | 02/28/12 | The paper introduces algorithms for efficiently finding the best match with respect to the inner-product, proposing a branch-and-bound approach and a dual-tree algorithm with a new data structure called the cone tree, achieving significant improvements in query time. |
### <a id='category-ip-based-mips-approaches'></a>IP-Based MIPS Approaches: 1 papers found.
Context: 
	Document 1: [Snippet]: «The inner-product navigable small world graph (ip-NSW) represents the state-of-the-art method for approximate maximum inner product search (MIPS) and it can achieve an order of magnitude speedup over the fastest baseline. However, to date it is still unclear where its exceptional performance comes from. In this paper, we show that there is a strong norm bias in the MIPS problem, which means that the large norm items are very likely to become the result of MIPS. Then we explain the good performance of ip-NSW as matching the norm bias of the MIPS problem — large norm items have big in-degrees in the ip-NSW proximity graph and a walk on the graph spends the majority of computation on these items, thus effectively avoids unnecessary computation on small norm items. Furthermore, we propose the ip-NSW+ algorithm, which improves ip-NSW by introducing an additional angular proximity graph. Search is first conducted on the angular graph to find the angular neighbors of a query and then the MIPS neighbors of these angular neighbors are used to initialize the candidate pool for search on the inner-product proximity graph. Experiment results show that ip-NSW+ consistently and significantly outperforms ip-NSW and provides more robust performance under different data distributions.»
[_citation_number]: «3»
[Category]: «IP-Based MIPS Approaches»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-21T05:01:58+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1909.13459)\]. Further details \[[6](http://arxiv.org/abs/1410.5410)\]\[[7](https://www.semanticscholar.org/paper/f2171bc79fb72693f60c8e6b0dd547f7d4f850ac)\]\[[8](http://arxiv.org/abs/1509.01469)\]\[[9](https://www.semanticscholar.org/paper/0b2790c2c1e23e5535421696e1ec763bbc651bbd)\]\[[10](https://www.semanticscholar.org/paper/d8aad5d9c2c336c550ca9621b73c7688f184d50b)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Maximum Inner Product Search (MIPS) is a fundamental challenge in machine
learning and information retrieval, particularly in high-dimensional data
applications. Existing approaches to MIPS either rely solely on Inner Product
(IP) similarity, which faces issues with local optima and redundant
computations, or reduce the MIPS problem to the Nearest Neighbor Search under
the Euclidean metric via space projection, leading to topology destruction and
information loss. Despite the divergence of the two paradigms, we argue that
there is no inherent binary opposition between IP and Euclidean metrics. By
stitching IP and Euclidean in the design of indexing and search algorithms, we
can significantly enhance MIPS performance. Specifically, this paper explores
the theoretical and empirical connections between these two metrics from the
MIPS perspective. Our investigation, grounded in graph-based search, reveals
that different indexing and search strategies offer distinct advantages for
MIPS, depending on the underlying data topology. Building on these insights, we
introduce a novel graph-based index called Metric-Amphibious Graph (MAG) and a
corresponding search algorithm, Adaptive Navigation with Metric Switch (ANMS).
To facilitate parameter tuning for optimal performance, we identify three
statistical indicators that capture essential data topology properties and
correlate strongly with parameter tuning. Extensive experiments on 12
real-world datasets demonstrate that MAG outperforms existing state-of-the-art
methods, achieving up to 4x search speedup while maintaining adaptability and
scalability.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1909.13459)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1610.03317)\]\[[7](https://www.semanticscholar.org/paper/f2171bc79fb72693f60c8e6b0dd547f7d4f850ac)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer:  
IP-based approaches for Maximum Inner Product Search (MIPS) have gained significant attention due to their effectiveness in high-dimensional data applications. One such method is the inner-product navigable small world graph (ip-NSW), which has been identified as a state-of-the-art technique for approximate MIPS \[[3](http://arxiv.org/abs/1909.13459)\]. This approach leverages a navigable small-world graph structure to achieve a substantial speedup over existing baselines, often by an order of magnitude. The performance of ip-NSW is attributed to its ability to align with the norm bias inherent in the MIPS problem, where items with larger norms are more likely to be relevant search results \[[3](http://arxiv.org/abs/1909.13459)\]. This alignment is achieved by ensuring that large norm items have high in-degrees in the proximity graph, allowing the search process to focus computational resources on these items and avoid unnecessary computations on smaller norm items \[[3](http://arxiv.org/abs/1909.13459)\]. To further enhance performance, the ip-NSW+ algorithm was introduced, which integrates an additional angular proximity graph to refine the search process by first identifying angular neighbors and then using these to initialize the candidate pool for inner-product search \[[3](http://arxiv.org/abs/1909.13459)\]. These developments highlight the ongoing efforts to optimize MIPS through graph-based methods that account for both norm and angular similarities.
|    | reference                                                                                                         | date     | key idea/summary                                                                                                                                                                                                                     |
|----|-------------------------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Understanding and Improving Proximity Graph based Maximum Inner Product Search](http://arxiv.org/abs/1909.13459) | 09/30/19 | The paper introduces ip-NSW+, an improved version of the ip-NSW algorithm for approximate maximum inner product search, which leverages angular proximity to enhance performance and robustness across different data distributions. |
### <a id='category-graph-based-indexing-for-mips'></a>Graph-Based Indexing for MIPS: 2 papers found.
Context: 
	Document 1: [Snippet]: «»
[_citation_number]: «7»
[Category]: «Graph-Based Indexing for MIPS»

	Document 2: [Snippet]: «Efficient inner product search on embedding vectors is often the vital stage for online ranking services, such as recommendation and information retrieval. Recommendation algorithms, e.g., matrix factorization, typically produce latent vectors to represent users or items. The recommendation services are conducted by retrieving the most relevant item vectors given the user vector, where the relevance is often defined by inner product. Therefore, developing efficient recommender systems often requires solving the so-called maximum inner product search (MIPS) problem. In the past decade, there have been many studies on efficient MIPS algorithms. This task is challenging in part because the inner product does not follow the triangle inequality of metric space. Compared with hash-based or quantization-based MIPS solutions, in recent years graph-based MIPS algorithms have demonstrated their strong empirical advantages in many real-world MIPS tasks. In this paper, we propose a new index graph construction method named norm adjusted proximity graph (NAPG), for efficient MIPS. With adjusting factors estimated on sampled data, NAPG is able to select more meaningful data points to connect with when constructing graph-based index for inner product search. Our extensive experiments on a variety of datasets verify that the improved graph-based index strategy provides another strong addition to the pool of efficient MIPS algorithms.»
[_citation_number]: «12»
[Category]: «Graph-Based Indexing for MIPS»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-21T05:01:58+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1909.13459)\]. Further details \[[6](http://arxiv.org/abs/1410.5410)\]\[[7](https://www.semanticscholar.org/paper/f2171bc79fb72693f60c8e6b0dd547f7d4f850ac)\]\[[8](http://arxiv.org/abs/1509.01469)\]\[[9](https://www.semanticscholar.org/paper/0b2790c2c1e23e5535421696e1ec763bbc651bbd)\]\[[10](https://www.semanticscholar.org/paper/d8aad5d9c2c336c550ca9621b73c7688f184d50b)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Maximum Inner Product Search (MIPS) is a fundamental challenge in machine
learning and information retrieval, particularly in high-dimensional data
applications. Existing approaches to MIPS either rely solely on Inner Product
(IP) similarity, which faces issues with local optima and redundant
computations, or reduce the MIPS problem to the Nearest Neighbor Search under
the Euclidean metric via space projection, leading to topology destruction and
information loss. Despite the divergence of the two paradigms, we argue that
there is no inherent binary opposition between IP and Euclidean metrics. By
stitching IP and Euclidean in the design of indexing and search algorithms, we
can significantly enhance MIPS performance. Specifically, this paper explores
the theoretical and empirical connections between these two metrics from the
MIPS perspective. Our investigation, grounded in graph-based search, reveals
that different indexing and search strategies offer distinct advantages for
MIPS, depending on the underlying data topology. Building on these insights, we
introduce a novel graph-based index called Metric-Amphibious Graph (MAG) and a
corresponding search algorithm, Adaptive Navigation with Metric Switch (ANMS).
To facilitate parameter tuning for optimal performance, we identify three
statistical indicators that capture essential data topology properties and
correlate strongly with parameter tuning. Extensive experiments on 12
real-world datasets demonstrate that MAG outperforms existing state-of-the-art
methods, achieving up to 4x search speedup while maintaining adaptability and
scalability.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1909.13459)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1610.03317)\]\[[7](https://www.semanticscholar.org/paper/f2171bc79fb72693f60c8e6b0dd547f7d4f850ac)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Graph-based indexing has emerged as a promising approach for solving the Maximum Inner Product Search (MIPS) problem, particularly in high-dimensional data applications \[[12](https://www.semanticscholar.org/paper/25454f456c514219c9d6eeb42200ebbf378db9ca)\]. Unlike hash-based or quantization-based methods, graph-based algorithms maintain the structural relationships between data points, which is crucial for inner product search \[[12](https://www.semanticscholar.org/paper/25454f456c514219c9d6eeb42200ebbf378db9ca)\]. The construction of graph-based indexes, such as the norm adjusted proximity graph (NAPG), involves selecting meaningful data points based on adjusting factors estimated from sampled data, leading to more efficient and accurate search results \[[12](https://www.semanticscholar.org/paper/25454f456c514219c9d6eeb42200ebbf378db9ca)\]. These methods have demonstrated strong empirical advantages in real-world tasks, such as recommendation systems and information retrieval, where inner product similarity is vital for ranking \[[12](https://www.semanticscholar.org/paper/25454f456c514219c9d6eeb42200ebbf378db9ca)\]. The success of graph-based indexing lies in its ability to adapt to the underlying data topology, offering distinct advantages over traditional approaches that either rely solely on inner product similarity or reduce the problem to Euclidean nearest neighbor search \[[12](https://www.semanticscholar.org/paper/25454f456c514219c9d6eeb42200ebbf378db9ca)\]. This category of work highlights the potential of graph-based indexing to enhance MIPS performance by leveraging the inherent structure of the data \[[12](https://www.semanticscholar.org/paper/25454f456c514219c9d6eeb42200ebbf378db9ca)\].
|    | reference                                                                                                                                        | date     | key idea/summary                                                                                                                                                                                                                                                                             |
|----|--------------------------------------------------------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Non-metric Similarity Graphs for Maximum Inner Product Search](https://www.semanticscholar.org/paper/f2171bc79fb72693f60c8e6b0dd547f7d4f850ac)  | nan      | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                    |
|  1 | [Norm Adjusted Proximity Graph for Fast Inner Product Retrieval](https://www.semanticscholar.org/paper/25454f456c514219c9d6eeb42200ebbf378db9ca) | 08/14/21 | The paper introduces a new graph-based index construction method called norm adjusted proximity graph (NAPG) for efficient maximum inner product search (MIPS), which improves the performance of recommendation systems by selecting more meaningful data points during graph construction. |
### <a id='category-quantization-based-mips-methods'></a>Quantization-Based MIPS Methods: 2 papers found.
Context: 
	Document 1: [Snippet]: «We propose a quantization based approach for fast approximate Maximum Inner Product Search (MIPS). Each database vector is quantized in multiple subspaces via a set of codebooks, learned directly by minimizing the inner product quantization error. Then, the inner product of a query to a database vector is approximated as the sum of inner products with the subspace quantizers. Different from recently proposed LSH approaches to MIPS, the database vectors and queries do not need to be augmented in a higher dimensional feature space. We also provide a theoretical analysis of the proposed approach, consisting of the concentration results under mild assumptions. Furthermore, if a small sample of example queries is given at the training time, we propose a modified codebook learning procedure which further improves the accuracy. Experimental results on a variety of datasets including those arising from deep neural networks show that the proposed approach significantly outperforms the existing state-of-the-art.»
[_citation_number]: «8»
[Category]: «Quantization-Based MIPS Methods»

	Document 2: [Snippet]: «This paper introduces a product quantization-based approach for approximate nearest neighbor search. The idea is to decompose the space into a Cartesian product of low-dimensional subspaces and to quantize each subspace separately. A vector is represented by a short code composed of its subspace quantization indices. The euclidean distance between two vectors can be efficiently estimated from their codes. An asymmetric version increases precision, as it computes the approximate distance between a vector and a code. Experimental results show that our approach searches for nearest neighbors efficiently, in particular in combination with an inverted file system. Results for SIFT and GIST image descriptors show excellent search accuracy, outperforming three state-of-the-art approaches. The scalability of our approach is validated on a data set of two billion vectors.»
[_citation_number]: «19»
[Category]: «Quantization-Based MIPS Methods»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-21T05:01:58+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1909.13459)\]. Further details \[[6](http://arxiv.org/abs/1410.5410)\]\[[7](https://www.semanticscholar.org/paper/f2171bc79fb72693f60c8e6b0dd547f7d4f850ac)\]\[[8](http://arxiv.org/abs/1509.01469)\]\[[9](https://www.semanticscholar.org/paper/0b2790c2c1e23e5535421696e1ec763bbc651bbd)\]\[[10](https://www.semanticscholar.org/paper/d8aad5d9c2c336c550ca9621b73c7688f184d50b)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Maximum Inner Product Search (MIPS) is a fundamental challenge in machine
learning and information retrieval, particularly in high-dimensional data
applications. Existing approaches to MIPS either rely solely on Inner Product
(IP) similarity, which faces issues with local optima and redundant
computations, or reduce the MIPS problem to the Nearest Neighbor Search under
the Euclidean metric via space projection, leading to topology destruction and
information loss. Despite the divergence of the two paradigms, we argue that
there is no inherent binary opposition between IP and Euclidean metrics. By
stitching IP and Euclidean in the design of indexing and search algorithms, we
can significantly enhance MIPS performance. Specifically, this paper explores
the theoretical and empirical connections between these two metrics from the
MIPS perspective. Our investigation, grounded in graph-based search, reveals
that different indexing and search strategies offer distinct advantages for
MIPS, depending on the underlying data topology. Building on these insights, we
introduce a novel graph-based index called Metric-Amphibious Graph (MAG) and a
corresponding search algorithm, Adaptive Navigation with Metric Switch (ANMS).
To facilitate parameter tuning for optimal performance, we identify three
statistical indicators that capture essential data topology properties and
correlate strongly with parameter tuning. Extensive experiments on 12
real-world datasets demonstrate that MAG outperforms existing state-of-the-art
methods, achieving up to 4x search speedup while maintaining adaptability and
scalability.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1909.13459)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1610.03317)\]\[[7](https://www.semanticscholar.org/paper/f2171bc79fb72693f60c8e6b0dd547f7d4f850ac)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Quantization-based methods have emerged as a promising approach for efficient Maximum Inner Product Search (MIPS). These methods typically involve decomposing high-dimensional vectors into multiple subspaces and quantizing each subspace independently, allowing for faster approximate inner product computation \[[8](http://arxiv.org/abs/1509.01469)\]. For example, one approach quantizes database vectors into multiple subspaces using codebooks, which are learned by minimizing the inner product quantization error. This enables the inner product between a query and a database vector to be approximated as the sum of inner products with the subspace quantizers, avoiding the need for augmenting vectors into higher-dimensional spaces as seen in some LSH-based approaches \[[8](http://arxiv.org/abs/1509.01469)\]. Another method, product quantization, decomposes the space into a Cartesian product of low-dimensional subspaces, quantizing each separately to form a compact code for efficient distance estimation \[[19](https://www.semanticscholar.org/paper/4748d22348e72e6e06c2476486afddbc76e5eca7)\]. These techniques demonstrate significant improvements in search efficiency and accuracy, particularly when combined with inverted file systems or used on large-scale datasets \[[19](https://www.semanticscholar.org/paper/4748d22348e72e6e06c2476486afddbc76e5eca7)\]. Both approaches highlight the potential of quantization to balance computational efficiency with search accuracy in MIPS, offering alternatives to traditional methods that rely solely on IP similarity or Euclidean metrics \[[8](http://arxiv.org/abs/1509.01469)\].
|    | reference                                                                                                                          | date     | key idea/summary                                                                                                                                                                                                                                           |
|----|------------------------------------------------------------------------------------------------------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Quantization based Fast Inner Product Search](http://arxiv.org/abs/1509.01469)                                                    | 09/04/15 | The paper proposes a quantization-based approach for fast approximate Maximum Inner Product Search (MIPS) that avoids the need for augmenting vectors in a higher-dimensional space, achieving significant performance improvements over existing methods. |
|  1 | [Product Quantization for Nearest Neighbor Search](https://www.semanticscholar.org/paper/4748d22348e72e6e06c2476486afddbc76e5eca7) | nan      | This paper introduces a product quantization-based approach for efficient approximate nearest neighbor search, achieving high accuracy and scalability, particularly for large datasets like two billion vectors.                                          |
### <a id='category-performance-evaluation-and-benchmarks'></a>Performance Evaluation and Benchmarks: 1 papers found.
Context: 
	Document 1: [Snippet]: «Exact Maximum Inner Product Search (MIPS) is an important task that is widely pertinent to recommender systems and high-dimensional similarity search. The brute-force approach to solving exact MIPS is computationally expensive, thus spurring recent development of novel indexes and pruning techniques for this task. In this paper we show that a hardware-efficient brute-force approach, blocked matrix multiply (BMM), can outperform the state-of-the-art MIPS solvers by over an order of magnitude, for some—but not all—inputs. In this paper we also present a novel MIPS solution, MAX-IMUS, that takes advantage of hardware efficiency and pruning of the search space. Like BMM, MAXIMUS is faster than other solvers by up to an order of magnitude, but again only for some inputs. Since no single solution offers the best runtime performance for all inputs, we introduce a new data-dependent optimizer, OPTIMUS, that selects online with minimal overhead the best MIPS solver for a given input. Together, OPTIMUS and MAXIMUS outperform state-of-the-art MIPS solvers by 3.2× on average, and up to 10.9×, on widely studied MIPS datasets.»
[_citation_number]: «9»
[Category]: «Performance Evaluation and Benchmarks»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-21T05:01:58+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1909.13459)\]. Further details \[[6](http://arxiv.org/abs/1410.5410)\]\[[7](https://www.semanticscholar.org/paper/f2171bc79fb72693f60c8e6b0dd547f7d4f850ac)\]\[[8](http://arxiv.org/abs/1509.01469)\]\[[9](https://www.semanticscholar.org/paper/0b2790c2c1e23e5535421696e1ec763bbc651bbd)\]\[[10](https://www.semanticscholar.org/paper/d8aad5d9c2c336c550ca9621b73c7688f184d50b)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Maximum Inner Product Search (MIPS) is a fundamental challenge in machine
learning and information retrieval, particularly in high-dimensional data
applications. Existing approaches to MIPS either rely solely on Inner Product
(IP) similarity, which faces issues with local optima and redundant
computations, or reduce the MIPS problem to the Nearest Neighbor Search under
the Euclidean metric via space projection, leading to topology destruction and
information loss. Despite the divergence of the two paradigms, we argue that
there is no inherent binary opposition between IP and Euclidean metrics. By
stitching IP and Euclidean in the design of indexing and search algorithms, we
can significantly enhance MIPS performance. Specifically, this paper explores
the theoretical and empirical connections between these two metrics from the
MIPS perspective. Our investigation, grounded in graph-based search, reveals
that different indexing and search strategies offer distinct advantages for
MIPS, depending on the underlying data topology. Building on these insights, we
introduce a novel graph-based index called Metric-Amphibious Graph (MAG) and a
corresponding search algorithm, Adaptive Navigation with Metric Switch (ANMS).
To facilitate parameter tuning for optimal performance, we identify three
statistical indicators that capture essential data topology properties and
correlate strongly with parameter tuning. Extensive experiments on 12
real-world datasets demonstrate that MAG outperforms existing state-of-the-art
methods, achieving up to 4x search speedup while maintaining adaptability and
scalability.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1909.13459)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1610.03317)\]\[[7](https://www.semanticscholar.org/paper/f2171bc79fb72693f60c8e6b0dd547f7d4f850ac)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Recent advancements in Maximum Inner Product Search (MIPS) have focused on improving computational efficiency and accuracy, particularly in high-dimensional data applications \[[9](https://www.semanticscholar.org/paper/0b2790c2c1e23e5535421696e1ec763bbc651bbd)\]. While brute-force methods are computationally expensive, recent work has introduced hardware-efficient approaches like blocked matrix multiply (BMM), which can outperform state-of-the-art solvers by over an order of magnitude for certain inputs \[[9](https://www.semanticscholar.org/paper/0b2790c2c1e23e5535421696e1ec763bbc651bbd)\]. Similarly, novel solutions such as MAX-IMUS leverage hardware efficiency and pruning techniques to achieve comparable speedups \[[9](https://www.semanticscholar.org/paper/0b2790c2c1e23e5535421696e1ec763bbc651bbd)\]. These developments highlight the importance of optimizing both algorithmic design and hardware utilization to address the challenges of MIPS. Furthermore, the introduction of data-dependent optimizers like OPTIMUS enables adaptive selection of the most suitable solver for a given input, further enhancing performance \[[9](https://www.semanticscholar.org/paper/0b2790c2c1e23e5535421696e1ec763bbc651bbd)\]. These findings underscore the ongoing efforts to balance computational efficiency with search accuracy in MIPS, paving the way for more scalable and adaptable solutions.
|    | reference                                                                                                                                                 | date     | key idea/summary                                                                                                                                                                                             |
|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [To Index or Not to Index: Optimizing Exact Maximum Inner Product Search](https://www.semanticscholar.org/paper/0b2790c2c1e23e5535421696e1ec763bbc651bbd) | 06/05/17 | The paper introduces MAXIMUS and OPTIMUS, which together outperform state-of-the-art MIPS solvers by up to 10.9× on widely studied datasets, leveraging hardware efficiency and data-dependent optimization. |
### <a id='category-euclidean-based-mips-approaches'></a>Euclidean-Based MIPS Approaches: 1 papers found.
Context: 
	Document 1: [Snippet]: «»
[_citation_number]: «10»
[Category]: «Euclidean-Based MIPS Approaches»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-21T05:01:58+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1909.13459)\]. Further details \[[6](http://arxiv.org/abs/1410.5410)\]\[[7](https://www.semanticscholar.org/paper/f2171bc79fb72693f60c8e6b0dd547f7d4f850ac)\]\[[8](http://arxiv.org/abs/1509.01469)\]\[[9](https://www.semanticscholar.org/paper/0b2790c2c1e23e5535421696e1ec763bbc651bbd)\]\[[10](https://www.semanticscholar.org/paper/d8aad5d9c2c336c550ca9621b73c7688f184d50b)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Maximum Inner Product Search (MIPS) is a fundamental challenge in machine
learning and information retrieval, particularly in high-dimensional data
applications. Existing approaches to MIPS either rely solely on Inner Product
(IP) similarity, which faces issues with local optima and redundant
computations, or reduce the MIPS problem to the Nearest Neighbor Search under
the Euclidean metric via space projection, leading to topology destruction and
information loss. Despite the divergence of the two paradigms, we argue that
there is no inherent binary opposition between IP and Euclidean metrics. By
stitching IP and Euclidean in the design of indexing and search algorithms, we
can significantly enhance MIPS performance. Specifically, this paper explores
the theoretical and empirical connections between these two metrics from the
MIPS perspective. Our investigation, grounded in graph-based search, reveals
that different indexing and search strategies offer distinct advantages for
MIPS, depending on the underlying data topology. Building on these insights, we
introduce a novel graph-based index called Metric-Amphibious Graph (MAG) and a
corresponding search algorithm, Adaptive Navigation with Metric Switch (ANMS).
To facilitate parameter tuning for optimal performance, we identify three
statistical indicators that capture essential data topology properties and
correlate strongly with parameter tuning. Extensive experiments on 12
real-world datasets demonstrate that MAG outperforms existing state-of-the-art
methods, achieving up to 4x search speedup while maintaining adaptability and
scalability.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1909.13459)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1610.03317)\]\[[7](https://www.semanticscholar.org/paper/f2171bc79fb72693f60c8e6b0dd547f7d4f850ac)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Euclidean-based MIPS approaches typically transform the problem into a nearest neighbor search under the Euclidean metric, often through space projection techniques \[[10](https://www.semanticscholar.org/paper/d8aad5d9c2c336c550ca9621b73c7688f184d50b)\]. This method aims to leverage the computational efficiency of Euclidean distance calculations while maintaining the relevance of inner product similarity. However, such transformations can lead to topology destruction and information loss, as the original data structure may not be preserved \[[10](https://www.semanticscholar.org/paper/d8aad5d9c2c336c550ca9621b73c7688f184d50b)\]. These approaches are often contrasted with IP-based methods, which directly compute inner product similarity but may suffer from local optima and redundant computations \[[10](https://www.semanticscholar.org/paper/d8aad5d9c2c336c550ca9621b73c7688f184d50b)\]. Despite these differences, recent research suggests that there is no inherent binary opposition between IP and Euclidean metrics, and integrating both can enhance MIPS performance \[[10](https://www.semanticscholar.org/paper/d8aad5d9c2c336c550ca9621b73c7688f184d50b)\].
|    | reference                                                                                                                                                                           | date     | key idea/summary                                                                                          |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------|
|  0 | [Speeding up the Xbox recommender system using a euclidean transformation for inner-product spaces](https://www.semanticscholar.org/paper/d8aad5d9c2c336c550ca9621b73c7688f184d50b) | 10/06/14 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
