## Related Works

Instruction-following text embedding is a critical area of research that aims to generate dynamic text embeddings that adapt to user instructions, highlighting specific attributes of text \[[1](http://arxiv.org/abs/1310.4546)\]. This task has gained significant attention due to its potential applications in information retrieval, semantic similarity, and natural language understanding. However, existing approaches often suffer from significant computational overhead, as they require re-encoding the entire corpus for each new instruction \[[1](http://arxiv.org/abs/1310.4546)\].

Several recent works have explored methods to improve the efficiency and effectiveness of instruction-following text embeddings. For instance, Sentence-BERT (SBERT) introduces a siamese BERT-network structure to derive semantically meaningful sentence embeddings that can be compared using cosine-similarity, reducing the computational overhead compared to traditional BERT-based methods \[[4](http://arxiv.org/abs/1908.10084)\]. Similarly, SimCSE proposes a simple contrastive learning framework that greatly advances state-of-the-art sentence embeddings by using an unsupervised approach where the model predicts itself in a contrastive objective \[[5](http://arxiv.org/abs/2104.08821)\].

The work in \[[8](http://arxiv.org/abs/2212.09741)\] introduces INSTRUCTOR, a new method for computing text embeddings given task instructions, which is a single embedder that can generate text embeddings tailored to different downstream tasks and domains without any further training. This approach is trained on a multitask mixture with a contrastive loss and achieves state-of-the-art performance on a range of tasks \[[8](http://arxiv.org/abs/2212.09741)\]. Similarly, the work in \[[9](http://arxiv.org/abs/2402.09642)\] presents InBedder, which treats the instruction as a question about the input text and encodes the expected answers to obtain the representation accordingly. This approach significantly improves instruction-following capabilities when applied to both large language models and smaller encoder-based models \[[9](http://arxiv.org/abs/2402.09642)\].

The paper \[[10](http://arxiv.org/abs/2409.11136)\] introduces Promptriever, the first retrieval model able to be prompted like an LM. It demonstrates that retrieval models can be controlled with prompts on a per-query basis, setting the stage for future work aligning LM prompting techniques with information retrieval \[[10](http://arxiv.org/abs/2409.11136)\]. Additionally, the work in \[[7](http://arxiv.org/abs/2402.09906)\] introduces GritLM, a model that unifies generative and embedding tasks by distinguishing between them through instructions, achieving new state-of-the-art results on the Massive Text Embedding Benchmark (MTEB) \[[7](http://arxiv.org/abs/2402.09906)\].

In contrast to these methods, the proposed GSTransform framework is designed to address the computational overhead by using a lightweight transformation mechanism that adapts pre-computed embeddings in real time to align with user instructions, guided by a small amount of text data with instruction-focused label annotation \[[1](http://arxiv.org/abs/1310.4546)\]. This approach significantly improves instruction-following text embedding quality over state-of-the-art methods while achieving
## Research papers
### Outline
- [Efficient Embedding Generation Techniques [3 papers]](#category-efficient-embedding-generation-techniques)
- [Performance Evaluation on Downstream Tasks [2 papers]](#category-performance-evaluation-on-downstream-tasks)
- [Contrastive Learning for Embeddings [4 papers]](#category-contrastive-learning-for-embeddings)
- [Unified Generative and Embedding Models [1 papers]](#category-unified-generative-and-embedding-models)
- [Instruction-tailored Embedding Frameworks [3 papers]](#category-instruction-tailored-embedding-frameworks)
- [Retrieval Models with Prompt Control [1 papers]](#category-retrieval-models-with-prompt-control)

### <a id='category-efficient-embedding-generation-techniques'></a>Efficient Embedding Generation Techniques: 3 papers found.
Context: 
	Document 1: [Category]: «Efficient Embedding Generation Techniques»
[Snippet]: «The recently introduced continuous Skip-gram model is an efficient method for learning high-quality distributed vector representations that capture a large number of precise syntactic and semantic word relationships. In this paper we present several extensions that improve both the quality of the vectors and the training speed. By subsampling of the frequent words we obtain significant speedup and also learn more regular word representations. We also describe a simple alternative to the hierarchical softmax called negative sampling. An inherent limitation of word representations is their indifference to word order and their inability to represent idiomatic phrases. For example, the meanings of "Canada" and "Air" cannot be easily combined to obtain "Air Canada". Motivated by this example, we present a simple method for finding phrases in text, and show that learning good vector representations for millions of phrases is possible.»
[_citation_number]: «1»

	Document 2: [Category]: «Efficient Embed: «»
[_citation_number]: «11»

	Document 3: [Category]: «Efficient Embedding Generation Techniques»
[Snippet]: «»
[_citation_number]: «14»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T16:16:22+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1810.04805)\]. Further details \[[6](http://arxiv.org/abs/2401.00368)\]\[[7](http://arxiv.org/abs/2402.09906)\]\[[8](http://arxiv.org/abs/2212.09741)\]\[[9](http://arxiv.org/abs/2402.09642)\]\[[10](http://arxiv.org/abs/2409.11136)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In this work, we investigate an important task named instruction-following text embedding, which generates dynamic text embeddings that adapt to user instructions, highlighting specific attributes of text. Despite recent advancements, existing approaches suffer from significant computational overhead, as they require re-encoding the entire corpus for each new instruction. To address this challenge, we propose GSTransform, a novel instruction
|    | reference                                                                                                        |   date | key idea/summary                                                                                                                                                                                                                                           |
|----|------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Distributed Representations of Words and Phrases and their
  Compositionality](http://arxiv.org/abs/1310.4546)  |    nan | The paper introduces improvements to the continuous Skip-gram model, including subsampling frequent words and negative sampling, to enhance vector quality and training speed, while also addressing the limitation of word order in word representations. |
|  1 | [Glove: Global Vectors for Word Representation](https://doi.org/10.3115/v1/d14-1162)                             |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                  |
|  2 | [AoE: Angle-optimized Embeddings for Semantic Textual Similarity](https://doi.org/10.18653/v1/2024.acl-long.101) |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                  |
### <a id='category-performance-evaluation-on-downstream-tasks'></a>Performance Evaluation on Downstream Tasks: 2 papers found.
Context: 
	Document 1: [Category]: «Performance Evaluation on Downstream Tasks»
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
[_citation_number]: «2»

	Document 2: [Category]: «Performance Evaluation on Downstream Tasks»
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
Test F1 to 93.2 (1.5 point absolute improvement
|    | reference                                                                                                             |   date | key idea/summary                                                                                                                                                                                                                                                   |
|----|-----------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Attention Is All You Need](http://arxiv.org/abs/1706.03762)                                                          |    nan | The Transformer model, based entirely on attention mechanisms, outperforms traditional recurrent and convolutional neural networks in machine translation tasks, offering higher quality results, better parallelization, and significantly reduced training time. |
|  1 | [BERT: Pre-training of Deep Bidirectional Transformers for Language
  Understanding](http://arxiv.org/abs/1810.04805) |    nan | BERT is a new language representation model that pre-trains deep bidirectional representations from unlabeled text, achieving state-of-the-art results on multiple natural language processing tasks.                                                              |
### <a id='category-contrastive-learning-for-embeddings'></a>Contrastive Learning for Embeddings: 4 papers found.
Context: 
	Document 1: [Category]: «Contrastive Learning for Embeddings»
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
[_citation_number]: «4»

	Document 2: [Category]: «Contrastive Learning for Embeddings»
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
supervised models using BERT base achieve an average of 76.3% and 81
|    | reference                                                                                                                 |   date | key idea/summary                                                                                                                                                                                                                                                        |
|----|---------------------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](http://arxiv.org/abs/1908.10084)                         |    nan | Sentence-BERT (SBERT) is a modified BERT model that uses siamese and triplet network structures to generate efficient and accurate sentence embeddings for semantic similarity tasks, significantly reducing computation time compared to traditional models like BERT. |
|  1 | [SimCSE: Simple Contrastive Learning of Sentence Embeddings](http://arxiv.org/abs/2104.08821)                             |    nan | SimCSE is a contrastive learning framework that improves sentence embeddings through both unsupervised and supervised approaches, achieving state-of-the-art results on semantic textual similarity tasks.                                                              |
|  2 | [Improving Text Embeddings with Large Language Models](http://arxiv.org/abs/2401.00368)                                   |    nan | This paper introduces a novel method for obtaining high-quality text embeddings using synthetic data and minimal training steps, achieving competitive performance without labeled data and setting new state-of-the-art results when combined with labeled data.       |
|  3 | [WhitenedCSE: Whitening-based Contrastive Learning of Sentence Embeddings](https://doi.org/10.18653/v1/2023.acl-long.677) |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                               |
### <a id='category-unified-generative-and-embedding-models'></a>Unified Generative and Embedding Models: 1 papers found.
Context: 
	Document 1: [Category]: «Unified Generative and Embedding Models»
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
[_citation_number]: «7»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T16:16:22+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1810.04805)\]. Further details \[[6](http://arxiv.org/abs/2401.00368)\]\[[7](http://arxiv.org/abs/2402.09906)\]\[[8](http://arxiv.org/abs/2212.09741)\]\[[9](http://arxiv.org/abs/2402.09642)\]\[[10](http://arxiv.org/abs/2409.11136)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In this work, we investigate an important task named instruction-following
text embedding, which generates dynamic text embeddings that adapt to user
instructions, highlighting specific attributes of text. Despite
|    | reference                                                                         |   date | key idea/summary                                                                                                                                                                                                                                    |
|----|-----------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Generative Representational Instruction Tuning](http://arxiv.org/abs/2402.09906) |    nan | GRIT is a method that unifies generative and embedding tasks in large language models, achieving state-of-the-art performance on both tasks without performance loss, and significantly improving the efficiency of Retrieval-Augmented Generation. |
### <a id='category-instruction-tailored-embedding-frameworks'></a>Instruction-tailored Embedding Frameworks: 3 papers found.
Context: 
	Document 1: [Category]: «Instruction-tailored Embedding Frameworks»
[Snippet]: «We introduce INSTRUCTOR, a new method for computing text embeddings given task instructions: every text input is embedded together with instructions explaining the use case (e.g., task and domain descriptions). Unlike encoders from prior work that are more specialized, INSTRUCTOR is a single embedder that can generate text embeddings tailored to different downstream tasks and domains, without any further training. We first annotate instructions for 330 diverse tasks and train INSTRUCTOR on this multitask mixture with a contrastive loss. We evaluate INSTRUCTOR on 70 embedding evaluation tasks (66 of which are unseen during training), ranging from classification and information retrieval to semantic textual similarity and text generation evaluation. INSTRUCTOR, while having an order of magnitude fewer parameters than the previous best model, achieves state-of-the-art performance, with an average improvement of 3.4% compared to the previous best results on the 70 diverse datasets. Our analysis suggests that INSTRUCTOR is robust to changes in instructions, and that instruction fine-tuning mitigates the challenge of training a single model on diverse datasets. Our model, code, and data are available at https://instructor-embedding.github.io.»
[_citation_number]: «8»

	Document 2: [Category]: «Instruction-tailored Embedding Frameworks»
[Snippet]: «This work aims to build a text embedder that can capture characteristics of texts specified by user instructions. Despite its tremendous potential to deploy user-oriented embeddings, none of previous approaches provides a concrete solution for it. This paper offers a new viewpoint, which treats the instruction as a question about the input text and encodes the expected answers to obtain the representation accordingly. Intuitively, texts with the same (implicit) semantics would share similar answers following the instruction, thus leading to more similar embeddings. Specifically, we propose InBedder that instantiates this embed-via-answering idea by only fine-tuning language models on abstractive question answering tasks. InBedder demonstrates significantly improved instruction-following capabilities according to our proposed instruction awareness tests and instruction robustness tests, when applied to both large language models (LLMs) (e.g., llama-2-7b) and smaller encoder-based LMs (e.g., roberta-large). Additionally, our qualitative analysis of clustering outcomes, achieved by applying different instructions to the same corpus, demonstrates a high degree of interpretability.»
[_citation
|    | reference                                                                                                                    |   date | key idea/summary                                                                                                                                                                                                                                                                     |
|----|------------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [One Embedder, Any Task: Instruction-Finetuned Text Embeddings](http://arxiv.org/abs/2212.09741)                             |    nan | INSTRUCTOR is a new method for generating text embeddings by incorporating task instructions, enabling a single embedder to perform well across diverse downstream tasks without additional training.                                                                                |
|  1 | [Answer is All You Need: Instruction-following Text Embedding via
  Answering the Question](http://arxiv.org/abs/2402.09642) |    nan | This paper introduces InBedder, a text embedder that follows user instructions by treating them as questions about the input text, and fine-tunes language models on abstractive question answering tasks to generate more semantically consistent and instruction-aware embeddings. |
|  2 | [Universal Sentence Encoder for English](https://doi.org/10.18653/v1/d18-2029)                                               |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                            |
### <a id='category-retrieval-models-with-prompt-control'></a>Retrieval Models with Prompt Control: 1 papers found.
Context: 
	Document 1: [Category]: «Retrieval Models with Prompt Control»
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
[_citation_number]: «10»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T16:16:22+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1810.04805)\]. Further details \[[6](http://arxiv.org/abs/2401.00368)\]\[[7](http://arxiv.org/abs/2402.09906)\]\[[8](http://arxiv.org/abs/2212.09741)\]\[[9](http://arxiv.org/abs/2402.09642)\]\[[10](http://arxiv.org/abs/2409.11136)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In this work, we investigate an important task named instruction-following
text embedding, which generates dynamic text embeddings that adapt to user
instructions, highlighting specific attributes of text
|    | reference                                                                                                              |   date | key idea/summary                                                                                                                                                                                                                               |
|----|------------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Promptriever: Instruction-Trained Retrievers Can Be Prompted Like
  Language Models](http://arxiv.org/abs/2409.11136) |    nan | Promptriever is the first retrieval model that can be prompted like a language model, achieving strong performance on standard retrieval tasks and demonstrating the ability to follow instructions and improve performance through prompting. |
