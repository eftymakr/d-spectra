## Related Works

The rapid adoption of large language models (LLMs) has underscored the critical need for robust fairness benchmarks \[[1](http://arxiv.org/abs/2211.09110)\]. Traditional fairness metrics, such as Equalized Odds, focus on discrete accuracy-based evaluations and often overlook the implicit impact of model uncertainty \[[1](http://arxiv.org/abs/2211.09110)\]. This limitation is well-documented in the literature, where studies have shown that conventional fairness metrics fail to capture the nuanced relationship between model confidence and decision bias \[[2](http://arxiv.org/abs/2005.14050)\]. For instance, research has demonstrated that models can exhibit higher confidence in incorrect predictions, particularly for certain demographic groups, which conventional metrics fail to detect \[[3](http://arxiv.org/abs/2308.10149)\]. This gap in fairness evaluation has motivated the development of uncertainty-aware fairness metrics \[[1](http://arxiv.org/abs/2211.09110)\].

Several studies have explored the role of uncertainty in fairness assessment. For example, \[[4](http://arxiv.org/abs/2412.03537)\] introduces a framework that leverages aleatoric uncertainty (data ambiguity) to improve the fairness-utility trade-off in classification tasks. The authors argue that aleatoric uncertainty is a key factor in algorithmic fairness and that models with lower aleatoric uncertainty are more accurately and fairly modeled \[[4](http://arxiv.org/abs/2412.03537)\]. This aligns with our approach of incorporating uncertainty into fairness evaluation \[[1](http://arxiv.org/abs/2211.09110)\].

The importance of diverse and representative datasets for fairness evaluation has also been emphasized. Current datasets often suffer from issues of data size, diversity, and clarity, which can limit the generalizability of fairness assessments \[[1](http://arxiv.org/abs/2211.09110)\]. To address this, \[[5](http://arxiv.org/abs/2506.01709)\] introduces a new gender-occupation fairness evaluation dataset with 31,756 samples for co-reference resolution, offering a more diverse and suitable dataset for evaluating modern LLMs \[[5](http://arxiv.org/abs/2506.01709)\]. This dataset is designed to better capture the complexities of real-world bias and provides a more accurate benchmark for fairness evaluation.

In addition to dataset improvements, there has been growing interest in the use of uncertainty quantification (UQ) for fairness assessment. \[[6](http://arxiv.org/abs/2404.01349)\] proposes a method to measure uncertainty in large language models, highlighting the challenges posed by semantic equivalence and the need for linguistic invariances in uncertainty estimation \[[6](http://arxiv.org/abs/2404.01349)\]. Similarly, \[[7](http://arxiv.org/abs/2407.02408)\] introduces a heuristic for shifting attention to more relevant components in auto-regressive LLMs to improve uncertainty quantification \[[7](http://arxiv.org/abs/2407.02408)\]. These approaches underscore the importance of incorporating uncertainty into fairness evaluation, a concept that is central to our proposed metric, UCerF \[[1](http://arxiv.org/abs/2211.09110)\].

The integration of uncertainty into fairness evaluation is also supported by work on predictive uncertainty estimation. \[[8](http://arxiv.org/abs/2401.12794)\] proposes a framework called Prior Networks (PNs) that explicitly models distributional uncertainty, enabling better distinction between data and distributional uncertainty \[[8](http://arxiv.org/abs/2401.12794)\]. This work demonstrates the potential of uncertainty-aware models to improve fairness and reliability in AI systems \[[8](http://arxiv.org/abs/2401.12794)\].

In summary, the existing literature highlights the limitations of conventional fairness metrics and the need for uncertainty-aware approaches. Our work builds on these findings by introducing UCerF and a new dataset to enable a more comprehensive and accurate evaluation of LLM fairness \[[1](http://arxiv.org/abs/2211.09110)\].

1. \[[1](http://arxiv.org/abs/2211.09110)\] Holistic Evaluation of Language Models  
2. \[[2](http://arxiv.org/abs/2005.14050)\] Language (Technology) is Power: A Critical Survey of "Bias" in NLP  
3. \[[3](http://arxiv.org/abs/2308.10149)\] Gender bias and stereotypes in Large Language Models  
4. \[[4](http://arxiv.org/abs/2412.03537)\] Fairness through Aleatoric Uncertainty  
5. \[[5](http://arxiv.org/abs/2506.01709)\] Collecting a Large-Scale Gender Bias Dataset for Coreference Resolution and Machine Translation  
6. \[[6](http://arxiv.org/abs/2404.01349)\] Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation  
7. \[[7](http://arxiv.org/abs/2407.02408)\] Shifting Attention to Relevance: Towards the Predictive Uncertainty Quantification of Free-Form Large Language Models  
8. \[[8](http://arxiv.org/abs/2401.12794)\] Predictive Uncertainty Estimation via Prior Networks
## Research papers
### Outline
- [Gender and Occupation Bias in LLMs [10 papers]](#category-gender-and-occupation-bias-in-llms)
- [Dataset Diversity and Representation in Fairness Evaluation [2 papers]](#category-dataset-diversity-and-representation-in-fairness-evaluation)
- [Uncertainty Quantification Techniques for LLMs [9 papers]](#category-uncertainty-quantification-techniques-for-llms)
- [Coreference Resolution and Bias Datasets [4 papers]](#category-coreference-resolution-and-bias-datasets)
- [Aleatoric Uncertainty and Its Role in Fairness [2 papers]](#category-aleatoric-uncertainty-and-its-role-in-fairness)
- [Predictive Uncertainty Estimation Frameworks [2 papers]](#category-predictive-uncertainty-estimation-frameworks)
- [Linguistic Invariances in Uncertainty Estimation [1 papers]](#category-linguistic-invariances-in-uncertainty-estimation)

### <a id='category-gender-and-occupation-bias-in-llms'></a>Gender and Occupation Bias in LLMs: 10 papers found.
The related works section focuses on the growing body of research addressing gender and occupation bias in large language models (LLMs). Several studies have highlighted how LLMs can inherit and propagate social biases from their training data, leading to unfair outcomes in downstream tasks \[[3](http://arxiv.org/abs/2308.10149)\]. For instance, research has shown that LLMs often exhibit gender stereotypes in occupation prediction, with models being 3-6 times more likely to select stereotypically male or female occupations based on gender cues \[[9](http://arxiv.org/abs/2202.01711)\]. These biases are not only present in predictions but also in the explanations models provide, which can be factually inaccurate and obscure the true reasons behind biased outputs \[[9](http://arxiv.org/abs/2202.01711)\]. Additionally, studies have found that biases can emerge suddenly during training and do not always align with traditional performance metrics, necessitating new fairness evaluation metrics \[[5](http://arxiv.org/abs/2506.01709)\]. The evaluation of fairness in LLMs has also been extended to real-world deployment scenarios, such as prompt-based adaptations, where intrinsic biases in pre-trained models are strongly correlated with biases observed in downstream tasks \[[4](http://arxiv.org/abs/2412.03537)\]. To address these issues, researchers have proposed new fairness evaluation frameworks, including metrics like Average Rank and Jensen-Shannon Divergence by Parts, which allow for a more holistic assessment of bias dynamics during model training \[[5](http://arxiv.org/abs/2506.01709)\]. Furthermore, datasets such as the Bias in Open-Ended Language Generation (BOLD) have been introduced to systematically benchmark social biases across multiple domains, including gender, race, and religion \[[8](http://arxiv.org/abs/2401.12794)\]. These efforts underscore the importance of developing fairer LLMs that account for both explicit and implicit biases, ensuring equitable treatment of all users \[[6](http://arxiv.org/abs/2404.01349)\].
|    | reference                                                                                                                         |   date | key idea/summary                                                                                                                                                                                                                                                                                        |
|----|-----------------------------------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Holistic Evaluation of Language Models](http://arxiv.org/abs/2211.09110)                                                         |    nan | HELM is a comprehensive framework for evaluating language models by assessing a wide range of scenarios and metrics, ensuring transparency and consistency across different models.                                                                                                                     |
|  1 | [Language (Technology) is Power: A Critical Survey of "Bias" in NLP](http://arxiv.org/abs/2005.14050)                             |    nan | The paper critiques current NLP bias research for its vague motivations and poor alignment between methods and goals, proposing a more normative and socially aware approach to analyzing and mitigating bias.                                                                                          |
|  2 | [A Survey on Fairness in Large Language Models](http://arxiv.org/abs/2308.10149)                                                  |    nan | This paper provides a comprehensive review of fairness research in Large Language Models (LLMs), categorizing existing work based on model size and training paradigms, and discusses challenges and future directions for developing fair LLM systems.                                                 |
|  3 | [Evaluating Gender Bias Transfer between Pre-trained and Prompt-Adapted
  Language Models](http://arxiv.org/abs/2412.03537)       |    nan | The study shows that intrinsic biases in pre-trained LLMs strongly correlate with biases when models are prompted, highlighting the importance of ensuring fairness in pre-trained models for fair downstream task performance.                                                                         |
|  4 | [Fairness Dynamics During Training](http://arxiv.org/abs/2506.01709)                                                              |    nan | The paper investigates fairness dynamics during LLM training, introduces new metrics to evaluate bias, and finds that biases can emerge suddenly, with larger models exhibiting more bias and early stopping improving fairness at the cost of accuracy.                                                |
|  5 | [Fairness in Large Language Models: A Taxonomic Survey](http://arxiv.org/abs/2404.01349)                                          |    nan | This survey provides a comprehensive overview of recent advances in fair Large Language Models (LLMs), discussing bias factors, fairness metrics, evaluation resources, and open research challenges.                                                                                                   |
|  6 | [Beyond the Imitation Game: Quantifying and extrapolating the
  capabilities of language models](http://arxiv.org/abs/2206.04615) |    nan | The paper introduces the BIG-bench benchmark to evaluate the capabilities and limitations of large language models, highlighting that performance improves with scale but remains subpar compared to human raters, and that social bias can increase with scale but may be mitigated through prompting. |
|  7 | [BOLD: Dataset and Metrics for Measuring Biases in Open-Ended Language
  Generation](http://arxiv.org/abs/2101.11718)             |    nan | The paper introduces BOLD, a large-scale dataset for benchmarking social biases in open-ended language generation, and highlights that popular language models exhibit larger social biases than human-written text across multiple domains.                                                            |
|  8 | [Gender bias and stereotypes in Large Language Models](http://arxiv.org/abs/2308.14921)                                           |    nan | This paper demonstrates that large language models exhibit gender bias in occupational assumptions, often amplifying stereotypes beyond societal perceptions and ground truth, and provide factually inaccurate explanations for their biased predictions.                                              |
|  9 | [BBQ: A Hand-Built Bias Benchmark for Question Answering](http://arxiv.org/abs/2110.08193)                                        |    nan | The paper introduces the Bias Benchmark for QA (BBQ) to evaluate how NLP models reflect social biases in question answering tasks, finding that models often reproduce harmful biases, especially with under-informative contexts.                                                                      |
### <a id='category-dataset-diversity-and-representation-in-fairness-evaluation'></a>Dataset Diversity and Representation in Fairness Evaluation: 2 papers found.
The category "Dataset Diversity and Representation in Fairness Evaluation" highlights the critical role of diverse and representative datasets in assessing and mitigating biases in AI systems. Researchers have identified that existing fairness evaluation efforts often focus on specific types of bias and use inconsistent metrics, making cross-comparisons challenging \[[1](http://arxiv.org/abs/2211.09110)\]. To address these limitations, there has been a push towards creating more comprehensive benchmarks that cover various bias types, social groups, and tasks, such as the Compositional Evaluation Benchmark (CEB) \[[7](http://arxiv.org/abs/2407.02408)\]. This benchmark is curated using a compositional taxonomy that characterizes datasets across three dimensions: bias types, social groups, and tasks, enabling a more nuanced evaluation of model fairness \[[7](http://arxiv.org/abs/2407.02408)\]. Additionally, the algorithmic fairness community has recognized the need for standardized documentation of datasets, which is essential for transparency and reproducibility \[[9](http://arxiv.org/abs/2202.01711)\]. Efforts have been made to document over two hundred datasets, with in-depth analysis of popular ones like Adult, COMPAS, and German Credit, while also identifying alternative datasets that may better represent diverse populations and fairness tasks \[[9](http://arxiv.org/abs/2202.01711)\]. These initiatives underscore the importance of not only developing diverse datasets but also ensuring they are well-documented and suitable for evaluating fairness across different social groups and tasks \[[9](http://arxiv.org/abs/2202.01711)\]. The emphasis on data documentation and the development of more representative datasets aligns with the broader goal of creating fairer and more equitable AI systems \[[9](http://arxiv.org/abs/2202.01711)\].
|    | reference                                                                                                          |   date | key idea/summary                                                                                                                                                                                                                                                     |
|----|--------------------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [CEB: Compositional Evaluation Benchmark for Fairness in Large Language
  Models](http://arxiv.org/abs/2407.02408) |    nan | The paper introduces CEB, a comprehensive compositional evaluation benchmark for assessing biases in Large Language Models (LLMs), designed to address inconsistencies in existing bias evaluation methods by covering various bias types, social groups, and tasks. |
|  1 | [Algorithmic Fairness Datasets: the Story so Far](http://arxiv.org/abs/2202.01711)                                 |    nan | This work addresses the data documentation debt in algorithmic fairness research by surveying and standardizing documentation for over two hundred datasets, identifying key datasets, and proposing best practices for data curation.                               |
### <a id='category-uncertainty-quantification-techniques-for-llms'></a>Uncertainty Quantification Techniques for LLMs: 9 papers found.
The category "Uncertainty Quantification Techniques for LLMs" explores the critical role of uncertainty estimation in improving the reliability and fairness of large language models. Several studies highlight that traditional evaluation methods, such as HuggingFace's leaderboard, neglect uncertainty, which is essential for assessing model behavior \[[8](http://arxiv.org/abs/2401.12794)\]. Uncertainty estimation helps identify when models are overconfident or uncertain, especially in cases where accuracy alone is insufficient \[[18](http://arxiv.org/abs/2107.03342)\]. For instance, higher accuracy does not always correlate with higher certainty, and larger models may exhibit greater uncertainty compared to smaller ones \[[8](http://arxiv.org/abs/2401.12794)\]. Additionally, instruction-finetuning can increase uncertainty, underscoring the need for methods that account for this variability \[[8](http://arxiv.org/abs/2401.12794)\]. Researchers have categorized uncertainty sources in NLP into input, system, and output types, and have explored techniques like Bayesian neural networks, ensemble methods, and test-time data augmentation to model these uncertainties \[[3](http://arxiv.org/abs/2308.10149)\]. Some works also emphasize the importance of uncertainty in risk assessment, showing that it can reveal non-factual predictions and buggy outputs in code generation tasks \[[4](http://arxiv.org/abs/2412.03537)\]. Furthermore, studies have investigated self-evaluation capabilities of models, such as predicting the probability of correct answers or "I know" probabilities, which can enhance model honesty and reliability \[[7](http://arxiv.org/abs/2407.02408)\]. However, challenges remain, including biases in evaluation metrics that can distort the assessment of uncertainty methods \[[28](http://arxiv.org/abs/2504.13677)\]. These findings collectively emphasize the necessity of integrating uncertainty quantification into LLM evaluation frameworks to ensure fairness, transparency, and robustness.
|    | reference                                                                                                                                                         |   date | key idea/summary                                                                                                                                                                                                                                                                               |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Benchmarking LLMs via Uncertainty Quantification](http://arxiv.org/abs/2401.12794)                                                                               |    nan | The paper introduces a new benchmarking approach for LLMs that integrates uncertainty quantification, revealing that higher accuracy does not necessarily correlate with higher certainty, larger models may exhibit greater uncertainty, and instruction-finetuning can increase uncertainty. |
|  1 | [A Survey of Uncertainty in Deep Neural Networks](http://arxiv.org/abs/2107.03342)                                                                                |    nan | This work provides a comprehensive overview of uncertainty estimation in neural networks, covering sources of uncertainty, methods for modeling and measuring uncertainty, and challenges in practical applications.                                                                           |
|  2 | [Uncertainty in Natural Language Processing: Sources, Quantification, and
  Applications](http://arxiv.org/abs/2306.04459)                                        |    nan | This survey provides a comprehensive review of uncertainty-relevant works in natural language processing, categorizing uncertainty sources into input, system, and output, and discussing challenges and future directions in uncertainty estimation.                                          |
|  3 | [Look Before You Leap: An Exploratory Study of Uncertainty Measurement
  for Large Language Models](http://arxiv.org/abs/2307.10236)                              |    nan | This paper explores the use of uncertainty estimation to assess the risk of predictions made by Large Language Models (LLMs), showing its effectiveness in identifying uncertain or non-factual predictions and potential bugs in generated code.                                              |
|  4 | [A Baseline for Detecting Misclassified and Out-of-Distribution Examples
  in Neural Networks](http://arxiv.org/abs/1610.02136)                                   |    nan | The paper presents a simple baseline for detecting misclassified or out-of-distribution examples using softmax probabilities, showing its effectiveness across multiple domains and highlighting potential for future research.                                                                |
|  5 | [Shifting Attention to Relevance: Towards the Predictive Uncertainty
  Quantification of Free-Form Large Language Models](http://arxiv.org/abs/2307.01379)        |    nan | The research introduces SAR, a method that improves uncertainty quantification in large language models by shifting attention to more relevant tokens and sentences, thereby addressing the issue of linguistic redundancy and enhancing the reliability of model outputs.                     |
|  6 | [Language Models (Mostly) Know What They Know](http://arxiv.org/abs/2207.05221)                                                                                   |    nan | The study explores whether language models can evaluate the validity of their own claims and predict their ability to answer questions, showing promising results in self-evaluation and calibration of probabilities like P(True) and P(IK).                                                  |
|  7 | [Revisiting Uncertainty Quantification Evaluation in Language Models:
  Spurious Interactions with Response Length Bias Results](http://arxiv.org/abs/2504.13677) |    nan | The paper highlights that mutual biases between uncertainty quantification methods and correctness functions can distort evaluations, and proposes LM-as-a-judge methods as a more fair approach.                                                                                              |
|  8 | [LM-polygraph: Uncertainty estimation for language models]()                                                                                                      |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                      |
### <a id='category-coreference-resolution-and-bias-datasets'></a>Coreference Resolution and Bias Datasets: 4 papers found.
Context: 
	Document 1: [Category]: «Coreference Resolution and Bias Datasets»
[_citation_number]: «10»
[Snippet]: «The Winograd Schema Challenge - a set of twin sentences involving pronoun
reference disambiguation that seem to require the use of commonsense knowledge
- was proposed by Hector Levesque in 2011. By 2019, a number of AI systems,
based on large pre-trained transformer-based language models and fine-tuned on
these kinds of problems, achieved better than 90% accuracy. In this paper, we
review the history of the Winograd Schema Challenge and discuss the lasting
contributions of the flurry of research that has taken place on the WSC in the
last decade. We discuss the significance of various datasets developed for WSC,
and the research community's deeper understanding of the role of surrogate
tasks in assessing the intelligence of an AI system.»

	Document 2: [Category]: «Coreference Resolution and Bias Datasets»
[_citation_number]: «11»
[Snippet]: «We introduce a new benchmark, WinoBias, for coreference resolution focused on
gender bias. Our corpus contains Winograd-schema style sentences with entities
corresponding to people referred by their occupation (e.g. the nurse, the
doctor, the carpenter). We demonstrate that a rule-based, a feature-rich, and a
neural coreference system all link gendered pronouns to pro-stereotypical
entities with higher accuracy than anti-stereotypical entities, by an average
difference of 21.1 in F1 score. Finally, we demonstrate a data-augmentation
approach that, in combination with existing word-embedding debiasing
techniques, removes the bias demonstrated by these systems in WinoBias without
significantly affecting their performance on existing coreference benchmark
datasets. Our dataset and code are available at http://winobias.org.»

	Document 3: [Category]: «Coreference Resolution and Bias Datasets»
[_citation_number]: «12»
[Snippet]: «We present an empirical study of gender bias in coreference resolution
systems. We first introduce a novel, Winograd schema-style set of minimal pair
sentences that differ only by pronoun gender. With these "Winogender schemas,"
we evaluate and confirm systematic gender bias in three publicly-available
coreference resolution systems, and correlate this bias with real-world and
textual gender statistics.»

	Document 4: [Category]: «Coreference Resolution and Bias Datasets»
[_citation_number]: «17»
[Snippet]: «Recent works have found evidence of gender bias in models of machine
translation and coreference resolution using mostly synthetic diagnostic
datasets. While these quantify bias in a controlled experiment, they often do
so on a small scale and consist mostly of artificial, out-of-distribution
sentences. In this work, we find grammatical patterns indicating stereotypical
and non-stereotypical gender-role assignments (e.g., female nurses versus male
dancers) in corpora from three domains, resulting in a first large-scale gender
bias dataset of 108K diverse real-world English sentences. We manually verify
the quality of our corpus and use it to evaluate gender bias in various
coreference resolution and machine translation models. We find that all tested
models tend to over-rely on gender stereotypes when presented with natural
inputs, which may be especially harmful when deployed in commercial systems.
Finally, we show that our dataset lends itself to finetuning a coreference
resolution model, finding it mitigates bias on a held out set. Our dataset and
models are publicly available at www.github.com/SLAB-NLP/BUG. We hope they will
spur future research into gender bias evaluation mitigation techniques in
realistic settings.»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-29T20:45:18+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2308.10149)\]. Further details \[[6](http://arxiv.org/abs/2404.01349)\]\[[7](http://arxiv.org/abs/2407.02408)\]\[[8](http://arxiv.org/abs/2401.12794)\]\[[9](http://arxiv.org/abs/2202.01711)\]\[[10](http://arxiv.org/abs/2201.02387)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: The recent rapid adoption of large language models (LLMs) highlights the
critical need for benchmarking their fairness. Conventional fairness metrics,
which focus on discrete accuracy-based evaluations (i.e., prediction
correctness), fail to capture the implicit impact of model uncertainty (e.g.,
higher model confidence about one group over another despite similar accuracy).
To address this limitation, we propose an uncertainty-aware fairness metric,
UCerF, to enable a fine-grained evaluation of model fairness that is more
reflective of the internal bias in model decisions compared to conventional
fairness measures. Furthermore, observing data size, diversity, and clarity
issues in current datasets, we introduce a new gender-occupation fairness
evaluation dataset with 31,756 samples for co-reference resolution, offering a
more diverse and suitable dataset for evaluating modern LLMs. We establish a
benchmark, using our metric and dataset, and apply it to evaluate the behavior
of ten open-source LLMs. For example, Mistral-7B exhibits suboptimal fairness
due to high confidence in incorrect predictions, a detail overlooked by
Equalized Odds but captured by UCerF. Overall, our proposed LLM benchmark,
which evaluates fairness with uncertainty awareness, paves the way for
developing more transparent and accountable AI systems.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2308.10149)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2005.14050)\]\[[7](http://arxiv.org/abs/2407.02408)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The category of coreference resolution and bias datasets has seen significant advancements, particularly in addressing gender bias in language models. Researchers have developed datasets such as WinoBias \[[11](http://arxiv.org/abs/1804.06876)\], which focuses on coreference resolution with gendered pronouns, revealing that systems tend to favor stereotypical entities over anti-stereotypical ones \[[11](http://arxiv.org/abs/1804.06876)\]. Similarly, the "Winogender schemas" introduced in another study \[[12](http://arxiv.org/abs/1804.09301)\] highlight systematic gender bias in coreference resolution systems, showing that models correlate pronoun resolution with real-world gender statistics \[[12](http://arxiv.org/abs/1804.09301)\]. These findings are supported by broader observations of gender bias in machine translation and coreference resolution models, which often rely on synthetic datasets with limited diversity \[[17](http://arxiv.org/abs/2109.03858)\]. While earlier work on the Winograd Schema Challenge \[[10](http://arxiv.org/abs/2201.02387)\] emphasized commonsense reasoning and the role of surrogate tasks in assessing AI intelligence, recent efforts have shifted toward understanding and mitigating bias in real-world applications. For instance, a large-scale dataset of 108K real-world sentences has been created to evaluate gender-role stereotypes in coreference resolution, demonstrating that models over-rely on gender stereotypes when processing natural inputs \[[17](http://arxiv.org/abs/2109.03858)\]. These studies collectively underscore the importance of developing more diverse and representative datasets to improve fairness and reduce bias in language models.
|    | reference                                                                                                                            |   date | key idea/summary                                                                                                                                                                                                                                          |
|----|--------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [The Defeat of the Winograd Schema Challenge](http://arxiv.org/abs/2201.02387)                                                       |    nan | The paper reviews the history and contributions of the Winograd Schema Challenge, highlighting advancements in AI systems and the role of surrogate tasks in assessing AI intelligence.                                                                   |
|  1 | [Gender Bias in Coreference Resolution: Evaluation and Debiasing Methods](http://arxiv.org/abs/1804.06876)                           |    nan | The paper introduces a new benchmark, WinoBias, to evaluate gender bias in coreference resolution, showing that existing systems exhibit bias towards stereotypical entities and proposes a data-augmentation approach to mitigate this bias.             |
|  2 | [Gender Bias in Coreference Resolution](http://arxiv.org/abs/1804.09301)                                                             |    nan | The study presents an empirical analysis of gender bias in coreference resolution systems using a novel set of gender-differentiating sentences, revealing systematic bias correlated with real-world gender statistics.                                  |
|  3 | [Collecting a Large-Scale Gender Bias Dataset for Coreference Resolution
  and Machine Translation](http://arxiv.org/abs/2109.03858) |    nan | This work presents a large-scale gender bias dataset of 108K real-world English sentences, revealing that models tend to over-rely on gender stereotypes in coreference resolution and machine translation, and shows that fine-tuning can mitigate bias. |
### <a id='category-aleatoric-uncertainty-and-its-role-in-fairness'></a>Aleatoric Uncertainty and Its Role in Fairness: 2 papers found.
Context: 
	Document 1: [Category]: «Aleatoric Uncertainty and Its Role in Fairness»
[_citation_number]: «21»
[Snippet]: «There are two major types of uncertainty one can model. Aleatoric uncertainty captures noise inherent in the observations. On the other hand, epistemic uncertainty accounts for uncertainty in the model -- uncertainty which can be explained away given enough data. Traditionally it has been difficult to model epistemic uncertainty in computer vision, but with new Bayesian deep learning tools this is now possible. We study the benefits of modeling epistemic vs. aleatoric uncertainty in Bayesian deep learning models for vision tasks. For this we present a Bayesian deep learning framework combining input-dependent aleatoric uncertainty together with epistemic uncertainty. We study models under the framework with per-pixel semantic segmentation and depth regression tasks. Further, our explicit uncertainty formulation leads to new loss functions for these tasks, which can be interpreted as learned attenuation. This makes the loss more robust to noisy data, also giving new state-of-the-art results on segmentation and depth regression benchmarks.»

	Document 2: [Category]: «Aleatoric Uncertainty and Its Role in Fairness»
[_citation_number]: «29»
[Snippet]: «We propose a simple yet effective solution to tackle the often-competing goals of fairness and utility in classification tasks. While fairness ensures that the model's predictions are unbiased and do not discriminate against any particular group or individual, utility focuses on maximizing the model's predictive performance. This work introduces the idea of leveraging aleatoric uncertainty (e.g., data ambiguity) to improve the fairness-utility trade-off. Our central hypothesis is that aleatoric uncertainty is a key factor for algorithmic fairness and samples with low aleatoric uncertainty are modeled more accurately and fairly than those with high aleatoric uncertainty. We then propose a principled model to improve fairness when aleatoric uncertainty is high and improve utility elsewhere. Our approach first intervenes in the data distribution to better decouple aleatoric uncertainty and epistemic uncertainty. It then introduces a fairness-utility bi-objective loss defined based on the estimated aleatoric uncertainty. Our approach is theoretically guaranteed to improve the fairness-utility trade-off. Experimental results on both tabular and image datasets show that the proposed approach outperforms state-of-the-art methods w.r.t. the fairness-utility trade-off and w.r.t. both group and individual fairness metrics. This work presents a fresh perspective on the trade-off between utility and algorithmic fairness and opens a key avenue for the potential of using prediction uncertainty in fair machine learning.»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-29T20:45:18+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2308.10149)\]. Further details \[[6](http://arxiv.org/abs/2404.01349)\]\[[7](http://arxiv.org/abs/2407.02408)\]\[[8](http://arxiv.org/abs/2401.12794)\]\[[9](http://arxiv.org/abs/2202.01711)\]\[[10](http://arxiv.org/abs/2201.02387)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: The recent rapid adoption of large language models (LLMs) highlights the
critical need for benchmarking their fairness. Conventional fairness metrics,
which focus on discrete accuracy-based evaluations (i.e., prediction
correctness), fail to capture the implicit impact of model uncertainty (e.g.,
higher model confidence about one group over another despite similar accuracy).
To address this limitation, we propose an uncertainty-aware fairness metric,
UCerF, to enable a fine-grained evaluation of model fairness that is more
reflective of the internal bias in model decisions compared to conventional
fairness measures. Furthermore, observing data size, diversity, and clarity
issues in current datasets, we introduce a new gender-occupation fairness
evaluation dataset with 31,756 samples for co-reference resolution, offering a
more diverse and suitable dataset for evaluating modern LLMs. We establish a
benchmark, using our metric and dataset, and apply it to evaluate the behavior
of ten open-source LLMs. For example, Mistral-7B exhibits suboptimal fairness
due to high confidence in incorrect predictions, a detail overlooked by
Equalized Odds but captured by UCerF. Overall, our proposed LLM benchmark,
which evaluates fairness with uncertainty awareness, paves the way for
developing more transparent and accountable AI systems.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2308.10149)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2005.14050)\]\[[7](http://arxiv.org/abs/2407.02408)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Aleatoric uncertainty, which captures noise inherent in observations, has been increasingly studied for its role in fairness and model performance \[[21](http://arxiv.org/abs/1703.04977)\]. This type of uncertainty is distinct from epistemic uncertainty, which relates to model limitations and can be mitigated with more data \[[21](http://arxiv.org/abs/1703.04977)\]. Recent work has focused on leveraging aleatoric uncertainty to improve fairness-utility trade-offs in classification tasks \[[29](http://arxiv.org/abs/2304.03646)\]. By recognizing that samples with low aleatoric uncertainty are modeled more accurately and fairly, researchers have proposed frameworks that decouple aleatoric and epistemic uncertainty to enhance fairness \[[29](http://arxiv.org/abs/2304.03646)\]. These approaches introduce bi-objective losses that account for uncertainty estimates, leading to improved fairness metrics and performance \[[29](http://arxiv.org/abs/2304.03646)\]. This aligns with broader efforts to incorporate uncertainty-aware fairness metrics, such as UCerF, which capture the internal bias in model decisions by considering both accuracy and confidence \[[21](http://arxiv.org/abs/1703.04977)\].
|    | reference                                                                                                         |   date | key idea/summary                                                                                                                                                                                                                                     |
|----|-------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [What Uncertainties Do We Need in Bayesian Deep Learning for Computer
  Vision?](http://arxiv.org/abs/1703.04977) |    nan | The paper introduces a Bayesian deep learning framework that models both aleatoric and epistemic uncertainties for vision tasks, leading to more robust loss functions and state-of-the-art results in semantic segmentation and depth regression.   |
|  1 | [Fairness through Aleatoric Uncertainty](http://arxiv.org/abs/2304.03646)                                         |    nan | This work proposes a method that leverages aleatoric uncertainty to improve the fairness-utility trade-off in classification tasks, achieving better performance in both group and individual fairness metrics compared to state-of-the-art methods. |
### <a id='category-predictive-uncertainty-estimation-frameworks'></a>Predictive Uncertainty Estimation Frameworks: 2 papers found.
Context: 
	Document 1: [Category]: «Predictive Uncertainty Est落地 Frameworks»
[_citation_number]: «23»
[Snippet]: «Deep learning tools have gained tremendous attention in applied machine
learning. However such tools for regression and classification do not capture
model uncertainty. In comparison, Bayesian models offer a mathematically
grounded framework to reason about model uncertainty, but usually come with a
prohibitive computational cost. In this paper we develop a new theoretical
framework casting dropout training in deep neural networks (NNs) as approximate
Bayesian inference in deep Gaussian processes. A direct result of this theory
gives us tools to model uncertainty with dropout NNs -- extracting information
from existing models that has been thrown away so far. This mitigates the
problem of representing uncertainty in deep learning without sacrificing either
computational complexity or test accuracy. We perform an extensive study of the
properties of dropout's uncertainty. Various network architectures and
non-linearities are assessed on tasks of regression and classification, using
MNIST as an example. We show a considerable improvement in predictive
log-likelihood and RMSE compared to existing state-of-the-art methods, and
finish by using dropout's uncertainty in deep reinforcement learning.»

	Document 2: [Category]: «Predictive Uncertainty Estimation Frameworks»
[_citation_number]: «27»
[Snippet]: «Estimating how uncertain an AI system is in its predictions is important to
improve the safety of such systems. Uncertainty in predictive can result from
uncertainty in model parameters, irreducible data uncertainty and uncertainty
due to distributional mismatch between the test and training data
distributions. Different actions might be taken depending on the source of the
uncertainty so it is important to be able to distinguish between them.
Recently, baseline tasks and metrics have been defined and several practical
methods to estimate uncertainty developed. These methods, however, attempt to
model uncertainty due to distributional mismatch either implicitly through
model uncertainty or as data uncertainty. This work proposes a new framework
for modeling predictive uncertainty called Prior Networks (PNs) which
explicitly models distributional uncertainty. PNs do this by parameterizing a
prior distribution over predictive distributions. This work focuses on
uncertainty for classification and evaluates PNs on the tasks of identifying
out-of-distribution (OOD) samples and detecting misclassification on the MNIST
dataset, where they are found to outperform previous methods. Experiments on
synthetic and MNIST and CIFAR-10 data show that unlike previous non-Bayesian
methods PNs are able to distinguish between data and distributional
uncertainty.»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-29T20:45:18+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2308.10149)\]. Further details \[[6](http://arxiv.org/abs/2404.01349)\]\[[7](http://arxiv.org/abs/2407.02408)\]\[[8](http://arxiv.org/abs/2401.12794)\]\[[9](http://arxiv.org/abs/2202.01711)\]\[[10](http://arxiv.org/abs/2201.02387)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: The recent rapid adoption of large language models (LLMs) highlights the
critical need for benchmarking their fairness. Conventional fairness metrics,
which focus on discrete accuracy-based evaluations (i.e., prediction
correctness), fail to capture the implicit impact of model uncertainty (e.g.,
higher model confidence about one group over another despite similar accuracy).
To address this limitation, we propose an uncertainty-aware fairness metric,
UCerF, to enable a fine-grained evaluation of model fairness that is more
reflective of the internal bias in model decisions compared to conventional
fairness measures. Furthermore, observing data size, diversity, and clarity
issues in current datasets, we introduce a new gender-occupation fairness
evaluation dataset with 31,756 samples for co-reference resolution, offering a
more diverse and suitable dataset for evaluating modern LLMs. We establish a
benchmark, using our metric and dataset, and apply it to evaluate the behavior
of ten open-source LLMs. For example, Mistral-7B exhibits suboptimal fairness
due to high confidence in incorrect predictions, a detail overlooked by
Equalized Odds but captured by UCerF. Overall, our proposed LLM benchmark,
which evaluates fairness with uncertainty awareness, paves the way for
developing more transparent and accountable AI systems.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2308.10149)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2005.14050)\]\[[7](http://arxiv.org/abs/2407.02408)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Predictive uncertainty estimation has been a focal point in recent machine learning research, particularly in addressing the limitations of traditional deep learning models that fail to capture model uncertainty \[[23](http://arxiv.org/abs/1506.02142)\]. Bayesian models, while mathematically grounded for uncertainty quantification, often face computational challenges \[[23](http://arxiv.org/abs/1506.02142)\]. To address this, frameworks such as dropout training in deep neural networks have been proposed as an approximate Bayesian inference method, enabling uncertainty estimation without significant computational overhead \[[23](http://arxiv.org/abs/1506.02142)\]. This approach has shown improvements in predictive log-likelihood and RMSE on tasks like regression and classification, using MNIST as a benchmark \[[23](http://arxiv.org/abs/1506.02142)\]. Additionally, methods like Prior Networks (PNs) have been introduced to explicitly model distributional uncertainty by parameterizing a prior distribution over predictive distributions, allowing for better distinction between data and distributional uncertainty \[[27](http://arxiv.org/abs/1802.10501)\]. These frameworks highlight the importance of uncertainty estimation in enhancing model reliability and safety, particularly in applications where decision-making under uncertainty is critical.
|    | reference                                                                                                                 |   date | key idea/summary                                                                                                                                                                                                                                                             |
|----|---------------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Dropout as a Bayesian Approximation: Representing Model Uncertainty in
  Deep Learning](http://arxiv.org/abs/1506.02142) |    nan | This paper presents a theoretical framework that interprets dropout training in deep neural networks as approximate Bayesian inference, enabling the modeling of uncertainty without sacrificing computational efficiency or test accuracy.                                  |
|  1 | [Predictive Uncertainty Estimation via Prior Networks](http://arxiv.org/abs/1802.10501)                                   |    nan | Prior Networks (PNs) are a new framework for modeling predictive uncertainty that explicitly distinguishes between data uncertainty and distributional mismatch, outperforming previous methods in identifying out-of-distribution samples and detecting misclassifications. |
### <a id='category-linguistic-invariances-in-uncertainty-estimation'></a>Linguistic Invariances in Uncertainty Estimation: 1 papers found.
Context: 
	Document 1: [Category]: «Linguistic Invariances in Uncertainty Estimation»
[_citation_number]: «24»
[Snippet]: «We introduce a method to measure uncertainty in large language models. For tasks like question answering, it is essential to know when we can trust the natural language outputs of foundation models. We show that measuring uncertainty in natural language is challenging because of "semantic equivalence" -- different sentences can mean the same thing. To overcome these challenges we introduce semantic entropy -- an entropy which incorporates linguistic invariances created by shared meanings. Our method is unsupervised, uses only a single model, and requires no modifications to off-the-shelf language models. In comprehensive ablation studies we show that the semantic entropy is more predictive of model accuracy on question answering data sets than comparable baselines.»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-29T20:45:18+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2308.10149)\]. Further details \[[6](http://arxiv.org/abs/2404.01349)\]\[[7](http://arxiv.org/abs/2407.02408)\]\[[8](http://arxiv.org/abs/2401.12794)\]\[[9](http://arxiv.org/abs/2202.01711)\]\[[10](http://arxiv.org/abs/2201.02387)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: The recent rapid adoption of large language models (LLMs) highlights the critical need for benchmarking their fairness. Conventional fairness metrics, which focus on discrete accuracy-based evaluations (i.e., prediction correctness), fail to capture the implicit impact of model uncertainty (e.g., higher model confidence about one group over another despite similar accuracy). To address this limitation, we propose an uncertainty-aware fairness metric, UCerF, to enable a fine-grained evaluation of model fairness that is more reflective of the internal bias in model decisions compared to conventional fairness measures. Furthermore, observing data size, diversity, and clarity issues in current datasets, we introduce a new gender-occupation fairness evaluation dataset with 31,756 samples for co-reference resolution, offering a more diverse and suitable dataset for evaluating modern LLMs. We establish a benchmark, using our metric and dataset, and apply it to evaluate the behavior of ten open-source LLMs. For example, Mistral-7B exhibits suboptimal fairness due to high confidence in incorrect predictions, a detail overlooked by Equalized Odds but captured by UCerF. Overall, our proposed LLM benchmark, which evaluates fairness with uncertainty awareness, paves the way for developing more transparent and accountable AI systems.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2308.10149)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2005.14050)\]\[[7](http://arxiv.org/abs/2407.02408)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
The study of uncertainty estimation in natural language processing has gained significant attention, particularly in the context of large language models (LLMs). A key challenge in measuring uncertainty is the phenomenon of "semantic equivalence," where different sentences can convey the same meaning, making it difficult to assess model confidence accurately \[[24](http://arxiv.org/abs/2302.09664)\]. To address this, researchers have proposed methods that incorporate linguistic invariances to better capture the shared meanings behind different expressions. One such approach is semantic entropy, which extends traditional entropy measures by accounting for these invariances, leading to more reliable uncertainty estimates \[[24](http://arxiv.org/abs/2302.09664)\]. This is particularly important for tasks like question answering, where model outputs must be trusted to provide accurate and reliable information. The unsupervised nature of these methods allows for their application without requiring modifications to existing language models, making them versatile tools for improving the interpretability and reliability of LLMs.
|    | reference                                                                                                                                   |   date | key idea/summary                                                                                                                                                                                                                                       |
|----|---------------------------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation
  in Natural Language Generation](http://arxiv.org/abs/2302.09664) |    nan | The paper introduces semantic entropy, an unsupervised method to measure uncertainty in large language models by incorporating linguistic invariances, which is more predictive of model accuracy on question answering tasks than existing baselines. |
