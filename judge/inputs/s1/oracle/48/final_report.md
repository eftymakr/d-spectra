## Related Works

Neural retrieval methods using transformer-based pre-trained language models have advanced multilingual and cross-lingual retrieval \[[10](http://arxiv.org/abs/2402.05672)\]. However, their effectiveness for low-resource, morphologically rich languages such as Amharic remains underexplored due to data scarcity and suboptimal tokenization \[[15](https://aclanthology.org/2021.mrl-1.11/)\]. This gap is addressed by introducing Amharic-specific dense retrieval models based on pre-trained Amharic BERT and RoBERTa backbones \[[15](https://aclanthology.org/2021.mrl-1.11/)\]. These models demonstrate significant improvements over existing multilingual baselines, such as Arctic Embed 2.0 \[[9](http://arxiv.org/abs/2412.04506)\], which, while effective for many languages, suffers from degraded English retrieval quality \[[9](http://arxiv.org/abs/2412.04506)\]. The proposed RoBERTa-Base-Amharic-Embed model (110M parameters) achieves a 17.6% relative improvement in MRR@10 and a 9.86% gain in Recall@10 over the strongest multilingual baseline \[[15](https://aclanthology.org/2021.mrl-1.11/)\]. More compact variants, such as RoBERTa-Medium-Amharic-Embed (42M), remain competitive while being over 13x smaller \[[15](https://aclanthology.org/2021.mrl-1.11/)\].

The importance of language-specific adaptation is underscored by the limitations of multilingual models, which often exhibit systematic deficiencies affecting certain language pairs \[[4](http://arxiv.org/abs/1906.01502)\]. For instance, Multilingual BERT (M-BERT) shows surprising zero-shot cross-lingual transfer capabilities but still has systematic deficiencies \[[4](http://arxiv.org/abs/1906.01502)\]. Similarly, XLM-R, a multilingual language model trained at scale, outperforms mBERT on a variety of cross-lingual benchmarks but still faces challenges in low-resource languages \[[5](http://arxiv.org/abs/1911.02116)\]. These findings highlight the need for language-specific models to achieve optimal performance in low-resource settings.

In addition to dense retrieval, sparse retrieval methods such as BM25 have been widely used in open-domain question answering \[[2](http://arxiv.org/abs/2004.04906)\]. However, recent work has shown that dense retrievers can outperform sparse methods by a significant margin \[[2](http://arxiv.org/abs/2004.04906)\]. For example, dense passage retrieval using a dual-encoder framework has been shown to outperform BM25 by 9%-19% in top-20 passage retrieval accuracy \[[2](http://arxiv.org/abs/2004.04906)\]. Furthermore, contrastive learning has been used to train unsupervised dense retrievers, achieving strong performance in various retrieval settings \[[7](http://arxiv.org/abs/2112.09118)\]. This includes cross-lingual retrieval, where training data is even scarcer than for English \[[7](http://arxiv.org/abs/2112.09118)\].

The development of multilingual language models for African languages has also been an active area of research. SERENGETI, a massively multilingual language
## Research papers
### Outline
- [Sparse vs. Dense Retrieval Methods [5 papers]](#category-sparse-vs.-dense-retrieval-methods)
- [Contrastive Learning in Retrieval [2 papers]](#category-contrastive-learning-in-retrieval)
- [Cross-Lingual Retrieval [4 papers]](#category-cross-lingual-retrieval)
- [Low-Resource Language Challenges [3 papers]](#category-low-resource-language-challenges)
- [Tokenization and Data Scarcity [1 papers]](#category-tokenization-and-data-scarcity)
- [Multilingual Retrieval Models [1 papers]](#category-multilingual-retrieval-models)
- [Public Dataset and Code Release [2 papers]](#category-public-dataset-and-code-release)

### <a id='category-sparse-vs.-dense-retrieval-methods'></a>Sparse vs. Dense Retrieval Methods: 5 papers found.
Context: 
	Document 1: [Category]: «Sparse vs. Dense Retrieval Methods»
[Snippet]: «In neural Information Retrieval (IR), ongoing research is directed towards improving the first retriever in ranking pipelines. Learning dense embeddings to conduct retrieval using efficient approximate nearest neighbors methods has proven to work well. Meanwhile, there has been a growing interest in learning sparse representations for documents and queries, that could inherit from the desirable properties of bag-of-words models such as the exact matching of terms and the efficiency of inverted indexes. Introduced recently, the SPLADE model provides highly sparse representations and competitive results with respect to state-of-the-art dense and sparse approaches. In this paper, we build on SPLADE and propose several significant improvements in terms of effectiveness and/or efficiency. More specifically, we modify the pooling mechanism, benchmark a model solely based on document expansion, and introduce models trained with distillation. We also report results on the BEIR benchmark. Overall, SPLADE is considerably improved with more than 9% gains on NDCG@10 on TREC DL 2019, leading to state-of-the-art results on the BEIR benchmark.»
[_citation_number]: «1»

	Document 2: [Category]: «Sparse vs. Dense Retrieval Methods»
[Snippet]: «Open-domain question answering relies on efficient passage retrieval to select candidate contexts, where traditional sparse vector space models, such as TF-IDF or BM25, are the de facto method. In this work, we show that retrieval can be practically implemented using dense representations alone, where embeddings are learned from a small number of questions and passages by a simple dual-encoder framework. When evaluated on a wide range of open-domain QA datasets, our dense retriever outperforms a strong Lucene-BM25 system largely by 9%-19% absolute in terms of top-20 passage retrieval accuracy, and helps our end-to-end QA system establish new state-of-the-art on multiple open-domain QA benchmarks.»
[_citation_number]: «2»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-25T23:06:20+00:00. Mention them in a separate, numbered
|    | reference                                                                                                  |   date | key idea/summary                                                                                                                                                                                                    |
|----|------------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [SPLADE v2: Sparse Lexical and Expansion Model for Information Retrieval](http://arxiv.org/abs/2109.10086) |    nan | The paper presents improvements to the SPLADE model, resulting in significant gains in effectiveness and efficiency, achieving state-of-the-art results on the BEIR benchmark.                                      |
|  1 | [Dense Passage Retrieval for Open-Domain Question Answering](http://arxiv.org/abs/2004.04906)              |    nan | This work demonstrates that dense representations can effectively replace traditional sparse methods like BM25 in open-domain question answering, achieving significant improvements in passage retrieval accuracy. |
|  2 | [The Probabilistic Relevance Framework: (BM25) and Beyond]()                                               |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                           |
|  3 | [SPLADE: Sparse Lexical and Expansion Model for First Stage Ranking]()                                     |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                           |
|  4 | [Context-aware term weighting for first stage passage retrieval]()                                         |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                           |
### <a id='category-contrastive-learning-in-retrieval'></a>Contrastive Learning in Retrieval: 2 papers found.
Document 1 highlights the challenges in dense retrieval (DR) where negative instances used during training are not representative of the irrelevant documents encountered during testing, leading to a discrepancy between training and testing data distributions \[[3](http://arxiv.org/abs/2007.00808)\]. To address this, the paper introduces Approximate Nearest Neighbor Negative Contrastive Estimation (ANCE), a training mechanism that constructs more realistic negative training instances by leveraging an Approximate Nearest Neighbor (ANN) index of the corpus, which is updated in parallel with the learning process \[[3](http://arxiv.org/abs/2007.00808)\]. This approach significantly improves the effectiveness of DR models, as demonstrated by the performance of the BERT-Siamese model using ANCE, which outperforms existing dense and sparse retrieval baselines and nearly matches the accuracy of sparse-retrieval-and-BERT-reranking \[[3](http://arxiv.org/abs/2007.00808)\]. 

Document 2 discusses the limitations of dense retrievers, particularly in scenarios with limited training data, and explores the potential of contrastive learning for training unsupervised dense retrievers \[[7](http://arxiv.org/abs/2112.09118)\]. The study demonstrates that contrastive learning can achieve strong performance across various retrieval settings, outperforming BM25 on 11 out of 15 datasets in the BEIR benchmark \[[7](http://arxiv.org/abs/2112.09118)\]. Furthermore, the paper emphasizes the importance of cross-lingual transfer, showing that unsupervised models can effectively retrieve documents in low-resource languages like Swahili when fine-tuned on English data \[[7](http://arxiv.org/abs/2112.09118)\]. These findings underscore the value of contrastive learning in enhancing retrieval effectiveness, especially in multilingual and low-resource settings \[[7](http://arxiv.org/abs/2112.09118)\].
|    | reference                                                                                                                |   date | key idea/summary                                                                                                                                                                                                                                             |
|----|--------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Approximate Nearest Neighbor Negative Contrastive Learning for Dense
  Text Retrieval](http://arxiv.org/abs/2007.00808) |    nan | ANCE improves dense retrieval by using an Approximate Nearest Neighbor index to generate more realistic negative training instances, resolving the discrepancy between training and testing data distributions and achieving superior performance and speed. |
|  1 | [Unsupervised Dense Information Retrieval with Contrastive Learning](http://arxiv.org/abs/2112.09118)                    |    nan | This work explores contrastive learning for training unsupervised dense retrievers, achieving strong performance in various retrieval settings and demonstrating cross-lingual transfer capabilities.                                                        |
### <a id='category-cross-lingual-retrieval'></a>Cross-Lingual Retrieval: 4 papers found.
Context: 
	Document 1: [Category]: «Cross-Lingual Retrieval»
[Snippet]: «In this paper, we show that Multilingual BERT (M-BERT), released by Devlin et
al. (2018) as a single language model pre-trained from monolingual corpora in
104 languages, is surprisingly good at zero-shot cross-lingual model transfer,
in which task-specific annotations in one language are used to fine-tune the
model for evaluation in another language. To understand why, we present a large
number of probing experiments, showing that transfer is possible even to
languages in different scripts, that transfer works best between typologically
similar languages, and that the model can find translation pairs. From these
results, we can conclude that M-BERT does create multilingual representations,
but that these representations exhibit systematic deficiencies affecting
certain language pairs.»
[_citation_number]: «4»

	Document 2: [Category]: «Cross-Lingual Retrieval»
[Snippet]: «This paper shows that pretraining multilingual language models at scale leads
to significant performance gains for a wide range of cross-lingual transfer
tasks. We train a Transformer-based masked language model on one hundred
languages, using more than two terabytes of filtered CommonCrawl data. Our
model, dubbed XLM-R, significantly outperforms multilingual BERT (mBERT) on a
variety of cross-lingual benchmarks, including +14.6% average accuracy on XNLI,
+13% average F1 score on MLQA, and +2.4% F1 score on NER. XLM-R performs
particularly well on low-resource languages, improving 15.7% in XNLI accuracy
for Swahili and 11.4% for Urdu over previous XLM models.»
[_citation_number]: «5»

	Document 3: [Category]: «Cross-Lingual Retrieval»
[Snippet]: «This technical report presents the training methodology and evaluation
results of the open-source multilingual E5 text embedding models, released in
mid-2023. Three embedding models of different sizes (small / base / large) are
provided, offering a balance between the inference efficiency and embedding
quality. The training procedure adheres to the English E5 model recipe,
involving contrastive pre-training on 1 billion multilingual text pairs,
follow
|    | reference                                                                                      |   date | key idea/summary                                                                                                                                                                                                                                                                                             |
|----|------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [How multilingual is Multilingual BERT?](http://arxiv.org/abs/1906.01502)                      |    nan | Multilingual BERT (M-BERT) demonstrates strong zero-shot cross-lingual transfer capabilities, even across different scripts and typologically similar languages, though it has systematic deficiencies in certain language pairs.                                                                            |
|  1 | [Unsupervised Cross-lingual Representation Learning at Scale](http://arxiv.org/abs/1911.02116) |    nan | This paper demonstrates that pretraining multilingual language models at scale significantly improves cross-lingual transfer tasks, with XLM-R outperforming mBERT on various benchmarks and maintaining strong performance on both high- and low-resource languages.                                        |
|  2 | [Multilingual E5 Text Embeddings: A Technical Report](http://arxiv.org/abs/2402.05672)         |    nan | This technical report introduces open-source multilingual E5 text embedding models, offering different sizes (small, base, large) with a balance between inference efficiency and embedding quality, and includes a new instruction-tuned model performing on par with state-of-the-art English-only models. |
|  3 | [Morphologically annotated (Amharic) text corpora]()                                           |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                                    |
### <a id='category-low-resource-language-challenges'></a>Low-Resource Language Challenges: 3 papers found.
Context: 
	Document 1: [Category]: «Low-Resource Language Challenges»
[Snippet]: «Multilingual pretrained language models (mPLMs) acquire valuable, generalizable linguistic information during pretraining and have advanced the state of the art on task-specific finetuning. To date, only ~31 out of ~2,000 African languages are covered in existing language models. We ameliorate this limitation by developing SERENGETI, a massively multilingual language model that covers 517 African languages and language varieties. We evaluate our novel models on eight natural language understanding tasks across 20 datasets, comparing to 4 mPLMs that cover 4-23 African languages. SERENGETI outperforms other models on 11 datasets across the eight tasks, achieving 82.27 average F_1. We also perform analyses of errors from our models, which allows us to investigate the influence of language genealogy and linguistic similarity when the models are applied under zero-shot settings. We will publicly release our models for research.\footnote(\href(https://github.com/UBC-NLP/serengeti)(https://github.com/UBC-NLP/serengeti))»
[_citation_number]: «6»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-25T23:06:20+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2007.00808)\]. Further details \[[6](http://arxiv.org/abs/2212.10785)\]\[[7](http://arxiv.org/abs/2112.09118)\]\[[8](http://arxiv.org/abs/2012.15613)\]\[[9](http://arxiv.org/abs/2412.04506)\]\[[10](http://arxiv.org/abs/2402.05672)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Neural retrieval methods using transformer-based pre-trained language models have advanced multilingual and cross-lingual retrieval. However, their effectiveness for low-resource, morphologically rich languages such as Amharic remains underexplored due to data scarcity and suboptimal tokenization. We address this
|    | reference                                                                                                                                                             |   date | key idea/summary                                                                                                                                                                                               |
|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [SERENGETI: Massively Multilingual Language Models for Africa](http://arxiv.org/abs/2212.10785)                                                                       |    nan | SERENGETI is a massively multilingual language model that covers 517 African languages and language varieties, outperforming existing models on 11 datasets across eight natural language understanding tasks. |
|  1 | [Small Data? (No) Problem! (Exploring) the Viability of Pretrained Multilingual Language Models for Low-resourced Languages](https://aclanthology.org/2021.mrl-1.11/) |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                      |
|  2 | [The Development of Pre-processing Tools and Pre-trained Embedding Models for (A)mharic](https://aclanthology.org/2021.winlp-1.5/)                                    |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                      |
### <a id='category-tokenization-and-data-scarcity'></a>Tokenization and Data Scarcity: 1 papers found.
Context: 
	Document 1: [Category]: «Tokenization and Data Scarcity»
[Snippet]: «In this work, we provide a systematic and comprehensive empirical comparison
of pretrained multilingual language models versus their monolingual
counterparts with regard to their monolingual task performance. We study a set
of nine typologically diverse languages with readily available pretrained
monolingual models on a set of five diverse monolingual downstream tasks. We
first aim to establish, via fair and controlled comparisons, if a gap between
the multilingual and the corresponding monolingual representation of that
language exists, and subsequently investigate the reason for any performance
difference. To disentangle conflating factors, we train new monolingual models
on the same data, with monolingually and multilingually trained tokenizers. We
find that while the pretraining data size is an important factor, a designated
monolingual tokenizer plays an equally important role in the downstream
performance. Our results show that languages that are adequately represented in
the multilingual model's vocabulary exhibit negligible performance decreases
over their monolingual counterparts. We further find that replacing the
original multilingual tokenizer with the specialized monolingual tokenizer
improves the downstream performance of the multilingual model for almost every
task and language.»
[_citation_number]: «8»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-25T23:06:20+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2007.00808)\]. Further details \[[6](http://arxiv.org/abs/2212.10785)\]\[[7](http://arxiv.org/abs/2112.09118)\]\[[8](http://arxiv.org/abs/2012.15613)\]\[[9](http://arxiv.org/abs/2412.04506)\]\[[10](http://arxiv.org/abs/2402.05672)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Neural retrieval methods using transformer-based pre-trained language models
have advanced multilingual and cross-lingual retrieval. However, their
effectiveness for low-resource, morphologically rich languages such as Amharic

|    | reference                                                                                                                       |   date | key idea/summary                                                                                                                                                                                                                                                      |
|----|---------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [How Good is Your Tokenizer? On the Monolingual Performance of
  Multilingual Language Models](http://arxiv.org/abs/2012.15613) |    nan | This work compares pretrained multilingual language models with monolingual counterparts, finding that monolingual tokenizers significantly impact downstream performance, and that adequate representation in multilingual models leads to minimal performance loss. |
### <a id='category-multilingual-retrieval-models'></a>Multilingual Retrieval Models: 1 papers found.
Context: 
	Document 1: [Category]: «Multilingual Retrieval Models»
[Snippet]: «This paper presents the training methodology of Arctic-Embed 2.0, a set of
open-source text embedding models built for accurate and efficient multilingual
retrieval. While prior works have suffered from degraded English retrieval
quality, Arctic-Embed 2.0 delivers competitive retrieval quality on
multilingual and English-only benchmarks, and supports Matryoshka
Representation Learning (MRL) for efficient embedding storage with
significantly lower compressed quality degradation compared to alternatives. We
detail the design and implementation, presenting several important open
research questions that arose during model development. We conduct experiments
exploring these research questions and include extensive discussion aimed at
fostering further discussion in this field.»
[_citation_number]: «9»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-25T23:06:20+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2007.00808)\]. Further details \[[6](http://arxiv.org/abs/2212.10785)\]\[[7](http://arxiv.org/abs/2112.09118)\]\[[8](http://arxiv.org/abs/2012.15613)\]\[[9](http://arxiv.org/abs/2412.04506)\]\[[10](http://arxiv.org/abs/2402.05672)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Neural retrieval methods using transformer-based pre-trained language models
have advanced multilingual and cross-lingual retrieval. However, their
effectiveness for low-resource, morphologically rich languages such as Amharic
remains underexplored due to data scarcity and suboptimal tokenization. We
address this gap by introducing Amharic-specific dense retrieval models based
on pre-trained Amharic BERT and RoBERTa backbones. Our proposed
RoBERTa-Base-Amharic-Embed model (110M parameters) achieves a 17.6% relative
improvement in MRR@10 and a 9.86% gain in Recall@10 over the strongest

|    | reference                                                                                      |   date | key idea/summary                                                                                                                                                                                                                      |
|----|------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Arctic-Embed 2.0: Multilingual Retrieval Without Compromise](http://arxiv.org/abs/2412.04506) |    nan | Arctic-Embed 2.0 is an open-source multilingual text embedding model that provides competitive retrieval quality in both multilingual and English-only benchmarks, with efficient storage through Matryoshka Representation Learning. |
### <a id='category-public-dataset-and-code-release'></a>Public Dataset and Code Release: 2 papers found.
Context: 
	Document 1: [Category]: «Public Dataset and Code Release»
[Snippet]: «In NLP, text classification is one of the primary problems we try to solve
and its uses in language analyses are indisputable. The lack of labeled
training data made it harder to do these tasks in low resource languages like
Amharic. The task of collecting, labeling, annotating, and making valuable this
kind of data will encourage junior researchers, schools, and machine learning
practitioners to implement existing classification models in their language. In
this short paper, we aim to introduce the Amharic text classification dataset
that consists of more than 50k news articles that were categorized into 6
classes. This dataset is made available with easy baseline performances to
encourage studies and better performance experiments.»
[_citation_number]: «11»

	Document 2: [Category]: «Public Dataset and Code Release»
[Snippet]: «»
[_citation_number]: «18»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-25T23:06:20+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2007.00808)\]. Further details \[[6](http://arxiv.org/abs/2212.10785)\]\[[7](http://arxiv.org/abs/2112.09118)\]\[[8](http://arxiv.org/abs/2012.15613)\]\[[9](http://arxiv.org/abs/2412.04506)\]\[[10](http://arxiv.org/abs/2402.05672)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Neural retrieval methods using transformer-based pre-trained language models
have advanced multilingual and cross-lingual retrieval. However,
their effectiveness for low-resource, morphologically rich languages such as Amharic
remains underexplored due to data scarcity and suboptimal tokenization. We
address this gap by introducing Amharic-specific dense retrieval models based
on pre-trained Amharic BERT and RoBERTa backbones. Our proposed
RoBERTa-Base-Amharic-Embed model (110M parameters)
|    | reference                                                                                                          |   date | key idea/summary                                                                                                                                                                                        |
|----|--------------------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [An Amharic News Text classification Dataset](http://arxiv.org/abs/2103.05639)                                     |    nan | This paper introduces an Amharic text classification dataset with over 50k news articles categorized into 6 classes, aimed at encouraging research and improving performance in low-resource languages. |
|  1 | [(2AIRTC): The (Amharic) Adhoc Information Retrieval Test Collection](https://doi.org/10.1007/978-3-030-58219-7_5) |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                               |
