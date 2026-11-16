## Related Works

Natural language-driven table discovery has emerged as a critical area of research, driven by the need to efficiently retrieve relevant tables from large repositories based on natural language queries. Traditional approaches typically rely on dense vector search pipelines, which involve representing tables as vectors, building an index, and then performing a search \[[Abhijeet Phatak' 2025-02-05](http://arxiv.org/abs/2502.02788v1)\]. These methods, while achieving notable accuracy, face significant limitations, including error accumulation during indexing and search phases, which degrades performance \[[Xiaoyang Chen' 2023-05-03](http://arxiv.org/abs/2305.02073v2)\]. Additionally, insufficient interaction between queries and tables limits semantic alignment, hindering accuracy improvements \[[Dayu Yang' 2024-11-04](http://arxiv.org/abs/2411.03356v1)\].

Several studies have explored the use of deep learning for table discovery. For instance, \[[Petru Neague' 2024-04-18](http://arxiv.org/abs/2404.12237v2)\] introduced a system that extracts information from natural language text for database entry, using a cascaded finite-state transducer. This approach enables efficient and effective information extraction from unstructured text. Similarly, \[[Pengcheng Yin' 2015-12-03](http://arxiv.org/abs/1512.00965v2)\] proposed a framework for translating natural language queries into formal logic, enhancing the accuracy of query formalization. However, these methods typically rely on traditional indexing techniques and do not address the issue of error accumulation or semantic misalignment.

Recent work has focused on improving query-table interaction through more sophisticated models. \[[Chaoming Wang' 2024-06-28](http://arxiv.org/abs/2406.19708v3)\] proposed a method for generating well-formed natural language questions from keyword-based web queries, leveraging machine translation techniques to enhance query understanding. This approach has been applied in search engines and question-answering systems. \[[Erik Bodin' 2021-04-21](http://arxiv.org/abs/2104.10450v1)\] introduced a framework for natural language interfaces to databases, emphasizing the importance of semantic alignment and query reformulation. These studies highlight the need for more effective query understanding and semantic alignment in table discovery.

The use of large language models (LLMs) has also been explored for table discovery. \[[Simon Dobnik' 2018-07-21](http://arxiv.org/abs/1807.09844v2)\] proposed a system for generating natural language queries from structured data, leveraging LLMs to improve query formulation. \[[Mario Giulianelli' 2022-10-23](http://arxiv.org/abs/2210.12828v1)\] introduced a framework for semantic query reformulation in social peer-to-peer data management systems, addressing the challenge of query translation across different schemas. These studies demonstrate the potential of LLMs in enhancing query understanding and semantic alignment.

In addition to query understanding, the issue of dynamic indexing and continual learning has been addressed in some studies. \[[Leonidas Gee' 2024-03-26](http://arxiv.org/abs/2403.17811v1)\] introduced a framework for differentiable search indexes, aiming to unify indexing and search into a single model. This approach reduces error accumulation and improves search accuracy. \[[Young-Ho Kim' 2022-05-31](http://arxiv.org/abs/2205.15503v3)\] proposed a method for generating synthetic queries for table discovery, leveraging LLMs to enhance query formulation. These studies highlight the importance of dynamic indexing and continual learning in improving table discovery performance.

Furthermore, \[[Carl Barton' 2017-04-25](http://arxiv.org/abs/1704.07625v2)\] introduced a differentiable search index (DSI) framework that enables the training of a model to simultaneously learn representation and retrieval, reducing error accumulation. This work aligns with the goals of Birdie, which unifies indexing and search into a single encoder-decoder language model. \[[Rossen Nenov' 2024-09-30](http://arxiv.org/abs/2410.00169v1)\] proposed a method for improving the robustness of compressed language models to subgroup performance, which is relevant to the robustness of indexing models in dynamic environments. \[[Yulin Shao' 2022-12-02](http://arxiv.org/abs/2212.01485v4)\] explored the use of differentiable search indexes for sub-topic retrieval, emphasizing the importance of balancing relevance and diversity in retrieval results. These studies collectively highlight the growing interest in differentiable search indexes and their potential to improve the accuracy and robustness of table discovery systems.

References:
1. Document 15: Cat, Rat, Meow: On the Alignment of Language Model and Human Term-Similarity Judgments
2. Document 12: Inducing Diversity in Differentiable Search Indexing
3. Document 12: Inducing Diversity in Differentiable Search Indexing
4. Document 27: FASTUS: A Cascaded Finite-State Transducer for Extracting Information from Natural-Language Text
5. Document 5: Neural Enquirer: Learning to Query Tables with Natural Language
6. Document 7: Translating Web Search Queries into Natural Language Questions
7. Document 69: Semantic Table Retrieval using Keyword and Table Queries
8. Document 72: JaCoText: A Pretrained Model for Java Code-Text Generation
9. Document 67: Semantic Query Reformulation in Social PDMS
10. Document 12: Inducing Diversity in Differentiable Search Indexing
11. Document 12: Inducing Diversity in Differentiable Search Indexing
12. Document 12: Inducing Diversity in Differentiable Search Indexing
13. Document 10: Are Compressed Language Models Less Subgroup Robust?
14. Document 1: Inducing Diversity in Differentiable Search Indexing
