## Related Works

Fact verification has seen significant advancements with the integration of structured knowledge sources such as knowledge graphs (KGs). Early efforts focused on unstructured text corpora, limiting the ability to leverage the rich semantic relationships provided by KGs \[[3](http://arxiv.org/abs/2011.03088)\]. For instance, FEVER introduces a large-scale dataset for fact verification, emphasizing the importance of evidence retrieval and classification \[[1](http://arxiv.org/abs/1803.05355)\]. However, these methods often lack the structured reasoning capabilities that KGs provide \[[3](http://arxiv.org/abs/2011.03088)\]. 

Recent works have explored the use of KGs for fact verification, but most rely on simplistic reasoning strategies. FactKG is a notable dataset that includes various reasoning types, such as one-hop and multi-hop reasoning, and provides a structured framework for evaluating KG-based fact verification \[[8](http://arxiv.org/abs/2305.06590)\]. Despite this, existing methods often fail to effectively integrate KGs with large language models (LLMs), which are known for their strong reasoning abilities \[[3](http://arxiv.org/abs/2011.03088)\]. 

To address these limitations, several approaches have been proposed. VitaminC introduces a benchmark that challenges models to discern subtle factual changes and adapt to evolving evidence \[[2](http://arxiv.org/abs/2103.08541)\]. This dataset emphasizes contrastive evidence pairs, which are critical for robust fact verification. Similarly, HoVer presents a dataset requiring many-hop reasoning across multiple Wikipedia articles, highlighting the complexity of long-range dependencies \[[3](http://arxiv.org/abs/2011.03088)\]. 

The integration of LLMs with KGs has also been explored. RoG proposes a novel method that synergizes LLMs with KGs to enable faithful and interpretable reasoning by leveraging the structural information of KGs \[[9](http://arxiv.org/abs/2310.01061)\]. This approach uses a planning-retrieval-reasoning framework to generate relation paths grounded in KGs, which are then used to retrieve valid reasoning paths for LLMs. 

Additionally, ProgramFC introduces a novel fact-checking model that decomposes complex claims into sub-tasks, using a shared library of specialized functions to guide the verification process \[[6](http://arxiv.org/abs/2305.12744)\]. This model leverages the in-context learning ability of LLMs to generate reasoning programs, making the process both explanatory and data-efficient. 

Another approach, FOLK, uses First-Order-Logic (FOL) to guide knowledge-grounded reasoning, translating claims into FOL clauses and performing reasoning over a set of question-and-answer pairs \[[7](http://arxiv.org/abs/2310.05253)\]. This method provides comprehensive explanations without relying on human-annotated data, enhancing the transparency of the verification process. 

In summary, while existing works have made strides in fact verification, the integration of KGs with LLMs remains a critical challenge. The proposed ClaimPKG framework addresses these challenges by seamlessly integrating LLM reasoning with structured knowledge from KGs, achieving state-of-the-art performance on benchmark datasets \[[3](http://arxiv.org/abs/2011.03088)\].

References:
1. \[[1](http://arxiv.org/abs/1803.05355)\] FEVER: a large-scale dataset for Fact Extraction and VERification [http://arxiv.org/abs/1803.05355]
2. \[[2](http://arxiv.org/abs/2103.08541)\] Get Your Vitamin C! Robust Fact Verification with Contrastive Evidence [http://arxiv.org/abs/2103.08541]
3. \[[3](http://arxiv.org/abs/2011.03088)\] FactKG: Fact Verification via Reasoning on Knowledge Graphs [http://arxiv.org/abs/2305.06590]
4. \[[4](http://arxiv.org/abs/1812.08434)\] Graph Neural Networks: A Review of Methods and Applications [http://arxiv.org/abs/1812.08434]
5. \[[5](http://arxiv.org/abs/2004.02349)\] TAPAS: Weakly Supervised Table Parsing via Pre-training [http://arxiv.org/abs/2004.02349]
6. \[[6](http://arxiv.org/abs/2305.12744)\] Fact-Checking Complex Claims with Program-Guided Reasoning [http://arxiv.org/abs/2305.12744]
7. \[[7](http://arxiv.org/abs/2310.05253)\] Explainable Claim Verification via Knowledge-Grounded Reasoning with Large Language Models [http://arxiv.org/abs/2310.05253]
8. \[[8](http://arxiv.org/abs/2305.06590)\] HoVer: A Dataset for Many-Hop Fact Extraction And Claim Verification [http://arxiv.org/abs/2011.03088]
9. \[[9](http://arxiv.org/abs/2310.01061)\] Reasoning on Graphs: Faithful and Interpretable Large Language Model Reasoning [http://arxiv.org/abs/2310.01061]
