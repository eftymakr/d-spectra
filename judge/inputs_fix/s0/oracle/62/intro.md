## Related Works

Generative retrieval has emerged as a promising paradigm in information retrieval, offering a shift from traditional index-based methods to end-to-end neural models that directly generate document identifiers \[[1](http://arxiv.org/abs/2404.14851)\]. This approach leverages large language models to perform both indexing and retrieval, enabling seamless integration with generative tasks \[[12](http://arxiv.org/abs/2204.10628)\]. Prior work has explored various aspects of this paradigm, including the design of differentiable search indexes \[[13](http://arxiv.org/abs/2202.06991)\], the use of autoregressive models for document retrieval \[[12](http://arxiv.org/abs/2204.10628)\], and the challenges of updating and scaling generative retrieval systems \[[14](http://arxiv.org/abs/2306.11397)\].

A key challenge in generative retrieval is the reliance on constrained decoding to generate document identifiers that are both relevant and distinct \[[1](http://arxiv.org/abs/2404.14851)\]. This process often involves the use of beam search, which has been shown to introduce biases and suboptimal results due to its reliance on marginal distributions \[[1](http://arxiv.org/abs/2404.14851)\]. Several studies have investigated the limitations of beam search in this context, highlighting the need for more effective decoding strategies \[[28](http://arxiv.org/abs/2404.14600)\]. For instance, PAG introduces a novel optimization approach that guides autoregressive generation through simultaneous decoding, improving both retrieval performance and query latency \[[28](http://arxiv.org/abs/2404.14600)\].

The generalization capabilities of generative retrieval on out-of-distribution corpora have also been a focus of recent research \[[18](http://arxiv.org/abs/2412.18768)\]. Studies have shown that generative retrieval models often struggle with robustness when faced with unseen data, particularly in scenarios involving query variations, unseen query types, and corpus expansion \[[18](http://arxiv.org/abs/2412.18768)\]. This has led to the development of methods aimed at improving the out-of-distribution generalization of these models, such as the use of nonparametric decoding to enhance memory capacity and flexibility \[[19](http://arxiv.org/abs/2210.02068)\].

In addition to decoding strategies, the design of document identifiers plays a crucial role in the effectiveness of generative retrieval \[[1](http://arxiv.org/abs/2404.14851)\]. Several approaches have been proposed to address this, including the use of autoregressive models to generate identifiers token-by-token \[[3](http://arxiv.org/abs/2010.00904)\], and the introduction of semantic-enhanced identifiers that incorporate query generation techniques \[[9](http://arxiv.org/abs/2305.15115)\]. These methods aim to improve the accuracy and distinctiveness of generated identifiers, thereby enhancing retrieval performance.

The integration of generative retrieval with other tasks, such as question answering, has also been explored. For example, the UniGen framework unifies generative retrieval and question answering into a single model, leveraging the capabilities of large language models to improve both tasks simultaneously \[[30](http://arxiv.org/abs/2312.11036)\]. This approach introduces shared encoders and distinct decoders, along with connectors that bridge the gap between query inputs and generation targets \[[30](http://arxiv.org/abs/2312.11036)\].

In summary, the field of generative retrieval has seen significant advancements, with a growing body of research addressing the challenges of constrained decoding, beam search, and generalization on out-of-distribution data. These efforts aim to improve the robustness, efficiency, and effectiveness of generative retrieval systems, paving the way for their broader adoption in real-world applications.

References:
1. \[[1](http://arxiv.org/abs/2404.14851)\] http://arxiv.org/abs/2404.14851
2. \[[2](http://arxiv.org/abs/2105.02274)\] http://arxiv.org/abs/2105.02274
3. \[[3](http://arxiv.org/abs/2010.00904)\] http://arxiv.org/abs/2010.00904
4. \[[4](http://arxiv.org/abs/2304.04171)\] http://arxiv.org/abs/2304.04171
5. \[[5](http://arxiv.org/abs/2206.02743)\] http://arxiv.org/abs/2206.02743
6. \[[6](http://arxiv.org/abs/2306.15222)\] http://arxiv.org/abs/2306.15222
7. \[[7](http://arxiv.org/abs/2206.10128)\] http://arxiv.org/abs/2206.10128
8. \[[8](http://arxiv.org/abs/2310.12455)\] http://arxiv.org/abs/2310.12455
9. \[[9](http://arxiv.org/abs/2305.15115)\] http://arxiv.org/abs/2305.15115
10. \[[10](http://arxiv.org/abs/2409.18409)\] http://arxiv.org/abs/2409.18409
11. \[[11](http://arxiv.org/abs/2404.00684)\] http://arxiv.org/abs/2404.00684
12. \[[12](http://arxiv.org/abs/2204.10628)\] http://arxiv.org/abs/2204.10628
13. \[[13](http://arxiv.org/abs/2202.06991)\] http://arxiv.org/abs/2202.06991
14. \[[14](http://arxiv.org/abs/2306.11397)\] http://arxiv.org/abs/2306.11397
15. \[[15](http://arxiv.org/abs/2311.09134)\] http://arxiv.org/abs/2311.09134
16. \[[16](http://arxiv.org/abs/2408.02152)\] http://arxiv.org/abs/2408.02152
17. \[[17](http://arxiv.org/abs/2308.14968)\] http://arxiv.org/abs/2308.14968
18. \[[18](http://arxiv.org/abs/2412.18768)\] http://arxiv.org/abs/2412.18768
19. \[[19](http://arxiv.org/abs/2210.02068)\] http://arxiv.org/abs/2210.02068
20. \[[20](http://arxiv.org/abs/2401.10487)\] http://arxiv.org/abs/2401.10487
21. \[[21](http://arxiv.org/abs/2307.10323)\] http://arxiv.org/abs/2307.10323
22. \[[22](http://arxiv.org/abs/2210.05331)\] http://arxiv.org/abs/2210.05331
23. \[[23](http://arxiv.org/abs/2410.06716)\] http://arxiv.org/abs/2410.06716
24. \[[24](http://arxiv.org/abs/2304.07438)\] http://arxiv.org/abs/2304.07438
25. \[[25](http://arxiv.org/abs/2304.11943)\] http://arxiv.org/abs/2304.11943
26. \[[26](http://arxiv.org/abs/2006.15408)\] http://arxiv.org/abs/2006.15408
27. \[[27](http://arxiv.org/abs/1902.07565)\] http://arxiv.org/abs/1902.07565
28. \[[28](http://arxiv.org/abs/2404.14600)\] http://arxiv.org/abs/2404.14600
29. \[[29](http://arxiv.org/abs/2402.01176)\] http://arxiv.org/abs/2402.01176
30. \[[30](http://arxiv.org/abs/2312.11036)\] http://arxiv.org/abs/2312.11036
