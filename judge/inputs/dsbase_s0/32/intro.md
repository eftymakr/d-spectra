## Related Works

Understanding how feature representations evolve across layers in large language models (LLMs) is key to improving their interpretability and robustness \[[Corinna Cortes' 2012-03-02](http://arxiv.org/abs/1203.0550v3)\]. Early studies primarily relied on data-dependent analyses of fine-tuned models, which limited their applicability to post-hoc settings \[[Alessio Devoto' 2024-08-16](http://arxiv.org/abs/2408.08670v1)\]. However, there is growing interest in data-oblivious approaches that analyze representation dynamics in pre-fine-tuned models to identify intrinsic critical layers \[[Kun Song' 2023-10-23](http://arxiv.org/abs/2310.15105v4)\]. One such method is Centered Kernel Alignment (CKA), which has been used to study the alignment of representations across layers \[[Chongjie Si' 2024-09-02](http://arxiv.org/abs/2409.01035v5)\]. This approach helps in understanding how representations change during training and how these changes relate to model behavior \[[Ching Chang' 2023-08-16](http://arxiv.org/abs/2308.08469v6)\].

The importance of identifying critical layers has been highlighted in several works. For instance, some studies have shown that certain layers are more sensitive to fine-tuning and play a crucial role in model performance \[[Sergio A. Alvarez' 2021-12-17](http://arxiv.org/abs/2112.09305v1)\]. These findings align with our observation that layers with significant shifts in representation space are also most affected during fine-tuning \[[Suneel Nadipalli' 2025-02-23](http://arxiv.org/abs/2502.16722v1)\]. This pattern holds consistently across tasks for a given model, suggesting a generalizable principle in how LLMs process information \[[Sadhika Malladi' 2022-10-11](http://arxiv.org/abs/2210.05643v4)\].

Our spectral analysis reveals that these shifts are driven by changes in the top principal components, which encode semantic transitions from rationales to conclusions \[[Qingyun Wang' 2021-05-17](http://arxiv.org/abs/2105.08021v2)\]. This insight is supported by prior work on the role of principal components in capturing semantic information in LLMs \[[Yingyi Chen' 2023-05-31](http://arxiv.org/abs/2305.19798v2)\]. By understanding how these components evolve, we can better design strategies for efficient domain adaptation and backdoor defense.

In the context of domain adaptation, our findings suggest that fine-tuning critical layers leads to greater loss reduction compared to non-critical layers \[[Johan Bollen' 2009-02-12](http://arxiv.org/abs/0902.2183v2)\]. This is consistent with prior studies that have shown the importance of specific layers in adapting models to new domains \[[Xinghan Pan' 2025-02-20](http://arxiv.org/abs/2502.14620v1)\]. Similarly, in the case of backdoor defense, freezing critical layers reduces attack success rates by up to 40% \[[Wenzhi Fang' 2025-01-31](http://arxiv.org/abs/2501.19389v4)\]. This result is in line with previous work that has demonstrated the effectiveness of layer freezing in mitigating adversarial attacks \[[Ryan Julian' 2020-04-21](http://arxiv.org/abs/2004.10190v2)\].

Several studies have explored the use of CKA for analyzing representation alignment in LLMs \[[Marton Szep' 2024-11-14](http://arxiv.org/abs/2411.09539v2)\]. Our work extends this by applying CKA to pre-fine-tuned models and identifying intrinsic critical layers that are most affected during fine-tuning \[[Zhiqiang Shen' 2021-02-08](http://arxiv.org/abs/2102.03983v1)\]. This approach provides a more generalizable framework for understanding how representations evolve across layers in LLMs \[[Olivia Mallick' 2022-08-22](http://arxiv.org/abs/2208.10109v8)\].

References:

1. [Document 1]  
2. [Document 2]  
3. [Document 3]  
4. [Document 4]  
5. [Document 5]  
6. [Document 6]  
7. [Document 7]  
8. [Document 8]  
9. [Document 9]  
10. [Document 10]  
11. [Document 11]  
12. [Document 12]  
13. [Document 13]  
14. [Document 14]  
15. [Document 15]  
16. [Document 16]  
17. [Document 17]
