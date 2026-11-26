## Related Works

Generative retrieval has emerged as a promising paradigm in information retrieval, shifting from traditional index-based methods to end-to-end neural models that directly generate document identifiers \[[12](http://arxiv.org/abs/2202.06991)\]. This approach leverages large language models to encode the entire corpus within a single Transformer, eliminating the need for external indices \[[12](http://arxiv.org/abs/2202.06991)\]. Prior work has explored various methods to enable this, including the use of n-grams as document identifiers \[[1](http://arxiv.org/abs/2204.10628)\], the development of single-step generative retrieval models \[[2](http://arxiv.org/abs/2208.07652)\], and the use of autoregressive decoding to generate document identifiers \[[3](http://arxiv.org/abs/2304.04171)\]. These models aim to improve efficiency and integration with generative models, while also enabling better generalization across different corpora \[[1](http://arxiv.org/abs/2204.10628)\].

The concept of using autoregressive models for retrieval has been explored in several works. For instance, SEAL proposes using all n-grams in a passage as potential identifiers and maps them to full passages via an efficient data structure \[[1](http://arxiv.org/abs/2204.10628)\]. Similarly, GenRet introduces a tokenization learning method to generate semantic docids through a discrete auto-encoding approach \[[3](http://arxiv.org/abs/2304.04171)\]. These methods highlight the importance of defining meaningful document identifiers that capture semantic information, which is critical for effective retrieval \[[3](http://arxiv.org/abs/2304.04171)\].

Another key contribution in this area is the development of the Differentiable Search Index (DSI), which uses a single transformer model to perform both indexing and retrieval \[[12](http://arxiv.org/abs/2202.06991)\]. DSI-QG, an extension of this approach, addresses the issue of data distribution mismatch by generating relevant queries during indexing, which are then used to connect document identifiers to queries during retrieval \[[5](http://arxiv.org/abs/2206.10128)\]. This helps mitigate the mismatch between the indexing and retrieval phases, improving performance in both mono-lingual and cross-lingual settings \[[5](http://arxiv.org/abs/2206.10128)\].

The effectiveness of generative retrieval has also been evaluated on large-scale corpora, with studies showing that it can achieve competitive performance with state-of-the-art dual encoder models on small datasets \[[10](http://arxiv.org/abs/2305.11841)\]. However, scaling to millions of passages remains a challenge, with findings indicating the importance of synthetic queries during indexing and the limitations of naive parameter scaling \[[10](http://arxiv.org/abs/2305.11841)\].

In addition, the use of learning-to-rank frameworks has been proposed to bridge the gap between autoregressive models and passage ranking targets \[[8](http://arxiv.org/abs/2306.15222)\]. LTRGR enables generative retrieval to learn to rank passages directly, optimizing the autoregressive model toward the final ranking target via a rank loss \[[8](http://arxiv.org/abs/2306.15222)\]. This approach improves performance without adding significant overhead during inference \[[8](http://arxiv.org/abs/2306.15222)\].

Finally, the integration of prompt learning into generative retrieval has been explored to unify different retrieval tasks into a single model \[[13](http://arxiv.org/abs/2304.14856)\]. UGR introduces an n-gram-based identifier for contexts at different levels of granularity and employs prompt learning to address various retrieval tasks with a single model \[[13](http://arxiv.org/abs/2304.14856)\]. This approach enhances generalization across tasks and domains \[[13](http://arxiv.org/abs/2304.14856)\].

References:  
\[[1](http://arxiv.org/abs/2204.10628)\] http://arxiv.org/abs/2204.10628  
\[[2](http://arxiv.org/abs/2208.07652)\] http://arxiv.org/abs/2208.07652  
\[[3](http://arxiv.org/abs/2304.04171)\] http://arxiv.org/abs/2304.04171  
\[[5](http://arxiv.org/abs/2206.10128)\] http://arxiv.org/abs/2206.10128  
\[[8](http://arxiv.org/abs/2306.15222)\] http://arxiv.org/abs/2306.15222  
\[[10](http://arxiv.org/abs/2305.11841)\] http://arxiv.org/abs/2305.11841  
\[[12](http://arxiv.org/abs/2202.06991)\] http://arxiv.org/abs/2202.06991  
\[[13](http://arxiv.org/abs/2304.14856)\] http://arxiv.org/abs/2304.14856
