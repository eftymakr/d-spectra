## Related Works

Generative retrieval has emerged as a promising paradigm that replaces traditional search index data structures with a single large-scale neural network, enabling improved efficiency and seamless integration with generative large language models \[[12](http://arxiv.org/abs/2305.11841)\]. This approach directly generates document identifiers through corpus-specific constrained decoding, offering a more end-to-end solution compared to conventional index-retrieve pipelines \[[10](http://arxiv.org/abs/2208.07652)\]. Several recent works have explored the potential of generative retrieval, highlighting its ability to generalize across different document collections \[[13](http://arxiv.org/abs/2311.09134)\].

One of the earliest works in this area is the Differentiable Search Index (DSI), which encodes all information about the corpus within a single Transformer model, allowing direct query-to-docid mapping without external indices \[[8](http://arxiv.org/abs/2202.06991)\]. This approach has been shown to outperform strong baselines such as dual encoder models, particularly in zero-shot settings \[[8](http://arxiv.org/abs/2202.06991)\]. However, the scalability of generative retrieval to large corpora remains a challenge, as most prior studies have only evaluated performance on small-scale datasets \[[12](http://arxiv.org/abs/2305.11841)\].

The concept of using autoregressive models for document retrieval has also been explored in the context of passage retrieval. For example, SEAL leverages autoregressive language models to generate and score distinctive ngrams, mapping them to full passages through an efficient data structure \[[1](http://arxiv.org/abs/2204.10628)\]. This method achieves significant improvements over traditional retrieval systems, particularly on the KILT benchmark \[[1](http://arxiv.org/abs/2204.10628)\]. Similarly, GenRet introduces a discrete auto-encoding approach to learn semantic document identifiers, enabling end-to-end modeling of retrieval tasks \[[3](http://arxiv.org/abs/2304.04171)\].

Another line of work focuses on improving the effectiveness of generative retrieval by addressing the limitations of constrained auto-regressive generation. For instance, the Blended RAG approach combines semantic search techniques with hybrid query strategies to enhance retrieval accuracy, achieving new benchmarks on IR datasets like NQ and TREC-COVID \[[2](http://arxiv.org/abs/2404.07220)\]. Additionally, the RAG framework itself has been widely studied, where pre-trained models are combined with dense vector indexes to provide context for generation \[[5](http://arxiv.org/abs/2005.11401)\]. These approaches demonstrate the potential of integrating retrieval with generation for knowledge-intensive tasks.

In terms of training and optimization, recent studies have focused on improving the efficiency of generative retrieval models. For example, the CorpusBrain model is pre-trained on a large corpus to encode all information about the collection in its parameters, eliminating the need for external indexing \[[10](http://arxiv.org/abs/2208.07652)\]. This approach has shown significant improvements on the KILT benchmark, particularly in zero- and low-resource settings \[[10](http://arxiv.org/abs/2208.07652)\]. Similarly, the Neural Corpus Indexer (NCI) proposes a sequence-to-sequence network that generates relevant document identifiers directly for a query, achieving substantial improvements in recall performance \[[9](http://arxiv.org/abs/2206.02743)\].

Finally, the scalability of generative retrieval to large-scale corpora has been investigated in several studies. The RIPOR framework, for example, introduces a novel prefix-oriented ranking optimization algorithm and constructs document IDs based on relevance associations between queries and documents, leading to significant improvements in retrieval performance \[[13](http://arxiv.org/abs/2311.09134)\]. These findings highlight the ongoing efforts to enhance the generalization capabilities of generative retrieval models on out-of-distribution corpora.

1. \[[1](http://arxiv.org/abs/2204.10628)\] Autoregressive Search Engines: Generating Substrings as Document Identifiers  
2. \[[2](http://arxiv.org/abs/2404.07220)\] Blended RAG: Improving RAG Accuracy with Semantic Search and Hybrid Query-Based Retrievers  
3. \[[3](http://arxiv.org/abs/2304.04171)\] Learning to Tokenize for Generative Retrieval  
4. \[[5](http://arxiv.org/abs/2005.11401)\] Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks  
5. \[[8](http://arxiv.org/abs/2202.06991)\] Transformer Memory as a Differentiable Search Index  
6. \[[9](http://arxiv.org/abs/2206.02743)\] A Neural Corpus Indexer for Document Retrieval  
7. \[[10](http://arxiv.org/abs/2208.07652)\] CorpusBrain: Pre-train a Generative Retrieval Model for Knowledge-Intensive Language Tasks  
8. \[[12](http://arxiv.org/abs/2305.11841)\] How Does Generative Retrieval Scale to Millions of Passages?  
9. \[[13](http://arxiv.org/abs/2311.09134)\] Scalable and Effective Generative Information Retrieval
## Research papers
### Outline
- [Autoregressive Passage Retrieval [1 papers]](#category-autoregressive-passage-retrieval)
- [Retrieval-Augmented Generation Frameworks [2 papers]](#category-retrieval-augmented-generation-frameworks)
- [Generalization on Out-of-Distribution Corpora [1 papers]](#category-generalization-on-out-of-distribution-corpora)
- [Differentiable Search Index Models [2 papers]](#category-differentiable-search-index-models)
- [Training and Optimization Techniques [5 papers]](#category-training-and-optimization-techniques)
- [Generative Retrieval Paradigm [2 papers]](#category-generative-retrieval-paradigm)
- [Scalability of Generative Retrieval [1 papers]](#category-scalability-of-generative-retrieval)

### <a id='category-autoregressive-passage-retrieval'></a>Autoregressive Passage Retrieval: 1 papers found.
Context: 
	Document 1: [Snippet]: «Knowledge-intensive language tasks require NLP systems to both provide the correct answer and retrieve supporting evidence for it in a given corpus. Autoregressive language models are emerging as the de-facto standard for generating answers, with newer and more powerful systems emerging at an astonishing pace. In this paper we argue that all this (and future) progress can be directly applied to the retrieval problem with minimal intervention to the models' architecture. Previous work has explored ways to partition the search space into hierarchical structures and retrieve documents by autoregressively generating their unique identifier. In this work we propose an alternative that doesn't force any structure in the search space: using all ngrams in a passage as its possible identifiers. This setup allows us to use an autoregressive model to generate and score distinctive ngrams, that are then mapped to full passages through an efficient data structure. Empirically, we show this not only outperforms prior autoregressive approaches but also leads to an average improvement of at least 10 points over more established retrieval solutions for passage-level retrieval on the KILT benchmark, establishing new state-of-the-art downstream performance on some datasets, while using a considerably lighter memory footprint than competing systems. Code and pre-trained models at https://github.com/facebookresearch/SEAL.»
[_citation_number]: «1»
[Category]: «Autoregressive Passage Retrieval»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-14T06:54:49+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2304.04171)\]. Further details \[[6](http://arxiv.org/abs/2007.00808)\]\[[7](http://arxiv.org/abs/2308.14968)\]\[[8](http://arxiv.org/abs/2202.06991)\]\[[9](http://arxiv.org/abs/2206.02743)\]\[[10](http://arxiv.org/abs/2208.07652)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Generative retrieval seeks to replace traditional search index data
structures with a single large-scale neural network, offering the potential for
improved efficiency and seamless integration with generative large language
models. As an end-to-end paradigm, generative retrieval adopts a learned
differentiable search index to conduct retrieval by directly generating
document identifiers through corpus-specific constrained decoding. The
generalization capabilities of generative retrieval on out-of-distribution
corpora have gathered significant attention.
  In this paper, we examine the inherent limitations of constrained
auto-regressive generation from two essential perspectives: constraints and
beam search. We begin with the Bayes-optimal setting where the generative
retrieval model exactly captures the underlying relevance distribution of all
possible documents. Then we apply the model to specific corpora by simply
adding corpus-specific constraints. Our main findings are two-fold: (i) For the
effect of constraints, we derive a lower bound of the error, in terms of the KL
divergence between the ground-truth and the model-predicted step-wise marginal
distributions. (ii) For the beam search algorithm used during generation, we
reveal that the usage of marginal distributions may not be an ideal approach.
This paper aims to improve our theoretical understanding of the generalization
capabilities of the auto-regressive decoding retrieval paradigm, laying a
foundation for its limitations and inspiring future advancements toward more
robust and generalizable generative retrieval.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2304.04171)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2404.07220)\]\[[7](http://arxiv.org/abs/2308.14968)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Autoregressive passage retrieval has emerged as a promising approach to address knowledge-intensive language tasks by leveraging the capabilities of autoregressive language models. These models are capable of generating answers while also retrieving supporting evidence from a given corpus \[[1](http://arxiv.org/abs/2204.10628)\]. Unlike traditional methods that rely on structured search indexes, autoregressive models offer a more flexible and integrated solution by directly generating document identifiers through constrained decoding \[[1](http://arxiv.org/abs/2204.10628)\]. Recent work has explored hierarchical structures for document retrieval, but this paper proposes an alternative approach that avoids imposing any structure on the search space \[[1](http://arxiv.org/abs/2204.10628)\]. Instead, it utilizes all ngrams in a passage as potential identifiers, enabling the model to generate and score distinctive ngrams that can then be mapped to full passages using an efficient data structure \[[1](http://arxiv.org/abs/2204.10628)\]. This method not only outperforms prior autoregressive approaches but also achieves significant improvements over established retrieval solutions, demonstrating a new state-of-the-art performance on certain datasets while maintaining a lighter memory footprint \[[1](http://arxiv.org/abs/2204.10628)\].
|    | reference                                                                                                       | date     | key idea/summary                                                                                                                                                                                    |
|----|-----------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Autoregressive Search Engines: Generating Substrings as Document Identifiers](http://arxiv.org/abs/2204.10628) | 04/22/22 | The paper proposes an autoregressive approach for passage-level retrieval that uses all ngrams in a passage as identifiers, achieving state-of-the-art performance with a lighter memory footprint. |
### <a id='category-retrieval-augmented-generation-frameworks'></a>Retrieval-Augmented Generation Frameworks: 2 papers found.
Context: 
	Document 1: [Snippet]: «Retrieval-Augmented Generation (RAG) is a prevalent approach to infuse a private knowledge base of documents with Large Language Models (LLM) to build Generative Q&A (Question-Answering) systems. However, RAG accuracy becomes increasingly challenging as the corpus of documents scales up, with Retrievers playing an outsized role in the overall RAG accuracy by extracting the most relevant document from the corpus to provide context to the LLM. In this paper, we propose the ‘Blended RAG’ method of leveraging semantic search techniques, such as Dense Vector indexes and Sparse Encoder indexes, blended with hybrid query strategies. Our study achieves better retrieval results and sets new benchmarks for IR (Information Retrieval) datasets like NQ and TREC-COVID datasets. We further extend such a ‘Blended Retriever’ to the RAG system to demonstrate far superior results on Generative Q&A datasets like SQUAD, even surpassing fine-tuning performance.»
[_citation_number]: «2»
[Category]: «Retrieval-Augmented Generation Frameworks»

	Document 2: [Snippet]: «Large pre-trained language models have been shown to store factual knowledge in their parameters, and achieve state-of-the-art results when fine-tuned on downstream NLP tasks. However, their ability to access and precisely manipulate knowledge is still limited, and hence on knowledge-intensive tasks, their performance lags behind task-specific architectures. Additionally, providing provenance for their decisions and updating their world knowledge remain open research problems. Pre-trained models with a differentiable access mechanism to explicit non-parametric memory can overcome this issue, but have so far been only investigated for extractive downstream tasks. We explore a general-purpose fine-tuning recipe for retrieval-augmented generation (RAG) -- models which combine pre-trained parametric and non-parametric memory for language generation. We introduce RAG models where the parametric memory is a pre-trained seq2seq model and the non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural retriever. We compare two RAG formulations, one which conditions on the same retrieved passages across the whole generated sequence, the other can use different passages per token. We fine-tune and evaluate our models on a wide range of knowledge-intensive NLP tasks and set the state-of-the-art on three open domain QA tasks, outperforming parametric seq2seq models and task-specific retrieve-and-extract architectures. For language generation tasks, we find that RAG models generate more specific, diverse and factual language than a state-of-the-art parametric-only seq2seq baseline.»
[_citation_number]: «5»
[Category]: «Retrieval-Augmented Generation Frameworks»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-14T06:54:49+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2304.04171)\]. Further details \[[6](http://arxiv.org/abs/2007.00808)\]\[[7](http://arxiv.org/abs/2308.14968)\]\[[8](http://arxiv.org/abs/2202.06991)\]\[[9](http://arxiv.org/abs/2206.02743)\]\[[10](http://arxiv.org/abs/2208.07652)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Generative retrieval seeks to replace traditional search index data
structures with a single large-scale neural network, offering the potential for
improved efficiency and seamless integration with generative large language
models. As an end-to-end paradigm, generative retrieval adopts a learned
differentiable search index to conduct retrieval by directly generating
document identifiers through corpus-specific constrained decoding. The
generalization capabilities of generative retrieval on out-of-distribution
corpora have gathered significant attention.
  In this paper, we examine the inherent limitations of constrained
auto-regressive generation from two essential perspectives: constraints and
beam search. We begin with the Bayes-optimal setting where the generative
retrieval model exactly captures the underlying relevance distribution of all
possible documents. Then we apply the model to specific corpora by simply
adding corpus-specific constraints. Our main findings are two-fold: (i) For the
effect of constraints, we derive a lower bound of the error, in terms of the KL
divergence between the ground-truth and the model-predicted step-wise marginal
distributions. (ii) For the beam search algorithm used during generation, we
reveal that the usage of marginal distributions may not be an ideal approach.
This paper aims to improve our theoretical understanding of the generalization
capabilities of the auto-regressive decoding retrieval paradigm, laying a
foundation for its limitations and inspiring future advancements toward more
robust and generalizable generative retrieval.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2304.04171)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2404.07220)\]\[[7](http://arxiv.org/abs/2308.14968)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Retrieval-Augmented Generation (RAG) frameworks have emerged as a promising approach to enhance the performance of large language models (LLMs) on knowledge-intensive tasks by integrating external knowledge bases \[[2](http://arxiv.org/abs/2404.07220)\]. These frameworks combine pre-trained parametric models with non-parametric memory, such as dense vector indexes, to improve the accuracy and relevance of generated responses \[[5](http://arxiv.org/abs/2005.11401)\]. The effectiveness of RAG relies heavily on the retrievers, which are responsible for selecting the most relevant documents from a large corpus to provide context to the LLM \[[2](http://arxiv.org/abs/2404.07220)\]. Recent studies have explored hybrid retrieval strategies, such as blending dense vector indexes with sparse encoder indexes, to achieve better retrieval results and set new benchmarks on information retrieval datasets like NQ and TREC-COVID \[[2](http://arxiv.org/abs/2404.07220)\]. Furthermore, RAG models have demonstrated superior performance on generative QA tasks, such as SQUAD, often surpassing fine-tuned models \[[2](http://arxiv.org/abs/2404.07220)\]. The integration of differentiable search mechanisms and constrained decoding has also been investigated to improve the generalization capabilities of generative retrieval systems \[[5](http://arxiv.org/abs/2005.11401)\]. These advancements highlight the potential of RAG to address the limitations of standalone LLMs in accessing and manipulating knowledge, while also offering a more robust and flexible framework for language generation tasks \[[5](http://arxiv.org/abs/2005.11401)\].
|    | reference                                                                                                                                                      | date     | key idea/summary                                                                                                                                                                                                                                             |
|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Blended RAG: Improving RAG (Retriever-Augmented Generation) Accuracy with Semantic Search and Hybrid Query-Based Retrievers](http://arxiv.org/abs/2404.07220) | 03/22/24 | Blended RAG improves retrieval accuracy by combining semantic search techniques and hybrid query strategies, achieving better results on both information retrieval and generative Q&A datasets.                                                             |
|  1 | [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](http://arxiv.org/abs/2005.11401)                                                            | 05/22/20 | The paper introduces RAG models that combine pre-trained parametric and non-parametric memory for language generation, achieving state-of-the-art results on knowledge-intensive NLP tasks by improving factual accuracy and diversity in generated outputs. |
### <a id='category-generalization-on-out-of-distribution-corpora'></a>Generalization on Out-of-Distribution Corpora: 1 papers found.
Context: 
	Document 1: [Snippet]: «Conventional document retrieval techniques are mainly based on the index-retrieve paradigm. It is challenging to optimize pipelines based on this paradigm in an end-to-end manner. As an alternative, generative retrieval represents documents as identifiers (docid) and retrieves documents by generating docids, enabling end-to-end modeling of document retrieval tasks. However, it is an open question how one should define the document identifiers. Current approaches to the task of defining document identifiers rely on fixed rule-based docids, such as the title of a document or the result of clustering BERT embeddings, which often fail to capture the complete semantic information of a document. We propose GenRet, a document tokenization learning method to address the challenge of defining document identifiers for generative retrieval. GenRet learns to tokenize documents into short discrete representations (i.e., docids) via a discrete auto-encoding approach. Three components are included in GenRet: (i) a tokenization model that produces docids for documents; (ii) a reconstruction model that learns to reconstruct a document based on a docid; and (iii) a sequence-to-sequence retrieval model that generates relevant document identifiers directly for a designated query. By using an auto-encoding framework, GenRet learns semantic docids in a fully end-to-end manner. We also develop a progressive training scheme to capture the autoregressive nature of docids and to stabilize training. We conduct experiments on the NQ320K, MS MARCO, and BEIR datasets to assess the effectiveness of GenRet. GenRet establishes the new state-of-the-art on the NQ320K dataset. Especially, compared to generative retrieval baselines, GenRet can achieve significant improvements on the unseen documents. GenRet also outperforms comparable baselines on MS MARCO and BEIR, demonstrating the method's generalizability.»
[_citation_number]: «3»
[Category]: «Generalization on Out-of-Distribution Corpora»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-14T06:54:49+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2304.04171)\]. Further details \[[6](http://arxiv.org/abs/2007.00808)\]\[[7](http://arxiv.org/abs/2308.14968)\]\[[8](http://arxiv.org/abs/2202.06991)\]\[[9](http://arxiv.org/abs/2206.02743)\]\[[10](http://arxiv.org/abs/2208.07652)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Generative retrieval seeks to replace traditional search index data
structures with a single large-scale neural network, offering the potential for
improved efficiency and seamless integration with generative large language
models. As an end-to-end paradigm, generative retrieval adopts a learned
differentiable search index to conduct retrieval by directly generating
document identifiers through corpus-specific constrained decoding. The
generalization capabilities of generative retrieval on out-of-distribution
corpora have gathered significant attention.
  In this paper, we examine the inherent limitations of constrained
auto-regressive generation from two essential perspectives: constraints and
beam search. We begin with the Bayes-optimal setting where the generative
retrieval model exactly captures the underlying relevance distribution of all
possible documents. Then we apply the model to specific corpora by simply
adding corpus-specific constraints. Our main findings are two-fold: (i) For the
effect of constraints, we derive a lower bound of the error, in terms of the KL
divergence between the ground-truth and the model-predicted step-wise marginal
distributions. (ii) For the beam search algorithm used during generation, we
reveal that the usage of marginal distributions may not be an ideal approach.
This paper aims to improve our theoretical understanding of the generalization
capabilities of the auto-regressive decoding retrieval paradigm, laying a
foundation for its limitations and inspiring future advancements toward more
robust and generalizable generative retrieval.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2304.04171)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2404.07220)\]\[[7](http://arxiv.org/abs/2308.14968)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The category of generalization on out-of-distribution corpora is a critical area in generative retrieval research, focusing on the ability of models to perform effectively when applied to data not seen during training. This challenge is particularly relevant in real-world applications where models must adapt to new and varied data sources. Current approaches often rely on fixed rule-based document identifiers, such as titles or BERT embeddings, which may not capture the full semantic information of documents, thereby limiting generalization \[[3](http://arxiv.org/abs/2304.04171)\]. To address this, methods like GenRet have been proposed, which use a discrete auto-encoding framework to learn semantic document identifiers in an end-to-end manner, enabling better performance on unseen data \[[3](http://arxiv.org/abs/2304.04171)\]. These methods demonstrate improved generalization on datasets such as NQ320K, MS MARCO, and BEIR, highlighting the importance of learning robust and flexible document representations \[[3](http://arxiv.org/abs/2304.04171)\]. Understanding the limitations of constrained auto-regressive generation, such as the impact of constraints and beam search algorithms, further informs the development of more generalizable generative retrieval models \[[3](http://arxiv.org/abs/2304.04171)\].
|    | reference                                                                        | date     | key idea/summary                                                                                                                                                                                                                                                 |
|----|----------------------------------------------------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Learning to Tokenize for Generative Retrieval](http://arxiv.org/abs/2304.04171) | 04/09/23 | GenRet is a document tokenization learning method that enables end-to-end generative retrieval by learning semantic document identifiers (docids) through a discrete auto-encoding framework, achieving state-of-the-art results on multiple benchmark datasets. |
### <a id='category-differentiable-search-index-models'></a>Differentiable Search Index Models: 2 papers found.
Context: 
	Document 1: [Snippet]: «Open-domain question answering relies on efficient passage retrieval to select candidate contexts, where traditional sparse vector space models, such as TF-IDF or BM25, are the de facto method. In this work, we show that retrieval can be practically implemented using dense representations alone, where embeddings are learned from a small number of questions and passages by a simple dual-encoder framework. When evaluated on a wide range of open-domain QA datasets, our dense retriever outperforms a strong Lucene-BM25 system largely by 9%-19% absolute in terms of top-20 passage retrieval accuracy, and helps our end-to-end QA system establish new state-of-the-art on multiple open-domain QA benchmarks.»
[_citation_number]: «4»
[Category]: «Differentiable Search Index Models»

	Document 2: [Snippet]: «In this paper, we demonstrate that information retrieval can be accomplished with a single Transformer, in which all information about the corpus is encoded in the parameters of the model. To this end, we introduce the Differentiable Search Index (DSI), a new paradigm that learns a text-to-text model that maps string queries directly to relevant docids; in other words, a DSI model answers queries directly using only its parameters, dramatically simplifying the whole retrieval process. We study variations in how documents and their identifiers are represented, variations in training procedures, and the interplay between models and corpus sizes. Experiments demonstrate that given appropriate design choices, DSI significantly outperforms strong baselines such as dual encoder models. Moreover, DSI demonstrates strong generalization capabilities, outperforming a BM25 baseline in a zero-shot setup.»
[_citation_number]: «8»
[Category]: «Differentiable Search Index Models»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-14T06:54:49+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2304.04171)\]. Further details \[[6](http://arxiv.org/abs/2007.00808)\]\[[7](http://arxiv.org/abs/2308.14968)\]\[[8](http://arxiv.org/abs/2202.06991)\]\[[9](http://arxiv.org/abs/2206.02743)\]\[[10](http://arxiv.org/abs/2208.07652)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Generative retrieval seeks to replace traditional search index data
structures with a single large-scale neural network, offering the potential for
improved efficiency and seamless integration with generative large language
models. As an end-to-end paradigm, generative retrieval adopts a learned
differentiable search index to conduct retrieval by directly generating
document identifiers through corpus-specific constrained decoding. The
generalization capabilities of generative retrieval on out-of-distribution
corpora have gathered significant attention.
  In this paper, we examine the inherent limitations of constrained
auto-regressive generation from two essential perspectives: constraints and
beam search. We begin with the Bayes-optimal setting where the generative
retrieval model exactly captures the underlying relevance distribution of all
possible documents. Then we apply the model to specific corpora by simply
adding corpus-specific constraints. Our main findings are two-fold: (i) For the
effect of constraints, we derive a lower bound of the error, in terms of the KL
divergence between the ground-truth and the model-predicted step-wise marginal
distributions. (ii) For the beam search algorithm used during generation, we
reveal that the usage of marginal distributions may not be an ideal approach.
This paper aims to improve our theoretical understanding of the generalization
capabilities of the auto-regressive decoding retrieval paradigm, laying a
foundation for its limitations and inspiring future advancements toward more
robust and generalizable generative retrieval.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2304.04171)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2404.07220)\]\[[7](http://arxiv.org/abs/2308.14968)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Recent advances in differentiable search index models have demonstrated the potential of using neural networks to replace traditional search index structures, enabling more efficient and integrated retrieval systems \[[8](http://arxiv.org/abs/2202.06991)\]. These models, such as the Differentiable Search Index (DSI), encode all corpus information into model parameters, allowing direct query-to-docid mapping without the need for separate index structures \[[8](http://arxiv.org/abs/2202.06991)\]. This approach simplifies the retrieval process and enhances compatibility with generative large language models. Earlier work has also explored dense retrieval methods, where embeddings are learned from questions and passages using dual-encoder frameworks, achieving competitive performance over traditional sparse methods like BM25 \[[4](http://arxiv.org/abs/2004.04906)\]. These studies highlight the shift towards end-to-end retrieval systems that leverage neural representations for improved accuracy and generalization.
|    | reference                                                                                     | date     | key idea/summary                                                                                                                                                                                                                                                                                       |
|----|-----------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Dense Passage Retrieval for Open-Domain Question Answering](http://arxiv.org/abs/2004.04906) | 04/10/20 | This work demonstrates that dense representations can effectively replace traditional sparse methods like TF-IDF or BM25 for open-domain question answering, achieving significant improvements in passage retrieval accuracy.                                                                         |
|  1 | [Transformer Memory as a Differentiable Search Index](http://arxiv.org/abs/2202.06991)        | 02/14/22 | The paper introduces the Differentiable Search Index (DSI), a novel paradigm that uses a single Transformer model to directly answer queries by encoding all corpus information into its parameters, significantly simplifying the information retrieval process and outperforming existing baselines. |
### <a id='category-training-and-optimization-techniques'></a>Training and Optimization Techniques: 5 papers found.
Training and optimization techniques in document retrieval have seen significant advancements, particularly in improving the efficiency and effectiveness of dense and generative retrieval models. Recent approaches focus on addressing the limitations of traditional training mechanisms, such as the use of non-representative negative samples, which can hinder the performance of dense retrieval (DR) models \[[1](http://arxiv.org/abs/2204.10628)\]. To resolve this, methods like Approximate Nearest Neighbor Negative Contrastive Estimation (ANCE) have been introduced, which constructs more realistic negative training instances by leveraging an Approximate Nearest Neighbor (ANN) index updated in parallel with the learning process \[[6](http://arxiv.org/abs/2007.00808)\]. This approach significantly improves the alignment between training and testing data distributions, leading to better performance in DR models \[[6](http://arxiv.org/abs/2007.00808)\]. Similarly, generative retrieval (GR) models, which directly predict document identifiers based on parametric models, face challenges in dynamic environments where new documents are continuously added to the corpus \[[7](http://arxiv.org/abs/2308.14968)\]. To address this, the Continual-LEarner for generatiVE Retrieval (CLEVER) model has been proposed, incorporating techniques like Incremental Product Quantization for efficient encoding of new documents and a memory-augmented learning mechanism to prevent catastrophic forgetting \[[7](http://arxiv.org/abs/2308.14968)\]. Additionally, the Neural Corpus Indexer (NCI) presents an end-to-end deep neural network that unifies training and indexing stages, enhancing recall performance through a prefix-aware weight-adaptive decoder and tailored techniques such as semantic document identifiers \[[9](http://arxiv.org/abs/2206.02743)\]. These innovations highlight the ongoing efforts to optimize retrieval models for both static and dynamic document collections, ensuring they remain effective and efficient in real-world applications \[[9](http://arxiv.org/abs/2206.02743)\].
|    | reference                                                                                                               | date     | key idea/summary                                                                                                                                                                                                                                             |
|----|-------------------------------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval](http://arxiv.org/abs/2007.00808)  | 07/01/20 | ANCE improves dense retrieval by using an Approximate Nearest Neighbor index to generate more realistic negative training instances, resolving the discrepancy between training and testing data distributions and achieving superior performance and speed. |
|  1 | [Continual Learning for Generative Retrieval over Dynamic Corpora](http://arxiv.org/abs/2308.14968)                     | 08/29/23 | The paper introduces CLEVER, a novel model for continual learning in generative retrieval, addressing the challenge of dynamically updating document collections while maintaining retrieval performance.                                                    |
|  2 | [A Neural Corpus Indexer for Document Retrieval](http://arxiv.org/abs/2206.02743)                                       | 06/06/22 | The paper introduces Neural Corpus Indexer (NCI), an end-to-end deep neural network that improves recall performance in document retrieval by unifying training and indexing stages with a prefix-aware weight-adaptive decoder and tailored techniques.     |
|  3 | [Scalable and Effective Generative Information Retrieval](http://arxiv.org/abs/2311.09134)                              | 11/15/23 | RIPOR is an optimization framework for generative retrieval models that improves performance on large-scale benchmarks by introducing a prefix-oriented ranking optimization algorithm and constructing document IDs based on relevance associations.        |
|  4 | [Efficiently Teaching an Effective Dense Retriever with Balanced Topic Aware Sampling](http://arxiv.org/abs/2104.06967) | 04/14/21 | The paper introduces TAS-Balanced, an efficient training method for dense retrieval models that enables state-of-the-art low-latency performance and outperforms existing methods on recall across various cutoffs.                                          |
### <a id='category-generative-retrieval-paradigm'></a>Generative Retrieval Paradigm: 2 papers found.
Context: 
	Document 1: [Snippet]: «Knowledge-intensive language tasks (KILT) usually require a large body of information to provide correct answers. A popular paradigm to solve this problem is to combine a search system with a machine reader, where the former retrieves supporting evidences and the latter examines them to produce answers. Recently, the reader component has witnessed significant advances with the help of large-scale pre-trained generative models. Meanwhile most existing solutions in the search component rely on the traditional "index-retrieve-then-rank'' pipeline, which suffers from large memory footprint and difficulty in end-to-end optimization. Inspired by recent efforts in constructing model-based IR models, we propose to replace the traditional multi-step search pipeline with a novel single-step generative model, which can dramatically simplify the search process and be optimized in an end-to-end manner.»
[_citation_number]: «10»
[Category]: «Generative Retrieval Paradigm»

	Document 2: [Snippet]: «Entities are at the center of how we represent and aggregate knowledge. For instance, Encyclopedias such as Wikipedia are structured by entities (e.g., one per article). The ability to retrieve such entities given a query is fundamental for knowledge-intensive tasks such as entity linking and open-domain question answering. One way to understand current approaches is as classifiers among atomic labels, one for each entity. Their weight vectors are dense entity representations produced by encoding entity information such as descriptions. This approach leads to several shortcomings: i) context and entity affinity is mainly captured through a vector dot product, potentially missing fine-grained interactions between the two; ii) a large memory footprint is needed to store dense representations when considering large entity sets; iii) an appropriately hard set of negative data has to be subsampled at training time.»
[_citation_number]: «11»
[Category]: «Generative Retrieval Paradigm»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-14T06:54:49+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2304.04171)\]. Further details \[[6](http://arxiv.org/abs/2007.00808)\]\[[7](http://arxiv.org/abs/2308.14968)\]\[[8](http://arxiv.org/abs/2202.06991)\]\[[9](http://arxiv.org/abs/2206.02743)\]\[[10](http://arxiv.org/abs/2208.07652)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Generative retrieval seeks to replace traditional search index data
structures with a single large-scale neural network, offering the potential for
improved efficiency and seamless integration with generative large language
models. As an end-to-end paradigm, generative retrieval adopts a learned
differentiable search index to conduct retrieval by directly generating
document identifiers through corpus-specific constrained decoding. The
generalization capabilities of generative retrieval on out-of-distribution
corpora have gathered significant attention.
  In this paper, we examine the inherent limitations of constrained
auto-regressive generation from two essential perspectives: constraints and
beam search. We begin with the Bayes-optimal setting where the generative
retrieval model exactly captures the underlying relevance distribution of all
possible documents. Then we apply the model to specific corpora by simply
adding corpus-specific constraints. Our main findings are two-fold: (i) For the
effect of constraints, we derive a lower bound of the error, in terms of the KL
divergence between the ground-truth and the model-predicted step-wise marginal
distributions. (ii) For the beam search algorithm used during generation, we
reveal that the usage of marginal distributions may not be an ideal approach.
This paper aims to improve our theoretical understanding of the generalization
capabilities of the auto-regressive decoding retrieval paradigm, laying a
foundation for its limitations and inspiring future advancements toward more
robust and generalizable generative retrieval.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2304.04171)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2404.07220)\]\[[7](http://arxiv.org/abs/2308.14968)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Generative retrieval has emerged as a promising paradigm to replace traditional search systems with a single large-scale neural network, offering improved efficiency and seamless integration with generative large language models \[[10](http://arxiv.org/abs/2208.07652)\]. This approach leverages a learned differentiable search index to directly generate document identifiers through corpus-specific constrained decoding, enabling end-to-end optimization \[[10](http://arxiv.org/abs/2208.07652)\]. Recent work has focused on addressing the limitations of existing methods, such as the reliance on traditional "index-retrieve-then-rank" pipelines, which suffer from high memory footprints and suboptimal end-to-end performance \[[10](http://arxiv.org/abs/2208.07652)\]. To mitigate these issues, researchers have proposed novel generative models that encode all information about the corpus into their parameters, eliminating the need for additional indexing structures \[[10](http://arxiv.org/abs/2208.07652)\]. For instance, CorpusBrain is a pre-trained generative retrieval model that demonstrates significant improvements over traditional baselines in KILT tasks, achieving state-of-the-art results while maintaining a compact representation of the corpus \[[10](http://arxiv.org/abs/2208.07652)\]. Similarly, GENRE introduces a generative approach for entity retrieval, where entities are generated token-by-token in an autoregressive fashion, conditioned on the context, thereby capturing fine-grained interactions between the query and entity names \[[11](http://arxiv.org/abs/2010.00904)\]. These models address key shortcomings of previous methods, such as the reliance on dense representations and the need for extensive negative sampling during training \[[11](http://arxiv.org/abs/2010.00904)\]. By directly modeling the retrieval process as a generative task, these approaches enable more flexible and efficient search, particularly in zero- and low-resource settings \[[10](http://arxiv.org/abs/2208.07652)\].
|    | reference                                                                                                                     | date     | key idea/summary                                                                                                                                                                                                                                                                             |
|----|-------------------------------------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [CorpusBrain: Pre-train a Generative Retrieval Model for Knowledge-Intensive Language Tasks](http://arxiv.org/abs/2208.07652) | 08/16/22 | CorpusBrain is a pre-trained generative retrieval model that replaces traditional search pipelines, enabling end-to-end optimization and significant performance improvements on knowledge-intensive language tasks.                                                                         |
|  1 | [Autoregressive Entity Retrieval](http://arxiv.org/abs/2010.00904)                                                            | 10/02/20 | GENRE is a novel system that retrieves entities by generating their unique names token-by-token in an autoregressive fashion, conditioned on the context, addressing limitations of dense representation methods through reduced memory usage and more effective context-entity interaction. |
### <a id='category-scalability-of-generative-retrieval'></a>Scalability of Generative Retrieval: 1 papers found.
Context: 
	Document 1: [Snippet]: «Popularized by the Differentiable Search Index, the emerging paradigm of generative retrieval re-frames the classic information retrieval problem into a sequence-to-sequence modeling task, forgoing external indices and encoding an entire document corpus within a single Transformer. Although many different approaches have been proposed to improve the effectiveness of generative retrieval, they have only been evaluated on document corpora on the order of 100k in size. We conduct the first empirical study of generative retrieval techniques across various corpus scales, ultimately scaling up to the entire MS MARCO passage ranking task with a corpus of 8.8M passages and evaluating model sizes up to 11B parameters. We uncover several findings about scaling generative retrieval to millions of passages; notably, the central importance of using synthetic queries as document representations during indexing, the ineffectiveness of existing proposed architecture modifications when accounting for compute cost, and the limits of naively scaling model parameters with respect to retrieval performance. While we find that generative retrieval is competitive with state-of-the-art dual encoders on small corpora, scaling to millions of passages remains an important and unsolved challenge.»
[_citation_number]: «12»
[Category]: «Scalability of Generative Retrieval»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-14T06:54:49+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2304.04171)\]. Further details \[[6](http://arxiv.org/abs/2007.00808)\]\[[7](http://arxiv.org/abs/2308.14968)\]\[[8](http://arxiv.org/abs/2202.06991)\]\[[9](http://arxiv.org/abs/2206.02743)\]\[[10](http://arxiv.org/abs/2208.07652)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Generative retrieval seeks to replace traditional search index data
structures with a single large-scale neural network, offering the potential for
improved efficiency and seamless integration with generative large language
models. As an end-to-end paradigm, generative retrieval adopts a learned
differentiable search index to conduct retrieval by directly generating
document identifiers through corpus-specific constrained decoding. The
generalization capabilities of generative retrieval on out-of-distribution
corpora have gathered significant attention.
  In this paper, we examine the inherent limitations of constrained
auto-regressive generation from two essential perspectives: constraints and
beam search. We begin with the Bayes-optimal setting where the generative
retrieval model exactly captures the underlying relevance distribution of all
possible documents. Then we apply the model to specific corpora by simply
adding corpus-specific constraints. Our main findings are two-fold: (i) For the
effect of constraints, we derive a lower bound of the error, in terms of the KL
divergence between the ground-truth and the model-predicted step-wise marginal
distributions. (ii) For the beam search algorithm used during generation, we
reveal that the usage of marginal distributions may not be an ideal approach.
This paper aims to improve our theoretical understanding of the generalization
capabilities of the auto-regressive decoding retrieval paradigm, laying a
foundation for its limitations and inspiring future advancements toward more
robust and generalizable generative retrieval.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2304.04171)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2404.07220)\]\[[7](http://arxiv.org/abs/2308.14968)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The scalability of generative retrieval has emerged as a critical area of research, particularly with the increasing size of document corpora. Recent work has highlighted the challenges of scaling generative retrieval techniques to large-scale datasets, such as those containing millions of passages \[[12](http://arxiv.org/abs/2305.11841)\]. This includes the need for efficient indexing strategies, such as the use of synthetic queries as document representations during indexing, which has been shown to significantly improve retrieval performance \[[12](http://arxiv.org/abs/2305.11841)\]. Additionally, the effectiveness of existing architectural modifications for generative retrieval models has been questioned, particularly when considering the trade-offs between model size, computational cost, and retrieval accuracy \[[12](http://arxiv.org/abs/2305.11841)\]. These findings underscore the limitations of naively scaling model parameters, suggesting that performance gains may not be linear with increased model size \[[12](http://arxiv.org/abs/2305.11841)\]. As generative retrieval continues to gain traction as an alternative to traditional indexing methods, addressing these scalability challenges remains a key focus for future research.
|    | reference                                                                                       | date     | key idea/summary                                                                                                                                                                                                                                                        |
|----|-------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [How Does Generative Retrieval Scale to Millions of Passages?](http://arxiv.org/abs/2305.11841) | 05/19/23 | This paper presents the first empirical study of generative retrieval techniques across large-scale document corpora, revealing challenges in scaling to millions of passages and highlighting the importance of synthetic queries and compute-efficient architectures. |
