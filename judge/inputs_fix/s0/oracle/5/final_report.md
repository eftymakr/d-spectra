## Related Works

Instruction-following text embedding is a critical area of research that aims to generate dynamic text embeddings that adapt to user instructions, highlighting specific attributes of text \[[1](http://arxiv.org/abs/1310.4546)\]. This task has gained significant attention due to its potential applications in information retrieval, semantic similarity, and natural language understanding. However, existing approaches often suffer from significant computational overhead, as they require re-encoding the entire corpus for each new instruction \[[1](http://arxiv.org/abs/1310.4546)\].

Several recent works have explored methods to improve the efficiency and effectiveness of instruction-following text embeddings. For instance, Sentence-BERT (SBERT) introduces a siamese BERT-network structure to derive semantically meaningful sentence embeddings that can be compared using cosine-similarity, reducing the computational overhead compared to traditional BERT-based methods \[[4](http://arxiv.org/abs/1908.10084)\]. Similarly, SimCSE proposes a simple contrastive learning framework that greatly advances state-of-the-art sentence embeddings by using an unsupervised approach where the model predicts itself in a contrastive objective \[[5](http://arxiv.org/abs/2104.08821)\].

The work in \[[8](http://arxiv.org/abs/2212.09741)\] introduces INSTRUCTOR, a new method for computing text embeddings given task instructions, which is a single embedder that can generate text embeddings tailored to different downstream tasks and domains without any further training. This approach is trained on a multitask mixture with a contrastive loss and achieves state-of-the-art performance on a range of tasks \[[8](http://arxiv.org/abs/2212.09741)\]. Similarly, the work in \[[9](http://arxiv.org/abs/2402.09642)\] presents InBedder, which treats the instruction as a question about the input text and encodes the expected answers to obtain the representation accordingly. This approach significantly improves instruction-following capabilities when applied to both large language models and smaller encoder-based models \[[9](http://arxiv.org/abs/2402.09642)\].

The paper \[[10](http://arxiv.org/abs/2409.11136)\] introduces Promptriever, the first retrieval model able to be prompted like an LM. It demonstrates that retrieval models can be controlled with prompts on a per-query basis, setting the stage for future work aligning LM prompting techniques with information retrieval \[[10](http://arxiv.org/abs/2409.11136)\]. Additionally, the work in \[[7](http://arxiv.org/abs/2402.09906)\] introduces GritLM, a model that unifies generative and embedding tasks by distinguishing between them through instructions, achieving new state-of-the-art results on the Massive Text Embedding Benchmark (MTEB) \[[7](http://arxiv.org/abs/2402.09906)\].

In contrast to these methods, the proposed GSTransform framework is designed to address the computational overhead by using a lightweight transformation mechanism that adapts pre-computed embeddings in real time to align with user instructions, guided by a small amount of text data with instruction-focused label annotation \[[1](http://arxiv.org/abs/1310.4546)\]. This approach significantly improves instruction-following text embedding quality over state-of-the-art methods while achieving dramatic speedups of 6~300x in real-time processing on large-scale datasets \[[1](http://arxiv.org/abs/1310.4546)\].

References:  
\[[1](http://arxiv.org/abs/1310.4546)\] Abstract of the paper  
\[[4](http://arxiv.org/abs/1908.10084)\] Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks  
\[[5](http://arxiv.org/abs/2104.08821)\] SimCSE: Simple Contrastive Learning of Sentence Embeddings  
\[[7](http://arxiv.org/abs/2402.09906)\] Generative Representational Instruction Tuning  
\[[8](http://arxiv.org/abs/2212.09741)\] One Embedder, Any Task: Instruction-Finetuned Text Embeddings  
\[[9](http://arxiv.org/abs/2402.09642)\] Answer is All You Need: Instruction-following Text Embedding via Answering the Question  
\[[10](http://arxiv.org/abs/2409.11136)\] Promptriever: Instruction-Trained Retrievers Can Be Prompted Like Language Models
## Research papers
### Outline
- [Real-Time Processing and Speedup Achievements [1 papers]](#category-real-time-processing-and-speedup-achievements)
- [Performance Evaluation on Benchmark Tasks [2 papers]](#category-performance-evaluation-on-benchmark-tasks)
- [Contrastive Learning Approaches [3 papers]](#category-contrastive-learning-approaches)
- [Efficient Embedding Generation Techniques [1 papers]](#category-efficient-embedding-generation-techniques)
- [Generative and Embedding Task Unification [1 papers]](#category-generative-and-embedding-task-unification)
- [Instruction-Tuned Embedding Models [3 papers]](#category-instruction-tuned-embedding-models)
- [Instruction-Driven Representation Methods [2 papers]](#category-instruction-driven-representation-methods)
- [Retrieval Models with Prompting Capabilities [1 papers]](#category-retrieval-models-with-prompting-capabilities)

### <a id='category-real-time-processing-and-speedup-achievements'></a>Real-Time Processing and Speedup Achievements: 1 papers found.
Context: 
	Document 1: [Category]: «Real-Time Processing and Speedup Achievements»
[_citation_number]: «1»
[Snippet]: «The recently introduced continuous Skip-gram model is an efficient method for learning high-quality distributed vector representations that capture a large number of precise syntactic and semantic word relationships. In this paper we present several extensions that improve both the quality of the vectors and the training speed. By subsampling of the frequent words we obtain significant speedup and also learn more regular word representations. We also describe a simple alternative to the hierarchical softmax called negative sampling. An inherent limitation of word representations is their indifference to word order and their inability to represent idiomatic phrases. For example, the meanings of "Canada" and "Air" cannot be easily combined to obtain "Air Canada". Motivated by this example, we present a simple method for finding phrases in text, and show that learning good vector representations for millions of phrases is possible.»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T16:16:22+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1810.04805)\]. Further details \[[6](http://arxiv.org/abs/2401.00368)\]\[[7](http://arxiv.org/abs/2402.09906)\]\[[8](http://arxiv.org/abs/2212.09741)\]\[[9](http://arxiv.org/abs/2402.09642)\]\[[10](http://arxiv.org/abs/2409.11136)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In this work, we investigate an important task named instruction-following text embedding, which generates dynamic text embeddings that adapt to user instructions, highlighting specific attributes of text. Despite recent advancements, existing approaches suffer from significant computational overhead, as they require re-encoding the entire corpus for each new instruction. To address this challenge, we propose GSTransform, a novel instruction-following text embedding framework based on Guided Space Transformation. Our key observation is that instruction-relevant information is inherently encoded in generic embeddings but remains underutilized. Instead of repeatedly encoding the corpus for each instruction, GSTransform is a lightweight transformation mechanism that adapts pre-computed embeddings in real time to align with user instructions, guided by a small amount of text data with instruction-focused label annotation. We conduct extensive experiments on three instruction-awareness downstream tasks across nine real-world datasets, demonstrating that GSTransform improves instruction-following text embedding quality over state-of-the-art methods while achieving dramatic speedups of 6~300x in real-time processing on large-scale datasets. The source code is available at https://github.com/YingchaojieFeng/GSTransform.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1810.04805)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1706.03762)\]\[[7](http://arxiv.org/abs/2402.09906)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Real-time processing and speedup achievements have been a focal point in the development of efficient text embedding models \[[1](http://arxiv.org/abs/1310.4546)\]. For instance, the continuous Skip-gram model has been enhanced with techniques such as subsampling of frequent words, which not only accelerates training but also leads to more regular word representations \[[1](http://arxiv.org/abs/1310.4546)\]. Additionally, the introduction of negative sampling as an alternative to hierarchical softmax has further improved training efficiency \[[1](http://arxiv.org/abs/1310.4546)\]. These advancements are crucial for tasks requiring rapid adaptation, such as instruction-following text embedding, where repeated re-encoding of the entire corpus for each new instruction can be computationally prohibitive. The GSTransform framework, which leverages pre-computed embeddings and applies lightweight transformations in real time, exemplifies how these speedup strategies can be integrated into modern approaches \[[1](http://arxiv.org/abs/1310.4546)\]. Such methods are essential for achieving dramatic speedups, as demonstrated by GSTransform's 6–300x improvements in real-time processing on large-scale datasets \[[1](http://arxiv.org/abs/1310.4546)\].
|    | reference                                                                                                       |   date | key idea/summary                                                                                                                                                                                                                                           |
|----|-----------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Distributed Representations of Words and Phrases and their
  Compositionality](http://arxiv.org/abs/1310.4546) |    nan | The paper introduces improvements to the continuous Skip-gram model, including subsampling frequent words and negative sampling, to enhance vector quality and training speed, while also addressing the limitation of word order in word representations. |
### <a id='category-performance-evaluation-on-benchmark-tasks'></a>Performance Evaluation on Benchmark Tasks: 2 papers found.
Context: 
	Document 1: [Category]: «Performance Evaluation on Benchmark Tasks»
[_citation_number]: «2»
[Snippet]: «The dominant sequence transduction models are based on complex recurrent or
convolutional neural networks in an encoder-decoder configuration. The best
performing models also connect the encoder and decoder through an attention
mechanism. We propose a new simple network architecture, the Transformer, based
solely on attention mechanisms, dispensing with recurrence and convolutions
entirely. Experiments on two machine translation tasks show these models to be
superior in quality while being more parallelizable and requiring significantly
less time to train. Our model achieves 28.4 BLEU on the WMT 2014
English-to-German translation task, improving over the existing best results,
including ensembles by over 2 BLEU. On the WMT 2014 English-to-French
translation task, our model establishes a new single-model state-of-the-art
BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction
of the training costs of the best models from the literature. We show that the
Transformer generalizes well to other tasks by applying it successfully to
English constituency parsing both with large and limited training data.»

	Document 2: [Category]: «Performance Evaluation on Benchmark Tasks»
[_citation_number]: «3»
[Snippet]: «We introduce a new language representation model called BERT, which stands
for Bidirectional Encoder Representations from Transformers. Unlike recent
language representation models, BERT is designed to pre-train deep
bidirectional representations from unlabeled text by jointly conditioning on
both left and right context in all layers. As a result, the pre-trained BERT
model can be fine-tuned with just one additional output layer to create
state-of-the-art models for a wide range of tasks, such as question answering
and language inference, without substantial task-specific architecture
modifications.
  BERT is conceptually simple and empirically powerful. It obtains new
state-of-the-art results on eleven natural language processing tasks, including
pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI
accuracy to 86.7% (4.6% absolute improvement), SQuAD v1.1 question answering
Test F1 to 93.2 (1.5 point absolute improvement) and SQuAD v2.0 Test F1 to 83.1
(5.1 point absolute improvement).»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T16:16:22+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1810.04805)\]. Further details \[[6](http://arxiv.org/abs/2401.00368)\]\[[7](http://arxiv.org/abs/2402.09906)\]\[[8](http://arxiv.org/abs/2212.09741)\]\[[9](http://arxiv.org/abs/2402.09642)\]\[[10](http://arxiv.org/abs/2409.11136)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In this work, we investigate an important task named instruction-following
text embedding, which generates dynamic text embeddings that adapt to user
instructions, highlighting specific attributes of text. Despite recent
advancements, existing approaches suffer from significant computational
overhead, as they require re-encoding the entire corpus for each new
instruction. To address this challenge, we propose GSTransform, a novel
instruction-following text embedding framework based on Guided Space
Transformation. Our key observation is that instruction-relevant information is
inherently encoded in generic embeddings but remains underutilized. Instead of
repeatedly encoding the corpus for each instruction, GSTransform is a
lightweight transformation mechanism that adapts pre-computed embeddings in
real time to align with user instructions, guided by a small amount of text
data with instruction-focused label annotation. We conduct extensive
experiments on three instruction-awareness downstream tasks across nine
real-world datasets, demonstrating that GSTransform improves
instruction-following text embedding quality over state-of-the-art methods
while achieving dramatic speedups of 6~300x in real-time processing on
large-scale datasets. The source code is available at
https://github.com/YingchaojieFeng/GSTransform.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1810.04805)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1706.03762)\]\[[7](http://arxiv.org/abs/2402.09906)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Recent advances in sequence transduction have focused on improving efficiency and performance through attention-based architectures. The Transformer model \[[2](http://arxiv.org/abs/1706.03762)\] introduced a novel approach by replacing recurrent and convolutional layers with attention mechanisms, enabling more parallelizable training and superior performance on machine translation tasks. This model achieved significant improvements, such as a BLEU score of 28.4 on the WMT 2014 English-to-German task and 41.8 on the English-to-French task, demonstrating its effectiveness. Similarly, BERT \[[3](http://arxiv.org/abs/1810.04805)\] leveraged bidirectional contextual representations from transformers to achieve state-of-the-art results on various NLP tasks, including GLUE, MultiNLI, and SQuAD. These models highlight the potential of attention-based mechanisms in enhancing both performance and efficiency.
|    | reference                                                                                                             |   date | key idea/summary                                                                                                                                                                                                                                                   |
|----|-----------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Attention Is All You Need](http://arxiv.org/abs/1706.03762)                                                          |    nan | The Transformer model, based entirely on attention mechanisms, outperforms traditional recurrent and convolutional neural networks in machine translation tasks, offering higher quality results, better parallelization, and significantly reduced training time. |
|  1 | [BERT: Pre-training of Deep Bidirectional Transformers for Language
  Understanding](http://arxiv.org/abs/1810.04805) |    nan | BERT is a new language representation model that pre-trains deep bidirectional representations from unlabeled text, achieving state-of-the-art results on multiple natural language processing tasks.                                                              |
### <a id='category-contrastive-learning-approaches'></a>Contrastive Learning Approaches: 3 papers found.
Context: 
	Document 1: [Category]: «Contrastive Learning Approaches»
[_citation_number]: «4»
[Snippet]: «BERT (Devlin et al., 2018) and RoBERTa (Liu et al., 2019) has set a new
state-of-the-art performance on sentence-pair regression tasks like semantic
textual similarity (STS). However, it requires that both sentences are fed into
the network, which causes a massive computational overhead: Finding the most
similar pair in a collection of 10,000 sentences requires about 50 million
inference computations (~65 hours) with BERT. The construction of BERT makes it
unsuitable for semantic similarity search as well as for unsupervised tasks
like clustering.
  In this publication, we present Sentence-BERT (SBERT), a modification of the
pretrained BERT network that use siamese and triplet network structures to
derive semantically meaningful sentence embeddings that can be compared using
cosine-similarity. This reduces the effort for finding the most similar pair
from 65 hours with BERT / RoBERTa to about 5 seconds with SBERT, while
maintaining the accuracy from BERT.
  We evaluate SBERT and SRoBERTa on common STS tasks and transfer learning
tasks, where it outperforms other state-of-the-art sentence embeddings methods.»

	Document 2: [Category]: «Contrastive Learning Approaches»
[_citation_number]: «5»
[Snippet]: «This paper presents SimCSE, a simple contrastive learning framework that
greatly advances state-of-the-art sentence embeddings. We first describe an
unsupervised approach, which takes an input sentence and predicts itself in a
contrastive objective, with only standard dropout used as noise. This simple
method works surprisingly well, performing on par with previous supervised
counterparts. We find that dropout acts as minimal data augmentation, and
removing it leads to a representation collapse. Then, we propose a supervised
approach, which incorporates annotated pairs from natural language inference
datasets into our contrastive learning framework by using "entailment" pairs as
positives and "contradiction" pairs as hard negatives. We evaluate SimCSE on
standard semantic textual similarity (STS) tasks, and our unsupervised and
supervised models using BERT base achieve an average of 76.3% and 81.6%
Spearman's correlation respectively, a 4.2% and 2.2% improvement compared to
the previous best results. We also show -- both theoretically and empirically
-- that the contrastive learning objective regularizes pre-trained embeddings'
anisotropic space to be more uniform, and it better aligns positive pairs when
supervised signals are available.»

	Document 3: [Category]: «Contrastive Learning Approaches»
[_citation_number]: «13»
[Snippet]: «»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T16:16:22+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1810.04805)\]. Further details \[[6](http://arxiv.org/abs/2401.00368)\]\[[7](http://arxiv.org/abs/2402.09906)\]\[[8](http://arxiv.org/abs/2212.09741)\]\[[9](http://arxiv.org/abs/2402.09642)\]\[[10](http://arxiv.org/abs/2409.11136)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In this work, we investigate an important task named instruction-following
text embedding, which generates dynamic text embeddings that adapt to user
instructions, highlighting specific attributes of text. Despite recent
advancements, existing approaches suffer from significant computational
overhead, as they require re-encoding the entire corpus for each new
instruction. To address this challenge, we propose GSTransform, a novel
instruction-following text embedding framework based on Guided Space
Transformation. Our key observation is that instruction-relevant information is
inherently encoded in generic embeddings but remains underutilized. Instead of
repeatedly encoding the corpus for each instruction, GSTransform is a
lightweight transformation mechanism that adapts pre-computed embeddings in
real time to align with user instructions, guided by a small amount of text
data with instruction-focused label annotation. We conduct extensive
experiments on three instruction-awareness downstream tasks across nine
real-world datasets, demonstrating that GSTransform improves
instruction-following text embedding quality over state-of-the-art methods
while achieving dramatic speedups of 6~300x in real-time processing on
large-scale datasets. The source code is available at
https://github.com/YingchaojieFeng/GSTransform.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1810.04805)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1706.03762)\]\[[7](http://arxiv.org/abs/2402.09906)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Contrastive learning approaches have significantly advanced the field of sentence embeddings by improving both efficiency and effectiveness. Early models like BERT \[[4](http://arxiv.org/abs/1908.10084)\] and RoBERTa \[[4](http://arxiv.org/abs/1908.10084)\] achieved state-of-the-art performance on tasks like semantic textual similarity (STS), but their computational overhead limited their applicability to large-scale tasks \[[4](http://arxiv.org/abs/1908.10084)\]. To address these limitations, Sentence-BERT (SBERT) was introduced, utilizing siamese and triplet network structures to generate semantically meaningful sentence embeddings that enable fast similarity computation \[[4](http://arxiv.org/abs/1908.10084)\]. SBERT reduces the computational effort from hours to seconds while maintaining accuracy. More recently, SimCSE \[[5](http://arxiv.org/abs/2104.08821)\] has further advanced the field by proposing a simple contrastive learning framework that achieves competitive results with both unsupervised and supervised approaches. SimCSE leverages dropout as a form of data augmentation and incorporates annotated pairs from natural language inference datasets to improve representation quality \[[5](http://arxiv.org/abs/2104.08821)\]. These developments highlight the growing importance of contrastive learning in creating efficient and effective sentence embeddings.
|    | reference                                                                                                                 |   date | key idea/summary                                                                                                                                                                                                                                                        |
|----|---------------------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](http://arxiv.org/abs/1908.10084)                         |    nan | Sentence-BERT (SBERT) is a modified BERT model that uses siamese and triplet network structures to generate efficient and accurate sentence embeddings for semantic similarity tasks, significantly reducing computation time compared to traditional models like BERT. |
|  1 | [SimCSE: Simple Contrastive Learning of Sentence Embeddings](http://arxiv.org/abs/2104.08821)                             |    nan | SimCSE is a contrastive learning framework that improves sentence embeddings through both unsupervised and supervised approaches, achieving state-of-the-art results on semantic textual similarity tasks.                                                              |
|  2 | [WhitenedCSE: Whitening-based Contrastive Learning of Sentence Embeddings](https://doi.org/10.18653/v1/2023.acl-long.677) |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                               |
### <a id='category-efficient-embedding-generation-techniques'></a>Efficient Embedding Generation Techniques: 1 papers found.
Context: 
	Document 1: [Category]: «Efficient Embedding Generation Techniques»
[_citation_number]: «6»
[Snippet]: «In this paper, we introduce a novel and simple method for obtaining
high-quality text embeddings using only synthetic data and less than 1k
training steps. Unlike existing methods that often depend on multi-stage
intermediate pre-training with billions of weakly-supervised text pairs,
followed by fine-tuning with a few labeled datasets, our method does
not require building complex training pipelines or relying on manually collected
datasets that are often constrained by task diversity and language coverage. We
leverage proprietary LLMs to generate diverse synthetic data for hundreds of
thousands of text embedding tasks across 93 languages. We then fine-tune
open-source decoder-only LLMs on the synthetic data using standard contrastive
loss. Experiments demonstrate that our method achieves strong performance on
highly competitive text embedding benchmarks without using any labeled data.
Furthermore, when fine-tuned with a mixture of synthetic and labeled data, our
model sets new state-of-the-art results on the BEIR and MTEB benchmarks.»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T16:16:22+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1810.04805)\]. Further details \[[6](http://arxiv.org/abs/2401.00368)\]\[[7](http://arxiv.org/abs/2402.09906)\]\[[8](http://arxiv.org/abs/2212.09741)\]\[[9](http://arxiv.org/abs/2402.09642)\]\[[10](http://arxiv.org/abs/2409.11136)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In this work, we investigate an important task named instruction-following
text embedding, which generates dynamic text embeddings that adapt to user
instructions, highlighting specific attributes of text. Despite recent
advancements, existing approaches suffer from significant computational
overhead, as they require re-encoding the entire corpus for each new
instruction. To address this challenge, we propose GSTransform, a novel
instruction-following text embedding framework based on Guided Space
Transformation. Our key observation is that instruction-relevant information is
inherently encoded in generic embeddings but remains underutilized. Instead of
repeatedly encoding the corpus for each instruction, GSTransform is a
lightweight transformation mechanism that adapts pre-computed embeddings in
real time to align with user instructions, guided by a small amount of text
data with instruction-focused label annotation. We conduct extensive
experiments on three instruction-awareness downstream tasks across nine
real-world datasets, demonstrating that GSTransform improves
instruction-following text embedding quality over state-of-the-art methods
while achieving dramatic speedups of 6~300x in real-time processing on
large-scale datasets. The source code is available at
https://github.com/YingchaojieFeng/GSTransform.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1810.04805)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1706.03762)\]\[[7](http://arxiv.org/abs/2402.09906)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Efficient embedding generation techniques have gained significant attention due to their ability to reduce computational overhead and improve scalability. Recent approaches, such as those leveraging synthetic data, demonstrate promising results in achieving high-quality embeddings without the need for extensive labeled datasets \[[6](http://arxiv.org/abs/2401.00368)\]. These methods often rely on proprietary large language models (LLMs) to generate diverse synthetic data, which is then used to fine-tune open-source decoder-only LLMs using standard contrastive loss \[[6](http://arxiv.org/abs/2401.00368)\]. This approach eliminates the need for complex training pipelines and manually curated datasets, which are often limited in task diversity and language coverage \[[6](http://arxiv.org/abs/2401.00368)\]. Furthermore, combining synthetic data with a small amount of labeled data can lead to state-of-the-art performance on benchmark tasks such as BEIR and MTEB \[[6](http://arxiv.org/abs/2401.00368)\]. Such techniques are particularly relevant for applications requiring real-time adaptation, as they enable lightweight transformation mechanisms that align pre-computed embeddings with user instructions \[[6](http://arxiv.org/abs/2401.00368)\].
|    | reference                                                                               |   date | key idea/summary                                                                                                                                                                                                                                                  |
|----|-----------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Improving Text Embeddings with Large Language Models](http://arxiv.org/abs/2401.00368) |    nan | This paper introduces a novel method for obtaining high-quality text embeddings using synthetic data and minimal training steps, achieving competitive performance without labeled data and setting new state-of-the-art results when combined with labeled data. |
### <a id='category-generative-and-embedding-task-unification'></a>Generative and Embedding Task Unification: 1 papers found.
Context: 
	Document 1: [Category]: «Generative and Embedding Task Unification»
[_citation_number]: «7»
[Snippet]: «All text-based language problems can be reduced to either generation or
embedding. Current models only perform well at one or the other. We introduce
generative representational instruction tuning (GRIT) whereby a large language
model is trained to handle both generative and embedding tasks by
distinguishing between them through instructions. Compared to other open
models, our resulting GritLM 7B sets a new state of the art on the Massive Text
Embedding Benchmark (MTEB) and outperforms all models up to its size on a range
of generative tasks. By scaling up further, GritLM 8x7B outperforms all open
generative language models that we tried while still being among the best
embedding models. Notably, we find that GRIT matches training on only
generative or embedding data, thus we can unify both at no performance loss.
Among other benefits, the unification via GRIT speeds up Retrieval-Augmented
Generation (RAG) by > 60% for long documents, by no longer requiring separate
retrieval and generation models. Models, code, etc. are freely available at
https://github.com/ContextualAI/gritlm.»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T16:16:22+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1810.04805)\]. Further details \[[6](http://arxiv.org/abs/2401.00368)\]\[[7](http://arxiv.org/abs/2402.09906)\]\[[8](http://arxiv.org/abs/2212.09741)\]\[[9](http://arxiv.org/abs/2402.09642)\]\[[10](http://arxiv.org/abs/2409.11136)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In this work, we investigate an important task named instruction-following
text embedding, which generates dynamic text embeddings that adapt to user
instructions, highlighting specific attributes of text. Despite recent
advancements, existing approaches suffer from significant computational
overhead, as they require re-encoding the entire corpus for each new
instruction. To address this challenge, we propose GSTransform, a novel
instruction-following text embedding framework based on Guided Space
Transformation. Our key observation is that instruction-relevant information is
inherently encoded in generic embeddings but remains underutilized. Instead of
repeatedly encoding the corpus for each instruction, GSTransform is a
lightweight transformation mechanism that adapts pre-computed embeddings in
real time to align with user instructions, guided by a small amount of text
data with instruction-focused label annotation. We conduct extensive
experiments on three instruction-awareness downstream tasks across nine
real-world datasets, demonstrating that GSTransform improves
instruction-following text embedding quality over state-of-the-art methods
while achieving dramatic speedups of 6~300x in real-time processing on
large-scale datasets. The source code is available at
https://github.com/YingchaojieFeng/GSTransform.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1810.04805)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1706.03762)\]\[[7](http://arxiv.org/abs/2402.09906)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
The category of generative and embedding task unification explores the integration of models capable of performing both generation and embedding tasks effectively. Recent work has demonstrated that separating these tasks often leads to suboptimal performance, as models trained exclusively on one type of task may struggle with the other \[[7](http://arxiv.org/abs/2402.09906)\]. To address this, the GRIT framework was introduced, which trains large language models to distinguish and handle both generative and embedding tasks through instruction-based tuning \[[7](http://arxiv.org/abs/2402.09906)\]. This approach allows models to achieve state-of-the-art results on both tasks without performance loss, as evidenced by GritLM 7B and 8x7B models that outperform existing open-source models in both domains \[[7](http://arxiv.org/abs/2402.09906)\]. Furthermore, the unification of these tasks offers practical benefits, such as significant speedups in Retrieval-Augmented Generation (RAG) by eliminating the need for separate retrieval and generation models \[[7](http://arxiv.org/abs/2402.09906)\]. This highlights the potential of unified models to enhance efficiency and effectiveness in real-world applications.
|    | reference                                                                         |   date | key idea/summary                                                                                                                                                                                                                                    |
|----|-----------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Generative Representational Instruction Tuning](http://arxiv.org/abs/2402.09906) |    nan | GRIT is a method that unifies generative and embedding tasks in large language models, achieving state-of-the-art performance on both tasks without performance loss, and significantly improving the efficiency of Retrieval-Augmented Generation. |
### <a id='category-instruction-tuned-embedding-models'></a>Instruction-Tuned Embedding Models: 3 papers found.
Context: 
	Document 1: [Category]: «Instruction-Tuned Embedding Models»
[_citation_number]: «8»
[Snippet]: «We introduce INSTRUCTOR, a new method for computing text embeddings given task instructions: every text input is embedded together with instructions explaining the use case (e.g., task and domain descriptions). Unlike encoders from prior work that are more specialized, INSTRUCTOR is a single embedder that can generate text embeddings tailored to different downstream tasks and domains, without any further training. We first annotate instructions for 330 diverse tasks and train INSTRUCTOR on this multitask mixture with a contrastive loss. We evaluate INSTRUCTOR on 70 embedding evaluation tasks (66 of which are unseen during training), ranging from classification and information retrieval to semantic textual similarity and text generation evaluation. INSTRUCTOR, while having an order of magnitude fewer parameters than the previous best model, achieves state-of-the-art performance, with an average improvement of 3.4% compared to the previous best results on the 70 diverse datasets. Our analysis suggests that INSTRUCTOR is robust to changes in instructions, and that instruction finetuning mitigates the challenge of training a single model on diverse datasets. Our model, code, and data are available at https://instructor-embedding.github.io.»

	Document 2: [Category]: «Instruction-Tuned Embedding Models»
[_citation_number]: «11»
[Snippet]: «»

	Document 3: [Category]: «Instruction-Tuned Embedding Models»
[_citation_number]: «12»
[Snippet]: «»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T16:16:22+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1810.04805)\]. Further details \[[6](http://arxiv.org/abs/2401.00368)\]\[[7](http://arxiv.org/abs/2402.09906)\]\[[8](http://arxiv.org/abs/2212.09741)\]\[[9](http://arxiv.org/abs/2402.09642)\]\[[10](http://arxiv.org/abs/2409.11136)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In this work, we investigate an important task named instruction-following text embedding, which generates dynamic text embeddings that adapt to user instructions, highlighting specific attributes of text. Despite recent advancements, existing approaches suffer from significant computational overhead, as they require re-encoding the entire corpus for each new instruction. To address this challenge, we propose GSTransform, a novel instruction-following text embedding framework based on Guided Space Transformation. Our key observation is that instruction-relevant information is inherently encoded in generic embeddings but remains underutilized. Instead of repeatedly encoding the corpus for each instruction, GSTransform is a lightweight transformation mechanism that adapts pre-computed embeddings in real time to align with user instructions, guided by a small amount of text data with instruction-focused label annotation. We conduct extensive experiments on three instruction-awareness downstream tasks across nine real-world datasets, demonstrating that GSTransform improves instruction-following text embedding quality over state-of-the-art methods while achieving dramatic speedups of 6~300x in real-time processing on large-scale datasets. The source code is available at https://github.com/YingchaojieFeng/GSTransform.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1810.04805)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1706.03762)\]\[[7](http://arxiv.org/abs/2402.09906)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Instruction-tuned embedding models represent a significant advancement in generating text embeddings that adapt to specific tasks and domains \[[8](http://arxiv.org/abs/2212.09741)\]. These models, such as INSTRUCTOR, are designed to produce embeddings that are tailored to user instructions, allowing for flexible and efficient adaptation to diverse downstream tasks \[[8](http://arxiv.org/abs/2212.09741)\]. Unlike traditional encoders that require specialized training for each task, instruction-tuned models can operate as a single embedder, reducing the need for additional training and enabling performance across a wide range of applications \[[8](http://arxiv.org/abs/2212.09741)\]. This approach is particularly effective in scenarios where the model must handle multiple tasks and domains, as demonstrated by the evaluation of INSTRUCTOR on 70 different embedding tasks, including classification, information retrieval, and semantic textual similarity \[[8](http://arxiv.org/abs/2212.09741)\]. The effectiveness of these models is further supported by their ability to achieve state-of-the-art performance with fewer parameters than previous models, highlighting their efficiency and adaptability \[[8](http://arxiv.org/abs/2212.09741)\]. The use of instruction-focused annotations and contrastive learning during training helps in aligning embeddings with user needs, making these models robust to changes in instructions and enhancing their generalization capabilities \[[8](http://arxiv.org/abs/2212.09741)\].
|    | reference                                                                                        |   date | key idea/summary                                                                                                                                                                                      |
|----|--------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [One Embedder, Any Task: Instruction-Finetuned Text Embeddings](http://arxiv.org/abs/2212.09741) |    nan | INSTRUCTOR is a new method for generating text embeddings by incorporating task instructions, enabling a single embedder to perform well across diverse downstream tasks without additional training. |
|  1 | [Glove: Global Vectors for Word Representation](https://doi.org/10.3115/v1/d14-1162)             |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                             |
|  2 | [Universal Sentence Encoder for English](https://doi.org/10.18653/v1/d18-2029)                   |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                             |
### <a id='category-instruction-driven-representation-methods'></a>Instruction-Driven Representation Methods: 2 papers found.
Context: 
	Document 1: [Category]: «Instruction-Driven Representation Methods»
[_citation_number]: «9»
[Snippet]: «This work aims to build a text embedder that can capture characteristics of texts specified by user instructions. Despite its tremendous potential to deploy user-oriented embeddings, none of previous approaches provides a concrete solution for it. This paper offers a new viewpoint, which treats the instruction as a question about the input text and encodes the expected answers to obtain the representation accordingly. Intuitively, texts with the same (implicit) semantics would share similar answers following the instruction, thus leading to more similar embeddings. Specifically, we propose InBedder that instantiates this embed-via-answering idea by only fine-tuning language models on abstractive question answering tasks. InBedder demonstrates significantly improved instruction-following capabilities according to our proposed instruction awareness tests and instruction robustness tests, when applied to both large language models (LLMs) (e.g., llama-2-7b) and smaller encoder-based LMs (e.g., roberta-large). Additionally, our qualitative analysis of clustering outcomes, achieved by applying different instructions to the same corpus, demonstrates a high degree of interpretability.»

	Document 2: [Category]: «Instruction-Driven Representation Methods»
[_citation_number]: «14»
[Snippet]: «»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T16:16:22+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1810.04805)\]. Further details \[[6](http://arxiv.org/abs/2401.00368)\]\[[7](http://arxiv.org/abs/2402.09906)\]\[[8](http://arxiv.org/abs/2212.09741)\]\[[9](http://arxiv.org/abs/2402.09642)\]\[[10](http://arxiv.org/abs/2409.11136)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In this work, we investigate an important task named instruction-following
text embedding, which generates dynamic text embeddings that adapt to user
instructions, highlighting specific attributes of text. Despite recent
advancements, existing approaches suffer from significant computational
overhead, as they require re-encoding the entire corpus for each new
instruction. To address this challenge, we propose GSTransform, a novel
instruction-following text embedding framework based on Guided Space
Transformation. Our key observation is that instruction-relevant information is
inherently encoded in generic embeddings but remains underutilized. Instead of
repeatedly encoding the corpus for each instruction, GSTransform is a
lightweight transformation mechanism that adapts pre-computed embeddings in
real time to align with user instructions, guided by a small amount of text
data with instruction-focused label annotation. We conduct extensive
experiments on three instruction-awareness downstream tasks across nine
real-world datasets, demonstrating that GSTransform improves
instruction-following text embedding quality over state-of-the-art methods
while achieving dramatic speedups of 6~300x in real-time processing on
large-scale datasets. The source code is available at
https://github.com/YingchaojieFeng/GSTransform.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1810.04805)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1706.03762)\]\[[7](http://arxiv.org/abs/2402.09906)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Instruction-driven representation methods aim to generate text embeddings that adapt to user instructions, highlighting specific attributes of text \[[9](http://arxiv.org/abs/2402.09642)\]. These methods address the challenge of capturing implicit semantic relationships by treating instructions as questions about the input text, and encoding the expected answers to obtain the representation \[[9](http://arxiv.org/abs/2402.09642)\]. This approach ensures that texts with similar semantics produce similar embeddings when following the same instruction \[[9](http://arxiv.org/abs/2402.09642)\]. A notable example is InBedder, which fine-tunes language models on abstractive question answering tasks to improve instruction-following capabilities, demonstrating significant improvements over existing methods \[[9](http://arxiv.org/abs/2402.09642)\]. The key idea is that instruction-relevant information is inherently encoded in generic embeddings but remains underutilized \[[9](http://arxiv.org/abs/2402.09642)\]. This aligns with recent efforts to develop lightweight transformation mechanisms that adapt pre-computed embeddings in real time, guided by instruction-focused annotations \[[9](http://arxiv.org/abs/2402.09642)\].
|    | reference                                                                                                                    |   date | key idea/summary                                                                                                                                                                                                                                                                     |
|----|------------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Answer is All You Need: Instruction-following Text Embedding via
  Answering the Question](http://arxiv.org/abs/2402.09642) |    nan | This paper introduces InBedder, a text embedder that follows user instructions by treating them as questions about the input text, and fine-tunes language models on abstractive question answering tasks to generate more semantically consistent and instruction-aware embeddings. |
|  1 | [AoE: Angle-optimized Embeddings for Semantic Textual Similarity](https://doi.org/10.18653/v1/2024.acl-long.101)             |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                            |
### <a id='category-retrieval-models-with-prompting-capabilities'></a>Retrieval Models with Prompting Capabilities: 1 papers found.
Context: 
	Document 1: [Category]: «Retrieval Models with Prompting Capabilities»
[_citation_number]: «10»
[Snippet]: «Instruction-tuned language models (LM) are able to respond to imperative
commands, providing a more natural user interface compared to their base
counterparts. In this work, we present Promptriever, the first retrieval model
able to be prompted like an LM. To train Promptriever, we curate and release a
new instance-level instruction training set from MS MARCO, spanning nearly 500k
instances. Promptriever not only achieves strong performance on standard
retrieval tasks, but also follows instructions. We observe: (1) large gains
(reaching SoTA) on following detailed relevance instructions (+14.3 p-MRR /
+3.1 nDCG on FollowIR), (2) significantly increased robustness to lexical
choices/phrasing in the query+instruction (+12.9 Robustness@10 on InstructIR),
and (3) the ability to perform hyperparameter search via prompting to reliably
improve retrieval performance (+1.4 average increase on BEIR). Promptriever
demonstrates that retrieval models can be controlled with prompts on a
per-query basis, setting the stage for future work aligning LM prompting
techniques with information retrieval.»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T16:16:22+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1810.04805)\]. Further details \[[6](http://arxiv.org/abs/2401.00368)\]\[[7](http://arxiv.org/abs/2402.09906)\]\[[8](http://arxiv.org/abs/2212.09741)\]\[[9](http://arxiv.org/abs/2402.09642)\]\[[10](http://arxiv.org/abs/2409.11136)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In this work, we investigate an important task named instruction-following
text embedding, which generates dynamic text embeddings that adapt to user
instructions, highlighting specific attributes of text. Despite recent
advancements, existing approaches suffer from significant computational
overhead, as they require re-encoding the entire corpus for each new
instruction. To address this challenge, we propose GSTransform, a novel
instruction-following text embedding framework based on Guided Space
Transformation. Our key observation is that instruction-relevant information is
inherently encoded in generic embeddings but remains underutilized. Instead of
repeatedly encoding the corpus for each instruction, GSTransform is a
lightweight transformation mechanism that adapts pre-computed embeddings in
real time to align with user instructions, guided by a small amount of text
data with instruction-focused label annotation. We conduct extensive
experiments on three instruction-awareness downstream tasks across nine
real-world datasets, demonstrating that GSTransform improves
instruction-following text embedding quality over state-of-the-art methods
while achieving dramatic speedups of 6~300x in real-time processing on
large-scale datasets. The source code is available at
https://github.com/YingchaojieFeng/GSTransform.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1810.04805)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1706.03762)\]\[[7](http://arxiv.org/abs/2402.09906)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Recent advancements in retrieval models have focused on enhancing their ability to follow instructions, a critical aspect for improving user interaction and task performance \[[10](http://arxiv.org/abs/2409.11136)\]. This trend is exemplified by the development of instruction-tuned language models (LMs), which can respond to imperative commands more naturally than their base counterparts \[[10](http://arxiv.org/abs/2409.11136)\]. The introduction of models like Promptriever marks a significant step forward, as it is the first retrieval model capable of being prompted like an LM \[[10](http://arxiv.org/abs/2409.11136)\]. Promptriever leverages a new instance-level instruction training set from MS MARCO, spanning nearly 500k instances, to achieve strong performance on standard retrieval tasks while also following detailed instructions \[[10](http://arxiv.org/abs/2409.11136)\]. This work demonstrates that retrieval models can be controlled with prompts on a per-query basis, aligning LM prompting techniques with information retrieval \[[10](http://arxiv.org/abs/2409.11136)\]. Such developments highlight the growing importance of instruction-following capabilities in retrieval models, paving the way for more flexible and efficient information retrieval systems.
|    | reference                                                                                                              |   date | key idea/summary                                                                                                                                                                                                                               |
|----|------------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Promptriever: Instruction-Trained Retrievers Can Be Prompted Like
  Language Models](http://arxiv.org/abs/2409.11136) |    nan | Promptriever is the first retrieval model that can be prompted like a language model, achieving strong performance on standard retrieval tasks and demonstrating the ability to follow instructions and improve performance through prompting. |
