## Related Works

Efficient memory management and KV cache optimization have been extensively studied in the context of large language model (LLM) serving systems. Early work focused on the challenges of managing the key-value (KV) cache, which stores attention keys and values to avoid recomputation during inference \[[1](http://arxiv.org/abs/2309.06180)\]. The memory footprint of the KV cache, which grows dynamically with sequence length and batch size, has been identified as a critical bottleneck in LLM deployment \[[2](http://arxiv.org/abs/2402.02750)\]. Traditional approaches often rely on static memory allocation, leading to significant waste due to fragmentation and redundant duplication \[[1](http://arxiv.org/abs/2309.06180)\]. 

Recent research has introduced more sophisticated techniques to manage the KV cache. PagedAttention, inspired by virtual memory paging, enables near-zero memory waste and flexible sharing of KV cache across requests \[[1](http://arxiv.org/abs/2309.06180)\]. Similarly, KIVI proposes a tuning-free 2-bit quantization method for KV cache, reducing peak memory usage by up to 2.6× while maintaining model quality \[[2](http://arxiv.org/abs/2402.02750)\]. These methods highlight the importance of memory-aware design in improving throughput and latency.

The importance of KV cache reuse has also been explored. Scissorhands leverages the persistence of importance hypothesis, assuming that only pivotal tokens influence future generations \[[3](http://arxiv.org/abs/2305.17118)\]. This leads to a 5× reduction in memory usage without compromising model quality \[[3](http://arxiv.org/abs/2305.17118)\]. Similarly, InfiniGen introduces dynamic KV cache management for long-text generation, prefetching essential KV cache entries to reduce fetch overhead \[[9](http://arxiv.org/abs/2406.19707)\]. These approaches demonstrate the potential of adaptive and context-aware cache management.

Another line of work focuses on KV cache compression, aiming to reduce memory usage while preserving generation quality. H2O introduces a heavy-hitter oracle, retaining only the most influential tokens for attention computation \[[5](http://arxiv.org/abs/2306.14048)\]. This method reduces memory usage and improves throughput by up to 29× compared to existing systems \[[5](http://arxiv.org/abs/2306.14048)\]. GEAR further refines this idea by combining quantization, low-rank approximation, and sparsity to achieve near-lossless compression with up to 2.38× throughput improvement \[[10](http://arxiv.org/abs/2403.05527)\]. These methods show that careful selection and quantization of KV cache entries can significantly enhance efficiency.

Prompt Cache introduces a modular approach to attention reuse, precomputing and storing attention states for frequently occurring text segments \[[11](http://arxiv.org/abs/2311.04934)\]. This allows for efficient reuse across different prompts, reducing latency by up to 60× in CPU-based inference \[[11](http://arxiv.org/abs/2311.04934)\]. LESS integrates a constant-sized cache with eviction-based methods, enabling full query access to all tokens while maintaining efficiency \[[12](http://arxiv.org/abs/2402.09398)\]. These techniques highlight the value of caching and reuse in reducing redundant computation.

Finally, PyramidKV dynamically adjusts KV cache size across layers, allocating more cache in lower layers where attention is more dispersed and less in higher layers where it converges on critical tokens \[[13](http://arxiv.org/abs/2406.02069)\]. This approach reduces memory usage by up to 98% while maintaining high accuracy, demonstrating the effectiveness of layer-specific cache management.

These studies collectively highlight the ongoing efforts to optimize KV cache management in LLM serving systems, emphasizing the need for adaptive, memory-efficient, and performance-aware strategies.

References:  
\[[1](http://arxiv.org/abs/2309.06180)\] http://arxiv.org/abs/2309.06180  
\[[2](http://arxiv.org/abs/2402.02750)\] http://arxiv.org/abs/2402.02750  
\[[3](http://arxiv.org/abs/2305.17118)\] http://arxiv.org/abs/2305.17118  
\[[5](http://arxiv.org/abs/2306.14048)\] http://arxiv.org/abs/2306.14048  
\[[9](http://arxiv.org/abs/2406.19707)\] http://arxiv.org/abs/2309.17453  
\[[10](http://arxiv.org/abs/2403.05527)\] http://arxiv.org/abs/2402.18096  
\[[11](http://arxiv.org/abs/2311.04934)\] http://arxiv.org/abs/2311.04934  
\[[12](http://arxiv.org/abs/2402.09398)\] http://arxiv.org/abs/2402.09398  
\[[13](http://arxiv.org/abs/2406.02069)\] http://arxiv.org/abs/2406.02069
