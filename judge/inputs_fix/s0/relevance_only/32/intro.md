## Related Works

Recent research has focused on understanding how feature representations evolve across layers in large language models (LLMs), aiming to improve interpretability and robustness \[[1](http://arxiv.org/abs/2411.09539)\]. While several studies have identified critical layers linked to specific functions or behaviors, these approaches often rely on data-dependent analyses of fine-tuned models, limiting their applicability to post-hoc settings \[[1](http://arxiv.org/abs/2411.09539)\]. In contrast, our work introduces a data-oblivious approach to identify intrinsic critical layers in pre-fine-tuned LLMs by analyzing representation dynamics via Centered Kernel Alignment (CKA) \[[1](http://arxiv.org/abs/2411.09539)\]. This method enables the identification of critical layers without requiring fine-tuning, offering a more generalizable framework \[[1](http://arxiv.org/abs/2411.09539)\].

The importance of analyzing representation dynamics during fine-tuning has been explored in several studies. For instance, \[[6](http://arxiv.org/abs/2502.16722)\] investigates how fine-tuning affects the representation space of pre-trained models, showing that certain layers undergo significant shifts, which are closely correlated with performance changes. Similarly, \[[7](http://arxiv.org/abs/2402.16363)\] highlights the role of layer-specific adaptations in enhancing model performance on downstream tasks, emphasizing the need for targeted fine-tuning strategies. Our work builds on these findings by demonstrating that layers with significant representation shifts are also most affected during fine-tuning, a pattern that holds consistently across tasks for a given model \[[1](http://arxiv.org/abs/2411.09539)\].

Further, our spectral analysis reveals that these shifts are driven by changes in the top principal components, which encode semantic transitions from rationales to conclusions \[[1](http://arxiv.org/abs/2411.09539)\]. This insight aligns with prior work on the role of principal components in capturing semantic information \[[8](http://arxiv.org/abs/2210.05643)\]. Additionally, \[[9](http://arxiv.org/abs/2501.05032)\] explores how layer-specific adaptations can improve domain adaptation, suggesting that fine-tuning critical layers leads to greater loss reduction compared to non-critical layers. Our findings support this by showing that fine-tuning critical layers significantly improves performance in domain adaptation scenarios \[[1](http://arxiv.org/abs/2411.09539)\].

In the context of backdoor defense, \[[10](http://arxiv.org/abs/2402.11651)\] demonstrates that freezing critical layers can reduce attack success rates by up to 40%, highlighting the importance of layer-specific strategies in enhancing model security. Our work extends this by showing that identifying critical layers in pre-fine-tuned models can enable more effective and efficient backdoor defense mechanisms \[[1](http://arxiv.org/abs/2411.09539)\].

In summary, our approach contributes to the growing body of research on understanding and leveraging layer-specific adaptations in LLMs. By introducing a data-oblivious method for identifying critical layers, we provide a more generalizable and efficient framework for improving model performance and robustness across various tasks and settings \[[1](http://arxiv.org/abs/2411.09539)\].

References:  
\[[1](http://arxiv.org/abs/2411.09539)\] Document 6  
\[[6](http://arxiv.org/abs/2502.16722)\] Document 5  
\[[7](http://arxiv.org/abs/2402.16363)\] Document 5  
\[[8](http://arxiv.org/abs/2210.05643)\] Document 8  
\[[9](http://arxiv.org/abs/2501.05032)\] Document 5  
\[[10](http://arxiv.org/abs/2402.11651)\] Document 13
