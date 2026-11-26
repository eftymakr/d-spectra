## Related Works

Deploying large language models (LLMs) on edge devices presents significant challenges due to the limited storage, computational power, and energy resources available \[[8](https://www.semanticscholar.org/paper/ec93fc7ec82c65a7bf7213488327d391014539ed)\]. Prior research has explored various techniques to address these limitations, including quantization, model compression, and efficient inference strategies. For instance, quantization methods such as those proposed in \[[11](http://arxiv.org/abs/2208.07339)\] enable inference using integer-only arithmetic, reducing memory usage and improving on-device latency. Similarly, \[[13](http://arxiv.org/abs/2306.00978)\] introduces AWQ, an activation-aware weight quantization method that significantly reduces model size while preserving performance. These approaches are crucial for enabling LLM deployment on resource-constrained devices \[[8](https://www.semanticscholar.org/paper/ec93fc7ec82c65a7bf7213488327d391014539ed)\].

Efficient memory management is another critical area of research. \[[1](http://arxiv.org/abs/2309.06180)\] proposes PagedAttention, an attention algorithm inspired by virtual memory techniques, which minimizes memory waste and enables flexible sharing of key-value caches. This is particularly important for large models where memory usage can be prohibitive. Additionally, \[[17](http://arxiv.org/abs/2505.03745)\] introduces AccLLM, which combines algorithmic and hardware-level optimizations to reduce memory and bandwidth requirements, enabling efficient long-context inference on edge devices.

Hardware accelerators have also been explored to improve the performance of LLMs on edge devices. \[[22](http://arxiv.org/abs/2401.09890)\] provides a comprehensive survey of hardware accelerators, including GPUs, FPGAs, and custom architectures, highlighting their role in enhancing the energy efficiency and performance of LLMs. \[[23](https://www.semanticscholar.org/paper/a821a00c54749a69a9d9fe0a7411de590d247715)\] introduces DNNBuilder, an automated tool for designing high-performance FPGA accelerators, which significantly reduces latency and improves throughput for DNNs. These accelerators are essential for achieving the high performance required by LLMs on edge platforms \[[8](https://www.semanticscholar.org/paper/ec93fc7ec82c65a7bf7213488327d391014539ed)\].

Furthermore, the deployment of LLMs on edge devices has been studied in the context of edge computing frameworks. \[[18](http://arxiv.org/abs/1709.04061)\] presents ENORM, a framework for managing edge node resources, which helps reduce application latency and communication frequency between edge nodes and the cloud. This is particularly relevant for applications requiring real-time processing and low-latency responses \[[8](https://www.semanticscholar.org/paper/ec93fc7ec82c65a7bf7213488327d391014539ed)\].

In addition to hardware and algorithmic optimizations, the use of efficient inference techniques has been explored. \[[16](http://arxiv.org/abs/2402.16363)\] provides a survey of efficient LLM inference methods, categorizing them into data-level, model-level, and system-level optimizations. These methods include techniques such as early exit, mixture-of-experts, and quantization, which collectively contribute to the efficient deployment of LLMs \[[8](https://www.semanticscholar.org/paper/ec93fc7ec82c65a7bf7213488327d391014539ed)\].

The importance of model compression and pruning has also been emphasized in the context of edge deployment. \[[21](http://arxiv.org/abs/2402.14800)\] introduces post-training expert pruning and skipping techniques for MoE LLMs, which reduce model size and improve inference speed without compromising performance. These methods are particularly useful for deploying large models on resource-constrained edge devices \[[8](https://www.semanticscholar.org/paper/ec93fc7ec82c65a7bf7213488327d391014539ed)\].

In summary, the deployment of LLMs on edge devices is a multifaceted challenge that requires a combination of algorithmic, hardware, and system-level optimizations. The related works highlight the importance of quantization, memory management, efficient inference techniques, and hardware accelerators in enabling the deployment of LLMs on edge platforms \[[8](https://www.semanticscholar.org/paper/ec93fc7ec82c65a7bf7213488327d391014539ed)\].

References:  
\[[1](http://arxiv.org/abs/2309.06180)\] Efficient Memory Management for Large Language Model Serving with PagedAttention  
\[[2](http://arxiv.org/abs/1712.05877)\] Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference  
\[[3](http://arxiv.org/abs/2312.11514)\] LLM in a flash: Efficient Large Language Model Inference with Limited Memory  
\[[4](http://arxiv.org/abs/2408.00462)\] Designing Efficient LLM Accelerators for Edge Devices  
\[[5](http://arxiv.org/abs/2304.12244)\] WizardLM: Empowering Large Pre-Trained Language Models to Follow Complex Instructions  
\[[6](http://arxiv.org/abs/1804.07461)\] GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding  
\[[7](http://arxiv.org/abs/1904.04421)\] FPGA/DNN Co-Design: An Efficient Design Methodology for 1oT Intelligence on the Edge  
\[[8](https://www.semanticscholar.org/paper/ec93fc7ec82c65a7bf7213488327d391014539ed)\] An Empirical Analysis and Resource Footprint Study of Deploying Large Language Models on Edge Devices  
\[[9](http://arxiv.org/abs/1704.04760)\] In-datacenter performance analysis of a tensor processing unit  
\[[10](http://arxiv.org/abs/2309.02144)\] Making Large Language Models Better Reasoners with Alignment  
\[[11](http://arxiv.org/abs/2208.07339)\] LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale  
\[[12](http://arxiv.org/abs/2305.14019)\] ChipGPT: How far are we from natural language hardware design  
\[[13](http://arxiv.org/abs/2306.00978)\] AWQ: Activation-aware Weight Quantization for On-Device LLM Compression and Acceleration  
\[[14](http://arxiv.org/abs/2210.11416)\] Scaling Instruction-Finetuned Language Models  
\[[15](http://arxiv.org/abs/2109.01652)\] Finetuned Language Models Are Zero-Shot Learners  
\[[16](http://arxiv.org/abs/2402.16363)\] LLM Inference Unveiled: Survey and Roofline Model Insights  
\[[17](http://arxiv.org/abs/2505.03745)\] AccLLM: Accelerating Long-Context LLM Inference via Algorithm-Hardware Co-Design  
\[[18](http://arxiv.org/abs/1709.04061)\] ENORM: A Framework For Edge NOde Resource Management  
\[[19](http://arxiv.org/abs/2305.10403)\] PaLM 2 Technical Report  
\[[20](http://arxiv.org/abs/2404.14294)\] A Survey on Efficient Inference for Large Language Models  
\[[21](http://arxiv.org/abs/2402.14800)\] Not All Experts are Equal: Efficient Expert Pruning and Skipping for Mixture-of-Experts Large Language Models  
\[[22](http://arxiv.org/abs/2401.09890)\] A Survey on Hardware Accelerators for Large Language Models  
\[[23](https://www.semanticscholar.org/paper/a821a00c54749a69a9d9fe0a7411de590d247715)\] DNNBuilder: an Automated Tool for Building High-Performance DNN Hardware Accelerators for FPGAs
