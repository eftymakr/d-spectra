## Related Works

Recent research has focused on understanding how feature representations evolve across layers in large language models (LLMs), aiming to improve interpretability and robustness \[[1](http://arxiv.org/abs/2411.09539)\]. Early studies primarily analyzed fine-tuned models, relying on data-dependent methods to identify critical layers linked to specific functions or behaviors \[[2](http://arxiv.org/abs/2503.04346)\]. However, these approaches are limited to post-hoc analysis and do not provide insights into pre-fine-tuned models \[[3](http://arxiv.org/abs/2502.16722)\]. 

Several works have explored the dynamics of representation learning in transformers. For instance, \[[4](http://arxiv.org/abs/2210.05643)\] investigates the evolution of representations in fine-tuned BERT models, revealing that early layers retain general representations, while later layers specialize in task adaptation. This finding aligns with our understanding that representation changes occur across layers during fine-tuning \[[5](http://arxiv.org/abs/2501.05032)\]. Additionally, \[[6](http://arxiv.org/abs/2402.11651)\] explores how fine-tuning affects the internal mechanisms of LLMs, noting that fine-tuning can lead to catastrophic forgetting and shifts in internal reasoning processes \[[7](http://arxiv.org/abs/2408.15600)\]. 

The use of kernel-based methods to understand fine-tuning has also been explored. \[[8](http://arxiv.org/abs/2412.19512)\] proposes a kernel-based view of language model fine-tuning, suggesting that the Neural Tangent Kernel (NTK) can describe fine-tuning updates to pre-trained models, offering theoretical insights into the success of parameter-efficient methods \[[9](http://arxiv.org/abs/2212.08853)\]. This aligns with our approach of using Centered Kernel Alignment (CKA) to analyze representation dynamics in pre-fine-tuned models \[[10](http://arxiv.org/abs/2408.07888)\].

In the context of domain adaptation and backdoor defense, several studies have examined the impact of fine-tuning specific layers. \[[11](http://arxiv.org/abs/2410.10739)\] discusses how selective layer fine-tuning in federated learning can improve model convergence by allowing clients to adjust their selected layers based on local data and resources \[[12](http://arxiv.org/abs/2504.02268)\]. Similarly, \[[13](http://arxiv.org/abs/2312.10793)\] highlights the importance of layer selection in fine-tuning, showing that freezing certain layers can reduce attack success rates in backdoor defense scenarios \[[14](http://arxiv.org/abs/2411.15382)\]. 

Moreover, \[[15](http://arxiv.org/abs/2102.06605)\] investigates the impact of fine-tuning on chain-of-thought (CoT) reasoning, finding that while fine-tuning improves task-specific performance, it can also lead to a decrease in the faithfulness of CoT reasoning \[[16](http://arxiv.org/abs/2502.05945)\]. This underscores the need for careful layer selection to maintain reasoning capabilities \[[17](http://arxiv.org/abs/2304.05216)\]. 

In addition, \[[18](http://arxiv.org/abs/2502.16147)\] proposes a method to enhance semantic caching by using domain-specific embedding models fine-tuned on specialized datasets, demonstrating improved precision and recall compared to state-of-the-art alternatives \[[19](http://arxiv.org/abs/2308.08469)\]. This aligns with our approach of analyzing representation dynamics to identify critical layers for efficient fine-tuning \[[20](http://arxiv.org/abs/2501.19389)\].

Finally, \[[21](http://arxiv.org/abs/2402.10208)\] explores the recovery of pre-fine-tuning weights in generative models, showing that it is possible to recover the original weights using a few low-rank fine-tuned models, which has implications for model alignment and safety \[[22](http://arxiv.org/abs/2207.09225)\].

---

**References**  
\[[1](http://arxiv.org/abs/2411.09539)\] Fine-tuning Large Language Models with Limited Data: A Survey and Practical Guide [http://arxiv.org/abs/2411.09539]  
\[[2](http://arxiv.org/abs/2503.04346)\] Layer-Wise Evolution of Representations in Fine-Tuned Transformers: Insights from Sparse AutoEncoders [http://arxiv.org/abs/2502.16722]  
\[[3](http://arxiv.org/abs/2502.16722)\] A Kernel-Based View of Language Model Fine-Tuning [http://arxiv.org/abs/2210.05643]  
\[[4](http://arxiv.org/abs/2210.05643)\] Exploring Selective Layer Fine-Tuning in Federated Learning [http://arxiv.org/abs/2408.15600]  
\[[5](http://arxiv.org/abs/2501.05032)\] Safeguard Fine-Tuned LLMs Through Pre- and Post-Tuning Model Merging [http://arxiv.org/abs/2412.19512]  
\[[6](http://arxiv.org/abs/2402.11651)\] HyPe: Better Pre-trained Language Model Fine-tuning with Hidden Representation Perturbation [http://arxiv.org/abs/2212.08853]  
\[[7](http://arxiv.org/abs/2408.15600)\] On the Impact of Fine-Tuning on Chain-of-Thought Reasoning [http://arxiv.org/abs/2411.15382]  
\[[8](http://arxiv.org/abs/2412.19512)\] Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents [http://arxiv.org/abs/2402.11651]  
\[[9](http://arxiv.org/abs/2212.08853)\] Demystifying Instruction Mixing for Fine-tuning Large Language Models [http://arxiv.org/abs/2312.10793]  
\[[10](http://arxiv.org/abs/2408.07888)\] Balancing Continuous Pre-Training and Instruction Fine-Tuning: Optimizing Instruction-Following in LLMs [http://arxiv.org/abs/2410.10739]  
\[[11](http://arxiv.org/abs/2410.10739)\] Advancing Semantic Caching for LLMs with Domain-Specific Embeddings and Synthetic Data [http://arxiv.org/abs/2504.02268]  
\[[12](http://arxiv.org/abs/2504.02268)\] Head-Specific Intervention Can Induce Misaligned AI Coordination in Large Language Models [http://arxiv.org/abs/2502.05945]  
\[[13](http://arxiv.org/abs/2312.10793)\] Towards Efficient Fine-Tuning of Pre-trained Code Models: An Experimental Study and Beyond [http://arxiv.org/abs/2304.05216]  
\[[14](http://arxiv.org/abs/2411.15382)\] Number Representations in LLMs: A Computational Parallel to Human Perception [http://arxiv.org/abs/2502.16147]  
\[[15](http://arxiv.org/abs/2102.06605)\] LLM4TS: Aligning Pre-Trained LLMs as Data-Efficient Time-Series Forecasters [http://arxiv.org/abs/2308.08469]  
\[[16](http://arxiv.org/abs/2502.05945)\] Federated Sketching LoRA: A Flexible Framework for Heterogeneous Collaborative Fine-Tuning of LLMs [http://arxiv.org/abs/2501.19389]  
\[[17](http://arxiv.org/abs/2304.05216)\] Recovering the Pre-Fine-Tuning Weights of Generative Models [http://arxiv.org/abs/2402.10208]  
\[[18](http://arxiv.org/abs/2502.16147)\] Similarity of Pre-trained and Fine-tuned Representations [http://arxiv.org/abs/2207.09225]
