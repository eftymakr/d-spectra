## Related Works

The integration of knowledge graphs (KGs) with large language models (LLMs) to enhance reasoning and claim verification has gained considerable attention recently. KGs provide structured, semantically rich representations that complement the implicit knowledge embedded in LLMs, addressing challenges such as hallucinations, outdated knowledge, and multi-step reasoning deficiencies \[[2306.08302](http://arxiv.org/abs/2306.08302)\]\[[2505.02737](http://arxiv.org/abs/2505.02737)\]. However, many existing claim verification approaches have relied predominantly on unstructured text corpora, limiting their ability to exploit the explicit relational structure and interpretability that KGs offer \[[https://www.semanticscholar.org/paper/08cc15080d093fa776e9b3377bc96a67ea2693e4](https://www.semanticscholar.org/paper/08cc15080d093fa776e9b3377bc96a67ea2693e4)\]\[[2408.14317](http://arxiv.org/abs/2408.14317)\].

### LLMs and Knowledge Graph Integration

A foundational line of work explores frameworks that unify KGs and LLMs, benefiting from their complementary strengths. Mao et al. propose a roadmap categorizing integration into three frameworks: KG-enhanced LLMs, where KGs augment LLM pre-training or inference; LLM-augmented KGs, leveraging LLMs for KG completion and construction; and synergized LLM+KG systems that enable bidirectional reasoning between these components \[[https://www.semanticscholar.org/paper/08cc15080d093fa776e9b3377bc96a67ea2693e4](https://www.semanticscholar.org/paper/08cc15080d093fa776e9b3377bc96a67ea2693e4)\]. This comprehensive perspective underscores the potential for combining structured and unstructured knowledge to improve reasoning and fact verification.

Several methods focus on enhancing LLM reasoning by incorporating KG structure. For example, QA-GNN uses LLMs to score the relevance of KG nodes and jointly reason over a combined graph of question context and KG facts, enabling interpretable and structured reasoning on question answering tasks \[[2104.06378](http://arxiv.org/abs/2104.06378)\]. Similarly, the reasoning-on-graphs (RoG) framework generates KG-based relation paths as faithful, interpretable plans to guide LLM reasoning, effectively mitigating hallucinations by grounding inference on factual KG subgraphs \[[2310.01061](http://arxiv.org/abs/2310.01061)\]. Think-on-Graph (ToG) treats the LLM as an agent exploring KG entities and relations interactively, improving deep reasoning and knowledge traceability without requiring additional training \[[2307.07697](http://arxiv.org/abs/2307.07697)\]. These approaches highlight the value of KG structure in guiding multi-step reasoning and enhancing the fidelity of LLM outputs.

### Knowledge Graph Construction and Utilization with LLMs

LLMs have also been applied to KG construction and refinement tasks. Recent evaluations demonstrate that models like GPT-4 excel more as inference assistants than few-shot extractors in entity/relation extraction and link prediction tasks, motivating multi-agent systems like AutoKG that combine LLMs with external resources for scalable KG construction and reasoning \[[2305.13168](http://arxiv.org/abs/2305.13168)\]. Other works, such as KEPLER, integrate KG embeddings with pre-trained language models to jointly optimize factual knowledge representation and language understanding, improving link prediction and downstream NLP tasks \[[1911.06136](http://arxiv.org/abs/1911.06136)\].

To facilitate KG querying, systems like LinkQ employ LLMs to translate natural language questions into formal KG queries, enabling users to interact with complex KGs without specialized query language expertise while guarding against hallucinations by grounding answers exclusively in KG data \[[2406.06621](http://arxiv.org/abs/2406.06621)\]. In multi-document question answering, Knowledge Graph Prompting (KGP) constructs KGs over document collections and uses LLM-based graph traversal agents to gather supporting evidence, improving retrieval quality and reasoning over long text corpora \[[2308.11730](http://arxiv.org/abs/2308.11730)\].

### Claim Verification with Knowledge Graphs and LLMs

In the specific domain of claim verification, KGs have been recognized as crucial for providing structured evidence and supporting explainable reasoning. ClaimsKG, a large KG of fact-checked claims with rich metadata, exemplifies efforts to curate and harmonize structured claim data from fact-checking sources, enabling robust querying and analysis \[[https://www.semanticscholar.org/paper/08cc15080d093fa776e9b3377bc96a67ea2693e4](https://www.semanticscholar.org/paper/08cc15080d093fa776e9b3377bc96a67ea2693e4)\]. Explainable verification frameworks like FOLK leverage LLMs to translate claims into First-Order Logic clauses and perform knowledge-grounded reasoning over KG-derived question-answer pairs, generating human-readable explanations without requiring annotated evidence \[[2310.05253](http://arxiv.org/abs/2310.05253)\]. Program-Guided Fact-Checking (ProgramFC) decomposes claims into sub-tasks executed by specialized handlers, orchestrated by reasoning programs generated via LLMs, offering data-efficient, interpretable verification \[[2305.12744](http://arxiv.org/abs/2305.12744)\].

Furthermore, approaches that integrate political domain-specific KGs with LLMs demonstrate improved knowledge acquisition and aggregation for specialized fact verification tasks, emphasizing the importance of domain adaptation and multi-view KG construction \[[https://www.semanticscholar.org/paper/379e3ee9a6a92817bd0812848b409eafb9bf9550](https://www.semanticscholar.org/paper/379e3ee9a6a92817bd0812848b409eafb9bf9550)\]. KGLens proposes efficient probing of LLM factual accuracy against large KGs using graph-guided question generation and sampling, enabling scalable evaluation of LLM knowledge alignment critical for trustworthy verification \[[2312.11539](http://arxiv.org/abs/2312.11539)\].

### Challenges and Future Directions

Despite these advances, challenges remain in seamlessly integrating LLMs with KGs for claim verification. LLMs often struggle with multi-step reasoning pipelines and require mechanisms to effectively represent and retrieve relevant KG subgraphs to guide inference, as addressed by frameworks like ClaimPKG. The ability to generalize zero-shot across structured and unstructured datasets remains an ongoing research focus \[[2306.08302](http://arxiv.org/abs/2306.08302)\]\[[https://www.semanticscholar.org/paper/08cc15080d093fa776e9b3377bc96a67ea2693e4](https://www.semanticscholar.org/paper/08cc15080d093fa776e9b3377bc96a67ea2693e4)\]. Recent works also emphasize leveraging KG causal structures via random-walk reasoning to enhance LLM reasoning performance, highlighting novel avenues for incorporating KG topology into inference \[[2410.11588](http://arxiv.org/abs/2410.11588)\].

In summary, the literature shows a growing consensus on the complementary roles of KGs and LLMs in claim verification, with efforts spanning KG-enhanced LLM reasoning, LLM-aided KG construction, and synergistic frameworks for faithful, interpretable verification. These developments motivate end-to-end systems that dynamically retrieve and reason over KG subgraphs guided by LLMs, significantly advancing the state of the art in claim verification tasks \[[https://www.semanticscholar.org/paper/08cc15080d093fa776e9b3377bc96a67ea2693e4](https://www.semanticscholar.org/paper/08cc15080d093fa776e9b3377bc96a67ea2693e4)\]\[[2310.05253](http://arxiv.org/abs/2310.05253)\]\[[2307.07697](http://arxiv.org/abs/2307.07697)\].

---

### References

\[[2306.08302](http://arxiv.org/abs/2306.08302)\] http://arxiv.org/abs/2306.08302  
\[[2305.13168](http://arxiv.org/abs/2305.13168)\] http://arxiv.org/abs/2305.13168  
\[[2104.06378](http://arxiv.org/abs/2104.06378)\] http://arxiv.org/abs/2104.06378  
\[[2310.01061](http://arxiv.org/abs/2310.01061)\] http://arxiv.org/abs/2310.01061  
\[[https://www.semanticscholar.org/paper/08cc15080d093fa776e9b3377bc96a67ea2693e4](https://www.semanticscholar.org/paper/08cc15080d093fa776e9b3377bc96a67ea2693e4)\] http://arxiv.org/abs/2306.08302  
\[[2310.05253](http://arxiv.org/abs/2310.05253)\] http://arxiv.org/abs/2310.05253  
\[[1911.06136](http://arxiv.org/abs/1911.06136)\] http://arxiv.org/abs/1911.06136  
\[[2406.06621](http://arxiv.org/abs/2406.06621)\] http://arxiv.org/abs/2406.06621  
\[[2307.07697](http://arxiv.org/abs/2307.07697)\] http://arxiv.org/abs/2307.07697  
\[[2308.11730](http://arxiv.org/abs/2308.11730)\] http://arxiv.org/abs/2308.11730  
\[[2505.02737](http://arxiv.org/abs/2505.02737)\] http://arxiv.org/abs/2505.02737  
\[[https://www.semanticscholar.org/paper/379e3ee9a6a92817bd0812848b409eafb9bf9550](https://www.semanticscholar.org/paper/379e3ee9a6a92817bd0812848b409eafb9bf9550)\] https://www.semanticscholar.org/paper/379e3ee9a6a92817bd0812848b409eafb9bf9550  
\[[2305.12744](http://arxiv.org/abs/2305.12744)\] http://arxiv.org/abs/2305.12744  
\[[2312.11539](http://arxiv.org/abs/2312.11539)\] http://arxiv.org/abs/2312.11539  
\[[2410.11588](http://arxiv.org/abs/2410.11588)\] http://arxiv.org/abs/2410.11588  
\[[2408.14317](http://arxiv.org/abs/2408.14317)\] http://arxiv.org/abs/2408.14317