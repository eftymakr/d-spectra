## Related Works

The integration of knowledge graphs (KGs) with large language models (LLMs) to enhance reasoning capabilities for claim verification is an emerging research area. While KGs offer structured, semantically rich representations suitable for reasoning, most existing verification methods rely on unstructured text corpora, limiting their ability to leverage KGs effectively \[[Zhenyu Li' 2023-08-23](http://arxiv.org/abs/2308.12060v3)\]. Additionally, modern LLMs, despite their strong reasoning abilities, struggle with multi-step modular pipelines and reasoning over KGs without adaptation \[[Qianbo Zang' 2025-05-08](http://arxiv.org/abs/2505.05583v1)\]. This section reviews related works that address these challenges, focusing on methods that integrate KGs with LLMs for claim verification and reasoning tasks.

Several studies have explored the use of KGs to enhance LLMs' reasoning capabilities. For instance, \[[Lei Sun' 2024-04-11](http://arxiv.org/abs/2404.07677v2)\] proposes a method for evaluating class membership relations in KGs using LLMs, achieving high F1-scores on datasets like Wikidata and CaLiGraph. This work highlights the potential of LLMs in knowledge graph refinement, though it does not directly address claim verification. Similarly, \[[Shirui Pan' 2023-06-14](http://arxiv.org/abs/2306.08302v3)\] introduces a framework for designing Graph Neural Networks (GNNs) by leveraging knowledge from LLMs, emphasizing the need for structured knowledge priors. These works demonstrate the value of structured knowledge in improving model performance but do not focus on claim verification.

In the realm of claim verification, \[[Jiaoyan Chen' 2021-12-18](http://arxiv.org/abs/2112.10006v6)\] presents a comprehensive roadmap for unifying LLMs and KGs, outlining three frameworks: KG-enhanced LLMs, LLM-augmented KGs, and synergized LLMs + KGs. This work sets the stage for future research on integrating LLMs and KGs for reasoning tasks. \[[Haoran Wang' 2023-10-08](http://arxiv.org/abs/2310.05253v2)\] introduces a framework for generating knowledge graphs in the scholarly domain, using NLP and ML techniques to extract entities and relationships from research publications. This work shows the potential of KGs in managing complex interconnected data but does not directly address claim verification.

The use of LLMs for knowledge engineering tasks has also been explored. \[[Harry Li' 2024-06-07](http://arxiv.org/abs/2406.06621v2)\] presents a case study on using LLMs for knowledge engineering in Wikidata, achieving a macro-averaged F1-score of 0.701. This work highlights the potential of LLMs in KG completion and correction but does not focus on claim verification. \[[Qiyuan Li' 2025-02-28](http://arxiv.org/abs/2502.20988v2)\] introduces a framework for knowledge engineering that leverages LLMs to probe KGs and link entities to their respective QIDs, demonstrating the effectiveness of LLMs in KG tasks.

In addition, \[[Zhi Zheng' 2025-05-18](http://arxiv.org/abs/2505.12348v1)\] proposes a framework for knowledge graph curation, defining quality metrics and validation strategies to improve KG quality. This work is foundational for ensuring the reliability of KGs used in claim verification. \[[Dirk Väth' 2024-10-08](http://arxiv.org/abs/2410.05821v2)\] presents a method for evaluating the alignment between KGs and LLMs, using a Thompson-sampling-inspired framework to efficiently measure alignment. This work is relevant to claim verification as it assesses the factualness of LLMs against KGs.

These related works collectively highlight the potential of integrating KGs with LLMs for claim verification and reasoning tasks, though few directly address the specific challenges of multi-step reasoning and zero-shot generalizability across unstructured datasets.

### References

1. http://arxiv.org/abs/2404.17000v1  
2. http://arxiv.org/abs/2408.06717v3  
3. http://arxiv.org/abs/2404.17000v1  
4. http://arxiv.org/abs/2408.06717v3  
5. http://arxiv.org/abs/2306.08302v3  
6. http://arxiv.org/abs/2011.01103v1  
7. http://arxiv.org/abs/2309.08491v1  
8. http://arxiv.org/abs/2308.08130v1  
9. http://arxiv.org/abs/2402.14679v2  
10. http://arxiv.org/abs/2312.11539v3
