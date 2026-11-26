## Related Works

Large language models (LLMs) have seen significant advancements in recent years, with a focus on improving their efficiency, scalability, and performance across diverse tasks. Early work on LLMs primarily focused on pre-training on large corpora and fine-tuning for specific tasks \[[2](http://arxiv.org/abs/2005.14165)\]. For instance, GPT-3 demonstrated strong few-shot learning capabilities, achieving competitive performance on various NLP tasks without any fine-tuning \[[2](http://arxiv.org/abs/2005.14165)\]. This was further extended by FLAN, which showed that instruction tuning significantly improves zero-shot performance on unseen tasks \[[3](http://arxiv.org/abs/2109.01652)\]. Instruction tuning involves fine-tuning models on a collection of tasks described via natural language instructions, leading to substantial improvements in performance across multiple benchmarks \[[3](http://arxiv.org/abs/2109.01652)\].

The training of large models also presents significant challenges, particularly in terms of computational resources and memory constraints. Megatron-LM introduced techniques for training multi-billion parameter models using model parallelism, enabling the training of models up to 8.3 billion parameters on 512 GPUs \[[4](http://arxiv.org/abs/1909.08053)\]. This work demonstrated the importance of careful architectural design and optimization to achieve state-of-the-art results on benchmark datasets \[[4](http://arxiv.org/abs/1909.08053)\].

Recent research has also explored the use of LLMs for code generation and mathematical reasoning. Codex, a GPT model fine-tuned on GitHub code, demonstrated impressive capabilities in writing Python code, solving 28.8% of problems on the HumanEval benchmark \[[10](http://arxiv.org/abs/2107.03374)\]. Similarly, GSM8K was introduced as a dataset of grade school math word problems, highlighting the limitations of current models in multi-step mathematical reasoning \[[13](http://arxiv.org/abs/2110.14168)\]. To address this, researchers proposed training verifiers to judge the correctness of model completions, significantly improving performance on GSM8K \[[13](http://arxiv.org/abs/2110.14168)\].

Instruction tuning has also been shown to enhance the performance of LLMs on a variety of tasks. WizardLM, for example, used an evolutionary instruction generation method to create complex instructions and fine-tune LLaMA, achieving performance comparable to ChatGPT on 17 out of 29 skills \[[1](http://arxiv.org/abs/2304.12244)\]. This work demonstrated the potential of AI-evolved instructions for improving LLM performance \[[1](http://arxiv.org/abs/2304.12244)\].

Furthermore, the development of efficient finetuning methods has enabled the training of large models on limited resources. QLoRA introduced a method for efficient finetuning of quantized LLMs, allowing the finetuning of a 65B parameter model on a single 48GB GPU while preserving full 16-bit finetuning performance \[[15](http://arxiv.org/abs/2305.14314)\]. This approach, which uses low-rank adapters, has led to state-of-the-art results on various benchmarks \[[15](http://arxiv.org/abs/2305.14314)\].

In addition to these advancements, there has been growing interest in evaluating LLMs using human preferences and benchmarks. MT-Bench and Chatbot Arena were introduced as benchmarks to evaluate LLMs on more open-ended questions, demonstrating that strong LLMs like GPT-4 can match both controlled and crowdsourced human preferences well \[[7](http://arxiv.org/abs/2306.05685)\].

1. \[[2](http://arxiv.org/abs/2005.14165)\] Language Models are Few-Shot Learners  
2. \[[3](http://arxiv.org/abs/2109.01652)\] Finetuned Language Models Are Zero-Shot Learners  
3. \[[4](http://arxiv.org/abs/1909.08053)\] Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism  
4. \[[10](http://arxiv.org/abs/2107.03374)\] Evaluating Large Language Models Trained on Code  
5. \[[13](http://arxiv.org/abs/2110.14168)\] Training Verifiers to Solve Math Word Problems  
6. \[[1](http://arxiv.org/abs/2304.12244)\] WizardLM: Empowering Large Pre-Trained Language Models to Follow Complex Instructions  
7. \[[7](http://arxiv.org/abs/2306.05685)\] Judging LLM-as-a-judge with MT-Bench and Chatbot Arena  
8. \[[15](http://arxiv.org/abs/2305.14314)\] QLoRA: Efficient Finetuning of Quantized LLMs
