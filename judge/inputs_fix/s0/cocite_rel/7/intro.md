## Related Works

Recent research has explored the internal mechanisms of large language models (LLMs), particularly focusing on how they encode and express behaviors such as refusal and alignment. A key insight is that refusal behavior is mediated by a single direction in the model's activation space, which can be manipulated to alter model behavior \[[1](http://arxiv.org/abs/2406.11717)\]. This finding highlights the importance of understanding the internal structure of LLMs to develop effective steering techniques. However, existing methods often rely on predefined refusal templates detectable in output tokens or require manual analysis, which limits their applicability in adversarial or weakly aligned settings \[[1](http://arxiv.org/abs/2406.11717)\].

To address these limitations, researchers have proposed automated frameworks for identifying and steering model behavior. One such approach is the use of contrastive activation addition (CAA), which computes steering vectors by averaging the difference in residual stream activations between positive and negative examples of a behavior \[[4](http://arxiv.org/abs/2312.06681)\]. This method allows for precise control over the degree of the targeted behavior, and it has been shown to significantly alter model behavior with minimal impact on other capabilities. CAA is particularly effective when combined with traditional methods like fine-tuning and system prompt design.

Another line of research focuses on improving the truthfulness of LLMs through inference-time intervention (ITI), which shifts model activations during inference to enhance truthfulness \[[7](http://arxiv.org/abs/2306.03341)\]. ITI has been shown to significantly improve the performance of LLaMA models on the TruthfulQA benchmark, increasing truthfulness from 32.5% to 65.1%. This approach is minimally invasive and computationally inexpensive, making it a promising technique for enhancing model reliability.

Additionally, the use of chain-of-thought (CoT) prompting has been explored as a way to improve reasoning capabilities in LLMs \[[2](http://arxiv.org/abs/2205.11916)\]. CoT prompting involves generating intermediate reasoning steps to guide the model toward correct answers. This technique has been shown to significantly improve performance on arithmetic and symbolic reasoning tasks. More recently, multimodal chain-of-thought (Multimodal-CoT) has been proposed to incorporate vision and language modalities, further enhancing reasoning capabilities \[[5](http://arxiv.org/abs/2302.00923)\].

The ability of LLMs to teach themselves to use external tools has also been investigated, leading to the development of models like Toolformer, which can decide which APIs to call and how to incorporate their results into future token prediction \[[6](http://arxiv.org/abs/2302.04761)\]. This approach allows LLMs to achieve the best of both worlds—leveraging their language modeling abilities while also accessing external information.

In summary, recent work has made significant strides in understanding and manipulating the internal mechanisms of LLMs, particularly in terms of alignment, refusal, and reasoning. These findings provide a foundation for developing more robust and controllable models.

References:
1. \[[1](http://arxiv.org/abs/2406.11717)\] Refusal in Language Models Is Mediated by a Single Direction
2. \[[2](http://arxiv.org/abs/2205.11916)\] Large Language Models are Zero-Shot Reasoners
3. \[[4](http://arxiv.org/abs/2312.06681)\] Steering Llama 2 via Contrastive Activation Addition
4. \[[5](http://arxiv.org/abs/2302.00923)\] Multimodal Chain-of-Thought Reasoning in Language Models
5. \[[6](http://arxiv.org/abs/2302.04761)\] Toolformer: Language Models Can Teach Themselves to Use Tools
6. \[[7](http://arxiv.org/abs/2306.03341)\] Inference-Time Intervention: Eliciting Truthful Answers from a Language Model
