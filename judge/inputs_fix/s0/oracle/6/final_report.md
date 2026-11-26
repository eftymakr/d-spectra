## Related Works

Long-form narrative summarization, encompassing books, movies, and TV scripts, remains a challenging task for existing large language models (LLMs) due to the complexity of capturing intricate plotlines, character interactions, and thematic coherence \[[13](http://arxiv.org/abs/2310.00785)\]. Prior work has explored various approaches to address these challenges, including abstractive summarization techniques, efficient attention mechanisms, and multi-agent collaboration frameworks. For instance, \[[2](http://arxiv.org/abs/2404.03561)\] introduced a two-stage abstractive summarization approach for movie scripts, where salient scenes are first identified and then used to generate summaries. This work highlights the importance of focusing on key narrative elements to improve summary quality. Similarly, \[[12](http://arxiv.org/abs/2406.02818)\] proposed Chain-of-Agents (CoA), a framework that enables multi-agent collaboration to process long-context tasks, mitigating the limitations of input reduction and window extension strategies. CoA processes the entire input by interleaving reading and reasoning, assigning each agent a short context to maintain focus on pertinent information.

Efficient attention mechanisms have also been crucial in enabling the processing of long sequences. Models such as Longformer \[[4](http://arxiv.org/abs/2004.05150)\], Reformer \[[5](http://arxiv.org/abs/2001.04451)\], and Linformer \[[6](http://arxiv.org/abs/2006.04768)\] have been developed to reduce the computational and memory costs associated with standard self-attention mechanisms. Longformer, for example, uses a combination of local and global attention to handle long documents, while Reformer employs locality-sensitive hashing to reduce attention complexity. Linformer further simplifies the attention mechanism by approximating it with a low-rank matrix, achieving linear complexity in both time and space. These advancements have made it possible to process long documents without truncation, which is essential for narrative summarization tasks.

In addition to attention mechanisms, the use of pre-trained models and fine-tuning strategies has played a significant role in improving summarization performance. \[[11](http://arxiv.org/abs/2501.01805)\] proposed CachED, an approach that enables end-to-end training of encoder-decoder models for long document summarization without input truncation. This method uses gradient caching to manage memory consumption during training, allowing models to process extensive documents. Similarly, \[[7](http://arxiv.org/abs/2306.15595)\] introduced Position Interpolation, which extends the context window sizes of RoPE-based LLMs to up to 32768 tokens with minimal fine-tuning, demonstrating strong performance on tasks requiring long context.

The importance of structured summarization pipelines has also been emphasized in recent work. \[[13](http://arxiv.org/abs/2310.00785)\] explored the challenges of summarizing book-length documents, highlighting the need for chunking and merging strategies to maintain coherence. They introduced BooookScore, an automatic metric to evaluate the quality of LLM-generated summaries, identifying common coherence errors and measuring their impact. This work underscores the need for robust evaluation methods when assessing long-form narrative summaries.

In summary, the field of long-form narrative summarization has seen significant advancements through the development of efficient attention mechanisms, multi-agent collaboration frameworks, and structured summarization pipelines. These approaches collectively address the challenges of capturing complex narratives and maintaining coherence in summaries.

References:  
\[[1](http://arxiv.org/abs/2005.01840)\] [Document 1]  
\[[2](http://arxiv.org/abs/2404.03561)\] [Document 2]  
\[[3](http://arxiv.org/abs/2007.14062)\] [Document 3]  
\[[4](http://arxiv.org/abs/2004.05150)\] [Document 4]  
\[[5](http://arxiv.org/abs/2001.04451)\] [Document 5]  
\[[6](http://arxiv.org/abs/2006.04768)\] [Document 6]  
\[[7](http://arxiv.org/abs/2306.15595)\] [Document 7]  
\[[8](http://arxiv.org/abs/2307.03172)\] [Document 8]  
\[[9](http://arxiv.org/abs/2208.00748)\] [Document 9]  
\[[10](http://arxiv.org/abs/2305.01625)\] [Document 10]  
\[[11](http://arxiv.org/abs/2501.01805)\] [Document 11]  
\[[12](http://arxiv.org/abs/2406.02818)\] [Document 12]  
\[[13](http://arxiv.org/abs/2310.00785)\] [Document 13]
## Research papers
### Outline
- [Narrative Summarization Challenges [1 papers]](#category-narrative-summarization-challenges)
- [Abstractive Summarization Techniques [1 papers]](#category-abstractive-summarization-techniques)
- [Long-Context Processing Methods [10 papers]](#category-long-context-processing-methods)
- [Efficient Attention Mechanisms [2 papers]](#category-efficient-attention-mechanisms)
- [Coherence and Quality Assessment [1 papers]](#category-coherence-and-quality-assessment)
- [Evaluation Metrics for Summaries [1 papers]](#category-evaluation-metrics-for-summaries)
- [Structured Summarization Pipelines [1 papers]](#category-structured-summarization-pipelines)

### <a id='category-narrative-summarization-challenges'></a>Narrative Summarization Challenges: 1 papers found.
Context: 
	Document 1: [Category]: «Narrative Summarization Challenges»
[_citation_number]: «1»
[Snippet]: «We present a new summarization task, generating summaries of novel chapters using summary/chapter pairs from online study guides. This is a harder task than the news summarization task, given the chapter length as well as the extreme paraphrasing and generalization found in the summaries. We focus on extractive summarization, which requires the creation of a gold-standard set of extractive summaries. We present a new metric for aligning reference summary sentences with chapter sentences to create gold extracts and also experiment with different alignment methods. Our experiments demonstrate significant improvement over prior alignment approaches for our task as shown through automatic metrics and a crowd-sourced pyramid analysis. We make our data collection scripts available at https://github.com/manestay/novel-chapter-dataset .»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T13:26:23+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2007.14062)\]. Further details \[[6](http://arxiv.org/abs/2006.04768)\]\[[7](http://arxiv.org/abs/2306.15595)\]\[[8](http://arxiv.org/abs/2307.03172)\]\[[9](http://arxiv.org/abs/2208.00748)\]\[[10](http://arxiv.org/abs/2305.01625)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Summarizing long-form narratives--such as books, movies, and TV scripts--requires capturing intricate plotlines, character interactions, and thematic coherence, a task that remains challenging for existing LLMs. We introduce NexusSum, a multi-agent LLM framework for narrative summarization that processes long-form text through a structured, sequential pipeline--without requiring fine-tuning. Our approach introduces two key innovations: (1) Dialogue-to-Description Transformation: A narrative-specific preprocessing method that standardizes character dialogue and descriptive text into a unified format, improving coherence. (2) Hierarchical Multi-LLM Summarization: A structured summarization pipeline that optimizes chunk processing and controls output length for accurate, high-quality summaries. Our method establishes a new state-of-the-art in narrative summarization, achieving up to a 30.0% improvement in BERTScore (F1) across books, movies, and TV scripts. These results demonstrate the effectiveness of multi-agent LLMs in handling long-form content, offering a scalable approach for structured summarization in diverse storytelling domains.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2007.14062)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2404.03561)\]\[[7](http://arxiv.org/abs/2306.15595)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer:
Narrative summarization presents unique challenges due to the complexity of long-form content, requiring the preservation of intricate plotlines, character interactions, and thematic coherence \[[1](http://arxiv.org/abs/2005.01840)\]. Unlike news summarization, which often deals with shorter, more structured texts, narrative summarization involves handling extended chapters with significant length and nuanced language \[[1](http://arxiv.org/abs/2005.01840)\]. This task is further complicated by the need for extreme paraphrasing and generalization in summaries, which are common in online study guides \[[1](http://arxiv.org/abs/2005.01840)\]. Extractive summarization methods, which rely on selecting key sentences from the source text, are particularly challenging in this context due to the need for precise alignment between summary sentences and corresponding chapter content \[[1](http://arxiv.org/abs/2005.01840)\]. The development of new metrics and alignment techniques is crucial for creating reliable gold-standard summaries, as demonstrated by recent advancements in this area \[[1](http://arxiv.org/abs/2005.01840)\].
|    | reference                                                                                         |   date | key idea/summary                                                                                                                                                                                               |
|----|---------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Exploring Content Selection in Summarization of Novel Chapters](http://arxiv.org/abs/2005.01840) |    nan | The paper introduces a new summarization task for generating summaries of novel chapters using study guide pairs, focusing on extractive methods and presenting a novel alignment metric for improved results. |
### <a id='category-abstractive-summarization-techniques'></a>Abstractive Summarization Techniques: 1 papers found.
Context: 
	Document 1: [Category]: «Abstractive Summarization Techniques»
[_citation_number]: «2»
[Snippet]: «Abstractive summarization for long-form narrative texts such as movie scripts is challenging due to the computational and memory constraints of current language models. A movie script typically comprises a large number of scenes; however, only a fraction of these scenes are salient, i.e., important for understanding the overall narrative. The salience of a scene can be operationalized by considering it as salient if it is mentioned in the summary. Automatically identifying salient scenes is difficult due to the lack of suitable datasets. In this work, we introduce a scene saliency dataset that consists of human-annotated salient scenes for 100 movies. We propose a two-stage abstractive summarization approach which first identifies the salient scenes in script and then generates a summary using only those scenes. Using QA-based evaluation, we show that our model outperforms previous state-of-the-art summarization methods and reflects the information content of a movie more accurately than a model that takes the whole movie script as input.»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T13:26:23+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2007.14062)\]. Further details \[[6](http://arxiv.org/abs/2006.04768)\]\[[7](http://arxiv.org/abs/2306.15595)\]\[[8](http://arxiv.org/abs/2307.03172)\]\[[9](http://arxiv.org/abs/2208.00748)\]\[[10](http://arxiv.org/abs/2305.01625)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Summarizing long-form narratives--such as books, movies, and TV scripts--requires capturing intricate plotlines, character interactions, and thematic coherence, a task that remains challenging for existing LLMs. We introduce NexusSum, a multi-agent LLM framework for narrative summarization that processes long-form text through a structured, sequential pipeline--without requiring fine-tuning. Our approach introduces two key innovations: (1) Dialogue-to-Description Transformation: A narrative-specific preprocessing method that standardizes character dialogue and descriptive text into a unified format, improving coherence. (2) Hierarchical Multi-LLM Summarization: A structured summarization pipeline that optimizes chunk processing and controls output length for accurate, high-quality summaries. Our method establishes a new state-of-the-art in narrative summarization, achieving up to a 30.0% improvement in BERTScore (F1) across books, movies, and TV scripts. These results demonstrate the effectiveness of multi-agent LLMs in handling long-form content, offering a scalable approach for structured summarization in diverse storytelling domains.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2007.14062)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2404.03561)\]\[[7](http://arxiv.org/abs/2306.15595)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Abstractive summarization for long-form narrative texts, such as movie scripts, remains a challenging task due to the computational and memory constraints of current language models \[[2](http://arxiv.org/abs/2404.03561)\]. These constraints are exacerbated by the fact that long-form narratives often consist of a large number of scenes, only a fraction of which are salient—i.e., important for understanding the overall narrative \[[2](http://arxiv.org/abs/2404.03561)\]. The identification of salient scenes is particularly difficult due to the lack of suitable datasets, which has hindered the development of effective summarization methods \[[2](http://arxiv.org/abs/2404.03561)\]. To address this, recent work has introduced datasets with human-annotated salient scenes for a large number of movies, enabling more accurate scene selection \[[2](http://arxiv.org/abs/2404.03561)\]. This highlights the importance of scene saliency in improving the quality of abstractive summaries, as models that rely on the entire script often fail to capture the most relevant information \[[2](http://arxiv.org/abs/2404.03561)\]. The challenge of identifying salient scenes underscores the need for more sophisticated approaches that can effectively prioritize content, which is a key area of ongoing research in the field of narrative summarization.
|    | reference                                                                                              |   date | key idea/summary                                                                                                                                                                                                                                 |
|----|--------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Select and Summarize: Scene Saliency for Movie Script Summarization](http://arxiv.org/abs/2404.03561) |    nan | This work introduces a scene saliency dataset and a two-stage abstractive summarization approach for long-form narrative texts like movie scripts, which outperforms existing methods by focusing on salient scenes for more accurate summaries. |
### <a id='category-long-context-processing-methods'></a>Long-Context Processing Methods: 10 papers found.
Long-context processing methods have been extensively explored to address the limitations of traditional transformer models in handling long sequences. These models often rely on sparse attention mechanisms, such as BigBird, which reduces the quadratic memory dependency to linear by introducing a universal approximator of sequence functions and maintaining Turing completeness \[[3](http://arxiv.org/abs/2007.14062)\]. Similarly, Longformer employs a combination of local windowed attention and global attention to enable efficient processing of long documents, achieving state-of-the-art results on tasks like text8 and enwik8 \[[4](http://arxiv.org/abs/2004.05150)\]. Position Interpolation extends the context window of RoPE-based models like LLaMA to up to 32768 tokens with minimal fine-tuning, preserving performance on both extended and original contexts \[[7](http://arxiv.org/abs/2306.15595)\]. Unlimiformer further advances this by offloading cross-attention computation to a k-nearest-neighbor index, allowing for processing of extremely long inputs without truncation \[[6](http://arxiv.org/abs/2006.04768)\]. CachED enables end-to-end training of encoder-decoder models on long documents by caching gradients during backpropagation, allowing models like BART to handle over 500K tokens without parameter expansion \[[7](http://arxiv.org/abs/2306.15595)\]. Chain-of-Agents (CoA) introduces a multi-agent collaboration framework that addresses long-context focus issues by segmenting the input and enabling structured information aggregation across multiple LLMs, achieving significant improvements in tasks like question answering and summarization \[[8](http://arxiv.org/abs/2307.03172)\]. These approaches collectively highlight the ongoing efforts to enhance the ability of LLMs to process and generate coherent summaries from long-form narratives, as demonstrated by NexusSum’s innovations in structured summarization \[[1](http://arxiv.org/abs/2005.01840)\].
|    | reference                                                                                                                                                                   |   date | key idea/summary                                                                                                                                                                                                                                          |
|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Big Bird: Transformers for Longer Sequences](http://arxiv.org/abs/2007.14062)                                                                                              |    nan | BigBird is a sparse attention mechanism that reduces the quadratic memory dependency of Transformers to linear, enabling handling of longer sequences and improving performance on NLP tasks.                                                             |
|  1 | [Longformer: The Long-Document Transformer](http://arxiv.org/abs/2004.05150)                                                                                                |    nan | Longformer is a transformer variant with an attention mechanism that scales linearly with sequence length, enabling efficient processing of long documents and achieving state-of-the-art results on various downstream tasks.                            |
|  2 | [Extending Context Window of Large Language Models via Positional
  Interpolation](http://arxiv.org/abs/2306.15595)                                                         |    nan | Position Interpolation (PI) extends the context window of RoPE-based LLMs to up to 32768 with minimal fine-tuning, maintaining strong performance on long-context tasks while preserving quality within the original context window.                      |
|  3 | [Lost in the Middle: How Language Models Use Long Contexts](http://arxiv.org/abs/2307.03172)                                                                                |    nan | The paper analyzes how language models use long input contexts and finds that performance degrades when relevant information is in the middle, suggesting a need for better evaluation protocols for long-context models.                                 |
|  4 | [Efficient Long-Text Understanding with Short-Text Models](http://arxiv.org/abs/2208.00748)                                                                                 |    nan | SLED is a simple approach for processing long sequences using pretrained short-text LMs by partitioning input into overlapping chunks and leveraging a pretrained decoder for information fusion.                                                         |
|  5 | [Unlimiformer: Long-Range Transformers with Unlimited Length Input](http://arxiv.org/abs/2305.01625)                                                                        |    nan | Unlimiformer is a method that allows transformers to handle unlimited input lengths by offloading cross-attention computation to a k-nearest-neighbor index, enabling efficient processing of extremely long sequences without modifying existing models. |
|  6 | [End-to-End Long Document Summarization using Gradient Caching](http://arxiv.org/abs/2501.01805)                                                                            |    nan | CachED enables end-to-end training of transformer-based encoder-decoder models for long document summarization without input truncation by caching gradients and re-computing hidden vectors during backpropagation.                                      |
|  7 | [Chain of Agents: Large Language Models Collaborating on Long-Context
  Tasks](http://arxiv.org/abs/2406.02818)                                                             |    nan | Chain-of-Agents (CoA) is a novel framework that addresses the challenge of processing long contexts in LLMs by using multi-agent collaboration to improve information aggregation and context reasoning across various tasks.                             |
|  8 | [(L)ong(T)5: (E)fficient Text-To-Text Transformer for Long Sequences](https://aclanthology.org/2022.findings-naacl.55/)                                                     |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                 |
|  9 | [Advances in Neural Information Processing Systems 33, NeurIPS 2020](https://proceedings.neurips.cc/paper_files/paper/2020/file/6b493230205f780e1bc26945df7481e5-Paper.pdf) |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                 |
### <a id='category-efficient-attention-mechanisms'></a>Efficient Attention Mechanisms: 2 papers found.
Efficient attention mechanisms have been a focal point in improving the scalability and performance of transformer models, particularly for handling long sequences. Researchers have introduced techniques such as locality-sensitive hashing to reduce the computational complexity of attention mechanisms from O(L²) to O(L log L) \[[1](http://arxiv.org/abs/2005.01840)\]. Additionally, reversible residual layers have been proposed to minimize memory usage by storing activations only once during training \[[1](http://arxiv.org/abs/2005.01840)\]. Similarly, the linear transformer, or Linformer, leverages low-rank approximations of self-attention to achieve O(n) time and space complexity, significantly enhancing efficiency without compromising performance \[[2](http://arxiv.org/abs/2404.03561)\]. These advancements align with the challenges faced by models like NexusSum, which processes long-form narratives, as they aim to optimize computational resources for extended input lengths. The use of efficient attention mechanisms is crucial for applications requiring structured summarization of lengthy texts, such as books, movies, and TV scripts, where maintaining coherence and accuracy is essential \[[2](http://arxiv.org/abs/2404.03561)\].
|    | reference                                                                           |   date | key idea/summary                                                                                                                                                                                                        |
|----|-------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Reformer: The Efficient Transformer](http://arxiv.org/abs/2001.04451)              |    nan | The Reformer improves Transformer efficiency by using locality-sensitive hashing for attention and reversible residual layers, achieving similar performance with better memory efficiency and speed on long sequences. |
|  1 | [Linformer: Self-Attention with Linear Complexity](http://arxiv.org/abs/2006.04768) |    nan | The paper introduces Linformer, a new self-attention mechanism that reduces the computational complexity of transformers from $O(n^2)$ to $O(n)$, achieving similar performance with greater efficiency.                |
### <a id='category-coherence-and-quality-assessment'></a>Coherence and Quality Assessment: 1 papers found.
Context: 
	Document 1: [Category]: «Coherence and Quality Assessment»
[_citation_number]: «13»
[Snippet]: «Summarizing book-length documents (>100K tokens) that exceed the context
window size of large language models (LLMs) requires first breaking the input
document into smaller chunks and then prompting an LLM to merge, update, and
compress chunk-level summaries. Despite the complexity and importance of this
task, it has yet to be meaningfully studied due to the challenges of
evaluation: existing book-length summarization datasets (e.g., BookSum) are in
the pretraining data of most public LLMs, and existing evaluation methods
struggle to capture errors made by modern LLM summarizers. In this paper, we
present the first study of the coherence of LLM-based book-length summarizers
implemented via two prompting workflows: (1) hierarchically merging chunk-level
summaries, and (2) incrementally updating a running summary. We obtain 1193
fine-grained human annotations on GPT-4 generated summaries of 100
recently-published books and identify eight common types of coherence errors
made by LLMs. Because human evaluation is expensive and time-consuming, we
develop an automatic metric, BooookScore, that measures the proportion of
sentences in a summary that do not contain any of the identified error types.
BooookScore has high agreement with human annotations and allows us to
systematically evaluate the impact of many other critical parameters (e.g.,
chunk size, base LLM) while saving $15K USD and 500 hours in human evaluation
costs. We find that closed-source LLMs such as GPT-4 and Claude 2 produce
summaries with higher BooookScore than those generated by open-source models.
While LLaMA 2 falls behind other models, Mixtral achieves performance on par
with GPT-3.5-Turbo. Incremental updating yields lower BooookScore but higher
level of detail than hierarchical merging, a trade-off sometimes preferred by
annotators.»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T13:26:23+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2007.14062)\]. Further details \[[6](http://arxiv.org/abs/2006.04768)\]\[[7](http://arxiv.org/abs/2306.15595)\]\[[8](http://arxiv.org/abs/2307.03172)\]\[[9](http://arxiv.org/abs/2208.00748)\]\[[10](http://arxiv.org/abs/2305.01625)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Summarizing long-form narratives--such as books, movies, and TV
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2007.14062)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2404.03561)\]\[[7](http://arxiv.org/abs/2306.15595)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The coherence and quality assessment of long-form summaries remain a critical challenge, particularly when dealing with book-length documents that exceed the context window of large language models (LLMs) \[[13](http://arxiv.org/abs/2310.00785)\]. Existing methods often struggle to capture the intricate plotlines, character interactions, and thematic coherence required for such tasks \[[13](http://arxiv.org/abs/2310.00785)\]. This issue is compounded by the lack of robust evaluation metrics, as many datasets used for training are part of the pretraining data for public LLMs, limiting the ability to assess model performance accurately \[[13](http://arxiv.org/abs/2310.00785)\]. To address this, recent work has focused on developing structured summarization pipelines and automated metrics to evaluate coherence. For instance, the BooookScore metric has been introduced to measure the proportion of sentences in a summary that avoid common coherence errors, showing high agreement with human annotations \[[13](http://arxiv.org/abs/2310.00785)\]. These advancements highlight the importance of both human evaluation and automated metrics in improving the quality and coherence of long-form summaries.
|    | reference                                                                                                                  |   date | key idea/summary                                                                                                                                                                                                |
|----|----------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [BooookScore: A systematic exploration of book-length summarization in
  the era of LLMs](http://arxiv.org/abs/2310.00785) |    nan | This paper introduces BooookScore, an automatic metric to evaluate the coherence of LLM-based book-length summaries, and finds that closed-source models like GPT-4 outperform open-source models in this task. |
### <a id='category-evaluation-metrics-for-summaries'></a>Evaluation Metrics for Summaries: 1 papers found.
Context: 
	Document 1: [Category]: «Evaluation Metrics for Summaries»
[_citation_number]: «14»
[Snippet]: «Large Language Models (LLMs) have demonstrated near-human performance in
summarization tasks based on traditional metrics such as ROUGE and BERTScore.
However, these metrics do not adequately capture critical aspects of
summarization quality, such as factual accuracy, particularly for long
narratives (>100K tokens). Recent advances, such as LLM-as-a-Judge, address the
limitations of metrics based on lexical similarity but still exhibit factual
inconsistencies, especially in understanding character relationships and
states. In this work, we introduce NarrativeFactScore, a novel
"Agent-as-a-Judge" framework for evaluating and refining summaries. By
leveraging a Character Knowledge Graph (CKG) extracted from input and generated
summaries, NarrativeFactScore assesses the factual consistency and provides
actionable guidance for refinement, such as identifying missing or erroneous
facts. We demonstrate the effectiveness of NarrativeFactScore through a
detailed workflow illustration and extensive validation on widely adopted
benchmarks, achieving superior performance compared to competitive methods. Our
results highlight the potential of agent-driven evaluation systems to improve
the factual reliability of LLM-generated summaries.»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T13:26:23+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2007.14062)\]. Further details \[[6](http://arxiv.org/abs/2006.04768)\]\[[7](http://arxiv.org/abs/2306.15595)\]\[[8](http://arxiv.org/abs/2307.03172)\]\[[9](http://arxiv.org/abs/2208.00748)\]\[[10](http://arxiv.org/abs/2305.01625)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Summarizing long-form narratives--such as books, movies, and TV
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2007.14062)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2404.03561)\]\[[7](http://arxiv.org/abs/2306.15595)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer:  
Evaluation metrics for summarization have traditionally relied on lexical similarity measures such as ROUGE and BERTScore, which have shown near-human performance in many tasks \[[14](http://arxiv.org/abs/2501.09993)\]. However, these metrics fall short in capturing essential aspects of quality, such as factual accuracy, especially for long narratives exceeding 100K tokens \[[14](http://arxiv.org/abs/2501.09993)\]. Recent approaches, like LLM-as-a-Judge, attempt to address these limitations by incorporating judgment-based evaluation, yet they still struggle with understanding complex character relationships and states \[[14](http://arxiv.org/abs/2501.09993)\]. This highlights the need for more sophisticated evaluation frameworks that can assess not only the surface-level coherence of summaries but also their factual consistency. The introduction of NarrativeFactScore, which leverages a Character Knowledge Graph (CKG) to evaluate and refine summaries, represents a significant step forward by providing actionable insights for improving factual reliability \[[14](http://arxiv.org/abs/2501.09993)\]. Such agent-driven evaluation systems are increasingly seen as vital for enhancing the quality of LLM-generated summaries in narrative contexts.
|    | reference                                                                                      |   date | key idea/summary                                                                                                                                                                                    |
|----|------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Agent-as-Judge for Factual Summarization of Long Narratives](http://arxiv.org/abs/2501.09993) |    nan | NarrativeFactScore introduces an 'Agent-as-a-Judge' framework to improve factual accuracy in LLM-generated summaries by leveraging a Character Knowledge Graph (CKG) for evaluation and refinement. |
### <a id='category-structured-summarization-pipelines'></a>Structured Summarization Pipelines: 1 papers found.
Context: 
	Document 1: [Category]: «Structured Summarization Pipelines»
[_citation_number]: «15»
[Snippet]: «»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T13:26:23+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2007.14062)\]. Further details \[[6](http://arxiv.org/abs/2006.04768)\]\[[7](http://arxiv.org/abs/2306.15595)\]\[[8](http://arxiv.org/abs/2307.03172)\]\[[9](http://arxiv.org/abs/2208.00748)\]\[[10](http://arxiv.org/abs/2305.01625)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Summarizing long-form narratives--such as books, movies, and TV
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2007.14062)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2404.03561)\]\[[7](http://arxiv.org/abs/2306.15595)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
The category of "Structured Summarization Pipelines" focuses on the development of systematic approaches for generating coherent and accurate summaries of long-form narratives. These pipelines often incorporate modular stages that address specific challenges such as maintaining thematic coherence, preserving character interactions, and ensuring narrative flow \[[15](https://aclanthology.org/N15-1113/)\]. A key aspect of such pipelines is the integration of preprocessing techniques that standardize input formats, enabling more effective summarization \[[15](https://aclanthology.org/N15-1113/)\]. Additionally, hierarchical structures are commonly employed to manage the complexity of long-form content by breaking down the material into manageable chunks and optimizing the summarization process \[[15](https://aclanthology.org/N15-1113/)\]. These structured approaches aim to enhance the quality of generated summaries by leveraging sequential processing and controlled output generation, which is crucial for maintaining fidelity to the original content \[[15](https://aclanthology.org/N15-1113/)\].
|    | reference                                                                                        |   date | key idea/summary                                                                                          |
|----|--------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------|
|  0 | [Movie Script Summarization as Graph-based Scene Extraction](https://aclanthology.org/N15-1113/) |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
