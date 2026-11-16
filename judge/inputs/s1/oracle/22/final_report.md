## Related Works

Unsupervised domain adaptation (UDA) for semantic segmentation aims to transfer knowledge from a labeled source domain to an unlabeled target domain without requiring additional annotations \[[1](http://arxiv.org/abs/1411.4038)\]. Traditional UDA methods assume that the category settings between the source and target domains are known, which is a restrictive assumption in real-world applications \[[1](http://arxiv.org/abs/1411.4038)\]. This assumption leads to performance degradation when private classes—classes present in the target domain but absent in the source—exist \[[1](http://arxiv.org/abs/1411.4038)\]. To address this limitation, recent works have explored more flexible domain adaptation settings, such as open-set and universal domain adaptation \[[1](http://arxiv.org/abs/1411.4038)\].

Several methods have been proposed to handle domain shift in semantic segmentation. For instance, \[[2](http://arxiv.org/abs/1606.00915)\] introduced DeepLab, which combines atrous convolution and fully connected CRFs to improve localization accuracy. Similarly, \[[3](http://arxiv.org/abs/1506.04579)\] proposed ParseNet, which enhances semantic segmentation by incorporating global context into deep convolutional networks. These methods focus on improving performance within a fixed domain setting, rather than addressing the more challenging problem of unknown category shifts \[[1](http://arxiv.org/abs/1411.4038)\].

To handle open-set domain adaptation, where the target domain may contain classes not present in the source, \[[4](http://arxiv.org/abs/1612.01105)\] introduced a method that uses image rotation recognition as a self-supervised task to distinguish between known and unknown classes. This approach improves the robustness of models in open-set scenarios \[[1](http://arxiv.org/abs/1411.4038)\]. Additionally, \[[5](http://arxiv.org/abs/2105.15203)\] proposed a universal domain adaptation framework called DANCE, which uses self-supervised learning and entropy-based feature alignment to handle arbitrary category shifts \[[1](http://arxiv.org/abs/1411.4038)\].

In the context of domain adaptation, \[[6](http://arxiv.org/abs/2012.15840)\] proposed a method that leverages adversarial learning to align features between source and target domains. This approach has been further refined in \[[7](http://arxiv.org/abs/1802.10349)\], where the authors introduced a multi-level adversarial network to enhance domain adaptation performance. These methods, while effective, typically assume that the target domain contains only known classes, which is not always the case in real-world applications \[[1](http://arxiv.org/abs/1411.4038)\].

To address the problem of unknown categories, \[[8](http://arxiv.org/abs/2003.00867)\] proposed a method that learns a threshold to distinguish between known and unknown classes in the target domain. This threshold is learned using source samples and adapted to the target domain. This approach is more robust than manually setting a threshold \[[1](http://arxiv.org/abs/1411.4038)\].

The problem of domain adaptation in semantic segmentation has also been tackled through self-training strategies. For example, \[[9](http://arxiv.org/abs/2004.07703)\] introduced a method that uses pseudo-labels to iteratively refine the model's predictions on the target domain. However, pseudo-labels can be noisy, leading to overfitting to the source domain \[[1](http://arxiv.org/abs/1411.4038)\]. To mitigate this issue, [
## Research papers
### Outline
- [Feature Alignment Techniques [7 papers]](#category-feature-alignment-techniques)
- [Benchmark Datasets for UDA-SS [1 papers]](#category-benchmark-datasets-for-uda-ss)
- [Adversarial Learning Approaches [8 papers]](#category-adversarial-learning-approaches)
- [Self-Training Strategies [8 papers]](#category-self-training-strategies)
- [Class Separation Mechanisms [2 papers]](#category-class-separation-mechanisms)
- [Universal Domain Adaptation Frameworks [2 papers]](#category-universal-domain-adaptation-frameworks)
- [Open-Set Domain Adaptation [1 papers]](#category-open-set-domain-adaptation)
- [Threshold Learning for Unknown Classes [1 papers]](#category-threshold-learning-for-unknown-classes)

### <a id='category-feature-alignment-techniques'></a>Feature Alignment Techniques: 7 papers found.
In the context of feature alignment techniques for semantic segmentation, recent research has focused on improving the adaptability and accuracy of models across different domains and resolutions. For instance, the use of fully convolutional networks (FCNs) has been pivotal in enabling spatially dense predictions, allowing models to handle input of arbitrary size while maintaining efficient inference \[[1](http://arxiv.org/abs/1411.4038)\]. Atrous convolution, or dilated convolutions, has been introduced to enhance the receptive field without increasing computational load, enabling better context modeling \[[2](http://arxiv.org/abs/1606.00915)\]. Additionally, techniques such as global feature augmentation have been proposed to improve performance by incorporating global context into local feature maps, leading to state-of-the-art results on datasets like SiftFlow and PASCAL-Context \[[3](http://arxiv.org/abs/1506.04579)\]. More recently, models like SegFormer have emerged, integrating Transformers with lightweight decoders to achieve efficient and accurate segmentation, demonstrating significant improvements in performance and efficiency \[[5](http://arxiv.org/abs/2105.15203)\]. Similarly, the SETR model treats segmentation as a sequence-to-sequence task, leveraging transformers to model global context effectively, achieving new state-of-the-art results on multiple benchmarks \[[6](http://arxiv.org/abs/2012.15840)\]. These approaches highlight the ongoing evolution in feature alignment techniques, emphasizing the importance of context modeling, efficient computation, and domain adaptation in semantic segmentation tasks.
|    | reference                                                                                                                                            |   date | key idea/summary                                                                                                                                                                                                                                                                                          |
|----|------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Fully Convolutional Networks for Semantic Segmentation](http://arxiv.org/abs/1411.4038)                                                             |    nan | Fully convolutional networks achieve state-of-the-art semantic segmentation by adapting existing classification networks and combining deep semantic features with shallow appearance details.                                                                                                            |
|  1 | [DeepLab: Semantic Image Segmentation with Deep Convolutional Nets,
  Atrous Convolution, and Fully Connected CRFs](http://arxiv.org/abs/1606.00915) |    nan | The paper introduces the DeepLab system, which uses atrous convolution, atrous spatial pyramid pooling (ASPP), and a Conditional Random Field (CRF) to achieve state-of-the-art results in semantic image segmentation, achieving 79.7% mIOU on the PASCAL VOC-2012 dataset.                              |
|  2 | [ParseNet: Looking Wider to See Better](http://arxiv.org/abs/1506.04579)                                                                             |    nan | ParseNet improves semantic segmentation by adding global context to deep convolutional networks, achieving state-of-the-art performance with minimal computational cost.                                                                                                                                  |
|  3 | [SegFormer: Simple and Efficient Design for Semantic Segmentation with
  Transformers](http://arxiv.org/abs/2105.15203)                              |    nan | SegFormer is a simple and efficient semantic segmentation framework that combines Transformers with lightweight MLP decoders, achieving state-of-the-art performance with significantly reduced parameters and improved robustness.                                                                       |
|  4 | [Rethinking Semantic Segmentation from a Sequence-to-Sequence Perspective
  with Transformers](http://arxiv.org/abs/2012.15840)                      |    nan | The paper introduces SETR, a segmentation model based on a pure transformer architecture that treats semantic segmentation as a sequence-to-sequence prediction task, achieving state-of-the-art results on multiple benchmarks.                                                                          |
|  5 | [HRDA: Context-Aware High-Resolution Domain-Adaptive Semantic
  Segmentation](http://arxiv.org/abs/2204.13132)                                       |    nan | HRDA is a multi-resolution training approach for unsupervised domain adaptation in semantic segmentation that combines high-resolution crops for fine details and low-resolution crops for long-range context, achieving significant improvements in mIoU on GTA-to-Cityscapes and Synthia-to-Cityscapes. |
|  6 | [Psanet: Point-wise spatial attention network for scene parsing]()                                                                                   |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                                 |
### <a id='category-benchmark-datasets-for-uda-ss'></a>Benchmark Datasets for UDA-SS: 1 papers found.
Context: 
	Document 1: [Category]: «Benchmark Datasets for UDA-SS»
[Snippet]: «Scene parsing is challenging for unrestricted open vocabulary and diverse
scenes. In this paper, we exploit the capability of global context information
by different-region-based context aggregation through our pyramid pooling
module together with the proposed pyramid scene parsing network (PSPNet). Our
global prior representation is effective to produce good quality results on the
scene parsing task, while PSPNet provides a superior framework for pixel-level
prediction tasks. The proposed approach achieves state-of-the-art performance
on various datasets. It came first in ImageNet scene parsing challenge 2016,
PASCAL VOC 2012 benchmark and Cityscapes benchmark. A single PSPNet yields new
record of mIoU accuracy 85.4% on PASCAL VOC 2012 and accuracy 80.2% on
Cityscapes.»
[_citation_number]: «4»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-28T15:14:11+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1506.04579)\]. Further details \[[6](http://arxiv.org/abs/2012.15840)\]\[[7](http://arxiv.org/abs/1802.10349)\]\[[8](http://arxiv.org/abs/2003.00867)\]\[[9](http://arxiv.org/abs/2004.07703)\]\[[10](http://arxiv.org/abs/1901.05427)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Unsupervised domain adaptation for semantic segmentation (UDA-SS) aims to
transfer knowledge from labeled source data to unlabeled target data. However,
traditional UDA-SS methods assume that category settings between source and
target domains are known, which is unrealistic in real-world scenarios. This
leads to performance degradation if private classes exist. To address this
limitation, we propose Universal Domain Adaptation for Semantic Segmentation
(UniDA-SS), achieving robust adaptation even without prior knowledge of
category settings. We define the problem in the UniDA-SS scenario
|    | reference                                                        |   date | key idea/summary                                                                                                                                                                                        |
|----|------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Pyramid Scene Parsing Network](http://arxiv.org/abs/1612.01105) |    nan | The paper introduces PSPNet, a pyramid scene parsing network that leverages global context information through a pyramid pooling module, achieving state-of-the-art performance in scene parsing tasks. |
### <a id='category-adversarial-learning-approaches'></a>Adversarial Learning Approaches: 8 papers found.
Context: 
	Document 1: [Category]: «Adversarial Learning Approaches»
[Snippet]: «Convolutional neural network-based approaches for semantic segmentation rely on supervision with pixel-level ground truth, but may not generalize well to unseen image domains. As the labeling process is tedious and labor intensive, developing algorithms that can adapt source ground truth labels to the target domain is of great interest. In this paper, we propose an adversarial learning method for domain adaptation in the context of semantic segmentation. Considering semantic segmentations as structured outputs that contain spatial similarities between the source and target domains, we adopt adversarial learning in the output space. To further enhance the adapted model, we construct a multi-level adversarial network to effectively perform output space domain adaptation at different feature levels. Extensive experiments and ablation study are conducted under various domain adaptation settings, including synthetic-to-real and cross-city scenarios. We show that the proposed method performs favorably against the state-of-the-art methods in terms of accuracy and visual quality.»
[_citation_number]: «7»

	Document 2: [Category]: «Adversarial Learning Approaches»
[Snippet]: «Predicting structured outputs such as semantic segmentation relies on expensive per-pixel annotations to learn supervised models like convolutional neural networks. However, models trained on one data domain may not generalize well to other domains without annotations for model finetuning. To avoid the labor-intensive process of annotation, we develop a domain adaptation method to adapt the source data to the unlabeled target domain. We propose to learn discriminative feature representations of patches in the source domain by discovering multiple modes of patch-wise output distribution through the construction of a clustered space. With such representations as guidance, we use an adversarial learning scheme to push the feature representations of target patches in the clustered space closer to the distributions of source patches. In addition, we show that our framework is complementary to existing domain adaptation techniques and achieves consistent improvements on semantic segmentation. Extensive ablations and results are demonstrated on numerous benchmark datasets with various settings, such as synthetic-to-real and cross-city scenarios.»
[_citation_number]: «10»

	Document 3: [Category]: «Adversarial Learning Approaches»
[Snippet]: «This paper presents a novel unsupervised domain adaptation framework, called Synergistic Image and Feature Adaptation (SIFA), to effectively tackle the problem of domain shift. Domain adaptation has become an important and hot topic in recent studies on deep learning, aiming to recover performance degradation when applying the neural networks to
|    | reference                                                                                                                                              |   date | key idea/summary                                                                                                                                                                                                                                                  |
|----|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Learning to Adapt Structured Output Space for Semantic Segmentation](http://arxiv.org/abs/1802.10349)                                                 |    nan | The paper proposes an adversarial learning method for domain adaptation in semantic segmentation, enhancing model performance by adapting source labels to target domains through multi-level adversarial networks.                                               |
|  1 | [Domain Adaptation for Structured Output via Discriminative Patch
  Representations](http://arxiv.org/abs/1901.05427)                                  |    nan | The paper proposes a domain adaptation method for semantic segmentation that adapts source data to an unlabeled target domain by learning discriminative feature representations through clustered spaces and adversarial learning.                               |
|  2 | [Synergistic Image and Feature Adaptation: Towards Cross-Modality Domain
  Adaptation for Medical Image Segmentation](http://arxiv.org/abs/1901.08211) |    nan | The paper introduces SIFA, an unsupervised domain adaptation framework that improves cross-domain performance by synergistically adapting both image appearance and feature invariance through adversarial learning without target domain annotations.            |
|  3 | [PixMatch: Unsupervised Domain Adaptation via Pixelwise Consistency
  Training](http://arxiv.org/abs/2105.08128)                                       |    nan | The paper introduces a novel unsupervised domain adaptation framework for semantic segmentation that enforces pixelwise consistency between target images and their perturbed versions, achieving strong results with simplicity and efficiency.                  |
|  4 | [Bidirectional Learning for Domain Adaptation of Semantic Segmentation](http://arxiv.org/abs/1904.10620)                                               |    nan | The paper introduces a novel bidirectional learning framework for domain adaptation in semantic image segmentation, which alternately improves image translation and segmentation adaptation models, achieving superior performance compared to existing methods. |
|  5 | [Conditional generative adversarial network for structured domain adaptation]()                                                                        |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                         |
|  6 | [Domain adaptation for semantic segmentation with maximum squares loss]()                                                                              |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                         |
|  7 | [Domain adaptive semantic segmentation with self-supervised depth estimation]()                                                                        |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                         |
### <a id='category-self-training-strategies'></a>Self-Training Strategies: 8 papers found.
Context: 
	Document 1: [Category]: «Self-Training Strategies»
[Snippet]: «Since annotating pixel-level labels for semantic segmentation is laborious,
leveraging synthetic data is an attractive solution. However, due to the domain
gap between synthetic domain and real domain, it is challenging for a model
trained with synthetic data to generalize to real data. In this paper,
considering the fundamental difference between the two domains as the texture,
we propose a method to adapt to the texture of the target domain. First, we
diversity the texture of synthetic images using a style transfer algorithm. The
various textures of generated images prevent a segmentation model from
overfitting to one specific (synthetic) texture. Then, we fine-tune the model
with self-training to get direct supervision of the target texture. Our results
achieve state-of-the-art performance and we analyze the properties of the model
trained on the stylized dataset with extensive experiments.»
[_citation_number]: «8»

	Document 2: [Category]: «Self-Training Strategies»
[Snippet]: «As acquiring pixel-wise annotations of real-world images for semantic
segmentation is a costly process, a model can instead be trained with more
accessible synthetic data and adapted to real images without requiring their
annotations. This process is studied in unsupervised domain adaptation (UDA).
Even though a large number of methods propose new adaptation strategies, they
are mostly based on outdated network architectures. As the influence of recent
network architectures has not been systematically studied, we first benchmark
different network architectures for UDA and newly reveal the potential of
Transformers for UDA semantic segmentation. Based on the findings, we propose a
novel UDA method, DAFormer. The network architecture of DAFormer consists of a
Transformer encoder and a multi-level context-aware feature fusion decoder. It
is enabled by three simple but crucial training strategies to stabilize the
training and to avoid overfitting to the source domain: While (1) Rare Class
Sampling on the source domain improves the quality of the pseudo-labels by
mitigating the confirmation bias of self-training toward common classes, (2) a
Thing-Class ImageNet Feature Distance and (3) a learning rate warmup promote
feature transfer from ImageNet pretraining. DAFormer represents a major advance
in UDA. It improves the state of the art by 10.8 mIoU for GTA-to-Cityscapes and
5
|    | reference                                                                                                                                               |   date | key idea/summary                                                                                                                                                                                                                                              |
|----|---------------------------------------------------------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Learning Texture Invariant Representation for Domain Adaptation of
  Semantic Segmentation](http://arxiv.org/abs/2003.00867)                           |    nan | The paper proposes a method to adapt segmentation models trained on synthetic data to real-world textures by diversifying synthetic textures using style transfer and fine-tuning with self-training.                                                         |
|  1 | [DAFormer: Improving Network Architectures and Training Strategies for
  Domain-Adaptive Semantic Segmentation](http://arxiv.org/abs/2111.14887)        |    nan | DAFormer is a novel unsupervised domain adaptation method for semantic segmentation that leverages Transformers and three training strategies to improve performance on real-world datasets.                                                                  |
|  2 | [Confidence Regularized Self-Training](http://arxiv.org/abs/1908.09822)                                                                                 |    nan | The paper proposes a confidence regularized self-training (CRST) framework to address the issue of noisy pseudo-labels in domain adaptation by introducing label and model regularization to improve the reliability of predictions.                          |
|  3 | [Constructing Self-motivated Pyramid Curriculums for Cross-Domain
  Semantic Segmentation: A Non-Adversarial Approach](http://arxiv.org/abs/1908.09547) |    nan | The paper introduces PyCDA, a novel approach for semantic segmentation domain adaptation that uses a pyramid curriculum derived from the segmentation network itself, improving generalization without requiring additional models or complex optimization.   |
|  4 | [Prototypical Pseudo Label Denoising and Target Structure Learning for
  Domain Adaptive Semantic Segmentation](http://arxiv.org/abs/2101.10979)        |    nan | The paper proposes a method for unsupervised domain adaptation that uses representative prototypes and feature distances to improve pseudo label quality and align target features, achieving better performance than existing methods.                       |
|  5 | [DACS: Domain Adaptation via Cross-domain Mixed Sampling](http://arxiv.org/abs/2007.08702)                                                              |    nan | The paper proposes DACS, a method for unsupervised domain adaptation that improves performance by mixing images and labels from source and target domains, along with pseudo-labels, to achieve state-of-the-art results on the GTA5 to Cityscapes benchmark. |
|  6 | [Unsupervised domain adaptation for semantic segmentation via class-balanced self-training]()                                                           |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                     |
|  7 | [Uncertainty-aware pseudo label refinery for domain adaptive semantic segmentation]()                                                                   |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                     |
### <a id='category-class-separation-mechanisms'></a>Class Separation Mechanisms: 2 papers found.
Context: 
	Document 1: [Category]: «Class Separation Mechanisms»
[Snippet]: «Convolutional neural network-based approaches have achieved remarkable progress in semantic segmentation. However, these approaches heavily rely on annotated data which are labor intensive. To cope with this limitation, automatically annotated data generated from graphic engines are used to train segmentation models. However, the models trained from synthetic data are difficult to transfer to real images. To tackle this issue, previous works have considered directly adapting models from the source data to the unlabeled target data (to reduce the inter-domain gap). Nonetheless, these techniques do not consider the large distribution gap among the target data itself (intra-domain gap). In this work, we propose a two-step self-supervised domain adaptation approach to minimize the inter-domain and intra-domain gap together. First, we conduct the inter-domain adaptation of the model; from this adaptation, we separate the target domain into an easy and hard split using an entropy-based ranking function. Finally, to decrease the intra-domain gap, we propose to employ a self-supervised adaptation technique from the easy to the hard split. Experimental results on numerous benchmark datasets highlight the effectiveness of our method against existing state-of-the-art approaches. The source code is available at https://github.com/feipan664/IntraDA.git.»
[_citation_number]: «9»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-28T15:14:11+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1506.04579)\]. Further details \[[6](http://arxiv.org/abs/2012.15840)\]\[[7](http://arxiv.org/abs/1802.10349)\]\[[8](http://arxiv.org/abs/2003.00867)\]\[[9](http://arxiv.org/abs/2004.07703)\]\[[10](http://arxiv.org/abs/1901.05427)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Unsupervised domain adaptation for semantic segmentation (UDA-SS) aims to transfer knowledge from labeled source data to unlabeled target data. However, traditional UDA-SS methods assume that category settings between source and target
|    | reference                                                                                                                    |   date | key idea/summary                                                                                                                                                                                        |
|----|------------------------------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Unsupervised Intra-domain Adaptation for Semantic Segmentation through
  Self-Supervision](http://arxiv.org/abs/2004.07703) |    nan | This work proposes a two-step self-supervised domain adaptation approach to simultaneously minimize the inter-domain and intra-domain gaps in semantic segmentation models trained with synthetic data. |
|  1 | [Ssf-dan: Separated semantic feature based domain adaptation network for semantic segmentation]()                            |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                               |
### <a id='category-universal-domain-adaptation-frameworks'></a>Universal Domain Adaptation Frameworks: 2 papers found.
Context: 
	Document 1: [Category]: «Universal Domain Adaptation Frameworks»
[Snippet]: «Unsupervised domain adaptation enables intelligent models to transfer
knowledge from a labeled source domain to a similar but unlabeled target
domain. Recent study reveals that knowledge can be transferred from one source
domain to another unknown target domain, called Universal Domain Adaptation
(UDA). However, in the real-world application, there are often more than one
source domain to be exploited for domain adaptation. In this paper, we formally
propose a more general domain adaptation setting, universal multi-source domain
adaptation (UMDA), where the label sets of multiple source domains can be
different and the label set of target domain is completely unknown. The main
challenges in UMDA are to identify the common label set between each source
domain and target domain, and to keep the model scalable as the number of
source domains increases. To address these challenges, we propose a universal
multi-source adaptation network (UMAN) to solve the domain adaptation problem
without increasing the complexity of the model in various UMDA settings. In
UMAN, we estimate the reliability of each known class in the common label set
via the prediction margin, which helps adversarial training to better align the
distributions of multiple source domains and target domain in the common label
set. Moreover, the theoretical guarantee for UMAN is also provided. Massive
experimental results show that existing UDA and multi-source DA (MDA) methods
cannot be directly applied to UMDA and the proposed UMAN achieves the
state-of-the-art performance in various UMDA settings.»
[_citation_number]: «20»

	Document 2: [Category]: «Universal Domain Adaptation Frameworks»
[Snippet]: «Unsupervised domain adaptation methods traditionally assume that all source
categories are present in the target domain. In practice, little may be known
about the category overlap between the two domains. While some methods address
target settings with either partial or open-set categories, they assume that
the particular setting is known a priori. We propose a more universally
applicable domain adaptation framework that can handle arbitrary category
shift, called Domain Adaptative Neighborhood Clustering via Entropy
optimization (DANCE). DANCE combines two novel ideas: First, as we cannot fully
rely on source categories to learn features discriminative for the target, we
propose a novel neighborhood clustering technique to learn the structure of the
|    | reference                                                                               |   date | key idea/summary                                                                                                                                                                                                                                                                                                               |
|----|-----------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Universal Multi-Source Domain Adaptation](http://arxiv.org/abs/2011.02594)             |    nan | The paper introduces Universal Multi-Source Domain Adaptation (UMDA), a more general setting where knowledge is transferred from multiple source domains with different label sets to an unlabeled target domain, and proposes a scalable solution called UMAN to address the challenges of domain adaptation in this setting. |
|  1 | [Universal Domain Adaptation through Self Supervision](http://arxiv.org/abs/2002.07953) |    nan | DANCE is a domain adaptation framework that handles arbitrary category shifts by combining self-supervised neighborhood clustering and entropy-based feature alignment/rejection to improve performance across open-set, open-partial, and partial domain adaptation settings.                                                 |
### <a id='category-open-set-domain-adaptation'></a>Open-Set Domain Adaptation: 1 papers found.
Context: 
	Document 1: [Category]: «Open-Set Domain Adaptation»
[Snippet]: «Open Set Domain Adaptation (OSDA) bridges the domain gap between a labeled source domain and an unlabeled target domain, while also rejecting target classes that are not present in the source. To avoid negative transfer, OSDA can be tackled by first separating the known/unknown target samples and then aligning known target samples with the source data. We propose a novel method to addresses both these problems using the self-supervised task of rotation recognition. Moreover, we assess the performance with a new open set metric that properly balances the contribution of recognizing the known classes and rejecting the unknown samples. Comparative experiments with existing OSDA methods on the standard Office-31 and Office-Home benchmarks show that: (i) our method outperforms its competitors, (ii) reproducibility for this field is a crucial issue to tackle, (iii) our metric provides a reliable tool to allow fair open set evaluation.»
[_citation_number]: «21»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-28T15:14:11+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1506.04579)\]. Further details \[[6](http://arxiv.org/abs/2012.15840)\]\[[7](http://arxiv.org/abs/1802.10349)\]\[[8](http://arxiv.org/abs/2003.00867)\]\[[9](http://arxiv.org/abs/2004.07703)\]\[[10](http://arxiv.org/abs/1901.05427)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Unsupervised domain adaptation for semantic segmentation (UDA-SS) aims to transfer knowledge from labeled source data to unlabeled target data. However, traditional UDA-SS methods assume that category settings between source and target domains are known, which is unrealistic in real-world scenarios. This leads to performance degradation if private classes exist. To address this limitation, we propose Universal Domain Adaptation for Semantic Segmentation (UniDA-SS), achieving robust adaptation even without prior knowledge of category settings. We define the problem in the UniDA-
|    | reference                                                                                                |   date | key idea/summary                                                                                                                                                                                        |
|----|----------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [On the Effectiveness of Image Rotation for Open Set Domain Adaptation](http://arxiv.org/abs/2007.12360) |    nan | The paper proposes a novel method for Open Set Domain Adaptation that uses self-supervised rotation recognition to address domain gaps and introduces a new metric for evaluating open set performance. |
### <a id='category-threshold-learning-for-unknown-classes'></a>Threshold Learning for Unknown Classes: 1 papers found.
Context: 
	Document 1: [Category]: «Threshold Learning for Unknown Classes»
[Snippet]: «Universal Domain Adaptation (UNDA) aims to handle both domain-shift and
category-shift between two datasets, where the main challenge is to transfer
knowledge while rejecting unknown classes which are absent in the labeled
source data but present in the unlabeled target data. Existing methods manually
set a threshold to reject unknown samples based on validation or a pre-defined
ratio of unknown samples, but this strategy is not practical. In this paper, we
propose a method to learn the threshold using source samples and to adapt it to
the target domain. Our idea is that a minimum inter-class distance in the
source domain should be a good threshold to decide between known or unknown in
the target. To learn the inter-and intra-class distance, we propose to train a
one-vs-all classifier for each class using labeled source data. Then, we adapt
the open-set classifier to the target domain by minimizing class entropy. The
resulting framework is the simplest of all baselines of UNDA and is insensitive
to the value of a hyper-parameter yet outperforms baselines with a large
margin.»
[_citation_number]: «23»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-28T15:14:11+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1506.04579)\]. Further details \[[6](http://arxiv.org/abs/2012.15840)\]\[[7](http://arxiv.org/abs/1802.10349)\]\[[8](http://arxiv.org/abs/2003.00867)\]\[[9](http://arxiv.org/abs/2004.07703)\]\[[10](http://arxiv.org/abs/1901.05427)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Unsupervised domain adaptation for semantic segmentation (UDA-SS) aims to
transfer knowledge from labeled source data to unlabeled target data. However,
traditional UDA-SS methods assume that category settings between source and
target domains are known, which is unrealistic in real-world scenarios. This
leads to performance degradation if private
|    | reference                                                                                     |   date | key idea/summary                                                                                                                                                                                                                             |
|----|-----------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [OVANet: One-vs-All Network for Universal Domain Adaptation](http://arxiv.org/abs/2104.03344) |    nan | The paper proposes a method for Universal Domain Adaptation (UNDA) that learns a threshold to distinguish known and unknown classes in the target domain using source samples and adapts an open-set classifier by minimizing class entropy. |
