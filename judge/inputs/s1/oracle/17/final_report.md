## Related Works

Semi-supervised learning (SSL) has emerged as a powerful paradigm for leveraging unlabeled data to improve model performance when labeled data is limited \[[1](http://arxiv.org/abs/2001.06001)\]. Traditional SSL methods assume that labeled and unlabeled data share the same class distribution, a strong assumption that is often violated in real-world scenarios \[[1](http://arxiv.org/abs/2001.06001)\]. Specifically, unlabeled data may contain out-of-distribution (OOD) samples, or outliers, which are not present in the labeled set \[[1](http://arxiv.org/abs/2001.06001)\]. These outliers can significantly degrade the performance of SSL models if not properly handled \[[1](http://arxiv.org/abs/2001.06001)\]. 

Several approaches have been proposed to address the challenges posed by open-set SSL, where unlabeled data may contain OOD samples \[[1](http://arxiv.org/abs/2001.06001)\]. For instance, Temporal Ensembling \[[2](http://arxiv.org/abs/1703.01780)\] and Mean Teacher \[[3](http://arxiv.org/abs/1610.02242)\] have been widely used to improve semi-supervised learning by maintaining consistency between predictions on unlabeled data. However, these methods often fail to account for the presence of outliers, leading to performance degradation \[[1](http://arxiv.org/abs/2001.06001)\]. 

FixMatch \[[4](http://arxiv.org/abs/1905.02249)\] introduced a simple yet effective approach by combining consistency regularization with pseudo-labeling, achieving state-of-the-art results on various benchmarks \[[4](http://arxiv.org/abs/1905.02249)\]. However, FixMatch uses a fixed threshold for pseudo-labeling, which may not be optimal for all classes \[[1](http://arxiv.org/abs/2001.06001)\]. To address this, FlexMatch \[[5](http://arxiv.org/abs/2001.07685)\] introduced curriculum pseudo labeling (CPL), allowing for dynamic threshold adjustments based on the model's learning status \[[5](http://arxiv.org/abs/2001.07685)\]. This approach significantly improved performance, especially when labeled data is scarce \[[5](http://arxiv.org/abs/2001.07685)\]. 

FreeMatch \[[6](http://arxiv.org/abs/1911.09785)\] further refined the thresholding mechanism by introducing a self-adaptive approach that adjusts the confidence threshold based on the model's learning progress \[[6](http://arxiv.org/abs/1911.09785)\]. This method demonstrated superior performance, particularly when labeled data is extremely rare \[[6](http://arxiv.org/abs/1911.09785)\]. 

In addition to thresholding, several works have focused on improving the robustness of SSL models to OOD samples. For example, CoMatch \[[7](http://arxiv.org/abs/2110.08263)\] introduced a contrastive graph regularization approach to enhance pseudo-labels and improve performance on label-scarce datasets \[[7](http://arxiv.org/abs/2110.08263)\]. Similarly, SCOMatch \[[8](http://arxiv.org/abs/2205.07246)\] addressed the overtrusting issue in open-set SSL by treating OOD samples as an additional class and refining the decision boundary through simultaneous close-set and open-set self-training \[[8](http://arxiv.org/abs/2205.07246)\]. 

Recent methods have also explored the use of multi-task learning and curriculum learning to improve SSL performance in open-set settings. For example, IOMatch \[[9](http://arxiv.org/abs/2011.11183)\] proposed a framework that jointly utilizes inliers and outliers, even when distinguishing between them is challenging \[[9](http://arxiv.org/abs/2011.11183)\]. This approach demonstrated strong performance across various
## Research papers
### Outline
- [Pseudo-Labeling Methods and Thresholding [9 papers]](#category-pseudo-labeling-methods-and-thresholding)
- [Consistency Regularization Techniques [1 papers]](#category-consistency-regularization-techniques)
- [Contrastive Regularization for Pseudo-Labels [1 papers]](#category-contrastive-regularization-for-pseudo-labels)
- [Assumptions in SSL and Their Violations [1 papers]](#category-assumptions-in-ssl-and-their-violations)
- [Open-Set Self-Training Strategies [2 papers]](#category-open-set-self-training-strategies)
- [Outlier Handling in Open-Set SSL [9 papers]](#category-outlier-handling-in-open-set-ssl)
- [Multi-Task Learning in SSL [1 papers]](#category-multi-task-learning-in-ssl)
- [Semi-Supervised Learning Foundations [2 papers]](#category-semi-supervised-learning-foundations)

### <a id='category-pseudo-labeling-methods-and-thresholding'></a>Pseudo-Labeling Methods and Thresholding: 9 papers found.
In the context of pseudo-labeling methods and thresholding, several studies have explored techniques to improve semi-supervised learning (SSL) by leveraging unlabeled data effectively. Pseudo-labeling, where a model generates labels for unlabeled data and iteratively refines them, has been revisited with the introduction of curriculum learning and parameter restarting to combat concept drift \[[1](http://arxiv.org/abs/2001.06001)\]. This approach has shown competitive results, achieving high accuracy on benchmarks like CIFAR-10 and ImageNet-ILSVRC \[[1](http://arxiv.org/abs/2001.06001)\]. Similarly, self-ensembling methods, which use predictions from different training epochs and augmented inputs to form a consensus, have demonstrated significant improvements in tasks like SVHN and CIFAR-10 \[[3](http://arxiv.org/abs/1610.02242)\]. MixMatch further advances this by combining pseudo-labeling with mixup, achieving state-of-the-art results across multiple datasets \[[4](http://arxiv.org/abs/1905.02249)\]. FixMatch, another notable method, uses consistency regularization and pseudo-labeling with a confidence threshold to improve performance, achieving strong results even with minimal labeled data \[[5](http://arxiv.org/abs/2001.07685)\]. ReMixMatch builds on these ideas by introducing distribution alignment and augmentation anchoring, significantly improving data efficiency \[[6](http://arxiv.org/abs/1911.09785)\]. Curriculum Pseudo Labeling (CPL) further refines pseudo-labeling by dynamically adjusting thresholds per class, leading to better performance in scenarios with limited labeled data \[[7](http://arxiv.org/abs/2110.08263)\]. FreeMatch extends this by self-adaptively adjusting thresholds and incorporating fairness regularization, achieving even greater error reduction on challenging benchmarks \[[8](http://arxiv.org/abs/2205.07246)\]. These methods collectively highlight the ongoing evolution of pseudo-labeling strategies, emphasizing the importance of adaptive thresholding, curriculum learning, and model diversity to enhance robustness and performance in semi-supervised settings.
|    | reference                                                                                                                        |   date | key idea/summary                                                                                                                                                                                                                                          |
|----|----------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Curriculum Labeling: Revisiting Pseudo-Labeling for Semi-Supervised
  Learning](http://arxiv.org/abs/2001.06001)                |    nan | The paper revisits pseudo-labeling in semi-supervised learning, demonstrating its competitiveness with state-of-the-art methods through curriculum learning and avoiding concept drift, achieving high accuracy with limited labeled data.                |
|  1 | [Temporal Ensembling for Semi-Supervised Learning](http://arxiv.org/abs/1610.02242)                                              |    nan | The paper introduces a semi-supervised learning method called self-ensembling, which uses ensemble predictions from different training epochs and conditions to improve model performance, achieving new state-of-the-art results on standard benchmarks. |
|  2 | [MixMatch: A Holistic Approach to Semi-Supervised Learning](http://arxiv.org/abs/1905.02249)                                     |    nan | MixMatch is a semi-supervised learning algorithm that combines data augmentation and label guessing with MixUp to achieve state-of-the-art results across various datasets and labeled data amounts.                                                      |
|  3 | [FixMatch: Simplifying Semi-Supervised Learning with Consistency and
  Confidence](http://arxiv.org/abs/2001.07685)              |    nan | FixMatch is a simple semi-supervised learning method that combines consistency regularization and pseudo-labeling, achieving state-of-the-art performance on standard benchmarks.                                                                         |
|  4 | [ReMixMatch: Semi-Supervised Learning with Distribution Alignment and
  Augmentation Anchoring](http://arxiv.org/abs/1911.09785) |    nan | ReMixMatch improves upon MixMatch by introducing distribution alignment and augmentation anchoring, achieving higher data efficiency and accuracy with significantly fewer labeled examples.                                                              |
|  5 | [FlexMatch: Boosting Semi-Supervised Learning with Curriculum Pseudo
  Labeling](http://arxiv.org/abs/2110.08263)                |    nan | CPL improves semi-supervised learning by dynamically adjusting class-specific thresholds for unlabeled data, leading to better performance and faster convergence compared to FixMatch.                                                                   |
|  6 | [FreeMatch: Self-adaptive Thresholding for Semi-supervised Learning](http://arxiv.org/abs/2205.07246)                            |    nan | FreeMatch is a semi-supervised learning method that adaptively adjusts the confidence threshold and introduces a class fairness regularization penalty to improve performance, especially when labeled data are scarce.                                   |
|  7 | [Pseudo-label: The simple and efficient semi-supervised learning method for deep neural networks]()                              |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                 |
|  8 | [Semi-Supervised Learning under Class Distribution Mismatch]()                                                                   |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                 |
### <a id='category-consistency-regularization-techniques'></a>Consistency Regularization Techniques: 1 papers found.
Context: 
	Document 1: [Category]: «Consistency Regularization Techniques»
[Snippet]: «The recently proposed Temporal Ensembling has achieved state-of-the-art
results in several semi-supervised learning benchmarks. It maintains an
exponential moving average of label predictions on each training example, and
penalizes predictions that are inconsistent with this target. However, because
the targets change only once per epoch, Temporal Ensembling becomes unwieldy
when learning large datasets. To overcome this problem, we propose Mean
Teacher, a method that averages model weights instead of label predictions. As
an additional benefit, Mean Teacher improves test accuracy and enables training
with fewer labels than Temporal Ensembling. Without changing the network
architecture, Mean Teacher achieves an error rate of 4.35% on SVHN with 250
labels, outperforming Temporal Ensembling trained with 1000 labels. We also
show that a good network architecture is crucial to performance. Combining Mean
Teacher and Residual Networks, we improve the state of the art on CIFAR-10 with
4000 labels from 10.55% to 6.28%, and on ImageNet 2012 with 10% of the labels
from 35.24% to 9.11%.»
[_citation_number]: «2»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T10:24:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1610.02242)\]. Further details \[[6](http://arxiv.org/abs/1911.09785)\]\[[7](http://arxiv.org/abs/2110.08263)\]\[[8](http://arxiv.org/abs/2205.07246)\]\[[9](http://arxiv.org/abs/2011.11183)\]\[[10](http://arxiv.org/abs/1804.09170)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Conventional semi-supervised learning (SSL) ideally assumes that labeled and
unlabeled data share an identical class distribution, however in practice
|    | reference                                                                                                                                                    |   date | key idea/summary                                                                                                                                                                                                     |
|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Mean teachers are better role models: Weight-averaged consistency
  targets improve semi-supervised deep learning results](http://arxiv.org/abs/1703.01780) |    nan | Mean Teacher is a semi-supervised learning method that improves upon Temporal Ensembling by averaging model weights instead of label predictions, leading to better test accuracy and performance with fewer labels. |
### <a id='category-contrastive-regularization-for-pseudo-labels'></a>Contrastive Regularization for Pseudo-Labels: 1 papers found.
Context: 
	Document 1: [Category]: «Contrastive Regularization for Pseudo-Labels»
[Snippet]: «Semi-supervised learning has been an effective paradigm for leveraging
unlabeled data to reduce the reliance on labeled data. We propose CoMatch, a
new semi-supervised learning method that unifies dominant approaches and
addresses their limitations. CoMatch jointly learns two representations of the
training data, their class probabilities and low-dimensional embeddings. The
two representations interact with each other to jointly evolve. The embeddings
impose a smoothness constraint on the class probabilities to improve the
pseudo-labels, whereas the pseudo-labels regularize the structure of the
embeddings through graph-based contrastive learning. CoMatch achieves
state-of-the-art performance on multiple datasets. It achieves substantial
accuracy improvements on the label-scarce CIFAR-10 and STL-10. On ImageNet with
1% labels, CoMatch achieves a top-1 accuracy of 66.0%, outperforming FixMatch
by 12.6%. Furthermore, CoMatch achieves better representation learning
performance on downstream tasks, outperforming both supervised learning and
self-supervised learning. Code and pre-trained models are available at
https://github.com/salesforce/CoMatch.»
[_citation_number]: «9»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T10:24:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1610.02242)\]. Further details \[[6](http://arxiv.org/abs/1911.09785)\]\[[7](http://arxiv.org/abs/2110.08263)\]\[[8](http://arxiv.org/abs/2205.07246)\]\[[9](http://arxiv.org/abs/2011.11183)\]\[[10](http://arxiv.org/abs/1804.09170)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Conventional semi-supervised learning (SSL) ideally assumes that labeled and
unlabeled data share an identical class distribution, however in practice, this
assumption is easily violated, as unlabeled data often
|    | reference                                                                                                  |   date | key idea/summary                                                                                                                                                                                                                                      |
|----|------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [CoMatch: Semi-supervised Learning with Contrastive Graph Regularization](http://arxiv.org/abs/2011.11183) |    nan | CoMatch is a semi-supervised learning method that unifies dominant approaches by jointly learning class probabilities and low-dimensional embeddings, achieving state-of-the-art performance on multiple datasets and better representation learning. |
### <a id='category-assumptions-in-ssl-and-their-violations'></a>Assumptions in SSL and Their Violations: 1 papers found.
Context: 
	Document 1: [Category]: «Assumptions in SSL and Their Violations»
[Snippet]: «Semi-supervised learning (SSL) provides a powerful framework for leveraging
unlabeled data when labels are limited or expensive to obtain. SSL algorithms
based on deep neural networks have recently proven successful on standard
benchmark tasks. However, we argue that these benchmarks fail to address many
issues that these algorithms would face in real-world applications. After
creating a unified reimplementation of various widely-used SSL techniques, we
test them in a suite of experiments designed to address these issues. We find
that the performance of simple baselines which do not use unlabeled data is
often underreported, that SSL methods differ in sensitivity to the amount of
labeled and unlabeled data, and that performance can degrade substantially when
the unlabeled dataset contains out-of-class examples. To help guide SSL
research towards real-world applicability, we make our unified reimplemention
and evaluation platform publicly available.»
[_citation_number]: «10»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T10:24:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1610.02242)\]. Further details \[[6](http://arxiv.org/abs/1911.09785)\]\[[7](http://arxiv.org/abs/2110.08263)\]\[[8](http://arxiv.org/abs/2205.07246)\]\[[9](http://arxiv.org/abs/2011.11183)\]\[[10](http://arxiv.org/abs/1804.09170)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Conventional semi-supervised learning (SSL) ideally assumes that labeled and
unlabeled data share an identical class distribution, however in practice, this
assumption is easily violated, as unlabeled data often includes unknown class
data, i.e., outliers. The outliers are treated as noise, considerably degrading
the performance of SSL models. To address this drawback, we propose a novel
framework, Diversify and Conquer (DAC), to enhance SSL robustness in the
context of open
|    | reference                                                                                           |   date | key idea/summary                                                                                                                                                                               |
|----|-----------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Realistic Evaluation of Deep Semi-Supervised Learning Algorithms](http://arxiv.org/abs/1804.09170) |    nan | The paper argues that existing SSL benchmarks fail to address real-world challenges and presents a unified reimplemention and evaluation platform to improve the applicability of SSL methods. |
### <a id='category-open-set-self-training-strategies'></a>Open-Set Self-Training Strategies: 2 papers found.
Context: 
	Document 1: [Category]: «Open-Set Self-Training Strategies»
[Snippet]: «Open-set semi-supervised learning (OSSL) leverages practical open-set unlabeled data, comprising both in-distribution (ID) samples from seen classes and out-of-distribution (OOD) samples from unseen classes, for semi-supervised learning (SSL). Prior OSSL methods initially learned the decision boundary between ID and OOD with labeled ID data, subsequently employing self-training to refine this boundary. These methods, however, suffer from the tendency to overtrust the labeled ID data: the scarcity of labeled data caused the distribution bias between the labeled samples and the entire ID data, which misleads the decision boundary to overfit. The subsequent self-training process, based on the overfitted result, fails to rectify this problem. In this paper, we address the overtrusting issue by treating OOD samples as an additional class, forming a new SSL process. Specifically, we propose SCOMatch, a novel OSSL method that 1) selects reliable OOD samples as new labeled data with an OOD memory queue and a corresponding update strategy and 2) integrates the new SSL process into the original task through our Simultaneous Close-set and Open-set self-training. SCOMatch refines the decision boundary of ID and OOD classes across the entire dataset, thereby leading to improved results. Extensive experimental results show that SCOMatch significantly outperforms the state-of-the-art methods on various benchmarks. The effectiveness is further verified through ablation studies and visualization.»
[_citation_number]: «11»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T10:24:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1610.02242)\]. Further details \[[6](http://arxiv.org/abs/1911.09785)\]\[[7](http://arxiv.org/abs/2110.08263)\]\[[8](http://arxiv.org/abs/2205.07246)\]\[[9](http://arxiv.org/abs/2011.11183)\]\[[10](http://arxiv.org/abs/1804.09170)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the
|    | reference                                                                                                     |   date | key idea/summary                                                                                                                                                                                                                                                                                     |
|----|---------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [SCOMatch: Alleviating Overtrusting in Open-set Semi-supervised Learning](http://arxiv.org/abs/2409.17512)    |    nan | SCOMatch is a novel open-set semi-supervised learning method that addresses the overtrust issue by treating OOD samples as an additional class and integrating them into the training process through a simultaneous close-set and open-set self-training approach, leading to improved performance. |
|  1 | [(SAFER-STUDENT) for Safe Deep Semi-Supervised Learning With Unseen-Class
                  Unlabeled Data]() |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                            |
### <a id='category-outlier-handling-in-open-set-ssl'></a>Outlier Handling in Open-Set SSL: 9 papers found.
In the context of open-set semi-supervised learning (OSSL), existing methods often assume that unlabeled data contains only in-distribution (ID) samples, but in reality, out-of-distribution (OOD) outliers are prevalent and can severely degrade model performance \[[16](http://arxiv.org/abs/2105.14148)\]. To address this, several approaches have been proposed, such as Weight-Aware Distillation (WAD), which selectively transfers knowledge from unsupervised contrastive representations to the target classifier by capturing adaptive weights and high-quality pseudo-labels \[[12](http://arxiv.org/abs/2308.11874)\]. Similarly, OpenMatch integrates novelty detection with FixMatch to reject outliers while learning robust representations \[[16](http://arxiv.org/abs/2105.14148)\]. Another approach, IOMatch, jointly utilizes inliers and outliers by employing a multi-binary classifier alongside a closed-set classifier, treating outliers as a single class \[[17](http://arxiv.org/abs/2308.13168)\]. Additionally, the Simple but Strong Baseline (SSB) leverages high-confidence pseudo-labeled data and non-linear transformations to separate inlier and outlier features, improving both classification and detection \[[18](http://arxiv.org/abs/2311.10572)\]. The Transferable OOD data Recycling (TOOR) method further enhances performance by utilizing recyclable OOD data through adversarial domain adaptation \[[19](http://arxiv.org/abs/2011.13529)\]. These methods highlight the growing interest in effectively handling outliers in OSSL, with a focus on robustness and performance improvements under class distribution mismatches.
|    | reference                                                                                                                                                         |   date | key idea/summary                                                                                                                                                                                                                                                                                                      |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Semi-Supervised Learning via Weight-aware Distillation under Class
  Distribution Mismatch](http://arxiv.org/abs/2308.11874)                                     |    nan | The paper introduces a robust semi-supervised learning framework called Weight-Aware Distillation (WAD) that addresses class distribution mismatch by selectively transferring knowledge from unlabeled data to the target classifier, improving performance through adaptive weights and high-quality pseudo labels. |
|  1 | [Trash to Treasure: Harvesting OOD Data with Cross-Modal Matching for
  Open-Set Semi-Supervised Learning](http://arxiv.org/abs/2108.05617)                       |    nan | The paper proposes a novel training mechanism for open-set semi-supervised learning that effectively exploits out-of-distribution samples for enhanced feature learning while mitigating their adverse impact through a cross-modal matching strategy.                                                                |
|  2 | [Out-of-Distributed Semantic Pruning for Robust Semi-Supervised Learning](http://arxiv.org/abs/2305.18158)                                                        |    nan | The paper introduces OOD Semantic Pruning (OSP), a unified framework that addresses the issue of corrupted semantic information in robust semi-supervised learning by pruning out-of-distribution semantics from in-distribution features, achieving state-of-the-art results on benchmark datasets.                  |
|  3 | [OpenMatch: Open-set Consistency Regularization for Semi-supervised
  Learning with Outliers](http://arxiv.org/abs/2105.14148)                                    |    nan | OpenMatch is a novel open-set semi-supervised learning approach that combines FixMatch with novelty detection using one-vs-all classifiers and a soft-consistency regularization loss to effectively handle outliers in unlabeled data.                                                                               |
|  4 | [IOMatch: Simplifying Open-Set Semi-Supervised Learning with Joint
  Inliers and Outliers Utilization](http://arxiv.org/abs/2308.13168)                           |    nan | IOMatch is a novel open-set semi-supervised learning framework that jointly utilizes inliers and outliers by employing a multi-binary classifier and standard closed-set classifier to create unified open-set classification targets, leading to significant performance improvements across benchmark datasets.     |
|  5 | [SSB: Simple but Strong Baseline for Boosting Performance of Open-Set
  Semi-Supervised Learning](http://arxiv.org/abs/2311.10572)                                |    nan | The paper introduces a simple yet effective approach for open-set semi-supervised learning, combining pseudo-labeled data, non-linear feature transformations, and pseudo-negative mining to improve both inlier classification and outlier detection.                                                                |
|  6 | [They are Not Completely Useless: Towards Recycling Transferable
  Unlabeled Data for Class-Mismatched Semi-Supervised Learning](http://arxiv.org/abs/2011.13529) |    nan | The TOOR method improves semi-supervised learning with mismatched classes by utilizing both in-distribution (ID) and recyclable out-of-distribution (OOD) data through adversarial domain adaptation, thereby extracting more information from unlabeled data and achieving better performance.                       |
|  7 | [Unknown-Aware Graph Regularization for Robust Semi-supervised Learning
                  from Uncurated Data]()                                                  |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                                             |
|  8 | [Binary Decomposition: A Problem Transformation Perspective for Open-Set Semi-Supervised Learning]()                                                              |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                                             |
### <a id='category-multi-task-learning-in-ssl'></a>Multi-Task Learning in SSL: 1 papers found.
Context: 
	Document 1: [Category]: «Multi-Task Learning in SSL»
[Snippet]: «Semi-supervised learning (SSL) has been proposed to leverage unlabeled data
for training powerful models when only limited labeled data is available. While
existing SSL methods assume that samples in the labeled and unlabeled data
share the classes of their samples, we address a more complex novel scenario
named open-set SSL, where out-of-distribution (OOD) samples are contained in
unlabeled data. Instead of training an OOD detector and SSL separately, we
propose a multi-task curriculum learning framework. First, to detect the OOD
samples in unlabeled data, we estimate the probability of the sample belonging
to OOD. We use a joint optimization framework, which updates the network
parameters and the OOD score alternately. Simultaneously, to achieve high
performance on the classification of in-distribution (ID) data, we select ID
samples in unlabeled data having small OOD scores, and use these data with
labeled data for training the deep neural networks to classify ID samples in a
semi-supervised manner. We conduct several experiments, and our method achieves
state-of-the-art results by successfully eliminating the effect of OOD samples.»
[_citation_number]: «13»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T10:24:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1610.02242)\]. Further details \[[6](http://arxiv.org/abs/1911.09785)\]\[[7](http://arxiv.org/abs/2110.08263)\]\[[8](http://arxiv.org/abs/2205.07246)\]\[[9](http://arxiv.org/abs/2011.11183)\]\[[10](http://arxiv.org/abs/1804.09170)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Conventional semi-supervised learning (SSL) ideally assumes that labeled and
unlabeled data share an identical class distribution, however in practice, this
assumption is easily violated, as unlabeled data often includes unknown class

|    | reference                                                                                                |   date | key idea/summary                                                                                                                                                                                                                             |
|----|----------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Multi-Task Curriculum Framework for Open-Set Semi-Supervised Learning](http://arxiv.org/abs/2007.11330) |    nan | The paper proposes a multi-task curriculum learning framework for open-set semi-supervised learning, addressing the challenge of out-of-distribution samples in unlabeled data by jointly optimizing OOD detection and classification tasks. |
### <a id='category-semi-supervised-learning-foundations'></a>Semi-Supervised Learning Foundations: 2 papers found.
Context: 
	Document 1: [Category]: «Semi-Supervised Learning Foundations»
[Snippet]: «»
[_citation_number]: «21»

	Document 2: [Category]: «Semi-Supervised Learning Foundations»
[Snippet]: «»
[_citation_number]: «22»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-30T10:24:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1610.02242)\]. Further details \[[6](http://arxiv.org/abs/1911.09785)\]\[[7](http://arxiv.org/abs/2110.08263)\]\[[8](http://arxiv.org/abs/2205.07246)\]\[[9](http://arxiv.org/abs/2011.11183)\]\[[10](http://arxiv.org/abs/1804.09170)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Conventional semi-supervised learning (SSL) ideally assumes that labeled and
unlabeled data share an identical class distribution, however in practice, this
assumption is easily violated, as unlabeled data often includes unknown class
data, i.e., outliers. The outliers are treated as noise, considerably degrading
the performance of SSL models. To address this drawback, we propose a novel
framework, Diversify and Conquer (DAC), to enhance SSL robustness in the
context of open-set semi-supervised learning. In particular, we note that
existing open-set SSL methods rely on prediction discrepancies between inliers
and outliers from a single model trained on labeled data. This approach can be
easily failed when the labeled data is insufficient, leading to performance
degradation that is worse than naive SSL that do not account for outliers. In
contrast, our approach exploits prediction disagreements among multiple models
that are differently biased towards the unlabeled distribution. By leveraging
the discrepancies arising from training on unlabeled data, our method enables
robust outlier detection even when the labeled data is underspecified. Our key
contribution is constructing a collection of differently biased models through
a single training process. By encouraging divergent heads to be differently

|    | reference                                                          |   date | key idea/summary                                                                                          |
|----|--------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------|
|  0 | [Semi-supervised Learning by Entropy Minimization]()               |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
|  1 | [Graph-Based Semi-Supervised Learning: (A) Comprehensive Review]() |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
