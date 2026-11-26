## Related Works

The field of in-context learning (ICL) has seen significant advancements, particularly in the context of large language models (LLMs) and their ability to leverage annotated corpora for task execution \[[1](http://arxiv.org/abs/2110.10456)\]. However, the reliance on high-quality demonstrations has exposed critical limitations when dealing with noisy annotations. Existing approaches often assume that noisy samples yield higher perplexity than clean ones, using local perplexity rankings to detect anomalies \[[2](http://arxiv.org/abs/2012.11854)\]. This assumption, however, becomes invalid under high noise ratios, where many demonstrations are flawed, leading to unreliable detection \[[3](http://arxiv.org/abs/2406.16966)\].

Several studies have addressed the issue of noisy annotations in deep learning models. For instance, \[[4](http://arxiv.org/abs/2207.13316)\] explores the challenges of training models with noisy labels, emphasizing the need for robust methods to correct such errors. Similarly, \[[5](http://arxiv.org/abs/2312.12275)\] proposes a framework for mitigating noisy supervision by generating synthetic samples with soft labels, which helps in improving generalization performance. These approaches, while effective in some settings, often fail to account for the complex interplay between annotation quality and model behavior \[[6](http://arxiv.org/abs/2212.01189)\].

In the context of object detection, \[[7](http://arxiv.org/abs/1407.5155)\] highlights the importance of correcting noisy annotations, particularly in large-scale datasets obtained through cloud sourcing. Their work demonstrates that entangled noises in class labels and bounding boxes can significantly degrade model performance, necessitating methods to decouple and correct these errors \[[8](http://arxiv.org/abs/2401.14360)\]. This aligns with the broader challenge of handling noisy annotations in various NLP and vision tasks \[[9](http://arxiv.org/abs/1809.04019)\].

The problem of label noise has also been studied in the context of reinforcement learning, where \[[10](http://arxiv.org/abs/2410.09365)\] introduces a novel data acquisition approach to enable in-context learning from noisy data. This work shows that synthetic noise injection can be used to generate learning histories, reducing the reliance on optimal policy generation \[[11](http://arxiv.org/abs/2305.10736)\]. These findings are relevant to the broader discussion on handling noisy annotations in ICL settings \[[12](http://arxiv.org/abs/2106.07704)\].

In addition, \[[13](http://arxiv.org/abs/2412.04727)\] proposes a method for robust image denoising by translating unknown real-world noise into Gaussian noise, enabling the use of pre-trained denoising networks. This approach is particularly relevant to the generalization challenges faced by models trained on noisy data \[[14](http://arxiv.org/abs/1911.05241)\].

The importance of annotation quality in downstream tasks has also been highlighted in the context of named entity recognition, where \[[15](http://arxiv.org/abs/2408.15204)\] demonstrates the brittleness of standard models to capitalization errors. Their approach, based on data augmentation, allows models to learn how to handle such noise without sacrificing performance on well-formed text \[[16](http://arxiv.org/abs/2004.10283)\].

Finally, \[[17](http://arxiv.org/abs/2103.06413)\] explores the use of LLM annotations in computational social science, emphasizing the need for confidence-driven inference to ensure validity while reducing the reliance on human annotations. This work provides insights into the broader implications of using noisy annotations in downstream tasks .

---

**References**  
\[[1](http://arxiv.org/abs/2110.10456)\] http://arxiv.org/abs/2110.10456  
\[[2](http://arxiv.org/abs/2012.11854)\] http://arxiv.org/abs/2012.11854  
\[[3](http://arxiv.org/abs/2406.16966)\] http://arxiv.org/abs/2406.16966  
\[[4](http://arxiv.org/abs/2207.13316)\] http://arxiv.org/abs/2207.13316  
\[[5](http://arxiv.org/abs/2312.12275)\] http://arxiv.org/abs/2212.01189  
\[[6](http://arxiv.org/abs/2212.01189)\] http://arxiv.org/abs/2401.14360  
\[[7](http://arxiv.org/abs/1407.5155)\] http://arxiv.org/abs/1407.5155  
\[[8](http://arxiv.org/abs/2401.14360)\] http://arxiv.org/abs/1809.04019  
\[[9](http://arxiv.org/abs/1809.04019)\] http://arxiv.org/abs/2410.09365  
\[[10](http://arxiv.org/abs/2410.09365)\] http://arxiv.org/abs/2312.12275  
\[[11](http://arxiv.org/abs/2305.10736)\] http://arxiv.org/abs/2106.07704  
\[[12](http://arxiv.org/abs/2106.07704)\] http://arxiv.org/abs/2412.04727  
\[[13](http://arxiv.org/abs/2412.04727)\] http://arxiv.org/abs/1911.05241  
\[[14](http://arxiv.org/abs/1911.05241)\] http://arxiv.org/abs/2408.15204  
\[[15](http://arxiv.org/abs/2408.15204)\] http://arxiv.org/abs/2004.10283  
\[[16](http://arxiv.org/abs/2004.10283)\] http://arxiv.org/abs/2103.06413  
\[[17](http://arxiv.org/abs/2103.06413)\] http://arxiv.org/abs/2406.16966  
 http://arxiv.org/abs/2408.15204
## Research papers
### Outline
- [Noise Correction in Object Detection [1 papers]](#category-noise-correction-in-object-detection)
- [Annotation Quality and Its Impact on Model Performance [2 papers]](#category-annotation-quality-and-its-impact-on-model-performance)
- [Synthetic Data Generation for Noisy Label Mitigation [2 papers]](#category-synthetic-data-generation-for-noisy-label-mitigation)
- [Label Noise in Reinforcement Learning [2 papers]](#category-label-noise-in-reinforcement-learning)
- [Generalization Challenges with Noisy Data [6 papers]](#category-generalization-challenges-with-noisy-data)
- [Data Augmentation for Handling Noisy Annotations [2 papers]](#category-data-augmentation-for-handling-noisy-annotations)
- [Confidence-Driven Inference in LLMs [1 papers]](#category-confidence-driven-inference-in-llms)
- [Annotation Reliability in Downstream Tasks [1 papers]](#category-annotation-reliability-in-downstream-tasks)

### <a id='category-noise-correction-in-object-detection'></a>Noise Correction in Object Detection: 1 papers found.
Context: 
	Document 1: [Snippet]: «Supervised training of object detectors requires well-annotated large-scale datasets, whose production is costly. Therefore, some efforts have been made to obtain annotations in economical ways, such as cloud sourcing. However, datasets obtained by these methods tend to contain noisy annotations such as inaccurate bounding boxes and incorrect class labels. In this study, we propose a new problem setting of training object detectors on datasets with entangled noises of annotations of class labels and bounding boxes. Our proposed method efficiently decouples the entangled noises, corrects the noisy annotations, and subsequently trains the detector using the corrected annotations. We verified the effectiveness of our proposed method and compared it with the baseline on noisy datasets with different noise levels. The experimental results show that our proposed method significantly outperforms the baseline.»
[_citation_number]: «1»
[Category]: «Noise Correction in Object Detection»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T06:44:48+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2406.16966)\]. Further details \[[6](http://arxiv.org/abs/2212.01189)\]\[[7](http://arxiv.org/abs/1407.5155)\]\[[8](http://arxiv.org/abs/2401.14360)\]\[[9](http://arxiv.org/abs/1809.04019)\]\[[10](http://arxiv.org/abs/2410.09365)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In context learning (ICL) relies heavily on high quality demonstrations drawn
from large annotated corpora. Existing approaches detect noisy annotations by
ranking local perplexities, presuming that noisy samples yield higher
perplexities than their clean counterparts. However, this assumption breaks
down when the noise ratio is high and many demonstrations are flawed. We
reexamine the perplexity based paradigm for text generation under noisy
annotations, highlighting two sources of bias in perplexity: the annotation
itself and the domain specific knowledge inherent in large language models
(LLMs). To overcome these biases, we introduce a dual debiasing framework that
uses synthesized neighbors to explicitly correct perplexity estimates, yielding
a robust Sample Cleanliness Score. This metric uncovers absolute sample
cleanliness regardless of the overall corpus noise level. Extensive experiments
demonstrate our method's superior noise detection capabilities and show that
its final ICL performance is comparable to that of a fully clean demonstration
corpus. Moreover, our approach remains robust even when noise ratios are
extremely high.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2406.16966)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2012.11854)\]\[[7](http://arxiv.org/abs/1407.5155)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Noise correction in object detection has been a critical area of research, particularly due to the challenges posed by noisy annotations in large-scale datasets. These datasets, often obtained through cost-effective methods like cloud sourcing, frequently contain inaccuracies such as incorrect class labels and imprecise bounding boxes \[[1](http://arxiv.org/abs/2110.10456)\]. Addressing these issues is essential for improving the reliability of object detectors trained on such data. Recent studies have focused on developing methods that can decouple and correct these entangled noises, leading to more accurate training outcomes \[[1](http://arxiv.org/abs/2110.10456)\]. The proposed approaches aim to enhance the quality of annotations by systematically identifying and rectifying errors, which in turn improves the overall performance of the object detection models. This work builds on previous efforts to handle noisy data, emphasizing the need for robust solutions that can effectively mitigate annotation errors and ensure the accuracy of the final models.
|    | reference                                                                           | date     | key idea/summary                                                                                                                                                                      |
|----|-------------------------------------------------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Noisy Annotation Refinement for Object Detection](http://arxiv.org/abs/2110.10456) | 10/20/21 | The study proposes a method to train object detectors on noisy datasets by decoupling and correcting entangled annotation errors, achieving better performance than baseline methods. |
### <a id='category-annotation-quality-and-its-impact-on-model-performance'></a>Annotation Quality and Its Impact on Model Performance: 2 papers found.
Context: 
	Document 1: [Snippet]: «The presence of label noise often misleads the training of deep neural networks. Departing from the recent literature which largely assumes the label noise rate is only determined by the true label class, the errors in human-annotated labels are more likely to be dependent on the difficulty levels of tasks, resulting in settings with instance-dependent label noise.»
[_citation_number]: «2»
[Category]: «Annotation Quality and Its Impact on Model Performance»

	Document 2: [Snippet]: «Nearly all existing scene graph generation (SGG) models have overlooked the ground-truth annotation qualities of mainstream SGG datasets, i.e., they assume: 1) all the manually annotated positive samples are equally correct; 2) all the un-annotated negative samples are absolutely background. In this article, we argue that neither of the assumptions applies to SGG: there are numerous “noisy” ground-truth predicate labels that break these two assumptions and harm the training of unbiased SGG models.»
[_citation_number]: «4»
[Category]: «Annotation Quality and Its Impact on Model Performance»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T06:44:48+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2406.16966)\]. Further details \[[6](http://arxiv.org/abs/2212.01189)\]\[[7](http://arxiv.org/abs/1407.5155)\]\[[8](http://arxiv.org/abs/2401.14360)\]\[[9](http://arxiv.org/abs/1809.04019)\]\[[10](http://arxiv.org/abs/2410.09365)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In context learning (ICL) relies heavily on high quality demonstrations drawn
from large annotated corpora. Existing approaches detect noisy annotations by
ranking local perplexities, presuming that noisy samples yield higher
perplexities than their clean counterparts. However, this assumption breaks
down when the noise ratio is high and many demonstrations are flawed. We
reexamine the perplexity based paradigm for text generation under noisy
annotations, highlighting two sources of bias in perplexity: the annotation
itself and the domain specific knowledge inherent in large language models
(LLMs). To overcome these biases, we introduce a dual debiasing framework that
uses synthesized neighbors to explicitly correct perplexity estimates, yielding
a robust Sample Cleanliness Score. This metric uncovers absolute sample
cleanliness regardless of the overall corpus noise level. Extensive experiments
demonstrate our method's superior noise detection capabilities and show that
its final ICL performance is comparable to that of a fully clean demonstration
corpus. Moreover, our approach remains robust even when noise ratios are
extremely high.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2406.16966)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2012.11854)\]\[[7](http://arxiv.org/abs/1407.5155)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Annotation quality significantly impacts model performance, as evidenced by research highlighting the challenges posed by noisy annotations. Existing studies have shown that label noise, particularly instance-dependent noise, can mislead the training of deep neural networks, as errors in human-annotated labels are often dependent on task difficulty rather than just class distribution \[[2](http://arxiv.org/abs/2012.11854)\]. This insight contrasts with traditional assumptions that label noise is class-dependent, leading to ineffective strategies for handling noisy data \[[2](http://arxiv.org/abs/2012.11854)\]. Similarly, in scene graph generation (SGG), models often overlook the quality of ground-truth annotations, assuming all positive samples are equally correct and all un-annotated negatives are background \[[4](http://arxiv.org/abs/2207.13316)\]. However, this assumption is flawed, as numerous noisy predicate labels exist, which can distort training and lead to biased models \[[4](http://arxiv.org/abs/2207.13316)\]. These findings underscore the need for robust methods to detect and correct noisy annotations, ensuring that models are trained on reliable data.
|    | reference                                                                                                        | date     | key idea/summary                                                                                                                                                                                                                                                         |
|----|------------------------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [A Second-Order Approach to Learning with Instance-Dependent Label Noise](http://arxiv.org/abs/2012.11854)       | 12/22/20 | The paper addresses instance-dependent label noise in deep neural networks by proposing a second-order approach that leverages covariance terms to capture imbalances caused by heterogeneous noise, enabling the use of existing class-dependent label noise solutions. |
|  1 | [NICEST: Noisy Label Correction and Training for Robust Scene Graph Generation](http://arxiv.org/abs/2207.13316) | 07/27/22 | The paper introduces NICEST, a novel strategy to address noisy label issues in scene graph generation by detecting and correcting noisy samples and using a multi-teacher knowledge distillation training method, leading to improved performance and generalization.    |
### <a id='category-synthetic-data-generation-for-noisy-label-mitigation'></a>Synthetic Data Generation for Noisy Label Mitigation: 2 papers found.
In the context of synthetic data generation for noisy label mitigation, several approaches have been proposed to improve the robustness of deep learning models. One such method involves leveraging the early learning phase of neural networks, where clean samples are learned before mislabeled ones, and using this insight to create synthetic samples that help mitigate the impact of noisy labels \[[3](http://arxiv.org/abs/2406.16966)\]. This is achieved through a mixing strategy that aggregates original samples with their top-K nearest neighbors, using a mixture model to calculate weights based on per-sample loss distribution \[[3](http://arxiv.org/abs/2406.16966)\]. Additionally, methods have been developed to estimate soft targets by gradually correcting noisy labels, which leads to more accurate approximations of ground truth labels and better-separated clusters in learned representations \[[3](http://arxiv.org/abs/2406.16966)\]. Another approach focuses on text-only debiasing, where pre-trained vision-language models are adapted to reduce visual biases by utilizing a text-as-image training paradigm and generating balanced text datasets through large language models \[[10](http://arxiv.org/abs/2410.09365)\]. This method also introduces a Multi-Target Prediction task to prevent overfitting to text modality and improve robustness against biased information \[[10](http://arxiv.org/abs/2410.09365)\]. These techniques highlight the importance of synthetic data generation in addressing noisy labels and improving model generalization in real-world scenarios.
|    | reference                                                                                                | date     | key idea/summary                                                                                                                                                                                                           |
|----|----------------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Mitigating Noisy Supervision Using Synthetic Samples with Soft Labels](http://arxiv.org/abs/2406.16966) | 06/22/24 | The paper proposes a framework to mitigate the impact of noisy labels in deep learning by generating synthetic samples through a mixing strategy and estimating soft targets to improve generalization performance.        |
|  1 | [Debiasing Vison-Language Models with Text-Only Training](http://arxiv.org/abs/2410.09365)               | 10/12/24 | The TOD framework addresses the bias problem in pre-trained vision-language models by using a text-as-image training paradigm and a Multi-Target Prediction task to improve group robustness without requiring image data. |
### <a id='category-label-noise-in-reinforcement-learning'></a>Label Noise in Reinforcement Learning: 2 papers found.
Context: 
	Document 1: [Snippet]: «Recently, extensive studies in Reinforcement Learning have been carried out on the ability of transformers to adapt in-context to various environments and tasks. Current in-context RL methods are limited by their strict requirements for data, which needs to be generated by RL agents or labeled with actions from an optimal policy. In order to address this prevalent problem, we propose AD$^\varepsilon$, a new data acquisition approach that enables in-context Reinforcement Learning from noise-induced curriculum. We show that it is viable to construct a synthetic noise injection curriculum which helps to obtain learning histories. Moreover, we experimentally demonstrate that it is possible to alleviate the need for generation using optimal policies, with in-context RL still able to outperform the best suboptimal policy in a learning dataset by a 2x margin.»
[_citation_number]: «5»
[Category]: «Label Noise in Reinforcement Learning»

	Document 2: [Snippet]: «Maximum likelihood estimation (MLE) is the predominant algorithm for training text generation models. This paradigm relies on direct supervision examples, which is not applicable to many emerging applications, such as generating adversarial attacks or generating prompts to control language models. Reinforcement learning (RL) on the other hand offers a more flexible solution by allowing users to plug in arbitrary task metrics as reward. Yet previous RL algorithms for text generation, such as policy gradient (on-policy RL) and Q-learning (off-policy RL), are often notoriously inefficient or unstable to train due to the large sequence space and the sparse reward received only at the end of sequences. In this paper, we introduce a new RL formulation for text generation from the soft Q-learning (SQL) perspective. It enables us to draw from the latest RL advances, such as path consistency learning, to combine the best of on-/off-policy updates, and learn effectively from sparse reward. We apply the approach to a wide range of novel text generation tasks, including learning from noisy/negative examples, adversarial attacks, and prompt generation. Experiments show our approach consistently outperforms both task-specialized algorithms and the previous RL methods.»
[_citation_number]: «12»
[Category]: «Label Noise in Reinforcement Learning»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T06:44:48+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2406.16966)\]. Further details \[[6](http://arxiv.org/abs/2212.01189)\]\[[7](http://arxiv.org/abs/1407.5155)\]\[[8](http://arxiv.org/abs/2401.14360)\]\[[9](http://arxiv.org/abs/1809.04019)\]\[[10](http://arxiv.org/abs/2410.09365)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In context learning (ICL) relies heavily on high quality demonstrations drawn
from large annotated corpora. Existing approaches detect noisy annotations by
ranking local perplexities, presuming that noisy samples yield higher
perplexities than their clean counterparts. However, this assumption breaks
down when the noise ratio is high and many demonstrations are flawed. We
reexamine the perplexity based paradigm for text generation under noisy
annotations, highlighting two sources of bias in perplexity: the annotation
itself and the domain specific knowledge inherent in large language models
(LLMs). To overcome these biases, we introduce a dual debiasing framework that
uses synthesized neighbors to explicitly correct perplexity estimates, yielding
a robust Sample Cleanliness Score. This metric uncovers absolute sample
cleanliness regardless of the overall corpus noise level. Extensive experiments
demonstrate our method's superior noise detection capabilities and show that
its final ICL performance is comparable to that of a fully clean demonstration
corpus. Moreover, our approach remains robust even when noise ratios are
extremely high.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2406.16966)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2012.11854)\]\[[7](http://arxiv.org/abs/1407.5155)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Label noise in reinforcement learning has been a significant challenge, particularly in the context of in-context learning (ICL) where high-quality demonstrations are essential. Recent studies have focused on improving data acquisition and training methodologies to mitigate the effects of noisy annotations. For instance, AD$^\varepsilon$ introduces a novel approach to in-context reinforcement learning by leveraging synthetic noise injection to construct a curriculum that enhances learning histories without relying on optimal policy generation \[[5](http://arxiv.org/abs/2312.12275)\]. This aligns with broader efforts to develop more robust training paradigms that can handle sparse or noisy rewards. Similarly, in text generation, traditional methods like maximum likelihood estimation (MLE) face limitations when applied to tasks involving adversarial attacks or prompt generation, prompting the exploration of reinforcement learning (RL) as a more flexible alternative \[[12](http://arxiv.org/abs/2106.07704)\]. These works highlight the growing interest in combining RL techniques with advanced training strategies to address label noise and improve performance in complex, real-world scenarios.
|    | reference                                                                                                 | date     | key idea/summary                                                                                                                                                                                                                                                   |
|----|-----------------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Emergence of In-Context Reinforcement Learning from Noise Distillation](http://arxiv.org/abs/2312.12275) | 12/19/23 | AD$^	ext(\varepsilon)$ is a new data acquisition approach for in-context Reinforcement Learning that uses a synthetic noise injection curriculum to reduce reliance on optimal policy-generated data, achieving performance improvements over suboptimal policies. |
|  1 | [Efficient (Soft) Q-Learning for Text Generation with Limited Good Data](http://arxiv.org/abs/2106.07704) | 06/14/21 | This paper introduces a new reinforcement learning formulation for text generation based on soft Q-learning, enabling effective training from sparse rewards and outperforming existing methods across various text generation tasks.                              |
### <a id='category-generalization-challenges-with-noisy-data'></a>Generalization Challenges with Noisy Data: 6 papers found.
Generalization challenges with noisy data have been extensively studied, highlighting the adverse effects of noisy labels and biased datasets on model performance. Previous approaches often relied on label-based difficulty quantification, which can be undermined by the presence of noisy labels, as these are misclassified as difficult samples \[[1](http://arxiv.org/abs/2110.10456)\]. Additionally, denoising algorithms applied before debiasing have been shown to reduce the impact of bias-conflicting samples, thereby limiting the effectiveness of debiasing techniques \[[1](http://arxiv.org/abs/2110.10456)\]. In the context of text classification, industry datasets are often noisy, with both text and labels containing errors, which can lead to misleading performance metrics \[[4](http://arxiv.org/abs/2207.13316)\]. Similarly, in sentiment analysis, noisy texts pose significant challenges, as existing noise reduction methods have not been sufficiently effective in improving sentiment analysis accuracy \[[3](http://arxiv.org/abs/2406.16966)\]. In image processing, deep learning-based denoising methods struggle with out-of-distribution noise, prompting the development of noise translation frameworks that convert real-world noise into Gaussian noise for more effective denoising \[[5](http://arxiv.org/abs/2312.12275)\]. These challenges underscore the need for robust methods that address both noise and bias, such as the proposed DENEB approach, which integrates denoising after entropy-based debiasing to enhance generalization \[[1](http://arxiv.org/abs/2110.10456)\].
|    | reference                                                                                                                                    | date     | key idea/summary                                                                                                                                                                                                        |
|----|----------------------------------------------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Denoising after Entropy-based Debiasing A Robust Training Method for Dataset Bias with Noisy Labels](http://arxiv.org/abs/2212.01189)       | 12/01/22 | The study proposes a new debiasing approach called DENEB, which combines entropy-based debiasing with denoising algorithms to improve generalization by addressing noisy labels and bias in datasets.                   |
|  1 | [Sparse and Spurious: Dictionary Learning With Noise and Outliers](http://arxiv.org/abs/1407.5155)                                           | 07/18/14 | This paper presents a probabilistic analysis of sparse coding, showing that under certain conditions, it admits a local minimum around the reference dictionary, even in the presence of noise and outliers.            |
|  2 | [A Comparative Analysis of Noise Reduction Methods in Sentiment Analysis on Noisy Bangla Texts](http://arxiv.org/abs/2401.14360)             | 01/25/24 | This paper introduces a dataset of noisy Bangla texts and evaluates noise reduction methods for improving sentiment analysis, highlighting the need for better techniques in this domain.                               |
|  3 | [Training and Prediction Data Discrepancies: Challenges of Text Classification with Noisy, Historical Data](http://arxiv.org/abs/1809.04019) | 09/01/18 | The paper examines how performance metrics on noisy, historical industry datasets can still be useful for building prediction models that handle cleaner, future input data.                                            |
|  4 | [Learning to Translate Noise for Robust Image Denoising](http://arxiv.org/abs/2412.04727)                                                    | 12/06/24 | The paper proposes a noise translation framework that translates real-world noise into Gaussian noise for improved image denoising performance, achieving better robustness and generalizability than existing methods. |
|  5 | [FairFil: Contrastive Neural Debiasing Method for Pretrained Text Encoders](http://arxiv.org/abs/2103.06413)                                 | 03/11/21 | The paper introduces FairFil, a post-hoc neural debiasing method for pretrained sentence encoders that reduces social bias while preserving semantic information and maintaining performance on downstream tasks.       |
### <a id='category-data-augmentation-for-handling-noisy-annotations'></a>Data Augmentation for Handling Noisy Annotations: 2 papers found.
In the context of data augmentation for handling noisy annotations, recent research has focused on improving model robustness without sacrificing performance on well-formed text. One approach involves using data augmentation techniques that allow models to learn how to utilize or ignore orthographic information based on contextual relevance, leading to improved robustness to capitalization errors \[[14](http://arxiv.org/abs/1911.05241)\]. Similarly, another study addresses factual inconsistency in abstractive summarization by identifying biases such as language and irrelevancy biases and proposes a debiasing framework that employs counterfactual estimation strategies to mitigate these issues \[[11](http://arxiv.org/abs/2305.10736)\]. These methods demonstrate that data augmentation can be effectively leveraged to enhance model reliability in the presence of noisy or inconsistent data, while maintaining performance on clean, well-structured inputs.
|    | reference                                                                                                      | date     | key idea/summary                                                                                                                                                                                                                                                           |
|----|----------------------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Counterfactual Debiasing for Generating Factually Consistent Text Summaries](http://arxiv.org/abs/2305.10736) | 05/18/23 | The paper introduces CoFactSum, a debiasing framework that addresses factual inconsistency in abstractive text summarization by identifying and mitigating language and irrelevancy biases through counterfactual estimation strategies and a dynamic debiasing mechanism. |
|  1 | [Robustness to Capitalization Errors in Named Entity Recognition](http://arxiv.org/abs/1911.05241)             | 11/01/19 | The paper proposes a data augmentation approach to improve named entity recognizers' robustness to capitalization errors without compromising performance on well-formed text.                                                                                             |
### <a id='category-confidence-driven-inference-in-llms'></a>Confidence-Driven Inference in LLMs: 1 papers found.
Context: 
	Document 1: [Snippet]: «Large language models (LLMs) have shown high agreement with human raters across a variety of tasks, demonstrating potential to ease the challenges of human data collection. In computational social science (CSS), researchers are increasingly leveraging LLM annotations to complement slow and expensive human annotations. Still, guidelines for collecting and using LLM annotations, without compromising the validity of downstream conclusions, remain limited. We introduce Confidence-Driven Inference: a method that combines LLM annotations and LLM confidence indicators to strategically select which human annotations should be collected, with the goal of producing accurate statistical estimates and provably valid confidence intervals while reducing the number of human annotations needed. Our approach comes with safeguards against LLM annotations of poor quality, guaranteeing that the conclusions will be both valid and no less accurate than if we only relied on human annotations. We demonstrate the effectiveness of Confidence-Driven Inference over baselines in statistical estimation tasks across three CSS settings--text politeness, stance, and bias--reducing the needed number of human annotations by over 25% in each. Although we use CSS settings for demonstration, Confidence-Driven Inference can be used to estimate most standard quantities across a broad range of NLP problems.»
[_citation_number]: «15»
[Category]: «Confidence-Driven Inference in LLMs»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T06:44:48+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2406.16966)\]. Further details \[[6](http://arxiv.org/abs/2212.01189)\]\[[7](http://arxiv.org/abs/1407.5155)\]\[[8](http://arxiv.org/abs/2401.14360)\]\[[9](http://arxiv.org/abs/1809.04019)\]\[[10](http://arxiv.org/abs/2410.09365)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In context learning (ICL) relies heavily on high quality demonstrations drawn
from large annotated corpora. Existing approaches detect noisy annotations by
ranking local perplexities, presuming that noisy samples yield higher
perplexities than their clean counterparts. However, this assumption breaks
down when the noise ratio is high and many demonstrations are flawed. We
reexamine the perplexity based paradigm for text generation under noisy
annotations, highlighting two sources of bias in perplexity: the annotation
itself and the domain specific knowledge inherent in large language models
(LLMs). To overcome these biases, we introduce a dual debiasing framework that
uses synthesized neighbors to explicitly correct perplexity estimates, yielding
a robust Sample Cleanliness Score. This metric uncovers absolute sample
cleanliness regardless of the overall corpus noise level. Extensive experiments
demonstrate our method's superior noise detection capabilities and show that
its final ICL performance is comparable to that of a fully clean demonstration
corpus. Moreover, our approach remains robust even when noise ratios are
extremely high.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2406.16966)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2012.11854)\]\[[7](http://arxiv.org/abs/1407.5155)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Confidence-Driven Inference in LLMs represents a significant advancement in the use of large language models for data annotation and statistical estimation. This approach leverages both LLM annotations and confidence indicators to strategically decide when human annotations are necessary, aiming to produce accurate results while minimizing human input \[[15](http://arxiv.org/abs/2408.15204)\]. By incorporating confidence metrics, the method introduces safeguards against poor-quality annotations, ensuring that the final conclusions are both valid and as accurate as those derived solely from human annotations \[[15](http://arxiv.org/abs/2408.15204)\]. This is particularly important in computational social science, where LLMs are increasingly used to complement traditional human annotation methods due to their speed and cost-effectiveness \[[15](http://arxiv.org/abs/2408.15204)\]. The framework has been tested across various tasks, including text politeness, stance, and bias, where it has shown the ability to reduce the number of human annotations required by over 25% without compromising accuracy \[[15](http://arxiv.org/abs/2408.15204)\]. The approach is not limited to social science applications and can be extended to a wide range of NLP tasks, offering a scalable solution for improving the efficiency and reliability of data annotation processes.
|    | reference                                                                                             | date     | key idea/summary                                                                                                                                                                                                                        |
|----|-------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Can Unconfident LLM Annotations Be Used for Confident Conclusions?](http://arxiv.org/abs/2408.15204) | 08/27/24 | Confidence-Driven Inference is a method that combines LLM annotations and confidence indicators to reduce the need for human annotations while ensuring valid and accurate statistical estimates in computational social science tasks. |
### <a id='category-annotation-reliability-in-downstream-tasks'></a>Annotation Reliability in Downstream Tasks: 1 papers found.
Context: 
	Document 1: [Snippet]: «The annotation of textual information is a fundamental activity in Linguistics and Computational Linguistics. This article presents various observations on annotations. It approaches the topic from several angles including Hypertext, Computational Linguistics and Language Technology, Artificial Intelligence and Open Science. Annotations can be examined along different dimensions. In terms of complexity, they can range from trivial to highly sophisticated, in terms of maturity from experimental to standardised. Annotations can be annotated themselves using more abstract annotations. Primary research data such as, e.g., text documents can be annotated on different layers concurrently, which are independent but can be exploited using multi-layer querying. Standards guarantee interoperability and reusability of data sets. The chapter concludes with four final observations, formulated as research questions or rather provocative remarks on the current state of annotation research.»
[_citation_number]: «16»
[Category]: «Annotation Reliability in Downstream Tasks»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T06:44:48+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2406.16966)\]. Further details \[[6](http://arxiv.org/abs/2212.01189)\]\[[7](http://arxiv.org/abs/1407.5155)\]\[[8](http://arxiv.org/abs/2401.14360)\]\[[9](http://arxiv.org/abs/1809.04019)\]\[[10](http://arxiv.org/abs/2410.09365)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In context learning (ICL) relies heavily on high quality demonstrations drawn
from large annotated corpora. Existing approaches detect noisy annotations by
ranking local perplexities, presuming that noisy samples yield higher
perplexities than their clean counterparts. However, this assumption breaks
down when the noise ratio is high and many demonstrations are flawed. We
reexamine the perplexity based paradigm for text generation under noisy
annotations, highlighting two sources of bias in perplexity: the annotation
itself and the domain specific knowledge inherent in large language models
(LLMs). To overcome these biases, we introduce a dual debiasing framework that
uses synthesized neighbors to explicitly correct perplexity estimates, yielding
a robust Sample Cleanliness Score. This metric uncovers absolute sample
cleanliness regardless of the overall corpus noise level. Extensive experiments
demonstrate our method's superior noise detection capabilities and show that
its final ICL performance is comparable to that of a fully clean demonstration
corpus. Moreover, our approach remains robust even when noise ratios are
extremely high.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2406.16966)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2012.11854)\]\[[7](http://arxiv.org/abs/1407.5155)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Annotation reliability in downstream tasks is a critical area of research, particularly in the context of computational linguistics and language technology. The reliability of annotations directly impacts the performance of models trained on annotated data, as noisy or inconsistent annotations can introduce biases and reduce the effectiveness of downstream applications \[[16](http://arxiv.org/abs/2004.10283)\]. This issue is especially relevant in scenarios where annotations are used to train large language models (LLMs) or to support context learning (ICL) tasks, where high-quality demonstrations are essential \[[16](http://arxiv.org/abs/2004.10283)\]. The challenge lies in distinguishing between annotations that are inherently noisy and those that are affected by the domain-specific knowledge embedded in LLMs, which can further distort the evaluation of annotation quality \[[16](http://arxiv.org/abs/2004.10283)\]. Existing methods often rely on perplexity-based metrics to detect noisy annotations, but these approaches can fail under high noise conditions, where the assumption that noisy samples yield higher perplexity than clean ones breaks down \[[16](http://arxiv.org/abs/2004.10283)\]. This highlights the need for more robust frameworks that account for both annotation quality and model-specific biases, ensuring that downstream tasks benefit from reliable and consistent annotations.
|    | reference                                                      | date     | key idea/summary                                                                                                                                                                                                                                                                       |
|----|----------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Observations on Annotations](http://arxiv.org/abs/2004.10283) | 04/21/20 | The article discusses the multifaceted nature of annotations in linguistics and computational linguistics, highlighting their complexity, maturity, and potential for multi-layer querying, while emphasizing the role of standards in ensuring data interoperability and reusability. |
