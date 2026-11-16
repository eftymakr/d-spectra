## Related Works

Collaborative filtering has seen significant advancements through the integration of graph-based methods and representation learning. Early approaches, such as matrix factorization and its variants, often failed to capture complex user-item interactions, leading to suboptimal performance . More recently, graph neural networks (GNNs) have been leveraged to model these interactions, as seen in Neural Graph Collaborative Filtering (NGCF) , which explicitly captures high-order connectivity in user-item graphs. While NGCF improved performance, it still faced challenges in handling sparsity and over-smoothing .

To address these limitations, researchers have explored binarization techniques to reduce computational overhead while preserving essential information. For instance, PB-LLM \[[Zekun Li' 2020-11-13](http://arxiv.org/abs/2011.06807v2)\] introduced a partially binarized approach for large language models, maintaining linguistic reasoning capacity by selectively binarizing weights. Similarly, Binarized Collaborative Filtering \[[Jianing Sun' 2020-01-01](http://arxiv.org/abs/2001.00267v1)\] utilized graph convolutional networks to distill ranking information into binary representations, improving efficiency in online recommendations. However, these methods often neglected the information loss inherent in binarization, which could degrade model performance \[[Jianing Sun' 2020-01-01](http://arxiv.org/abs/2001.00267v1)\].

Recent work has also focused on the integration of graph signal processing (GSP) with collaborative filtering. GSPRec  proposed a framework that incorporates item-item proximity derived from user interaction ordering, enhancing the spectral representation of items. This approach improved the model's ability to capture both local and global structures, leading to better recommendation performance . Another notable contribution is the use of graph neural networks for collaborative filtering, as seen in Multi-Graph Convolution Collaborative Filtering (Multi-GCCF) , which explicitly models multiple graphs to capture diverse user-item interactions .

In addition, the problem of information loss during binarization has been addressed in several studies. For example, Loss-aware Binarization of Deep Networks  proposed a proximal Newton algorithm that directly minimizes the loss with respect to binarized weights, improving the robustness of binarized models. This approach was validated on both feedforward and recurrent networks, demonstrating its effectiveness in preserving model performance . Similarly, near-lossless binarization of word embeddings  was explored, where binary embeddings were generated while preserving semantic information, achieving a minimal accuracy loss of around 2% .

Furthermore, the use of graph-based methods for collaborative filtering has been extended to handle heterogeneous data. Heterogeneous Graph Collaborative Filtering (HGCF)  incorporated user-user and item-item edges, enabling the model to capture both interaction and similarity signals. This approach alleviated the sparsity issue and improved recommendation accuracy by leveraging richer graph structures . Similarly, Disentangled Graph Collaborative Filtering (DGCF)  focused on disentangling user intents by modeling distribution over intents for each user-item interaction, leading to more interpretable and accurate representations .

In summary, while existing methods have made strides in improving collaborative filtering through graph-based approaches and binarization, they often overlook the information loss during these processes. Our work builds on these prior efforts, introducing BiGeaR++ to explicitly mitigate information loss during binarization, leading to improved performance and state-of-the-art results.

References:
1. \[[Jianing Sun' 2020-01-01](http://arxiv.org/abs/2001.00267v1)\] Binarized Collaborative Filtering with Distilling Graph Convolutional Networks
2.  Collaborative Filtering with Graph-based Implicit Feedback
3.  Neural Graph Collaborative Filtering
4. \[[Zekun Li' 2020-11-13](http://arxiv.org/abs/2011.06807v2)\] PB-LLM: Partially Binarized Large Language Models
5.  Loss-aware Binarization of Deep Networks
6.  Near-lossless Binarization of Word Embeddings
7.  Heterogeneous Graph Collaborative Filtering
8.  Disentangled Graph Collaborative Filtering
