## Related Works

The integration of knowledge graphs (KGs) with large language models (LLMs) to enhance reasoning capabilities in claim verification has gained significant attention in recent research. While KGs offer structured, semantically rich representations suitable for reasoning, most existing verification methods rely on unstructured text corpora, limiting their ability to effectively leverage KGs \[[1' 2023-08-23](http://arxiv.org/abs/2308.12060v3)\]. This limitation is further exacerbated by the fact that modern LLMs, despite their strong reasoning abilities, struggle with multi-step modular pipelines and reasoning over KGs without adaptation \[[1' 2023-08-23](http://arxiv.org/abs/2308.12060v3)\]. 

Several works have explored the use of KGs for zero-shot and few-shot learning scenarios. For instance, FlexKBQA leverages LLMs to generate synthetic data for training lightweight models, enabling performance in zero-shot settings \[[2' 2025-05-08](http://arxiv.org/abs/2505.05583v1)\]. Similarly, KG-HTC integrates knowledge graphs with LLMs to provide structured semantic context during classification, significantly outperforming baselines in zero-shot settings \[[3' 2024-04-11](http://arxiv.org/abs/2404.07677v2)\]. These methods highlight the potential of combining KGs with LLMs to address the challenges of structured reasoning in low-resource scenarios.

In the domain of claim verification, recent approaches have focused on improving the interpretability and accuracy of LLMs by incorporating external knowledge. For example, the FOLK method utilizes first-order logic-guided reasoning to verify complex claims and generate explanations without relying on annotated evidence \[[6' 2023-10-08](http://arxiv.org/abs/2310.05253v2)\]. This approach aligns with the goals of ClaimPKG, which aims to integrate structured knowledge from KGs with LLM reasoning for improved claim verification. 

Furthermore, the integration of LLMs with KGs has been explored in various contexts, including visual interfaces for KG question-answering \[[7' 2024-06-07](http://arxiv.org/abs/2406.06621v2)\] and medical knowledge integration \[[8' 2025-02-28](http://arxiv.org/abs/2502.20988v2)\]. These studies emphasize the importance of structured knowledge in enhancing the reasoning capabilities of LLMs, particularly in domains where factual accuracy is critical. 

The use of KGs for knowledge completion and link prediction has also been extensively studied. For example, the Dual Graph Embedding (DGE) method models both first-order and high-order proximities in KGs to improve object-tag link prediction \[[12' 2020-07-16](http://arxiv.org/abs/2007.08304v1)\]. This approach demonstrates the potential of leveraging KG structures to enhance the performance of LLMs in tasks requiring structured reasoning. 

In addition to these efforts, several works have focused on improving the robustness of LLMs in the presence of noisy or adversarial inputs. For instance, the PROBLEMATHIC dataset was introduced to evaluate LLMs' ability to handle irrelevant information in math word problems, revealing their susceptibility to numerical noise \[[13' 2024-05-30](http://arxiv.org/abs/2406.15444v5)\]. This highlights the importance of robust reasoning mechanisms, which is a key component of ClaimPKG's design.

In summary, the integration of KGs with LLMs represents a promising direction for enhancing reasoning capabilities in claim verification. While existing methods have made significant strides, the proposed ClaimPKG framework offers a novel approach that seamlessly integrates LLM reasoning with structured knowledge from KGs, achieving state-of-the-art performance across multiple categories \[[1' 2023-08-23](http://arxiv.org/abs/2308.12060v3)\].

### References

1. FlexKBQA: A Flexible LLM-Powered Framework for Few-Shot Knowledge Base Question Answering [http://arxiv.org/abs/2308.12060v3]  
2. KG-HTC: Integrating Knowledge Graphs into LLMs for Effective Zero-shot Hierarchical Text Classification [http://arxiv.org/abs/2505.05583v1]  
3. Knowledge Graphs for zero-shot Hierarchical Text Classification (KG-HTC) [http://arxiv.org/abs/2505.05583v1]  
6. Explainable Claim Verification via Knowledge-Grounded Reasoning with Large Language Models [http://arxiv.org/abs/2310.05253v2]  
7. LinkQ: An LLM-Assisted Visual Interface for Knowledge Graph Question-Answering [http://arxiv.org/abs/2406.06621v2]  
8. Reviewing Clinical Knowledge in Medical Large Language Models: Training and Beyond [http://arxiv.org/abs/2502.20988v2]  
12. Dual Graph Embedding for Object-Tag Link Prediction on the Knowledge Graph [http://arxiv.org/abs/2007.08304v1]  
13. Cutting Through the Noise: Boosting LLM Performance on Math Word Problems [http://arxiv.org/abs/2406.15444v5]
