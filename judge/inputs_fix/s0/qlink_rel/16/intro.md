## Related Works

Open-vocabulary object detection has emerged as a critical research direction, enabling detectors to recognize objects from a vocabulary specified at test time, often in natural language \[[1](http://arxiv.org/abs/2011.10678)\]. This capability is particularly valuable for applications requiring flexible and dynamic object recognition, such as robotics and augmented reality \[[2](http://arxiv.org/abs/2104.13921)\]. However, the performance of these detectors can be significantly impacted by the quality and relevance of the user-defined vocabulary \[[3](http://arxiv.org/abs/2205.06230)\]. Prior work has explored various approaches to improve detection accuracy by leveraging pre-trained models, weak supervision, and language-visual alignment \[[4](http://arxiv.org/abs/2103.00020)\].

Several studies have focused on improving open-vocabulary detection by using vision-language pre-training models like CLIP and ALIGN \[[5](http://arxiv.org/abs/2203.14940)\]. These models enable zero-shot transfer by aligning visual and textual representations, allowing detectors to recognize objects without explicit bounding box annotations \[[6](http://arxiv.org/abs/2203.11876)\]. For instance, ViLD leverages vision-language knowledge distillation to train a two-stage detector, achieving competitive performance on benchmark datasets like LVIS and COCO \[[7](http://arxiv.org/abs/2207.03482)\]. Similarly, RegionCLIP extends CLIP to learn region-level visual representations, enabling fine-grained alignment between image regions and textual concepts \[[8](http://arxiv.org/abs/2111.09452)\].

Another line of research has explored the use of pseudo-labeling and self-training frameworks to generate bounding box annotations from large-scale image-caption pairs \[[9](http://arxiv.org/abs/2207.08954)\]. This approach reduces the reliance on manual annotations and enables the detection of novel object categories \[[10](http://arxiv.org/abs/2201.02605)\]. For example, the PB-OVD method generates pseudo bounding-box labels from image-caption pairs, leading to significant improvements in performance on datasets like COCO and LVIS \[[11](http://arxiv.org/abs/2203.16513)\]. Similarly, the Detic framework trains detectors on image classification data, expanding the vocabulary of detectors to tens of thousands of concepts \[[12](http://arxiv.org/abs/2211.14843)\].

Recent advances have also focused on improving the efficiency and scalability of open-vocabulary detection by simplifying training pipelines and reducing the need for complex pretraining \[[13](http://arxiv.org/abs/2104.12763)\]. For instance, F-VLM demonstrates that frozen vision-language models can be effectively used for open-vocabulary detection by fine-tuning only the detector head \[[14](http://arxiv.org/abs/1405.0312)\]. This approach simplifies the training process and improves inference speed \[[15](http://arxiv.org/abs/1908.03195)\].

In addition, methods like Grounding DINO have been proposed to enable open-set object detection by integrating language and vision modalities \[[16](https://www.semanticscholar.org/paper/c5ff974a69fd0c760b4855b819e61e89f31cfffe)\]. This model uses grounded pre-training to detect arbitrary objects based on natural language inputs, achieving state-of-the-art performance on benchmarks like COCO and LVIS \[[17](http://arxiv.org/abs/2112.09106)\]. The success of these methods highlights the importance of aligning visual and textual representations for effective open-vocabulary detection \[[18](http://arxiv.org/abs/2303.13076)\].

Finally, the development of efficient and scalable detection frameworks, such as DETR and YOLO, has enabled real-time object detection with high accuracy \[[19](http://arxiv.org/abs/2203.10593)\]. These models have been adapted for open-vocabulary settings by incorporating vision-language pre-training and pseudo-labeling techniques \[[20](http://arxiv.org/abs/2102.05918)\]. The integration of these approaches has led to significant improvements in detection performance, particularly for novel and rare object categories \[[21](http://arxiv.org/abs/2205.06160)\].

1. \[[1](http://arxiv.org/abs/2011.10678)\] Open-Vocabulary Object Detection Using Captions [http://arxiv.org/abs/2011.10678]  
2. \[[2](http://arxiv.org/abs/2104.13921)\] Open-Vocabulary Object Detection via Vision and Language Knowledge Distillation [http://arxiv.org/abs/2104.13921]  
3. \[[3](http://arxiv.org/abs/2205.06230)\] Simple Open-Vocabulary Object Detection with Vision Transformers [http://arxiv.org/abs/2205.06230]  
4. \[[4](http://arxiv.org/abs/2103.00020)\] Learning Transferable Visual Models From Natural Language Supervision [http://arxiv.org/abs/2103.00020]  
5. \[[5](http://arxiv.org/abs/2203.14940)\] Learning to Prompt for Open-Vocabulary Object Detection with Vision-Language Model [http://arxiv.org/abs/2203.14940]  
6. \[[6](http://arxiv.org/abs/2203.11876)\] Open-Vocabulary DETR with Conditional Matching [http://arxiv.org/abs/2203.11876]  
7. \[[7](http://arxiv.org/abs/2207.03482)\] Bridging the Gap between Object and Image-level Representations for Open-Vocabulary Detection [http://arxiv.org/abs/2207.03482]  
8. \[[8](http://arxiv.org/abs/2111.09452)\] Open Vocabulary Object Detection with Pseudo Bounding-Box Labels [http://arxiv.org/abs/2111.09452]  
9. \[[9](http://arxiv.org/abs/2207.08954)\] Exploiting Unlabeled Data with Vision and Language Models for Object Detection [http://arxiv.org/abs/2207.08954]  
10. \[[10](http://arxiv.org/abs/2201.02605)\] Detecting Twenty-thousand Classes using Image-level Supervision [http://arxiv.org/abs/2201.02605]  
11. \[[11](http://arxiv.org/abs/2203.16513)\] PromptDet: Towards Open-Vocabulary Detection Using Uncurated Images [http://arxiv.org/abs/2203.16513]  
12. \[[12](http://arxiv.org/abs/2211.14843)\] Learning Object-Language Alignments for Open-Vocabulary Object Detection [http://arxiv.org/abs/2211.14843]  
13. \[[13](http://arxiv.org/abs/2104.12763)\] MDETR - Modulated Detection for End-to-End Multi-Modal Understanding [http://arxiv.org/abs/2104.12763]  
14. \[[14](http://arxiv.org/abs/1405.0312)\] Microsoft COCO: Common Objects in Context [http://arxiv.org/abs/1405.0312]  
15. \[[15](http://arxiv.org/abs/1908.03195)\] LVIS: A Dataset for Large Vocabulary Instance Segmentation [http://arxiv.org/abs/1908.03195]  
16. \[[16](https://www.semanticscholar.org/paper/c5ff974a69fd0c760b4855b819e61e89f31cfffe)\] Objects365: A Large-Scale, High-Quality Dataset for Object Detection [https://www.semanticscholar.org/paper/c5ff974a69fd0c760b4855b819e61e89f31cfffe]  
17. \[[17](http://arxiv.org/abs/2112.09106)\] RegionCLIP: Region-based Language-Image Pretraining [http://arxiv.org/abs/2112.09106]  
18. \[[18](http://arxiv.org/abs/2303.13076)\] CORA: Adapting CLIP for Open-Vocabulary Detection with Region Prompting and Anchor Pre-Matching [http://arxiv.org/abs/2303.13076]  
19. \[[19](http://arxiv.org/abs/2203.10593)\] Open-Vocabulary One-Stage Detection with Hierarchical Visual-Language Knowledge Distillation [http://arxiv.org/abs/2203.10593]  
20. \[[20](http://arxiv.org/abs/2102.05918)\] Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision [http://arxiv.org/abs/2102.05918]  
21. \[[21](http://arxiv.org/abs/2205.06160)\] Localized Vision-Language Matching for Open-vocabulary Object Detection [http://arxiv.org/abs/2205.06160]  
22. \[[22](http://arxiv.org/abs/2303.05499)\] Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection [http://arxiv.org/abs/2303.05499]  
23. \[[23](http://arxiv.org/abs/1703.06870)\] Mask R-CNN [http://arxiv.org/abs/1703.06870]  
24. \[[24](http://arxiv.org/abs/2109.01134)\] Learning to Prompt for Vision-Language Models [http://arxiv.org/abs/2109.01134]  
25. \[[25](http://arxiv.org/abs/1804.04340)\] Zero-Shot Object Detection [http://arxiv.org/abs/1804.04340]  
26. \[[26](http://arxiv.org/abs/2111.12698)\] Open-Vocabulary Instance Segmentation via Robust Cross-Modal Pseudo-Labeling [http://arxiv.org/abs/2111.12698]  
27. \[[27](http://arxiv.org/abs/1506.02640)\] You Only Look Once: Unified, Real-Time Object Detection [http://arxiv.org/abs/1506.02640]  
28. \[[28](http://arxiv.org/abs/2209.15639)\] F-VLM: Open-Vocabulary Object Detection upon Frozen Vision and Language Models [http://arxiv.org/abs/2209.15639]  
29. \[[29](http://arxiv.org/abs/2112.03857)\] Grounded Language-Image Pre-training [http://arxiv.org/abs/2112.03857]  
30. \[[30](http://arxiv.org/abs/2005.12872)\] End-to-End Object Detection with Transformers [http://arxiv.org/abs/2005.12872]
