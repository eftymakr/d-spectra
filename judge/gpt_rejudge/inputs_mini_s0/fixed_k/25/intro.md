## Related Works

The integration of knowledge graphs (KGs) with large language models (LLMs) to enhance claim verification is a rapidly evolving research area that addresses the limitations of relying solely on unstructured text for reasoning. KGs provide a structured and semantically rich representation of knowledge, which is crucial for complex reasoning tasks, but traditional claim verification methods often depend on textual evidence, limiting their effectiveness in leveraging KGs \[[2406.06621](http://arxiv.org/abs/2406.06621)\]. Meanwhile, LLMs, despite their strong reasoning capabilities, face challenges in multi-step modular reasoning and direct utilization of KG structures without specific adaptations \[[2310.05253](http://arxiv.org/abs/2310.05253)\].

Several frameworks have explored the synergy between LLMs and KGs to improve reasoning and verification. A comprehensive roadmap identifies three main paradigms: KG-enhanced LLMs that incorporate external knowledge during pre-training or inference; LLM-augmented KGs where LLMs assist in KG completion, construction, and question answering; and synergized approaches where LLMs and KGs mutually enhance each other for bidirectional reasoning \[[2306.08302](http://arxiv.org/abs/2306.08302)\]. This taxonomy situates current efforts and guides the integration of structured knowledge and LLM reasoning.

In claim verification specifically, recent methods have moved beyond traditional text retrieval to incorporate structured knowledge. The FOLK framework translates claims into first-order logic clauses and performs knowledge-grounded reasoning over question-answer pairs derived from KGs, enabling explainable veracity predictions without requiring annotated evidence \[[2310.05253](http://arxiv.org/abs/2310.05253)\]. Similarly, CRAVE leverages LLM-generated conflicting rationales coupled with refined evidence retrieval from Wikipedia and a specialized judgment module to enhance both accuracy and interpretability in claim verification \[[2504.14905](http://arxiv.org/abs/2504.14905)\]. These approaches demonstrate the benefits of combining KG-based evidence with LLM reasoning for nuanced verification tasks.

Another line of work focuses on improving KG quality and reliability, which is critical for downstream verification. Validators compute confidence scores for KG triples by cross-referencing weighted external sources, achieving validated KG subsets suitable for trustworthy applications \[[2104.12622](http://arxiv.org/abs/2104.12622)\]\[[2208.0813](http://arxiv.org/abs/2208.08130)\]. Efficient probing of LLM factual accuracy against KGs has also been proposed, with methods like KGLens employing graph-guided question generation and sampling to measure KG-LLM alignment with near-human accuracy \[[2312.11539](http://arxiv.org/abs/2312.11539)\]. Such validation frameworks ensure the knowledge bases that support claim verification are reliable.

In addition to claim verification, knowledge-enhanced LLMs have been applied to related tasks such as hierarchical text classification \[[2505.05583](http://arxiv.org/abs/2505.05583)\], question answering over KGs with few-shot learning \[[2308.1206](http://arxiv.org/abs/2308.12060)\], and KG construction from domain-specific data sources \[[2408.13521](http://arxiv.org/abs/2408.13521)\]\[[2206.10318](http://arxiv.org/abs/2206.10318)\]. Techniques like message passing on hierarchical relational graphs have been developed to dynamically integrate KG context into language model representations, improving comprehension and reasoning in machine reading \[[2109.04223](http://arxiv.org/abs/2109.04223)\]. Moreover, hybrid frameworks like LangGSL jointly refine node features via LLMs and graph structure learning models to produce robust graph embeddings, highlighting the complementary strengths of LLMs and graph-based models in representation learning \[[2410.12096](http://arxiv.org/abs/2410.12096)\].

Recent advances in claim verification have also explored alternative reasoning paradigms within LLMs. The Chain-of-Thought (CoT)-Verify approach fine-tunes LLMs to generate verification reasoning paths without decomposing claims into sub-claims, reducing error propagation and improving verification accuracy beyond traditional Decompose-Then-Verify methods \[[2505.12348](http://arxiv.org/abs/2505.12348)\]. This aligns with findings that causal and structured reasoning, supported by KG-based prompts or random-walk strategies, can significantly enhance LLM performance on commonsense and knowledge-intensive tasks \[[2410.11588](http://arxiv.org/abs/2410.11588)\].

While many LLM-based claim verification systems still depend on annotated corpora or text retrieval, integrating KGs offers a promising direction to improve explainability, accuracy, and zero-shot generalizability. Frameworks like LinkQ facilitate KG query construction via LLMs, helping users refine questions and explore KGs directly for trustworthy answers \[[2406.06621](http://arxiv.org/abs/2406.06621)\]. Similarly, FlexKBQA leverages LLMs to translate KG programs into natural language questions and uses iterative self-training to adapt to real user queries, achieving strong few-shot and zero-shot KBQA performance \[[2308.1206](http://arxiv.org/abs/2308.12060)\].

Overall, these works underscore the importance of tightly coupling LLM reasoning with structured KG knowledge to overcome challenges of claim verification, including multi-step reasoning, evidence retrieval, and generalizability across datasets. Nevertheless, few systems explicitly integrate lightweight LLM-driven subgraph retrieval with general-purpose LLM verification, as proposed by ClaimPKG, highlighting a key area for further research and development.

### References

1. http://arxiv.org/abs/2406.06621  
2. http://arxiv.org/abs/2310.05253  
3. http://arxiv.org/abs/2504.14905  
4. http://arxiv.org/abs/2109.04223  
5. http://arxiv.org/abs/2410.12096  
6. http://arxiv.org/abs/2505.05583  
7. http://arxiv.org/abs/2308.12060  
8. http://arxiv.org/abs/2104.12622  
9. http://arxiv.org/abs/2312.11539  
10. http://arxiv.org/abs/2505.12348  
11. http://arxiv.org/abs/2306.08302  
13. http://arxiv.org/abs/2410.11588  
14. http://arxiv.org/abs/2408.13521  
16. http://arxiv.org/abs/2208.08130  
21. http://arxiv.org/abs/2206.10318