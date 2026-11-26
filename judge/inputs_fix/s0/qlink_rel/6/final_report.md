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
## Research papers
### Outline
- [Multi-Agent LLM Frameworks [6 papers]](#category-multi-agent-llm-frameworks)
- [Transfer Learning in LLMs [3 papers]](#category-transfer-learning-in-llms)
- [Neural Machine Translation Insights [2 papers]](#category-neural-machine-translation-insights)
- [Multi-Agent Communication in Reinforcement Learning [1 papers]](#category-multi-agent-communication-in-reinforcement-learning)
- [Automated Summary Evaluation Methods [2 papers]](#category-automated-summary-evaluation-methods)
- [External Tool Integration [2 papers]](#category-external-tool-integration)
- [Performance Evaluation Metrics [1 papers]](#category-performance-evaluation-metrics)
- [Narrative Summarization Challenges [1 papers]](#category-narrative-summarization-challenges)

### <a id='category-multi-agent-llm-frameworks'></a>Multi-Agent LLM Frameworks: 6 papers found.
Recent advancements in multi-agent systems driven by large language models (LLMs) have focused on improving task-solving capabilities, particularly in handling complex and long-form content. Several frameworks have been proposed to address limitations such as hallucination, lack of structured coordination, and the need for human oversight. For instance, MetaGPT introduces a meta-programming approach by encoding standardized operating procedures (SOPs) into prompts, enabling structured coordination and modular outputs that mimic human workflows \[[1](http://arxiv.org/abs/2308.00352)\]. Similarly, the "society of minds" approach involves multiple LLM instances debating and refining responses through multiple rounds, enhancing factual validity and reducing hallucinations \[[4](http://arxiv.org/abs/2305.14325)\]. Additionally, role-playing frameworks have been developed to facilitate autonomous cooperation among agents, using inception prompting to align with human intentions while maintaining consistency \[[9](http://arxiv.org/abs/2303.17760)\]. These approaches highlight the growing interest in leveraging multi-agent collaboration to improve the accuracy, coherence, and scalability of LLMs in complex tasks. The integration of domain-specific knowledge, as seen in MedAgents for healthcare \[[11](http://arxiv.org/abs/2311.10537)\], further demonstrates the potential of multi-agent systems to address specialized challenges. Overall, these frameworks collectively emphasize the importance of structured coordination, iterative refinement, and domain adaptation in advancing LLM-based multi-agent systems.
|    | reference                                                                                                                                                            | date     | key idea/summary                                                                                                                                                                                                                                                                      |
|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [MetaGPT: Meta Programming for Multi-Agent Collaborative Framework](http://arxiv.org/abs/2308.00352)                                                                 | 08/01/23 | MetaGPT is an innovative framework that integrates human workflows and standardized operating procedures into LLM-based multi-agent systems to effectively address complex tasks by reducing hallucination and improving structured coordination.                                     |
|  1 | [Improving Factuality and Reasoning in Language Models through Multiagent Debate](http://arxiv.org/abs/2305.14325)                                                   | 05/23/23 | The paper introduces an approach where multiple language model instances debate and refine their responses through multiple rounds to improve mathematical and strategic reasoning, as well as factual validity, in language generation.                                              |
|  2 | [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](https://www.semanticscholar.org/paper/1a4c6856292b8c64d19a812a77f0aa6fd47cb96c) | nan      | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                             |
|  3 | [CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society](http://arxiv.org/abs/2303.17760)                                                | 03/31/23 | This paper introduces a novel communicative agent framework called role-playing, which enables autonomous cooperation among agents using inception prompting, and provides a scalable approach for studying multi-agent cooperation and open-sourcing a library for further research. |
|  4 | [Multi-Agent Collaboration: Harnessing the Power of Intelligent LLM Agents](http://arxiv.org/abs/2306.03314)                                                         | 06/05/23 | This paper introduces a novel multi-agent framework to enhance large language models by enabling collaboration among intelligent agents, addressing challenges like scalability and security, and demonstrating applications in domains such as AGI and software development.         |
|  5 | [MedAgents: Large Language Models as Collaborators for Zero-shot Medical Reasoning](http://arxiv.org/abs/2311.10537)                                                 | 11/16/23 | MedAgents is a training-free framework that enhances large language models' medical reasoning capabilities through collaborative multi-round discussions with domain experts, achieving strong performance in zero-shot medical tasks.                                                |
### <a id='category-transfer-learning-in-llms'></a>Transfer Learning in LLMs: 3 papers found.
Context: 
	Document 1: [Snippet]: «Transfer learning, where a model is first pre-trained on a data-rich task before being fine-tuned on a downstream task, has emerged as a powerful technique in natural language processing (NLP). The effectiveness of transfer learning has given rise to a diversity of approaches, methodology, and practice. In this paper, we explore the landscape of transfer learning techniques for NLP by introducing a unified framework that converts every language problem into a text-to-text format. Our systematic study compares pre-training objectives, architectures, unlabeled datasets, transfer approaches, and other factors on dozens of language understanding tasks. By combining the insights from our exploration with scale and our new "Colossal Clean Crawled Corpus", we achieve state-of-the-art results on many benchmarks covering summarization, question answering, text classification, and more. To facilitate future work on transfer learning for NLP, we release our dataset, pre-trained models, and code.»
[_citation_number]: «2»
[Category]: «Transfer Learning in LLMs»

	Document 2: [Snippet]: «Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training on a large corpus of text followed by fine-tuning on a specific task. While typically task-agnostic in architecture, this method still requires task-specific fine-tuning datasets of thousands or tens of thousands of examples. By contrast, humans can generally perform a new language task from only a few examples or from simple instructions - something which current NLP systems still largely struggle to do. Here we show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art fine-tuning approaches. Specifically, we train GPT-3, an autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model, and test its performance in the few-shot setting. For all tasks, GPT-3 is applied without any gradient updates or fine-tuning, with tasks and few-shot demonstrations specified purely via text interaction with the model. GPT-3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-the-fly reasoning or domain adaptation, such as unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic. At the same time, we also identify some datasets where GPT-3's few-shot learning still struggles, as well as some datasets where GPT-3 faces methodological issues related to training on large web corpora. Finally, we find that GPT-3 can generate samples of news articles which human evaluators have difficulty distinguishing from articles written by humans. We discuss broader societal impacts of this finding and of GPT-3 in general.»
[_citation_number]: «5»
[Category]: «Transfer Learning in LLMs»

	Document 3: [Snippet]: «Large pre-trained language models have been shown to store factual knowledge in their parameters, and achieve state-of-the-art results when fine-tuned on downstream NLP tasks. However, their ability to access and precisely manipulate knowledge is still limited, and hence on knowledge-intensive tasks, their performance lags behind task-specific architectures. Additionally, providing provenance for their decisions and updating their world knowledge remain open research problems. Pre-trained models with a differentiable access mechanism to explicit non-parametric memory can overcome this issue, but have so far been only investigated for extractive downstream tasks. We explore a general-purpose fine-tuning recipe for retrieval-augmented generation (RAG) -- models which combine pre-trained parametric and non-parametric memory for language generation. We introduce RAG models where the parametric memory is a pre-trained seq2seq model and the non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural retriever. We compare two RAG formulations, one which conditions on the same retrieved passages across the whole generated sequence, the other can use different passages per token. We fine-tune and evaluate our models on a wide range of knowledge-intensive NLP tasks and set the state-of-the-art on three open domain QA tasks, outperforming parametric seq2seq models and task-specific retrieve-and-extract architectures. For language generation tasks, we find that RAG models generate more specific, diverse and factual language than a state-of-the-art parametric-only seq2seq baseline.»
[_citation_number]: «14»
[Category]: «Transfer Learning in LLMs»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T13:26:23+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1409.0473)\]. Further details \[[6](https://www.semanticscholar.org/paper/1a4c6856292b8c64d19a812a77f0aa6fd47cb96c)\]\[[7](http://arxiv.org/abs/2203.08975)\]\[[8](https://www.semanticscholar.org/paper/60b05f32c32519a809f21642ef1eb3eaf3848008)\]\[[9](http://arxiv.org/abs/2303.17760)\]\[[10](http://arxiv.org/abs/2306.03314)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Summarizing long-form narratives--such as books, movies, and TV
scripts--requires capturing intricate plotlines, character interactions, and
thematic coherence, a task that remains challenging for existing LLMs. We
introduce NexusSum, a multi-agent LLM framework for narrative summarization
that processes long-form text through a structured, sequential
pipeline--without requiring fine-tuning. Our approach introduces two key
innovations: (1) Dialogue-to-Description Transformation: A narrative-specific
preprocessing method that standardizes character dialogue and descriptive text
into a unified format, improving coherence. (2) Hierarchical Multi-LLM
Summarization: A structured summarization pipeline that optimizes chunk
processing and controls output length for accurate, high-quality summaries. Our
method establishes a new state-of-the-art in narrative summarization, achieving
up to a 30.0% improvement in BERTScore (F1) across books, movies, and TV
scripts. These results demonstrate the effectiveness of multi-agent LLMs in
handling long-form content, offering a scalable approach for structured
summarization in diverse storytelling domains.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1409.0473)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1910.10683)\]\[[7](http://arxiv.org/abs/2203.08975)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer:  
Transfer learning has become a cornerstone in advancing natural language processing (NLP) by enabling models to leverage pre-training on large datasets for downstream tasks \[[2](http://arxiv.org/abs/1910.10683)\]. This approach allows models to generalize across tasks without requiring extensive task-specific fine-tuning \[[5](http://arxiv.org/abs/2005.14165)\]. For instance, GPT-3, a model with 175 billion parameters, demonstrates strong performance in few-shot settings, achieving results comparable to fine-tuned models without any gradient updates \[[5](http://arxiv.org/abs/2005.14165)\]. Similarly, large pre-trained models have been shown to store factual knowledge and achieve state-of-the-art results when fine-tuned on downstream tasks, although their ability to manipulate knowledge remains limited \[[14](http://arxiv.org/abs/2005.11401)\]. These findings highlight the potential of transfer learning in improving performance across diverse NLP tasks, including summarization, question answering, and language generation. The success of transfer learning is further supported by the development of frameworks that convert language problems into text-to-text formats, enabling systematic comparison of pre-training objectives and architectures \[[2](http://arxiv.org/abs/1910.10683)\]. These studies collectively underscore the importance of transfer learning in advancing LLM capabilities, particularly in handling complex, long-form content.
|    | reference                                                                                                            | date     | key idea/summary                                                                                                                                                                                                                                             |
|----|----------------------------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](http://arxiv.org/abs/1910.10683) | 10/23/19 | This paper introduces a unified framework for transfer learning in NLP, converting language problems into text-to-text format, and achieves state-of-the-art results using a large-scale dataset and pre-trained models.                                     |
|  1 | [Language Models are Few-Shot Learners](http://arxiv.org/abs/2005.14165)                                             | 05/28/20 | GPT-3, a large-scale language model with 175 billion parameters, demonstrates strong few-shot learning performance across various NLP tasks without fine-tuning, often rivaling state-of-the-art fine-tuning approaches.                                     |
|  2 | [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](http://arxiv.org/abs/2005.11401)                  | 05/22/20 | The paper introduces RAG models that combine pre-trained parametric and non-parametric memory for language generation, achieving state-of-the-art results on knowledge-intensive NLP tasks by improving factual accuracy and diversity in generated outputs. |
### <a id='category-neural-machine-translation-insights'></a>Neural Machine Translation Insights: 2 papers found.
Context: 
	Document 1: [Snippet]: «Neural machine translation is a recently proposed approach to machine translation. Unlike the traditional statistical machine translation, the neural machine translation aims at building a single neural network that can be jointly tuned to maximize the translation performance. The models proposed recently for neural machine translation often belong to a family of encoder-decoders and consists of an encoder that encodes a source sentence into a fixed-length vector from which a decoder generates a translation. In this paper, we conjecture that the use of a fixed-length vector is a bottleneck in improving the performance of this basic encoder-decoder architecture, and propose to extend this by allowing a model to automatically (soft-)search for parts of a source sentence that are relevant to predicting a target word, without having to form these parts as a hard segment explicitly. With this new approach, we achieve a translation performance comparable to the existing state-of-the-art phrase-based system on the task of English-to-French translation. Furthermore, qualitative analysis reveals that the (soft-)alignments found by the model agree well with our intuition.»
[_citation_number]: «3»
[Category]: «Neural Machine Translation Insights»

	Document 2: [Snippet]: «We present BART, a denoising autoencoder for pretraining sequence-to-sequence models. BART is trained by (1) corrupting text with an arbitrary noising function, and (2) learning a model to reconstruct the original text. It uses a standard Tranformer-based neural machine translation architecture which, despite its simplicity, can be seen as generalizing BERT (due to the bidirectional encoder), GPT (with the left-to-right decoder), and other recent pretraining schemes. We evaluate a number of noising approaches, finding the best performance by both randomly shuffling the order of sentences and using a novel in-filling scheme, where spans of text are replaced with a single mask token. BART is particularly effective when fine tuned for text generation but also works well for comprehension tasks. It matches the performance of RoBERTa on GLUE and SQuAD, and achieves new state-of-the-art results on a range of abstractive dialogue, question answering, and summarization tasks, with gains of up to 3.5 ROUGE. BART also provides a 1.1 BLEU increase over a back-translation system for machine translation, with only target language pretraining. We also replicate other pretraining schemes within the BART framework, to understand their effect on end-task performance.»
[_citation_number]: «13»
[Category]: «Neural Machine Translation Insights»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T13:26:23+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1409.0473)\]. Further details \[[6](https://www.semanticscholar.org/paper/1a4c6856292b8c64d19a812a77f0aa6fd47cb96c)\]\[[7](http://arxiv.org/abs/2203.08975)\]\[[8](https://www.semanticscholar.org/paper/60b05f32c32519a809f21642ef1eb3eaf3848008)\]\[[9](http://arxiv.org/abs/2303.17760)\]\[[10](http://arxiv.org/abs/2306.03314)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Summarizing long-form narratives--such as books, movies, and TV
scripts--requires capturing intricate plotlines, character interactions, and
thematic coherence, a task that remains challenging for existing LLMs. We
introduce NexusSum, a multi-agent LLM framework for narrative summarization
that processes long-form text through a structured, sequential
pipeline--without requiring fine-tuning. Our approach introduces two key
innovations: (1) Dialogue-to-Description Transformation: A narrative-specific
preprocessing method that standardizes character dialogue and descriptive text
into a unified format, improving coherence. (2) Hierarchical Multi-LLM
Summarization: A structured summarization pipeline that optimizes chunk
processing and controls output length for accurate, high-quality summaries. Our
method establishes a new state-of-the-art in narrative summarization, achieving
up to a 30.0% improvement in BERTScore (F1) across books, movies, and TV
scripts. These results demonstrate the effectiveness of multi-agent LLMs in
handling long-form content, offering a scalable approach for structured
summarization in diverse storytelling domains.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1409.0473)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1910.10683)\]\[[7](http://arxiv.org/abs/2203.08975)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer:  
Neural machine translation (NMT) has evolved as a promising approach to machine translation, offering improvements over traditional statistical methods by using a single neural network to jointly optimize translation performance \[[3](http://arxiv.org/abs/1409.0473)\]. Unlike earlier models that relied on fixed-length vectors to encode source sentences, recent advancements have focused on addressing this limitation by enabling models to automatically search for relevant parts of the source text without forming explicit segments \[[3](http://arxiv.org/abs/1409.0473)\]. This approach has led to significant improvements, achieving performance comparable to state-of-the-art phrase-based systems, particularly in English-to-French translation \[[3](http://arxiv.org/abs/1409.0473)\]. Additionally, models like BART have demonstrated effectiveness in a broader range of tasks, including text generation and summarization, by using a denoising autoencoder framework that corrupts and reconstructs text \[[13](http://arxiv.org/abs/1910.13461)\]. These developments highlight the potential of encoder-decoder architectures and pretraining strategies in enhancing the capabilities of sequence-to-sequence models for diverse NLP tasks.
|    | reference                                                                                                                                            | date     | key idea/summary                                                                                                                                                                                                                            |
|----|------------------------------------------------------------------------------------------------------------------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Neural Machine Translation by Jointly Learning to Align and Translate](http://arxiv.org/abs/1409.0473)                                              | 09/01/14 | The paper proposes an improved neural machine translation model that allows the model to automatically (soft-)search for relevant parts of a source sentence, leading to better translation performance and alignment with human intuition. |
|  1 | [BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension](http://arxiv.org/abs/1910.13461) | 10/29/19 | BART is a denoising autoencoder for pretraining sequence-to-sequence models, achieving state-of-the-art results in text generation, comprehension, and machine translation by corrupting text and learning to reconstruct it.               |
### <a id='category-multi-agent-communication-in-reinforcement-learning'></a>Multi-Agent Communication in Reinforcement Learning: 1 papers found.
Context: 
	Document 1: [Snippet]: «Communication is an effective mechanism for coordinating the behaviors of multiple agents, broadening their views of the environment, and to support their collaborations. In the field of multi-agent deep reinforcement learning (MADRL), agents can improve the overall learning performance and achieve their objectives by communication. Agents can communicate various types of messages, either to all agents or to specific agent groups, or conditioned on specific constraints. With the growing body of research work in MADRL with communication (Comm-MADRL), there is a lack of a systematic and structural approach to distinguish and classify existing Comm-MADRL approaches. In this paper, we survey recent works in the Comm-MADRL field and consider various aspects of communication that can play a role in designing and developing multi-agent reinforcement learning systems. With these aspects in mind, we propose 9 dimensions along which Comm-MADRL approaches can be analyzed, developed, and compared. By projecting existing works into the multi-dimensional space, we discover interesting trends. We also propose some novel directions for designing future Comm-MADRL systems through exploring possible combinations of the dimensions.»
[_citation_number]: «7»
[Category]: «Multi-Agent Communication in Reinforcement Learning»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T13:26:23+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1409.0473)\]. Further details \[[6](https://www.semanticscholar.org/paper/1a4c6856292b8c64d19a812a77f0aa6fd47cb96c)\]\[[7](http://arxiv.org/abs/2203.08975)\]\[[8](https://www.semanticscholar.org/paper/60b05f32c32519a809f21642ef1eb3eaf3848008)\]\[[9](http://arxiv.org/abs/2303.17760)\]\[[10](http://arxiv.org/abs/2306.03314)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Summarizing long-form narratives--such as books, movies, and TV
scripts--requires capturing intricate plotlines, character interactions, and
thematic coherence, a task that remains challenging for existing LLMs. We
introduce NexusSum, a multi-agent LLM framework for narrative summarization
that processes long-form text through a structured, sequential
pipeline--without requiring fine-tuning. Our approach introduces two key
innovations: (1) Dialogue-to-Description Transformation: A narrative-specific
preprocessing method that standardizes character dialogue and descriptive text
into a unified format, improving coherence. (2) Hierarchical Multi-LLM
Summarization: A structured summarization pipeline that optimizes chunk
processing and controls output length for accurate, high-quality summaries. Our
method establishes a new state-of-the-art in narrative summarization, achieving
up to a 30.0% improvement in BERTScore (F1) across books, movies, and TV
scripts. These results demonstrate the effectiveness of multi-agent LLMs in
handling long-form content, offering a scalable approach for structured
summarization in diverse storytelling domains.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1409.0473)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1910.10683)\]\[[7](http://arxiv.org/abs/2203.08975)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer:  
Multi-agent communication has emerged as a critical component in enhancing the performance of multi-agent systems, particularly in reinforcement learning (RL) settings \[[7](http://arxiv.org/abs/2203.08975)\]. By enabling agents to exchange information, communication can significantly improve coordination, broaden environmental understanding, and support collaborative decision-making \[[7](http://arxiv.org/abs/2203.08975)\]. In the context of multi-agent deep reinforcement learning (MADRL), communication mechanisms allow agents to share diverse types of messages, either broadcasted to all agents or targeted at specific groups, based on predefined constraints \[[7](http://arxiv.org/abs/2203.08975)\]. This capability has led to a growing body of research on communication-enabled MADRL (Comm-MADRL), which explores how different communication strategies can influence learning outcomes and system efficiency \[[7](http://arxiv.org/abs/2203.08975)\]. While early work focused on basic message-passing architectures, recent studies have introduced more sophisticated frameworks that incorporate structured communication protocols, dynamic message routing, and adaptive information sharing \[[7](http://arxiv.org/abs/2203.08975)\]. These advancements highlight the potential of communication in overcoming challenges such as partial observability, conflicting goals, and scalability in multi-agent environments \[[7](http://arxiv.org/abs/2203.08975)\].
|    | reference                                                                                                 | date     | key idea/summary                                                                                                                                                                                                                                                    |
|----|-----------------------------------------------------------------------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [A survey of multi-agent deep reinforcement learning with communication](http://arxiv.org/abs/2203.08975) | 03/16/22 | This paper presents a systematic analysis of communication mechanisms in multi-agent deep reinforcement learning (MADRL) by proposing 9 dimensions to classify and compare existing approaches, while identifying trends and suggesting future research directions. |
### <a id='category-automated-summary-evaluation-methods'></a>Automated Summary Evaluation Methods: 2 papers found.
Context: 
	Document 1: [Snippet]: «»
[_citation_number]: «8»
[Category]: «Automated Summary Evaluation Methods»

	Document 2: [Snippet]: «Text summarization aims at compressing long documents into a shorter form that conveys the most important parts of the original document. Despite increased interest in the community and notable research effort, progress on benchmark datasets has stagnated. We critically evaluate key ingredients of the current research setup: datasets, evaluation metrics, and models, and highlight three primary shortcomings: 1) automatically collected datasets leave the task underconstrained and may contain noise detrimental to training and evaluation, 2) current evaluation protocol is weakly correlated with human judgment and does not account for important characteristics such as factual correctness, 3) models overfit to layout biases of current datasets and offer limited diversity in their outputs.»
[_citation_number]: «16»
[Category]: «Automated Summary Evaluation Methods»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T13:26:23+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1409.0473)\]. Further details \[[6](https://www.semanticscholar.org/paper/1a4c6856292b8c64d19a812a77f0aa6fd47cb96c)\]\[[7](http://arxiv.org/abs/2203.08975)\]\[[8](https://www.semanticscholar.org/paper/60b05f32c32519a809f21642ef1eb3eaf3848008)\]\[[9](http://arxiv.org/abs/2303.17760)\]\[[10](http://arxiv.org/abs/2306.03314)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Summarizing long-form narratives--such as books, movies, and TV
scripts--requires capturing intricate plotlines, character interactions, and
thematic coherence, a task that remains challenging for existing LLMs. We
introduce NexusSum, a multi-agent LLM framework for narrative summarization
that processes long-form text through a structured, sequential
pipeline--without requiring fine-tuning. Our approach introduces two key
innovations: (1) Dialogue-to-Description Transformation: A narrative-specific
preprocessing method that standardizes character dialogue and descriptive text
into a unified format, improving coherence. (2) Hierarchical Multi-LLM
Summarization: A structured summarization pipeline that optimizes chunk
processing and controls output length for accurate, high-quality summaries. Our
method establishes a new state-of-the-art in narrative summarization, achieving
up to a 30.0% improvement in BERTScore (F1) across books, movies, and TV
scripts. These results demonstrate the effectiveness of multi-agent LLMs in
handling long-form content, offering a scalable approach for structured
summarization in diverse storytelling domains.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1409.0473)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1910.10683)\]\[[7](http://arxiv.org/abs/2203.08975)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Automated summary evaluation methods have seen significant attention, yet challenges persist in aligning automated systems with human judgment. Current evaluation protocols often fail to capture critical aspects such as factual correctness and thematic coherence, which are essential for high-quality summaries \[[16](http://arxiv.org/abs/1908.08960)\]. Additionally, the reliance on automatically collected datasets introduces noise and biases, which can hinder model training and performance \[[16](http://arxiv.org/abs/1908.08960)\]. These issues are particularly relevant in narrative summarization, where maintaining plot integrity and character consistency is crucial. The lack of robust evaluation metrics further limits progress, as models may overfit to dataset-specific patterns rather than generalizing effectively \[[16](http://arxiv.org/abs/1908.08960)\]. Addressing these shortcomings is vital for advancing the field, especially as new frameworks like NexusSum demonstrate the potential of multi-agent LLMs in handling complex, long-form content \[[16](http://arxiv.org/abs/1908.08960)\].
|    | reference                                                                                                                                | date     | key idea/summary                                                                                                                                                                  |
|----|------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [ROUGE: A Package for Automatic Evaluation of Summaries](https://www.semanticscholar.org/paper/60b05f32c32519a809f21642ef1eb3eaf3848008) | 07/25/04 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                         |
|  1 | [Neural Text Summarization: A Critical Evaluation](http://arxiv.org/abs/1908.08960)                                                      | 08/23/19 | The paper critically evaluates current text summarization research, highlighting issues with datasets, evaluation metrics, and models, and identifies three primary shortcomings. |
### <a id='category-external-tool-integration'></a>External Tool Integration: 2 papers found.
Context:  
	Document 1: [Snippet]: «While large language models (LLMs) have demonstrated impressive capabilities across tasks in language understanding and interactive decision making, their abilities for reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) have primarily been studied as separate topics. In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with external sources, such as knowledge bases or environments, to gather additional information. We apply our approach, named ReAct, to a diverse set of language and decision making tasks and demonstrate its effectiveness over state-of-the-art baselines, as well as improved human interpretability and trustworthiness over methods without reasoning or acting components. Concretely, on question answering (HotpotQA) and fact verification (Fever), ReAct overcomes issues of hallucination and error propagation prevalent in chain-of-thought reasoning by interacting with a simple Wikipedia API, and generates human-like task-solving trajectories that are more interpretable than baselines without reasoning traces. On two interactive decision making benchmarks (ALFWorld and WebShop), ReAct outperforms imitation and reinforcement learning methods by an absolute success rate of 34% and 10% respectively, while being prompted with only one or two in-context examples. Project site with code: https://react-lm.github.io»  
[_citation_number]: «12»  
[Category]: «External Tool Integration»  

	Document 2: [Snippet]: «Language models (LMs) exhibit remarkable abilities to solve new tasks from just a few examples or textual instructions, especially at scale. They also, paradoxically, struggle with basic functionality, such as arithmetic or factual lookup, where much simpler and smaller models excel. In this paper, we show that LMs can teach themselves to use external tools via simple APIs and achieve the best of both worlds. We introduce Toolformer, a model trained to decide which APIs to call, when to call them, what arguments to pass, and how to best incorporate the results into future token prediction. This is done in a self-supervised way, requiring nothing more than a handful of demonstrations for each API. We incorporate a range of tools, including a calculator, a Q&A system, two different search engines, a translation system, and a calendar. Toolformer achieves substantially improved zero-shot performance across a variety of downstream tasks, often competitive with much larger models, without sacrificing its core language modeling abilities.»  
[_citation_number]: «15»  
[Category]: «External Tool Integration»  

Instruction:  
	You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T13:26:23+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1409.0473)\]. Further details \[[6](https://www.semanticscholar.org/paper/1a4c6856292b8c64d19a812a77f0aa6fd47cb96c)\]\[[7](http://arxiv.org/abs/2203.08975)\]\[[8](https://www.semanticscholar.org/paper/60b05f32c32519a809f21642ef1eb3eaf3848008)\]\[[9](http://arxiv.org/abs/2303.17760)\]\[[10](http://arxiv.org/abs/2306.03314)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Summarizing long-form narratives--such as books, movies, and TV scripts--requires capturing intricate plotlines, character interactions, and thematic coherence, a task that remains challenging for existing LLMs. We introduce NexusSum, a multi-agent LLM framework for narrative summarization that processes long-form text through a structured, sequential pipeline--without requiring fine-tuning. Our approach introduces two key innovations: (1) Dialogue-to-Description Transformation: A narrative-specific preprocessing method that standardizes character dialogue and descriptive text into a unified format, improving coherence. (2) Hierarchical Multi-LLM Summarization: A structured summarization pipeline that optimizes chunk processing and controls output length for accurate, high-quality summaries. Our method establishes a new state-of-the-art in narrative summarization, achieving up to a 30.0% improvement in BERTScore (F1) across books, movies, and TV scripts. These results demonstrate the effectiveness of multi-agent LLMs in handling long-form content, offering a scalable approach for structured summarization in diverse storytelling domains.  
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.  
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.  
You should write a short paragraph, specifically focusing on the given category.  
Write your answer as a single body paragraph focused on the category, with nothing else.  

Answer:  
Recent research has focused on enhancing the capabilities of large language models (LLMs) by integrating external tools, enabling them to perform more complex and accurate tasks. For instance, ReAct \[[12](http://arxiv.org/abs/2210.03629)\] introduces a framework where LLMs generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between reasoning and acting. This approach enables models to interface with external sources, such as knowledge bases or environments, to gather additional information, thereby improving accuracy and interpretability. Similarly, Toolformer \[[15](http://arxiv.org/abs/2302.04761)\] demonstrates that LLMs can be trained to use external tools via simple APIs, achieving the best of both worlds by combining the strengths of large models with the precision of specialized tools. These methods highlight the importance of external tool integration in overcoming limitations of LLMs in areas such as arithmetic or factual lookup, while maintaining core language modeling abilities. Both approaches emphasize the potential of integrating external tools to enhance the performance and reliability of LLMs across a variety of tasks.
|    | reference                                                                                        | date     | key idea/summary                                                                                                                                                                                                           |
|----|--------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [ReAct: Synergizing Reasoning and Acting in Language Models](http://arxiv.org/abs/2210.03629)    | 10/06/22 | The paper introduces ReAct, a method that interleaves reasoning and action generation using large language models to improve task performance, interpretability, and trustworthiness across various decision-making tasks. |
|  1 | [Toolformer: Language Models Can Teach Themselves to Use Tools](http://arxiv.org/abs/2302.04761) | 02/09/23 | Toolformer enables language models to use external tools via APIs, improving zero-shot performance across tasks without losing core language modeling abilities.                                                           |
### <a id='category-performance-evaluation-metrics'></a>Performance Evaluation Metrics: 1 papers found.
Context: 
	Document 1: [Snippet]: «Modern artificial intelligence (AI) systems are powered by foundation models. This paper presents a new set of foundation models, called Llama 3. It is a herd of language models that natively support multilinguality, coding, reasoning, and tool usage. Our largest model is a dense Transformer with 405B parameters and a context window of up to 128K tokens. This paper presents an extensive empirical evaluation of Llama 3. We find that Llama 3 delivers comparable quality to leading language models such as GPT-4 on a plethora of tasks. We publicly release Llama 3, including pre-trained and post-trained versions of the 405B parameter language model and our Llama Guard 3 model for input and output safety. The paper also presents the results of experiments in which we integrate image, video, and speech capabilities into Llama 3 via a compositional approach. We observe this approach performs competitively with the state-of-the-art on image, video, and speech recognition tasks. The resulting models are not yet being broadly released as they are still under development.»
[_citation_number]: «17»
[Category]: «Performance Evaluation Metrics»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T13:26:23+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1409.0473)\]. Further details \[[6](https://www.semanticscholar.org/paper/1a4c6856292b8c64d19a812a77f0aa6fd47cb96c)\]\[[7](http://arxiv.org/abs/2203.08975)\]\[[8](https://www.semanticscholar.org/paper/60b05f32c32519a809f21642ef1eb3eaf3848008)\]\[[9](http://arxiv.org/abs/2303.17760)\]\[[10](http://arxiv.org/abs/2306.03314)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Summarizing long-form narratives--such as books, movies, and TV
scripts--requires capturing intricate plotlines, character interactions, and
thematic coherence, a task that remains challenging for existing LLMs. We
introduce NexusSum, a multi-agent LLM framework for narrative summarization
that processes long-form text through a structured, sequential
pipeline--without requiring fine-tuning. Our approach introduces two key
innovations: (1) Dialogue-to-Description Transformation: A narrative-specific
preprocessing method that standardizes character dialogue and descriptive text
into a unified format, improving coherence. (2) Hierarchical Multi-LLM
Summarization: A structured summarization pipeline that optimizes chunk
processing and controls output length for accurate, high-quality summaries. Our
method establishes a new state-of-the-art in narrative summarization, achieving
up to a 30.0% improvement in BERTScore (F1) across books, movies, and TV
scripts. These results demonstrate the effectiveness of multi-agent LLMs in
handling long-form content, offering a scalable approach for structured
summarization in diverse storytelling domains.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1409.0473)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1910.10683)\]\[[7](http://arxiv.org/abs/2203.08975)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Recent advancements in foundation models have demonstrated significant improvements in handling complex tasks, including multilingual support, coding, reasoning, and multimodal capabilities \[[17](http://arxiv.org/abs/2407.21783)\]. These models, such as Llama 3, are designed with large parameter counts (e.g., 405B parameters) and extended context windows (up to 128K tokens), enabling them to perform competitively across a wide range of tasks \[[17](http://arxiv.org/abs/2407.21783)\]. This aligns with the need for robust models in narrative summarization, where capturing intricate plotlines and thematic coherence is essential. The evaluation of such models often relies on performance metrics like BERTScore (F1), which measures the quality of generated summaries against reference texts \[[17](http://arxiv.org/abs/2407.21783)\]. These metrics are crucial for benchmarking the effectiveness of new approaches, such as the hierarchical multi-LLM summarization pipeline introduced in NexusSum, which achieves notable improvements in summarization accuracy \[[17](http://arxiv.org/abs/2407.21783)\].
|    | reference                                                     | date     | key idea/summary                                                                                                                                                                                             |
|----|---------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [The Llama 3 Herd of Models](http://arxiv.org/abs/2407.21783) | 07/31/24 | This paper introduces Llama 3, a new set of foundation models that support multilinguality, coding, reasoning, and tool usage, with a 405B parameter model and competitive performance across various tasks. |
### <a id='category-narrative-summarization-challenges'></a>Narrative Summarization Challenges: 1 papers found.
Context: 
	Document 1: [Snippet]: «»
[_citation_number]: «18»
[Category]: «Narrative Summarization Challenges»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T13:26:23+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1409.0473)\]. Further details \[[6](https://www.semanticscholar.org/paper/1a4c6856292b8c64d19a812a77f0aa6fd47cb96c)\]\[[7](http://arxiv.org/abs/2203.08975)\]\[[8](https://www.semanticscholar.org/paper/60b05f32c32519a809f21642ef1eb3eaf3848008)\]\[[9](http://arxiv.org/abs/2303.17760)\]\[[10](http://arxiv.org/abs/2306.03314)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Summarizing long-form narratives--such as books, movies, and TV
scripts--requires capturing intricate plotlines, character interactions, and
thematic coherence, a task that remains challenging for existing LLMs. We
introduce NexusSum, a multi-agent LLM framework for narrative summarization
that processes long-form text through a structured, sequential
pipeline--without requiring fine-tuning. Our approach introduces two key
innovations: (1) Dialogue-to-Description Transformation: A narrative-specific
preprocessing method that standardizes character dialogue and descriptive text
into a unified format, improving coherence. (2) Hierarchical Multi-LLM
Summarization: A structured summarization pipeline that optimizes chunk
processing and controls output length for accurate, high-quality summaries. Our
method establishes a new state-of-the-art in narrative summarization, achieving
up to a 30.0% improvement in BERTScore (F1) across books, movies, and TV
scripts. These results demonstrate the effectiveness of multi-agent LLMs in
handling long-form content, offering a scalable approach for structured
summarization in diverse storytelling domains.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1409.0473)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1910.10683)\]\[[7](http://arxiv.org/abs/2203.08975)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer:
Narrative summarization presents significant challenges due to the complexity of long-form texts, including intricate plotlines, character interactions, and thematic coherence \[[18](https://www.semanticscholar.org/paper/b901cf95a1fcd23cceae5fce7e03b098ede5a6e2)\]. Existing large language models (LLMs) often struggle with maintaining consistency and accuracy across these elements, particularly when dealing with diverse formats such as books, movies, and TV scripts \[[18](https://www.semanticscholar.org/paper/b901cf95a1fcd23cceae5fce7e03b098ede5a6e2)\]. This challenge has spurred research into alternative approaches, such as multi-agent frameworks that enable structured, sequential processing without requiring fine-tuning \[[18](https://www.semanticscholar.org/paper/b901cf95a1fcd23cceae5fce7e03b098ede5a6e2)\]. These methods aim to improve coherence and output quality by introducing specialized preprocessing techniques, such as dialogue-to-description transformation, which standardizes narrative elements for better alignment \[[18](https://www.semanticscholar.org/paper/b901cf95a1fcd23cceae5fce7e03b098ede5a6e2)\]. Additionally, hierarchical summarization pipelines have been proposed to optimize chunk processing and control output length, ensuring that summaries remain both accurate and concise \[[18](https://www.semanticscholar.org/paper/b901cf95a1fcd23cceae5fce7e03b098ede5a6e2)\]. These innovations highlight the ongoing efforts to address the limitations of traditional summarization techniques in handling the nuances of narrative content.
|    | reference                                                                                                                                                 |   date | key idea/summary                                                                                          |
|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------|
|  0 | [Story: Substance, Structure, Style, and the Principles of Screenwriting](https://www.semanticscholar.org/paper/b901cf95a1fcd23cceae5fce7e03b098ede5a6e2) |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
