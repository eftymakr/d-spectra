## Related Works

The integration of knowledge graphs (KGs) with large language models (LLMs) to enhance reasoning and claim verification has gained significant attention recently. KGs provide structured, semantically rich representations that are well-suited for reasoning tasks, while LLMs excel at natural language understanding and generation but often struggle with multi-step reasoning and grounding in factual knowledge \[[2306.08302](http://arxiv.org/abs/2306.08302)\]. This section reviews prior work addressing the combination of KGs and LLMs, focusing on knowledge-enhanced language representations, KG-based reasoning frameworks, and retrieval-augmented generation approaches relevant to claim verification.

### Knowledge-Enhanced Language Models

Early attempts to incorporate structured knowledge into language models include KEPLER \[[1911.06136](http://arxiv.org/abs/1911.06136)\] and ERNIE \[[1905.07129](http://arxiv.org/abs/1905.07129)\], which embed KG facts alongside textual data to improve factual knowledge capture. KEPLER jointly optimizes knowledge embedding and language modeling to produce text-enhanced entity representations, demonstrating strong performance on various NLP and KG link prediction tasks \[[1911.06136](http://arxiv.org/abs/1911.06136)\]. Similarly, ERNIE enhances language representations with informative entities from KGs, improving knowledge-driven tasks by integrating lexical, syntactic, and structured knowledge \[[1905.07129](http://arxiv.org/abs/1905.07129)\]. CoLAKE extends this idea by jointly contextualizing language and knowledge embeddings within a unified word-knowledge graph structure, outperforming prior models on knowledge probing and language understanding benchmarks \[[2010.00309](http://arxiv.org/abs/2010.00309)\]. These models establish a foundation for enriching LLMs with explicit KG knowledge, although they primarily focus on pre-training rather than downstream claim verification.

K-BERT specifically addresses the challenge of injecting domain knowledge from KGs into language representations while mitigating knowledge noise through soft-position and visibility controls, yielding improvements in domain-specific reasoning tasks such as medicine and law \[[1909.07606](http://arxiv.org/abs/1909.07606)\]. These approaches highlight the necessity of carefully integrating KG information to avoid semantic distortion and optimize reasoning capacity.

### LLM Reasoning over Knowledge Graphs

Recent work emphasizes enabling LLMs to perform faithful and interpretable reasoning grounded on KG structure. The RoG framework proposes a planning-retrieval-reasoning pipeline that generates KG-based relation paths as reasoning plans, retrieves valid subgraphs, and guides LLMs to conduct stepwise, faithful reasoning, improving interpretability and accuracy on KG question answering tasks \[[2310.01061](http://arxiv.org/abs/2310.01061)\]. Similarly, StructGPT develops an iterative reading-then-reasoning approach over structured data, employing external interfaces to extract relevant evidence and perform reasoning in a zero-shot setting, significantly boosting LLM performance on structured QA \[[2305.09645](http://arxiv.org/abs/2305.09645)\]. These methods illustrate approaches to modularize and scaffold LLM reasoning with explicit structured knowledge, addressing the limitations of LLMs performing multi-hop reasoning natively.

QA-GNN integrates language models with graph neural networks to jointly reason over QA contexts and KGs by message passing, improving interpretability and handling complex logical structures such as negation \[[2104.06378](http://arxiv.org/abs/2104.06378)\]. Knowledge Solver (KSL) trains LLMs to autonomously search external KGs via multi-hop retrieval prompts, enhancing domain-specific knowledge access and reducing hallucination during inference \[[2309.03118](http://arxiv.org/abs/2309.03118)\]. These approaches align with the ClaimPKG design philosophy of employing lightweight specialized LLM modules for subgraph retrieval and general LLMs for final verdict generation.

### Retrieval-Augmented Generation and KG Prompting

Retrieval-Augmented Generation (RAG) paradigms combine parametric LLM knowledge with non-parametric external databases to mitigate hallucination and update knowledge dynamically, showing strong results on knowledge-intensive tasks including open-domain QA \[[2312.10997](http://arxiv.org/abs/2312.10997)\]\[[2005.11401](http://arxiv.org/abs/2005.11401)\]. RAG models retrieve relevant passages and integrate them into generation, improving factuality and specificity. Extending this idea, Knowledge Graph Prompting (KGP) constructs graphs over multi-document inputs, using LLM-based traversal agents to navigate and retrieve relevant passages, thereby enhancing multi-document QA with graph-structured retrieval \[[2308.11730](http://arxiv.org/abs/2308.11730)\]. MindMap further proposes knowledge graph prompting to elicit LLM reasoning pathways as mind maps, combining implicit and explicit knowledge for transparent inference, particularly in medical domains \[[2308.09729](http://arxiv.org/abs/2308.09729)\]. These methods demonstrate the synergy between KGs and LLMs for retrieval and reasoning, crucial for claim verification systems requiring explainability.

### Unified Frameworks and Roadmaps

A comprehensive survey on unifying LLMs and KGs delineates three general frameworks: KG-enhanced LLMs that incorporate KGs during pre-training or inference, LLM-augmented KGs that leverage LLMs for KG construction and completion, and synergized LLM+KG systems that enable bidirectional reasoning between data and knowledge \[[2306.08302](http://arxiv.org/abs/2306.08302)\]. This roadmap highlights the complementary strengths of LLMs and KGs, advocating integrated systems like ClaimPKG that combine specialized subgraph retrieval with general LLM reasoning to achieve strong accuracy and zero-shot generalizability.

### Challenges and Advances in Claim Verification

Fact-checking complex claims involves multi-step reasoning and evidence aggregation, which is addressed by Program-Guided Fact-Checking (ProgramFC), decomposing claims into sub-tasks solved by specialized functions and LLM-generated reasoning programs for explainability \[[2305.12744](http://arxiv.org/abs/2305.12744)\]. This aligns with the modular pipeline approach in ClaimPKG. Additionally, hallucination remains a key challenge in NLG and LLM-based tasks, motivating retrieval and knowledge grounding techniques to improve factuality and trustworthiness \[[2202.03629](http://arxiv.org/abs/2202.03629)\].

### Summary

Collectively, these works establish a rich foundation for integrating KGs with LLMs to enhance reasoning, interpretability, and factual accuracy in claim verification. Approaches range from knowledge-enhanced pre-training and embedding (KEPLER, ERNIE, CoLAKE), to modular reasoning frameworks (RoG, StructGPT, QA-GNN, KSL), retrieval-augmented generation (RAG, KGP, MindMap), and systematic roadmaps for unification (Unifying LLMs and KGs). ClaimPKG advances this state of the art by combining lightweight LLM-driven subgraph retrieval with general LLM verdict generation, achieving superior performance and zero-shot generalization across datasets, addressing key challenges identified in prior research.

### References

\[[1911.06136](http://arxiv.org/abs/1911.06136)\] http://arxiv.org/abs/1911.06136  
\[[2308.09729](http://arxiv.org/abs/2308.09729)\] http://arxiv.org/abs/2308.09729  
\[[1909.07606](http://arxiv.org/abs/1909.07606)\] http://arxiv.org/abs/1909.07606  
\[[2305.12744](http://arxiv.org/abs/2305.12744)\] http://arxiv.org/abs/2305.12744  
\[[2312.10997](http://arxiv.org/abs/2312.10997)\] http://arxiv.org/abs/2312.10997  
\[[2305.09645](http://arxiv.org/abs/2305.09645)\] http://arxiv.org/abs/2305.09645  
\[[2310.01061](http://arxiv.org/abs/2310.01061)\] http://arxiv.org/abs/2310.01061  
\[[2308.11730](http://arxiv.org/abs/2308.11730)\] http://arxiv.org/abs/2308.11730  
\[[1905.07129](http://arxiv.org/abs/1905.07129)\] http://arxiv.org/abs/1905.07129  
\[[2306.08302](http://arxiv.org/abs/2306.08302)\] http://arxiv.org/abs/2306.08302  
\[[2010.00309](http://arxiv.org/abs/2010.00309)\] http://arxiv.org/abs/2010.00309  
\[[2005.11401](http://arxiv.org/abs/2005.11401)\] http://arxiv.org/abs/2005.11401  
\[[2202.03629](http://arxiv.org/abs/2202.03629)\] http://arxiv.org/abs/2202.03629  
\[[2104.06378](http://arxiv.org/abs/2104.06378)\] http://arxiv.org/abs/2104.06378  
\[[2309.03118](http://arxiv.org/abs/2309.03118)\] http://arxiv.org/abs/2309.03118