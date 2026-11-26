## Related Works

Narrative summarization, which involves condensing long-form texts such as books, movies, and TV scripts into coherent and accurate summaries, remains a challenging task for large language models (LLMs). Existing approaches often struggle with maintaining thematic coherence, capturing intricate plotlines, and preserving character interactions \[[16](http://arxiv.org/abs/1908.08960)\]. This challenge is exacerbated by the lack of fine-tuning, which is typically required to adapt LLMs to specific tasks \[[5](http://arxiv.org/abs/2005.14165)\]. In contrast, our proposed NexusSum framework introduces a multi-agent LLM approach that enables structured, sequential processing of long-form narratives without the need for fine-tuning \[[1](http://arxiv.org/abs/2308.00352)\].

Several studies have explored the use of multi-agent systems to enhance the performance of LLMs in complex tasks. For instance, MetaGPT introduces a framework that incorporates standardized operating procedures (SOPs) into prompts to improve structured coordination among agents \[[1](http://arxiv.org/abs/2308.00352)\]. This approach mandates modular outputs, allowing agents to validate their work and minimize compounded errors. Similarly, AutoGen enables next-generation LLM applications through a multi-agent conversation framework, facilitating collaborative problem-solving \[[6](https://www.semanticscholar.org/paper/1a4c6856292b8c64d19a812a77f0aa6fd47cb96c)\]. These frameworks highlight the potential of multi-agent systems to improve task performance by leveraging structured collaboration and role assignment.

In the realm of multi-agent deep reinforcement learning, communication has been identified as a key mechanism for coordinating behaviors and improving learning performance \[[7](http://arxiv.org/abs/2203.08975)\]. This aligns with the principles of our NexusSum framework, which uses a structured pipeline to optimize chunk processing and control output length. The hierarchical multi-LLM summarization approach in NexusSum is inspired by the modular and task-specific design of such systems, ensuring that each agent contributes effectively to the overall summarization process \[[1](http://arxiv.org/abs/2308.00352)\].

The use of external tools to enhance LLM capabilities has also been explored. For example, Toolformer demonstrates that LLMs can be trained to use external APIs, such as calculators and search engines, to improve their performance on tasks requiring factual lookup or arithmetic \[[15](http://arxiv.org/abs/2302.04761)\]. This is particularly relevant to our work, as our framework leverages structured processing to ensure accurate and coherent outputs, similar to how external tools can be used to validate and refine results.

Additionally, the importance of structured preprocessing in improving the quality of generated outputs has been emphasized in several studies. For example, the Dialogue-to-Description Transformation in NexusSum is inspired by the need to standardize input formats to improve coherence and consistency \[[1](http://arxiv.org/abs/2308.00352)\]. This is consistent with findings from the field of neural machine translation, where the use of encoder-decoder architectures has been shown to improve translation performance by allowing models to automatically search for relevant parts of the source sentence \[[3](http://arxiv.org/abs/1409.0473)\].

In summary, the related works highlight the potential of multi-agent systems, structured preprocessing, and external tools in improving the performance of LLMs on complex tasks such as narrative summarization. Our NexusSum framework builds upon these insights, offering a scalable and effective approach to structured summarization of long-form narratives.

References:  
\[[1](http://arxiv.org/abs/2308.00352)\] MetaGPT: Meta Programming for Multi-Agent Collaborative Framework  
\[[2](http://arxiv.org/abs/1910.10683)\] Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer  
\[[3](http://arxiv.org/abs/1409.0473)\] Neural Machine Translation by Jointly Learning to Align and Translate  
\[[4](http://arxiv.org/abs/2305.14325)\] Improving Factuality and Reasoning in Language Models through Multiagent Debate  
\[[5](http://arxiv.org/abs/2005.14165)\] Language Models are Few-Shot Learners  
\[[6](https://www.semanticscholar.org/paper/1a4c6856292b8c64d19a812a77f0aa6fd47cb96c)\] AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework  
\[[7](http://arxiv.org/abs/2203.08975)\] A survey of multi-agent deep reinforcement learning with communication  
\[[8](https://www.semanticscholar.org/paper/60b05f32c32519a809f21642ef1eb3eaf3848008)\] ROUGE: A Package for Automatic Evaluation of Summaries  
\[[9](http://arxiv.org/abs/2303.17760)\] CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society  
\[[10](http://arxiv.org/abs/2306.03314)\] Multi-Agent Collaboration: Harnessing the Power of Intelligent LLM Agents  
\[[11](http://arxiv.org/abs/2311.10537)\] MedAgents: Large Language Models as Collaborators for Zero-shot Medical Reasoning  
\[[12](http://arxiv.org/abs/2210.03629)\] ReAct: Synergizing Reasoning and Acting in Language Models  
\[[13](http://arxiv.org/abs/1910.13461)\] BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension  
\[[14](http://arxiv.org/abs/2005.11401)\] Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks  
\[[15](http://arxiv.org/abs/2302.04761)\] Toolformer: Language Models Can Teach Themselves to Use Tools  
\[[16](http://arxiv.org/abs/1908.08960)\] Neural Text Summarization: A Critical Evaluation
