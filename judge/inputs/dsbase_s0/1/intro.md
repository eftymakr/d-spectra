## Related Works

The efficient serving of large language models (LLMs) has been a focal point of recent research, with a particular emphasis on optimizing the use of key-value (KV) caches to reduce latency and improve throughput. Prior work has explored various strategies for KV cache management, including quantization, compression, and eviction policies. These approaches aim to address the memory and computational bottlenecks inherent in LLM inference, especially when dealing with long-context generation and multi-turn conversations \[[Yucheng Li' 2024-12-13](http://arxiv.org/abs/2412.10319v2)\].

Several studies have investigated the use of quantization techniques to reduce the memory footprint of LLMs. For instance, WKVQuant proposes a PTQ framework that quantizes both model weights and the KV cache, achieving memory savings comparable to weight-activation quantization while maintaining performance close to weight-only quantization \[[Yucheng Li' 2024-12-13](http://arxiv.org/abs/2412.10319v2)\]. Similarly, MiniCache introduces a depth-based compression strategy that reduces the memory footprint of the KV cache by leveraging the high similarity between adjacent layers . These methods highlight the importance of memory optimization in enabling efficient LLM deployment.

KV cache reuse has also been a central theme in recent research, particularly in the context of multi-tenant and multi-request scenarios. KVLink introduces a strategy to precompute and concatenate KV caches for documents that appear in multiple queries, significantly reducing redundant computation and improving question-answering accuracy \[[Junyoung Park' 2025-04-21](http://arxiv.org/abs/2504.15364v4)\]. EFIM further enhances KV cache reuse in infilling tasks by transforming the prompt format to enable more effective cache utilization while addressing subtoken generation issues through fragment tokenization \[[Yixuan Wang' 2025-05-24](http://arxiv.org/abs/2505.20334v2)\]. These approaches demonstrate the potential of KV cache reuse in improving inference efficiency across different LLM applications.

Efforts to optimize cache eviction policies have also gained traction, with several works proposing workload-aware strategies to balance memory usage and performance. For example, NACL introduces a general framework for long-context KV cache eviction that combines accurate attention score statistics with diversified random eviction strategies, achieving significant improvements in both short- and long-text tasks . Similarly, SAGE-KV leverages self-attention to guide KV cache eviction, achieving higher memory efficiency without compromising accuracy . These methods reflect the growing recognition that effective cache management is crucial for real-world LLM deployment.

In addition to these techniques, there has been increasing interest in combining multiple strategies to further enhance performance. For instance, InfiniGen integrates dynamic KV cache management with offloading-based inference systems, allowing for efficient prefetching of essential KV cache entries . Similarly, MorphServe introduces runtime mechanisms for quantized layer swapping and pressure-aware KV cache resizing, enabling adaptive and efficient LLM serving under dynamic workloads . These hybrid approaches underscore the complexity of LLM serving and the need for flexible, workload-aware solutions.

The work presented in this paper builds on these prior contributions, offering a systematic characterization of KV cache workload patterns from a real-world LLM service provider. By analyzing the reuse patterns, timing, and predictability of KV cache access, this study provides insights that were previously unexplored in synthetic workload studies. The proposed workload-aware cache eviction policy is designed to improve serving performance under real-world traces, especially when cache capacity is limited.

### References

1. [Document 1] CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences  
2. [Document 2] Lookahead Q-Cache: Achieving More Consistent KV Cache Eviction via Pseudo Query  
3. [Document 3] In-context KV-Cache Eviction for LLMs via Attention-Gate  
4. [Document 4] MPCache: MPC-Friendly KV Cache Eviction for Efficient Private LLM Inference  
5. [Document 5] NACL: A General and Effective KV Cache Eviction Framework for LLMs at Inference Time  
6. [Document 6] Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference  
7. [Document 7] LLMs Know What to Drop: Self-Attention Guided KV Cache Eviction for Efficient Long-Context Inference  
8. [Document 8] CriticalKV: Optimizing KV Cache Eviction from an Output Perturbation Perspective  
9. [Document 9] KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments  
10. [Document 10] Towards More Economical Context-Augmented LLM Generation by Reusing Stored KV Cache  
11. [Document 11] KVLink: Accelerating Large Language Models via Efficient KV Cache Reuse  
12. [Document 12] KVShare: An LLM Service System with Efficient and Effective Multi-Tenant KV Cache Reuse  
13. [Document 13] EFIM: Efficient Serving of LLMs for Infilling Tasks with Improved KV Cache Reuse  
14. [Document 14] InfiniGen: Efficient Generative Inference of Large Language Models with Dynamic KV Cache Management  
15. [Document 15] MiniCache: KV Cache Compression in Depth Dimension for Large Language Models
