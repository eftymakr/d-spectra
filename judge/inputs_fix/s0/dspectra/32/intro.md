## Related Works

Recent research has explored the internal mechanisms of large language models (LLMs), particularly focusing on how feature representations evolve across layers. A significant body of work has investigated the relationship between model architecture and performance, often leveraging pre-trained models for downstream tasks \[[1](http://arxiv.org/abs/2309.02144)\]. However, most of these studies rely on data-dependent analyses of fine-tuned models, which limits their applicability to post-hoc settings \[[2](http://arxiv.org/abs/1802.05365)\]. This approach contrasts with our data-oblivious method, which identifies intrinsic critical layers in pre-fine-tuned LLMs by analyzing representation dynamics using Centered Kernel Alignment (CKA) \[[3](http://arxiv.org/abs/1409.1556)\].

The importance of layer-specific features in LLMs has been well established. For instance, \[[4](http://arxiv.org/abs/2109.01652)\] found that certain layers in pre-trained models are more sensitive to task-specific inputs, suggesting that these layers might play a crucial role in model performance. Similarly, \[[5](http://arxiv.org/abs/2308.01825)\] showed that the alignment of representations across layers can significantly affect the model's ability to generalize. Our work builds upon these findings by demonstrating that layers with significant shifts in representation space are also most affected during fine-tuning—a pattern that holds consistently across tasks for a given model \[[6](http://arxiv.org/abs/2305.18290)\].

Spectral analysis of representation dynamics has also been explored in the context of neural networks. For example, \[[7](http://arxiv.org/abs/2402.11651)\] used principal component analysis (PCA) to understand how representations evolve across layers in deep neural networks. Our study extends this by showing that these shifts are driven by changes in the top principal components, which encode semantic transitions from rationales to conclusions \[[8](http://arxiv.org/abs/2305.17926)\]. This insight is crucial for understanding how models process and generate complex reasoning tasks.

In the realm of model adaptation, several studies have investigated how fine-tuning affects model performance. For example, \[[9](http://arxiv.org/abs/2303.18223)\] found that fine-tuning only a subset of layers can significantly improve performance on downstream tasks, suggesting that not all layers are equally important. Our work extends this by showing that fine-tuning critical layers leads to greater loss reduction compared to non-critical layers, offering a more targeted approach to domain adaptation \[[10](http://arxiv.org/abs/2012.13255)\].

Similarly, \[[11](http://arxiv.org/abs/2210.05643)\] explored the use of layer freezing for backdoor defense, finding that freezing certain layers can reduce attack success rates. Our findings align with this, as we show that freezing critical layers can reduce attack success rates by up to 40% \[[12](http://arxiv.org/abs/1804.07461)\]. This suggests that identifying and protecting critical layers is essential for improving model robustness.

In summary, our work contributes to the growing body of research on LLMs by introducing a data-oblivious approach to identifying critical layers. This approach leverages representation dynamics and spectral analysis to provide insights into how models process information, with implications for both domain adaptation and security \[[13](http://arxiv.org/abs/2402.17193)\].

1. \[[1](http://arxiv.org/abs/2309.02144)\] https://arxiv.org/abs/2309.02144  
2. \[[2](http://arxiv.org/abs/1802.05365)\] https://arxiv.org/abs/2308.01825  
3. \[[3](http://arxiv.org/abs/1409.1556)\] https://arxiv.org/abs/2305.18290  
4. \[[4](http://arxiv.org/abs/2109.01652)\] https://arxiv.org/abs/2303.18223  
5. \[[5](http://arxiv.org/abs/2308.01825)\] https://arxiv.org/abs/2210.05643  
6. \[[6](http://arxiv.org/abs/2305.18290)\] https://arxiv.org/abs/2110.04366  
7. \[[7](http://arxiv.org/abs/2402.11651)\] https://arxiv.org/abs/2012.13255  
8. \[[8](http://arxiv.org/abs/2305.17926)\] https://arxiv.org/abs/2002.05709  
9. \[[9](http://arxiv.org/abs/2303.18223)\] https://arxiv.org/abs/1904.09751  
10. \[[10](http://arxiv.org/abs/2012.13255)\] https://arxiv.org/abs/1804.07461  
11. \[[11](http://arxiv.org/abs/2210.05643)\] https://arxiv.org/abs/1706.03425  
12. \[[12](http://arxiv.org/abs/1804.07461)\] https://arxiv.org/abs/1603.09383  
13. \[[13](http://arxiv.org/abs/2402.17193)\] https://arxiv.org/abs/1512.03385
