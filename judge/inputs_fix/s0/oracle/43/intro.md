## Related Works

The training of large language models (LLMs) in distributed environments presents significant challenges due to the complexity of model execution, deployment systems, and the vast space of configurable strategies \[[1](http://arxiv.org/abs/2304.01433)\]. Various optimization techniques have been proposed to address these challenges, but achieving high efficiency in practice remains difficult \[[1](http://arxiv.org/abs/2304.01433)\]. Accurate performance models that effectively characterize and predict a model's behavior are essential for guiding optimization efforts and system-level studies \[[1](http://arxiv.org/abs/2304.01433)\]. 

Several works have focused on improving the efficiency of training large models. For instance, the Transformer architecture has become the foundation of many state-of-the-art models, achieving superior performance in quality while being more parallelizable and requiring significantly less time to train \[[2](http://arxiv.org/abs/1706.03762)\]. The Transformer model has been successfully applied to various tasks, including machine translation and English constituency parsing \[[2](http://arxiv.org/abs/1706.03762)\]. 

Efforts to scale training to larger models have led to the development of systems like Pathways, which enables highly efficient training across multiple TPU Pods \[[3](http://arxiv.org/abs/2204.02311)\]. This system was used to train a 540-billion parameter Transformer language model called PaLM, which demonstrated continued benefits of scaling by achieving state-of-the-art few-shot learning results on hundreds of language understanding and generation benchmarks \[[3](http://arxiv.org/abs/2204.02311)\]. Similarly, the Megatron framework has been used to train the largest monolithic transformer-based language model, Megatron-Turing NLG 530B (MT-NLG), with 530 billion parameters \[[4](http://arxiv.org/abs/2201.11990)\]. This model achieved superior zero-, one-, and few-shot learning accuracies on several NLP benchmarks \[[4](http://arxiv.org/abs/2201.11990)\].

To further enhance the scalability of training, systems like GSPMD have been developed to provide automatic, compiler-based parallelization for machine learning computations \[[5](http://arxiv.org/abs/2105.04663)\]. GSPMD allows users to write programs as if for a single device and then distribute the computation across multiple devices using annotations \[[5](http://arxiv.org/abs/2105.04663)\]. This system has been shown to achieve up to 62% compute utilization on up to 2048 Cloud TPUv3 cores for models with up to one trillion parameters \[[5](http://arxiv.org/abs/2105.04663)\].

Another key challenge in training large models is the memory and communication overhead associated with long sequences. Several works have proposed solutions to this problem, including sequence parallelism, which enables training with longer sequences by splitting the input into chunks and distributing them across devices \[[7](http://arxiv.org/abs/2105.13120)\]. Additionally, DeepSpeed-Ulysses has been introduced to enable highly efficient and scalable LLM training with extremely long sequence length by partitioning input data along the sequence dimension and using efficient all-to-all collective communication for attention computation \[[8](http://arxiv.org/abs/2309.14509)\]. 

Finally, tools like Daydream have been developed to help programmers explore the efficacy of DNN optimizations by modeling DNN execution with a fine-grained dependency graph based on low-level traces \[[10](http://arxiv.org/abs/2006.03318)\]. This tool allows for accurate prediction of the efficacy of optimizations and facilitates efficient exploration of model and deployment configurations \[[10](http://arxiv.org/abs/2006.03318)\].

1. \[[1](http://arxiv.org/abs/2304.01433)\] "Training LLMs in distributed environments presents significant challenges due to the complexity of model execution, deployment systems, and the vast space of configurable strategies. Although various optimization techniques exist, achieving high efficiency in practice remains difficult. Accurate performance models that effectively characterize and predict a model's behavior are essential for guiding optimization efforts and system-level studies. We propose Lumos, a trace-driven performance modeling and estimation toolkit for large-scale LLM training, designed to accurately capture and predict the execution behaviors of modern LLMs. We evaluate Lumos on a production ML cluster with up to 512 NVIDIA H100 GPUs using various GPT-3 variants, demonstrating that it can replay execution time with an average error of just 3.3%, along with other runtime details, across different models and configurations. Additionally, we validate its ability to estimate performance for new setups from existing traces, facilitating efficient exploration of model and deployment configurations."

2. \[[2](http://arxiv.org/abs/1706.03762)\] "Attention Is All You Need" [http://arxiv.org/abs/1706.03762]

3. \[[3](http://arxiv.org/abs/2204.02311)\] "PaLM: Scaling Language Modeling with Pathways" [http://arxiv.org/abs/2204.02311]

4. \[[4](http://arxiv.org/abs/2201.11990)\] "Using DeepSpeed and Megatron to Train Megatron-Turing NLG 530B, A Large-Scale Generative Language Model" [http://arxiv.org/abs/2201.11990]

5. \[[5](http://arxiv.org/abs/2105.04663)\] "GSPMD: General and Scalable Parallelization for ML Computation Graphs" [http://arxiv.org/abs/2105.04663]

6. \[[6](http://arxiv.org/abs/2211.13878)\] "Galvatron: Efficient Transformer Training over Multiple GPUs Using Automatic Parallelism" [http://arxiv.org/abs/2211.13878]

7. \[[7](http://arxiv.org/abs/2105.13120)\] "Sequence Parallelism: Long Sequence Training from System Perspective" [http://arxiv.org/abs/2105.13120]

8. \[[8](http://arxiv.org/abs/2309.14509)\] "DeepSpeed Ulysses: System Optimizations for Enabling Training of Extreme Long Sequence Transformer Models" [http://arxiv.org/abs/2309.14509]

9. \[[9](http://arxiv.org/abs/2310.01889)\] "Ring Attention with Blockwise Transformers for Near-Infinite Context" [http://arxiv.org/abs/2310.01889]

10. \[[10](http://arxiv.org/abs/2006.03318)\] "Daydream: Accurately Estimating the Efficacy of Optimizations for DNN Training" [http://arxiv.org/abs/2006.03318]
