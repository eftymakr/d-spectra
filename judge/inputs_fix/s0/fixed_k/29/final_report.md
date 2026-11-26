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
## Research papers
### Outline
- [Graph-Based Indexing Techniques [1 papers]](#category-graph-based-indexing-techniques)
- [Budgeted MIPS Algorithms [2 papers]](#category-budgeted-mips-algorithms)
- [IP-Based MIPS Approaches [3 papers]](#category-ip-based-mips-approaches)
- [Approximate MIPS Algorithms [10 papers]](#category-approximate-mips-algorithms)
- [MIPS Problem Definition and Challenges [1 papers]](#category-mips-problem-definition-and-challenges)
- [Reverse MIPS Applications [1 papers]](#category-reverse-mips-applications)
- [Data Topology and Parameter Tuning [1 papers]](#category-data-topology-and-parameter-tuning)

### <a id='category-graph-based-indexing-techniques'></a>Graph-Based Indexing Techniques: 1 papers found.
Context: 
	Document 1: [Snippet]: «
 Maximum Inner Product Search (MIPS) for high-dimensional vectors is pivotal across databases, information retrieval, and artificial intelligence. Existing methods either reduce MIPS to Nearest Neighbor Search (NNS) while suffering from harmful vector space transformations, or attempt to tackle MIPS directly but struggle to mitigate redundant computations due to the absence of the triangle inequality. This paper presents a novel theoretical framework that equates MIPS with NNS without requiring space transformation, thereby allowing us to leverage advanced graph-based indices for NNS and efficient edge pruning strategies, significantly reducing unnecessary computations. Despite a strong baseline set by our theoretical analysis, we identify and address two persistent challenges to further refine our method: the introduction of the
 P
 roximity Graph with
 S
 pherical
 P
 athway (PSP), designed to mitigate the issue of MIPS solutions clustering around large-norm vectors, and the implementation of
 A
 daptive
 E
 arly
 T
 ermination (AET), which efficiently curtails the excessive exploration once an accuracy bottleneck is reached. Extensive experiments reveal that our method is superior to existing state-of-the-art techniques in search efficiency, scalability, and practical applicability. Compared with state-of-the-art graph-based methods, it achieves an average 35% speed-up in query processing and a 3× reduction in index size. Notably, our approach has been validated and deployed in the search engines of Shopee, a well-known online shopping platform. Our code and an industrial-scale dataset for offline evaluation will also be released to address the absence of e-commerce data in public benchmarks.
»
[_citation_number]: «1»
[Category]: «Graph-Based Indexing Techniques»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-21T05:01:58+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1909.13459)\]. Further details \[[6](http://arxiv.org/abs/1908.08656)\]\[[7](http://arxiv.org/abs/1509.01469)\]\[[8](http://arxiv.org/abs/2402.13858)\]\[[9](http://arxiv.org/abs/2104.04406)\]\[[10](http://arxiv.org/abs/1507.05910)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Maximum Inner Product Search (MIPS) is a fundamental challenge in machine
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1909.13459)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1610.03317)\]\[[7](http://arxiv.org/abs/1509.01469)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Graph-based indexing techniques have emerged as a promising approach for addressing the challenges of Maximum Inner Product Search (MIPS) in high-dimensional spaces \[[1](http://arxiv.org/abs/2503.06882)\]. Traditional methods often reduce MIPS to Nearest Neighbor Search (NNS) through vector space transformations, which can introduce distortions and information loss \[[1](http://arxiv.org/abs/2503.06882)\]. Alternatively, some approaches attempt to solve MIPS directly but face limitations due to the absence of the triangle inequality, leading to redundant computations \[[1](http://arxiv.org/abs/2503.06882)\]. This paper introduces a novel theoretical framework that equates MIPS with NNS without requiring space transformation, enabling the use of advanced graph-based indices for NNS and efficient edge pruning strategies \[[1](http://arxiv.org/abs/2503.06882)\]. The proposed method introduces the Proximity Graph with Spherical Pathway (PSP) to mitigate clustering around large-norm vectors and Adaptive Early Termination (AET) to curtail excessive exploration once an accuracy bottleneck is reached \[[1](http://arxiv.org/abs/2503.06882)\]. These innovations significantly enhance search efficiency and scalability, achieving an average 35% speed-up in query processing and a 3× reduction in index size compared to state-of-the-art graph-based methods \[[1](http://arxiv.org/abs/2503.06882)\]. The approach has been validated and deployed in real-world applications, such as the search engines of Shopee, demonstrating its practical applicability and effectiveness \[[1](http://arxiv.org/abs/2503.06882)\].
|    | reference                                                                                 | date     | key idea/summary                                                                                                                                                                                                                                                                                                             |
|----|-------------------------------------------------------------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Maximum Inner Product is Query-Scaled Nearest Neighbor](http://arxiv.org/abs/2503.06882) | 02/01/25 | This paper introduces a novel framework that equates Maximum Inner Product Search (MIPS) with Nearest Neighbor Search (NNS) without space transformation, leveraging graph-based indices and edge pruning strategies to improve search efficiency and scalability, with practical applications in e-commerce search engines. |
### <a id='category-budgeted-mips-algorithms'></a>Budgeted MIPS Algorithms: 2 papers found.
Context: 
	Document 1: [Snippet]: «Maximum Inner Product Search (MIPS) is an important task in many machine learning applications such as the prediction phase of a low-rank matrix factorization model for a recommender system. There have been some works on how to perform MIPS in sub-linear time recently. However, most of them do not have the flexibility to control the trade-off between search efficient and search quality. In this paper, we study the MIPS problem with a computational budget. By carefully studying the problem structure of MIPS, we develop a novel Greedy-MIPS algorithm, which can handle budgeted MIPS by design. While simple and intuitive, Greedy-MIPS yields surprisingly superior performance compared to state-of-the-art approaches. As a specific example, on a candidate set containing half a million vectors of dimension 200, Greedy-MIPS runs 200x faster than the naive approach while yielding search results with the top-5 precision greater than 75\%.»
[_citation_number]: «2»
[Category]: «Budgeted MIPS Algorithms»

	Document 2: [Snippet]: «Top-k maximum inner product search (MIPS) is a central task in many machine learning applications. This paper extends top-k MIPS with a budgeted setting, that asks for the best approximate top-k MIPS given a limit of B computational operations. We investigate recent advanced sampling algorithms, including wedge and diamond sampling to solve it. Though the design of these sampling schemes naturally supports budgeted top-k MIPS, they suffer from the linear cost from scanning all data points to retrieve top-k results and the performance degradation for handling negative inputs. 
This paper makes two main contributions. First, we show that diamond sampling is essentially a combination between wedge sampling and basic sampling for top-k MIPS. Our theoretical analysis and empirical evaluation show that wedge is competitive (often superior) to diamond on approximating top-k MIPS regarding both efficiency and accuracy. Second, we propose a series of algorithmic engineering techniques to deploy wedge sampling on budgeted top-k MIPS. Our novel deterministic wedge-based algorithm runs significantly faster than the state-of-the-art methods for budgeted and exact top-k MIPS while maintaining the top-5 precision at least 80% on standard recommender system data sets.»
[_citation_number]: «6»
[Category]: «Budgeted MIPS Algorithms»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-21T05:01:58+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1909.13459)\]. Further details \[[6](http://arxiv.org/abs/1908.08656)\]\[[7](http://arxiv.org/abs/1509.01469)\]\[[8](http://arxiv.org/abs/2402.13858)\]\[[9](http://arxiv.org/abs/2104.04406)\]\[[10](http://arxiv.org/abs/1507.05910)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Maximum Inner Product Search (MIPS) is a fundamental challenge in machine
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1909.13459)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1610.03317)\]\[[7](http://arxiv.org/abs/1509.01469)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Recent research has focused on improving the efficiency and accuracy of Maximum Inner Product Search (MIPS) under computational budget constraints, particularly in high-dimensional data applications \[[2](http://arxiv.org/abs/1610.03317)\]. Several approaches have been proposed to address the challenge of balancing search efficiency and quality, with a growing emphasis on budgeted MIPS settings where the number of computational operations is limited \[[6](http://arxiv.org/abs/1908.08656)\]. For instance, the Greedy-MIPS algorithm was introduced to handle budgeted MIPS by design, offering significant speed improvements over naive approaches while maintaining high top-5 precision \[[2](http://arxiv.org/abs/1610.03317)\]. Similarly, studies have explored advanced sampling techniques such as wedge and diamond sampling to approximate top-k MIPS under budget constraints, although these methods face challenges such as linear scanning costs and performance degradation with negative inputs \[[6](http://arxiv.org/abs/1908.08656)\]. Theoretical analysis has shown that wedge sampling can often outperform diamond sampling in terms of both efficiency and accuracy for budgeted top-k MIPS \[[6](http://arxiv.org/abs/1908.08656)\]. These developments highlight the ongoing efforts to enhance MIPS performance through algorithmic innovations that accommodate computational limitations.
|    | reference                                                                                              | date     | key idea/summary                                                                                                                                                                                                        |
|----|--------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [A Greedy Approach for Budgeted Maximum Inner Product Search](http://arxiv.org/abs/1610.03317)         | 10/11/16 | The paper introduces a novel Greedy-MIPS algorithm that efficiently solves the Maximum Inner Product Search problem with a computational budget, achieving superior performance compared to existing methods.           |
|  1 | [Revisiting Wedge Sampling for Budgeted Maximum Inner Product Search](http://arxiv.org/abs/1908.08656) | 08/23/19 | This paper introduces a budgeted approach to top-k maximum inner product search (MIPS) and proposes a novel deterministic wedge-based algorithm that significantly improves efficiency while maintaining high accuracy. |
### <a id='category-ip-based-mips-approaches'></a>IP-Based MIPS Approaches: 3 papers found.
Document 1 discusses the inner-product navigable small world graph (ip-NSW), which is a state-of-the-art method for approximate maximum inner product search (MIPS) and achieves significant speedup over baselines \[[3](http://arxiv.org/abs/1909.13459)\]. It highlights the norm bias in MIPS, where large norm items are more likely to be results, and explains how ip-NSW leverages this by giving higher in-degrees to large norm items, thus reducing unnecessary computations \[[3](http://arxiv.org/abs/1909.13459)\]. The paper also introduces ip-NSW+, which improves performance by incorporating an angular proximity graph to enhance search efficiency \[[3](http://arxiv.org/abs/1909.13459)\].

Document 2 presents a quantization-based approach for fast MIPS, where database vectors are quantized into multiple subspaces using codebooks learned to minimize inner product quantization error \[[7](http://arxiv.org/abs/1509.01469)\]. This method avoids the need for augmenting vectors in higher-dimensional spaces, unlike LSH approaches, and provides theoretical guarantees on approximation accuracy \[[7](http://arxiv.org/abs/1509.01469)\]. The approach also allows for improved accuracy when trained with example queries \[[7](http://arxiv.org/abs/1509.01469)\].

Document 3 introduces CEOs, a dimensionality reduction method for MIPS based on extreme order statistics, which enables sublinear MIPS with exponential indexing space complexity \[[15](http://arxiv.org/abs/2012.11098)\]. It proposes practical variants, such as sCEOs-TA and coCEOs, that use linear space and achieve high search recall and speedup over brute-force methods \[[15](http://arxiv.org/abs/2012.11098)\]. These methods are particularly effective for large-scale datasets, offering significant performance improvements \[[15](http://arxiv.org/abs/2012.11098)\].

These works collectively highlight the diversity of approaches to MIPS, ranging from graph-based methods like ip-NSW and ip-NSW+ \[[3](http://arxiv.org/abs/1909.13459)\], to quantization-based techniques \[[7](http://arxiv.org/abs/1509.01469)\], and dimensionality reduction strategies \[[15](http://arxiv.org/abs/2012.11098)\]. Each approach addresses specific challenges in MIPS, such as computational efficiency, accuracy, and scalability, while contributing to the broader understanding of inner product search in high-dimensional spaces.
|    | reference                                                                                                                | date     | key idea/summary                                                                                                                                                                                                                                           |
|----|--------------------------------------------------------------------------------------------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Understanding and Improving Proximity Graph based Maximum Inner Product Search](http://arxiv.org/abs/1909.13459)        | 09/30/19 | The paper introduces ip-NSW+, an improved version of the ip-NSW algorithm for approximate maximum inner product search, which leverages angular proximity to enhance performance and robustness across different data distributions.                       |
|  1 | [Quantization based Fast Inner Product Search](http://arxiv.org/abs/1509.01469)                                          | 09/04/15 | The paper proposes a quantization-based approach for fast approximate Maximum Inner Product Search (MIPS) that avoids the need for augmenting vectors in a higher-dimensional space, achieving significant performance improvements over existing methods. |
|  2 | [Sublinear Maximum Inner Product Search using Concomitants of Extreme Order Statistics](http://arxiv.org/abs/2012.11098) | 12/21/20 | CEOs is a novel dimensionality reduction method for maximum inner product search that achieves sublinear time complexity and high search recall, with practical variants offering linear space complexity and significant speedup over brute-force search. |
### <a id='category-approximate-mips-algorithms'></a>Approximate MIPS Algorithms: 10 papers found.
Related Works on Approximate MIPS Algorithms \[[1](http://arxiv.org/abs/2503.06882)\]\[[2](http://arxiv.org/abs/1610.03317)\]\[[3](http://arxiv.org/abs/1909.13459)\]\[[4](http://arxiv.org/abs/2212.07551)\]\[[5](http://arxiv.org/abs/2309.09013)\]\[[6](http://arxiv.org/abs/1908.08656)\]\[[7](http://arxiv.org/abs/1509.01469)\]\[[8](http://arxiv.org/abs/2402.13858)\]\[[9](http://arxiv.org/abs/2104.04406)\]\[[10](http://arxiv.org/abs/1507.05910)\]. The Maximum Inner Product Search (MIPS) problem has been extensively studied, with a variety of approaches proposed to address its computational challenges, particularly in high-dimensional settings. Early methods, such as Locality Sensitive Hashing (LSH) \[[4](http://arxiv.org/abs/2212.07551)\], aimed to reduce the search space by hashing vectors into buckets, but they often required significant preprocessing and were sensitive to data distribution \[[8](http://arxiv.org/abs/2402.13858)\]. More recent work has focused on improving efficiency and accuracy through randomized and adaptive sampling techniques, such as BanditMIPS \[[1](http://arxiv.org/abs/2503.06882)\], which leverages multi-armed bandit strategies to dynamically allocate computational resources, achieving constant-time complexity independent of dimensionality. Similarly, clustering-based approaches \[[2](http://arxiv.org/abs/1610.03317)\] have been explored to partition data into manageable subsets, enabling efficient retrieval by searching only a fraction of the dataset. These methods are particularly effective for sparse vectors, where traditional dense vector techniques may not perform well \[[5](http://arxiv.org/abs/2309.09013)\]. Additionally, asymmetric transformations have been introduced to convert MIPS into problems that can be solved using existing hashing or projection techniques \[[7](http://arxiv.org/abs/1509.01469)\]\[[14](http://arxiv.org/abs/1410.5410)\]. For instance, spherical $k$-means has been adapted to approximate MIPS by aligning vectors in a way that preserves inner product relationships \[[4](http://arxiv.org/abs/2212.07551)\]. Another line of research has focused on sublinear-time algorithms, such as those based on asymmetric LSH (ALSH) \[[11](http://arxiv.org/abs/1405.5869)\], which provide theoretical guarantees for approximate MIPS by leveraging mathematical properties of inner products. These approaches often require careful tuning of parameters to balance accuracy and runtime \[[6](http://arxiv.org/abs/1908.08656)\]. Furthermore, methods like NORM-RANGING LSH \[[16](http://arxiv.org/abs/1809.08782)\] have been proposed to address issues with normalization in real-world datasets, improving query efficiency by partitioning data into sub-datasets. Overall, these works highlight the diversity of strategies for approximate MIPS, ranging from hashing and clustering to adaptive sampling and mathematical transformations, each with its own trade-offs in terms of accuracy, speed, and preprocessing requirements.
|    | reference                                                                                                                                  | date     | key idea/summary                                                                                                                                                                                                                                                                                                     |
|----|--------------------------------------------------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Faster Maximum Inner Product Search in High Dimensions](http://arxiv.org/abs/2212.07551)                                                  | 12/14/22 | BanditMIPS is a novel randomized algorithm for Maximum Inner Product Search (MIPS) that achieves constant-time complexity independent of dimensionality, outperforming existing methods by adaptively sampling coordinates using a multi-armed bandit strategy.                                                      |
|  1 | [Bridging Dense and Sparse Maximum Inner Product Search](http://arxiv.org/abs/2309.09013)                                                  | 09/16/23 | This work explores the application of dense vector algorithms to sparse vectors, proposing clustering-based approximate MIPS and dynamic pruning for efficient sparse vector retrieval.                                                                                                                              |
|  2 | [ProMIPS: Efficient High-Dimensional c-Approximate Maximum Inner Product Search with a Lightweight Index](http://arxiv.org/abs/2104.04406) | 04/01/21 | The paper proposes an efficient method for c-Approximate Maximum Inner Product (c-AMIP) search using a lightweight iDistance index and 2-stable random projections, achieving better efficiency and search quality compared to existing methods.                                                                     |
|  3 | [Clustering is Efficient for Approximate Maximum Inner Product Search](http://arxiv.org/abs/1507.05910)                                    | 07/21/15 | The paper proposes a new approach using spherical k-means to solve approximate Maximum Inner Product Search (MIPS), which outperforms LSH-based methods in recall rate tests and can benefit large-scale applications like training neural probabilistic language models.                                            |
|  4 | [Asymmetric LSH (ALSH) for Sublinear Time Maximum Inner Product Search (MIPS)](http://arxiv.org/abs/1405.5869)                             | 05/22/14 | The paper introduces the first provably sublinear time algorithm for approximate Maximum Inner Product Search (MIPS) using an extended Locality Sensitive Hashing (LSH) framework with asymmetric hashing schemes.                                                                                                   |
|  5 | [A Bandit Approach to Maximum Inner Product Search](http://arxiv.org/abs/1812.06360)                                                       | 12/15/18 | The paper introduces the first approximate algorithm for Maximum Inner Product Search (MIPS) that requires no preprocessing and allows users to control and bound the suboptimality of results, outperforming existing methods.                                                                                      |
|  6 | [Improved Asymmetric Locality Sensitive Hashing (ALSH) for Maximum Inner Product Search (MIPS)](http://arxiv.org/abs/1410.5410)            | 10/20/14 | This work introduces a new asymmetric transformation that converts approximate Maximum Inner Product Search (MIPS) into approximate cosine similarity search, enabling efficient solutions using signed random projections, and demonstrates its superiority over previous methods theoretically and experimentally. |
|  7 | [Norm-Ranging LSH for Maximum Inner Product Search](http://arxiv.org/abs/1809.08782)                                                       | 09/24/18 | NORM-RANGING LSH is a hashing-based algorithm that addresses the performance issues of SIMPLE-LSH by partitioning datasets into sub-datasets and building independent hash indexes, leading to lower query time complexity and improved efficiency in maximum inner product search.                                  |
|  8 | [An Approximate Algorithm for Maximum Inner Product Search over Streaming Sparse Vectors](http://arxiv.org/abs/2301.10622)                 | 01/25/23 | The paper introduces Sinnamon, a novel approximate algorithm for efficiently retrieving top-k results for sparse real-valued vectors in dynamic streaming settings, offering trade-offs between memory, latency, and accuracy.                                                                                       |
|  9 | [Optimistic Query Routing in Clustering-based Approximate Maximum Inner Product Search](http://arxiv.org/abs/2405.12207)                   | 05/20/24 | This work introduces a framework for clustering-based maximum inner product search that leverages the moments of inner product distributions within shards to improve search efficiency, achieving state-of-the-art accuracy with fewer probes and space-efficient designs.                                          |
### <a id='category-mips-problem-definition-and-challenges'></a>MIPS Problem Definition and Challenges: 1 papers found.
Context: 
	Document 1: [Snippet]: «The $k$-Maximum Inner Product Search ($k$MIPS) serves as a foundational component in recommender systems and various data mining tasks. However, while most existing $k$MIPS approaches prioritize the efficient retrieval of highly relevant items for users, they often neglect an equally pivotal facet of search results: \emph(diversity). To bridge this gap, we revisit and refine the diversity-aware $k$MIPS (D$k$MIPS) problem by incorporating two well-known diversity objectives -- minimizing the average and maximum pairwise item similarities within the results -- into the original relevance objective. This enhancement, inspired by Maximal Marginal Relevance (MMR), offers users a controllable trade-off between relevance and diversity. We introduce \textsc(Greedy) and \textsc(DualGreedy), two linear scan-based algorithms tailored for D$k$MIPS. They both achieve data-dependent approximations and, when aiming to minimize the average pairwise similarity, \textsc(DualGreedy) attains an approximation ratio of $1/4$ with an additive term for regularization. To further improve query efficiency, we integrate a lightweight Ball-Cone Tree (BC-Tree) index with the two algorithms. Finally, comprehensive experiments on ten real-world data sets demonstrate the efficacy of our proposed methods, showcasing their capability to efficiently deliver diverse and relevant search results to users.»
[_citation_number]: «8»
[Category]: «MIPS Problem Definition and Challenges»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-21T05:01:58+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1909.13459)\]. Further details \[[6](http://arxiv.org/abs/1908.08656)\]\[[7](http://arxiv.org/abs/1509.01469)\]\[[8](http://arxiv.org/abs/2402.13858)\]\[[9](http://arxiv.org/abs/2104.04406)\]\[[10](http://arxiv.org/abs/1507.05910)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Maximum Inner Product Search (MIPS) is a fundamental challenge in machine
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1909.13459)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1610.03317)\]\[[7](http://arxiv.org/abs/1509.01469)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer:  
The $k$-Maximum Inner Product Search ($k$MIPS) is a critical task in recommendation systems and data mining, where the goal is to retrieve the most relevant items for users \[[8](http://arxiv.org/abs/2402.13858)\]. However, many existing approaches focus primarily on maximizing relevance, often at the expense of diversity in the search results \[[8](http://arxiv.org/abs/2402.13858)\]. This limitation highlights a key challenge in $k$MIPS: balancing relevance with diversity to ensure that the retrieved items are both pertinent and varied \[[8](http://arxiv.org/abs/2402.13858)\]. To address this, recent work has introduced diversity-aware $k$MIPS (D$k$MIPS) by incorporating objectives such as minimizing the average and maximum pairwise similarities among retrieved items \[[8](http://arxiv.org/abs/2402.13858)\]. This approach is inspired by the Maximal Marginal Relevance (MMR) framework, which enables a controllable trade-off between relevance and diversity \[[8](http://arxiv.org/abs/2402.13858)\]. Two algorithms, \textsc(Greedy) and \textsc(DualGreedy), have been proposed to achieve this balance, with \textsc(DualGreedy) offering an approximation ratio of $1/4$ when minimizing average pairwise similarity \[[8](http://arxiv.org/abs/2402.13858)\]. Additionally, the integration of a lightweight Ball-Cone Tree (BC-Tree) index has been shown to improve query efficiency, demonstrating the potential for combining efficiency and diversity in $k$MIPS \[[8](http://arxiv.org/abs/2402.13858)\]. These developments underscore the ongoing efforts to enhance the practicality and effectiveness of $k$MIPS in real-world applications.
|    | reference                                                                                   | date     | key idea/summary                                                                                                                                                                                                                                |
|----|---------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Diversity-Aware k-Maximum Inner Product Search Revisited](http://arxiv.org/abs/2402.13858) | 02/21/24 | The paper introduces D$k$MIPS, a diversity-aware $k$-Maximum Inner Product Search method that balances relevance and diversity in search results, achieving efficient and effective retrieval through novel algorithms and indexing techniques. |
### <a id='category-reverse-mips-applications'></a>Reverse MIPS Applications: 1 papers found.
Context: 
	Document 1: [Snippet]: «The MIPS (maximum inner product search), which finds the item with the highest inner product with a given query user, is an essential problem in the recommendation field. It is usual that e-commerce companies face situations where they want to promote and sell new or discounted items. In these situations, we have to consider a question: who are interested in the items and how to find them? This paper answers this question by addressing a new problem called reverse maximum inner product search (reverse MIPS). Given a query vector and two sets of vectors (user vectors and item vectors), the problem of reverse MIPS finds a set of user vectors whose inner product with the query vector is the maximum among the query and item vectors. Although the importance of this problem is clear, its straightforward implementation incurs a computationally expensive cost. We therefore propose Simpfer, a simple, fast, and exact algorithm for reverse MIPS. In an offline phase, Simpfer builds a simple index that maintains a lower-bound of the maximum inner product. By exploiting this index, Simpfer judges whether the query vector can have the maximum inner product or not, for a given user vector, in a constant time. Besides, our index enables filtering user vectors, which cannot have the maximum inner product with the query vector, in a batch. We theoretically demonstrate that Simpfer outperforms baselines employing state-of-the-art MIPS techniques. Furthermore, our extensive experiments on real datasets show that Simpfer is about 500–8000 times faster than the baselines.»
[_citation_number]: «13»
[Category]: «Reverse MIPS Applications»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-21T05:01:58+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1909.13459)\]. Further details \[[6](http://arxiv.org/abs/1908.08656)\]\[[7](http://arxiv.org/abs/1509.01469)\]\[[8](http://arxiv.org/abs/2402.13858)\]\[[9](http://arxiv.org/abs/2104.04406)\]\[[10](http://arxiv.org/abs/1507.05910)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Maximum Inner Product Search (MIPS) is a fundamental challenge in machine
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1909.13459)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1610.03317)\]\[[7](http://arxiv.org/abs/1509.01469)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Reverse Maximum Inner Product Search (Reverse MIPS) has emerged as a critical problem in recommendation systems, particularly in scenarios where e-commerce platforms aim to promote new or discounted items \[[13](http://arxiv.org/abs/2110.07131)\]. The challenge lies in efficiently identifying user vectors that have the highest inner product with a given query vector, which is essential for targeted marketing and personalized recommendations. Traditional approaches to Maximum Inner Product Search (MIPS) often face computational inefficiencies, especially when dealing with large-scale datasets \[[13](http://arxiv.org/abs/2110.07131)\]. To address this, researchers have proposed novel algorithms such as Simpfer, which introduces an offline indexing phase that maintains a lower-bound of the maximum inner product, enabling efficient filtering and constant-time evaluation of user vectors \[[13](http://arxiv.org/abs/2110.07131)\]. This approach significantly reduces the computational overhead, making it feasible to handle real-time queries in high-dimensional spaces. The effectiveness of such methods is further validated by empirical studies demonstrating substantial performance improvements over existing baselines \[[13](http://arxiv.org/abs/2110.07131)\].
|    | reference                                                                                                                             | date     | key idea/summary                                                                                                                                                                                                                                 |
|----|---------------------------------------------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Reverse Maximum Inner Product Search: How to efficiently find users who would like to buy my item?](http://arxiv.org/abs/2110.07131) | 09/13/21 | The paper introduces Simpfer, an efficient and exact algorithm for reverse maximum inner product search (reverse MIPS) that significantly outperforms existing methods by using a lower-bound index to filter and evaluate user vectors quickly. |
### <a id='category-data-topology-and-parameter-tuning'></a>Data Topology and Parameter Tuning: 1 papers found.
Context: 
	Document 1: [Snippet]: «Despite the efficacy of graph-based algorithms for Approximate Nearest Neighbor (ANN) searches, the optimal tuning of such systems remains unclear. This study introduces a method to tune the performance of off-the-shelf graph-based indexes, focusing on the dimension of vectors, database size, and entry points of graph traversal. We utilize a black-box optimization algorithm to perform integrated tuning to meet the required levels of recall and Queries Per Second (QPS). We applied our approach to Task A of the SISAP 2023 Indexing Challenge and got second place in the 10M and 30M tracks. It improves performance substantially compared to brute force methods. This research offers a universally applicable tuning method for graph-based indexes, extending beyond the specific conditions of the competition to broader uses.»
[_citation_number]: «19»
[Category]: «Data Topology and Parameter Tuning»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-21T05:01:58+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1909.13459)\]. Further details \[[6](http://arxiv.org/abs/1908.08656)\]\[[7](http://arxiv.org/abs/1509.01469)\]\[[8](http://arxiv.org/abs/2402.13858)\]\[[9](http://arxiv.org/abs/2104.04406)\]\[[10](http://arxiv.org/abs/1507.05910)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Maximum Inner Product Search (MIPS) is a fundamental challenge in machine
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1909.13459)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1610.03317)\]\[[7](http://arxiv.org/abs/1509.01469)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The category of Data Topology and Parameter Tuning is crucial in the development of efficient graph-based indexing systems for Approximate Nearest Neighbor (ANN) searches. This area focuses on optimizing the performance of graph-based indexes by considering factors such as vector dimension, database size, and traversal entry points \[[19](http://arxiv.org/abs/2309.00472)\]. The tuning process often involves black-box optimization algorithms that integrate multiple parameters to achieve desired levels of recall and Queries Per Second (QPS) \[[19](http://arxiv.org/abs/2309.00472)\]. Such methods are particularly important in scenarios where brute force approaches are inefficient, and where the data topology significantly influences search performance. This research highlights the need for adaptive strategies that can dynamically adjust to varying data characteristics, ensuring that the indexing and search algorithms remain effective across different datasets and application scenarios \[[19](http://arxiv.org/abs/2309.00472)\].
|    | reference                                                                                                                                                  | date     | key idea/summary                                                                                                                                                                                                                                  |
|----|------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [General and Practical Tuning Method for Off-the-Shelf Graph-Based Index: SISAP Indexing Challenge Report by Team UTokyo](http://arxiv.org/abs/2309.00472) | 09/01/23 | This study introduces a method to optimally tune graph-based indexes for Approximate Nearest Neighbor searches by considering vector dimension, database size, and traversal entry points, achieving better performance than brute force methods. |
