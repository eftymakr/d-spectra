## Related Works

Efficient memory management and KV cache optimization have been central to improving the performance of large language model (LLM) serving systems. Prior work has focused on reducing memory usage and improving throughput through various techniques, including quantization, caching strategies, and dynamic memory allocation. 

Several approaches have been proposed to reduce the memory footprint of KV caches. For instance, **KIVI** introduces a tuning-free 2-bit quantization method for KV cache, achieving up to 2.6× memory reduction and enabling up to 4× larger batch sizes \[[2](http://arxiv.org/abs/2402.02750)\]. Similarly, **KVQuant** advances sub-4-bit quantization by introducing novel methods such as per-channel key quantization and non-uniform KV cache quantization, achieving less than 0.1 perplexity degradation on benchmark datasets \[[7](http://arxiv.org/abs/2401.18079)\]. These methods demonstrate the potential of quantization to reduce memory usage while maintaining model quality.

Dynamic memory management has also been explored. **PagedAttention** is inspired by virtual memory techniques and enables near-zero waste in KV cache memory by allowing flexible sharing within and across requests \[[1](http://arxiv.org/abs/2309.06180)\]. **H2O** introduces a heavy-hitter oracle to dynamically retain important tokens, reducing memory usage and improving throughput by up to 29× on certain models \[[5](http://arxiv.org/abs/2306.14048)\]. These approaches highlight the importance of intelligent eviction policies to maintain performance while minimizing memory consumption.

Efforts to optimize KV cache for streaming applications have also gained traction. **StreamingLLM** addresses the challenge of long-text generation by introducing attention sinks, which allow models to generalize to infinite sequence lengths without fine-tuning \[[4](http://arxiv.org/abs/2309.17453)\]. This is further complemented by **CacheGen**, which compresses KV caches and reduces network delays by up to 3.7× through efficient encoding and adaptive compression \[[8](http://arxiv.org/abs/2310.07240)\]. These systems demonstrate the potential of combining compression and streaming techniques to improve real-time performance.

Additionally, **Scissorhands** exploits the persistence of importance hypothesis, maintaining memory usage within a fixed budget by prioritizing pivotal tokens \[[3](http://arxiv.org/abs/2305.17118)\]. **SnapKV** further reduces memory footprint and improves decoding speed by selectively retaining important KV positions for each attention head \[[9](http://arxiv.org/abs/2404.14469)\]. These methods underscore the importance of adaptive and workload-aware strategies for KV cache management.

In summary, recent research has focused on reducing memory usage, improving throughput, and enabling efficient streaming inference through advanced caching and quantization techniques. These approaches collectively contribute to the broader goal of making LLM serving more scalable and efficient.

References:  
\[[1](http://arxiv.org/abs/2309.06180)\] Efficient Memory Management for Large Language Model Serving with PagedAttention  
[2
