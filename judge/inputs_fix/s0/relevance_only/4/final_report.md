## Related Works

The problem of learning from noisy labels has been extensively studied in recent years, with a focus on both theoretical understanding and practical solutions. Early approaches treated label noise as statistical outliers, proposing techniques such as importance re-weighting and bootstrapping to alleviate the problem \[[11](http://arxiv.org/abs/1703.02391)\]. However, these methods often fail to account for the complex structure of real-world label noise, which can exhibit multimodal characteristics and be influenced by the difficulty of the task \[[11](http://arxiv.org/abs/1703.02391)\]. 

Recent work has shifted toward more sophisticated frameworks that explicitly model the relationship between noisy and clean labels. For instance, a probabilistic model was introduced to show that sparse coding admits a local minimum around the reference dictionary generating the signals, even in the presence of noise and outliers \[[14](http://arxiv.org/abs/1407.5155)\]. This theoretical foundation has inspired a range of practical methods, including those that leverage semi-supervised learning to dynamically divide training data into clean and noisy subsets \[[5](http://arxiv.org/abs/2002.07394)\]. The DivideMix framework, for example, uses a mixture model to estimate per-sample loss distributions and trains two diverged networks to avoid confirmation bias \[[5](http://arxiv.org/abs/2002.07394)\].

Another line of research focuses on correcting noisy annotations by generating high-quality synthetic samples with soft labels. This approach aims to mitigate the impact of noisy labels during training by creating new samples that better represent the underlying data distribution \[[3](http://arxiv.org/abs/2406.16966)\]. Similarly, the NICEST framework addresses noisy labels in scene graph generation by detecting and correcting noisy predicate labels through a combination of clustering and knowledge distillation techniques \[[6](http://arxiv.org/abs/2207.13316)\]. This method not only improves the quality of the labels but also enhances the robustness of the model during training.

The challenge of learning from noisy labels is further compounded by the presence of human reporting bias, where annotators may selectively report certain aspects of an image while ignoring others \[[10](http://arxiv.org/abs/1512.06974)\]. This bias can lead to inconsistent and incomplete annotations, which are difficult to correct without additional domain knowledge. To address this, researchers have proposed algorithms that decouple human reporting bias from the visually grounded labels, enabling the learning of more accurate classifiers \[[10](http://arxiv.org/abs/1512.06974)\].

In addition to these methods, there has been growing interest in using loss correction techniques to make deep neural networks robust to label noise. A theoretically grounded approach was proposed that involves estimating the probability of each class being corrupted into another, allowing for the correction of the loss function during training \[[12](http://arxiv.org/abs/1609.03683)\]. This method has been validated on a variety of datasets, including MNIST, IMDB, CIFAR-10, and CIFAR-100, demonstrating its effectiveness in reducing label noise \[[12](http://arxiv.org/abs/1609.03683)\].

Finally, recent studies have explored the use of in-context learning (ICL) to improve the performance of large language models in the presence of noisy annotations. ICL leverages examples of the input-label relationship to make predictions, but it is not without limitations. While ICL can learn truly novel tasks in-context, it often struggles to fully overcome prediction preferences acquired from pre-training data \[[15](http://arxiv.org/abs/2307.12375)\].

1. \[[11](http://arxiv.org/abs/1703.02391)\] Learning from Noisy Labels with Distillation  
2. \[[5](http://arxiv.org/abs/2002.07394)\] DivideMix: Learning with Noisy Labels as Semi-supervised Learning  
3. \[[3](http://arxiv.org/abs/2406.16966)\] Mitigating Noisy Supervision Using Synthetic Samples with Soft Labels  
4. \[[6](http://arxiv.org/abs/2207.13316)\] NICEST: Noisy Label Correction and Training for Robust Scene Graph Generation  
5. \[[10](http://arxiv.org/abs/1512.06974)\] Seeing through the Human Reporting Bias: Visual Classifiers from Noisy Human-Centric Labels  
6. \[[12](http://arxiv.org/abs/1609.03683)\] Making Deep Neural Networks Robust to Label Noise: A Loss Correction Approach  
7. \[[15](http://arxiv.org/abs/2307.12375)\] In-Context Learning Learns Label Relationships but Is Not Conventional Learning
## Research papers
### Outline
- [Label Noise Modeling and Theoretical Foundations [7 papers]](#category-label-noise-modeling-and-theoretical-foundations)
- [Synthetic Sample Generation for Noise Mitigation [1 papers]](#category-synthetic-sample-generation-for-noise-mitigation)
- [Semi-Supervised Learning for Noisy Label Correction [1 papers]](#category-semi-supervised-learning-for-noisy-label-correction)
- [Probabilistic Frameworks for Label Noise Handling [2 papers]](#category-probabilistic-frameworks-for-label-noise-handling)
- [In-Context Learning and Its Limitations with Noisy Data [2 papers]](#category-in-context-learning-and-its-limitations-with-noisy-data)
- [Human Reporting Bias and Its Impact on Annotations [1 papers]](#category-human-reporting-bias-and-its-impact-on-annotations)
- [Loss Correction Techniques for Robust Training [1 papers]](#category-loss-correction-techniques-for-robust-training)
- [Evaluation Metrics for Noisy Label Detection [1 papers]](#category-evaluation-metrics-for-noisy-label-detection)
- [Robustness to High Noise Ratios in Training [1 papers]](#category-robustness-to-high-noise-ratios-in-training)

### <a id='category-label-noise-modeling-and-theoretical-foundations'></a>Label Noise Modeling and Theoretical Foundations: 7 papers found.
The category "Label Noise Modeling and Theoretical Foundations" encompasses a range of studies addressing the challenges posed by noisy labels in machine learning tasks, particularly in object detection, image classification, and scene graph generation. These works highlight the limitations of traditional approaches that assume label noise is either class-dependent or uniformly distributed, emphasizing the need for more nuanced models that account for instance-dependent noise patterns \[[2](http://arxiv.org/abs/2012.11854)\]. For instance, some studies demonstrate that real-world label noise often follows an instance-dependent pattern, which is more complex and harder to model than class-dependent noise \[[3](http://arxiv.org/abs/2406.16966)\]. This has led to the development of advanced techniques such as second-order statistical methods that leverage covariance terms between noise rates and Bayes optimal labels to better capture the imbalances caused by noisy data \[[2](http://arxiv.org/abs/2012.11854)\]. Additionally, there is a growing emphasis on creating controllable and moderate-sized real-world noisy datasets with ground-truth labels, enabling more rigorous theoretical analysis and benchmarking of noise handling methods \[[3](http://arxiv.org/abs/2406.16966)\]. Furthermore, some works propose novel strategies for correcting noisy annotations, such as decoupling entangled noises in object detection \[[1](http://arxiv.org/abs/2110.10456)\] and using knowledge distillation to train models on noisy data \[[4](http://arxiv.org/abs/2110.12088)\]. These approaches aim to improve the robustness of models by explicitly addressing the biases introduced by noisy labels, either through statistical modeling, data augmentation, or advanced training strategies \[[5](http://arxiv.org/abs/2002.07394)\]. Overall, this category reflects a shift towards more sophisticated and realistic modeling of label noise, driven by the increasing availability of large-scale, noisy datasets and the need for reliable methods to handle such data in practical applications.
|    | reference                                                                                                              | date     | key idea/summary                                                                                                                                                                                                                                                                                |
|----|------------------------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Noisy Annotation Refinement for Object Detection](http://arxiv.org/abs/2110.10456)                                    | 10/20/21 | The study proposes a method to train object detectors on noisy datasets by decoupling and correcting entangled annotation errors, achieving better performance than baseline methods.                                                                                                           |
|  1 | [A Second-Order Approach to Learning with Instance-Dependent Label Noise](http://arxiv.org/abs/2012.11854)             | 12/22/20 | The paper addresses instance-dependent label noise in deep neural networks by proposing a second-order approach that leverages covariance terms to capture imbalances caused by heterogeneous noise, enabling the use of existing class-dependent label noise solutions.                        |
|  2 | [Learning with Noisy Labels Revisited: A Study Using Real-World Human Annotations](http://arxiv.org/abs/2110.12088)    | 10/22/21 | This work introduces two new benchmark datasets, CIFAR-10N and CIFAR-100N, containing human-annotated real-world noisy labels to better understand and address real-world label noise, highlighting the instance-dependent nature of such noise and its challenges compared to synthetic noise. |
|  3 | [NICEST: Noisy Label Correction and Training for Robust Scene Graph Generation](http://arxiv.org/abs/2207.13316)       | 07/27/22 | The paper introduces NICEST, a novel strategy to address noisy label issues in scene graph generation by detecting and correcting noisy samples and using a multi-teacher knowledge distillation training method, leading to improved performance and generalization.                           |
|  4 | [CleanNet: Transfer Learning for Scalable Image Classifier Training with Label Noise](http://arxiv.org/abs/1711.07131) | 11/20/17 | CleanNet is a joint neural embedding network that reduces the need for human supervision in label noise cleaning by transferring knowledge from verified classes to others, achieving significant performance gains with minimal manual verification.                                           |
|  5 | [Learning from Noisy Labels with Distillation](http://arxiv.org/abs/1703.02391)                                        | 03/07/17 | The paper proposes a unified distillation framework that leverages side information, such as a small clean dataset and label relations in a knowledge graph, to effectively learn from noisy labels in practical settings.                                                                      |
|  6 | [Sparse and Spurious: Dictionary Learning With Noise and Outliers](http://arxiv.org/abs/1407.5155)                     | 07/18/14 | This paper presents a probabilistic analysis of sparse coding, showing that under certain conditions, it admits a local minimum around the reference dictionary, even in the presence of noise and outliers.                                                                                    |
### <a id='category-synthetic-sample-generation-for-noise-mitigation'></a>Synthetic Sample Generation for Noise Mitigation: 1 papers found.
Context: 
	Document 1: [Category]: «Synthetic Sample Generation for Noise Mitigation»
[Snippet]: «Noisy labels are ubiquitous in real-world datasets, especially in the large-scale ones derived from crowdsourcing and web searching. It is challenging to train deep neural networks with noisy datasets since the networks are prone to overfitting the noisy labels during training, resulting in poor generalization performance. During an early learning phase, deep neural networks have been observed to fit the clean samples before memorizing the mislabeled samples. In this paper, we dig deeper into the representation distributions in the early learning phase and find that, regardless of their noisy labels, learned representations of images from the same category still congregate together. Inspired by it, we propose a framework that trains the model with new synthetic samples to mitigate the impact of noisy labels. Specifically, we propose a mixing strategy to create the synthetic samples by aggregating original samples with their top-K nearest neighbours, wherein the weights are calculated using a mixture model learning from the per-sample loss distribution. To enhance the performance in the presence of extreme label noise, we estimate the soft targets by gradually correcting the noisy labels. Furthermore, we demonstrate that the estimated soft targets yield a more accurate approximation to ground truth labels and the proposed method produces a superior quality of learned representations with more separated and clearly bounded clusters. The extensive experiments in two benchmarks (CIFAR-10 and CIFAR-100) and two larg-scale real-world datasets (Clothing1M and Webvision) demonstrate that our approach outperforms the state-of-the-art methods and robustness of the learned representation.»
[_citation_number]: «3»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T06:44:48+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2406.16966)\]. Further details \[[6](http://arxiv.org/abs/2207.13316)\]\[[7](http://arxiv.org/abs/1706.00038)\]\[[8](http://arxiv.org/abs/1711.07131)\]\[[9](http://arxiv.org/abs/2312.12275)\]\[[10](http://arxiv.org/abs/1512.06974)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In context learning (ICL) relies heavily on high quality demonstrations drawn
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2406.16966)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2012.11854)\]\[[7](http://arxiv.org/abs/1706.00038)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer:  
The category of synthetic sample generation for noise mitigation addresses the challenge of training deep neural networks with noisy labels, which are common in large-scale datasets derived from crowdsourcing and web searching \[[3](http://arxiv.org/abs/2406.16966)\]. These noisy labels can lead to overfitting and poor generalization, as models may memorize incorrect labels rather than learning meaningful patterns \[[3](http://arxiv.org/abs/2406.16966)\]. Research in this area has focused on leveraging the early learning phase, where models tend to fit clean samples before being influenced by mislabeled ones \[[3](http://arxiv.org/abs/2406.16966)\]. One key insight is that representations of images from the same category still cluster together, even with noisy labels, suggesting that meaningful structure can be preserved \[[3](http://arxiv.org/abs/2406.16966)\]. Building on this, the proposed framework generates synthetic samples by combining original samples with their top-K nearest neighbors, using a mixture model to assign weights based on per-sample loss distribution \[[3](http://arxiv.org/abs/2406.16966)\]. This approach aims to enhance robustness against extreme label noise by estimating soft targets that better approximate ground truth labels \[[3](http://arxiv.org/abs/2406.16966)\]. The effectiveness of this method is validated through experiments on benchmark datasets such as CIFAR-10, CIFAR-100, Clothing1M, and Webvision, demonstrating superior performance compared to state-of-the-art methods \[[3](http://arxiv.org/abs/2406.16966)\].
|    | reference                                                                                                | date     | key idea/summary                                                                                                                                                                                                    |
|----|----------------------------------------------------------------------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Mitigating Noisy Supervision Using Synthetic Samples with Soft Labels](http://arxiv.org/abs/2406.16966) | 06/22/24 | The paper proposes a framework to mitigate the impact of noisy labels in deep learning by generating synthetic samples through a mixing strategy and estimating soft targets to improve generalization performance. |
### <a id='category-semi-supervised-learning-for-noisy-label-correction'></a>Semi-Supervised Learning for Noisy Label Correction: 1 papers found.
Context: 
	Document 1: [Category]: «Semi-Supervised Learning for Noisy Label Correction»
[Snippet]: «Deep neural networks are known to be annotation-hungry. Numerous efforts have been devoted to reducing the annotation cost when learning with deep networks. Two prominent directions include learning with noisy labels and semi-supervised learning by exploiting unlabeled data. In this work, we propose DivideMix, a novel framework for learning with noisy labels by leveraging semi-supervised learning techniques. In particular, DivideMix models the per-sample loss distribution with a mixture model to dynamically divide the training data into a labeled set with clean samples and an unlabeled set with noisy samples, and trains the model on both the labeled and unlabeled data in a semi-supervised manner. To avoid confirmation bias, we simultaneously train two diverged networks where each network uses the dataset division from the other network. During the semi-supervised training phase, we improve the MixMatch strategy by performing label co-refinement and label co-guessing on labeled and unlabeled samples, respectively. Experiments on multiple benchmark datasets demonstrate substantial improvements over state-of-the-art methods. Code is available at this https URL .»
[_citation_number]: «5»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T06:44:48+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2406.16966)\]. Further details \[[6](http://arxiv.org/abs/2207.13316)\]\[[7](http://arxiv.org/abs/1706.00038)\]\[[8](http://arxiv.org/abs/1711.07131)\]\[[9](http://arxiv.org/abs/2312.12275)\]\[[10](http://arxiv.org/abs/1512.06974)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In context learning (ICL) relies heavily on high quality demonstrations drawn
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2406.16966)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2012.11854)\]\[[7](http://arxiv.org/abs/1706.00038)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The category "Semi-Supervised Learning for Noisy Label Correction" focuses on addressing the challenges of training deep neural networks with noisy or unreliable labels, which are common in real-world datasets \[[5](http://arxiv.org/abs/2002.07394)\]. Traditional supervised learning methods require large amounts of clean labeled data, which is often costly and impractical to obtain. To mitigate this, researchers have explored semi-supervised learning techniques that leverage unlabeled data to improve model performance \[[5](http://arxiv.org/abs/2002.07394)\]. One notable approach is DivideMix, which introduces a novel framework that dynamically partitions training data into clean and noisy subsets using a mixture model to estimate per-sample loss distributions \[[5](http://arxiv.org/abs/2002.07394)\]. This enables the model to train on both labeled and unlabeled data in a semi-supervised manner, improving robustness against label noise. To further reduce confirmation bias, DivideMix employs two diverged networks that iteratively refine each other's dataset divisions, enhancing the overall learning process \[[5](http://arxiv.org/abs/2002.07394)\]. Additionally, the method incorporates label co-refinement and co-guessing strategies, improving the accuracy of predictions on both labeled and unlabeled samples \[[5](http://arxiv.org/abs/2002.07394)\]. These innovations demonstrate the potential of semi-supervised learning in effectively handling noisy labels, offering a promising direction for reducing annotation costs while maintaining model performance.
|    | reference                                                                                            | date     | key idea/summary                                                                                                                                                                                                                                     |
|----|------------------------------------------------------------------------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [DivideMix: Learning with Noisy Labels as Semi-supervised Learning](http://arxiv.org/abs/2002.07394) | 02/18/20 | DivideMix is a novel framework that reduces annotation cost by leveraging semi-supervised learning and mixture models to dynamically divide training data into clean and noisy sets, while avoiding confirmation bias through dual network training. |
### <a id='category-probabilistic-frameworks-for-label-noise-handling'></a>Probabilistic Frameworks for Label Noise Handling: 2 papers found.
Context: 
	Document 1: [Category]: «Probabilistic Frameworks for Label Noise Handling»
[Snippet]: «Collecting large training datasets, annotated with high-quality labels, is costly and time-consuming. This paper proposes a novel framework for training deep convolutional neural networks from noisy labeled datasets that can be obtained cheaply. The problem is formulated using an undirected graphical model that represents the relationship between noisy and clean labels, trained in a semi-supervised setting. In our formulation, the inference over latent clean labels is tractable and is regularized during training using auxiliary sources of information. The proposed model is applied to the image labeling problem and is shown to be effective in labeling unseen images as well as reducing label noise in training on CIFAR-10 and MS COCO datasets.»
[_citation_number]: «7»

	Document 2: [Category]: «Probabilism Frameworks for Label Noise Handling»
[Snippet]: «Improperly constructed datasets can result in inaccurate inferences. For instance, models trained on biased datasets perform poorly in terms of generalization (i.e., dataset bias). Recent debiasing techniques have successfully achieved generalization performance by underestimating easy-to-learn samples (i.e., bias-aligned samples) and highlighting difficult-to-learn samples (i.e., bias-conflicting samples). However, these techniques may fail owing to noisy labels, because the trained model recognizes noisy labels as difficult-to-learn and thus highlights them. In this study, we find that earlier approaches that used the provided labels to quantify difficulty could be affected by the small proportion of noisy labels. Furthermore, we find that running denoising algorithms before debiasing is ineffective because denoising algorithms reduce the impact of difficult-to-learn samples, including valuable bias-conflicting samples. Therefore, we propose an approach called denoising after entropy-based debiasing, i.e., DENEB, which has three main stages. (1) The prejudice model is trained by emphasizing (bias-aligned, clean) samples, which are selected using a Gaussian Mixture Model. (2) Using the per-sample entropy from the output of the prejudice model, the sampling probability of each sample that is proportional to the entropy is computed. (3) The final model is trained using existing denoising algorithms with the mini-batches constructed by following the computed sampling probability. Compared to existing debiasing and denoising algorithms, our method achieves better debiasing performance on multiple benchmarks.»
[_citation_number]: «13»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T06:44:48+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2406.16966)\]. Further details \[[6](http://arxiv.org/abs/2207.13316)\]\[[7](http://arxiv.org/abs/1706.00038)\]\[[8](http://arxiv.org/abs/1711.07131)\]\[[9](http://arxiv.org/abs/2312.12275)\]\[[10](http://arxiv.org/abs/1512.06974)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In context learning (ICL) relies heavily on high quality demonstrations drawn
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2406.16966)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2012.11854)\]\[[7](http://arxiv.org/abs/1706.00038)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Probabilistic frameworks for label noise handling have gained significant attention in recent years due to their ability to effectively manage noisy datasets in machine learning tasks. These frameworks often rely on modeling the relationship between noisy and clean labels, leveraging graphical models to infer latent clean labels from observed noisy ones \[[7](http://arxiv.org/abs/1706.00038)\]. For instance, one approach involves training deep convolutional neural networks using a semi-supervised setting, where the inference over latent clean labels is tractable and regularized using auxiliary information \[[7](http://arxiv.org/abs/1706.00038)\]. This method has shown effectiveness in tasks such as image labeling, particularly on benchmark datasets like CIFAR-10 and MS COCO, where label noise is prevalent \[[7](http://arxiv.org/abs/1706.00038)\]. Another study addresses the challenges of dataset bias and noisy labels by proposing a method called DENEB, which involves three stages: training a prejudice model on bias-aligned samples, computing sampling probabilities based on per-sample entropy, and finally training a denoising model using these probabilities \[[13](http://arxiv.org/abs/2212.01189)\]. This approach aims to mitigate the impact of noisy labels by first debiasing the dataset and then applying denoising techniques, leading to improved generalization performance \[[13](http://arxiv.org/abs/2212.01189)\]. These methods highlight the importance of addressing label noise through probabilistic modeling, emphasizing the need for robust frameworks that can handle both bias and noise in training data.
|    | reference                                                                                                                              | date     | key idea/summary                                                                                                                                                                                         |
|----|----------------------------------------------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Toward Robustness against Label Noise in Training Deep Discriminative Neural Networks](http://arxiv.org/abs/1706.00038)               | 05/31/17 | The paper introduces a novel framework for training deep convolutional neural networks using noisy labeled datasets, effectively reducing label noise and improving performance on image labeling tasks. |
|  1 | [Denoising after Entropy-based Debiasing A Robust Training Method for Dataset Bias with Noisy Labels](http://arxiv.org/abs/2212.01189) | 12/01/22 | The study proposes a new debiasing approach called DENEB, which combines entropy-based debiasing with denoising algorithms to improve generalization by addressing noisy labels and bias in datasets.    |
### <a id='category-in-context-learning-and-its-limitations-with-noisy-data'></a>In-Context Learning and Its Limitations with Noisy Data: 2 papers found.
Context: 
	Document 1: [Category]: «In-Context Learning and Its Limitations with Noisy Data»
[Snippet]: «Recently, extensive studies in Reinforcement Learning have been carried out on the ability of transformers to adapt in-context to various environments and tasks. Current in-context RL methods are limited by their strict requirements for data, which needs to be generated by RL agents or labeled with actions from an optimal policy. In order to address this prevalent problem, we propose AD$^\varepsilon$, a new data acquisition approach that enables in-context Reinforcement Learning from noise-induced curriculum. We show that it is viable to construct a synthetic noise injection curriculum which helps to obtain learning histories. Moreover, we experimentally demonstrate that it is possible to alleviate the need for generation using optimal policies, with in-context RL still able to outperform the best suboptimal policy in a learning dataset by a 2x margin.»
[_citation_number]: «9»

	Document 2: [Category]: «In-Context Learning and Its Limitations with Noisy Data»
[Snippet]: «The predictions of Large Language Models (LLMs) on downstream tasks often improve significantly when including examples of the input--label relationship in the context. However, there is currently no consensus about how this in-context learning (ICL) ability of LLMs works. For example, while Xie et al. (2021) liken ICL to a general-purpose learning algorithm, Min et al. (2022) argue ICL does not even learn label relationships from in-context examples. In this paper, we provide novel insights into how ICL leverages label information, revealing both capabilities and limitations. To ensure we obtain a comprehensive picture of ICL behavior, we study probabilistic aspects of ICL predictions and thoroughly examine the dynamics of ICL as more examples are provided. Our experiments show that ICL predictions almost always depend on in-context labels and that ICL can learn truly novel tasks in-context. However, we also find that ICL struggles to fully overcome prediction preferences acquired from pre-training data and, further, that ICL does not consider all in-context information equally.»
[_citation_number]: «15»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T06:44:48+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2406.16966)\]. Further details \[[6](http://arxiv.org/abs/2207.13316)\]\[[7](http://arxiv.org/abs/1706.00038)\]\[[8](http://arxiv.org/abs/1711.07131)\]\[[9](http://arxiv.org/abs/2312.12275)\]\[[10](http://arxiv.org/abs/1512.06974)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In context learning (ICL) relies heavily on high quality demonstrations drawn
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2406.16966)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2012.11854)\]\[[7](http://arxiv.org/abs/1706.00038)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Recent studies on in-context learning (ICL) have highlighted both its potential and its limitations, particularly in the presence of noisy data. Researchers have explored how ICL leverages in-context examples to improve downstream task performance, but there is still no consensus on the underlying mechanisms \[[15](http://arxiv.org/abs/2307.12375)\]. Some argue that ICL can learn truly novel tasks in-context, relying heavily on in-context labels \[[15](http://arxiv.org/abs/2307.12375)\], while others challenge this view, suggesting that ICL may not fully overcome pre-training biases or consider all in-context information equally \[[15](http://arxiv.org/abs/2307.12375)\]. Similarly, in the field of reinforcement learning, in-context methods face challenges due to their strict data requirements, often necessitating labeled data from optimal policies \[[9](http://arxiv.org/abs/2312.12275)\]. To address these limitations, new approaches such as AD$^\varepsilon$ have been proposed, which introduce synthetic noise injection curricula to enable learning from noisy data without relying on optimal policy generation \[[9](http://arxiv.org/abs/2312.12275)\]. These developments underscore the ongoing efforts to improve the robustness and effectiveness of ICL in real-world scenarios where data quality may be compromised.
|    | reference                                                                                                          | date     | key idea/summary                                                                                                                                                                                                                                                   |
|----|--------------------------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Emergence of In-Context Reinforcement Learning from Noise Distillation](http://arxiv.org/abs/2312.12275)          | 12/19/23 | AD$^	ext(\varepsilon)$ is a new data acquisition approach for in-context Reinforcement Learning that uses a synthetic noise injection curriculum to reduce reliance on optimal policy-generated data, achieving performance improvements over suboptimal policies. |
|  1 | [In-Context Learning Learns Label Relationships but Is Not Conventional Learning](http://arxiv.org/abs/2307.12375) | 07/23/23 | This paper provides novel insights into how in-context learning (ICL) in large language models leverages label information, revealing both its capabilities and limitations through probabilistic analysis and experiments.                                        |
### <a id='category-human-reporting-bias-and-its-impact-on-annotations'></a>Human Reporting Bias and Its Impact on Annotations: 1 papers found.
Context: 
	Document 1: [Category]: «Human Reporting Bias and Its Impact on Annotations»
[Snippet]: «When human annotators are given a choice about what to label in an image, they apply their own subjective judgments on what to ignore and what to mention. We refer to these noisy "human-centric" annotations as exhibiting human reporting bias. Examples of such annotations include image tags and keywords found on photo sharing sites, or in datasets containing image captions. In this paper, we use these noisy annotations for learning visually correct image classifiers. Such annotations do not use consistent vocabulary, and miss a significant amount of the information present in an image, however, we demonstrate that the noise in these annotations exhibits structure and can be modeled. We propose an algorithm to decouple the human reporting bias from the correct visually grounded labels. Our results are highly interpretable for reporting "what's in the image" versus "what's worth saying." We demonstrate the algorithm's efficacy along a variety of metrics and datasets, including MS COCO and Yahoo Flickr 100M. We show significant improvements over traditional algorithms for both image classification and image captioning, doubling the performance of existing methods in some cases.»
[_citation_number]: «10»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T06:44:48+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2406.16966)\]. Further details \[[6](http://arxiv.org/abs/2207.13316)\]\[[7](http://arxiv.org/abs/1706.00038)\]\[[8](http://arxiv.org/abs/1711.07131)\]\[[9](http://arxiv.org/abs/2312.12275)\]\[[10](http://arxiv.org/abs/1512.06974)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In context learning (ICL) relies heavily on high quality demonstrations drawn
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2406.16966)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2012.11854)\]\[[7](http://arxiv.org/abs/1706.00038)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer:  
Human reporting bias, as highlighted in the context of noisy annotations, refers to the subjective judgments made by human annotators when labeling images, leading to inconsistent and incomplete representations of visual content \[[10](http://arxiv.org/abs/1512.06974)\]. This phenomenon is particularly evident in image tagging and captioning tasks, where annotators may prioritize certain elements over others based on personal interpretation, resulting in a lack of standardized vocabulary and significant omissions of visual information \[[10](http://arxiv.org/abs/1512.06974)\]. Such biases can undermine the reliability of annotated datasets, especially in large-scale corpora like MS COCO and Yahoo Flickr 100M, where the diversity of human input introduces variability \[[10](http://arxiv.org/abs/1512.06974)\]. Addressing this issue requires algorithms capable of distinguishing between the inherent visual content of an image and the biases introduced by human annotators \[[10](http://arxiv.org/abs/1512.06974)\]. The challenge lies in developing methods that can effectively decouple these biases, ensuring that the resulting annotations better reflect the actual visual elements present in the image rather than the subjective preferences of the annotator \[[10](http://arxiv.org/abs/1512.06974)\].
|    | reference                                                                                                                      | date     | key idea/summary                                                                                                                                                                                           |
|----|--------------------------------------------------------------------------------------------------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Seeing through the Human Reporting Bias: Visual Classifiers from Noisy Human-Centric Labels](http://arxiv.org/abs/1512.06974) | 12/22/15 | The paper proposes an algorithm to decouple human reporting bias from visually grounded labels, improving image classification and captioning by leveraging structured noise in human-centric annotations. |
### <a id='category-loss-correction-techniques-for-robust-training'></a>Loss Correction Techniques for Robust Training: 1 papers found.
Context: 
	Document 1: [Category]: «Loss Correction Techniques for Robust Training»
[Snippet]: «We present a theoretically grounded approach to train deep neural networks, including recurrent networks, subject to class-dependent label noise. We propose two procedures for loss correction that are agnostic to both application domain and network architecture. They simply amount to at most a matrix inversion and multiplication, provided that we know the probability of each class being corrupted into another. We further show how one can estimate these probabilities, adapting a recent technique for noise estimation to the multi-class setting, and thus providing an end-to-end framework. Extensive experiments on MNIST, IMDB, CIFAR-10, CIFAR-100 and a large scale dataset of clothing images employing a diversity of architectures &#x2014; stacking dense, convolutional, pooling, dropout, batch normalization, word embedding, LSTM and residual layers &#x2014; demonstrate the noise robustness of our proposals. Incidentally, we also prove that, when ReLU is the only non-linearity, the loss curvature is immune to class-dependent label noise.»
[_citation_number]: «12»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T06:44:48+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2406.16966)\]. Further details \[[6](http://arxiv.org/abs/2207.13316)\]\[[7](http://arxiv.org/abs/1706.00038)\]\[[8](http://arxiv.org/abs/1711.07131)\]\[[9](http://arxiv.org/abs/2312.12275)\]\[[10](http://arxiv.org/abs/1512.06974)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In context learning (ICL) relies heavily on high quality demonstrations drawn
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2406.16966)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2012.11854)\]\[[7](http://arxiv.org/abs/1706.00038)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer:  
The category "Loss Correction Techniques for Robust Training" focuses on developing methods to train deep neural networks in the presence of label noise, particularly class-dependent noise, which can significantly degrade model performance \[[12](http://arxiv.org/abs/1609.03683)\]. The proposed approach introduces two loss correction procedures that are independent of the application domain and network architecture, relying on matrix operations to adjust for class corruption probabilities \[[12](http://arxiv.org/abs/1609.03683)\]. These probabilities can be estimated using an adapted noise estimation technique, enabling an end-to-end framework for robust training \[[12](http://arxiv.org/abs/1609.03683)\]. The methodology is validated across diverse datasets, including MNIST, IMDB, CIFAR-10, CIFAR-100, and a large-scale clothing image dataset, with a variety of architectures such as dense, convolutional, LSTM, and residual networks \[[12](http://arxiv.org/abs/1609.03683)\]. Additionally, the work demonstrates that under certain conditions, such as when ReLU is the only non-linearity, the loss curvature remains unaffected by class-dependent label noise \[[12](http://arxiv.org/abs/1609.03683)\]. This research contributes to the broader field of robust training by offering a theoretically grounded solution that enhances model reliability in noisy environments.
|    | reference                                                                                                        | date     | key idea/summary                                                                                                                                                                                                                       |
|----|------------------------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Making Deep Neural Networks Robust to Label Noise: A Loss Correction Approach](http://arxiv.org/abs/1609.03683) | 09/13/16 | The paper introduces a theoretically grounded approach to train deep neural networks with class-dependent label noise, proposing loss correction methods and demonstrating their robustness across various architectures and datasets. |
### <a id='category-evaluation-metrics-for-noisy-label-detection'></a>Evaluation Metrics for Noisy Label Detection: 1 papers found.
Context: 
	Document 1: [Category]: «Evaluation Metrics for Noisy Label Detection»
[Snippet]: «Abstract Rapid advancements of large language models (LLMs) have enabled the processing, understanding, and generation of human-like text, with increasing integration into systems that touch our social sphere. Despite this success, these models can learn, perpetuate, and amplify harmful social biases. In this article, we present a comprehensive survey of bias evaluation and mitigation techniques for LLMs. We first consolidate, formalize, and expand notions of social bias and fairness in natural language processing, defining distinct facets of harm and introducing several desiderata to operationalize fairness for LLMs. We then unify the literature by proposing three intuitive taxonomies, two for bias evaluation, namely, metrics and datasets, and one for mitigation. Our first taxonomy of metrics for bias evaluation disambiguates the relationship between metrics and evaluation datasets, and organizes metrics by the different levels at which they operate in a model: embeddings, probabilities, and generated text. Our second taxonomy of datasets for bias evaluation categorizes datasets by their structure as counterfactual inputs or prompts, and identifies the targeted harms and social groups; we also release a consolidation of publicly available datasets for improved access. Our third taxonomy of techniques for bias mitigation classifies methods by their intervention during pre-processing, in-training, intra-processing, and post-processing, with granular subcategories that elucidate research trends. Finally, we identify open problems and challenges for future work. Synthesizing a wide range of recent research, we aim to provide a clear guide of the existing literature that empowers researchers and practitioners to better understand and prevent the propagation of bias in LLMs.»
[_citation_number]: «16»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T06:44:48+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2406.16966)\]. Further details \[[6](http://arxiv.org/abs/2207.13316)\]\[[7](http://arxiv.org/abs/1706.00038)\]\[[8](http://arxiv.org/abs/1711.07131)\]\[[9](http://arxiv.org/abs/2312.12275)\]\[[10](http://arxiv.org/abs/1512.06974)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In context learning (ICL) relies heavily on high quality demonstrations drawn
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2406.16966)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2012.11854)\]\[[7](http://arxiv.org/abs/1706.00038)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The evaluation of bias in large language models (LLMs) has gained significant attention due to the potential for models to perpetuate harmful social biases \[[16](http://arxiv.org/abs/2309.00770)\]. This issue is particularly relevant in the context of noisy label detection, where the accuracy of model outputs can be significantly affected by biased or incorrect annotations \[[16](http://arxiv.org/abs/2309.00770)\]. Existing research has focused on developing metrics and datasets to evaluate and mitigate these biases, with a growing emphasis on understanding how different levels of model outputs—such as embeddings, probabilities, and generated text—contribute to biased outcomes \[[16](http://arxiv.org/abs/2309.00770)\]. Additionally, there is a need for robust frameworks that can address the inherent biases in both the annotation process and the domain-specific knowledge of LLMs \[[16](http://arxiv.org/abs/2309.00770)\]. These challenges highlight the importance of comprehensive evaluation strategies that go beyond traditional metrics to ensure fairness and reliability in model performance.
|    | reference                                                                               | date     | key idea/summary                                                                                                                                                                                                                   |
|----|-----------------------------------------------------------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Bias and Fairness in Large Language Models: A Survey](http://arxiv.org/abs/2309.00770) | 09/02/23 | This paper presents a comprehensive survey of bias evaluation and mitigation techniques for large language models (LLMs), organizing existing research into three taxonomies and identifying open challenges to guide future work. |
### <a id='category-robustness-to-high-noise-ratios-in-training'></a>Robustness to High Noise Ratios in Training: 1 papers found.
Context: 
	Document 1: [Category]: «Robustness to High Noise Ratios in Training»
[Snippet]: «Datasets with significant proportions of noisy (incorrect) class labels present challenges for training accurate Deep Neural Networks (DNNs). We propose a new perspective for understanding DNN generalization for such datasets, by investigating the dimensionality of the deep representation subspace of training samples. We show that from a dimensionality perspective, DNNs exhibit quite distinctive learning styles when trained with clean labels versus when trained with a proportion of noisy labels. Based on this finding, we develop a new dimensionality-driven learning strategy, which monitors the dimensionality of subspaces during training and adapts the loss function accordingly. We empirically demonstrate that our approach is highly tolerant to significant proportions of noisy labels, and can effectively learn low-dimensional local subspaces that capture the data distribution.»
[_citation_number]: «17»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T06:44:48+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2406.16966)\]. Further details \[[6](http://arxiv.org/abs/2207.13316)\]\[[7](http://arxiv.org/abs/1706.00038)\]\[[8](http://arxiv.org/abs/1711.07131)\]\[[9](http://arxiv.org/abs/2312.12275)\]\[[10](http://arxiv.org/abs/1512.06974)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In context learning (ICL) relies heavily on high quality demonstrations drawn
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2406.16966)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2012.11854)\]\[[7](http://arxiv.org/abs/1706.00038)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The category "Robustness to High Noise Ratios in Training" focuses on the challenges posed by noisy datasets in training Deep Neural Networks (DNNs) and proposes strategies to improve generalization under such conditions \[[17](http://arxiv.org/abs/1806.02612)\]. Specifically, the work highlights that DNNs exhibit distinct learning behaviors when trained with clean versus noisy labels, emphasizing the importance of understanding how noise affects the dimensionality of the representation subspaces \[[17](http://arxiv.org/abs/1806.02612)\]. This insight leads to the development of a dimensionality-driven learning strategy that dynamically adjusts the loss function during training, enabling the model to tolerate high noise levels while learning low-dimensional subspaces that better capture the underlying data distribution \[[17](http://arxiv.org/abs/1806.02612)\]. This approach aligns with broader efforts to enhance model robustness in the presence of noisy data, as seen in related work on improving training reliability under imperfect annotations \[[17](http://arxiv.org/abs/1806.02612)\].
|    | reference                                                                           | date     | key idea/summary                                                                                                                                                                                                              |
|----|-------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Dimensionality-Driven Learning with Noisy Labels](http://arxiv.org/abs/1806.02612) | 06/07/18 | The paper introduces a dimensionality-driven learning strategy for DNNs to improve generalization in the presence of noisy labels by adapting the loss function based on the dimensionality of deep representation subspaces. |
