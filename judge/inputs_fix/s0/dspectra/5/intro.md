## Related Works

Instruction-following text embedding has emerged as a critical area in natural language processing (NLP), aiming to generate dynamic text embeddings that adapt to user instructions \[[1](http://arxiv.org/abs/1910.10683)\]. This task is particularly relevant for applications requiring real-time adaptation, such as information retrieval, semantic similarity, and task-specific embeddings \[[2](http://arxiv.org/abs/1810.04805)\]. Existing approaches, however, often suffer from significant computational overhead due to the need to re-encode the entire corpus for each new instruction \[[3](http://arxiv.org/abs/2212.10560)\]. This limitation has motivated the development of more efficient methods that can adapt pre-computed embeddings in real time \[[4](http://arxiv.org/abs/1706.03762)\].

Several works have explored the use of pre-trained models for instruction-following tasks. BERT, for instance, is a bidirectional transformer model that pre-trains on unlabeled text and can be fine-tuned for various tasks, including question answering and language inference \[[5](http://arxiv.org/abs/2104.08773)\]. Similarly, the Transformer architecture, introduced in \[[6](http://arxiv.org/abs/2212.09741)\], has become a foundational model for sequence transduction tasks, offering superior performance and parallelizability compared to recurrent and convolutional models \[[7](http://arxiv.org/abs/2304.12244)\]. These models, while powerful, typically require retraining or re-encoding for new tasks, which is computationally expensive \[[8](http://arxiv.org/abs/2303.08774)\].

Recent efforts have focused on instruction tuning, where pre-trained models are fine-tuned using instruction-following data to improve their ability to generalize to new tasks \[[9](http://arxiv.org/abs/2304.03277)\]. For example, Self-Instruct introduces a framework for improving instruction-following capabilities by bootstrapping off the model's own generations \[[10](http://arxiv.org/abs/1506.06726)\]. Similarly, the Flan Collection provides a comprehensive set of instruction-tuning methods and datasets, demonstrating that task balancing and enrichment techniques are critical for effective instruction tuning \[[11](http://arxiv.org/abs/2212.09689)\]. These approaches rely on human-generated instruction data, which is often limited in quantity and diversity \[[12](http://arxiv.org/abs/2304.08485)\].

To address these limitations, Unnatural Instructions was introduced, a large dataset of creative and diverse instructions generated with minimal human labor \[[13](http://arxiv.org/abs/2202.12837)\]. This dataset has been used to train models that perform well on various benchmarks, surpassing the performance of models trained on manually-curated datasets \[[14](http://arxiv.org/abs/2301.13688)\]. Similarly, the INSTRUCTOR method introduces a single embedder that can generate text embeddings tailored to different downstream tasks and domains without additional training \[[15](http://arxiv.org/abs/1606.05250)\]. This approach is particularly promising for real-time applications where re-encoding the entire corpus is impractical \[[16](http://arxiv.org/abs/2210.07316)\].

In addition to instruction tuning, there has been growing interest in in-context learning, where models perform new tasks by conditioning on a few input-label pairs \[[17](http://arxiv.org/abs/2305.14327)\]. This approach has shown promise in reducing the need for extensive training data, but it remains unclear how much can be learned through inference alone \[[18](http://arxiv.org/abs/2308.06259)\]. The development of instruction-following models like GPT-4 has further advanced the field, demonstrating human-level performance on various professional and academic benchmarks \[[19](http://arxiv.org/abs/1711.07280)\].

The proposed GSTransform framework builds on these advancements by introducing a lightweight transformation mechanism that adapts pre-computed embeddings in real time, guided by a small amount of instruction-focused labeled data \[[20](http://arxiv.org/abs/2212.03533)\]. This approach significantly reduces computational overhead while maintaining high-quality instruction-following text embeddings \[[21](http://arxiv.org/abs/2110.08207)\].

1. \[[1](http://arxiv.org/abs/1910.10683)\] "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer"  
2. \[[2](http://arxiv.org/abs/1810.04805)\] "Self-Instruct: Aligning Language Models with Self-Generated Instructions"  
3. \[[3](http://arxiv.org/abs/2212.10560)\] "Instruction Tuning with GPT-4"  
4. \[[4](http://arxiv.org/abs/1706.03762)\] "One Embedder, Any Task: Instruction-Finetuned Text Embeddings"  
5. \[[5](http://arxiv.org/abs/2104.08773)\] "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"  
6. \[[6](http://arxiv.org/abs/2212.09741)\] "Attention is All you Need"  
7. \[[7](http://arxiv.org/abs/2304.12244)\] "Cross-Task Generalization via Natural Language Crowdsourcing Instructions"  
8. \[[8](http://arxiv.org/abs/2303.08774)\] "WizardLM: Empowering Large Pre-Trained Language Models to Follow Complex Instructions"  
9. \[[9](http://arxiv.org/abs/2304.03277)\] "GPT-4 Technical Report"  
10. \[[10](http://arxiv.org/abs/1506.06726)\] "Instruction Tuning with GPT-4"  
11. \[[11](http://arxiv.org/abs/2212.09689)\] "The Flan Collection: Designing Data and Methods for Effective Instruction Tuning"  
12. \[[12](http://arxiv.org/abs/2304.08485)\] "Unnatural Instructions: Tuning Language Models with (Almost) No Human Labor"  
13. \[[13](http://arxiv.org/abs/2202.12837)\] "Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?"  
14. \[[14](http://arxiv.org/abs/2301.13688)\] "SQuAD: 100,000+ Questions for Machine Comprehension of Text"  
15. \[[15](http://arxiv.org/abs/1606.05250)\] "MTEB: Massive Text Embedding Benchmark"  
16. \[[16](http://arxiv.org/abs/2210.07316)\] "Dynosaur: A Dynamic Growth Paradigm for Instruction-Tuning Data Curation"  
17. \[[17](http://arxiv.org/abs/2305.14327)\] "Self-Alignment with Instruction Backtranslation"  
18. \[[18](http://arxiv.org/abs/2308.06259)\] "Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments"  
19. \[[19](http://arxiv.org/abs/1711.07280)\] "Text Embeddings by Weakly-Supervised Contrastive Pre-training"  
20. \[[20](http://arxiv.org/abs/2212.03533)\] "Multitask Prompted Training Enables Zero-Shot Task Generalization"
