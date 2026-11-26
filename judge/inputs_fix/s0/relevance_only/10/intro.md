## Related Works

Multi-token prediction (MTP) has emerged as a promising pre-training objective for language models, offering potential improvements in downstream performance, inference speed, and training efficiency \[[2](http://arxiv.org/abs/2404.19737)\]. Unlike next-token prediction (NTP), which predicts only the immediate next token, MTP predicts multiple future tokens at each step, often using multiple prediction heads \[[2](http://arxiv.org/abs/2404.19737)\]. This approach has been shown to enhance generative capabilities, particularly for large models \[[2](http://arxiv.org/abs/2404.19737)\]. However, smaller language models (SLMs) face challenges in effectively leveraging MTP, as prior work indicates \[[1](http://arxiv.org/abs/2505.17505)\]. To address this, we propose a curriculum learning strategy for MTP training, exploring forward and reverse curricula \[[1](http://arxiv.org/abs/2505.17505)\].

Curriculum learning has been widely studied in various domains, including natural language understanding \[[5](https://www.semanticscholar.org/paper/2d315208dd88eed245dc4ae1ae398af75aa291f8)\], neural machine translation \[[7](http://arxiv.org/abs/1903.09848)\], and reinforcement learning \[[10](http://arxiv.org/abs/1812.00285)\]. In natural language understanding, curriculum learning has been shown to improve performance by arranging training examples in an easy-to-difficult order \[[5](https://www.semanticscholar.org/paper/2d315208dd88eed245dc4ae1ae398af75aa291f8)\]. Similarly, in neural machine translation, curriculum learning has been used to reduce training time and improve performance by filtering training samples based on difficulty and model competence \[[7](http://arxiv.org/abs/1903.09848)\]. These approaches align with our forward curriculum, which gradually increases the complexity of the pre-training objective from NTP to MTP \[[1](http://arxiv.org/abs/2505.17505)\].

In reinforcement learning, curriculum learning has been applied to automatically select a sequence of tasks to accelerate learning of a complex target task \[[10](http://arxiv.org/abs/1812.00285)\]. This concept is closely related to our reverse curriculum, which starts with MTP and gradually reduces complexity to NTP \[[1](http://arxiv.org/abs/2505.17505)\]. The effectiveness of curriculum learning in these domains suggests that similar strategies could benefit MTP training for SLMs \[[1](http://arxiv.org/abs/2505.17505)\].

The benefits of MTP extend beyond training efficiency. For example, speculative decoding, a technique that accelerates inference by predicting multiple tokens in parallel, has been shown to improve inference speed for large models \[[13](http://arxiv.org/abs/2401.07851)\]. While speculative decoding is not directly related to curriculum learning, it highlights the importance of efficient decoding strategies in language model inference \[[13](http://arxiv.org/abs/2401.07851)\].

In addition to MTP, other methods have explored alternative approaches to improve language model performance. For instance, Future Token Prediction (FTP) introduces a novel pretraining method that generates embedding vectors capturing the overall meaning of longer sequences of future text \[[6](http://arxiv.org/abs/2410.18160)\]. This approach improves topic coherence and text classification performance compared to standard GPT models \[[6](http://arxiv.org/abs/2410.18160)\]. Similarly, MuToR introduces a method that interleaves learnable register tokens into the input sequence to support multi-token prediction \[[3](http://arxiv.org/abs/2505.10518)\]. MuToR is particularly well-suited for supervised fine-tuning and parameter-efficient fine-tuning (PEFT) \[[3](http://arxiv.org/abs/2505.10518)\].

Overall, the related works highlight the growing interest in multi-token prediction and curriculum learning for improving language model performance. Our work builds on these advancements by proposing a curriculum learning strategy for MTP training, with promising results for SLMs \[[1](http://arxiv.org/abs/2505.17505)\].

### References

1. \[[1](http://arxiv.org/abs/2505.17505)\] https://arxiv.org/abs/2404.19737  
2. \[[2](http://arxiv.org/abs/2404.19737)\] https://arxiv.org/abs/2404.19737  
3. \[[3](http://arxiv.org/abs/2505.10518)\] https://arxiv.org/abs/2505.10518  
4. \[[4](http://arxiv.org/abs/2407.10194)\] https://arxiv.org/abs/2407.10194  
5. \[[5](https://www.semanticscholar.org/paper/2d315208dd88eed245dc4ae1ae398af75aa291f8)\] https://www.semanticscholar.org/paper/2d315208dd88eed245dc4ae1ae398af75aa291f8  
6. \[[6](http://arxiv.org/abs/2410.18160)\] https://arxiv.org/abs/2410.18160  
7. \[[7](http://arxiv.org/abs/1903.09848)\] https://arxiv.org/abs/1903.09848  
8. \[[8](http://arxiv.org/abs/1506.03099)\] https://arxiv.org/abs/1506.03099  
9. \[[9](http://arxiv.org/abs/2504.09710)\] https://arxiv.org/abs/2504.09710  
10. \[[10](http://arxiv.org/abs/1812.00285)\] https://arxiv.org/abs/1812.00285  
11. \[[11](http://arxiv.org/abs/2202.09061)\] https://arxiv.org/abs/2202.09061  
12. \[[12](http://arxiv.org/abs/1704.03003)\] https://arxiv.org/abs/1704.03003  
13. \[[13](http://arxiv.org/abs/2401.07851)\] https://arxiv.org/abs/2401.07851
