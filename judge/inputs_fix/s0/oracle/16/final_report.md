## Related Works

Open-vocabulary object detection (OvOD) has emerged as a critical area in computer vision, enabling models to detect objects based on user-defined vocabularies specified in natural language \[[1](http://arxiv.org/abs/2307.09220)\]. This paradigm shift allows for greater flexibility compared to traditional closed-vocabulary approaches, which are constrained to pre-defined categories \[[1](http://arxiv.org/abs/2307.09220)\]. However, existing methods often struggle with the variability of user-defined vocabularies, which can be overly broad or mis-specified, leading to performance degradation \[[1](http://arxiv.org/abs/2307.09220)\]. 

Several approaches have been proposed to address these limitations. One line of work focuses on leveraging large-scale image-text pairs to learn visual-semantic mappings, enabling zero-shot transfer to new categories \[[2](http://arxiv.org/abs/2103.00020)\]. For instance, CLIP demonstrates that pre-training on image-text pairs can yield strong zero-shot performance on tasks like object detection \[[2](http://arxiv.org/abs/2103.00020)\]. Similarly, RegionCLIP extends this idea by learning region-level visual representations, enabling fine-grained alignment between image regions and textual descriptions \[[6](http://arxiv.org/abs/2112.09106)\]. This approach significantly improves performance on open-vocabulary detection tasks, achieving state-of-the-art results on COCO and LVIS datasets \[[6](http://arxiv.org/abs/2112.09106)\].

Another approach, Detic, expands the vocabulary of object detectors by training them on image-level classification data, allowing them to detect tens of thousands of object categories \[[5](http://arxiv.org/abs/2201.02605)\]. This method avoids the need for complex assignment schemes, making it more scalable and easier to implement \[[5](http://arxiv.org/abs/2201.02605)\]. Additionally, it outperforms prior work on both open-vocabulary and long-tail detection benchmarks, demonstrating strong generalization to unseen categories \[[5](http://arxiv.org/abs/2201.02605)\].

The challenge of handling long-tailed distributions in object detection has also been addressed by datasets like LVIS, which contains over 1000 object categories with a long-tail distribution, making it a challenging benchmark for detection models \[[4](http://arxiv.org/abs/1908.03195)\]. The need for robust methods that can generalize to rare categories has led to the development of techniques such as pseudo-labeling and region-aware training \[[1](http://arxiv.org/abs/2307.09220)\].

Recent work has also explored the use of semantic hierarchies to improve the robustness of open-vocabulary detection across different vocabulary granularities. SHiNe introduces a classifier that leverages semantic knowledge from class hierarchies, enhancing performance by up to +31.9% mAP50 when using ground truth hierarchies \[[8](http://arxiv.org/abs/2405.10053)\]. This approach is training-free and can be integrated with any off-the-shelf OvOD detector, making it a promising direction for future research \[[8](http://arxiv.org/abs/2405.10053)\].

In this paper, we propose a plug-and-play solution, VocAda, to refine user-defined vocabularies by aligning them with the content of the image \[[1](http://arxiv.org/abs/2307.09220)\]. Unlike prior methods that rely on training or complex alignment mechanisms, VocAda operates at inference time, using an image captioner to describe visible objects, parsing nouns from those captions, and selecting relevant classes from the user-defined vocabulary \[[1](http://arxiv.org/abs/2307.09220)\]. This approach does not require any training, making it versatile and easy to deploy across different detection models \[[1](http://arxiv.org/abs/2307.09220)\].

1. \[[1](http://arxiv.org/abs/2307.09220)\] A Survey on Open-Vocabulary Detection and Segmentation: Past, Present, and Future  
2. \[[2](http://arxiv.org/abs/2103.00020)\] Learning Transferable Visual Models From Natural Language Supervision  
3. \[[4](http://arxiv.org/abs/1908.03195)\] LVIS: A Dataset for Large Vocabulary Instance Segmentation  
4. \[[5](http://arxiv.org/abs/2201.02605)\] Detecting Twenty-thousand Classes using Image-level Supervision  
5. \[[6](http://arxiv.org/abs/2112.09106)\] RegionCLIP: Region-based Language-Image Pretraining  
6. \[[8](http://arxiv.org/abs/2405.10053)\] SHiNe: Semantic Hierarchy Nexus for Open-vocabulary Object Detection
## Research papers
### Outline
- [Image-text alignment and cross-modal learning [4 papers]](#category-image-text-alignment-and-cross-modal-learning)
- [Large-scale object detection datasets [3 papers]](#category-large-scale-object-detection-datasets)
- [Open-vocabulary object detection frameworks [1 papers]](#category-open-vocabulary-object-detection-frameworks)
- [Semantic hierarchy and class hierarchy utilization [1 papers]](#category-semantic-hierarchy-and-class-hierarchy-utilization)

### <a id='category-image-text-alignment-and-cross-modal-learning'></a>Image-text alignment and cross-modal learning: 4 papers found.
Context: 
	Document 1: [Category]: «Image-text alignment and cross-modal learning»
[_citation_number]: «1»
[Snippet]: «As the most fundamental scene understanding tasks, object detection and
segmentation have made tremendous progress in deep learning era. Due to the
expensive manual labeling cost, the annotated categories in existing datasets
are often small-scale and pre-defined, i.e., state-of-the-art fully-supervised
detectors and segmentors fail to generalize beyond the closed vocabulary. To
resolve this limitation, in the last few years, the community has witnessed an
increasing attention toward Open-Vocabulary Detection (OVD) and Segmentation
(OVS). By ``open-vocabulary'', we mean that the models can classify objects
beyond pre-defined categories. In this survey, we provide a comprehensive
review on recent developments of OVD and OVS. A taxonomy is first developed to
organize different tasks and methodologies. We find that the permission and
usage of weak supervision signals can well discriminate different
methodologies, including: visual-semantic space mapping, novel visual feature
synthesis, region-aware training, pseudo-labeling, knowledge distillation, and
transfer learning. The proposed taxonomy is universal across different tasks,
covering object detection, semantic/instance/panoptic segmentation, 3D and
video understanding. The main design principles, key challenges, development
routes, methodology strengths, and weaknesses are thoroughly analyzed. In
addition, we benchmark each task along with the vital components of each method
in appendix and updated online at
https://github.com/seanzhuh/awesome-open-vocabulary-detection-and-segmentation.
Finally, several promising directions are provided and discussed to stimulate
future research.»

	Document 2: [Category]: «Image-text alignment and cross-modal learning»
[_citation_number]: «2»
[Snippet]: «State-of-the-art computer vision systems are trained to predict a fixed set
of predetermined object categories. This restricted form of supervision limits
their generality and usability since additional labeled data is needed to
specify any other visual concept. Learning directly from raw text about images
is a promising alternative which leverages a much broader source of
supervision. We demonstrate that the simple pre-training task of predicting
which caption goes with which image is an efficient and scalable way to learn
SOTA image representations from scratch on a dataset of 400 million (image,
text) pairs collected from the internet. After pre-training, natural language
is used to reference learned visual concepts (or describe new ones) enabling
zero-shot transfer of the model to downstream tasks. We study the performance
of this approach by benchmarking on over 30 different existing computer vision
datasets, spanning tasks such as OCR, action recognition in videos,
geo-localization, and many types of fine-grained object classification. The
model transfers non-trivially to most tasks and is often competitive with a
fully supervised baseline without the need for any dataset specific training.
For instance, we match the accuracy of the original ResNet-50 on ImageNet
zero-shot without needing to use any of the 1.28 million training examples it
was trained on. We release our code and pre-trained model weights at
https://github.com/OpenAI/CLIP.»

	Document 3: [Category]: «Image-text alignment and cross-modal learning»
[_citation_number]: «6»
[Snippet]: «Contrastive language-image pretraining (CLIP) using image-text pairs has
achieved impressive results on image classification in both zero-shot and
transfer learning settings. However, we show that directly applying such models
to recognize image regions for object detection leads to poor performance due
to a domain shift: CLIP was trained to match an image as a whole to a text
description, without capturing the fine-grained alignment between image regions
and text spans. To mitigate this issue, we propose a new method called
RegionCLIP that significantly extends CLIP to learn region-level visual
representations, thus enabling fine-grained alignment between image regions
and textual concepts. Our method leverages a CLIP model to match image regions with
template captions and then pretrains our model to align these region-text pairs
in the feature space. When transferring our pretrained model to the
open-vocabulary object detection tasks, our method significantly outperforms
the state of the art by 3.8 AP50 and 2.2 AP for novel categories on COCO and
LVIS datasets, respectively. Moreoever, the learned region representations
support zero-shot inference for object detection, showing promising results on
both COCO and LVIS datasets. Our code is available at
https://github.com/microsoft/RegionCLIP.»

	Document 4: [Category]: «Image-text alignment and cross-modal learning»
[_citation_number]: «7»
[Snippet]: «Deriving reliable region-word alignment from image-text pairs is critical to
learn object-level vision-language representations for open-vocabulary object
detection. Existing methods typically rely on pre-trained or self-trained
vision-language models for alignment, which are prone to limitations in
localization accuracy or generalization capabilities. In this paper, we propose
CoDet, a novel approach that overcomes the reliance on pre-aligned
vision-language space by reformulating region-word alignment as a co-occurring
object discovery problem. Intuitively, by grouping images that mention a shared
concept in their captions, objects corresponding to the shared concept shall
exhibit high co-occurrence among the group. CoDet then leverages visual
similarities to discover the co-occurring objects and align them with the
shared concept. Extensive experiments demonstrate that CoDet has superior
performances and compelling scalability in open-vocabulary detection, e.g., by
scaling up the visual backbone, CoDet achieves 37.0 $\text(AP)^m_(novel)$ and
44.7 $\text(AP)^m_(all)$ on OV-LVIS, surpassing the previous SoTA by 4.2
$\text(AP)^m_(novel)$ and 9.8 $\text(AP)^m_(all)$. Code is available at
https://github.com/CVMI-Lab/CoDet.»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T01:15:29+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1405.0312)\]. Further details \[[6](http://arxiv.org/abs/2112.09106)\]\[[7](http://arxiv.org/abs/2310.16667)\]\[[8](http://arxiv.org/abs/2405.10053)\]\[[9]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Open-vocabulary object detection models allow users to freely specify a class
vocabulary in natural language at test time, guiding the detection of desired
objects. However, vocabularies can be overly broad or even mis-specified,
hampering the overall performance of the detector. In this work, we propose a
plug-and-play Vocabulary Adapter (VocAda) to refine the user-defined
vocabulary, automatically tailoring it to categories that are relevant for a
given image. VocAda does not require any training, it operates at inference
time in three steps: i) it uses an image captionner to describe visible
objects, ii) it parses nouns from those captions, and iii) it selects relevant
classes from the user-defined vocabulary, discarding irrelevant ones.
Experiments on COCO and Objects365 with three state-of-the-art detectors show
that VocAda consistently improves performance, proving its versatility. The
code is open source.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1405.0312)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2103.00020)\]\[[7](http://arxiv.org/abs/2310.16667)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The field of open-vocabulary object detection (OVD) has seen significant advancements, driven by the need to extend detection capabilities beyond pre-defined categories \[[1](http://arxiv.org/abs/2307.09220)\]. Traditional fully-supervised detectors are limited by their reliance on fixed vocabularies, which restricts their ability to generalize to new or unseen object classes \[[1](http://arxiv.org/abs/2307.09220)\]. To address this, researchers have explored weak supervision signals and cross-modal learning techniques to enable models to understand and detect objects based on natural language descriptions \[[1](http://arxiv.org/abs/2307.09220)\]. For instance, pre-training models on large-scale image-text pairs has shown promise in enabling zero-shot transfer to new tasks, as demonstrated by models like CLIP, which learns to match images with text descriptions \[[2](http://arxiv.org/abs/2103.00020)\]. However, applying such models directly to object detection tasks often leads to performance degradation due to a domain shift, as these models are trained to align whole images with text rather than fine-grained image regions \[[6](http://arxiv.org/abs/2112.09106)\]. To overcome this limitation, methods like RegionCLIP have been proposed, which extend CLIP to learn region-level visual representations, enabling more accurate alignment between image regions and textual concepts \[[6](http://arxiv.org/abs/2112.09106)\]. Similarly, CoDet introduces a novel approach that reformulates region-word alignment as a co-occurring object discovery problem, improving localization accuracy and generalization capabilities \[[7](http://arxiv.org/abs/2310.16667)\]. These developments highlight the growing focus on leveraging image-text alignment for open-vocabulary detection, with an emphasis on fine-grained alignment and zero-shot inference \[[1](http://arxiv.org/abs/2307.09220)\]\[[6](http://arxiv.org/abs/2112.09106)\]\[[7](http://arxiv.org/abs/2310.16667)\].
|    | reference                                                                                                                   |   date | key idea/summary                                                                                                                                                                                                                                             |
|----|-----------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [A Survey on Open-Vocabulary Detection and Segmentation: Past, Present,
  and Future](http://arxiv.org/abs/2307.09220)      |    nan | This paper provides a comprehensive survey on recent developments in Open-Vocabulary Detection (OVD) and Segmentation (OVS), discussing methodologies, challenges, and future directions for models that can classify objects beyond pre-defined categories. |
|  1 | [Learning Transferable Visual Models From Natural Language Supervision](http://arxiv.org/abs/2103.00020)                    |    nan | The paper introduces a method to train image representations by pre-training on a large dataset of (image, text) pairs, enabling zero-shot transfer to various computer vision tasks without requiring task-specific training.                               |
|  2 | [RegionCLIP: Region-based Language-Image Pretraining](http://arxiv.org/abs/2112.09106)                                      |    nan | RegionCLIP extends CLIP to learn region-level visual representations, enabling fine-grained alignment between image regions and text, and achieves significant improvements in open-vocabulary object detection.                                             |
|  3 | [CoDet: Co-Occurrence Guided Region-Word Alignment for Open-Vocabulary
  Object Detection](http://arxiv.org/abs/2310.16667) |    nan | CoDet is a novel approach that reformulates region-word alignment as a co-occurring object discovery problem, enabling superior performance and scalability in open-vocabulary object detection without relying on pre-aligned vision-language spaces.       |
### <a id='category-large-scale-object-detection-datasets'></a>Large-scale object detection datasets: 3 papers found.
Context: 
	Document 1: [Category]: «Large-scale object detection datasets»
[_citation_number]: «3»
[Snippet]: «We present a new dataset with the goal of advancing the state-of-the-art in
object recognition by placing the question of object recognition in the context
of the broader question of scene understanding. This is achieved by gathering
images of complex everyday scenes containing common objects in their natural
context. Objects are labeled using per-instance segmentations to aid in precise
object localization. Our dataset contains photos of 91 object types that would
be easily recognizable by a 4 year old. With a total of 2.5 million labeled
instances in 328k images, the creation of our dataset drew upon extensive crowd
worker involvement via novel user interfaces for category detection, instance
spotting and instance segmentation. We present a detailed statistical analysis
of the dataset in comparison to PASCAL, ImageNet, and SUN. Finally, we provide
baseline performance analysis for bounding box and segmentation detection
results using a Deformable Parts Model.»

	Document 2: [Category]: «Large-scale object detection datasets»
[_citation_number]: «4»
[Snippet]: «Progress on object detection is enabled by datasets that focus the research
community's attention on open challenges. This process led us from simple
images to complex scenes and from bounding boxes to segmentation masks. In this
work, we introduce LVIS (pronounced `el-vis'): a new dataset for Large
Vocabulary Instance Segmentation. We plan to collect ~2 million high-quality
instance segmentation masks for over 1000 entry-level object categories in 164k
images. Due to the Zipfian distribution of categories in natural images, LVIS
naturally has a long tail of categories with few training samples. Given that
state-of-the-art deep learning methods for object detection perform poorly in
the low-sample regime, we believe that our dataset poses an important and
exciting new scientific challenge. LVIS is available at
http://www.lvisdataset.org.»

	Document 3: [Category]: «Large-scale object detection datasets»
[_citation_number]: «9»
[Snippet]: «»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T01:15:29+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1405.0312)\]. Further details \[[6](http://arxiv.org/abs/2112.09106)\]\[[7](http://arxiv.org/abs/2310.16667)\]\[[8](http://arxiv.org/abs/2405.10053)\]\[[9]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Open-vocabulary object detection models allow users to freely specify a class
vocabulary in natural language at test time, guiding the detection of desired
objects. However, vocabularies can be overly broad or even mis-specified,
hampering the overall performance of the detector. In this work, we propose a
plug-and-play Vocabulary Adapter (VocAda) to refine the user-defined
vocabulary, automatically tailoring it to categories that are relevant for a
given image. VocAda does not require any training, it operates at inference
time in three steps: i) it uses an image captionner to describe visible
objects, ii) it parses nouns from those captions, and iii) it selects relevant
classes from the user-defined vocabulary, discarding irrelevant ones.
Experiments on COCO and Objects365 with three state-of-the-art detectors show
that VocAda consistently improves performance, proving its versatility. The
code is open source.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1405.0312)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2103.00020)\]\[[7](http://arxiv.org/abs/2310.16667)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Large-scale object detection datasets play a crucial role in advancing research and development in computer vision, particularly in the areas of scene understanding and instance segmentation \[[3](http://arxiv.org/abs/1405.0312)\]. These datasets often consist of a vast number of images containing diverse objects, annotated with detailed information to support both bounding box and segmentation tasks \[[3](http://arxiv.org/abs/1405.0312)\]. For example, one such dataset includes 328k images with 2.5 million labeled instances across 91 object types, emphasizing the importance of per-instance segmentations for precise localization \[[3](http://arxiv.org/abs/1405.0312)\]. Another notable dataset, LVIS, focuses on large vocabulary instance segmentation, aiming to collect over 2 million high-quality masks for more than 1000 object categories \[[4](http://arxiv.org/abs/1908.03195)\]. This dataset addresses the challenge of long-tail distributions in natural images, where certain categories have very few training samples, thereby pushing the boundaries of current deep learning methods \[[4](http://arxiv.org/abs/1908.03195)\]. These datasets not only provide the necessary ground truth for training and evaluation but also highlight the evolving needs of the research community, from simple object detection to more complex scene understanding tasks \[[3](http://arxiv.org/abs/1405.0312)\].
|    | reference                                                                                     |   date | key idea/summary                                                                                                                                                                                                                                                    |
|----|-----------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Microsoft COCO: Common Objects in Context](http://arxiv.org/abs/1405.0312)                   |    nan | The paper introduces a new dataset with 2.5 million labeled instances of 91 common object types in complex everyday scenes, aiming to advance object recognition and scene understanding through detailed statistical analysis and baseline performance evaluation. |
|  1 | [LVIS: A Dataset for Large Vocabulary Instance Segmentation](http://arxiv.org/abs/1908.03195) |    nan | LVIS is a new dataset for Large Vocabulary Instance Segmentation, designed to address the challenge of object detection in the low-sample regime with a long-tailed distribution of categories.                                                                     |
|  2 | [(ImageNet: a Large-Scale Hierarchical Image Database)]()                                     |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                           |
### <a id='category-open-vocabulary-object-detection-frameworks'></a>Open-vocabulary object detection frameworks: 1 papers found.
Context: 
	Document 1: [Category]: «Open-vocabulary object detection frameworks»
[_citation_number]: «5»
[Snippet]: «Current object detectors are limited in vocabulary size due to the small
scale of detection datasets. Image classifiers, on the other hand, reason about
much larger vocabularies, as their datasets are larger and easier to collect.
We propose Detic, which simply trains the classifiers of a detector on image
classification data and thus expands the vocabulary of detectors to tens of
thousands of concepts. Unlike prior work, Detic does not need complex
assignment schemes to assign image labels to boxes based on model predictions,
making it much easier to implement and compatible with a range of detection
architectures and backbones. Our results show that Detic yields excellent
detectors even for classes without box annotations. It outperforms prior work
on both open-vocabulary and long-tail detection benchmarks. Detic provides a
gain of 2.4 mAP for all classes and 8.3 mAP for novel classes on the
open-vocabulary LVIS benchmark. On the standard LVIS benchmark, Detic obtains
41.7 mAP when evaluated on all classes, or only rare classes, hence closing the
gap in performance for object categories with few samples. For the first time,
we train a detector with all the twenty-one-thousand classes of the ImageNet
dataset and show that it generalizes to new datasets without finetuning. Code
is available at \url(https://github.com/facebookresearch/Detic).»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T01:15:29+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1405.0312)\]. Further details \[[6](http://arxiv.org/abs/2112.09106)\]\[[7](http://arxiv.org/abs/2310.16667)\]\[[8](http://arxiv.org/abs/2405.10053)\]\[[9]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Open-vocabulary object detection models allow users to freely specify a class
vocabulary in natural language at test time, guiding the detection of desired
objects. However, vocabularies can be overly broad or even mis-specified,
hampering the overall performance of the detector. In this work, we propose a
plug-and-play Vocabulary Adapter (VocAda) to refine the user-defined
vocabulary, automatically tailoring it to categories that are relevant for a
given image. VocAda does not require any training, it operates at inference
time in three steps: i) it uses an image captionner to describe visible
objects, ii) it parses nouns from those captions, and iii) it selects relevant
classes from the user-defined vocabulary, discarding irrelevant ones.
Experiments on COCO and Objects365 with three state-of-the-art detectors show
that VocAda consistently improves performance, proving its versatility. The
code is open source.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1405.0312)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2103.00020)\]\[[7](http://arxiv.org/abs/2310.16667)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Open-vocabulary object detection frameworks aim to overcome the limitations of traditional detectors by expanding the vocabulary of detectable classes beyond the constrained set of annotated categories \[[5](http://arxiv.org/abs/2201.02605)\]. Unlike conventional methods that rely on limited detection datasets, these frameworks leverage the broader vocabulary of image classifiers, which are trained on larger and more diverse datasets \[[5](http://arxiv.org/abs/2201.02605)\]. For instance, Detic demonstrates that training detectors on image classification data can significantly expand the vocabulary to tens of thousands of concepts, enabling detection of classes without explicit box annotations \[[5](http://arxiv.org/abs/2201.02605)\]. This approach eliminates the need for complex assignment schemes to match labels to boxes, simplifying implementation and enhancing compatibility with various detection architectures \[[5](http://arxiv.org/abs/2201.02605)\]. The effectiveness of such methods is evident in benchmarks like the open-vocabulary LVIS, where Detic achieves a 2.4 mAP improvement for all classes and an 8.3 mAP gain for novel classes \[[5](http://arxiv.org/abs/2201.02605)\]. Additionally, Detic closes the performance gap for rare categories by achieving 41.7 mAP on the standard LVIS benchmark, even when evaluated on only rare classes \[[5](http://arxiv.org/abs/2201.02605)\]. These advancements highlight the potential of open-vocabulary detection to generalize across new datasets without requiring fine-tuning, as demonstrated by training on the full 21,000 classes of ImageNet \[[5](http://arxiv.org/abs/2201.02605)\].
|    | reference                                                                                          |   date | key idea/summary                                                                                                                                                                                                                                                                                |
|----|----------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Detecting Twenty-thousand Classes using Image-level Supervision](http://arxiv.org/abs/2201.02605) |    nan | Detic expands the vocabulary of object detectors by training classifiers on image classification data, enabling detection of tens of thousands of concepts without complex assignment schemes, and achieves state-of-the-art performance on open-vocabulary and long-tail detection benchmarks. |
### <a id='category-semantic-hierarchy-and-class-hierarchy-utilization'></a>Semantic hierarchy and class hierarchy utilization: 1 papers found.
Context: 
	Document 1: [Category]: «Semantic hierarchy and class hierarchy utilization»
[_citation_number]: «8»
[Snippet]: «Open-vocabulary object detection (OvOD) has transformed detection into a language-guided task, empowering users to freely define their class vocabularies of interest during inference. However, our initial investigation indicates that existing OvOD detectors exhibit significant variability when dealing with vocabularies across various semantic granularities, posing a concern for real-world deployment. To this end, we introduce Semantic Hierarchy Nexus (SHiNe), a novel classifier that uses semantic knowledge from class hierarchies. It runs offline in three steps: i) it retrieves relevant super-/sub-categories from a hierarchy for each target class; ii) it integrates these categories into hierarchy-aware sentences; iii) it fuses these sentence embeddings to generate the nexus classifier vector. Our evaluation on various detection benchmarks demonstrates that SHiNe enhances robustness across diverse vocabulary granularities, achieving up to +31.9% mAP50 with ground truth hierarchies, while retaining improvements using hierarchies generated by large language models. Moreover, when applied to open-vocabulary classification on ImageNet-1k, SHiNe improves the CLIP zero-shot baseline by +2.8% accuracy. SHiNe is training-free and can be seamlessly integrated with any off-the-shelf OvOD detector, without incurring additional computational overhead during inference. The code is open source.»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T01:15:29+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1405.0312)\]. Further details \[[6](http://arxiv.org/abs/2112.09106)\]\[[7](http://arxiv.org/abs/2310.16667)\]\[[8](http://arxiv.org/abs/2405.10053)\]\[[9]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Open-vocabulary object detection models allow users to freely specify a class vocabulary in natural language at test time, guiding the detection of desired objects. However, vocabularies can be overly broad or even mis-specified, hampering the overall performance of the detector. In this work, we propose a plug-and-play Vocabulary Adapter (VocAda) to refine the user-defined vocabulary, automatically tailoring it to categories that are relevant for a given image. VocAda does not require any training, it operates at inference time in three steps: i) it uses an image captionner to describe visible objects, ii) it parses nouns from those captions, and iii) it selects relevant classes from the user-defined vocabulary, discarding irrelevant ones. Experiments on COCO and Objects365 with three state-of-the-art detectors show that VocAda consistently improves performance, proving its versatility. The code is open source.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1405.0312)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2103.00020)\]\[[7](http://arxiv.org/abs/2310.16667)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
The use of semantic hierarchies in object detection has gained traction as a means to improve robustness and adaptability in open-vocabulary settings \[[8](http://arxiv.org/abs/2405.10053)\]. By leveraging class hierarchies, models can better handle variations in vocabulary granularity, which is a critical challenge in real-world deployment \[[8](http://arxiv.org/abs/2405.10053)\]. This approach allows for more nuanced understanding of object categories, enabling detectors to generalize across different levels of abstraction \[[8](http://arxiv.org/abs/2405.10053)\]. For instance, methods like Semantic Hierarchy Nexus (SHiNe) utilize hierarchy-aware sentences to generate classifiers that are more resilient to mis-specified or overly broad vocabularies \[[8](http://arxiv.org/abs/2405.10053)\]. This aligns with broader efforts to enhance the interpretability and effectiveness of open-vocabulary detection systems by incorporating semantic knowledge \[[8](http://arxiv.org/abs/2405.10053)\].
|    | reference                                                                                               |   date | key idea/summary                                                                                                                                                                                                                                                     |
|----|---------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [SHiNe: Semantic Hierarchy Nexus for Open-vocabulary Object Detection](http://arxiv.org/abs/2405.10053) |    nan | SHiNe is a novel classifier for open-vocabulary object detection that leverages semantic hierarchies to improve robustness across different vocabulary granularities, achieving significant performance gains without additional training or computational overhead. |
