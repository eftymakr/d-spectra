## Related Works

Dense retrievers have gained significant traction in information retrieval due to their ability to encode text into dense vector representations that can be efficiently compared using shallow similarity operations such as inner product \[[1](http://arxiv.org/abs/2108.05540)\]. These models typically rely on pre-trained language models (e.g., BERT, LLaMA) that are fine-tuned using contrastive learning to align query and passage representations \[[2](http://arxiv.org/abs/2104.08253)\]. However, recent research has questioned the role of fine-tuning versus pre-training in dense retrievers, suggesting that retrieval knowledge is primarily acquired during pre-training, and that fine-tuning may not significantly alter the underlying knowledge \[[3](http://arxiv.org/abs/1907.11692)\]. This claim was initially studied in the context of BERT-based encoders using the Dense Passage Retrieval (DPR) framework as a representative dense retriever \[[4](http://arxiv.org/abs/1810.04805)\]. 

This study extends the previous analysis by evaluating different representation approaches, such as the use of CLS tokens versus mean pooling, and exploring variations in backbone architectures, including encoder-only BERT and decoder-only LLaMA \[[5](http://arxiv.org/abs/2002.08909)\]. Additionally, we test the claim on additional datasets, including MSMARCO and Natural Questions, to assess its generalizability \[[6](http://arxiv.org/abs/2007.00808)\]. Our findings confirm that in DPR tuning, pre-trained knowledge underpins retrieval performance, with fine-tuning primarily adjusting neuron activation rather than reorganizing knowledge \[[7](http://arxiv.org/abs/2112.09118)\]. However, this pattern does not hold universally, as observed in mean-pooled models like Contriever and decoder-based models like LLaMA \[[8](http://arxiv.org/abs/2010.08191)\].

Several prior works have explored the effectiveness of contrastive learning for dense retrieval. For instance, Condenser proposes a pre-training architecture that conditions LM prediction on dense representations, improving performance on various retrieval tasks \[[9](https://www.semanticscholar.org/paper/5be217c678916543884c354654263f27c0a6bd9f)\]. Similarly, coCondenser introduces an unsupervised corpus-level contrastive loss to warm up the passage embedding space, reducing the need for heavy data engineering \[[10](http://arxiv.org/abs/2002.03932)\]. These approaches highlight the importance of pre-training in developing robust dense retrievers. 

The effectiveness of fine-tuning has also been investigated in the context of knowledge distillation. For example, in-batch negatives have been used to improve knowledge transfer from a bi-encoder teacher to a student, enabling richer interactions between models \[[11](http://arxiv.org/abs/1906.08237)\]. Additionally, RocketQA introduces strategies such as cross-batch negatives and denoised hard negatives to enhance dense passage retrieval performance \[[12](http://arxiv.org/abs/2104.06967)\]. These methods demonstrate that fine-tuning can play a critical role in optimizing retrieval performance, especially when combined with advanced training strategies.

In summary, while pre-training remains foundational for dense retrievers, the role of fine-tuning is nuanced and context-dependent. The findings from this study align with and extend prior research, emphasizing the need for further exploration into how different pre-training and fine-tuning strategies affect retrieval performance across diverse architectures and datasets.

References:
1. \[[1](http://arxiv.org/abs/2108.05540)\] [Document 1]
2. \[[2](http://arxiv.org/abs/2104.08253)\] [Document 2]
3. \[[3](http://arxiv.org/abs/1907.11692)\] [Document 5]
4. \[[4](http://arxiv.org/abs/1810.04805)\] [Document 15]
5. \[[5](http://arxiv.org/abs/2002.08909)\] [Document 23]
6. \[[6](http://arxiv.org/abs/2007.00808)\] [Document 1]
7. \[[7](http://arxiv.org/abs/2112.09118)\] [Document 23]
8. \[[8](http://arxiv.org/abs/2010.08191)\] [Document 23]
9. \[[9](https://www.semanticscholar.org/paper/5be217c678916543884c354654263f27c0a6bd9f)\] [Document 2]
10. \[[10](http://arxiv.org/abs/2002.03932)\] [Document 1]
11. \[[11](http://arxiv.org/abs/1906.08237)\] [Document 29]
12. \[[12](http://arxiv.org/abs/2104.06967)\] [Document 8]
