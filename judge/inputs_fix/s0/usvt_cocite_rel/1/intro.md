## Related Works

KV cache compression has emerged as a critical area of research for improving the efficiency of large language model (LLM) inference, particularly in serving scenarios where memory and throughput are paramount. Prior work has focused on various strategies, including quantization, compression, and eviction policies, to reduce the memory footprint of KV caches while maintaining model performance.

Quantization techniques have been widely explored for reducing the memory usage of KV caches. KIVI \[[1](http://arxiv.org/abs/2402.02750)\] introduces a tuning-free 2-bit quantization approach that differentiates between key and value caches, applying per-channel quantization to keys and per-token quantization to values. This method enables significant memory reduction, allowing models like Llama and Mistral to maintain similar quality while using 2.6× less peak memory. Similarly, KVQuant \[[9](http://arxiv.org/abs/2401.18079)\] proposes a comprehensive set of methods for low-precision KV cache quantization, including per-channel key quantization, pre-RoPE quantization, and non-uniform quantization, achieving less than 0.1 perplexity degradation with 3-bit quantization. These approaches demonstrate that quantization can effectively reduce memory usage without significant performance loss.

KV cache compression techniques have also been investigated through the lens of token importance and similarity. H2O \[[7](http://arxiv.org/abs/2306.14048)\] introduces a dynamic eviction policy based on the observation that a small subset of tokens, referred to as heavy hitters, contribute most to attention scores. By retaining these tokens, H2O achieves up to 29× throughput improvements over existing systems. Similarly, Scissorhands \[[4](http://arxiv.org/abs/2305.17118)\] leverages the persistence of importance hypothesis, prioritizing the storage of pivotal tokens to maintain model quality while reducing memory usage by up to 5×. These methods highlight the importance of identifying and retaining critical tokens for efficient inference.

Adaptive KV cache compression has also been explored, with approaches such as FastGen \[[8](http://arxiv.org/abs/2310.01801)\] and KVMerger \[[11](http://arxiv.org/abs/2407.08454)\] aiming to reduce memory usage while preserving performance. FastGen employs adaptive compression by selectively evicting non-critical tokens based on attention head behavior, while KVMerger focuses on merging similar key states within sequences to reduce cache size without significant performance degradation. These methods demonstrate that adaptive strategies can offer a balance between memory efficiency and model accuracy.

Recent work has also focused on the structural properties of KV caches. MiniCache \[[3](http://arxiv.org/abs/2405.14366)\] introduces a depth-based compression approach, exploiting the high similarity between adjacent layers in the middle-to-deep portion of LLMs. By disentangling state vectors into magnitude and direction components, MiniCache achieves up to 5.02× compression ratios with minimal additional storage overhead. PyramidKV \[[13](http://arxiv.org/abs/2406.02069)\] further explores dynamic compression by adjusting cache size across layers, allocating more cache to lower layers where information is more dispersed and less to higher layers where attention is more focused. This approach reduces memory usage significantly while maintaining model performance.

In addition to compression, the management of KV cache memory has been addressed through system-level optimizations. PagedAttention \[[2](http://arxiv.org/abs/2309.06180)\] introduces an attention algorithm inspired by virtual memory paging, enabling efficient memory management and flexible sharing of KV cache across requests. This approach minimizes memory waste and improves throughput, especially for long sequences and large models.

These studies collectively highlight the diverse approaches to KV cache optimization, ranging from quantization and compression to adaptive eviction and structural analysis. Each contributes to a growing body of knowledge aimed at improving the efficiency and scalability of LLM inference.

### References

1. KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache [http://arxiv.org/abs/2402.02750]  
2. Efficient Memory Management for Large Language Model Serving with PagedAttention [http://arxiv.org/abs/2309.06180]  
3. MiniCache: KV Cache Compression in Depth Dimension for Large Language Models [http://arxiv.org/abs/2405.14366]  
4. Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time [http://arxiv.org/abs/2305.17118]  
5. SnapKV: LLM Knows What You are Looking for Before Generation [http://arxiv.org/abs/2404.14469]  
6. Efficient Streaming Language Models with Attention Sinks [http://arxiv.org/abs/2309.17453]  
7. H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models [http://arxiv.org/abs/2306.14048]  
8. Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs [http://arxiv.org/abs/2310.01801]  
9. KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization [http://arxiv.org/abs/2401.18079]  
10. WKVQuant: Quantizing Weight and Key/Value Cache for Large Language Models Gains More [http://arxiv.org/abs/2402.12065]  
11. Model Tells You Where to Merge: Adaptive KV Cache Merging for LLMs on Long-Context Tasks [http://arxiv.org/abs/2407.08454]  
12. GEAR: An Efficient KV Cache Compression Recipe for Near-Lossless Generative Inference of LLM [http://arxiv.org/abs/2403.05527]  
13. PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling [http://arxiv.org/abs/2406.02069]
