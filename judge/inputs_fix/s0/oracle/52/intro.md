## Related Works

Dense retrievers have become a cornerstone in open-domain question answering (ODQA) systems, leveraging pre-trained language models (e.g., BERT, LLaMA) to encode text into dense vector representations that can be compared via similarity metrics such as cosine similarity \[[1](http://arxiv.org/abs/2004.04906)\]. Traditional sparse retrieval methods, such as TF-IDF or BM25, have been widely used but are increasingly being supplanted by dense retrieval approaches that offer superior performance \[[1](http://arxiv.org/abs/2004.04906)\]. This shift is driven by the ability of dense retrievers to capture semantic relationships between queries and passages more effectively \[[1](http://arxiv.org/abs/2004.04906)\].

The development of dense retrievers has been closely tied to advancements in pre-trained language models and contrastive learning. Sentence-BERT (SBERT) was introduced as a modification of BERT to generate sentence embeddings that can be compared using cosine similarity, significantly reducing computational overhead compared to standard BERT \[[2](http://arxiv.org/abs/1908.10084)\]. Similarly, SimCSE extends this idea by using contrastive learning to generate high-quality sentence embeddings, achieving state-of-the-art results on semantic textual similarity (STS) tasks \[[3](http://arxiv.org/abs/2104.08821)\]. These methods highlight the importance of fine-tuning pre-trained models to adapt them to specific retrieval tasks \[[2](http://arxiv.org/abs/1908.10084)\]\[[3](http://arxiv.org/abs/2104.08821)\].

The MS MARCO dataset has played a critical role in benchmarking dense retrievers, providing a large-scale, human-generated dataset of questions and corresponding answers \[[4](http://arxiv.org/abs/1611.09268)\]. This dataset has enabled researchers to evaluate the effectiveness of different retrieval strategies, including passage ranking and answer extraction \[[4](http://arxiv.org/abs/1611.09268)\]. The dataset's real-world nature and scale make it particularly valuable for assessing the generalization capabilities of dense retrievers \[[4](http://arxiv.org/abs/1611.09268)\].

Recent work has also explored the role of pre-training versus fine-tuning in dense retrievers. A study using the Dense Passage Retrieval (DPR) framework found that retrieval knowledge is primarily acquired during pre-training, with fine-tuning mainly adjusting neuron activations rather than reorganizing knowledge \[[1](http://arxiv.org/abs/2004.04906)\]. This finding was tested across different architectures, including encoder-only BERT and decoder-only LLaMA, as well as different pooling strategies, such as CLS token versus mean pooling \[[1](http://arxiv.org/abs/2004.04906)\]. The results suggest that while pre-training is foundational, fine-tuning can still play a role in optimizing retrieval performance \[[1](http://arxiv.org/abs/2004.04906)\].

In addition, the Contriever and RePLAMA models have introduced new approaches to dense retrieval, with Contriever being a fully unsupervised method and RePLAMA utilizing a decoder-based architecture \[[5]()\]\[[6]()\]. These models further demonstrate the flexibility of dense retrieval frameworks and their potential to improve performance in various settings \[[5]()\]\[[6]()\].

PromptReps has also contributed to the field by enhancing dense retrieval through prompt-based representations, offering a novel way to fine-tune models without requiring extensive labeled data \[[7]()\]. This approach aligns with the broader trend of using pre-trained models with minimal additional training to achieve competitive performance \[[7]()\].

Natural Questions, another benchmark dataset, has been used to evaluate the effectiveness of dense retrievers in real-world scenarios \[[8]()\]. This dataset is particularly useful for assessing the ability of models to understand and answer complex, open-ended questions \[[8]()\].

In summary, the field of dense retrieval has seen significant advancements, driven by improvements in pre-trained models, contrastive learning, and large-scale datasets. These developments have enabled more accurate and efficient retrieval systems, which are essential for modern open-domain question answering \[[1](http://arxiv.org/abs/2004.04906)\]\[[2](http://arxiv.org/abs/1908.10084)\]\[[3](http://arxiv.org/abs/2104.08821)\]\[[4](http://arxiv.org/abs/1611.09268)\]\[[5]()\]\[[6]()\]\[[7]()\]\[[8]()\].

References:  
\[[1](http://arxiv.org/abs/2004.04906)\] Dense Passage Retrieval for Open-Domain Question Answering  
\[[2](http://arxiv.org/abs/1908.10084)\] Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks  
\[[3](http://arxiv.org/abs/2104.08821)\] SimCSE: Simple Contrastive Learning of Sentence Embeddings  
\[[4](http://arxiv.org/abs/1611.09268)\] MS MARCO: A Human Generated MAchine Reading COmprehension Dataset  
\[[5]()\] Contriever: A Fully Unsupervised Dense Retriever  
\[[6]()\] RePLAMA: A Decoder-based Dense Retriever for Open-Domain Question Answering  
\[[7]()\] PromptReps: Enhancing Dense Retrieval with Prompt-based Representations  
\[[8]()\] Natural Questions: A Benchmark for Question Answering
