## Related Works

Integrating knowledge graphs (KGs) with large language models (LLMs) to enhance reasoning capabilities, particularly in claim verification, has gained increasing attention. KGs provide structured, semantically rich representations that facilitate explicit reasoning, while LLMs excel at natural language understanding and generation but often struggle to leverage structured knowledge directly and to perform robust multi-step reasoning without adaptation \[[2306.08302v3](http://arxiv.org/abs/2306.08302v3)\]. This section surveys relevant literature on combining KGs and LLMs for reasoning, claim verification, and knowledge representation, highlighting advances and remaining challenges.

### Integration of KGs and LLMs for Reasoning and Verification

A prominent direction involves enhancing LLMs with external structured knowledge from KGs to improve reasoning and factual accuracy. The roadmap by Zhang et al. \[[2306.08302v3](http://arxiv.org/abs/2306.08302v3)\] categorizes integration into three frameworks: KG-enhanced LLMs that incorporate KGs during training or inference to augment knowledge, LLM-augmented KGs that use LLMs for KG tasks (e.g., completion and question answering), and synergized LLM+KG frameworks where both cooperate bidirectionally for improved reasoning. This taxonomy underscores the complementary strengths of KGs and LLMs and guides development of hybrid systems for claim verification.

In claim verification specifically, frameworks like First-Order-Logic-Guided Knowledge-Grounded (FOLK) reasoning leverage LLMs to translate complex claims into logical forms and then verify sub-claims against knowledge-grounded question-answer pairs, producing interpretable explanations without requiring annotated evidence \[[2310.05253v2](http://arxiv.org/abs/2310.05253v2)\]. Similarly, Reasoning-CV proposes a Chain-of-Thought verification paradigm, enabling LLMs to generate reasoning paths directly for claims, enhancing verification accuracy and interpretability through fine-tuning \[[2505.12348v1](http://arxiv.org/abs/2505.12348v1)\]. These approaches highlight the potential for LLMs to perform structured, multi-step reasoning when combined with knowledge-grounded inputs.

Observation-Driven Agent (ODA) frameworks extend this integration by introducing cyclic observation-action-reflection cycles over KGs, enabling iterative reasoning that effectively leverages KG structure to improve accuracy on knowledge-intensive tasks \[[2404.07677v2](http://arxiv.org/abs/2404.07677v2)\]. Likewise, FlexKBQA utilizes LLMs to convert KG query programs into natural language questions, generating synthetic datasets to train lightweight models for few-shot and zero-shot KBQA, demonstrating strong performance even with limited annotations \[[2308.12060v3](http://arxiv.org/abs/2308.12060v3)\]. These methods emphasize iterative and flexible interaction between LLMs and structured knowledge to enhance reasoning robustness.

### Challenges in Multi-Step Reasoning and Zero-Shot Generalization

Although LLMs possess strong inherent reasoning capabilities, they often struggle with multi-step modular pipelines and reasoning directly over KGs without adaptation. Recent work proposes structure-oriented autonomous reasoning agents (SARA) that explicitly model the reasoning process with refinement and external knowledge retrieval to improve zero-shot reasoning accuracy and robustness against adversarial attacks \[[2410.19000v1](http://arxiv.org/abs/2410.19000v1)\]. Similarly, Goal-Oriented Graphs (GoGs) have been introduced to represent plans and dependencies explicitly as nodes and edges, enabling coherent multi-step procedural reasoning over complex environments \[[2505.18607v2](http://arxiv.org/abs/2505.18607v2)\]. These advances suggest that structured representations aligned with KG subgraphs can guide LLM reasoning more effectively than fragmented entity-relation graphs.

Moreover, knowledge graph embeddings and contrastive learning methods contribute to richer entity and relation representations, which can facilitate better interaction between KGs and LLMs for downstream tasks including claim verification and link prediction \[[2007.08304v1](http://arxiv.org/abs/2007.08304v1)\]\[[2106.04509v2](http://arxiv.org/abs/2106.04509v2)\]\[[2004.14843v1](http://arxiv.org/abs/2004.14843v1)\]. However, hallucination and non-deterministic outputs from LLMs remain challenges for reliable KG completion and question answering, motivating methods that combine dense retrieval, grounding, and verification over KG subgraphs \[[2405.17249v2](http://arxiv.org/abs/2405.17249v2)\]\[[2406.06621v2](http://arxiv.org/abs/2406.06621v2)\].

### KG-Driven Knowledge Selection and Dialog Planning

Enhanced knowledge selection methods using document semantic graphs preserve sentence-level and concept-level relationships, improving the informativeness of knowledge-grounded dialogue systems \[[2206.07296v2](http://arxiv.org/abs/2206.07296v2)\]. Similarly, zero-shot dialog planning approaches integrate graph-based search over domain graphs to control conversation flow and avoid hallucination, demonstrating the utility of structured knowledge in sensitive domains \[[2410.05821v2](http://arxiv.org/abs/2410.05821v2)\]. These insights are relevant for claim verification systems that require precise knowledge retrieval and reasoning from KG subgraphs.

### Surveys and Broader Context

Comprehensive surveys on KG-aware zero-shot and few-shot learning summarize paradigms such as mapping-based, data augmentation, and propagation-based methods to reduce dependence on labeled data, emphasizing the importance of KGs as auxiliary information to improve model generalization \[[2112.10006v6](http://arxiv.org/abs/2112.10006v6)\]. Reviews on clinical knowledge integration into medical LLMs also highlight the use of KGs and retrieval-augmented generation to enhance factual correctness and traceability in high-stakes domains \[[2502.20988v2](http://arxiv.org/abs/2502.20988v2)\].

### Summary

Existing works collectively demonstrate that integrating KGs with LLMs improves reasoning and factual grounding crucial for claim verification. Approaches employ logical reasoning frameworks, graph-based retrieval, multi-step reasoning agents, and synthetic data generation to overcome limitations of LLMs in handling structured knowledge and compositional reasoning. However, challenges remain in developing end-to-end systems that can seamlessly combine lightweight specialized models with powerful general-purpose LLMs, maintain robustness in zero-shot settings, and generate interpretable explanations. The proposed ClaimPKG framework builds upon these insights by representing claims as pseudo-subgraphs to guide KG retrieval and LLM reasoning in a modular, scalable manner.

### References

\[[2308.12060v3](http://arxiv.org/abs/2308.12060v3)\] http://arxiv.org/abs/2308.12060v3  
\[[2404.07677v2](http://arxiv.org/abs/2404.07677v2)\] http://arxiv.org/abs/2404.07677v2  
\[[2310.05253v2](http://arxiv.org/abs/2310.05253v2)\] http://arxiv.org/abs/2310.05253v2  
\[[2406.06621v2](http://arxiv.org/abs/2406.06621v2)\] http://arxiv.org/abs/2306.08302v3  
\[[2502.20988v2](http://arxiv.org/abs/2502.20988v2)\] http://arxiv.org/abs/2502.20988v2  
\[[2007.08304v1](http://arxiv.org/abs/2007.08304v1)\] http://arxiv.org/abs/2007.08304v1  
\[[2410.19000v1](http://arxiv.org/abs/2410.19000v1)\] http://arxiv.org/abs/2410.19000v1  
\[[2112.10006v6](http://arxiv.org/abs/2112.10006v6)\] http://arxiv.org/abs/2112.10006v6  
\[[2410.05821v2](http://arxiv.org/abs/2410.05821v2)\] http://arxiv.org/abs/2410.05821v2  
\[[2306.08302v3](http://arxiv.org/abs/2306.08302v3)\] http://arxiv.org/abs/2306.08302v3  
\[[2505.18607v2](http://arxiv.org/abs/2505.18607v2)\] http://arxiv.org/abs/2505.18607v2  
\[[2505.12348v1](http://arxiv.org/abs/2505.12348v1)\] http://arxiv.org/abs/2505.12348v1  
\[[2106.04509v2](http://arxiv.org/abs/2106.04509v2)\] http://arxiv.org/abs/2106.04509v2  
\[[2405.17249v2](http://arxiv.org/abs/2405.17249v2)\] http://arxiv.org/abs/2405.17249v2  
\[[2206.07296v2](http://arxiv.org/abs/2206.07296v2)\] http://arxiv.org/abs/2206.07296v2  
\[[2004.14843v1](http://arxiv.org/abs/2004.14843v1)\] http://arxiv.org/abs/2004.14843v1