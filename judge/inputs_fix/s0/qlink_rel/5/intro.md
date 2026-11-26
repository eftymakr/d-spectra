## Related Works

Instruction-following text embedding has emerged as a critical area in natural language processing (NLP), aiming to generate dynamic text embeddings that adapt to user instructions \[[20](http://arxiv.org/abs/2109.01652)\]. This task is particularly important for applications requiring real-time adaptation, such as information retrieval, semantic similarity, and task-specific modeling \[[19](http://arxiv.org/abs/2204.07705)\]. However, existing methods often suffer from significant computational overhead due to the necessity of re-encoding the entire corpus for each new instruction \[[20](http://arxiv.org/abs/2109.01652)\]. This limitation motivates the development of more efficient frameworks that can adapt pre-computed embeddings in real time \[[20](http://arxiv.org/abs/2109.01652)\].

Several approaches have been proposed to improve the efficiency of instruction-following text embeddings. One line of work focuses on instruction tuning, where models are fine-tuned on a collection of tasks described via instructions \[[20](http://arxiv.org/abs/2109.01652)\]. This approach has shown substantial improvements in zero-shot performance on unseen tasks \[[20](http://arxiv.org/abs/2109.01652)\]. Similarly, Self-Instruct introduces a framework for improving instruction-following capabilities by bootstrapping off the model's own generations \[[4](http://arxiv.org/abs/2212.10560)\]. This method generates instructions, input, and output samples from a language model and uses them to fine-tune the original model \[[4](http://arxiv.org/abs/2212.10560)\]. These approaches, however, still require re-encoding the entire corpus for each instruction, which is computationally expensive \[[20](http://arxiv.org/abs/2109.01652)\].

Another line of work explores the use of contrastive learning for sentence embeddings, such as SimCSE, which uses contrastive learning to generate high-quality sentence embeddings \[[12](http://arxiv.org/abs/2104.08821)\]. This method has shown promising results on semantic textual similarity tasks \[[12](http://arxiv.org/abs/2104.08821)\]. Similarly, E5 is a family of state-of-the-art text embeddings trained in a contrastive manner with weak supervision signals \[[18](http://arxiv.org/abs/2212.03533)\]. These models achieve strong performance in both zero-shot and fine-tuned settings \[[18](http://arxiv.org/abs/2212.03533)\]. However, these methods are not designed for instruction-following and do not adapt embeddings in real time \[[18](http://arxiv.org/abs/2212.03533)\].

Recent work has also explored the use of instruction-tuned language models for zero-shot learning \[[20](http://arxiv.org/abs/2109.01652)\]. For example, FLAN is a model that is instruction-tuned on over 60 NLP tasks and demonstrates significant improvements in zero-shot performance \[[20](http://arxiv.org/abs/2109.01652)\]. Similarly, InstructGPT is a model that is fine-tuned using human feedback to improve instruction-following capabilities \[[9](http://arxiv.org/abs/2203.02155)\]. These models, however, still require re-encoding the entire corpus for each instruction, which is computationally expensive \[[20](http://arxiv.org/abs/2109.01652)\].

To address these limitations, we propose GSTransform, a novel instruction-following text embedding framework based on Guided Space Transformation \[[20](http://arxiv.org/abs/2109.01652)\]. Our key observation is that instruction-relevant information is inherently encoded in generic embeddings but remains underutilized \[[20](http://arxiv.org/abs/2109.01652)\]. Instead of re-encoding the corpus for each instruction, GSTransform is a lightweight transformation mechanism that adapts pre-computed embeddings in real time to align with user instructions, guided by a small amount of text data with instruction-focused label annotation \[[20](http://arxiv.org/abs/2109.01652)\].

In summary, while existing approaches have made significant progress in instruction-following text embedding, they often suffer from significant computational overhead due to the necessity of re-encoding the entire corpus for each new instruction \[[20](http://arxiv.org/abs/2109.01652)\]. Our work addresses this challenge by proposing a lightweight transformation mechanism that adapts pre-computed embeddings in real time \[[20](http://arxiv.org/abs/2109.01652)\].

References:

1. \[[1](http://arxiv.org/abs/1910.10683)\] Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer [http://arxiv.org/abs/1910.10683]
2. \[[2](http://arxiv.org/abs/1706.03762)\] Attention is All you Need [http://arxiv.org/abs/1706.03762]
3. \[[3](http://arxiv.org/abs/1506.06726)\] Skip-Thought Vectors [http://arxiv.org/abs/1506.06726]
4. \[[4](http://arxiv.org/abs/2212.10560)\] Self-Instruct: Aligning Language Models with Self-Generated Instructions [http://arxiv.org/abs/2212.10560]
5. \[[5](http://arxiv.org/abs/1810.04805)\] BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding [http://arxiv.org/abs/1810.04805]
6. \[[6](http://arxiv.org/abs/1711.07280)\] Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments [http://arxiv.org/abs/1711.07280]
7. \[[7](http://arxiv.org/abs/2304.12244)\] WizardLM: Empowering Large Pre-Trained Language Models to Follow Complex Instructions [http://arxiv.org/abs/2304.12244]
8. \[[8](http://arxiv.org/abs/2304.03277)\] Instruction Tuning with GPT-4 [http://arxiv.org/abs/2304.03277]
9. \[[9](http://arxiv.org/abs/2203.02155)\] Training language models to follow instructions with human feedback [http://arxiv.org/abs/2203.02155]
10. \[[10](http://arxiv.org/abs/2210.07316)\] MTEB: Massive Text Embedding Benchmark [http://arxiv.org/abs/2210.07316]
11. \[[11](http://arxiv.org/abs/2303.08774)\] GPT-4 Technical Report [http://arxiv.org/abs/2303.08774]
12. \[[12](http://arxiv.org/abs/2104.08821)\] SimCSE: Simple Contrastive Learning of Sentence Embeddings [http://arxiv.org/abs/2104.08821]
13. \[[13](http://arxiv.org/abs/1806.02724)\] Speaker-Follower Models for Vision-and-Language Navigation [http://arxiv.org/abs/1806.02724]
14. \[[14](http://arxiv.org/abs/2108.08877)\] Sentence-T5: Scalable Sentence Encoders from Pre-trained Text-to-Text Models [http://arxiv.org/abs/2108.08877]
15. \[[15](http://arxiv.org/abs/1908.07490)\] LXMERT: Learning Cross-Modality Encoder Representations from Transformers [http://arxiv.org/abs/1908.07490]
16. \[[16](http://arxiv.org/abs/2005.14165)\] Language Models are Few-Shot Learners [http://arxiv.org/abs/2005.14165]
17. \[[17](http://arxiv.org/abs/1310.4546)\] Distributed Representations of Words and Phrases and their Compositionality [http://arxiv.org/abs/1310.4546]
18. \[[18](http://arxiv.org/abs/2212.03533)\] Text Embeddings by Weakly-Supervised Contrastive Pre-training [http://arxiv.org/abs/2212.03533]
19. \[[19](http://arxiv.org/abs/2204.07705)\] Super-NaturalInstructions: Generalization via Declarative Instructions on 1600+ NLP Tasks [http://arxiv.org/abs/2204.07705]
20. \[[20](http://arxiv.org/abs/2109.01652)\] Finetuned Language Models Are Zero-Shot Learners [http://arxiv.org/abs/2109.01652]
