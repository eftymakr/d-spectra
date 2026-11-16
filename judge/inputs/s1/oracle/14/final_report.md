## Related Works

Video super-resolution (VSR) has attracted significant research interest due to its importance in enhancing the quality of low-resolution videos. Early methods primarily relied on convolutional neural networks (CNNs) and recurrent neural networks (RNNs) to exploit temporal information and improve resolution \[[1](http://arxiv.org/abs/2106.06847)\]. However, these approaches often struggled with capturing long-range dependencies and maintaining content consistency across frames \[[2](http://arxiv.org/abs/2012.02181)\]. More recently, Transformer-based models have been explored for VSR due to their ability to model long-range dependencies effectively \[[3](http://arxiv.org/abs/2008.00455)\]. Nevertheless, the typical Transformer architecture, with fully connected self-attention and token-wise feed-forward layers, has limitations in capturing spatial-temporal locality and feature alignment \[[3](http://arxiv.org/abs/2008.00455)\].

To address these limitations, several works have proposed modifications to the Transformer architecture. For instance, the Video Super-Resolution Transformer (VSR-Transformer) introduced a spatial-temporal convolutional self-attention layer to exploit locality and a bidirectional optical flow-based feed-forward layer to align features across frames \[[3](http://arxiv.org/abs/2008.00455)\]. Similarly, the BasicVSR framework emphasized the importance of four key functionalities: propagation, alignment, aggregation, and upscaling, leading to a more efficient and effective pipeline \[[2](http://arxiv.org/abs/2012.02181)\]. These approaches have laid the foundation for more advanced VSR methods.

Recent advances in VSR have also focused on recurrent architectures and efficient modeling of long sequences. The Recurrent Video Restoration Transformer (RVRT) integrates the advantages of parallel and recurrent processing by using guided deformable attention for clip-to-clip alignment \[[6](http://arxiv.org/abs/2206.02146)\]. Additionally, the EDVR framework introduced enhanced deformable convolutional networks to handle large motions and effectively fuse frames with diverse motion and blur \[[7](http://arxiv.org/abs/1905.02716)\]. These methods have demonstrated significant improvements in handling complex degradations and maintaining high-quality output.

In the context of real-world VSR, challenges such as severe in-the-wild degradations and artifact propagation have been addressed through pre-cleaning stages and improved training strategies \[[9](http://arxiv.org/abs/2111.12704)\]. The RealBasicVSR method incorporated a cleaning module to reduce noise and artifacts before propagation, leading to better performance and efficiency \[[9](http://arxiv.org/abs/2111.12704)\]. Furthermore, the FastRealVSR method introduced a Hidden State Attention (HSA) module to mitigate artifacts by selectively aggregating cleaner hidden states \[[10](http://arxiv.org/abs/2212.07339)\].

The use of self-supervised learning and contrastive learning has also gained traction in VSR. The SimCLR framework demonstrated the effectiveness of contrastive learning in learning robust visual representations without requiring explicit supervision \[[15](http://arxiv.org/abs/2002.05709)\]. Similarly, the SwAV method proposed an online algorithm that leverages contrastive learning without explicit pairwise comparisons, leading to
## Research papers
### Outline
- [Transformer-based VSR architectures [6 papers]](#category-transformer-based-vsr-architectures)
- [Spatial-temporal convolutional attention in VSR [2 papers]](#category-spatial-temporal-convolutional-attention-in-vsr)
- [Recurrent and parallel processing in VSR [3 papers]](#category-recurrent-and-parallel-processing-in-vsr)
- [Deformable convolutional networks for motion handling [5 papers]](#category-deformable-convolutional-networks-for-motion-handling)
- [Pre-cleaning stages in real-world VSR [2 papers]](#category-pre-cleaning-stages-in-real-world-vsr)
- [Hidden State Attention modules for artifact reduction [1 papers]](#category-hidden-state-attention-modules-for-artifact-reduction)
- [Contrastive learning for feature extraction [3 papers]](#category-contrastive-learning-for-feature-extraction)

### <a id='category-transformer-based-vsr-architectures'></a>Transformer-based VSR architectures: 6 papers found.
Video super-resolution (VSR) has seen significant advancements with the integration of Transformer-based architectures, addressing the challenges of spatial-temporal modeling and feature alignment \[[1](http://arxiv.org/abs/2106.06847)\]. Traditional Transformer designs, which rely on fully connected self-attention and token-wise feed-forward layers, struggle with data locality and feature alignment, limiting their effectiveness for VSR \[[1](http://arxiv.org/abs/2106.06847)\]. To overcome these limitations, researchers have introduced specialized layers, such as spatial-temporal convolutional self-attention, which better exploit locality by incorporating convolutional operations \[[1](http://arxiv.org/abs/2106.06847)\]. Additionally, bidirectional optical flow-based feed-forward layers have been designed to capture cross-frame correlations and align features more effectively \[[1](http://arxiv.org/abs/2106.06847)\]. Beyond these innovations, other approaches have focused on integrating recurrent mechanisms with Transformers to balance model efficiency and long-range dependency modeling \[[6](http://arxiv.org/abs/2206.02146)\]. For instance, the Video Restoration Transformer (VRT) employs temporal mutual self-attention and parallel warping to enable parallel frame prediction and long-range temporal modeling, achieving superior performance across multiple video restoration tasks \[[5](http://arxiv.org/abs/2201.12288)\]. Similarly, the Recurrent Video Restoration Transformer (RVRT) combines parallel processing with a globally recurrent framework, offering a good trade-off between model size, effectiveness, and efficiency \[[6](http://arxiv.org/abs/2206.02146)\]. These methods highlight the ongoing efforts to enhance Transformer-based VSR by addressing issues such as computational efficiency, artifact reduction, and temporal coherence \[[1](http://arxiv.org/abs/2106.06847)\]\[[5](http://arxiv.org/abs/2201.12288)\]\[[6](http://arxiv.org/abs/2206.02146)\]. Additionally, recent work has explored the use of state space models (SSMs), such as Mamba, to improve long-sequence modeling while maintaining hardware-aware efficiency \[[13](http://arxiv.org/abs/2401.09417)\]. These developments underscore the growing interest in leveraging Transformer variants for VSR, with a focus on improving both performance and practical deployment.
|    | reference                                                                                                                        |   date | key idea/summary                                                                                                                                                                                                                                                        |
|----|----------------------------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Video Super-Resolution Transformer](http://arxiv.org/abs/2106.06847)                                                            |    nan | This paper proposes a novel Transformer-based approach for video super-resolution (VSR) by addressing the limitations of traditional Transformer blocks through spatial-temporal convolutional self-attention and bidirectional optical flow-based feed-forward layers. |
|  1 | [VRT: A Video Restoration Transformer](http://arxiv.org/abs/2201.12288)                                                          |    nan | The paper introduces a Video Restoration Transformer (VRT) that effectively restores video frames by leveraging parallel frame prediction and long-range temporal dependency modeling, achieving significant improvements over existing methods.                        |
|  2 | [Recurrent Video Restoration Transformer with Guided Deformable Attention](http://arxiv.org/abs/2206.02146)                      |    nan | The paper proposes RVRT, a recurrent video restoration transformer that combines the advantages of parallel and sequential video restoration methods, achieving a good balance between model size, effectiveness, and efficiency.                                       |
|  3 | [Vision Mamba: Efficient Visual Representation Learning with
  Bidirectional State Space Model](http://arxiv.org/abs/2401.09417) |    nan | The paper introduces Vim, a new generic vision backbone based on bidirectional Mamba blocks, which outperforms vision transformers like DeiT in performance and efficiency for high-resolution image tasks.                                                             |
|  4 | [Efficiently modeling long sequences with structured state spaces]()                                                             |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                               |
|  5 | [Mamba-nd: Selective state space modeling for multi-dimensional data]()                                                          |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                               |
### <a id='category-spatial-temporal-convolutional-attention-in-vsr'></a>Spatial-temporal convolutional attention in VSR: 2 papers found.
Context: 
	Document 1: [Category]: «Spatial-temporal convolutional attention in VSR»
[Snippet]: «Video super-resolution (VSR) approaches tend to have more components than the
image counterparts as they need to exploit the additional temporal dimension.
Complex designs are not uncommon. In this study, we wish to untangle the knots
and reconsider some most essential components for VSR guided by four basic
functionalities, i.e., Propagation, Alignment, Aggregation, and Upsampling. By
reusing some existing components added with minimal redesigns, we show a
succinct pipeline, BasicVSR, that achieves appealing improvements in terms of
speed and restoration quality in comparison to many state-of-the-art
algorithms. We conduct systematic analysis to explain how such gain can be
obtained and discuss the pitfalls. We further show the extensibility of
BasicVSR by presenting an information-refill mechanism and a coupled
propagation scheme to facilitate information aggregation. The BasicVSR and its
extension, IconVSR, can serve as strong baselines for future VSR approaches.»
[_citation_number]: «2»

	Document 2: [Category]: «Spatial-temporal convolutional attention in VSR»
[Snippet]: «Video super-resolution, which aims at producing a high-resolution video from
its corresponding low-resolution version, has recently drawn increasing
attention. In this work, we propose a novel method that can effectively
incorporate temporal information in a hierarchical way. The input sequence is
divided into several groups, with each one corresponding to a kind of frame
rate. These groups provide complementary information to recover missing details
in the reference frame, which is further integrated with an attention module
and a deep intra-group fusion module. In addition, a fast spatial alignment is
proposed to handle videos with large motion. Extensive results demonstrate the
capability of the proposed model in handling videos with various motion. It
achieves favorable performance against state-of-the-art methods on several
benchmark datasets.»
[_citation_number]: «4»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-06-01T14:36:25+0
|    | reference                                                                                                               |   date | key idea/summary                                                                                                                                                                                                                                         |
|----|-------------------------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [BasicVSR: The Search for Essential Components in Video Super-Resolution
  and Beyond](http://arxiv.org/abs/2012.02181) |    nan | BasicVSR is a simplified and efficient video super-resolution approach that improves speed and restoration quality by focusing on essential components like propagation, alignment, aggregation, and upscaling, with extensions for better performance.  |
|  1 | [Video Super-resolution with Temporal Group Attention](http://arxiv.org/abs/2007.10595)                                 |    nan | The paper proposes a novel video super-resolution method that effectively incorporates temporal information through hierarchical grouping, attention modules, and fast spatial alignment to enhance detail recovery and handle various motion scenarios. |
### <a id='category-recurrent-and-parallel-processing-in-vsr'></a>Recurrent and parallel processing in VSR: 3 papers found.
Context: 
	Document 1: [Category]: «Recurrent and parallel processing in VSR»
[Snippet]: «Most video super-resolution methods super-resolve a single reference frame with the help of neighboring frames in a temporal sliding window. They are less efficient compared to the recurrent-based methods. In this work, we propose a novel recurrent video super-resolution method which is both effective and efficient in exploiting previous frames to super-resolve the current frame. It divides the input into structure and detail components which are fed to a recurrent unit composed of several proposed two-stream structure-detail blocks. In addition, a hidden state adaptation module that allows the current frame to selectively use information from hidden state is introduced to enhance its robustness to appearance change and error accumulation. Extensive ablation study validate the effectiveness of the proposed modules. Experiments on several benchmark datasets demonstrate the superior performance of the proposed method compared to state-of-the-art methods on video super-resolution.»
[_citation_number]: «3»

	Document 2: [Category]: «Recurrent and parallel processing in VSR»
[Snippet]: «Models using structured state space sequence (S4) layers have achieved state-of-the-art performance on long-range sequence modeling tasks. An S4 layer combines linear state space models (SSMs), the HiPPO framework, and deep learning to achieve high performance. We build on the design of the S4 layer and introduce a new state space layer, the S5 layer. Whereas an S4 layer uses many independent single-input, single-output SSMs, the S5 layer uses one multi-input, multi-output SSM. We establish a connection between S5 and S4, and use this to develop the initialization and parameterization used by the S5 model. The result is a state space layer that can leverage efficient and widely implemented parallel scans, allowing S5 to match the computational efficiency of S4, while also achieving state-of-the-art performance on several long-range sequence modeling tasks. S5 averages 87.4% on the long range arena benchmark, and 98.5% on the most difficult Path-X task.»
[_citation_number]: «11»

	Document 3: [Category]: «Recurrent and parallel processing in VSR»
[Snippet]: «Foundation models, now powering most of the exciting applications in deep learning, are almost universally based on the Transformer architecture and its core attention module. Many subquadratic-time architectures such as linear attention, gated convolution and recurrent models, and structured state space
|    | reference                                                                                           |   date | key idea/summary                                                                                                                                                                                                                                                                       |
|----|-----------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Video Super-Resolution with Recurrent Structure-Detail Network](http://arxiv.org/abs/2008.00455)   |    nan | The paper proposes a novel recurrent video super-resolution method that effectively and efficiently super-resolves video frames by leveraging structure and detail components with a hidden state adaptation module, achieving superior performance compared to existing methods.      |
|  1 | [Simplified State Space Layers for Sequence Modeling](http://arxiv.org/abs/2208.04933)              |    nan | The S5 layer improves upon the S4 layer by using a multi-input, multi-output SSM, achieving state-of-the-art performance and computational efficiency on long-range sequence modeling tasks.                                                                                           |
|  2 | [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](http://arxiv.org/abs/2312.00752) |    nan | Mamba is a novel sequence model based on structured state space models (SSMs) that improves upon traditional Transformers by enabling content-based reasoning and achieving faster inference and linear scaling with sequence length, outperforming Transformers in language modeling. |
### <a id='category-deformable-convolutional-networks-for-motion-handling'></a>Deformable convolutional networks for motion handling: 5 papers found.
The category "Deformable convolutional networks for motion handling" focuses on addressing challenges in video restoration tasks such as super-resolution and deblurring, where aligning and fusing multiple frames with large motions and diverse blur is critical \[[1](http://arxiv.org/abs/2106.06847)\]. Existing methods often rely on optical flow for temporal correspondence, which can be error-prone, and fail to exploit self-similarity in natural images \[[2](http://arxiv.org/abs/2012.02181)\]. To overcome these limitations, researchers have proposed advanced modules like the Pyramid, Cascading, and Deformable (PCD) alignment module, which uses deformable convolutions in a coarse-to-fine manner to handle large motions at the feature level \[[1](http://arxiv.org/abs/2106.06847)\]. Additionally, the Temporal and Spatial Attention (TSA) fusion module applies attention mechanisms both temporally and spatially to emphasize important features for restoration \[[1](http://arxiv.org/abs/2106.06847)\]. Another approach, the Multi-Correspondence Aggregation Network (MuCAN), introduces strategies for leveraging similar patches across frames and exploring self-similarity across scales, leading to state-of-the-art results on benchmark datasets \[[2](http://arxiv.org/abs/2012.02181)\]. These methods highlight the importance of deformable convolutions and attention mechanisms in improving motion handling and frame fusion in video restoration tasks. The proposed approaches demonstrate significant improvements over existing methods, as evidenced by their performance in challenges like NTIRE19 \[[1](http://arxiv.org/abs/2106.06847)\].
|    | reference                                                                                                       |   date | key idea/summary                                                                                                                                                                                                                                                                         |
|----|-----------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [EDVR: Video Restoration with Enhanced Deformable Convolutional Networks](http://arxiv.org/abs/1905.02716)      |    nan | EDVR is a novel video restoration framework that addresses challenges in aligning and fusing video frames through enhanced deformable networks, achieving state-of-the-art results in video super-resolution and deblurring.                                                             |
|  1 | [MuCAN: Multi-Correspondence Aggregation Network for Video
  Super-Resolution](http://arxiv.org/abs/2007.11803) |    nan | The paper proposes a novel Video Super-Resolution (VSR) method called MuCAN, which addresses limitations in existing approaches by leveraging temporal multi-correspondence and cross-scale nonlocal-correspondence aggregation to improve the recovery of high-resolution video frames. |
|  2 | [Basicvsr++: Improving video super-resolution with enhanced propagation and alignment]()                        |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                |
|  3 | [Deep video super-resolution network using dynamic upsampling filters without explicit motion compensation]()   |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                |
|  4 | [Ntire 2019 challenge on video deblurring and super-resolution: Dataset and study]()                            |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                |
### <a id='category-pre-cleaning-stages-in-real-world-vsr'></a>Pre-cleaning stages in real-world VSR: 2 papers found.
Context: 
	Document 1: [Category]: «Pre-cleaning stages in real-world VSR»
[Snippet]: «The diversity and complexity of degradations in real-world video super-resolution (VSR) pose non-trivial challenges in inference and training. First, while long-term propagation leads to improved performance in cases of mild degradations, severe in-the-wild degradations could be exaggerated through propagation, impairing output quality. To balance the tradeoff between detail synthesis and artifact suppression, we found an image pre-cleaning stage indispensable to reduce noises and artifacts prior to propagation. Equipped with a carefully designed cleaning module, our RealBasicVSR outperforms existing methods in both quality and efficiency. Second, real-world VSR models are often trained with diverse degradations to improve generalizability, requiring increased batch size to produce a stable gradient. Inevitably, the increased computational burden results in various problems, including 1) speed-performance tradeoff and 2) batch-length tradeoff. To alleviate the first tradeoff, we propose a stochastic degradation scheme that reduces up to 40\% of training time without sacrificing performance. We then analyze different training settings and suggest that employing longer sequences rather than larger batches during training allows more effective uses of temporal information, leading to more stable performance during inference. To facilitate fair comparisons, we propose the new VideoLQ dataset, which contains a large variety of real-world low-quality video sequences containing rich textures and patterns. Our dataset can serve as a common ground for benchmarking. Code, models, and the dataset will be made publicly available.»
[_citation_number]: «9»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-06-01T14:36:25+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2008.00455)\]. Further details \[[6](http://arxiv.org/abs/2206.02146)\]\[[7](http://arxiv.org/abs/1905.02716)\]\[[8](http://arxiv.org/abs/2007.11803)\]\[[9](http://arxiv.org/abs/2111.12704)\]\[[10](http://arxiv.org/abs/2212.07339)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 6
|    | reference                                                                                            |   date | key idea/summary                                                                                                                                                                                                                   |
|----|------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Investigating Tradeoffs in Real-World Video Super-Resolution](http://arxiv.org/abs/2111.12704)      |    nan | RealBasicVSR improves video super-resolution by incorporating a pre-cleaning stage and a stochastic degradation scheme, achieving better quality and efficiency while addressing training challenges with a new benchmark dataset. |
|  1 | [Real-world video super-resolution: A benchmark dataset and a decomposition based learning scheme]() |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                          |
### <a id='category-hidden-state-attention-modules-for-artifact-reduction'></a>Hidden State Attention modules for artifact reduction: 1 papers found.
Context: 
	Document 1: [Category]: «Hidden State Attention modules for artifact reduction»
[Snippet]: «The recurrent structure is a prevalent framework for the task of video
super-resolution, which models the temporal dependency between frames via
hidden states. When applied to real-world scenarios with unknown and complex
degradations, hidden states tend to contain unpleasant artifacts and propagate
them to restored frames. In this circumstance, our analyses show that such
artifacts can be largely alleviated when the hidden state is replaced with a
cleaner counterpart. Based on the observations, we propose a Hidden State
Attention (HSA) module to mitigate artifacts in real-world video
super-resolution. Specifically, we first adopt various cheap filters to produce
a hidden state pool. For example, Gaussian blur filters are for smoothing
artifacts while sharpening filters are for enhancing details. To aggregate a
new hidden state that contains fewer artifacts from the hidden state pool, we
devise a Selective Cross Attention (SCA) module, in which the attention between
input features and each hidden state is calculated. Equipped with HSA, our
proposed method, namely FastRealVSR, is able to achieve 2x speedup while
obtaining better performance than Real-BasicVSR. Codes will be available at
https://github.com/TencentARC/FastRealVSR»
[_citation_number]: «10»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-06-01T14:36:25+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2008.00455)\]. Further details \[[6](http://arxiv.org/abs/2206.02146)\]\[[7](http://arxiv.org/abs/1905.02716)\]\[[8](http://arxiv.org/abs/2007.11803)\]\[[9](http://arxiv.org/abs/2111.12704)\]\[[10](http://arxiv.org/abs/2212.07339)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Existing diffusion-based video super-resolution (VSR) methods are susceptible
to introducing complex degradations and noticeable artifacts into
high-resolution videos due
|    | reference                                                                                           |   date | key idea/summary                                                                                                                                                                                                                                                              |
|----|-----------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Mitigating Artifacts in Real-World Video Super-Resolution Models](http://arxiv.org/abs/2212.07339) |    nan | The paper proposes a Hidden State Attention (HSA) module to reduce artifacts in real-world video super-resolution by replacing hidden states with cleaner counterparts using a Selective Cross Attention (SCA) module, leading to improved performance and faster processing. |
### <a id='category-contrastive-learning-for-feature-extraction'></a>Contrastive learning for feature extraction: 3 papers found.
Context: 
	Document 1: [Category]: «Contrastive learning for feature extraction»
[Snippet]: «Unsupervised image representations have significantly reduced the gap with
supervised pretraining, notably with the recent achievements of contrastive
learning methods. These contrastive methods typically work online and rely on a
large number of explicit pairwise feature comparisons, which is computationally
challenging. In this paper, we propose an online algorithm, SwAV, that takes
advantage of contrastive methods without requiring to compute pairwise
comparisons. Specifically, our method simultaneously clusters the data while
enforcing consistency between cluster assignments produced for different
augmentations (or views) of the same image, instead of comparing features
directly as in contrastive learning. Simply put, we use a swapped prediction
mechanism where we predict the cluster assignment of a view from the
representation of another view. Our method can be trained with large and small
batches and can scale to unlimited amounts of data. Compared to previous
contrastive methods, our method is more memory efficient since it does not
require a large memory bank or a special momentum network. In addition, we also
propose a new data augmentation strategy, multi-crop, that uses a mix of views
with different resolutions in place of two full-resolution views, without
increasing the memory or compute requirements much. We validate our findings by
achieving 75.3% top-1 accuracy on ImageNet with ResNet-50, as well as
surpassing supervised pretraining on all the considered transfer tasks.»
[_citation_number]: «14»

	Document 2: [Category]: «Contrastive learning for feature extraction»
[Snippet]: «This paper presents SimCLR: a simple framework for contrastive learning of
visual representations. We simplify recently proposed contrastive
self-supervised learning algorithms without requiring specialized architectures
or a memory bank. In order to understand what enables the contrastive
prediction tasks to learn useful representations, we systematically study the
major components of our framework. We show that (1) composition of data
augmentations plays a critical role in defining effective predictive tasks, (2)
introducing a learnable nonlinear transformation between the representation and
the contrastive loss substantially improves the quality of the learned
representations, and (3) contrastive learning benefits from larger batch sizes
and more training steps compared to supervised learning. By combining these
findings,
|    | reference                                                                                                        |   date | key idea/summary                                                                                                                                                                                                                                                        |
|----|------------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Unsupervised Learning of Visual Features by Contrasting Cluster
  Assignments](http://arxiv.org/abs/2006.09882) |    nan | The paper introduces SwAV, an online contrastive learning method that avoids explicit pairwise feature comparisons by using a swapped prediction mechanism, enabling efficient and scalable training with improved memory efficiency and performance on transfer tasks. |
|  1 | [A Simple Framework for Contrastive Learning of Visual Representations](http://arxiv.org/abs/2002.05709)         |    nan | SimCLR is a simple contrastive learning framework that achieves state-of-the-art results in self-supervised and semi-supervised learning on ImageNet by improving data augmentation, nonlinear transformations, and training strategies.                                |
|  2 | [Momentum Contrast for Unsupervised Visual Representation Learning](http://arxiv.org/abs/1911.05722)             |    nan | Momentum Contrast (MoCo) is an unsupervised visual representation learning method that uses a dynamic dictionary and moving-averaged encoder to achieve competitive results, often outperforming supervised pre-training in downstream tasks.                           |
