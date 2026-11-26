## Related Works

Instruction-following text embedding has emerged as a critical area in natural language processing, aiming to generate dynamic embeddings that adapt to user instructions. This task is particularly challenging due to the need for embeddings to reflect specific attributes of text while being responsive to diverse instructions \[[17](http://arxiv.org/abs/2204.07705)\]. Prior approaches have primarily relied on re-encoding the entire corpus for each new instruction, which leads to significant computational overhead \[[17](http://arxiv.org/abs/2204.07705)\]. This limitation has motivated the development of more efficient methods that can adapt pre-computed embeddings in real time \[[17](http://arxiv.org/abs/2204.07705)\].

One early approach to text embeddings is the Transformer architecture, which has been foundational in many NLP tasks \[[3](http://arxiv.org/abs/1706.03762)\]. The Transformer's attention mechanism allows for parallel processing and has led to state-of-the-art results in machine translation and other sequence tasks \[[3](http://arxiv.org/abs/1706.03762)\]. However, these models are typically static and do not adapt well to dynamic instructions without retraining \[[17](http://arxiv.org/abs/2204.07705)\].

Recent work has focused on instruction-tuned models, such as InstructGPT, which fine-tunes large language models using human feedback to improve their ability to follow instructions \[[9](http://arxiv.org/abs/2203.02155)\]. Similarly, Self-Instruct introduces a framework for improving instruction-following capabilities by bootstrapping from a model's own generations, reducing reliance on human-annotated data \[[5](http://arxiv.org/abs/2212.10560)\]. These methods demonstrate that instruction tuning can significantly enhance model performance on a variety of tasks, but they often require extensive training and labeled data \[[5](http://arxiv.org/abs/2212.10560)\]\[[9](http://arxiv.org/abs/2203.02155)\].

The INSTRUCTOR model introduces a novel approach by embedding text together with task instructions, enabling a single model to generate embeddings tailored to different downstream tasks and domains \[[1](http://arxiv.org/abs/2212.09741)\]. This method uses a multitask mixture with a contrastive loss, achieving state-of-the-art performance on a wide range of tasks \[[1](http://arxiv.org/abs/2212.09741)\]. Similarly, E5 is a family of text embeddings trained with weak supervision signals from a large-scale text pair dataset, achieving strong performance in both zero-shot and fine-tuned settings \[[2](http://arxiv.org/abs/2212.03533)\]. These models highlight the potential of contrastive learning in improving the adaptability of text embeddings.

Another line of research explores the use of contrastive learning for sentence embeddings, such as SimCSE, which uses a simple contrastive framework to achieve state-of-the-art results on semantic textual similarity tasks \[[11](http://arxiv.org/abs/2104.08821)\]. This work demonstrates that contrastive learning can be effective even without explicit supervision, aligning with the goals of instruction-following text embeddings.

In the context of vision-language navigation, models like RCM and SIL have been developed to address challenges in cross-modal grounding and generalization \[[10](http://arxiv.org/abs/1811.10092)\]. These models use reinforcement learning and self-supervised imitation learning to improve performance on complex navigation tasks, showcasing the importance of adaptive and efficient learning mechanisms.

The proposed GSTransform framework builds on these advancements by introducing a lightweight transformation mechanism that adapts pre-computed embeddings in real time, guided by instruction-focused label annotation \[[17](http://arxiv.org/abs/2204.07705)\]. This approach significantly reduces computational overhead while maintaining high-quality instruction-following embeddings.

References:

1. \[[1](http://arxiv.org/abs/2212.09741)\] http://arxiv.org/abs/2212.09741  
2. \[[2](http://arxiv.org/abs/2212.03533)\] http://arxiv.org/abs/2212.03533  
3. \[[3](http://arxiv.org/abs/1706.03762)\] http://arxiv.org/abs/1706.03762  
5. \[[5](http://arxiv.org/abs/2212.10560)\] http://arxiv.org/abs/2212.10560  
9. \[[9](http://arxiv.org/abs/2203.02155)\] http://arxiv.org/abs/2203.02155  
10. \[[10](http://arxiv.org/abs/1811.10092)\] http://arxiv.org/abs/1811.10092  
11. \[[11](http://arxiv.org/abs/2104.08821)\] http://arxiv.org/abs/2104.08821  
17. \[[17](http://arxiv.org/abs/2204.07705)\] http://arxiv.org/abs/2204.07705
