## Related Works

KV cache management has emerged as a critical area of research for improving the efficiency of large language model (LLM) serving systems. Prior work has focused on reducing the memory footprint and computational overhead of KV caches, which are essential for enabling long-context inference. Several approaches have been proposed to address these challenges, including compression techniques, eviction policies, and adaptive reuse strategies.

Early efforts in KV cache compression focused on quantization and sparsity, aiming to reduce the memory usage of the cache while preserving generation quality. For instance, KIVI introduces a tuning-free 2bit quantization method that quantizes key caches per-channel and value caches per-token, achieving a 2.6× reduction in peak memory usage without significant performance degradation \[[7](http://arxiv.org/abs/2402.02750)\]. Similarly, MiniCache compresses the KV cache across layers by exploiting the high similarity between adjacent layers, achieving up to 5.02x compression ratios and improving inference throughput by approximately 5x \[[4](http://arxiv.org/abs/2405.14366)\]. These methods demonstrate the potential of compression to reduce memory demands, but they often require careful tuning or are limited in their applicability to specific model architectures.

In addition to compression, researchers have explored KV cache eviction strategies to manage memory constraints during inference. CAKE introduces a cascading and adaptive eviction policy that considers layer-specific attention patterns and temporal dynamics, enabling efficient resource allocation across layers \[[13](http://arxiv.org/abs/2503.12491)\]. This approach improves cache utilization by dynamically adjusting the cache size based on the importance of tokens over time. Similarly, KVMerger proposes an adaptive merging strategy that leverages the high similarity of key states within a sequence to reduce the cache size without significant performance loss \[[9](http://arxiv.org/abs/2407.08454)\]. These methods highlight the importance of adaptive and context-aware strategies in managing the KV cache effectively.

Another line of research focuses on the integration of KV cache compression with other optimization techniques, such as prompt compression and sparse attention. For example, VL-Cache extends KV cache compression to vision-language models (VLMs) by introducing sparsity-aware budget allocation and modality-aware token scoring, achieving a 90% reduction in memory footprint while maintaining high accuracy \[[5](http://arxiv.org/abs/2410.23317)\]. These methods demonstrate the versatility of KV cache management techniques across different model types and tasks.

Furthermore, recent studies have emphasized the need for comprehensive benchmarking of KV cache management strategies. SCBench provides a detailed analysis of long-context methods from a KV cache-centric perspective, evaluating techniques such as sparse attention, quantization, and retrieval \[[12](http://arxiv.org/abs/2412.10319)\]. This benchmarking framework helps identify the strengths and limitations of various approaches, guiding future research and development.

In summary, the field of KV cache management has seen significant advancements, with a growing focus on compression, eviction, and adaptive reuse strategies. These techniques aim to improve the efficiency and scalability of LLM serving systems, particularly in long-context scenarios. Future work should continue to explore the interplay between these methods and their impact on real-world deployment.

References:  
\[[1](http://arxiv.org/abs/2310.07240)\] http://arxiv.org/abs/2310.07240  
\[[2](http://arxiv.org/abs/2407.01527)\] http://arxiv.org/abs/2407.01527  
\[[3](http://arxiv.org/abs/2412.19442)\] http://arxiv.org/abs/2412.19442  
\[[4](http://arxiv.org/abs/2405.14366)\] http://arxiv.org/abs/2405.14366  
\[[5](http://arxiv.org/abs/2410.23317)\] http://arxiv.org/abs/2410.23317  
\[[6](http://arxiv.org/abs/2502.16002)\] http://arxiv.org/abs/2502.16002  
\[[7](http://arxiv.org/abs/2402.02750)\] http://arxiv.org/abs/2402.02750  
\[[8](http://arxiv.org/abs/2406.19707)\] http://arxiv.org/abs/2406.19707  
\[[9](http://arxiv.org/abs/2407.08454)\] http://arxiv.org/abs/2407.08454  
\[[10](http://arxiv.org/abs/2503.24000)\] http://arxiv.org/abs/2503.24000  
\[[11](http://arxiv.org/abs/2402.18096)\] http://arxiv.org/abs/2402.18096  
\[[12](http://arxiv.org/abs/2412.10319)\] http://arxiv.org/abs/2412.10319  
\[[13](http://arxiv.org/abs/2503.12491)\] http://arxiv.org/abs/2503.12491
