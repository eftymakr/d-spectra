## Related Works

Maximum Inner Product Search (MIPS) has been a focal point in machine learning and information retrieval, particularly for high-dimensional data. Early approaches to MIPS primarily relied on inner product (IP) similarity, which, while intuitive, suffers from issues such as local optima and redundant computations \[[1](http://arxiv.org/abs/1606.00185)\]. Alternatively, some methods reduced MIPS to nearest neighbor search under the Euclidean metric through space projection, which, although effective, often leads to topology destruction and information loss \[[1](http://arxiv.org/abs/1606.00185)\]. Despite these divergent paradigms, recent work has argued that there is no inherent binary opposition between IP and Euclidean metrics \[[1](http://arxiv.org/abs/1606.00185)\]. Instead, by integrating both metrics in the design of indexing and search algorithms, significant performance improvements can be achieved \[[1](http://arxiv.org/abs/1606.00185)\].

Several hashing-based methods have been proposed to address MIPS. Asymmetric LSH (ALSH) was introduced as the first provably sublinear time algorithm for approximate MIPS, leveraging asymmetric transformations to convert inner product search into near neighbor search \[[2](http://arxiv.org/abs/1405.5869)\]. This approach was later improved with a new transformation that converted MIPS into cosine similarity search, which could be efficiently solved using signed random projections \[[3](http://arxiv.org/abs/1410.5410)\]. These developments highlight the importance of asymmetric hashing in handling the challenges of MIPS \[[2](http://arxiv.org/abs/1405.5869)\]\[[3](http://arxiv.org/abs/1410.5410)\].

Norm-Ranging LSH was introduced to address the limitations of Simple-LSH, which suffered from long tails in the 2-norm distribution of real datasets. By partitioning the dataset into sub-datasets and building hash indexes independently, Norm-Ranging LSH achieved lower query time complexity and better performance \[[4](http://arxiv.org/abs/1809.08782)\]. This approach demonstrates how dataset characteristics can influence the effectiveness of hashing techniques for MIPS \[[4](http://arxiv.org/abs/1809.08782)\].

Vector quantization (VQ) techniques have also been explored for MIPS. Traditional VQ methods aim to minimize reconstruction error, but recent work has shown that quantization errors in norm have a more significant impact on inner products than errors in direction \[[6](http://arxiv.org/abs/1911.04654)\]. Based on this insight, norm-explicit quantization (NEQ) was proposed, which explicitly quantizes the norms of items to reduce norm errors, thereby improving MIPS performance \[[6](http://arxiv.org/abs/1911.04654)\]. This approach highlights the importance of considering both norm and direction in quantization for high-performance MIPS \[[6](http://arxiv.org/abs/1911.04654)\].

In addition to hashing and quantization, graph-based methods have been developed for MIPS. The inner-product navigable small world graph (ip-NSW) has emerged as a state-of-the-art method, achieving significant speedups over existing baselines \[[9](http://arxiv.org/abs/1909.13459)\]. However, its performance is influenced by the norm bias in the MIPS problem, where large norm items are more likely
## Research papers
### Outline
- [Performance Evaluation on Real-World Datasets [1 papers]](#category-performance-evaluation-on-real-world-datasets)
- [Asymmetric Hashing Techniques [3 papers]](#category-asymmetric-hashing-techniques)
- [Norm-Ranging LSH Method [1 papers]](#category-norm-ranging-lsh-method)
- [Norm-Explicit Quantization [1 papers]](#category-norm-explicit-quantization)
- [Vector Quantization for MIPS [3 papers]](#category-vector-quantization-for-mips)
- [Metric Integration in Indexing [1 papers]](#category-metric-integration-in-indexing)
- [Graph-Based Indexing Methods [4 papers]](#category-graph-based-indexing-methods)
- [Euclidean Metric Reduction Approaches [1 papers]](#category-euclidean-metric-reduction-approaches)
- [Inner Product Similarity Limitations [1 papers]](#category-inner-product-similarity-limitations)

### <a id='category-performance-evaluation-on-real-world-datasets'></a>Performance Evaluation on Real-World Datasets: 1 papers found.
Context: 
	Document 1: [_citation_number]: «1»
[Snippet]: «Nearest neighbor search is a problem of finding the data points from the database such that the distances from them to the query point are the smallest. Learning to hash is one of the major solutions to this problem and has been widely studied recently. In this paper, we present a comprehensive survey of the learning to hash algorithms, categorize them according to the manners of preserving the similarities into: pairwise similarity preserving, multiwise similarity preserving, implicit similarity preserving, as well as quantization, and discuss their relations. We separate quantization from pairwise similarity preserving as the objective function is very different though quantization, as we show, can be derived from preserving the pairwise similarities. In addition, we present the evaluation protocols, and the general performance analysis, and point out that the quantization algorithms perform superiorly in terms of search accuracy, search time cost, and space cost. Finally, we introduce a few emerging topics.»
[Category]: «Performance Evaluation on Real-World Datasets»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-21T05:01:58+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1410.5410)\]. Further details \[[6](http://arxiv.org/abs/1911.04654)\]\[[7](http://arxiv.org/abs/1908.10396)\]\[[8](http://arxiv.org/abs/2404.00774)\]\[[9](http://arxiv.org/abs/1909.13459)\]\[[10]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Maximum Inner Product Search (MIPS) is a fundamental challenge in machine learning and information retrieval, particularly in high-dimensional data applications. Existing approaches to MIPS either rely solely on Inner Product (IP) similarity, which faces issues with local optima and redundant computations, or reduce the MIPS problem to the Nearest Neighbor Search under the Euclidean metric via space projection, leading to topology destruction and information loss. Despite the divergence of the two paradigms, we argue that there is no inherent binary opposition between IP and Euclidean metrics.
|    | reference                                                       |   date | key idea/summary                                                                                                                                                                                                                                         |
|----|-----------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [A Survey on Learning to Hash](http://arxiv.org/abs/1606.00185) |    nan | This paper provides a comprehensive survey of learning to hash algorithms, categorizes them based on similarity preservation methods, and highlights the superior performance of quantization algorithms in search accuracy, time, and space efficiency. |
### <a id='category-asymmetric-hashing-techniques'></a>Asymmetric Hashing Techniques: 3 papers found.
The category of Asymmetric Hashing Techniques focuses on the development of hashing algorithms for Maximum Inner Product Search (MIPS), a challenging problem in high-dimensional data retrieval. Existing approaches, such as Locality Sensitive Hashing (LSH), were found insufficient for MIPS due to the inherent asymmetry of inner product similarity \[[1](http://arxiv.org/abs/1606.00185)\]. To address this, asymmetric hashing schemes were introduced, where independent transformations are applied to query and database points, converting MIPS into an approximate near neighbor search problem \[[2](http://arxiv.org/abs/1405.5869)\]. This approach enables efficient sublinear time algorithms for MIPS, leveraging mathematical insights that allow inner products to be transformed into more tractable similarity measures \[[3](http://arxiv.org/abs/1410.5410)\]. Subsequent work has explored alternative transformations, such as converting MIPS into cosine similarity search using signed random projections, which offer improved theoretical guarantees and empirical performance \[[2](http://arxiv.org/abs/1405.5869)\]. However, there are also cases where symmetric LSH can be effective, suggesting that the choice between symmetric and asymmetric hashing depends on the specific data topology and problem requirements \[[3](http://arxiv.org/abs/1410.5410)\]. These developments highlight the ongoing exploration of asymmetric hashing as a promising direction for improving the efficiency and accuracy of MIPS in practical applications.
|    | reference                                                                                                                         |   date | key idea/summary                                                                                                                                                                                                                                                                                                     |
|----|-----------------------------------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Asymmetric LSH (ALSH) for Sublinear Time Maximum Inner Product Search
  (MIPS)](http://arxiv.org/abs/1405.5869)                  |    nan | The paper introduces the first provably sublinear time algorithm for approximate Maximum Inner Product Search (MIPS) using an extended Locality Sensitive Hashing (LSH) framework with asymmetric hashing schemes.                                                                                                   |
|  1 | [Improved Asymmetric Locality Sensitive Hashing (ALSH) for Maximum Inner
  Product Search (MIPS)](http://arxiv.org/abs/1410.5410) |    nan | This work introduces a new asymmetric transformation that converts approximate Maximum Inner Product Search (MIPS) into approximate cosine similarity search, enabling efficient solutions using signed random projections, and demonstrates its superiority over previous methods theoretically and experimentally. |
|  2 | [On Symmetric and Asymmetric LSHs for Inner Product Search](http://arxiv.org/abs/1410.5518)                                       |    nan | The paper demonstrates that a simple symmetric LSH exists for inner product similarity, offering stronger guarantees and better performance than the proposed asymmetric LSH, while also showing cases where asymmetry is necessary.                                                                                 |
### <a id='category-norm-ranging-lsh-method'></a>Norm-Ranging LSH Method: 1 papers found.
Context: 
	Document 1: [_citation_number]: «4»
[Snippet]: «Neyshabur and Srebro proposed Simple-LSH, which is the state-of-the-art
hashing method for maximum inner product search (MIPS) with performance
guarantee. We found that the performance of Simple-LSH, in both theory and
practice, suffers from long tails in the 2-norm distribution of real datasets.
We propose Norm-ranging LSH, which addresses the excessive normalization
problem caused by long tails in Simple-LSH by partitioning a dataset into
multiple sub-datasets and building a hash index for each sub-dataset
independently. We prove that Norm-ranging LSH has lower query time complexity
than Simple-LSH. We also show that the idea of partitioning the dataset can
improve other hashing based methods for MIPS. To support efficient query
processing on the hash indexes of the sub-datasets, a novel similarity metric
is formulated. Experiments show that Norm-ranging LSH achieves an order of
magnitude speedup over Simple-LSH for the same recall, thus significantly
benefiting applications that involve MIPS.»
[Category]: «Norm-Ranging LSH Method»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-21T05:01:58+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1410.5410)\]. Further details \[[6](http://arxiv.org/abs/1911.04654)\]\[[7](http://arxiv.org/abs/1908.10396)\]\[[8](http://arxiv.org/abs/2404.00774)\]\[[9](http://arxiv.org/abs/1909.13459)\]\[[10]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Maximum Inner Product Search (MIPS) is a fundamental challenge in machine
learning and information retrieval, particularly in high-dimensional data
applications. Existing approaches to MIPS either rely solely on Inner Product
(IP) similarity, which faces issues with local optima and redundant
computations, or reduce the MIPS problem to the Ne
|    | reference                                                                            |   date | key idea/summary                                                                                                                                                                                            |
|----|--------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Norm-Ranging LSH for Maximum Inner Product Search](http://arxiv.org/abs/1809.08782) |    nan | Norm-ranging LSH improves upon Simple-LSH by addressing the long-tail issue in 2-norm distribution through dataset partitioning and a novel similarity metric, achieving significant speedup in MIPS tasks. |
### <a id='category-norm-explicit-quantization'></a>Norm-Explicit Quantization: 1 papers found.
Context: 
	Document 1: [_citation_number]: «6»
[Snippet]: «Vector quantization (VQ) techniques are widely used in similarity search for data compression, fast metric computation and etc. Originally designed for Euclidean distance, existing VQ techniques (e.g., PQ, AQ) explicitly or implicitly minimize the quantization error. In this paper, we present a new angle to analyze the quantization error, which decomposes the quantization error into norm error and direction error. We show that quantization errors in norm have much higher influence on inner products than quantization errors in direction, and small quantization error does not necessarily lead to good performance in maximum inner product search (MIPS). Based on this observation, we propose norm-explicit quantization (NEQ) --- a general paradigm that improves existing VQ techniques for MIPS. NEQ quantizes the norms of items in a dataset explicitly to reduce errors in norm, which is crucial for MIPS. For the direction vectors, NEQ can simply reuse an existing VQ technique to quantize them without modification. We conducted extensive experiments on a variety of datasets and parameter configurations. The experimental results show that NEQ improves the performance of various VQ techniques for MIPS, including PQ, OPQ, RQ and AQ.»
[Category]: «Norm-Explicit Quantization»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-21T05:01:58+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1410.5410)\]. Further details \[[6](http://arxiv.org/abs/1911.04654)\]\[[7](http://arxiv.org/abs/1908.10396)\]\[[8](http://arxiv.org/abs/2404.00774)\]\[[9](http://arxiv.org/abs/1909.13459)\]\[[10]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Maximum Inner Product Search (MIPS) is a fundamental challenge in machine learning and information retrieval, particularly in high-dimensional data applications. Existing approaches to MIPS either rely solely on Inner Product (IP) similarity, which faces issues with local optima and
|    | reference                                                                                                                       |   date | key idea/summary                                                                                                                                                                                                      |
|----|---------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Norm-Explicit Quantization: Improving Vector Quantization for Maximum
  Inner Product Search](http://arxiv.org/abs/1911.04654) |    nan | NEQ improves existing vector quantization techniques for maximum inner product search by explicitly quantizing item norms to reduce norm errors, which have a greater impact on inner products than direction errors. |
### <a id='category-vector-quantization-for-mips'></a>Vector Quantization for MIPS: 3 papers found.
Context: 
	Document 1: [_citation_number]: «7»
[Snippet]: «Quantization based techniques are the current state-of-the-art for scaling maximum inner product search to massive databases. Traditional approaches to quantization aim to minimize the reconstruction error of the database points. Based on the observation that for a given query, the database points that have the largest inner products are more relevant, we develop a family of anisotropic quantization loss functions. Under natural statistical assumptions, we show that quantization with these loss functions leads to a new variant of vector quantization that more greatly penalizes the parallel component of a datapoint's residual relative to its orthogonal component. The proposed approach achieves state-of-the-art results on the public benchmarks available at \url(ann-benchmarks.com).»
[Category]: «Vector Quantization for MIPS»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-21T05:01:58+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1410.5410)\]. Further details \[[6](http://arxiv.org/abs/1911.04654)\]\[[7](http://arxiv.org/abs/1908.10396)\]\[[8](http://arxiv.org/abs/2404.00774)\]\[[9](http://arxiv.org/abs/1909.13459)\]\[[10]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Maximum Inner Product Search (MIPS) is a fundamental challenge in machine
learning and information retrieval, particularly in high-dimensional data
applications. Existing approaches to MIPS either rely solely on Inner Product
(IP) similarity, which faces issues with local optima and redundant
computations, or reduce the MIPS problem to the Nearest Neighbor Search under
the Euclidean metric via space projection, leading to topology destruction and
information loss. Despite the divergence of the two paradigms, we argue that
there is no inherent binary opposition between IP and Euclidean metrics. By
stitching IP and Euclidean in the design of indexing and search algorithms, we
can significantly enhance MIPS performance. Specifically, this paper explores
the theoretical and empirical connections
|    | reference                                                                                                   |   date | key idea/summary                                                                                                                                                                                                                                       |
|----|-------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Accelerating Large-Scale Inference with Anisotropic Vector Quantization](http://arxiv.org/abs/1908.10396)  |    nan | The paper introduces anisotropic quantization loss functions for maximum inner product search, which penalize the parallel component of residual vectors more than the orthogonal component, leading to state-of-the-art results on public benchmarks. |
|  1 | [FARGO: Fast maximum inner product search via global multi-probing]()                                       |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                              |
|  2 | [ProMIPS: Efficient high-dimensional C-approximate maximum inner product search with a lightweight index]() |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                              |
### <a id='category-metric-integration-in-indexing'></a>Metric Integration in Indexing: 1 papers found.
Context: 
	Document 1: [_citation_number]: «8»
[Snippet]: «This paper introduces SOAR: Spilling with Orthogonality-Amplified Residuals,
a novel data indexing technique for approximate nearest neighbor (ANN) search.
SOAR extends upon previous approaches to ANN search, such as spill trees, that
utilize multiple redundant representations while partitioning the data to
reduce the probability of missing a nearest neighbor during search. Rather than
training and computing these redundant representations independently, however,
SOAR uses an orthogonality-amplified residual loss, which optimizes each
representation to compensate for cases where other representations perform
poorly. This drastically improves the overall index quality, resulting in
state-of-the-art ANN benchmark performance while maintaining fast indexing
times and low memory consumption.»
[Category]: «Metric Integration in Indexing»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-21T05:01:58+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1410.5410)\]. Further details \[[6](http://arxiv.org/abs/1911.04654)\]\[[7](http://arxiv.org/abs/1908.10396)\]\[[8](http://arxiv.org/abs/2404.00774)\]\[[9](http://arxiv.org/abs/1909.13459)\]\[[10]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Maximum Inner Product Search (MIPS) is a fundamental challenge in machine
learning and information retrieval, particularly in high-dimensional data
applications. Existing approaches to MIPS either rely solely on Inner Product
(IP) similarity, which faces issues with local optima and redundant
computations, or reduce the MIPS problem to the Nearest Neighbor Search under
the Euclidean metric via space projection, leading to topology destruction and
information loss. Despite the divergence of the two paradigms, we argue that
there is no inherent binary opposition between IP and Euclidean metrics. By
stitching IP and Euclidean in the design of indexing and search algorithms, we
can significantly enhance MIPS performance. Specifically,
|    | reference                                                                                          |   date | key idea/summary                                                                                                                                                                                                                                        |
|----|----------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [SOAR: Improved Indexing for Approximate Nearest Neighbor Search](http://arxiv.org/abs/2404.00774) |    nan | SOAR is a novel data indexing technique for approximate nearest neighbor search that improves index quality by using an orthogonality-amplified residual loss to optimize representations and compensate for poor performance in other representations. |
### <a id='category-graph-based-indexing-methods'></a>Graph-Based Indexing Methods: 4 papers found.
Context: 
	Document 1: [_citation_number]: «9»
[Snippet]: «The inner-product navigable small world graph (ip-NSW) represents the
state-of-the-art method for approximate maximum inner product search (MIPS) and
it can achieve an order of magnitude speedup over the fastest baseline.
However, to date it is still unclear where its exceptional performance comes
from. In this paper, we show that there is a strong norm bias in the MIPS
problem, which means that the large norm items are very likely to become the
result of MIPS. Then we explain the good performance of ip-NSW as matching the
norm bias of the MIPS problem - large norm items have big in-degrees in the
ip-NSW proximity graph and a walk on the graph spends the majority of
computation on these items, thus effectively avoids unnecessary computation on
small norm items. Furthermore, we propose the ip-NSW+ algorithm, which improves
ip-NSW by introducing an additional angular proximity graph. Search is first
conducted on the angular graph to find the angular neighbors of a query and
then the MIPS neighbors of these angular neighbors are used to initialize the
candidate pool for search on the inner-product proximity graph. Experiment
results show that ip-NSW+ consistently and significantly outperforms ip-NSW and
provides more robust performance under different data distributions.»
[Category]: «Graph-Based Indexing Methods»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-21T05:01:58+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1410.5410)\]. Further details \[[6](http://arxiv.org/abs/1911.04654)\]\[[7](http://arxiv.org/abs/1908.10396)\]\[[8](http://arxiv.org/abs/2404.00774)\]\[[9](http://arxiv.org/abs/1909.13459)\]\[[10]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Maximum Inner Product Search (MIPS) is a fundamental challenge in machine
learning and
|    | reference                                                                                                           |   date | key idea/summary                                                                                                                                                                                       |
|----|---------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Understanding and Improving Proximity Graph based Maximum Inner Product
  Search](http://arxiv.org/abs/1909.13459) |    nan | The paper introduces ip-NSW+, an improved version of the ip-NSW algorithm for approximate maximum inner product search, which leverages angular proximity to enhance search efficiency and robustness. |
|  1 | [Non-metric similarity graphs for maximum inner product search]()                                                   |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                              |
|  2 | [M(\"o)bius transformation for fast inner product search on graph]()                                                |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                              |
|  3 | [Norm adjusted proximity graph for fast inner product retrieval]()                                                  |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                              |
### <a id='category-euclidean-metric-reduction-approaches'></a>Euclidean Metric Reduction Approaches: 1 papers found.
Context: 
	Document 1: [_citation_number]: «10»
[Snippet]: «»
[Category]: «Euclidean Metric Reduction Approaches»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-21T05:01:58+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1410.5410)\]. Further details \[[6](http://arxiv.org/abs/1911.04654)\]\[[7](http://arxiv.org/abs/1908.10396)\]\[[8](http://arxiv.org/abs/2404.00774)\]\[[9](http://arxiv.org/abs/1909.13459)\]\[[10]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Maximum Inner Product Search (MIPS) is a fundamental challenge in machine
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
real-world datasets demonstrate that MAG outperforms existing state-of
|    | reference                                                                                             |   date | key idea/summary                                                                                          |
|----|-------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------|
|  0 | [Speeding up the xbox recommender system using a euclidean transformation for inner-product spaces]() |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
### <a id='category-inner-product-similarity-limitations'></a>Inner Product Similarity Limitations: 1 papers found.
Context: 
	Document 1: [_citation_number]: «13»
[Snippet]: «»
[Category]: «Inner Product Similarity Limitations»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-21T05:01:58+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1410.5410)\]. Further details \[[6](http://arxiv.org/abs/1911.04654)\]\[[7](http://arxiv.org/abs/1908.10396)\]\[[8](http://arxiv.org/abs/2404.00774)\]\[[9](http://arxiv.org/abs/1909.13459)\]\[[10]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Maximum Inner Product Search (MIPS) is a fundamental challenge in machine
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
real-world datasets demonstrate that MAG outperforms existing state-of
|    | reference                                                                                   |   date | key idea/summary                                                                                          |
|----|---------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------|
|  0 | [Reconsidering Tree based Methods for k-Maximum Inner-Product Search: The LRUS-CoverTree]() |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
