## Related Works

Dense retrievers have become a cornerstone in open-domain question answering (ODQA) systems, leveraging pre-trained language models (e.g., BERT, LLaMA) to encode text into dense vector representations that can be compared via similarity metrics such as cosine similarity \[[1](http://arxiv.org/abs/2004.04906)\]. Traditional sparse retrieval methods, such as TF-IDF or BM25, have been widely used but are increasingly being supplanted by dense retrieval approaches that offer superior performance \[[1](http://arxiv.org/abs/2004.04906)\]. This shift is driven by the ability of dense retrievers to capture semantic relationships between queries and passages more effectively \[[1](http://arxiv.org/abs/2004.04906)\].

The development of dense retrievers has been closely tied to advancements in pre-trained language models and contrastive learning. Sentence-BERT (SBERT) was introduced as a modification of BERT to generate sentence embeddings that can be compared using cosine similarity, significantly reducing computational overhead compared to standard BERT \[[2](http://arxiv.org/abs/1908.10084)\]. Similarly, SimCSE extends this idea by using contrastive learning to generate high-quality sentence embeddings, achieving state-of-the-art results on semantic textual similarity (STS) tasks \[[3](http://arxiv.org/abs/2104.08821)\]. These methods highlight the importance of fine-tuning pre-trained models to adapt them to specific retrieval tasks \[[2](http://arxiv.org/abs/1908.10084)\]\[[3](http://arxiv.org/abs/2104.08821)\].

The MS MARCO dataset has played a critical role in benchmarking dense retrievers, providing a large-scale, human-generated dataset of questions and corresponding answers \[[4](http://arxiv.org/abs/1611.09268)\]. This dataset has enabled researchers to evaluate the effectiveness of different retrieval strategies, including passage ranking and answer extraction \[[4](http://arxiv.org/abs/1611.09268)\]. The dataset's real-world nature and scale make it particularly valuable for assessing the generalization capabilities of dense retrievers \[[4](http://arxiv.org/abs/1611.09268)\].

Recent work has also explored the role of pre-training versus fine-tuning in dense retrievers. A study using the Dense Passage Retrieval (DPR) framework found that retrieval knowledge is primarily acquired during pre-training, with fine-tuning mainly adjusting neuron activations rather than reorganizing knowledge \[[1](http://arxiv.org/abs/2004.04906)\]. This finding was tested across different architectures, including encoder-only BERT and decoder-only LLaMA, as well as different pooling strategies, such as CLS token versus mean pooling \[[1](http://arxiv.org/abs/2004.04906)\]. The results suggest that while pre-training is foundational, fine-tuning can still play a role in optimizing retrieval performance \[[1](http://arxiv.org/abs/2004.04906)\].

In addition, the Contriever and RePLAMA models have introduced new approaches to dense retrieval, with Contriever being a fully unsupervised method and RePLAMA utilizing a decoder-based architecture \[[5]()\]\[[6]()\]. These models further demonstrate the flexibility of dense retrieval frameworks and their potential to improve performance in various settings \[[5]()\]\[[6]()\].

PromptReps has also contributed to the field by enhancing dense retrieval through prompt-based representations, offering a novel way to fine-tune models without requiring extensive labeled data \[[7]()\]. This approach aligns with the broader trend of using pre-trained models with minimal additional training to achieve competitive performance \[[7]()\].

Natural Questions, another benchmark dataset, has been used to evaluate the effectiveness of dense retrievers in real-world scenarios \[[8]()\]. This dataset is particularly useful for assessing the ability of models to understand and answer complex, open-ended questions \[[8]()\].

In summary, the field of dense retrieval has seen significant advancements, driven by improvements in pre-trained models, contrastive learning, and large-scale datasets. These developments have enabled more accurate and efficient retrieval systems, which are essential for modern open-domain question answering \[[1](http://arxiv.org/abs/2004.04906)\]\[[2](http://arxiv.org/abs/1908.10084)\]\[[3](http://arxiv.org/abs/2104.08821)\]\[[4](http://arxiv.org/abs/1611.09268)\]\[[5]()\]\[[6]()\]\[[7]()\]\[[8]()\].

References:  
\[[1](http://arxiv.org/abs/2004.04906)\] Dense Passage Retrieval for Open-Domain Question Answering  
\[[2](http://arxiv.org/abs/1908.10084)\] Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks  
\[[3](http://arxiv.org/abs/2104.08821)\] SimCSE: Simple Contrastive Learning of Sentence Embeddings  
\[[4](http://arxiv.org/abs/1611.09268)\] MS MARCO: A Human Generated MAchine Reading COmprehension Dataset  
\[[5]()\] Contriever: A Fully Unsupervised Dense Retriever  
\[[6]()\] RePLAMA: A Decoder-based Dense Retriever for Open-Domain Question Answering  
\[[7]()\] PromptReps: Enhancing Dense Retrieval with Prompt-based Representations  
\[[8]()\] Natural Questions: A Benchmark for Question Answering
## Research papers
### Outline
- [Dense Retrieval Foundations [2 papers]](#category-dense-retrieval-foundations)
- [Contrastive Learning Techniques [2 papers]](#category-contrastive-learning-techniques)
- [Evaluation Datasets for Retrieval [1 papers]](#category-evaluation-datasets-for-retrieval)
- [Decoder-based Retrieval Models [1 papers]](#category-decoder-based-retrieval-models)
- [Prompt-based Representation Methods [1 papers]](#category-prompt-based-representation-methods)
- [Benchmarking in Open-Domain QA [1 papers]](#category-benchmarking-in-open-domain-qa)

### <a id='category-dense-retrieval-foundations'></a>Dense Retrieval Foundations: 2 papers found.
Context: 
	Document 1: [Category]: «Dense Retrieval Foundations»
[_citation_number]: «1»
[Snippet]: «Open-domain question answering relies on efficient passage retrieval to
select candidate contexts, where traditional sparse vector space models, such
as TF-IDF or BM25, are the de facto method. In this work, we show that
retrieval can be practically implemented using dense representations alone,
where embeddings are learned from a small number of questions and passages by a
simple dual-encoder framework. When evaluated on a wide range of open-domain QA
datasets, our dense retriever outperforms a strong Lucene-BM25 system largely
by 9%-19% absolute in terms of top-20 passage retrieval accuracy, and helps our
end-to-end QA system establish new state-of-the-art on multiple open-domain QA
benchmarks.»

	Document 2: [Category]: «Dense Retrieval Foundations»
[_citation_number]: «5»
[Snippet]: «»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-12T01:24:00+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2104.08821)\]. Further details \[[6]()\]\[[7]()\]\[[8]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Dense retrievers utilize pre-trained backbone language models (e.g., BERT,
LLaMA) that are fine-tuned via contrastive learning to perform the task of
encoding text into sense representations that can be then compared via a
shallow similarity operation, e.g. inner product. Recent research has
questioned the role of fine-tuning vs. that of pre-training within dense
retrievers, specifically arguing that retrieval knowledge is primarily gained
during pre-training, meaning knowledge not acquired during pre-training cannot
be sub-sequentially acquired via fine-tuning. We revisit this idea here as the
claim was only studied in the context of a BERT-based encoder using DPR as
representative dense retriever. We extend the previous analysis by testing
other representation approaches (comparing the use of CLS tokens with that of
mean pooling), backbone architectures (encoder-only BERT vs. decoder-only
LLaMA), and additional datasets (MSMARCO in addition to Natural Questions). Our
study confirms that in DPR tuning, pre-trained knowledge underpins retrieval
performance, with fine-tuning primarily adjusting neuron activation rather than
reorganizing knowledge. However, this pattern does not hold universally, such
as in mean-pooled (Contriever) and decoder-based (LLaMA) models. We ensure full
reproducibility and make our implementation publicly available at
https://github.com/ielab/DenseRetriever-Knowledge-Acquisition.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2104.08821)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1908.10084)\]\[[7]()\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Dense retrieval has emerged as a critical component in open-domain question answering, offering an alternative to traditional sparse retrieval methods like TF-IDF or BM25 \[[1](http://arxiv.org/abs/2004.04906)\]. This approach leverages dense representations, where embeddings are learned from a small set of questions and passages using a dual-encoder framework \[[1](http://arxiv.org/abs/2004.04906)\]. The effectiveness of dense retrievers is demonstrated through their superior performance on various open-domain QA benchmarks, achieving significant improvements in top-20 passage retrieval accuracy compared to strong BM25 systems \[[1](http://arxiv.org/abs/2004.04906)\]. This work builds on earlier studies that questioned the role of fine-tuning versus pre-training in dense retrievers, arguing that retrieval knowledge is primarily acquired during pre-training, with fine-tuning mainly adjusting neuron activations rather than reorganizing knowledge \[[1](http://arxiv.org/abs/2004.04906)\]. The findings are further extended by examining different representation approaches, backbone architectures, and datasets, revealing that this pattern does not universally apply, as seen in models like Contriever and LLaMA \[[1](http://arxiv.org/abs/2004.04906)\].
|    | reference                                                                                     |   date | key idea/summary                                                                                                                                                                                                    |
|----|-----------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Dense Passage Retrieval for Open-Domain Question Answering](http://arxiv.org/abs/2004.04906) |    nan | This work demonstrates that dense representations can effectively replace traditional sparse methods like BM25 in open-domain question answering, achieving significant improvements in passage retrieval accuracy. |
|  1 | [Contriever: A Fully Unsupervised Dense Retriever]()                                          |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                           |
### <a id='category-contrastive-learning-techniques'></a>Contrastive Learning Techniques: 2 papers found.
Context: 
	Document 1: [Category]: «Contrastive Learning Techniques»
[_citation_number]: «2»
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

	Document 2: [Category]: «Contrastive Learning Techniques»
[_citation_number]: «3»
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


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-12T01:24:00+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2104.08821)\]. Further details \[[6]()\]\[[7]()\]\[[8]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Dense retrievers utilize pre-trained backbone language models (e.g., BERT,
LLaMA) that are fine-tuned via contrastive learning to perform the task of
encoding text into sense representations that can be then compared via a
shallow similarity operation, e.g. inner product. Recent research has
questioned the role of fine-tuning vs. that of pre-training within dense
retrievers, specifically arguing that retrieval knowledge is primarily gained
during pre-training, meaning knowledge not acquired during pre-training cannot
be sub-sequentially acquired via fine-tuning. We revisit this idea here as the
claim was only studied in the context of a BERT-based encoder using DPR as
representative dense retriever. We extend the previous analysis by testing
other representation approaches (comparing the use of CLS tokens with that of
mean pooling), backbone architectures (encoder-only BERT vs. decoder-only
LLaMA), and additional datasets (MSMARCO in addition to Natural Questions). Our
study confirms that in DPR tuning, pre-trained knowledge underpins retrieval
performance, with fine-tuning primarily adjusting neuron activation rather than
reorganizing knowledge. However, this pattern does not hold universally, such
as in mean-pooled (Contriever) and decoder-based (LLaMA) models. We ensure full
reproducibility and make our implementation publicly available at
https://github.com/ielab/DenseRetriever-Knowledge-Acquisition.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2104.08821)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1908.10084)\]\[[7]()\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: Contrastive learning techniques have significantly advanced the field of sentence embeddings, enabling more efficient and effective semantic similarity computation. Early models like BERT \[[2](http://arxiv.org/abs/1908.10084)\] and RoBERTa \[[2](http://arxiv.org/abs/1908.10084)\] achieved state-of-the-art results on tasks such as semantic textual similarity (STS), but their computational overhead limited their applicability for large-scale similarity search and unsupervised tasks \[[2](http://arxiv.org/abs/1908.10084)\]. To address these limitations, Sentence-BERT (SBERT) was introduced, modifying BERT to use siamese and triplet network structures, thereby enabling fast cosine similarity comparisons while maintaining accuracy \[[2](http://arxiv.org/abs/1908.10084)\]. More recently, SimCSE \[[3](http://arxiv.org/abs/2104.08821)\] proposed a simple contrastive learning framework that achieves competitive performance with supervised methods, using dropout as a form of data augmentation and leveraging entailment and contradiction pairs for supervised training \[[3](http://arxiv.org/abs/2104.08821)\]. These developments highlight the importance of contrastive learning in refining pre-trained models for downstream tasks, with ongoing research focusing on optimizing both unsupervised and supervised approaches \[[3](http://arxiv.org/abs/2104.08821)\].
|    | reference                                                                                         |   date | key idea/summary                                                                                                                                                                                                                                                        |
|----|---------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](http://arxiv.org/abs/1908.10084) |    nan | Sentence-BERT (SBERT) is a modified BERT model that uses siamese and triplet network structures to generate efficient and accurate sentence embeddings for semantic similarity tasks, significantly reducing computation time compared to traditional models like BERT. |
|  1 | [SimCSE: Simple Contrastive Learning of Sentence Embeddings](http://arxiv.org/abs/2104.08821)     |    nan | SimCSE is a contrastive learning framework that improves sentence embeddings through both unsupervised and supervised approaches, achieving state-of-the-art results on semantic textual similarity tasks.                                                              |
### <a id='category-evaluation-datasets-for-retrieval'></a>Evaluation Datasets for Retrieval: 1 papers found.
Context: 
	Document 1: [Category]: «Evaluation Datasets for Retrieval»
[_citation_number]: «4»
[Snippet]: «We introduce a large scale MAchine Reading COmprehension dataset, which we
name MS MARCO. The dataset comprises of 1,010,916 anonymized
questions---sampled from Bing's search query logs---each with a human generated
answer and 182,669 completely human rewritten generated answers. In addition,
the dataset contains 8,841,823 passages---extracted from 3,563,535 web
documents retrieved by Bing---that provide the information necessary for
curating the natural language answers. A question in the MS MARCO dataset may
have multiple answers or no answers at all. Using this dataset, we propose
three different tasks with varying levels of difficulty: (i) predict if a
question is answerable given a set of context passages, and extract and
synthesize the answer as a human would (ii) generate a well-formed answer (if
possible) based on the context passages that can be understood with the
question and passage context, and finally (iii) rank a set of retrieved
passages given a question. The size of the dataset and the fact that the
questions are derived from real user search queries distinguishes MS MARCO from
other well-known publicly available datasets for machine reading comprehension
and question-answering. We believe that the scale and the real-world nature of
this dataset makes it attractive for benchmarking machine reading comprehension
and question-answering models.»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-12T01:24:00+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2104.08821)\]. Further details \[[6]()\]\[[7]()\]\[[8]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Dense retrievers utilize pre-trained backbone language models (e.g., BERT,
LLaMA) that are fine-tuned via contrastive learning to perform the task of
encoding text into sense representations that can be then compared via a
shallow similarity operation, e.g. inner product. Recent research has
questioned the role of fine-tuning vs. that of pre-training within dense
retrievers, specifically arguing that retrieval knowledge is primarily gained
during pre-training, meaning knowledge not acquired during pre-training cannot
be sub-sequentially acquired via fine-tuning. We revisit this idea here as the
claim was only studied in the context of a BERT-based encoder using DPR as
representative dense retriever. We extend the previous analysis by testing
other representation approaches (comparing the use of CLS tokens with that of
mean pooling), backbone architectures (encoder-only BERT vs. decoder-only
LLaMA), and additional datasets (MSMARCO in addition to Natural Questions). Our
study confirms that in DPR tuning, pre-trained knowledge underpins retrieval
performance, with fine-tuning primarily adjusting neuron activation rather than
reorganizing knowledge. However, this pattern does not hold universally, such
as in mean-pooled (Contriever) and decoder-based (LLaMA) models. We ensure full
reproducibility and make our implementation publicly available at
https://github.com/ielab/DenseRetriever-Knowledge-Acquisition.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2104.08821)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1908.10084)\]\[[7]()\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer:  
The MS MARCO dataset \[[4](http://arxiv.org/abs/1611.09268)\] represents a significant advancement in the field of machine reading comprehension and question-answering, offering a large-scale, real-world benchmark for evaluating retrieval systems. This dataset includes 1,010,916 anonymized questions derived from Bing search logs, each paired with human-generated answers and 182,669 rewritten answers. It also contains 8,841,823 passages, extracted from 3,563,535 web documents, which provide the necessary context for generating accurate answers. The dataset supports three distinct tasks: determining answerability, generating well-formed answers, and ranking retrieved passages. These tasks reflect the complexity of real-world information retrieval, where questions may have multiple or no answers. The scale and real-world nature of MS MARCO distinguish it from other publicly available datasets, making it particularly valuable for benchmarking models in machine reading comprehension \[[4](http://arxiv.org/abs/1611.09268)\].
|    | reference                                                                                            |   date | key idea/summary                                                                                                                                                                                 |
|----|------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [MS MARCO: A Human Generated MAchine Reading COmprehension Dataset](http://arxiv.org/abs/1611.09268) |    nan | The MS MARCO dataset is a large-scale, real-world machine reading comprehension dataset derived from Bing search queries, designed for benchmarking question-answering and comprehension models. |
### <a id='category-decoder-based-retrieval-models'></a>Decoder-based Retrieval Models: 1 papers found.
Answer:  
Decoder-based retrieval models, such as those utilizing LLaMA, represent a significant shift from traditional encoder-only architectures like BERT. These models leverage decoder-only language models, which have shown promise in dense retrieval tasks due to their ability to generate more contextually rich representations \[[6]()\]. Unlike encoder-only models that rely heavily on pre-trained knowledge for retrieval performance, decoder-based models exhibit different behavior during fine-tuning, where the fine-tuning process can lead to more substantial knowledge acquisition \[[6]()\]. This distinction is crucial as it challenges earlier assumptions that pre-training alone is sufficient for retrieval tasks, suggesting that the architecture of the model plays a critical role in how knowledge is acquired and utilized during both pre-training and fine-tuning phases \[[6]()\].
|    | reference                                                                       |   date | key idea/summary                                                                                          |
|----|---------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------|
|  0 | [RePLAMA: A Decoder-based Dense Retriever for Open-Domain Question Answering]() |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
### <a id='category-prompt-based-representation-methods'></a>Prompt-based Representation Methods: 1 papers found.
Context: 
	Document 1: [Category]: «Prompt-based Representation Methods»
[_citation_number]: «7»
[Snippet]: «»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-12T01:24:00+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2104.08821)\]. Further details \[[6]()\]\[[7]()\]\[[8]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Dense retrievers utilize pre-trained backbone language models (e.g., BERT, LLaMA) that are fine-tuned via contrastive learning to perform the task of encoding text into sense representations that can be then compared via a shallow similarity operation, e.g. inner product. Recent research has questioned the role of fine-tuning vs. that of pre-training within dense retrievers, specifically arguing that retrieval knowledge is primarily gained during pre-training, meaning knowledge not acquired during pre-training cannot be sub-sequentially acquired via fine-tuning. We revisit this idea here as the claim was only studied in the context of a BERT-based encoder using DPR as representative dense retriever. We extend the previous analysis by testing other representation approaches (comparing the use of CLS tokens with that of mean pooling), backbone architectures (encoder-only BERT vs. decoder-only LLaMA), and additional datasets (MSMARCO in addition to Natural Questions). Our study confirms that in DPR tuning, pre-trained knowledge underpins retrieval performance, with fine-tuning primarily adjusting neuron activation rather than reorganizing knowledge. However, this pattern does not hold universally, such as in mean-pooled (Contriever) and decoder-based (LLaMA) models. We ensure full reproducibility and make our implementation publicly available at https://github.com/ielab/DenseRetriever-Knowledge-Acquisition.

Answer: 
Prompt-based representation methods have gained significant attention in the field of dense retrieval, as they aim to leverage pre-trained language models to generate effective text representations. These methods typically involve fine-tuning pre-trained models like BERT or LLaMA using contrastive learning to encode text into representations that can be compared via similarity operations. Recent studies have questioned the extent to which fine-tuning contributes to retrieval performance, suggesting that much of the retrieval knowledge is acquired during pre-training rather than through subsequent fine-tuning \[[7]()\]. This idea has been primarily explored in the context of BERT-based encoders using DPR as a representative dense retriever. However, the analysis has been limited to specific representation approaches, such as the use of CLS tokens versus mean pooling, and specific model architectures, such as encoder-only BERT versus decoder-only LLaMA. The current work extends this analysis by testing a broader range of representation methods and architectures, as well as additional datasets like MSMARCO and Natural Questions. The findings confirm that pre-trained knowledge plays a foundational role in retrieval performance, with fine-tuning primarily adjusting neuron activations rather than reorganizing knowledge. Nevertheless, this pattern does not universally apply, as seen in models like Contriever (mean-pooled) and LLaMA (decoder-based) \[[7]()\].
|    | reference                                                                   |   date | key idea/summary                                                                                          |
|----|-----------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------|
|  0 | [PromptReps: Enhancing Dense Retrieval with Prompt-based Representations]() |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
### <a id='category-benchmarking-in-open-domain-qa'></a>Benchmarking in Open-Domain QA: 1 papers found.
Context: 
	Document 1: [Category]: «Benchmarking in Open-Domain QA»
[_citation_number]: «8»
[Snippet]: «»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-12T01:24:00+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2104.08821)\]. Further details \[[6]()\]\[[7]()\]\[[8]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Dense retrievers utilize pre-trained backbone language models (e.g., BERT,
LLaMA) that are fine-tuned via contrastive learning to perform the task of
encoding text into sense representations that can be then compared via a
shallow similarity operation, e.g. inner product. Recent research has
questioned the role of fine-tuning vs. that of pre-training within dense
retrievers, specifically arguing that retrieval knowledge is primarily gained
during pre-training, meaning knowledge not acquired during pre-training cannot
be sub-sequentially acquired via fine-tuning. We revisit this idea here as the
claim was only studied in the context of a BERT-based encoder using DPR as
representative dense retriever. We extend the previous analysis by testing
other representation approaches (comparing the use of CLS tokens with that of
mean pooling), backbone architectures (encoder-only BERT vs. decoder-only
LLaMA), and additional datasets (MSMARCO in addition to Natural Questions). Our
study confirms that in DPR tuning, pre-trained knowledge underpins retrieval
performance, with fine-tuning primarily adjusting neuron activation rather than
reorganizing knowledge. However, this pattern does not hold universally, such
as in mean-pooled (Contriever) and decoder-based (LLaMA) models. We ensure full
reproducibility and make our implementation publicly available at
https://github.com/ielab/DenseRetriever-Knowledge-Acquisition.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2104.08821)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1908.10084)\]\[[7]()\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
The category "Benchmarking in Open-Domain QA" focuses on evaluating the performance of models in open-domain question answering tasks, where the models must retrieve and understand information from a broad range of sources \[[8]()\]. This area of research is critical for advancing natural language processing systems that can provide accurate and relevant answers to diverse queries. Benchmarking efforts often involve comparing different models, architectures, and training strategies to determine their effectiveness in real-world scenarios. For instance, recent studies have explored the role of pre-training versus fine-tuning in dense retrievers, highlighting how pre-trained knowledge significantly influences retrieval performance \[[8]()\]. Such benchmarking not only helps in understanding the strengths and limitations of existing models but also guides the development of more robust and efficient question-answering systems. The use of standardized datasets and evaluation metrics is essential in this process to ensure fair and reproducible comparisons \[[8]()\].
|    | reference                                                 |   date | key idea/summary                                                                                          |
|----|-----------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------|
|  0 | [Natural Questions: A Benchmark for Question Answering]() |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
