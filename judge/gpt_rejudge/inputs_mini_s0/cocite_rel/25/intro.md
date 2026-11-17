## Related Works

Integrating knowledge graphs (KGs) with large language models (LLMs) to enhance reasoning and claim verification has gained considerable attention due to complementary strengths: KGs offer structured, semantically rich representations ideal for explicit reasoning, while LLMs provide powerful generalization and natural language understanding capabilities. However, most existing claim verification methods predominantly rely on unstructured text corpora, limiting their ability to fully exploit the structured knowledge in KGs \[[2305.12744](http://arxiv.org/abs/2305.12744)\]. Moreover, although modern LLMs exhibit strong reasoning abilities, they face challenges when performing multi-step, modular reasoning pipelines and reasoning directly over KG structures without specialized adaptation \[[2310.01061](http://arxiv.org/abs/2310.01061)\]\[[2305.13168](http://arxiv.org/abs/2305.13168)\].

### KG-Enhanced LLMs and LLM-Augmented KGs

A broad taxonomy categorizes integration approaches into three frameworks: (1) KG-enhanced LLMs that incorporate KG information during model pre-training or inference to improve knowledge grounding and interpretability; (2) LLM-augmented KGs that leverage LLMs for KG construction, completion, and question answering; and (3) synergized LLM+KG systems where both components contribute interactively to reasoning tasks \[[2305.12744](http://arxiv.org/abs/2305.12744)\]. Early models such as KEPLER and JAKET jointly optimize language and knowledge embedding objectives to tightly integrate textual and structured KG information, improving performance on various knowledge-driven NLP tasks \[[1911.06136](http://arxiv.org/abs/1911.06136)\]\[[2010.00796](http://arxiv.org/abs/2010.00796)\]. K-BERT and ERNIE inject KG triples or entities directly into the input sentences or embeddings to enrich language representations, addressing domain-specific knowledge gaps but often requiring careful handling of knowledge noise \[[1905.07129](http://arxiv.org/abs/1905.07129)\]\[[1909.07606](http://arxiv.org/abs/1909.07606)\].

### Reasoning and Question Answering over KGs with LLMs

Recent works address the challenge of faithful and interpretable reasoning over KGs by LLMs. The RoG framework, for example, synergizes LLMs with KGs via a planning-retrieval-reasoning pipeline that generates KG-grounded relation paths to guide reasoning, reducing hallucinations and improving interpretability \[[2310.01061](http://arxiv.org/abs/2310.01061)\]. QA-GNN and KagNet employ graph neural networks to jointly reason on QA contexts and KG subgraphs, enabling structured, transparent reasoning in commonsense and open-domain QA settings \[[2104.06378](http://arxiv.org/abs/2104.06378)\]\[[1909.02151](http://arxiv.org/abs/1909.02151)\]. Similarly, knowledge graph prompting has been proposed to enhance multi-document question answering by constructing KG representations of document structure and content, enabling effective graph traversal and retrieval for LLMs \[[2308.1173](http://arxiv.org/abs/2308.11730)\].

### Retrieval-Augmented and Prompting Methods

Retrieval-augmented generation (RAG) methods combine parametric LLM knowledge with non-parametric external sources such as Wikipedia to improve factuality and specificity in generation, demonstrating state-of-the-art results on knowledge-intensive tasks \[[2005.11401](http://arxiv.org/abs/2005.11401)\]. However, these methods often focus on text corpora rather than structured KG data. To bridge this gap, prompting techniques that incorporate KG information as structured prompts or “graphs of thoughts” have been developed to enhance LLM inference and transparency, particularly in complex domains like medicine. The MindMap approach explicitly elicits reasoning pathways informed by knowledge ontologies, reducing hallucinations and improving combined inference from implicit LLM knowledge and external KGs \[[2308.09729](http://arxiv.org/abs/2308.09729)\].

### LLMs in Knowledge Graph Construction and Quality Assurance

LLMs also play an increasing role in KG construction, completion, and validation. Empirical studies show that models like GPT-4 excel more as inference assistants than few-shot extractors for KG tasks, inspiring multi-agent frameworks such as AutoKG for automated KG construction and reasoning \[[2305.13168](http://arxiv.org/abs/2305.13168)\]. Quality metrics and validation frameworks have been proposed to curate and maintain KG quality, which is crucial for downstream applications like claim verification \[[2011.00235](http://arxiv.org/abs/2011.00235)\]. Additionally, frameworks for fact-checking using program-guided multi-step reasoning leverage LLMs to decompose complex claims into sub-tasks, enhancing explanation and data efficiency \[[2305.12744](http://arxiv.org/abs/2305.12744)\].

### Challenges and Future Directions

Despite progress, challenges remain in effectively combining KGs and LLMs for claim verification. LLMs struggle with less popular or long-tail factual knowledge, where retrieval augmentation from explicit KG sources proves beneficial \[[2212.10511](http://arxiv.org/abs/2212.10511)\]. Larger LLMs tend to generate more factual outputs, but standard sampling algorithms may introduce factual errors, motivating enhanced training and sampling methods to improve factuality \[[2206.04624](http://arxiv.org/abs/2206.04624)\]. Furthermore, domain-specific KGs face construction and evolution challenges, limiting their immediate applicability across diverse claim verification scenarios \[[2011.00235](http://arxiv.org/abs/2011.00235)\]. Unifying the structural reasoning capabilities of KGs with the flexible inference of LLMs, while ensuring scalability and interpretability, remains an active research frontier \[[2305.12744](http://arxiv.org/abs/2305.12744)\]\[[2310.01061](http://arxiv.org/abs/2310.01061)\].

In summary, the integration of KGs and LLMs for claim verification leverages complementary strengths but requires careful system design to address multi-step modular reasoning, factual grounding, and knowledge retrieval challenges. ClaimPKG’s approach of representing claims as pseudo-subgraphs to guide KG retrieval and subsequent LLM reasoning aligns with emerging trends that emphasize structured prompt representations and modular pipelines for robust, interpretable verification.

### References

\[[2308.09729](http://arxiv.org/abs/2308.09729)\] http://arxiv.org/abs/2308.09729  
\[[2308.1173](http://arxiv.org/abs/2308.11730)\] http://arxiv.org/abs/2308.11730  
\[[2005.11401](http://arxiv.org/abs/2005.11401)\] http://arxiv.org/abs/2005.11401  
\[[2305.12744](http://arxiv.org/abs/2305.12744)\] http://arxiv.org/abs/2306.08302  
\[[1911.06136](http://arxiv.org/abs/1911.06136)\] http://arxiv.org/abs/1911.06136  
\[[2010.00796](http://arxiv.org/abs/2010.00796)\] http://arxiv.org/abs/2010.00796  
\[[2011.00235](http://arxiv.org/abs/2011.00235)\] http://arxiv.org/abs/2402.14679  
\[[2305.13168](http://arxiv.org/abs/2305.13168)\] http://arxiv.org/abs/2305.13168  
\[[2310.01061](http://arxiv.org/abs/2310.01061)\] http://arxiv.org/abs/2310.01061  
\[[2104.06378](http://arxiv.org/abs/2104.06378)\] http://arxiv.org/abs/2104.06378  
\[[1909.02151](http://arxiv.org/abs/1909.02151)\] http://arxiv.org/abs/1909.02151  
\[[1905.07129](http://arxiv.org/abs/1905.07129)\] http://arxiv.org/abs/1905.07129  
\[[1909.07606](http://arxiv.org/abs/1909.07606)\] http://arxiv.org/abs/1909.07606  
\[[2212.10511](http://arxiv.org/abs/2212.10511)\] http://arxiv.org/abs/2212.10511  
\[[2206.04624](http://arxiv.org/abs/2206.04624)\] http://arxiv.org/abs/2206.04624