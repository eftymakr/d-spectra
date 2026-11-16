## Related Works

Understanding the evolution of feature representations across layers in large language models (LLMs) is crucial for improving interpretability and robustness \[[10](http://arxiv.org/abs/2412.09563)\]. Recent studies have explored how representations change with training and across layers, but many rely on data-dependent analyses of fine-tuned models, limiting their applicability to post-hoc settings \[[10](http://arxiv.org/abs/2412.09563)\]. In contrast, our approach is data-oblivious, analyzing representation dynamics in pre-fine-tuned models using Centered Kernel Alignment (CKA) \[[10](http://arxiv.org/abs/2412.09563)\]. This method has been used to compare representations in neural networks, showing that CKA can reliably identify correspondences between representations in networks trained from different initializations \[[3](http://arxiv.org/abs/1905.00414)\]. CKA is closely connected to canonical correlation analysis (CCA), which has been used to compare representations in CNNs and RNNs \[[1](http://arxiv.org/abs/1806.05759)\]. 

Several studies have investigated how representations evolve during training and how they differ across network architectures. For example, SVCCA, a method for comparing representations in deep learning models, has been used to measure intrinsic dimensionality and probe learning dynamics \[[2](http://arxiv.org/abs/1706.05806)\]. SVCCA is invariant to affine transforms, allowing for comparisons between different layers and networks \[[2](http://arxiv.org/abs/1706.05806)\]. Similarly, CKA has been used to analyze the similarity of representations in fine-tuned Transformers, revealing a consistent block diagonal structure in the similarity of representations within fine-tuned RoBERTa and ALBERT models \[[4](http://arxiv.org/abs/2109.08406)\]. This suggests that representations in earlier and later layers are more similar within clusters than between them \[[4](http://arxiv.org/abs/2109.08406)\].

The role of different layers in model behavior has also been explored. For instance, research has shown that wider networks converge to more similar solutions than narrow networks \[[1](http://arxiv.org/abs/1806.05759)\]. Additionally, studies have found that the hidden state in RNNs is highly variable over the course of a sequence, even when accounting for linear transforms \[[1](http://arxiv.org/abs/1806.05759)\]. These findings highlight the importance of understanding how representations change across layers and how this relates to model performance.

Our work builds on these insights, showing that layers with significant shifts in representation space are also those most affected during fine-tuning \[[10](http://arxiv.org/abs/2412.09563)\]. This pattern holds consistently across tasks for a given model, suggesting that certain layers are more critical for model behavior \[[10](http://arxiv.org/abs/2412.09563)\]. Spectral analysis further reveals that these shifts are driven by changes in the top principal components, which encode semantic transitions from rationales to conclusions \[[10](http://arxiv.org/abs/2412.09563)\]. These findings have practical implications, as they can be applied to efficient domain adaptation and backdoor defense, where fine-tuning or freezing critical layers leads to greater loss reduction or reduced attack success rates, respectively [1
## Research papers
### Outline
- [Canonical Correlation Analysis (CCA) in Neural Networks [2 papers]](#category-canonical-correlation-analysis-(cca)-in-neural-networks)
- [SVCCA for Intrinsic Dimensionality and Learning Dynamics [1 papers]](#category-svcca-for-intrinsic-dimensionality-and-learning-dynamics)
- [Representation Similarity in Fine-Tuned Transformers [1 papers]](#category-representation-similarity-in-fine-tuned-transformers)
- [Feature Representation Evolution in LLMs [1 papers]](#category-feature-representation-evolution-in-llms)
- [Layer-Specific Behavior in Neural Networks [6 papers]](#category-layer-specific-behavior-in-neural-networks)
- [Practical Applications of Critical Layer Identification [1 papers]](#category-practical-applications-of-critical-layer-identification)

### <a id='category-canonical-correlation-analysis-(cca)-in-neural-networks'></a>Canonical Correlation Analysis (CCA) in Neural Networks: 2 papers found.
The use of Canonical Correlation Analysis (CCA) in understanding neural network representations has been explored in several recent studies, highlighting its potential to compare and analyze how representations evolve across different models and layers. Researchers have developed variants of CCA, such as projection weighted CCA, to better differentiate between signal and noise in neural network representations, enabling more accurate comparisons \[[1](http://arxiv.org/abs/1806.05759)\]. These methods have been applied to convolutional neural networks (CNNs) and recurrent neural networks (RNNs), revealing insights into how networks converge to similar or distinct representations based on factors like generalization ability, network width, and learning rates \[[1](http://arxiv.org/abs/1806.05759)\]. Additionally, work has shown that traditional CCA and other statistics invariant to invertible linear transformations face limitations when measuring similarities in high-dimensional representation spaces, prompting the development of alternative similarity indices like centered kernel alignment (CKA), which is closely related to CCA and can effectively identify correspondences between representations trained from different initializations \[[3](http://arxiv.org/abs/1905.00414)\]. These advancements underscore the importance of CCA and its extensions in providing a deeper understanding of neural network behavior and representation dynamics.
|    | reference                                                                                                                  |   date | key idea/summary                                                                                                                                                                                                                                                                          |
|----|----------------------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Insights on representational similarity in neural networks with
  canonical correlation](http://arxiv.org/abs/1806.05759) |    nan | The paper introduces projection weighted CCA as a tool to analyze neural network representations, showing that generalizing networks converge to similar representations, wider networks have more similar solutions, and RNNs exhibit bottom-up convergence with variable hidden states. |
|  1 | [Similarity of Neural Network Representations Revisited](http://arxiv.org/abs/1905.00414)                                  |    nan | The paper introduces a similarity index based on centered kernel alignment (CKA) to measure representational similarity in neural networks, overcoming limitations of canonical correlation analysis (CCA) in high-dimensional settings.                                                  |
### <a id='category-svcca-for-intrinsic-dimensionality-and-learning-dynamics'></a>SVCCA for Intrinsic Dimensionality and Learning Dynamics: 1 papers found.
Answer:  
The proposed SVCCA technique offers a novel approach for comparing neural network representations, enabling analysis of intrinsic dimensionality and learning dynamics \[[2](http://arxiv.org/abs/1706.05806)\]. Unlike previous methods, SVCCA is invariant to affine transformations, allowing for meaningful comparisons across different layers and networks, and it is computationally efficient, facilitating extensive analysis \[[2](http://arxiv.org/abs/1706.05806)\]. This method has been applied to study how representations evolve during training, revealing that networks converge to final representations from the bottom up, and it has also been used to identify where class-specific information is formed within networks \[[2](http://arxiv.org/abs/1706.05806)\]. These insights contribute to understanding over-parameterization and suggest potential improvements in training regimes that could enhance efficiency and reduce overfitting \[[2](http://arxiv.org/abs/1706.05806)\].
|    | reference                                                                                                                                  |   date | key idea/summary                                                                                                                                                                                                             |
|----|--------------------------------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning
  Dynamics and Interpretability](http://arxiv.org/abs/1706.05806) |    nan | SVCCA is a new technique for comparing neural network representations, offering affine transform invariance and computational efficiency to analyze layer dimensionality, learning dynamics, and class-specific information. |
### <a id='category-representation-similarity-in-fine-tuned-transformers'></a>Representation Similarity in Fine-Tuned Transformers: 1 papers found.
Context: 
	Document 1: [Category]: «Representation Similarity in Fine-Tuned Transformers»
[Snippet]: «Despite the success of fine-tuning pretrained language encoders like BERT for
downstream natural language understanding (NLU) tasks, it is still poorly
understood how neural networks change after fine-tuning. In this work, we use
centered kernel alignment (CKA), a method for comparing learned
representations, to measure the similarity of representations in task-tuned
models across layers. In experiments across twelve NLU tasks, we discover a
consistent block diagonal structure in the similarity of representations within
fine-tuned RoBERTa and ALBERT models, with strong similarity within clusters of
earlier and later layers, but not between them. The similarity of later layer
representations implies that later layers only marginally contribute to task
performance, and we verify in experiments that the top few layers of fine-tuned
Transformers can be discarded without hurting performance, even with no further
tuning.»
[_citation_number]: «4»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T04:21:39+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1905.00414)\]. Further details \[[6](http://arxiv.org/abs/2202.05262)\]\[[7](http://arxiv.org/abs/2304.13734)\]\[[8](http://arxiv.org/abs/2410.02330)\]\[[9](http://arxiv.org/abs/2404.07066)\]\[[10](http://arxiv.org/abs/2412.09563)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Understanding how feature representations evolve across layers in large
language models (LLMs) is key to improving their interpretability and
robustness. While recent studies have identified critical layers linked to
specific functions or behaviors, these efforts typically rely on data-dependent
analyses of fine-tuned models, limiting their use to post-hoc settings. In
contrast, we introduce a data-oblivious approach to identify intrinsic critical
layers in pre-fine-tuned LLMs by analyzing representation dynamics
|    | reference                                                                                                           |   date | key idea/summary                                                                                                                                                                                                                                        |
|----|---------------------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Fine-Tuned Transformers Show Clusters of Similar Representations Across
  Layers](http://arxiv.org/abs/2109.08406) |    nan | Fine-tuning pretrained language models like RoBERTa and ALBERT results in a block diagonal structure of representation similarity, indicating that later layers contribute minimally to task performance and can be discarded without performance loss. |
### <a id='category-feature-representation-evolution-in-llms'></a>Feature Representation Evolution in LLMs: 1 papers found.
Context: 
	Document 1: [Category]: «Feature Representation Evolution in LLMs»
[Snippet]: «As language models are applied to an increasing number of real-world
applications, understanding their inner workings has become an important issue
in model trust, interpretability, and transparency. In this work we show that
representation dissimilarity measures, which are functions that measure the
extent to which two model's internal representations differ, can be a valuable
tool for gaining insight into the mechanics of language models. Among our
insights are: (i) an apparent asymmetry in the internal representations of
model using SoLU and GeLU activation functions, (ii) evidence that
dissimilarity measures can identify and locate generalization properties of
models that are invisible via in-distribution test set performance, and (iii)
new evaluations of how language model features vary as width and depth are
increased. Our results suggest that dissimilarity measures are a promising set
of tools for shedding light on the inner workings of language models.»
[_citation_number]: «5»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T04:21:39+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1905.00414)\]. Further details \[[6](http://arxiv.org/abs/2202.05262)\]\[[7](http://arxiv.org/abs/2304.13734)\]\[[8](http://arxiv.org/abs/2410.02330)\]\[[9](http://arxiv.org/abs/2404.07066)\]\[[10](http://arxiv.org/abs/2412.09563)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Understanding how feature representations evolve across layers in large
language models (LLMs) is key to improving their interpretability and
robustness. While recent studies have identified critical layers linked to
specific functions or behaviors, these efforts typically rely on data-dependent
analyses of fine-tuned models, limiting their use to post-hoc settings. In
contrast, we introduce a data-oblivious approach to identify intrinsic critical
layers in pre-fine-tuned LLMs by analyzing
|    | reference                                                                                                                     |   date | key idea/summary                                                                                                                                                                                                                           |
|----|-------------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Understanding the Inner Workings of Language Models Through
  Representation Dissimilarity](http://arxiv.org/abs/2310.14993) |    nan | Representation dissimilarity measures provide valuable insights into the internal workings of language models, revealing asymmetries in activation functions, generalization properties, and how model features vary with width and depth. |
### <a id='category-layer-specific-behavior-in-neural-networks'></a>Layer-Specific Behavior in Neural Networks: 6 papers found.
Context: 
	Document 1: [Category]: «Layer-Specific Behavior in Neural Networks»
[Snippet]: «We analyze the storage and recall of factual associations in autoregressive
transformer language models, finding evidence that these associations
correspond to localized, directly-editable computations. We first develop a
causal intervention for identifying neuron activations that are decisive in a
model's factual predictions. This reveals a distinct set of steps in
middle-layer feed-forward modules that mediate factual predictions while
processing subject tokens. To test our hypothesis that these computations
correspond to factual association recall, we modify feed-forward weights to
update specific factual associations using Rank-One Model Editing (ROME). We
find that ROME is effective on a standard zero-shot relation extraction (zsRE)
model-editing task, comparable to existing methods. To perform a more sensitive
evaluation, we also evaluate ROME on a new dataset of counterfactual
assertions, on which it simultaneously maintains both specificity and
generalization, whereas other methods sacrifice one or another. Our results
confirm an important role for mid-layer feed-forward modules in storing factual
associations and suggest that direct manipulation of computational mechanisms
may be a feasible approach for model editing. The code, dataset,
visualizations, and an interactive demo notebook are available at
https://rome.baulab.info/»
[_citation_number]: «6»

	Document 2: [Category]: «Layer-Specific Behavior in Neural Networks»
[Snippet]: «As a manner to augment pre-trained large language models (LLM), knowledge
injection is critical to develop vertical domain large models and has been
widely studied. Although most current approaches, including parameter-efficient
fine-tuning (PEFT) and block expansion methods, uniformly apply knowledge
across all LLM layers, it raises the question: are all layers equally crucial
for knowledge injection? We begin by evaluating the importance of each layer in
finding the optimal layer range for knowledge injection. Intuitively, the more
important layers should play a more critical role in knowledge injection and
deserve a denser injection. We observe performance dips in question-answering
benchmarks after the removal or expansion of the shallow layers, and the
degradation shrinks as the layer gets deeper, indicating that the shallow
layers hold the key to knowledge injection. This insight leads us to propose
the S strategy, a post-pretraining strategy of selectively enhancing shallow
layers while pruning the less effective deep
|    | reference                                                                                                                                                                                 |   date | key idea/summary                                                                                                                                                                                                                                                                        |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Locating and Editing Factual Associations in GPT](http://arxiv.org/abs/2202.05262)                                                                                                       |    nan | The paper demonstrates that mid-layer feed-forward modules in autoregressive transformer models store factual associations, and proposes ROME, a method for directly editing these associations to improve model-editing tasks.                                                         |
|  1 | [Llama SLayer 8B: Shallow Layers Hold the Key to Knowledge Injection](http://arxiv.org/abs/2410.02330)                                                                                    |    nan | The paper proposes a strategy called S, which selectively enhances shallow layers and prunes deeper layers in pre-trained large language models to improve knowledge injection effectiveness, demonstrating its applicability across different domains and models.                      |
|  2 | [Exploring Concept Depth: How Large Language Models Acquire Knowledge and
  Concept at Different Layers?](http://arxiv.org/abs/2404.07066)                                                |    nan | This paper introduces the concept of 'Concept Depth' to explore how large language models process tasks of varying complexity across different layers, revealing that more complex tasks are typically handled in deeper layers.                                                        |
|  3 | [Does Representation Matter? Exploring Intermediate Layers in Large
  Language Models](http://arxiv.org/abs/2412.09563)                                                                   |    nan | This paper investigates the quality of intermediate representations in large language models, finding that intermediate layers often provide more informative representations than final layers, and highlights architectural differences and factors affecting representation quality. |
|  4 | [Do Wide and Deep Networks Learn the Same Things? Uncovering How Neural
                  Network Representations Vary with Width and Depth](https://openreview.net/forum?id=KJNcAkY8tY4) |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                               |
|  5 | [Defending Large Language Models Against Jailbreak Attacks via Layer-specific
                  Editing](https://aclanthology.org/2024.findings-emnlp.293)                                |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                               |
### <a id='category-practical-applications-of-critical-layer-identification'></a>Practical Applications of Critical Layer Identification: 1 papers found.
Context: 
	Document 1: [Category]: «Practical Applications of Critical Layer Identification»
[Snippet]: «While Large Language Models (LLMs) have shown exceptional performance in various tasks, one of their most prominent drawbacks is generating inaccurate or false information with a confident tone. In this paper, we provide evidence that the LLM's internal state can be used to reveal the truthfulness of statements. This includes both statements provided to the LLM, and statements that the LLM itself generates. Our approach is to train a classifier that outputs the probability that a statement is truthful, based on the hidden layer activations of the LLM as it reads or generates the statement. Experiments demonstrate that given a set of test sentences, of which half are true and half false, our trained classifier achieves an average of 71% to 83% accuracy labeling which sentences are true versus false, depending on the LLM base model. Furthermore, we explore the relationship between our classifier's performance and approaches based on the probability assigned to the sentence by the LLM. We show that while LLM-assigned sentence probability is related to sentence truthfulness, this probability is also dependent on sentence length and the frequencies of words in the sentence, resulting in our trained classifier providing a more reliable approach to detecting truthfulness, highlighting its potential to enhance the reliability of LLM-generated content and its practical applicability in real-world scenarios.»
[_citation_number]: «7»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T04:21:39+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1905.00414)\]. Further details \[[6](http://arxiv.org/abs/2202.05262)\]\[[7](http://arxiv.org/abs/2304.13734)\]\[[8](http://arxiv.org/abs/2410.02330)\]\[[9](http://arxiv.org/abs/2404.07066)\]\[[10](http://arxiv.org/abs/2412.09563)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Understanding how feature representations evolve across layers in large language models (LLMs) is key to improving their interpretability and robustness. While
|    | reference                                                                             |   date | key idea/summary                                                                                                                                                                                                     |
|----|---------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [The Internal State of an LLM Knows When It's Lying](http://arxiv.org/abs/2304.13734) |    nan | This paper introduces a classifier that uses LLM's internal state to detect the truthfulness of statements, achieving 71% to 83% accuracy, and shows it is more reliable than relying on LLM-assigned probabilities. |
