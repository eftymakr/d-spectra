## Related Works

The integration of knowledge graphs (KGs) with large language models (LLMs) to enhance reasoning, particularly for claim verification, is a rapidly evolving research area. KGs provide structured, semantically rich representations that are well-suited for complex reasoning tasks, whereas LLMs excel at natural language understanding and generation but often struggle with factual accuracy and multi-step reasoning over structured knowledge \[[2306.08302](http://arxiv.org/abs/2306.08302)\]\[[2302.12813](http://arxiv.org/abs/2302.12813)\]. This section reviews relevant works on combining KGs and LLMs, addressing challenges in knowledge representation, reasoning, retrieval, and claim verification.

### Knowledge Graphs and LLM Integration

LLMs are powerful generalists capable of few-shot and zero-shot reasoning, with methods like chain-of-thought prompting enhancing their multi-step reasoning abilities without fine-tuning \[[2205.11916](http://arxiv.org/abs/2205.11916)\]\[[2201.11903](http://arxiv.org/abs/2201.11903)\]. However, LLMs' parametric memory alone is insufficient for reliably encoding and retrieving detailed factual knowledge, especially for less popular or long-tail entities, which hampers their performance on knowledge-intensive tasks \[[2212.10511](http://arxiv.org/abs/2212.10511)\]. To mitigate these limitations, retrieval-augmented generation (RAG) frameworks have been proposed, combining LLMs with external non-parametric memory such as KGs or text corpora. RAG models improve factuality, specificity, and adaptability of generated outputs by conditioning on retrieved relevant knowledge \[[2005.11401](http://arxiv.org/abs/2005.11401)\]\[[2312.10997](http://arxiv.org/abs/2312.10997)\].

Several approaches incorporate KGs directly to enhance LLM reasoning. KG-enhanced LLMs integrate structured knowledge during training or inference, improving understanding and interpretability. Conversely, LLM-augmented KGs leverage LLMs for KG construction, completion, and question answering, facilitating dynamic and scalable knowledge management. Synergistic frameworks treat LLMs and KGs as complementary, enabling bidirectional reasoning and mutual enhancement \[[2302.12813](http://arxiv.org/abs/2302.12813)\]. Models like KEPLER unify knowledge embedding and language representation to jointly optimize KG facts and textual knowledge, improving downstream NLP tasks and KG completion \[[1911.06136](http://arxiv.org/abs/1911.06136)\]. ERNIE also exploits KGs to enhance language representations by injecting informative entities from structured data \[[1905.07129](http://arxiv.org/abs/1905.07129)\].

### Reasoning and Question Answering with KGs and LLMs

Graph-based neural methods such as QA-GNN and KagNet demonstrate effective joint reasoning over textual inputs and KGs by constructing schema graphs or joint graphs that combine question-answer contexts and KG nodes. They use graph neural networks to perform interpretable, multi-step reasoning, improving performance on commonsense and open-domain QA tasks \[[2104.06378](http://arxiv.org/abs/2104.06378)\]\[[1909.02151](http://arxiv.org/abs/1909.02151)\]. Knowledge graph prompting techniques, such as Knowledge Graph Prompting (KGP) and MindMap, utilize graph construction and traversal to guide LLMs in multi-document QA or domain-specific inference, reducing hallucinations and enhancing transparency \[[2308.1173](http://arxiv.org/abs/2308.11730)\]\[[2308.09729](http://arxiv.org/abs/2308.09729)\]. These methods highlight the benefits of explicitly modeling semantic relations and leveraging KG structure to improve LLM reasoning quality.

### Claim Verification and Fact-Checking

Fact-checking complex claims requires aggregating and reasoning over multiple evidence pieces, which can be facilitated by KGs providing structured, trustworthy knowledge \[[2305.12744](http://arxiv.org/abs/2305.12744)\]\[[2310.05253](http://arxiv.org/abs/2310.05253)\]. Program-guided reasoning frameworks decompose verification into sub-tasks executed via specialized modules, guided by LLM-generated reasoning programs, yielding interpretable and data-efficient fact-checking \[[2305.12744](http://arxiv.org/abs/2305.12744)\]. FOLK employs first-order logic clauses derived from claims to guide knowledge-grounded reasoning without relying on annotated evidence, producing explainable justifications \[[2310.05253](http://arxiv.org/abs/2310.05253)\].

Most claim verification systems rely heavily on unstructured text corpora, limiting their ability to fully exploit the structured semantics of KGs \[[2302.12813](http://arxiv.org/abs/2302.12813)\]. Recent works propose frameworks where LLMs generate subgraph representations or pseudo-subgraphs of claims, which guide retrieval of pertinent KG subgraphs for downstream verification and explanation generation. This modular approach tackles multi-step reasoning challenges and improves zero-shot generalizability to unstructured datasets by combining structured knowledge retrieval with LLM reasoning \[[2306.08302](http://arxiv.org/abs/2306.08302)\]\[[2302.12813](http://arxiv.org/abs/2302.12813)\].

### Challenges and Future Directions

Despite progress, challenges remain in scaling KG construction and maintenance, integrating KG reasoning seamlessly with LLM inference, and reducing hallucinations while maintaining fluency and informativeness \[[2202.03629](http://arxiv.org/abs/2202.03629)\]\[[2302.04023](http://arxiv.org/abs/2302.04023)\]. Advances in retrieval-augmented generation and graph-based reasoning offer promising paths to address these issues by combining parametric and non-parametric knowledge sources \[[2005.11401](http://arxiv.org/abs/2005.11401)\]\[[2312.10997](http://arxiv.org/abs/2312.10997)\]\[[2212.10511](http://arxiv.org/abs/2212.10511)\]. Further research is needed on effective prompt designs, retrieval strategies, and synergistic models that enable LLMs to fully leverage KGs for claim verification and other knowledge-intensive tasks.

Collectively, these works underscore the growing consensus that unifying LLMs and KGs can significantly enhance reasoning capabilities, factual accuracy, and explainability in claim verification systems, motivating the development of integrated frameworks such as ClaimPKG.

### References

\[[2306.08302](http://arxiv.org/abs/2306.08302)\] http://arxiv.org/abs/2306.08302  
\[[2104.06378](http://arxiv.org/abs/2104.06378)\] http://arxiv.org/abs/2104.06378  
\[[2308.1173](http://arxiv.org/abs/2308.11730)\] http://arxiv.org/abs/2308.11730  
\[[2005.11401](http://arxiv.org/abs/2005.11401)\] http://arxiv.org/abs/2005.11401  
\[[2302.12813](http://arxiv.org/abs/2302.12813)\] http://arxiv.org/abs/2306.08302  
\[[2205.11916](http://arxiv.org/abs/2205.11916)\] http://arxiv.org/abs/2205.11916  
\[[2202.03629](http://arxiv.org/abs/2202.03629)\] http://arxiv.org/abs/2202.03629  
\[[2305.12744](http://arxiv.org/abs/2305.12744)\] http://arxiv.org/abs/2305.12744  
\[[1911.06136](http://arxiv.org/abs/1911.06136)\] http://arxiv.org/abs/1911.06136  
\[[1905.07129](http://arxiv.org/abs/1905.07129)\] http://arxiv.org/abs/1905.07129  
\[[2308.09729](http://arxiv.org/abs/2308.09729)\] http://arxiv.org/abs/2308.09729  
\[[1909.02151](http://arxiv.org/abs/1909.02151)\] http://arxiv.org/abs/1909.02151  
\[[2312.10997](http://arxiv.org/abs/2312.10997)\] http://arxiv.org/abs/2312.10997  
\[[2212.10511](http://arxiv.org/abs/2212.10511)\] http://arxiv.org/abs/2212.10511  
\[[2201.11903](http://arxiv.org/abs/2201.11903)\] http://arxiv.org/abs/2201.11903  
\[[2302.04023](http://arxiv.org/abs/2302.04023)\] http://arxiv.org/abs/2302.04023  
\[[2310.05253](http://arxiv.org/abs/2310.05253)\] http://arxiv.org/abs/2310.05253