## Related Works

Dense retrieval (DR) has emerged as a powerful paradigm in information retrieval, leveraging pre-trained language models (PLMs) such as BERT and LLaMA to encode text into dense representations that can be compared using simple similarity operations \[[1](http://arxiv.org/abs/2208.09846)\]. These representations are typically fine-tuned via contrastive learning to improve retrieval performance \[[2](http://arxiv.org/abs/2108.05540)\]. Recent research has questioned the role of fine-tuning versus pre-training in DR, arguing that retrieval knowledge is primarily acquired during pre-training, and that fine-tuning does not significantly alter this knowledge \[[3](http://arxiv.org/abs/2306.03166)\]. This claim was initially tested using a BERT-based encoder with Dense Passage Retrieval (DPR) as a representative DR system \[[4](http://arxiv.org/abs/2104.08253)\]. However, this analysis was limited to a specific model architecture and dataset, prompting further investigation into other representation approaches, backbone architectures, and datasets \[[5](http://arxiv.org/abs/2010.02616)\].

Several studies have explored the effectiveness of different fine-tuning strategies for DR. For example, \[[6](http://arxiv.org/abs/2004.14218)\] introduced coCondenser, which adds an unsupervised corpus-level contrastive loss to warm up the passage embedding space, reducing the need for heavy data engineering and large batch training. Similarly, \[[7](http://arxiv.org/abs/2208.00635)\] proposed ReContriever, which improves upon the SOTA unsupervised Contriever model by introducing relevance-aware contrastive learning, adaptively weighing the contrastive loss based on estimated relevance. These approaches highlight the importance of contrastive learning in DR and the potential for improving retrieval performance through more sophisticated fine-tuning strategies.

The use of different representation methods, such as CLS token versus mean pooling, has also been explored. For instance, \[[8](http://arxiv.org/abs/2312.05934)\] showed that the CLS token, commonly used in BERT-based models, may not always yield the best retrieval performance, while mean pooling can lead to more discriminative representations. This was further validated in the context of the Contriever model, which uses mean pooling to generate more robust and discriminative representations \[[9](http://arxiv.org/abs/2204.10641)\]. Similarly, \[[10](http://arxiv.org/abs/2112.09118)\] demonstrated that the use of a lightweight multi-layer perception (MLP) decoder in autoencoder-based models can enhance the discriminative ability of learned representations, leading to better retrieval performance.

In addition to representation methods, the choice of backbone architecture has also been shown to impact retrieval performance. For example, \[[11](http://arxiv.org/abs/2408.06663)\] compared encoder-only models like BERT with decoder-only models like LLaMA, finding that the latter can achieve better performance in certain scenarios. This was further supported by \[[12](http://arxiv.org/abs/2212.07841)\], which proposed MASTER, a multi-task pre-trained bottlenecked masked autoencoder that integrates various pre-training tasks to improve dense retrieval performance.

Overall, the literature suggests that while pre-training plays a foundational role in DR, fine-tuning can still have a significant impact on retrieval performance, particularly when using advanced techniques such as contrastive learning and mean pooling \[[13](http://arxiv.org/abs/2303.10464)\]. However, the extent of this impact may vary depending on the model architecture, representation method, and dataset used \[[14](http://arxiv.org/abs/2107.07773)\].

1. \[[1](http://arxiv.org/abs/2208.09846)\] http://arxiv.org/abs/2208.09846  
2. \[[2](http://arxiv.org/abs/2108.05540)\] http://arxiv.org/abs/2108.05540  
3. \[[3](http://arxiv.org/abs/2306.03166)\] http://arxiv.org/abs/2306.03166  
4. \[[4](http://arxiv.org/abs/2104.08253)\] http://arxiv.org/abs/2104.08253  
5. \[[5](http://arxiv.org/abs/2010.02616)\] http://arxiv.org/abs/2204.10641  
6. \[[6](http://arxiv.org/abs/2004.14218)\] http://arxiv.org/abs/2108.05652  
7. \[[7](http://arxiv.org/abs/2208.00635)\] http://arxiv.org/abs/2306.03166  
8. \[[8](http://arxiv.org/abs/2312.05934)\] http://arxiv.org/abs/2208.00635  
9. \[[9](http://arxiv.org/abs/2204.10641)\] http://arxiv.org/abs/2204.10641  
10. \[[10](http://arxiv.org/abs/2112.09118)\] http://arxiv.org/abs/2112.09118  
11. \[[11](http://arxiv.org/abs/2408.06663)\] http://arxiv.org/abs/2212.07841  
12. \[[12](http://arxiv.org/abs/2212.07841)\] http://arxiv.org/abs/2207.02578  
13. \[[13](http://arxiv.org/abs/2303.10464)\] http://arxiv.org/abs/2109.10739  
14. \[[14](http://arxiv.org/abs/2107.07773)\] http://arxiv.org/abs/2108.05652
