## Related Works

Anomaly detection in industrial settings has garnered significant attention due to its critical role in quality control and fault prevention in modern manufacturing processes. Existing approaches often rely on deep learning techniques, which have seen remarkable progress in recent years. However, many state-of-the-art models are computationally intensive and unsuitable for deployment on resource-constrained embedded devices \[[1](http://arxiv.org/abs/2301.11514)\]. This limitation is particularly relevant for Small and Medium Enterprises (SMEs), which often lack the infrastructure to support large-scale AI systems \[[1](http://arxiv.org/abs/2301.11514)\].

Several studies have explored the use of autoencoders for unsupervised anomaly detection, where the reconstruction error is used to identify anomalies \[[2](http://arxiv.org/abs/1807.02011)\]. However, these methods often struggle with localization accuracy and fail to capture structural information, leading to suboptimal performance in real-world scenarios \[[2](http://arxiv.org/abs/1807.02011)\]. To address this, perceptual loss functions based on structural similarity have been proposed, which better capture local dependencies and improve segmentation accuracy \[[2](http://arxiv.org/abs/1807.02011)\].

Semi-supervised approaches, such as GANomaly, have also been introduced to tackle the class imbalance problem in anomaly detection \[[3](http://arxiv.org/abs/1805.06725)\]. These models leverage adversarial training to learn the distribution of normal samples and detect anomalies based on their deviation from this distribution \[[3](http://arxiv.org/abs/1805.06725)\]. While effective, such models often require extensive training and are not always suitable for deployment on embedded systems \[[3](http://arxiv.org/abs/1805.06725)\].

Recent advances in foundation models, such as DINOv2, have demonstrated the potential of vision-only models for few-shot anomaly detection \[[4](http://arxiv.org/abs/2405.14529)\]. These models leverage high-quality visual features and can achieve competitive performance without the need for additional training or fine-tuning \[[4](http://arxiv.org/abs/2405.14529)\]. Similarly, PatchCore has been proposed as a memory-based approach that uses maximally representative patch-features to achieve state-of-the-art performance in both detection and localization tasks \[[5](http://arxiv.org/abs/2106.08265)\].

The importance of model efficiency and mobile-friendliness has led to the development of lightweight models, such as MobileSAM, which is a variant of the Segment Anything Model (SAM) optimized for deployment on edge devices \[[13](http://arxiv.org/abs/2306.14289)\]. MobileSAM achieves comparable performance to its larger counterpart while significantly reducing computational requirements, making it suitable for real-time applications \[[13](http://arxiv.org/abs/2306.14289)\].

In addition to model efficiency, the ability to handle noisy data is crucial for practical deployment. SoftPatch has been proposed as a memory-based unsupervised anomaly detection method that effectively denoises data at the patch level \[[6](http://arxiv.org/abs/2403.14233)\]. This approach improves robustness to label-level noise and maintains strong modeling capabilities for normal data \[[6](http://arxiv.org/abs/2403.14233)\].

Finally, the integration of attention mechanisms has also been explored to enhance the performance of anomaly detection models \[[20](http://arxiv.org/abs/1706.03762)\]. Attention-based models, such as the Transformer, have shown promise in capturing long-range dependencies and improving the accuracy of anomaly localization \[[21](http://arxiv.org/abs/2101.01169)\].

In summary, while many existing approaches have made significant strides in anomaly detection, there remains a need for models that are both efficient and robust, particularly for deployment on resource-constrained devices. The proposed KairosAD model addresses these challenges by leveraging the MobileSAM model, offering a promising solution for real-world industrial applications \[[1](http://arxiv.org/abs/2301.11514)\].

### References

1. Deep Industrial Image Anomaly Detection: A Survey [http://arxiv.org/abs/2301.11514]  
2. Improving Unsupervised Defect Segmentation by Applying Structural Similarity to Autoencoders [http://arxiv.org/abs/1807.02011]  
3. GANomaly: Semi-Supervised Anomaly Detection via Adversarial Training [http://arxiv.org/abs/1805.06725]  
4. AnomalyDINO: Boosting Patch-based Few-shot Anomaly Detection with DINOv2 [http://arxiv.org/abs/2405.14529]  
5. Towards Total Recall in Industrial Anomaly Detection [http://arxiv.org/abs/2106.08265]  
6. SoftPatch: Unsupervised Anomaly Detection with Noisy Data [http://arxiv.org/abs/2403.14233]  
7. A SAM-guided Two-stream Lightweight Model for Anomaly Detection [http://arxiv.org/abs/2402.19145]  
8. Segment Anything [http://arxiv.org/abs/2304.02643]  
9. Learning Transferable Visual Models From Natural Language Supervision [http://arxiv.org/abs/2103.00020]  
10. Emerging Properties in Self-Supervised Vision Transformers [http://arxiv.org/abs/2104.14294]  
11. DINOv2: Learning Robust Visual Features without Supervision [http://arxiv.org/abs/2304.07193]  
12. Faster Segment Anything: Towards Lightweight SAM for Mobile Applications [http://arxiv.org/abs/2306.14289]
