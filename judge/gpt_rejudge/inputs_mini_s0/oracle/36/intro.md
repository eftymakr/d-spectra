## Related Works

The deployment of large language models (LLMs) on edge devices presents significant challenges due to limited storage, computational resources, and power budgets. Prior research has explored complementary algorithmic and hardware strategies to address these constraints while maintaining model accuracy and latency requirements.

### Model Compression and Quantization

Model compression techniques, such as pruning and quantization, are fundamental to adapting LLMs for resource-constrained environments. SparseGPT demonstrated that large GPT-family models can be pruned up to 60% sparsity in one shot without retraining or major accuracy loss, enabling substantial reduction in inference computation \[[2301.00774](http://arxiv.org/abs/2301.00774)\]. Similarly, SmoothQuant provides an effective post-training quantization method that enables 8-bit weight and activation quantization for LLMs like OPT and LLaMA while preserving accuracy and hardware efficiency, yielding up to 1.56x speedup and 2x memory reduction \[[2211.10438](http://arxiv.org/abs/2211.10438)\]. These methods are often complementary and can be combined to maximize compression.

Knowledge distillation (KD) techniques also play a critical role in compressing LLMs. DistiLLM introduced a novel KD framework with a skew Kullback-Leibler divergence loss and adaptive off-policy training to efficiently distill large auto-regressive models into smaller, high-performing student models, achieving up to 4.3× speedup over prior KD methods \[[2402.03898](http://arxiv.org/abs/2402.03898)\]. MiniLLM further refined KD for generative models using reverse KLD, improving calibration and long-text generation while scaling across different sizes \[[2306.08543](http://arxiv.org/abs/2306.08543)\].

### Efficient Inference Algorithms and Sparsity

To reduce inference latency and energy on edge devices, contextual sparsity approaches dynamically identify and utilize small input-dependent subsets of parameters to approximate dense model outputs. DejaVu demonstrated this by predicting contextual sparsity on the fly, achieving over 2× latency reduction on OPT-175B without compromising quality or in-context learning ability \[[2310.17157](http://arxiv.org/abs/2310.17157)\]. PowerInfer exploits the power-law distribution of neuron activations by preloading frequently active "hot" neurons on the GPU and offloading "cold" neurons to the CPU, significantly reducing memory demands and speeding up inference on consumer-grade GPUs, achieving near server-grade performance on OPT models \[[2312.12456](http://arxiv.org/abs/2312.12456)\].

### Hardware-Software Co-Design and Acceleration

Hardware specialization and co-design are crucial for balancing throughput, latency, and energy consumption on edge platforms. EdgeBERT presented a comprehensive co-design involving algorithmic techniques such as entropy-based early exit, adaptive attention span, pruning, and quantization, paired with a 12nm hardware accelerator integrating fast voltage regulators and embedded non-volatile memory to optimize latency-aware multi-task NLP inference, achieving up to 7× energy savings over conventional methods \[[2011.14203](http://arxiv.org/abs/2011.14203)\]. Similarly, LLM in a Flash proposed storing model parameters in flash memory with hardware-informed strategies like windowing and row-column bundling to enable running LLMs larger than DRAM capacity with 4-25× speedups over naive loading, demonstrating hardware-aware system design for memory-limited devices \[[2312.11514](http://arxiv.org/abs/2312.11514)\].

On the system side, PagedAttention and the vLLM serving system tackle the inefficiencies of key-value cache memory management by leveraging virtual memory-inspired paging and cache sharing, improving throughput by 2-4× with stable latency for large models and long sequences \[[2309.06180](http://arxiv.org/abs/2309.06180)\]. ExeGPT introduces a distributed scheduling framework that optimizes execution schedules under latency constraints, achieving up to 15.2× throughput improvements over FasterTransformer for various LLMs and workloads \[[2404.07947](http://arxiv.org/abs/2404.07947)\]. FlexGen targets high-throughput batched LLM generation on a single commodity GPU by aggregating GPU, CPU, and disk resources with weight and cache compression, enabling large models like OPT-175B to run with limited GPU memory \[[2303.06865](http://arxiv.org/abs/2303.06865)\].

Splitwise addresses inference efficiency by splitting LLM inference into two phases—compute-intensive prompt encoding and memory-intensive token generation—executed on different hardware optimized for each phase, improving throughput and reducing cost and power consumption \[[2311.18677](http://arxiv.org/abs/2311.18677)\].

### Training and Model Scaling

Scaling large models has been shown to significantly improve few-shot learning and reasoning capabilities, as demonstrated by PaLM, which achieved state-of-the-art results on various benchmarks with 540 billion parameters \[[2204.02311](http://arxiv.org/abs/2204.02311)\]. Open-source models like LLaMA and Llama 2 have also contributed to making large-scale pretrained models accessible, facilitating research in efficient deployment and fine-tuning on edge-relevant tasks \[[2302.13971](http://arxiv.org/abs/2302.13971)\]\[[2307.09288](http://arxiv.org/abs/2307.09288)\].

### Summary

Overall, the literature indicates that addressing the challenges of LLM deployment on edge devices requires a synergistic approach combining model compression (pruning, quantization, distillation), dynamic sparsity exploitation, and hardware-software co-design. Techniques such as contextual sparsity, early exit, and memory management optimizations complement specialized hardware accelerators and system-level scheduling to meet the demanding latency, energy, and accuracy trade-offs inherent to edge inference.

References  
\[[2204.02311](http://arxiv.org/abs/2204.02311)\]  
\[[2310.17157](http://arxiv.org/abs/2310.17157)\]  
\[[2011.14203](http://arxiv.org/abs/2011.14203)\]  
\[[2303.06865](http://arxiv.org/abs/2303.06865)\]  
\[[2211.10438](http://arxiv.org/abs/2211.10438)\]  
\[[2301.00774](http://arxiv.org/abs/2301.00774)\]  
\[[2309.06180](http://arxiv.org/abs/2309.06180)\]  
\[[2312.11514](http://arxiv.org/abs/2312.11514)\]  
\[[2402.03898](http://arxiv.org/abs/2402.03898)\]  
\[[2302.13971](http://arxiv.org/abs/2302.13971)\]  
\[[2307.09288](http://arxiv.org/abs/2307.09288)\]  
\[[2312.12456](http://arxiv.org/abs/2312.12456)\]  
\[[2404.07947](http://arxiv.org/abs/2404.07947)\]  
\[[2311.18677](http://arxiv.org/abs/2311.18677)\]  
\[[2306.08543](http://arxiv.org/abs/2306.08543)\]