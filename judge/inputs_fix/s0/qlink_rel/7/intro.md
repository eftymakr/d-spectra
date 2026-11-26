## Related Works

Large Language Models (LLMs) have been extensively studied for their ability to encode and exhibit various behaviors, including refusal, which is often a result of safety fine-tuning. Refusal behavior in LLMs is typically mediated by a single direction in the model's activation space, as demonstrated by \[[1](http://arxiv.org/abs/2406.11717)\]. This finding suggests that refusal can be systematically manipulated by altering specific directions in the residual stream, which has implications for both safety and controllability of model outputs. However, existing methods for identifying such directions often rely on predefined refusal templates detectable in output tokens or require manual analysis, which limits their generalizability \[[1](http://arxiv.org/abs/2406.11717)\].

Recent work has explored methods to steer LLMs by modifying their activations during inference, such as Contrastive Activation Addition (CAA) \[[4](http://arxiv.org/abs/2312.06681)\]. CAA computes steering vectors by averaging the difference in residual stream activations between positive and negative examples of a behavior, allowing for precise control over the model's output. This approach has been shown to significantly alter model behavior while maintaining core language modeling capabilities. Similarly, Inference-Time Intervention (ITI) \[[5](http://arxiv.org/abs/2306.03341)\] operates by shifting model activations during inference, improving truthfulness in models like LLaMA. ITI demonstrates that models may have an internal representation of truth likelihood, even when generating falsehoods, and can be tuned to balance truthfulness with helpfulness.

The ability of LLMs to perform zero-shot reasoning has also been a focus of recent research. Zero-shot reasoning, where models are prompted with a simple instruction like "Let's think step by step," has been shown to significantly improve performance on diverse reasoning tasks, including arithmetic and symbolic reasoning \[[2](http://arxiv.org/abs/2205.11916)\]. This suggests that LLMs possess untapped zero-shot reasoning capabilities that can be leveraged without the need for task-specific examples.

Multimodal large language models (MLLMs) have also emerged as a promising direction, capable of performing tasks such as image-based storytelling and math reasoning without optical character recognition \[[3](http://arxiv.org/abs/2306.13549)\]. These models leverage powerful LLMs as a core component, demonstrating the potential for broader cognitive capabilities through simple prompting.

In addition, adversarial attacks on aligned LLMs have been explored, where adversarial suffixes can be used to elicit objectionable content by maximizing the probability of affirmative responses \[[8](http://arxiv.org/abs/2307.15043)\]. This highlights the brittleness of current safety fine-tuning methods and the need for more robust alignment strategies.

Finally, the development of efficient and open foundation models like LLaMA \[[12](http://arxiv.org/abs/2302.13971)\] and the exploration of training verifiers to solve math word problems \[[13](http://arxiv.org/abs/2110.14168)\] underscore the ongoing efforts to improve model performance and alignment with human values.

1. Refusal in Language Models Is Mediated by a Single Direction [http://arxiv.org/abs/2406.11717]  
2. Large Language Models are Zero-Shot Reasoners [http://arxiv.org/abs/2205.11916]  
3. A survey on multimodal large language models [http://arxiv.org/abs/2306.13549]  
4. Steering Llama 2 via Contrastive Activation Addition [http://arxiv.org/abs/2312.06681]  
5. Inference-Time Intervention: Eliciting Truthful Answers from a Language Model [http://arxiv.org/abs/2306.03341]  
6. Ethical and social risks of harm from Language Models [http://arxiv.org/abs/2112.04359]  
7. Toolformer: Language Models Can Teach Themselves to Use Tools [http://arxiv.org/abs/2302.04761]  
8. Universal and Transferable Adversarial Attacks on Aligned Language Models [http://arxiv.org/abs/2307.15043]  
9. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding [http://arxiv.org/abs/1810.04805]  
10. A General Language Assistant as a Laboratory for Alignment [http://arxiv.org/abs/2112.00861]  
11. A Survey of Large Language Models [http://arxiv.org/abs/2303.18223]  
12. LLaMA: Open and Efficient Foundation Language Models [http://arxiv.org/abs/2302.13971]  
13. Training Verifiers to Solve Math Word Problems [http://arxiv.org/abs/2110.14168]
