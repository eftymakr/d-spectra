## Related Works

Deploying large language models (LLMs) on edge devices presents significant challenges due to limited storage, power, and computational resources \[[1](http://arxiv.org/abs/2309.06180)\]. Prior work has explored various techniques to optimize LLM inference on resource-constrained hardware. For instance, AWQ introduces activation-aware weight quantization to reduce model size and accelerate inference on edge devices, achieving up to 4x model size reduction and 3-4x speedup \[[4](http://arxiv.org/abs/2306.00978)\]. Similarly, SmoothQuant enables 8-bit weight and activation quantization without accuracy loss, allowing the deployment of 530B LLMs on a single node \[[7](http://arxiv.org/abs/2211.10438)\]. These methods are critical for reducing memory footprint and improving inference speed on edge platforms.

Efficient memory management is another key area of research. PagedAttention and vLLM address the issue of dynamic key-value cache (KV cache) memory management, achieving near-zero waste and flexible sharing of memory across requests \[[1](http://arxiv.org/abs/2309.06180)\]. FlashAttention further improves attention computation by exploiting the GPU memory hierarchy, reducing memory usage from quadratic to linear in sequence length \[[18](http://arxiv.org/abs/2205.14135)\]. FlashAttention-2 builds on this by optimizing work partitioning and parallelism, achieving up to 2× speedup over FlashAttention and reaching 50-73% of the theoretical maximum FLOPs/s \[[6](http://arxiv.org/abs/2307.08691)\]. These advancements are essential for enabling efficient LLM inference on devices with limited memory.

Hardware accelerators play a crucial role in improving the performance and energy efficiency of LLMs on edge devices. FTRANS proposes an efficient acceleration framework for transformer-based models using FPGAs, reducing model size by up to 16 times and achieving significant improvements in performance and energy efficiency over CPUs and GPUs \[[5](http://arxiv.org/abs/2007.08563)\]. NPE introduces an FPGA-based overlay processor for NLP tasks, offering 4x lower power than CPUs and 6x lower power than GPUs for the BERT model \[[14](http://arxiv.org/abs/2104.06535)\]. SECDA provides a hardware/software co-design methodology for FPGA-based DNN accelerators, reducing design time and improving energy efficiency \[[21](http://arxiv.org/abs/2110.00478)\]. These accelerators are vital for enabling real-time inference on edge devices with limited resources.

Efficient decoding algorithms are also essential for improving the performance of LLMs on edge devices. Speculative decoding enables the generation of multiple tokens in parallel, achieving up to 2-2.5x decoding speedup without compromising sample quality \[[22](http://arxiv.org/abs/2302.01318)\]. Inference with Reference leverages the overlap between generated text and reference documents to accelerate inference by up to 2x \[[13](http://arxiv.org/abs/2304.04487)\]. These methods are particularly useful in scenarios where significant overlap exists between the model's output and the reference text, such as in search engines and multi-turn conversations.

In addition to these techniques, several studies focus on reducing the computational complexity of attention mechanisms. A^3 accelerates attention mechanisms using algorithmic approximation and hardware specialization, achieving multiple orders of magnitude improvements in energy efficiency \[[16](http://arxiv.org/abs/2002.10941)\]. ELSA introduces a hardware-software co-designed solution for efficient self-attention, achieving a geomean speedup of 58.1× and significant energy savings \[[3](https://www.semanticscholar.org/paper/5af69480a7ae3b571df6782a11ec4437b386a7d9)\]. These methods are crucial for reducing the computational overhead of attention mechanisms, which are a major contributor to the runtime of LLMs.

Finally, model compression and pruning techniques are widely used to reduce the size and computational requirements of LLMs. Wanda introduces a novel pruning method that requires no retraining, achieving significant performance improvements over magnitude pruning \[[17](http://arxiv.org/abs/2306.11695)\]. These techniques are essential for deploying LLMs on edge devices with limited resources.

1. \[[1](http://arxiv.org/abs/2309.06180)\] Document 1  
2. \[[4](http://arxiv.org/abs/2306.00978)\] Document 4  
3. \[[7](http://arxiv.org/abs/2211.10438)\] Document 7  
4. \[[13](http://arxiv.org/abs/2304.04487)\] Document 13  
5. \[[14](http://arxiv.org/abs/2104.06535)\] Document 14  
6. \[[16](http://arxiv.org/abs/2002.10941)\] Document 16  
7. \[[17](http://arxiv.org/abs/2306.11695)\] Document 17  
8. \[[21](http://arxiv.org/abs/2110.00478)\] Document 21  
9. \[[22](http://arxiv.org/abs/2302.01318)\] Document 22  
10. \[[18](http://arxiv.org/abs/2205.14135)\] Document 18  
11. \[[5](http://arxiv.org/abs/2007.08563)\] Document 5  
12. \[[3](https://www.semanticscholar.org/paper/5af69480a7ae3b571df6782a11ec4437b386a7d9)\] Document 3  
13. \[[6](http://arxiv.org/abs/2307.08691)\] Document 6  
14. \[[10](http://arxiv.org/abs/2408.00462)\] Document 10  
15. \[[2](http://arxiv.org/abs/2312.11514)\] Document 2  
16. \[[9](http://arxiv.org/abs/2310.17157)\] Document 9  
17. \[[11](http://arxiv.org/abs/2209.10797)\] Document 11  
18. \[[12](http://arxiv.org/abs/2211.17192)\] Document 12  
19. \[[15](http://arxiv.org/abs/2309.17453)\] Document 15  
20. \[[20](http://arxiv.org/abs/2401.09890)\] Document 20  
21. \[[8](http://arxiv.org/abs/2307.09288)\] Document 8  
22. \[[19](http://arxiv.org/abs/2012.09852)\] Document 19  
23. \[[23](http://arxiv.org/abs/2401.02385)\] Document 23
