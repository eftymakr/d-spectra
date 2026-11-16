## Related Works

Representation learning is a cornerstone of modern recommender systems, where vectorized embeddings of users and items enable efficient and accurate collaborative filtering \[[25]()\]. While traditional methods such as matrix factorization and adaptive kNN have been widely used, they often lack direct optimization for personalized ranking \[[1](http://arxiv.org/abs/1205.2618)\]. Recent advances in deep learning have introduced more sophisticated approaches, such as Neural Collaborative Filtering (NCF), which leverages multi-layer perceptrons to model user-item interactions \[[2](http://arxiv.org/abs/1708.05031)\]. These models have shown significant improvements over earlier methods, particularly in capturing non-linear relationships \[[2](http://arxiv.org/abs/1708.05031)\].

Graph-based methods have also gained traction in recommendation systems, with models like LightGCN simplifying the design of Graph Convolution Networks (GCNs) by focusing on neighborhood aggregation \[[7](http://arxiv.org/abs/2002.02126)\]. LightGCN achieves substantial improvements over state-of-the-art GCN-based models like NGCF, demonstrating the effectiveness of a simpler architecture \[[7](http://arxiv.org/abs/2002.02126)\]. Similarly, Graph Convolutional Matrix Completion (GC-MC) has been proposed to address matrix completion from the perspective of link prediction on graphs, offering competitive performance on standard benchmarks \[[4](http://arxiv.org/abs/1706.02263)\].

The use of binary representations for efficient inference has been explored in several works. For example, HashNet introduces a novel deep architecture for learning binary hash codes directly from imbalanced similarity data, addressing the ill-posed gradient problem with a continuation method \[[8](http://arxiv.org/abs/1702.00758)\]. Candidate Generation with Binary Codes for Large-Scale Top-N Recommendation (CIGAR) further explores the use of binary embeddings for candidate retrieval, combining preference-preserving binary embeddings with real-valued ranking models to improve Top-N accuracy \[[9](http://arxiv.org/abs/1909.05475)\]. These methods highlight the potential of binary representations for reducing memory usage and computational overhead.

In the context of graph neural networks (GNNs), binary graph neural networks (BGNs) have been proposed to reduce model size and memory footprint by binarizing parameters and activations \[[11](http://arxiv.org/abs/2012.15823)\]. This approach enables significant speedups on embedded devices while maintaining acceptable performance. Additionally, Learning Binarized Graph Representations with Multi-faceted Quantization Reinforcement (BiGeaR) introduces a framework that retains representation informativeness during binarization, achieving up to 40% performance improvements over state-of-the-art quantization-based recommenders \[[12](http://arxiv.org/abs/2206.02115)\]. These works underscore the importance of carefully designing quantization strategies to minimize information loss.

Knowledge distillation has also been applied to GNNs, aiming to transfer knowledge from larger teacher models to smaller student models. For instance, Distilling Knowledge from Graph Convolutional Networks (DistillGCN)
## Research papers
### Outline
- [Traditional Recommendation Methods [2 papers]](#category-traditional-recommendation-methods)
- [Deep Learning in Recommender Systems [3 papers]](#category-deep-learning-in-recommender-systems)
- [Graph-Based Recommendation Models [9 papers]](#category-graph-based-recommendation-models)
- [Binary Representation Techniques [3 papers]](#category-binary-representation-techniques)
- [Binary Graph Neural Networks [2 papers]](#category-binary-graph-neural-networks)
- [Quantization Strategies for Embeddings [2 papers]](#category-quantization-strategies-for-embeddings)
- [Knowledge Distillation in GNNs [8 papers]](#category-knowledge-distillation-in-gnns)
- [Information Loss Mitigation Techniques [1 papers]](#category-information-loss-mitigation-techniques)

### <a id='category-traditional-recommendation-methods'></a>Traditional Recommendation Methods: 2 papers found.
Context: 
	Document 1: [Category]: «Traditional Recommendation Methods»
[Snippet]: «Item recommendation is the task of predicting a personalized ranking on a set
of items (e.g. websites, movies, products). In this paper, we investigate the
most common scenario with implicit feedback (e.g. clicks, purchases). There are
many methods for item recommendation from implicit feedback like matrix
factorization (MF) or adaptive knearest-neighbor (kNN). Even though these
methods are designed for the item prediction task of personalized ranking, none
of them is directly optimized for ranking. In this paper we present a generic
optimization criterion BPR-Opt for personalized ranking that is the maximum
posterior estimator derived from a Bayesian analysis of the problem. We also
provide a generic learning algorithm for optimizing models with respect to
BPR-Opt. The learning method is based on stochastic gradient descent with
bootstrap sampling. We show how to apply our method to two state-of-the-art
recommender models: matrix factorization and adaptive kNN. Our experiments
indicate that for the task of personalized ranking our optimization method
outperforms the standard learning techniques for MF and kNN. The results show
the importance of optimizing models for the right criterion.»
[_citation_number]: «1»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-06-03T11:11:43+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1609.02907)\]. Further details \[[6](http://arxiv.org/abs/2007.01764)\]\[[7](http://arxiv.org/abs/2002.02126)\]\[[8](http://arxiv.org/abs/1702.00758)\]\[[9](http://arxiv.org/abs/1909.05475)\]\[[10](http://arxiv.org/abs/1901.00596)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Learning vectorized embeddings is fundamental to many recommender systems for
user-item matching. To enable efficient online inference, representation
binarization, which embeds latent features into compact binary sequences, has
recently shown significant promise in optimizing both memory
|    | reference                                                                                   |   date | key idea/summary                                                                                                                                                                                 |
|----|---------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [BPR: Bayesian Personalized Ranking from Implicit Feedback](http://arxiv.org/abs/1205.2618) |    nan | The paper introduces BPR-Opt, a novel optimization criterion for personalized item recommendation from implicit feedback, which outperforms standard methods by directly optimizing for ranking. |
|  1 | [Discrete collaborative filtering]()                                                        |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                        |
### <a id='category-deep-learning-in-recommender-systems'></a>Deep Learning in Recommender Systems: 3 papers found.
Context: 
	Document 1: [Category]: «Deep Learning in Recommender Systems»
[Snippet]: «In recent years, deep neural networks have yielded immense success on speech
recognition, computer vision and natural language processing. However, the
exploration of deep neural networks on recommender systems has received
relatively less scrutiny. In this work, we strive to develop techniques based
on neural networks to tackle the key problem in recommendation -- collaborative
filtering -- on the basis of implicit feedback. Although some recent work has
employed deep learning for recommendation, they primarily used it to model
auxiliary information, such as textual descriptions of items and acoustic
features of musics. When it comes to model the key factor in collaborative
filtering -- the interaction between user and item features, they still
resorted to matrix factorization and applied an inner product on the latent
features of users and items. By replacing the inner product with a neural
architecture that can learn an arbitrary function from data, we present a
general framework named NCF, short for Neural network-based Collaborative
Filtering. NCF is generic and can express and generalize matrix factorization
under its framework. To supercharge NCF modelling with non-linearities, we
propose to leverage a multi-layer perceptron to learn the user-item interaction
function. Extensive experiments on two real-world datasets show significant
improvements of our proposed NCF framework over the state-of-the-art methods.
Empirical evidence shows that using deeper layers of neural networks offers
better recommendation performance.»
[_citation_number]: «2»

	Document 2: [Category]: «Deep Learning in Recommender Systems»
[Snippet]: «»
[_citation_number]: «20»

	Document 3: [Category]: «Deep Learning in Recommender Systems»
[Snippet]: «»
[_citation_number]: «25»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-06-03T11:11:43+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e
|    | reference                                                                                          |   date | key idea/summary                                                                                                                                                                                                                                                   |
|----|----------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Neural Collaborative Filtering](http://arxiv.org/abs/1708.05031)                                  |    nan | The paper introduces NCF, a neural network-based collaborative filtering framework that replaces traditional matrix factorization with a multi-layer perceptron to model user-item interactions, achieving significant improvements in recommendation performance. |
|  1 | [Deep neural networks for youtube recommendations]()                                               |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                          |
|  2 | [Learning binary codes with neural collaborative filtering for efficient recommendation systems]() |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                          |
### <a id='category-graph-based-recommendation-models'></a>Graph-Based Recommendation Models: 9 papers found.
Context: 
	Document 1: [Category]: «Graph-Based Recommendation Models»
[Snippet]: «We present a scalable approach for semi-supervised learning on graph-structured data that is based on an efficient variant of convolutional neural networks which operate directly on graphs. We motivate the choice of our convolutional architecture via a localized first-order approximation of spectral graph convolutions. Our model scales linearly in the number of graph edges and learns hidden layer representations that encode both local graph structure and features of nodes. In a number of experiments on citation networks and on a knowledge graph dataset we demonstrate that our approach outperforms related methods by a significant margin.»
[_citation_number]: «3»

	Document 2: [Category]: «Graph-Based Recommendation Models»
[Snippet]: «We consider matrix completion for recommender systems from the point of view of link prediction on graphs. Interaction data such as movie ratings can be represented by a bipartite user-item graph with labeled edges denoting observed ratings. Building on recent progress in deep learning on graph-structured data, we propose a graph auto-encoder framework based on differentiable message passing on the bipartite interaction graph. Our model shows competitive performance on standard collaborative filtering benchmarks. In settings where complimentary feature information or structured data such as a social network is available, our framework outperforms recent state-of-the-art methods.»
[_citation_number]: «4»

	Document 3: [Category]: «Graph-Based Recommendation Models»
[Snippet]: «Learning vector representations (aka. embeddings) of users and items lies at the core of modern recommender systems. Ranging from early matrix factorization to recently emerged deep learning based methods, existing efforts typically obtain a user's (or an item's) embedding by mapping from pre-existing features that describe the user (or the item), such as ID and attributes. We argue that an inherent drawback of such methods is that, the collaborative signal, which is latent in user-item interactions, is not encoded in the embedding process. As such, the resultant embeddings may not be sufficient to capture the collaborative filtering effect. In this work, we propose to integrate the user-item interactions -- more specifically the bipartite graph structure -- into the embedding process. We develop a new recommendation framework Neural Graph Collaborative Filtering (NGCF), which exploits the user-item graph structure by propagating embeddings on it. This leads to the expressive modeling of high-order connectivity in user-item graph, effectively injecting the collaborative signal into the embedding process in an explicit manner. We conduct
|    | reference                                                                                                            |   date | key idea/summary                                                                                                                                                                                                                                                                                   |
|----|----------------------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Semi-Supervised Classification with Graph Convolutional Networks](http://arxiv.org/abs/1609.02907)                  |    nan | The paper introduces a scalable semi-supervised learning approach for graph-structured data using an efficient convolutional neural network variant that operates directly on graphs and outperforms existing methods.                                                                             |
|  1 | [Graph Convolutional Matrix Completion](http://arxiv.org/abs/1706.02263)                                             |    nan | The paper proposes a graph auto-encoder framework for matrix completion in recommender systems, leveraging differentiable message passing on bipartite interaction graphs to achieve competitive performance and outperform state-of-the-art methods when additional structured data is available. |
|  2 | [Neural Graph Collaborative Filtering](http://arxiv.org/abs/1905.08108)                                              |    nan | NGCF is a new recommendation framework that integrates user-item interactions into the embedding process by propagating embeddings on a bipartite graph, enabling effective modeling of high-order connectivity and improving collaborative filtering performance.                                 |
|  3 | [Disentangled Graph Collaborative Filtering](http://arxiv.org/abs/2007.01764)                                        |    nan | DGCF disentangles user intents in collaborative filtering by modeling intent-aware interaction graphs and encouraging independence among intents, leading to more interpretable and effective representations.                                                                                     |
|  4 | [LightGCN: Simplifying and Powering Graph Convolution Network for
  Recommendation](http://arxiv.org/abs/2002.02126) |    nan | LightGCN simplifies the Graph Convolution Network (GCN) by removing non-essential components, retaining only neighborhood aggregation, and achieves significant performance improvements over existing GCN-based recommenders.                                                                     |
|  5 | [A Comprehensive Survey on Graph Neural Networks](http://arxiv.org/abs/1901.00596)                                   |    nan | This paper provides a comprehensive survey of graph neural networks (GNNs), categorizing them into four types and discussing their applications, benchmark datasets, and future research directions.                                                                                               |
|  6 | [Graph convolutional neural networks for web-scale recommender systems]()                                            |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                          |
|  7 | [Discrete personalized ranking for fast collaborative filtering from implicit feedback]()                            |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                          |
|  8 | [Learning to hash with GNNs for recommender systems]()                                                               |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                          |
### <a id='category-binary-representation-techniques'></a>Binary Representation Techniques: 3 papers found.
Context: 
	Document 1: [Category]: «Binary Representation Techniques»
[Snippet]: «Learning to hash has been widely applied to approximate nearest neighbor
search for large-scale multimedia retrieval, due to its computation efficiency
and retrieval quality. Deep learning to hash, which improves retrieval quality
by end-to-end representation learning and hash encoding, has received
increasing attention recently. Subject to the ill-posed gradient difficulty in
the optimization with sign activations, existing deep learning to hash methods
need to first learn continuous representations and then generate binary hash
codes in a separated binarization step, which suffer from substantial loss of
retrieval quality. This work presents HashNet, a novel deep architecture for
deep learning to hash by continuation method with convergence guarantees, which
learns exactly binary hash codes from imbalanced similarity data. The key idea
is to attack the ill-posed gradient problem in optimizing deep networks with
non-smooth binary activations by continuation method, in which we begin from
learning an easier network with smoothed activation function and let it evolve
during the training, until it eventually goes back to being the original,
difficult to optimize, deep network with the sign activation function.
Comprehensive empirical evidence shows that HashNet can generate exactly binary
hash codes and yield state-of-the-art multimedia retrieval performance on
standard benchmarks.»
[_citation_number]: «8»

	Document 2: [Category]: «Binary Representation Techniques»
[Snippet]: «Generating the Top-N recommendations from a large corpus is computationally
expensive to perform at scale. Candidate generation and re-ranking based
approaches are often adopted in industrial settings to alleviate efficiency
problems. However it remains to be fully studied how well such schemes
approximate complete rankings (or how many candidates are required to achieve a
good approximation), or to develop systematic approaches to generate
high-quality candidates efficiently. In this paper, we seek to investigate
these questions via proposing a candidate generation and re-ranking based
framework (CIGAR), which first learns a preference-preserving binary embedding
for building a hash table to retrieve candidates, and then learns to re-rank
the candidates using real-valued ranking models with a candidate-oriented
objective. We perform a comprehensive study on several large-scale real-world
datasets consisting of millions of users/items and hundreds of millions of
interactions. Our results show that CIGAR significantly boosts the Top-N
accuracy against state-of-the-art recommendation models, while reducing the
query time by orders of magnitude
|    | reference                                                                                                        |   date | key idea/summary                                                                                                                                                                                                                              |
|----|------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [HashNet: Deep Learning to Hash by Continuation](http://arxiv.org/abs/1702.00758)                                |    nan | HashNet is a novel deep learning architecture that addresses the ill-posed gradient problem in deep learning to hash by using a continuation method, enabling the direct learning of exact binary hash codes from imbalanced similarity data. |
|  1 | [Candidate Generation with Binary Codes for Large-Scale Top-N
  Recommendation](http://arxiv.org/abs/1909.05475) |    nan | CIGAR is a candidate generation and re-ranking framework that improves Top-N recommendation accuracy while significantly reducing query time by using preference-preserving embeddings and efficient re-ranking models.                       |
|  2 | [Similarity search in high dimensions via hashing]()                                                             |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                     |
### <a id='category-binary-graph-neural-networks'></a>Binary Graph Neural Networks: 2 papers found.
Context: 
	Document 1: [Category]: «Binary Graph Neural Networks»
[Snippet]: «Graph Neural Networks (GNNs) have emerged as a powerful and flexible
framework for representation learning on irregular data. As they generalize the
operations of classical CNNs on grids to arbitrary topologies, GNNs also bring
much of the implementation challenges of their Euclidean counterparts. Model
size, memory footprint, and energy consumption are common concerns for many
real-world applications. Network binarization allocates a single bit to
parameters and activations, thus dramatically reducing the memory requirements
(up to 32x compared to single-precision floating-point numbers) and maximizing
the benefits of fast SIMD instructions on modern hardware for measurable
speedups. However, in spite of the large body of work on binarization for
classical CNNs, this area remains largely unexplored in geometric deep
learning. In this paper, we present and evaluate different strategies for the
binarization of graph neural networks. We show that through careful design of
the models, and control of the training process, binary graph neural networks
can be trained at only a moderate cost in accuracy on challenging benchmarks.
In particular, we present the first dynamic graph neural network in Hamming
space, able to leverage efficient k-NN search on binary vectors to speed-up the
construction of the dynamic graph. We further verify that the binary models
offer significant savings on embedded devices. Our code is publicly available
on Github.»
[_citation_number]: «11»

	Document 2: [Category]: «Binary Graph Neural Networks»
[Snippet]: «»
[_citation_number]: «28»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-06-03T11:11:43+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1609.02907)\]. Further details \[[6](http://arxiv.org/abs/2007.01764)\]\[[7](http://arxiv.org/abs/2002.02126)\]\[[8](http://arxiv.org/abs/1702.00758)\]\[[9](http://arxiv.org/abs/1909.05475)\]\[[10](http://arxiv.org/abs/1901.00596)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do
|    | reference                                                       |   date | key idea/summary                                                                                                                                                                                                                                      |
|----|-----------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Binary Graph Neural Networks](http://arxiv.org/abs/2012.15823) |    nan | This paper introduces and evaluates strategies for binarizing graph neural networks, demonstrating that binary models can achieve moderate accuracy loss while offering significant memory and computational savings, especially on embedded devices. |
|  1 | [Bi-gcn: Binary graph convolutional network]()                  |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                             |
### <a id='category-quantization-strategies-for-embeddings'></a>Quantization Strategies for Embeddings: 2 papers found.
Context: 
	Document 1: [Category]: «Quantization Strategies for Embeddings»
[Snippet]: «Learning vectorized embeddings is at the core of various recommender systems
for user-item matching. To perform efficient online inference, representation
quantization, aiming to embed the latent features by a compact sequence of
discrete numbers, recently shows the promising potentiality in optimizing both
memory and computation overheads. However, existing work merely focuses on
numerical quantization whilst ignoring the concomitant information loss issue,
which, consequently, leads to conspicuous performance degradation. In this
paper, we propose a novel quantization framework to learn Binarized Graph
Representations for Top-K Recommendation (BiGeaR). BiGeaR introduces
multi-faceted quantization reinforcement at the pre-, mid-, and post-stage of
binarized representation learning, which substantially retains the
representation informativeness against embedding binarization. In addition to
saving the memory footprint, BiGeaR further develops solid online inference
acceleration with bitwise operations, providing alternative flexibility for the
realistic deployment. The empirical results over five large real-world
benchmarks show that BiGeaR achieves about 22%~40% performance improvement over
the state-of-the-art quantization-based recommender system, and recovers about
95%~102% of the performance capability of the best full-precision counterpart
with over 8x time and space reduction.»
[_citation_number]: «12»

	Document 2: [Category]: «Quantization Strategies for Embeddings»
[Snippet]: «»
[_citation_number]: «27»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-06-03T11:11:43+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1609.02907)\]. Further details \[[6](http://arxiv.org/abs/2007.01764)\]\[[7](http://arxiv.org/abs/2002.02126)\]\[[8](http://arxiv.org/abs/1702.00758)\]\[[9](http://arxiv.org/abs/1909.05475)\]\[[10](http://arxiv.org/abs/1901.00596)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use
|    | reference                                                                                                                                            |   date | key idea/summary                                                                                                                                                                                                                                                         |
|----|------------------------------------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Learning Binarized Graph Representations with Multi-faceted Quantization
  Reinforcement for Top-K Recommendation](http://arxiv.org/abs/2206.02115) |    nan | BiGeaR proposes a novel quantization framework for learning binarized graph representations in recommender systems, achieving significant performance improvements and efficient online inference through multi-stage quantization reinforcement and bitwise operations. |
|  1 | [Towards low-loss 1-bit quantization of user-item representations for top-k recommendation]()                                                        |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                |
### <a id='category-knowledge-distillation-in-gnns'></a>Knowledge Distillation in GNNs: 8 papers found.
Knowledge distillation has emerged as a powerful technique for improving the efficiency and performance of graph neural networks (GNNs), particularly in resource-constrained environments. This approach involves transferring knowledge from a complex, high-capacity teacher model to a smaller, more deployable student model. Early work focused on convolutional neural networks (CNNs), but recent studies have extended this idea to GNNs, where the challenge lies in preserving the topological semantics of graph data \[[15](http://arxiv.org/abs/2003.10477)\]. Researchers have proposed various methods to address this, such as the Local Structure Preserving (LSP) loss, which aligns local structural relationships between teacher and student node embeddings \[[16](http://arxiv.org/abs/2111.04964)\]. More recently, Graph Contrastive Representation Distillation (G-CRD) has been introduced, leveraging contrastive learning to preserve global topology by aligning student embeddings with those of the teacher in a shared representation space \[[16](http://arxiv.org/abs/2111.04964)\]. Additionally, efforts have been made to integrate both individual and relational knowledge during distillation, using graph-based embeddings to capture holistic information \[[17](http://arxiv.org/abs/2108.05507)\]. These approaches aim to balance the preservation of local and global relationships, ensuring that the compressed student model retains the essential features of the original teacher model \[[16](http://arxiv.org/abs/2111.04964)\]. Furthermore, some studies have focused on eliminating the need for a well-optimized teacher model by introducing frameworks like FreeKD, which uses reinforcement learning to enable knowledge transfer between two shallower GNNs \[[18](http://arxiv.org/abs/2206.06561)\]. These advancements highlight the growing interest in distillation techniques for GNNs, aiming to enhance model efficiency without compromising performance \[[15](http://arxiv.org/abs/2003.10477)\]\[[16](http://arxiv.org/abs/2111.04964)\]\[[17](http://arxiv.org/abs/2108.05507)\]\[[18](http://arxiv.org/abs/2206.06561)\].
|    | reference                                                                                                  |   date | key idea/summary                                                                                                                                                                                                                                                                                |
|----|------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Distilling the Knowledge in a Neural Network](http://arxiv.org/abs/1503.02531)                            |    nan | The paper introduces a method to compress knowledge from an ensemble of models into a single model, achieving improved performance and efficiency, particularly in applications like MNIST and commercial acoustic systems.                                                                     |
|  1 | [Knowledge Distillation on Graphs: A Survey](http://arxiv.org/abs/2302.00219)                              |    nan | This paper presents a survey on knowledge distillation for graph neural networks (GNNs), focusing on challenges, categorization of existing works, and future research directions to improve model compression and performance.                                                                 |
|  2 | [Distilling Knowledge from Graph Convolutional Networks](http://arxiv.org/abs/2003.10477)                  |    nan | This paper introduces the first dedicated approach for knowledge distillation in graph convolutional networks (GCNs), enabling topology-aware knowledge transfer through a local structure preserving module.                                                                                   |
|  3 | [On Representation Knowledge Distillation for Graph Neural Networks](http://arxiv.org/abs/2111.04964)      |    nan | This paper introduces Graph Contrastive Representation Distillation (G-CRD), a method for knowledge distillation in graph neural networks that preserves global topology through contrastive learning, outperforming existing methods in boosting lightweight GNNs' performance and robustness. |
|  4 | [Distilling Holistic Knowledge with Graph Neural Networks](http://arxiv.org/abs/2108.05507)                |    nan | The paper proposes a Knowledge Distillation method that integrates individual and relational knowledge by modeling holistic knowledge through a graph-based embedding, achieving effective student network learning.                                                                            |
|  5 | [FreeKD: Free-direction Knowledge Distillation for Graph Neural Networks](http://arxiv.org/abs/2206.06561) |    nan | FreeKD is a novel reinforcement learning-based knowledge distillation framework for GNNs that enables knowledge transfer between two shallower networks without requiring a pre-trained deeper teacher model, achieving competitive or better performance than traditional KD methods.          |
|  6 | [Knowledge distillation improves graph structure augmentation for graph neural networks]()                 |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                       |
|  7 | [Fine-grained learning behavior-oriented knowledge distillation for graph neural networks]()               |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                       |
### <a id='category-information-loss-mitigation-techniques'></a>Information Loss Mitigation Techniques: 1 papers found.
Context: 
	Document 1: [Category]: «Information Loss Mitigation Techniques»
[Snippet]: «In hash-based image retrieval systems, degraded or transformed inputs usually generate different codes from the original, deteriorating the retrieval accuracy. To mitigate this issue, data augmentation can be applied during training. However, even if augmented samples of an image are similar in real feature space, the quantization can scatter them far away in Hamming space. This results in representation discrepancies that can impede training and degrade performance. In this work, we propose a novel self-distilled hashing scheme to minimize the discrepancy while exploiting the potential of augmented data. By transferring the hash knowledge of the weakly-transformed samples to the strong ones, we make the hash code insensitive to various transformations. We also introduce hash proxy-based similarity learning and binary cross entropy-based quantization loss to provide fine quality hash codes. Ultimately, we construct a deep hashing framework that not only improves the existing deep hashing approaches, but also achieves the state-of-the-art retrieval results. Extensive experiments are conducted and confirm the effectiveness of our work.»
[_citation_number]: «19»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-06-03T11:11:43+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1609.02907)\]. Further details \[[6](http://arxiv.org/abs/2007.01764)\]\[[7](http://arxiv.org/abs/2002.02126)\]\[[8](http://arxiv.org/abs/1702.00758)\]\[[9](http://arxiv.org/abs/1909.05475)\]\[[10](http://arxiv.org/abs/1901.00596)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Learning vectorized embeddings is fundamental to many recommender systems for user-item matching. To enable efficient online inference, representation binarization, which embeds latent features into compact binary sequences, has recently shown significant promise in optimizing both memory usage and computational overhead. However, existing approaches primarily focus on numerical quantization, neglecting the associated information loss, which often results in noticeable performance degradation. To address these issues, we study the problem of graph representation binar
|    | reference                                                                     |   date | key idea/summary                                                                                                                                                                                                                                       |
|----|-------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Deep Hash Distillation for Image Retrieval](http://arxiv.org/abs/2112.08816) |    nan | The paper proposes a self-distilled hashing scheme to improve hash code robustness against image transformations by transferring hash knowledge from weakly-transformed to strongly-transformed samples, achieving state-of-the-art retrieval results. |
