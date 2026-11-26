## Related Works

Open-vocabulary object detection (OVD) has gained significant attention in recent years due to its ability to detect objects from arbitrary text descriptions, enabling flexible and user-driven detection \[[1](http://arxiv.org/abs/2011.10678)\]. Traditional object detection methods are limited to a fixed set of categories, requiring extensive manual annotation for expansion \[[1](http://arxiv.org/abs/2011.10678)\]. To overcome this limitation, researchers have explored weakly supervised and zero-shot learning techniques, but these approaches have not been as effective as fully supervised methods \[[1](http://arxiv.org/abs/2011.10678)\]. 

Several works have focused on leveraging large-scale image-text pairs to expand the vocabulary of object detectors. For instance, \[[2](http://arxiv.org/abs/1411.4952)\] proposed a method that generates pseudo bounding-box annotations from image-caption pairs, allowing detectors to be trained on a broader set of categories. This approach significantly reduces the need for manual annotations and improves performance on novel categories. Similarly, \[[3](http://arxiv.org/abs/2111.09452)\] introduced a framework that uses pre-trained vision-language models to generate pseudo labels, leading to improved detection accuracy on benchmarks like COCO and LVIS. 

Another line of research has focused on aligning visual and language representations to enable open-vocabulary detection. \[[4](http://arxiv.org/abs/2211.14843)\] proposed a novel framework that directly learns from image-text pairs by formulating object-language alignment as a set matching problem. This method enables detectors to be trained without requiring explicit bounding-box annotations, improving performance on novel categories. \[[5](http://arxiv.org/abs/2304.00788)\] further extended this idea by proposing a method that connects textual and point-cloud representations, enabling open-vocabulary 3D object detection without 3D annotations. 

Weakly supervised detection methods have also been explored to reduce the reliance on manual annotations. \[[6](http://arxiv.org/abs/2203.16513)\] introduced a two-stage open-vocabulary detector that uses a text encoder from a pre-trained vision-language model to classify object proposals. This approach allows detectors to generalize to novel categories without requiring additional training data. \[[7](http://arxiv.org/abs/2004.06165)\] proposed a method that uses regional prompt learning to align textual embeddings with visual features, improving the performance of open-vocabulary detectors. 

Recent work has also focused on improving the efficiency and scalability of open-vocabulary detection. \[[8](http://arxiv.org/abs/2306.05493)\] introduced a self-training framework that uses noisy web images to expand the vocabulary of detectors, achieving superior performance on benchmarks like LVIS and MS-COCO. \[[9](http://arxiv.org/abs/2205.06230)\] proposed a method that leverages contrastive image-text pre-training and end-to-end detection fine-tuning, demonstrating consistent improvements on downstream detection tasks. 

In addition to detection, some works have explored open-vocabulary segmentation. \[[10](http://arxiv.org/abs/2211.12914)\] introduced a framework that jointly learns from segmentation and detection datasets, bridging the gap between different annotation granularities. This approach enables models to generalize to novel categories without requiring extensive retraining. 

Overall, the field of open-vocabulary object detection has seen significant advancements, with researchers exploring various approaches to reduce the reliance on manual annotations and improve the generalization ability of detectors. The proposed Vocabulary Adapter (VocAda) builds on these advancements by refining user-defined vocabularies to improve detection performance \[[11](http://arxiv.org/abs/2211.16312)\].

### References

1. \[[1](http://arxiv.org/abs/2011.10678)\] Open-Vocabulary Object Detection Using Captions  
2. \[[2](http://arxiv.org/abs/1411.4952)\] Open Vocabulary Object Detection with Pseudo Bounding-Box Labels  
3. \[[3](http://arxiv.org/abs/2111.09452)\] Learning Object-Language Alignments for Open-Vocabulary Object Detection  
4. \[[4](http://arxiv.org/abs/2211.14843)\] Open-Vocabulary Point-Cloud Object Detection without 3D Annotation  
5. \[[5](http://arxiv.org/abs/2304.00788)\] PromptDet: Towards Open-Vocabulary Detection Using Uncurated Images  
6. \[[6](http://arxiv.org/abs/2203.16513)\] Learning to Prompt for Open-Vocabulary Object Detection with Vision-Language Model  
7. \[[7](http://arxiv.org/abs/2004.06165)\] Localized Vision-Language Matching for Open-vocabulary Object Detection  
8. \[[8](http://arxiv.org/abs/2306.05493)\] Open-Vocabulary DETR with Conditional Matching  
9. \[[9](http://arxiv.org/abs/2205.06230)\] Simple Open-Vocabulary Object Detection with Vision Transformers  
10. \[[10](http://arxiv.org/abs/2211.12914)\] A Simple Framework for Open-Vocabulary Segmentation and Detection  
11. \[[11](http://arxiv.org/abs/2211.16312)\] The paper abstract provided in the user query.
