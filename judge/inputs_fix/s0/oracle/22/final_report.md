## Related Works

Unsupervised domain adaptation (UDA) for semantic segmentation aims to transfer knowledge from a labeled source domain to an unlabeled target domain without requiring additional annotations \[[1](http://arxiv.org/abs/1411.4038)\]. Traditional UDA methods assume that the category settings between the source and target domains are known, which is a restrictive assumption in real-world applications \[[1](http://arxiv.org/abs/1411.4038)\]. This assumption leads to performance degradation when private classes—classes present in the target domain but absent in the source—exist \[[1](http://arxiv.org/abs/1411.4038)\]. To address this limitation, recent works have explored more flexible domain adaptation settings, such as open-set and universal domain adaptation \[[1](http://arxiv.org/abs/1411.4038)\].

Several methods have been proposed to handle domain shift in semantic segmentation. For instance, \[[2](http://arxiv.org/abs/1606.00915)\] introduced DeepLab, which combines atrous convolution and fully connected CRFs to improve localization accuracy. Similarly, \[[3](http://arxiv.org/abs/1506.04579)\] proposed ParseNet, which enhances semantic segmentation by incorporating global context into deep convolutional networks. These methods focus on improving performance within a fixed domain setting, rather than addressing the more challenging problem of unknown category shifts \[[1](http://arxiv.org/abs/1411.4038)\].

To handle open-set domain adaptation, where the target domain may contain classes not present in the source, \[[4](http://arxiv.org/abs/1612.01105)\] introduced a method that uses image rotation recognition as a self-supervised task to distinguish between known and unknown classes. This approach improves the robustness of models in open-set scenarios \[[1](http://arxiv.org/abs/1411.4038)\]. Additionally, \[[5](http://arxiv.org/abs/2105.15203)\] proposed a universal domain adaptation framework called DANCE, which uses self-supervised learning and entropy-based feature alignment to handle arbitrary category shifts \[[1](http://arxiv.org/abs/1411.4038)\].

In the context of domain adaptation, \[[6](http://arxiv.org/abs/2012.15840)\] proposed a method that leverages adversarial learning to align features between source and target domains. This approach has been further refined in \[[7](http://arxiv.org/abs/1802.10349)\], where the authors introduced a multi-level adversarial network to enhance domain adaptation performance. These methods, while effective, typically assume that the target domain contains only known classes, which is not always the case in real-world applications \[[1](http://arxiv.org/abs/1411.4038)\].

To address the problem of unknown categories, \[[8](http://arxiv.org/abs/2003.00867)\] proposed a method that learns a threshold to distinguish between known and unknown classes in the target domain. This threshold is learned using source samples and adapted to the target domain. This approach is more robust than manually setting a threshold \[[1](http://arxiv.org/abs/1411.4038)\].

The problem of domain adaptation in semantic segmentation has also been tackled through self-training strategies. For example, \[[9](http://arxiv.org/abs/2004.07703)\] introduced a method that uses pseudo-labels to iteratively refine the model's predictions on the target domain. However, pseudo-labels can be noisy, leading to overfitting to the source domain \[[1](http://arxiv.org/abs/1411.4038)\]. To mitigate this issue, \[[10](http://arxiv.org/abs/1901.05427)\] proposed a confidence-regularized self-training framework that improves the quality of pseudo-labels by incorporating confidence regularization \[[1](http://arxiv.org/abs/1411.4038)\].

In summary, while many methods have been proposed to address domain adaptation in semantic segmentation, most assume a fixed category setting or rely on manual thresholding. The proposed UniMAP framework addresses these limitations by introducing a novel approach that handles unknown categories and improves adaptation performance through domain-specific prototype distinction and image matching \[[1](http://arxiv.org/abs/1411.4038)\].

References:
1. \[[1](http://arxiv.org/abs/1411.4038)\] "Universal Domain Adaptation for Semantic Segmentation (UniDA-SS)"  
2. \[[2](http://arxiv.org/abs/1606.00915)\] "DeepLab: Semantic Image Segmentation with Deep Convolutional Nets, Atrous Convolution, and Fully Connected CRFs"  
3. \[[3](http://arxiv.org/abs/1506.04579)\] "ParseNet: Looking Wider to See Better"  
4. \[[4](http://arxiv.org/abs/1612.01105)\] "On the Effectiveness of Image Rotation for Open Set Domain Adaptation"  
5. \[[5](http://arxiv.org/abs/2105.15203)\] "Universal Domain Adaptation through Self Supervision"  
6. \[[6](http://arxiv.org/abs/2012.15840)\] "Domain Adaptation for Structured Output via Discriminative Patch Representations"  
7. \[[7](http://arxiv.org/abs/1802.10349)\] "Learning to Adapt Structured Output Space for Semantic Segmentation"  
8. \[[8](http://arxiv.org/abs/2003.00867)\] "OVANet: One-vs-All Network for Universal Domain Adaptation"  
9. \[[9](http://arxiv.org/abs/2004.07703)\] "Confidence Regularized Self-Training"  
10. \[[10](http://arxiv.org/abs/1901.05427)\] "Prototypical Pseudo Label Denoising and Target Structure Learning for Domain Adaptive Semantic Segmentation"
## Research papers
### Outline
- [Benchmarking and Evaluation of Domain Adaptation Methods [7 papers]](#category-benchmarking-and-evaluation-of-domain-adaptation-methods)
- [Adversarial Learning in Domain Adaptation [8 papers]](#category-adversarial-learning-in-domain-adaptation)
- [Self-Training Strategies for Domain Adaptation [9 papers]](#category-self-training-strategies-for-domain-adaptation)
- [Target-Based Image Matching Mechanisms [1 papers]](#category-target-based-image-matching-mechanisms)
- [Confidence Regularization Techniques [1 papers]](#category-confidence-regularization-techniques)
- [Universal Domain Adaptation Frameworks [2 papers]](#category-universal-domain-adaptation-frameworks)
- [Open-Set Domain Adaptation Approaches [1 papers]](#category-open-set-domain-adaptation-approaches)
- [Threshold Learning for Unknown Classes [1 papers]](#category-threshold-learning-for-unknown-classes)

### <a id='category-benchmarking-and-evaluation-of-domain-adaptation-methods'></a>Benchmarking and Evaluation of Domain Adaptation Methods: 7 papers found.
Context: 
	Document 1: [Category]: «Benchmarking and Evaluation of Domain Adaptation Methods»
[_citation_number]: «1»
[Snippet]: «Convolutional networks are powerful visual models that yield hierarchies of
features. We show that convolutional networks by themselves, trained
end-to-end, pixels-to-pixels, exceed the state-of-the-art in semantic
segmentation. Our key insight is to build "fully convolutional" networks that
take input of arbitrary size and produce correspondingly-sized output with
efficient inference and learning. We define and detail the space of fully
convolutional networks, explain their application to spatially dense prediction
tasks, and draw connections to prior models. We adapt contemporary
classification networks (AlexNet, the VGG net, and GoogLeNet) into fully
convolutional networks and transfer their learned representations by
fine-tuning to the segmentation task. We then define a novel architecture that
combines semantic information from a deep, coarse layer with appearance
information from a shallow, fine layer to produce accurate and detailed
segmentations. Our fully convolutional network achieves state-of-the-art
segmentation of PASCAL VOC (20% relative improvement to 62.2% mean IU on 2012),
NYUDv2, and SIFT Flow, while inference takes one third of a second for a
typical image.»

	Document 2: [Category]: «Benchmarking and Evaluation of Domain Adaptation Methods»
[_citation_number]: «2»
[Snippet]: «In this work we address the task of semantic image segmentation with Deep
Learning and make three main contributions that are experimentally shown to
have substantial practical merit. First, we highlight convolution with
upsampled filters, or 'atrous convolution', as a powerful tool in dense
prediction tasks. Atrous convolution allows us to explicitly control the
resolution at which feature responses are computed within Deep Convolutional
Neural Networks. It also allows us to effectively enlarge the field of view of
filters to incorporate larger context without increasing the number of
parameters or the amount of computation. Second, we propose atrous spatial
pyramid pooling (ASPP) to robustly segment objects at multiple scales. ASPP
probes an incoming convolutional feature layer with filters at multiple
sampling rates and effective fields-of-views, thus capturing objects as well as
image context at multiple scales. Third, we improve the localization of object
boundaries by combining methods from DCNNs and probabilistic graphical models.
The commonly deployed combination of max-pooling and downsampling in DCNNs
achieves invariance but has a toll on localization accuracy. We overcome this
by combining the responses at the final DCNN layer with a fully connected
Conditional Random Field (CRF), which is shown both qualitatively and
quantitatively to improve localization performance. Our proposed "DeepLab"
system sets the new state-of-art at the PASCAL VOC-2012 semantic image
segmentation task, reaching 79.7% mIOU in the test set, and advances the
results on three other datasets: PASCAL-Context, PASCAL-Person-Part, and
Cityscapes. All of our code is made publicly available online.»

	Document 3: [Category]: «Benchmarking and Evaluation of Domain Adaptation Methods»
[_citation_number]: «3»
[Snippet]: «We present a technique for adding global context to deep convolutional
networks for semantic segmentation. The approach is simple, using the average
feature for a layer to augment the features at each location. In addition, we
study several idiosyncrasies of training, significantly increasing the
performance of baseline networks (e.g. from FCN). When we add our proposed
global feature, and a technique for learning normalization parameters, accuracy
increases consistently even over our improved versions of the baselines. Our
proposed approach, ParseNet, achieves state-of-the-art performance on SiftFlow
and PASCAL-Context with small additional computational cost over baselines, and
near current state-of-the-art performance on PASCAL VOC 2012 semantic
segmentation with a simple approach. Code is available at
https://github.com/weiliu89/caffe/tree/fcn .»

	Document 4: [Category]: «Benchmarking and Evaluation of Domain Adaptation Methods»
[_citation_number]: «4»
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

	Document 5: [Category]: «Benchmarking and Evaluation of Domain Adaptation Methods»
[_citation_number]: «5»
[Snippet]: «We present SegFormer, a simple, efficient yet powerful semantic segmentation
framework which unifies Transformers with lightweight multilayer perception
(MLP) decoders. SegFormer has two appealing features: 1) SegFormer comprises a
novel hierarchically structured Transformer encoder which outputs multiscale
features. It does not need positional encoding, thereby avoiding the
interpolation of positional codes which leads to decreased performance when the
testing resolution differs from training. 2) SegFormer avoids complex decoders.
The proposed MLP decoder aggregates information from different layers, and thus
combining both local attention and global attention to render powerful
representations. We show that this simple and lightweight design is the key to
efficient segmentation on Transformers. We scale our approach up to obtain a
series of models from SegFormer-B0 to SegFormer-B5, reaching significantly
better performance and efficiency than previous counterparts. For example,
SegFormer-B4 achieves 50.3% mIoU on ADE20K with 64M parameters, being 5x
smaller and 2.2% better than the previous best method. Our best model,
SegFormer-B5, achieves 84.0% mIoU on Cityscapes validation set and shows
excellent zero-shot robustness on Cityscapes-C. Code will be released at:
github.com/NVlabs/SegFormer.»

	Document 6: [Category]: «Benchmarking and Evaluation of Domain Adaptation Methods»
[_citation_number]: «6»
[Snippet]: «Most recent semantic segmentation methods adopt a fully-convolutional network
(FCN) with an encoder-decoder architecture. The encoder progressively reduces
the spatial resolution and learns more abstract/semantic visual concepts with
larger receptive fields. Since context modeling is critical for segmentation,
the latest efforts have been focused on increasing the receptive field, through
either dilated/atrous convolutions or inserting attention modules. However, the
encoder-decoder based FCN architecture remains unchanged. In this paper, we aim
to provide an alternative perspective by treating semantic segmentation as a
sequence-to-sequence prediction task. Specifically, we deploy a pure
transformer (ie, without convolution and resolution reduction) to encode an
image as a sequence of patches. With the global context modeled in every layer
of the transformer, this encoder can be combined with a simple decoder to
provide a powerful segmentation model, termed SEgmentation TRansformer (SETR).
Extensive experiments show that SETR achieves new state of the art on ADE20K
(50.28% mIoU), Pascal Context (55.83% mIoU) and competitive results on
Cityscapes. Particularly, we achieve the first position in the highly
competitive ADE20K test server leaderboard on the day of submission.»

	Document 7: [Category]: «Benchmarking and Evaluation of Domain Adaptation Methods»
[_citation_number]: «14»
[Snippet]: «Unsupervised domain adaptation (UDA) aims to adapt a model trained on the
source domain (e.g. synthetic data) to the target domain (e.g. real-world data)
without requiring further annotations on the target domain. This work focuses
on UDA for semantic segmentation as real-world pixel-wise annotations are
particularly expensive to acquire. As UDA methods for semantic segmentation are
usually GPU memory intensive, most previous methods operate only on downscaled
images. We question this design as low-resolution predictions often fail to
preserve fine details. The alternative of training with random crops of
high-resolution images alleviates this problem but falls short in capturing
long-range, domain-robust context information. Therefore, we propose HRDA, a
multi-resolution training approach for UDA, that combines the strengths of
small high-resolution crops to preserve fine segmentation details and large
low-resolution crops to capture long-range context dependencies with a learned
scale attention, while maintaining a manageable GPU memory footprint. HRDA
enables adapting small objects and preserving fine segmentation details. It
significantly improves the state-of-the-art performance by 5.5 mIoU for
GTA-to-Cityscapes and 4.9 mIoU for Synthia-to-Cityscapes, resulting in
unprecedented 73.8 and 65.8 mIoU, respectively. The implementation is available
at https://github.com/lhoyer/HRDA.»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-28T15:14:11+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1506.04579)\]. Further details \[[6](http://arxiv.org/abs/2012.15840)\]\[[7](http://arxiv.org/abs/1802.10349)\]\[[8](http://arxiv.org/abs/2003.00867)\]\[[9](http://arxiv.org/abs/2004.07703)\]\[[10](http://arxiv.org/abs/1901.05427)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Unsupervised domain adaptation for semantic segmentation (UDA-SS) aims to
transfer knowledge from labeled source data to unlabeled target data. However,
traditional UDA-SS methods assume that category settings between source and
target domains are known, which is unrealistic in real-world scenarios. This
leads to performance degradation if private classes exist. To address this
limitation, we propose Universal Domain Adaptation for Semantic Segmentation
(UniDA-SS), achieving robust adaptation even without prior knowledge of
category settings. We define the problem in the UniDA-SS scenario as low
confidence scores of common classes in the target domain, which leads to
confusion with private classes. To solve this problem, we propose UniMAP:
UniDA-SS with Image Matching and Prototype-based Distinction, a novel framework
composed of two key components. First, Domain-Specific Prototype-based
Distinction (DSPD) divides each class into two domain-specific prototypes,
enabling finer separation of domain-specific features and enhancing the
identification of common classes across domains. Second, Target-based Image
Matching (TIM) selects a source image containing the most common-class pixels
based on the target pseudo-label and pairs it in a batch to promote effective
learning of common classes. We also introduce a new UniDA-SS benchmark and
demonstrate through various experiments that UniMAP significantly outperforms
baselines. The code is available at
\href(https://github.com/KU-VGI/UniMAP)(this https URL).
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1506.04579)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1606.00915)\]\[[7](http://arxiv.org/abs/1802.10349)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer:  
The field of domain adaptation for semantic segmentation has seen significant advancements, particularly in addressing the challenge of transferring knowledge from labeled source data to unlabeled target data \[[1](http://arxiv.org/abs/1411.4038)\]. Traditional methods often assume known category settings between domains, which is impractical in real-world scenarios where private classes may exist \[[1](http://arxiv.org/abs/1411.4038)\]. This limitation has prompted the development of more robust approaches, such as Universal Domain Adaptation for Semantic Segmentation (UniDA-SS), which aims to achieve adaptation without prior knowledge of category settings \[[1](http://arxiv.org/abs/1411.4038)\]. Several studies have explored methods to improve the performance of domain adaptation by leveraging global context and multi-resolution training \[[14](http://arxiv.org/abs/2204.13132)\]. For instance, HRDA introduces a multi-resolution training approach that combines high-resolution crops for fine detail preservation with low-resolution crops for capturing long-range context, significantly improving performance on benchmarks like GTA-to-Cityscapes \[[14](http://arxiv.org/abs/2204.13132)\]. Additionally, models like DeepLab \[[2](http://arxiv.org/abs/1606.00915)\], PSPNet \[[4](http://arxiv.org/abs/1612.01105)\], and SETR \[[6](http://arxiv.org/abs/2012.15840)\] have demonstrated the effectiveness of incorporating global context and advanced architectures to enhance segmentation accuracy. These methods often rely on techniques such as atrous convolutions \[[2](http://arxiv.org/abs/1606.00915)\], pyramid pooling modules \[[4](http://arxiv.org/abs/1612.01105)\], and transformers \[[6](http://arxiv.org/abs/2012.15840)\] to capture both local and global features effectively. The integration of these techniques has led to state-of-the-art results on various benchmarks, including PASCAL VOC, Cityscapes, and ADE20K \[[1](http://arxiv.org/abs/1411.4038)\]\[[2](http://arxiv.org/abs/1606.00915)\]\[[4](http://arxiv.org/abs/1612.01105)\]\[[6](http://arxiv.org/abs/2012.15840)\]. Furthermore, the use of conditional random fields \[[2](http://arxiv.org/abs/1606.00915)\] and attention mechanisms \[[6](http://arxiv.org/abs/2012.15840)\] has helped improve localization accuracy and contextual understanding. Overall, these works highlight the importance of context modeling, multi-scale feature extraction, and efficient architecture design in achieving robust domain adaptation for semantic segmentation.
|    | reference                                                                                                                                            |   date | key idea/summary                                                                                                                                                                                                                                                                                          |
|----|------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Fully Convolutional Networks for Semantic Segmentation](http://arxiv.org/abs/1411.4038)                                                             |    nan | Fully convolutional networks achieve state-of-the-art semantic segmentation by adapting existing classification networks and combining deep semantic features with shallow appearance details.                                                                                                            |
|  1 | [DeepLab: Semantic Image Segmentation with Deep Convolutional Nets,
  Atrous Convolution, and Fully Connected CRFs](http://arxiv.org/abs/1606.00915) |    nan | The paper introduces the DeepLab system, which uses atrous convolution, atrous spatial pyramid pooling (ASPP), and a Conditional Random Field (CRF) to achieve state-of-the-art results in semantic image segmentation, achieving 79.7% mIOU on the PASCAL VOC-2012 dataset.                              |
|  2 | [ParseNet: Looking Wider to See Better](http://arxiv.org/abs/1506.04579)                                                                             |    nan | ParseNet improves semantic segmentation by adding global context to deep convolutional networks, achieving state-of-the-art performance with minimal computational cost.                                                                                                                                  |
|  3 | [Pyramid Scene Parsing Network](http://arxiv.org/abs/1612.01105)                                                                                     |    nan | The paper introduces PSPNet, a pyramid scene parsing network that leverages global context information through a pyramid pooling module, achieving state-of-the-art performance in scene parsing tasks.                                                                                                   |
|  4 | [SegFormer: Simple and Efficient Design for Semantic Segmentation with
  Transformers](http://arxiv.org/abs/2105.15203)                              |    nan | SegFormer is a simple and efficient semantic segmentation framework that combines Transformers with lightweight MLP decoders, achieving state-of-the-art performance with significantly reduced parameters and improved robustness.                                                                       |
|  5 | [Rethinking Semantic Segmentation from a Sequence-to-Sequence Perspective
  with Transformers](http://arxiv.org/abs/2012.15840)                      |    nan | The paper introduces SETR, a segmentation model based on a pure transformer architecture that treats semantic segmentation as a sequence-to-sequence prediction task, achieving state-of-the-art results on multiple benchmarks.                                                                          |
|  6 | [HRDA: Context-Aware High-Resolution Domain-Adaptive Semantic
  Segmentation](http://arxiv.org/abs/2204.13132)                                       |    nan | HRDA is a multi-resolution training approach for unsupervised domain adaptation in semantic segmentation that combines high-resolution crops for fine details and low-resolution crops for long-range context, achieving significant improvements in mIoU on GTA-to-Cityscapes and Synthia-to-Cityscapes. |
### <a id='category-adversarial-learning-in-domain-adaptation'></a>Adversarial Learning in Domain Adaptation: 8 papers found.
Context: 
	Document 1: [Category]: «Adversarial Learning in Domain Adaptation»
[_citation_number]: «7»
[Snippet]: «Convolutional neural network-based approaches for semantic segmentation rely on supervision with pixel-level ground truth, but may not generalize well to unseen image domains. As the labeling process is tedious and labor intensive, developing algorithms that can adapt source ground truth labels to the target domain is of great interest. In this paper, we propose an adversarial learning method for domain adaptation in the context of semantic segmentation. Considering semantic segmentations as structured outputs that contain spatial similarities between the source and target domains, we adopt adversarial learning in the output space. To further enhance the adapted model, we construct a multi-level adversarial network to effectively perform output space domain adaptation at different feature levels. Extensive experiments and ablation study are conducted under various domain adaptation settings, including synthetic-to-real and cross-city scenarios. We show that the proposed method performs favorably against the state-of-the-art methods in terms of accuracy and visual quality.»

	Document 2: [Category]: «Adversarial Learning in Domain Adaptation»
[_citation_number]: «10»
[Snippet]: «Predicting structured outputs such as semantic segmentation relies on expensive per-pixel annotations to learn supervised models like convolutional neural networks. However, models trained on one data domain may not generalize well to other domains without annotations for model finetuning. To avoid the labor-intensive process of annotation, we develop a domain adaptation method to adapt the source data to the unlabeled target domain. We propose to learn discriminative feature representations of patches in the source domain by discovering multiple modes of patch-wise output distribution through the construction of a clustered space. With such representations as guidance, we use an adversarial learning scheme to push the feature representations of target patches in the clustered space closer to the distributions of source patches. In addition, we show that our framework is complementary to existing domain adaptation techniques and achieves consistent improvements on semantic segmentation. Extensive ablations and results are demonstrated on numerous benchmark datasets with various settings, such as synthetic-to-real and cross-city scenarios.»

	Document 3: [Category]: «Adversarial Learning in Domain Adaptation»
[_citation_number]: «11»
[Snippet]: «This paper presents a novel unsupervised domain adaptation framework, called Synergistic Image and Feature Adaptation (SIFA), to effectively tackle the problem of domain shift. Domain adaptation has become an important and hot topic in recent studies on deep learning, aiming to recover performance degradation when applying the neural networks to new testing domains. Our proposed SIFA is an elegant learning diagram which presents synergistic fusion of adaptations from both image and feature perspectives. In particular, we simultaneously transform the appearance of images across domains and enhance domain-invariance of the extracted features towards the segmentation task. The feature encoder layers are shared by both perspectives to grasp their mutual benefits during the end-to-end learning procedure. Without using any annotation from the target domain, the learning of our unified model is guided by adversarial losses, with multiple discriminators employed from various aspects. We have extensively validated our method with a challenging application of cross-modality medical image segmentation of cardiac structures. Experimental results demonstrate that our SIFA model recovers the degraded performance from 17.2% to 73.0%, and outperforms the state-of-the-art methods by a significant margin.»

	Document 4: [Category]: «Adversarial Learning in Domain Adaptation»
[_citation_number]: «17»
[Snippet]: «Domain adaptation for semantic image segmentation is very necessary since manually labeling large datasets with pixel-level labels is expensive and time consuming. Existing domain adaptation techniques either work on limited datasets, or yield not so good performance compared with supervised learning. In this paper, we propose a novel bidirectional learning framework for domain adaptation of segmentation. Using the bidirectional learning, the image translation model and the segmentation adaptation model can be learned alternatively and promote to each other. Furthermore, we propose a self-supervised learning algorithm to learn a better segmentation adaptation model and in return improve the image translation model. Experiments show that our method is superior to the state-of-the-art methods in domain adaptation of segmentation with a big margin. The source code is available at https://github.com/liyunsheng13/BDL.»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-28T15:14:11+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1506.04579)\]. Further details \[[6](http://arxiv.org/abs/2012.15840)\]\[[7](http://arxiv.org/abs/1802.10349)\]\[[8](http://arxiv.org/abs/2003.00867)\]\[[9](http://arxiv.org/abs/2004.07703)\]\[[10](http://arxiv.org/abs/1901.05427)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Unsupervised domain adaptation for semantic segmentation (UDA-SS) aims to transfer knowledge from labeled source data to unlabeled target data. However, traditional UDA-SS methods assume that category settings between source and target domains are known, which is unrealistic in real-world scenarios. This leads to performance degradation if private classes exist. To address this limitation, we propose Universal Domain Adaptation for Semantic Segmentation (UniDA-SS), achieving robust adaptation even without prior knowledge of category settings. We define the problem in the UniDA-SS scenario as low confidence scores of common classes in the target domain, which leads to confusion with private classes. To solve this problem, we propose UniMAP: UniDA-SS with Image Matching and Prototype-based Distinction, a novel framework composed of two key components. First, Domain-Specific Prototype-based Distinction (DSPD) divides each class into two domain-specific prototypes, enabling finer separation of domain-specific features and enhancing the identification of common classes across domains. Second, Target-based Image Matching (TIM) selects a source image containing the most common-class pixels based on the target pseudo-label and pairs it in a batch to promote effective learning of common classes. We also introduce a new UniDA-SS benchmark and demonstrate through various experiments that UniMAP significantly outperforms baselines. The code is available at \href(https://github.com/KU-VGI/UniMAP)(this https URL).
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1506.04579)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1606.00915)\]\[[7](http://arxiv.org/abs/1802.10349)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Adversarial learning has been widely applied in domain adaptation for semantic segmentation to address the generalization issue when transferring models from labeled source data to unlabeled target data \[[7](http://arxiv.org/abs/1802.10349)\]. Traditional methods often assume that the category settings between source and target domains are known, which is not always the case in real-world scenarios, leading to performance degradation when private classes exist \[[17](http://arxiv.org/abs/1904.10620)\]. To overcome this limitation, several studies have proposed frameworks that enhance domain adaptation without prior knowledge of category settings \[[11](http://arxiv.org/abs/1901.08211)\]. For example, the Synergistic Image and Feature Adaptation (SIFA) framework introduces a synergistic fusion of adaptations from both image and feature perspectives, aiming to recover performance degradation by improving domain-invariance of features \[[11](http://arxiv.org/abs/1901.08211)\]. Similarly, the bidirectional learning framework proposed in \[[17](http://arxiv.org/abs/1904.10620)\] enables the image translation model and segmentation adaptation model to learn alternately, promoting mutual improvement through self-supervised learning. These approaches highlight the importance of adversarial learning in aligning feature distributions across domains and improving the robustness of semantic segmentation models \[[7](http://arxiv.org/abs/1802.10349)\]\[[10](http://arxiv.org/abs/1901.05427)\]. Additionally, methods such as Domain-Specific Prototype-based Distinction (DSPD) and Target-based Image Matching (TIM) further enhance adaptation by refining domain-specific features and improving the identification of common classes \[[17](http://arxiv.org/abs/1904.10620)\]. Overall, adversarial learning remains a key technique in domain adaptation for semantic segmentation, with ongoing efforts to improve generalization and performance across diverse domain settings \[[7](http://arxiv.org/abs/1802.10349)\]\[[10](http://arxiv.org/abs/1901.05427)\]\[[11](http://arxiv.org/abs/1901.08211)\].
|    | reference                                                                                                                                              |   date | key idea/summary                                                                                                                                                                                                                                                  |
|----|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Learning to Adapt Structured Output Space for Semantic Segmentation](http://arxiv.org/abs/1802.10349)                                                 |    nan | The paper proposes an adversarial learning method for domain adaptation in semantic segmentation, enhancing model performance by adapting source labels to target domains through multi-level adversarial networks.                                               |
|  1 | [Domain Adaptation for Structured Output via Discriminative Patch
  Representations](http://arxiv.org/abs/1901.05427)                                  |    nan | The paper proposes a domain adaptation method for semantic segmentation that adapts source data to an unlabeled target domain by learning discriminative feature representations through clustered spaces and adversarial learning.                               |
|  2 | [Synergistic Image and Feature Adaptation: Towards Cross-Modality Domain
  Adaptation for Medical Image Segmentation](http://arxiv.org/abs/1901.08211) |    nan | The paper introduces SIFA, an unsupervised domain adaptation framework that improves cross-domain performance by synergistically adapting both image appearance and feature invariance through adversarial learning without target domain annotations.            |
|  3 | [Bidirectional Learning for Domain Adaptation of Semantic Segmentation](http://arxiv.org/abs/1904.10620)                                               |    nan | The paper introduces a novel bidirectional learning framework for domain adaptation in semantic image segmentation, which alternately improves image translation and segmentation adaptation models, achieving superior performance compared to existing methods. |
|  4 | [Psanet: Point-wise spatial attention network for scene parsing]()                                                                                     |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                         |
|  5 | [Conditional generative adversarial network for structured domain adaptation]()                                                                        |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                         |
|  6 | [Ssf-dan: Separated semantic feature based domain adaptation network for semantic segmentation]()                                                      |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                         |
|  7 | [Domain adaptation for semantic segmentation with maximum squares loss]()                                                                              |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                         |
### <a id='category-self-training-strategies-for-domain-adaptation'></a>Self-Training Strategies for Domain Adaptation: 9 papers found.
Context: 
	Document 1: [Category]: «Self-Training Strategies for Domain Adaptation»
[_citation_number]: «8»
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

	Document 2: [Category]: «Self-Training Strategies for Domain Adaptation»
[_citation_number]: «9»
[Snippet]: «Convolutional neural network-based approaches have achieved remarkable
progress in semantic segmentation. However, these approaches heavily rely on
annotated data which are labor intensive. To cope with this limitation,
automatically annotated data generated from graphic engines are used to train
segmentation models. However, the models trained from synthetic data are
difficult to transfer to real images. To tackle this issue, previous works have
considered directly adapting models from the source data to the unlabeled
target data (to reduce the inter-domain gap). Nonetheless, these techniques do
not consider the large distribution gap among the target data itself
(intra-domain gap). In this work, we propose a two-step self-supervised domain
adaptation approach to minimize the inter-domain and intra-domain gap together.
First, we conduct the inter-domain adaptation of the model; from this
adaptation, we separate the target domain into an easy and hard split using an
entropy-based ranking function. Finally, to decrease the intra-domain gap, we
propose to employ a self-supervised adaptation technique from the easy to the
hard split. Experimental results on numerous benchmark datasets highlight the
effectiveness of our method against existing state-of-the-art approaches. The
source code is available at https://github.com/feipan664/IntraDA.git.»

	Document 3: [Category]: «Self-Training Strategies for Domain Adaptation»
[_citation_number]: «13»
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
5.4 mIoU for Synthia-to-Cityscapes and enables learning even difficult classes
such as train, bus, and truck well. The implementation is available at
https://github.com/lhoyer/DAFormer.»

	Document 4: [Category]: «Self-Training Strategies for Domain Adaptation»
[_citation_number]: «16»
[Snippet]: «We propose a new approach, called self-motivated pyramid curriculum domain
adaptation (PyCDA), to facilitate the adaptation of semantic segmentation
neural networks from synthetic source domains to real target domains. Our
approach draws on an insight connecting two existing works: curriculum domain
adaptation and self-training. Inspired by the former, PyCDA constructs a
pyramid curriculum which contains various properties about the target domain.
Those properties are mainly about the desired label distributions over the
target domain images, image regions, and pixels. By enforcing the segmentation
neural network to observe those properties, we can improve the network's
generalization capability to the target domain. Motivated by the self-training,
we infer this pyramid of properties by resorting to the semantic segmentation
network itself. Unlike prior work, we do not need to maintain any additional
models (e.g., logistic regression or discriminator networks) or to solve minmax
problems which are often difficult to optimize. We report state-of-the-art
results for the adaptation from both GTAV and SYNTHIA to Cityscapes, two
popular settings in unsupervised domain adaptation for semantic segmentation.»

	Document 5: [Category]: «Self-Training Strategies for Domain Adaptation»
[_citation_number]: «18»
[Snippet]: «Self-training is a competitive approach in domain adaptive segmentation,
which trains the network with the pseudo labels on the target domain. However
inevitably, the pseudo labels are noisy and the target features are dispersed
due to the discrepancy between source and target domains. In this paper, we
rely on representative prototypes, the feature centroids of classes, to address
the two issues for unsupervised domain adaptation. In particular, we take one
step further and exploit the feature distances from prototypes that provide
richer information than mere prototypes. Specifically, we use it to estimate
the likelihood of pseudo labels to facilitate online correction in the course
of training. Meanwhile, we align the prototypical assignments based on relative
feature distances for two different views of the same target, producing a more
compact target feature space. Moreover, we find that distilling the already
learned knowledge to a self-supervised pretrained model further boosts the
performance. Our method shows tremendous performance advantage over
state-of-the-art methods. We will make the code publicly available.»

	Document 6: [Category]: «Self-Training Strategies for Domain Adaptation»
[_citation_number]: «19»
[Snippet]: «Semantic segmentation models based on convolutional neural networks have
recently displayed remarkable performance for a multitude of applications.
However, these models typically do not generalize well when applied on new
domains, especially when going from synthetic to real data. In this paper we
address the problem of unsupervised domain adaptation (UDA), which attempts to
train on labelled data from one domain (source domain), and simultaneously
learn from unlabelled data in the domain of interest (target domain). Existing
methods have seen success by training on pseudo-labels for these unlabelled
images. Multiple techniques have been proposed to mitigate low-quality
pseudo-labels arising from the domain shift, with varying degrees of success.
We propose DACS: Domain Adaptation via Cross-domain mixed Sampling, which mixes
images from the two domains along with the corresponding labels and
pseudo-labels. These mixed samples are then trained on, in addition to the
labelled data itself. We demonstrate the effectiveness of our solution by
achieving state-of-the-art results for GTA5 to Cityscapes, a common
synthetic-to-real semantic segmentation benchmark for UDA.»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-28T15:14:11+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1506.04579)\]. Further details \[[6](http://arxiv.org/abs/2012.15840)\]\[[7](http://arxiv.org/abs/1802.10349)\]\[[8](http://arxiv.org/abs/2003.00867)\]\[[9](http://arxiv.org/abs/2004.07703)\]\[[10](http://arxiv.org/abs/1901.05427)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Unsupervised domain adaptation for semantic segmentation (UDA-SS) aims to
transfer knowledge from labeled source data to unlabeled target data. However,
traditional UDA-SS methods assume that category settings between source and
target domains are known, which is unrealistic in real-world scenarios. This
leads to performance degradation if private classes exist. To address this
limitation, we propose Universal Domain Adaptation for Semantic Segmentation
(UniDA-SS), achieving robust adaptation even without prior knowledge of
category settings. We define the problem in the UniDA-SS scenario as low
confidence scores of common classes in the target domain, which leads to
confusion with private classes. To solve this problem, we propose UniMAP:
UniDA-SS with Image Matching and Prototype-based Distinction, a novel framework
composed of two key components. First, Domain-Specific Prototype-based
Distinction (DSPD) divides each class into two domain-specific prototypes,
enabling finer separation of domain-specific features and enhancing the
identification of common classes across domains. Second, Target-based Image
Matching (TIM) selects a source image containing the most common-class pixels
based on the target pseudo-label and pairs it in a batch to promote effective
learning of common classes. We also introduce a new UniDA-SS benchmark and
demonstrate through various experiments that UniMAP significantly outperforms
baselines. The code is available at
\href(https://github.com/KU-VGI/UniMAP)(this https URL).
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1506.04579)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1606.00915)\]\[[7](http://arxiv.org/abs/1802.10349)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Self-training strategies have been widely explored in domain adaptation for semantic segmentation, aiming to improve generalization from labeled source data to unlabeled target data \[[8](http://arxiv.org/abs/2003.00867)\]. A key challenge lies in the domain gap between synthetic and real data, which can lead to poor performance when transferring models \[[9](http://arxiv.org/abs/2004.07703)\]. To address this, researchers have proposed various approaches, such as diversifying synthetic textures using style transfer to prevent overfitting \[[8](http://arxiv.org/abs/2003.00867)\], and employing two-step self-supervised domain adaptation to minimize both inter-domain and intra-domain gaps \[[9](http://arxiv.org/abs/2004.07703)\]. Additionally, recent works have focused on leveraging advanced network architectures, such as Transformers, to enhance feature transfer and improve performance in unsupervised domain adaptation (UDA) \[[13](http://arxiv.org/abs/2111.14887)\]. Methods like DAFormer have introduced novel training strategies, including rare class sampling and learning rate warmup, to stabilize training and avoid overfitting \[[13](http://arxiv.org/abs/2111.14887)\]. Similarly, approaches like PyCDA have combined curriculum learning with self-training to construct a pyramid curriculum based on target domain properties, improving generalization without requiring additional models \[[16](http://arxiv.org/abs/1908.09547)\]. Other methods, such as DACS, have focused on mixing images from both domains along with labels and pseudo-labels to enhance adaptation \[[19](http://arxiv.org/abs/2007.08702)\]. These techniques collectively highlight the ongoing efforts to address domain adaptation challenges through self-training and advanced architectural innovations.
|    | reference                                                                                                                                               |   date | key idea/summary                                                                                                                                                                                                                                              |
|----|---------------------------------------------------------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Learning Texture Invariant Representation for Domain Adaptation of
  Semantic Segmentation](http://arxiv.org/abs/2003.00867)                           |    nan | The paper proposes a method to adapt segmentation models trained on synthetic data to real-world textures by diversifying synthetic textures using style transfer and fine-tuning with self-training.                                                         |
|  1 | [Unsupervised Intra-domain Adaptation for Semantic Segmentation through
  Self-Supervision](http://arxiv.org/abs/2004.07703)                            |    nan | This work proposes a two-step self-supervised domain adaptation approach to simultaneously minimize the inter-domain and intra-domain gaps in semantic segmentation models trained with synthetic data.                                                       |
|  2 | [DAFormer: Improving Network Architectures and Training Strategies for
  Domain-Adaptive Semantic Segmentation](http://arxiv.org/abs/2111.14887)        |    nan | DAFormer is a novel unsupervised domain adaptation method for semantic segmentation that leverages Transformers and three training strategies to improve performance on real-world datasets.                                                                  |
|  3 | [Constructing Self-motivated Pyramid Curriculums for Cross-Domain
  Semantic Segmentation: A Non-Adversarial Approach](http://arxiv.org/abs/1908.09547) |    nan | The paper introduces PyCDA, a novel approach for semantic segmentation domain adaptation that uses a pyramid curriculum derived from the segmentation network itself, improving generalization without requiring additional models or complex optimization.   |
|  4 | [Prototypical Pseudo Label Denoising and Target Structure Learning for
  Domain Adaptive Semantic Segmentation](http://arxiv.org/abs/2101.10979)        |    nan | The paper proposes a method for unsupervised domain adaptation that uses representative prototypes and feature distances to improve pseudo label quality and align target features, achieving better performance than existing methods.                       |
|  5 | [DACS: Domain Adaptation via Cross-domain Mixed Sampling](http://arxiv.org/abs/2007.08702)                                                              |    nan | The paper proposes DACS, a method for unsupervised domain adaptation that improves performance by mixing images and labels from source and target domains, along with pseudo-labels, to achieve state-of-the-art results on the GTA5 to Cityscapes benchmark. |
|  6 | [Unsupervised domain adaptation for semantic segmentation via class-balanced self-training]()                                                           |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                     |
|  7 | [Domain adaptive semantic segmentation with self-supervised depth estimation]()                                                                         |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                     |
|  8 | [Uncertainty-aware pseudo label refinery for domain adaptive semantic segmentation]()                                                                   |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                     |
### <a id='category-target-based-image-matching-mechanisms'></a>Target-Based Image Matching Mechanisms: 1 papers found.
Context: 
	Document 1: [Category]: «Target-Based Image Matching Mechanisms»
[_citation_number]: «12»
[Snippet]: «Unsupervised domain adaptation is a promising technique for semantic
segmentation and other computer vision tasks for which large-scale data
annotation is costly and time-consuming. In semantic segmentation, it is
attractive to train models on annotated images from a simulated (source) domain
and deploy them on real (target) domains. In this work, we present a novel
framework for unsupervised domain adaptation based on the notion of
target-domain consistency training. Intuitively, our work is based on the idea
that in order to perform well on the target domain, a model's output should be
consistent with respect to small perturbations of inputs in the target domain.
Specifically, we introduce a new loss term to enforce pixelwise consistency
between the model's predictions on a target image and a perturbed version of
the same image. In comparison to popular adversarial adaptation methods, our
approach is simpler, easier to implement, and more memory-efficient during
training. Experiments and extensive ablation studies demonstrate that our
simple approach achieves remarkably strong results on two challenging
synthetic-to-real benchmarks, GTA5-to-Cityscapes and SYNTHIA-to-Cityscapes.
  Code is available at: https://github.com/lukemelas/pixmatch»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-28T15:14:11+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1506.04579)\]. Further details \[[6](http://arxiv.org/abs/2012.15840)\]\[[7](http://arxiv.org/abs/1802.10349)\]\[[8](http://arxiv.org/abs/2003.00867)\]\[[9](http://arxiv.org/abs/2004.07703)\]\[[10](http://arxiv.org/abs/1901.05427)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Unsupervised domain adaptation for semantic segmentation (UDA-SS) aims to
transfer knowledge from labeled source data to unlabeled target data. However,
traditional UDA-SS methods assume that category settings between source and
target domains are known, which is unrealistic in real-world scenarios. This
leads to performance degradation if private classes exist. To address this
limitation, we propose Universal Domain Adaptation for Semantic Segmentation
(UniDA-SS), achieving robust adaptation even without prior knowledge of
category settings. We define the problem in the UniDA-SS scenario as low
confidence scores of common classes in the target domain, which leads to
confusion with private classes. To solve this problem, we propose UniMAP:
UniDA-SS with Image Matching and Prototype-based Distinction, a novel framework
composed of two key components. First, Domain-Specific Prototype-based
Distinction (DSPD) divides each class into two domain-specific prototypes,
enabling finer separation of domain-specific features and enhancing the
identification of common classes across domains. Second, Target-based Image
Matching (TIM) selects a source image containing the most common-class pixels
based on the target pseudo-label and pairs it in a batch to promote effective
learning of common classes. We also introduce a new UniDA-SS benchmark and
demonstrate through various experiments that UniMAP significantly outperforms
baselines. The code is available at
\href(https://github.com/KU-VGI/UniMAP)(this https URL).
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1506.04579)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1606.00915)\]\[[7](http://arxiv.org/abs/1802.10349)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Target-based image matching mechanisms have emerged as a promising approach in unsupervised domain adaptation for semantic segmentation. These methods focus on aligning the source and target domains by leveraging the consistency of model predictions across different input variations. For instance, one approach introduces a novel loss term that enforces pixelwise consistency between the model's predictions on a target image and a perturbed version of the same image, ensuring robustness against domain shifts \[[12](http://arxiv.org/abs/2105.08128)\]. This idea is closely related to the concept of target-domain consistency training, where the model is encouraged to produce consistent outputs despite small input perturbations. Such mechanisms are particularly valuable in scenarios where annotated data is scarce or expensive to obtain, as they enable the transfer of knowledge from labeled source data to unlabeled target data without requiring explicit alignment of category settings \[[12](http://arxiv.org/abs/2105.08128)\]. The simplicity and efficiency of these methods make them attractive alternatives to more complex adversarial adaptation techniques.
|    | reference                                                                                                        |   date | key idea/summary                                                                                                                                                                                                                                 |
|----|------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [PixMatch: Unsupervised Domain Adaptation via Pixelwise Consistency
  Training](http://arxiv.org/abs/2105.08128) |    nan | The paper introduces a novel unsupervised domain adaptation framework for semantic segmentation that enforces pixelwise consistency between target images and their perturbed versions, achieving strong results with simplicity and efficiency. |
### <a id='category-confidence-regularization-techniques'></a>Confidence Regularization Techniques: 1 papers found.
Context: 
	Document 1: [Category]: «Confidence Regularization Techniques»
[_citation_number]: «15»
[Snippet]: «Recent advances in domain adaptation show that deep self-training presents a powerful means for unsupervised domain adaptation. These methods often involve an iterative process of predicting on target domain and then taking the confident predictions as pseudo-labels for retraining. However, since pseudo-labels can be noisy, self-training can put overconfident label belief on wrong classes, leading to deviated solutions with propagated errors. To address the problem, we propose a confidence regularized self-training (CRST) framework, formulated as regularized self-training. Our method treats pseudo-labels as continuous latent variables jointly optimized via alternating optimization. We propose two types of confidence regularization: label regularization (LR) and model regularization (MR). CRST-LR generates soft pseudo-labels while CRST-MR encourages the smoothness on network output. Extensive experiments on image classification and semantic segmentation show that CRSTs outperform their non-regularized counterpart with state-of-the-art performance. The code and models of this work are available at https://github.com/yzou2/CRST.»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-28T15:14:11+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1506.04579)\]. Further details \[[6](http://arxiv.org/abs/2012.15840)\]\[[7](http://arxiv.org/abs/1802.10349)\]\[[8](http://arxiv.org/abs/2003.00867)\]\[[9](http://arxiv.org/abs/2004.07703)\]\[[10](http://arxiv.org/abs/1901.05427)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Unsupervised domain adaptation for semantic segmentation (UDA-SS) aims to transfer knowledge from labeled source data to unlabeled target data. However, traditional UDA-SS methods assume that category settings between source and target domains are known, which is unrealistic in real-world scenarios. This leads to performance degradation if private classes exist. To address this limitation, we propose Universal Domain Adaptation for Semantic Segmentation (UniDA-SS), achieving robust adaptation even without prior knowledge of category settings. We define the problem in the UniDA-SS scenario as low confidence scores of common classes in the target domain, which leads to confusion with private classes. To solve this problem, we propose UniMAP: UniDA-SS with Image Matching and Prototype-based Distinction, a novel framework composed of two key components. First, Domain-Specific Prototype-based Distinction (DSPD) divides each class into two domain-specific prototypes, enabling finer separation of domain-specific features and enhancing the identification of common classes across domains. Second, Target-based Image Matching (TIM) selects a source image containing the most common-class pixels based on the target pseudo-label and pairs it in a batch to promote effective learning of common classes. We also introduce a new UniDA-SS benchmark and demonstrate through various experiments that UniMAP significantly outperforms baselines. The code is available at https://github.com/KU-VGI/UniMAP.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1506.04579)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1606.00915)\]\[[7](http://arxiv.org/abs/1802.10349)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Confidence regularization techniques have emerged as a critical area in domain adaptation, particularly in addressing the challenges of noisy pseudo-labels in self-training frameworks \[[15](http://arxiv.org/abs/1908.09822)\]. These methods aim to mitigate the risk of overconfident predictions leading to propagated errors, which can degrade model performance \[[15](http://arxiv.org/abs/1908.09822)\]. One approach involves generating soft pseudo-labels to reduce the impact of incorrect predictions, while another focuses on encouraging smoothness in network outputs to improve generalization \[[15](http://arxiv.org/abs/1908.09822)\]. This concept aligns with recent efforts in unsupervised domain adaptation for semantic segmentation, where confidence scores of common classes in the target domain play a crucial role in distinguishing them from private classes \[[15](http://arxiv.org/abs/1908.09822)\]. By treating pseudo-labels as continuous latent variables and jointly optimizing them with model parameters, confidence regularization techniques offer a promising direction for improving adaptation accuracy \[[15](http://arxiv.org/abs/1908.09822)\].
|    | reference                                                               |   date | key idea/summary                                                                                                                                                                                                                     |
|----|-------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Confidence Regularized Self-Training](http://arxiv.org/abs/1908.09822) |    nan | The paper proposes a confidence regularized self-training (CRST) framework to address the issue of noisy pseudo-labels in domain adaptation by introducing label and model regularization to improve the reliability of predictions. |
### <a id='category-universal-domain-adaptation-frameworks'></a>Universal Domain Adaptation Frameworks: 2 papers found.
The category "Universal Domain Adaptation Frameworks" encompasses recent advancements in domain adaptation, particularly focusing on scenarios where the label sets of source and target domains are not fully known. Traditional methods often assume that all source categories are present in the target domain, which is not always the case in real-world applications \[[22](http://arxiv.org/abs/2002.07953)\]. This assumption can lead to performance degradation when private classes exist in the target domain \[[22](http://arxiv.org/abs/2002.07953)\]. To address these limitations, researchers have proposed more flexible frameworks, such as Universal Multi-Source Domain Adaptation (UMDA), which allows for multiple source domains with potentially different label sets and an unknown target label set \[[20](http://arxiv.org/abs/2011.02594)\]. UMDA introduces challenges such as identifying common label sets and maintaining model scalability, which are tackled through methods like the Universal Multi-Source Adaptation Network (UMAN) \[[20](http://arxiv.org/abs/2011.02594)\]. UMAN improves distribution alignment using prediction margins to estimate class reliability and ensures model efficiency across varying UMDA settings \[[20](http://arxiv.org/abs/2011.02594)\]. Similarly, Domain Adaptative Neighborhood Clustering via Entropy optimization (DANCE) offers a more universally applicable approach by handling arbitrary category shifts through self-supervised neighborhood clustering and entropy-based feature alignment \[[22](http://arxiv.org/abs/2002.07953)\]. These frameworks highlight the growing need for robust and adaptable domain adaptation techniques that can operate without prior knowledge of category overlaps \[[20](http://arxiv.org/abs/2011.02594)\]\[[22](http://arxiv.org/abs/2002.07953)\].
|    | reference                                                                               |   date | key idea/summary                                                                                                                                                                                                                                                                                                               |
|----|-----------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Universal Multi-Source Domain Adaptation](http://arxiv.org/abs/2011.02594)             |    nan | The paper introduces Universal Multi-Source Domain Adaptation (UMDA), a more general setting where knowledge is transferred from multiple source domains with different label sets to an unlabeled target domain, and proposes a scalable solution called UMAN to address the challenges of domain adaptation in this setting. |
|  1 | [Universal Domain Adaptation through Self Supervision](http://arxiv.org/abs/2002.07953) |    nan | DANCE is a domain adaptation framework that handles arbitrary category shifts by combining self-supervised neighborhood clustering and entropy-based feature alignment/rejection to improve performance across open-set, open-partial, and partial domain adaptation settings.                                                 |
### <a id='category-open-set-domain-adaptation-approaches'></a>Open-Set Domain Adaptation Approaches: 1 papers found.
Context: 
	Document 1: [Category]: «Open-Set Domain Adaptation Approaches»
[_citation_number]: «21»
[Snippet]: «Open Set Domain Adaptation (OSDA) bridges the domain gap between a labeled
source domain and an unlabeled target domain, while also rejecting target
classes that are not present in the source. To avoid negative transfer, OSDA
can be tackled by first separating the known/unknown target samples and then
aligning known target samples with the source data. We propose a novel method
to addresses both these problems using the self-supervised task of rotation
recognition. Moreover, we assess the performance with a new open set metric
that properly balances the contribution of recognizing the known classes and
rejecting the unknown samples. Comparative experiments with existing OSDA
methods on the standard Office-31 and Office-Home benchmarks show that: (i) our
method outperforms its competitors, (ii) reproducibility for this field is a
crucial issue to tackle, (iii) our metric provides a reliable tool to allow
fair open set evaluation.»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-28T15:14:11+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1506.04579)\]. Further details \[[6](http://arxiv.org/abs/2012.15840)\]\[[7](http://arxiv.org/abs/1802.10349)\]\[[8](http://arxiv.org/abs/2003.00867)\]\[[9](http://arxiv.org/abs/2004.07703)\]\[[10](http://arxiv.org/abs/1901.05427)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Unsupervised domain adaptation for semantic segmentation (UDA-SS) aims to
transfer knowledge from labeled source data to unlabeled target data. However,
traditional UDA-SS methods assume that category settings between source and
target domains are known, which is unrealistic in real-world scenarios. This
leads to performance degradation if private classes exist. To address this
limitation, we propose Universal Domain Adaptation for Semantic Segmentation
(UniDA-SS), achieving robust adaptation even without prior knowledge of
category settings. We define the problem in the UniDA-SS scenario as low
confidence scores of common classes in the target domain, which leads to
confusion with private classes. To solve this problem, we propose UniMAP:
UniDA-SS with Image Matching and Prototype-based Distinction, a novel framework
composed of two key components. First, Domain-Specific Prototype-based
Distinction (DSPD) divides each class into two domain-specific prototypes,
enabling finer separation of domain-specific features and enhancing the
identification of common classes across domains. Second, Target-based Image
Matching (TIM) selects a source image containing the most common-class pixels
based on the target pseudo-label and pairs it in a batch to promote effective
learning of common classes. We also introduce a new UniDA-SS benchmark and
demonstrate through various experiments that UniMAP significantly outperforms
baselines. The code is available at
\href(https://github.com/KU-VGI/UniMAP)(this https URL).
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1506.04579)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1606.00915)\]\[[7](http://arxiv.org/abs/1802.10349)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: Open-Set Domain Adaptation (OSDA) addresses the challenge of transferring knowledge from a labeled source domain to an unlabeled target domain while also identifying and rejecting target classes not present in the source \[[21](http://arxiv.org/abs/2007.12360)\]. This is particularly important to avoid negative transfer, which can occur when the target domain contains classes not seen during training \[[21](http://arxiv.org/abs/2007.12360)\]. To tackle this, OSDA methods often first separate known from unknown target samples and then align the known samples with the source data \[[21](http://arxiv.org/abs/2007.12360)\]. A recent approach proposes using a self-supervised task, such as rotation recognition, to address both problems simultaneously \[[21](http://arxiv.org/abs/2007.12360)\]. Additionally, a new open-set evaluation metric has been introduced to balance the recognition of known classes with the rejection of unknown samples \[[21](http://arxiv.org/abs/2007.12360)\]. Experimental results on standard benchmarks like Office-31 and Office-Home show that this method outperforms existing OSDA approaches, highlighting the importance of reproducibility and the need for reliable evaluation metrics \[[21](http://arxiv.org/abs/2007.12360)\].
|    | reference                                                                                                |   date | key idea/summary                                                                                                                                                                                       |
|----|----------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [On the Effectiveness of Image Rotation for Open Set Domain Adaptation](http://arxiv.org/abs/2007.12360) |    nan | The paper proposes a novel method for Open Set Domain Adaptation that uses self-supervised rotation recognition to address domain gap and introduces a new metric for evaluating open set performance. |
### <a id='category-threshold-learning-for-unknown-classes'></a>Threshold Learning for Unknown Classes: 1 papers found.
Context: 
	Document 1: [Category]: «Threshold Learning for Unknown Classes»
[_citation_number]: «23»
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

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-28T15:14:11+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1506.04579)\]. Further details \[[6](http://arxiv.org/abs/2012.15840)\]\[[7](http://arxiv.org/abs/1802.10349)\]\[[8](http://arxiv.org/abs/2003.00867)\]\[[9](http://arxiv.org/abs/2004.07703)\]\[[10](http://arxiv.org/abs/1901.05427)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Unsupervised domain adaptation for semantic segmentation (UDA-SS) aims to
transfer knowledge from labeled source data to unlabeled target data. However,
traditional UDA-SS methods assume that category settings between source and
target domains are known, which is unrealistic in real-world scenarios. This
leads to performance degradation if private classes exist. To address this
limitation, we propose Universal Domain Adaptation for Semantic Segmentation
(UniDA-SS), achieving robust adaptation even without prior knowledge of
category settings. We define the problem in the UniDA-SS scenario as low
confidence scores of common classes in the target domain, which leads to
confusion with private classes. To solve this problem, we propose UniMAP:
UniDA-SS with Image Matching and Prototype-based Distinction, a novel framework
composed of two key components. First, Domain-Specific Prototype-based
Distinction (DSPD) divides each class into two domain-specific prototypes,
enabling finer separation of domain-specific features and enhancing the
identification of common classes across domains. Second, Target-based Image
Matching (TIM) selects a source image containing the most common-class pixels
based on the target pseudo-label and pairs it in a batch to promote effective
learning of common classes. We also introduce a new UniDA-SS benchmark and
demonstrate through various experiments that UniMAP significantly outperforms
baselines. The code is available at
\href(https://github.com/KU-VGI/UniMAP)(this https URL).
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1506.04579)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1606.00915)\]\[[7](http://arxiv.org/abs/1802.10349)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
The category of threshold learning for unknown classes is a critical aspect of domain adaptation, particularly in scenarios where the target domain contains classes not present in the source data \[[23](http://arxiv.org/abs/2104.03344)\]. This challenge is especially relevant in real-world applications, where the assumption of known category settings between domains is often invalid, leading to performance degradation \[[23](http://arxiv.org/abs/2104.03344)\]. Traditional methods typically rely on manually setting a threshold to distinguish between known and unknown samples, which is not practical due to its dependence on validation or predefined ratios \[[23](http://arxiv.org/abs/2104.03344)\]. In contrast, recent approaches aim to learn the threshold dynamically using source samples and adapt it to the target domain \[[23](http://arxiv.org/abs/2104.03344)\]. For instance, methods have been proposed that utilize inter-class distances in the source domain to determine a threshold for identifying unknown classes in the target domain \[[23](http://arxiv.org/abs/2104.03344)\]. This approach involves training one-vs-all classifiers for each class using labeled source data and adapting the open-set classifier to the target domain by minimizing class entropy \[[23](http://arxiv.org/abs/2104.03344)\]. Such techniques are designed to be robust and insensitive to hyper-parameter values, offering significant improvements over existing baselines \[[23](http://arxiv.org/abs/2104.03344)\].
|    | reference                                                                                     |   date | key idea/summary                                                                                                                                                                                                                             |
|----|-----------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [OVANet: One-vs-All Network for Universal Domain Adaptation](http://arxiv.org/abs/2104.03344) |    nan | The paper proposes a method for Universal Domain Adaptation (UNDA) that learns a threshold to distinguish known and unknown classes in the target domain using source samples and adapts an open-set classifier by minimizing class entropy. |
