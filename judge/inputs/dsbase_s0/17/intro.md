## Related Works

Semi-supervised learning (SSL) has gained significant attention for its ability to improve model performance by leveraging both labeled and unlabeled data. However, traditional SSL methods assume that the distribution of labeled and unlabeled data is identical, which is often not the case in real-world applications \[[Kuniaki Saito' 2021-05-28](http://arxiv.org/abs/2105.14148v2)\]. In practice, unlabeled data may contain out-of-distribution (OOD) samples, referred to as outliers, which can significantly degrade the performance of SSL models \[[Yue Fan' 2023-11-17](http://arxiv.org/abs/2311.10572v1)\]. Several studies have addressed this issue by introducing open-set SSL frameworks that handle the presence of outliers \[[Yen-Cheng Liu' 2022-08-29](http://arxiv.org/abs/2208.13722v1)\].

One approach to open-set SSL is the use of outlier detection mechanisms to filter out OOD samples during training \[[Zekun Li' 2023-08-25](http://arxiv.org/abs/2308.13168v1)\]. For example, OpenMatch \[[Yang Yang' 2024-05-11](http://arxiv.org/abs/2405.06979v2)\] integrates novelty detection with consistency regularization to improve robustness against outliers. Similarly, IOMatch \[[Erik Wallin' 2023-01-24](http://arxiv.org/abs/2301.10127v3)\] proposes a framework that jointly utilizes inliers and outliers, even when distinguishing between them is challenging. These methods aim to enhance the robustness of SSL models by explicitly addressing the presence of OOD data \[[Yang Yu' 2023-03-21](http://arxiv.org/abs/2303.12091v4)\].

Another line of research focuses on improving the generalization of SSL models by incorporating self-supervised learning techniques \[[Jongjin Park' 2021-06-29](http://arxiv.org/abs/2107.08943v3)\]. For instance, SelfMatch \[[Zerun Wang' 2023-05-23](http://arxiv.org/abs/2305.13802v3)\] combines contrastive self-supervision with consistency regularization to achieve state-of-the-art results on benchmark datasets. Similarly, FreeMatch \[[Zhe Huang' 2024-03-15](http://arxiv.org/abs/2403.10658v1)\] introduces a self-adaptive thresholding mechanism to improve the utilization of unlabeled data in SSL. These methods demonstrate that self-supervised learning can complement SSL by providing more reliable pseudo-labels \[[Andreas Lohrer' 2022-11-23](http://arxiv.org/abs/2211.13314v2)\].

In addition to self-supervised learning, some studies have explored the use of generative adversarial networks (GANs) for SSL \[[Phi Vu Tran' 2019-06-25](http://arxiv.org/abs/1906.10343v2)\]. For example, Bad GAN \[[Doyup Lee' 2022-01-17](http://arxiv.org/abs/2201.06247v2)\] learns a classifier using unrealistic samples, while Triple GAN \[[Deepak Pathak' 2019-06-10](http://arxiv.org/abs/1906.04161v1)\] leverages good generated samples to improve classification results. These methods highlight the potential of GAN-based approaches in SSL, although they often require careful tuning to avoid performance degradation \[[Yan Luo' 2022-01-23](http://arxiv.org/abs/2201.09196v2)\].

Furthermore, the integration of semi-supervised learning with other paradigms, such as federated learning, has also been explored \[[Zhen Fang' 2021-06-30](http://arxiv.org/abs/2106.15792v1)\]. FedMatch \[[Zhanyun Lu' 2024-08-22](http://arxiv.org/abs/2408.12355v1)\] combines federated learning with SSL to address the challenge of limited labeled data in distributed settings. This approach enables the training of models across multiple clients while maintaining privacy and reducing the reliance on centralized labeled data \[[Huayi Zhou' 2024-04-03](http://arxiv.org/abs/2404.02544v4)\].

In summary, the field of SSL has seen significant advancements, particularly in handling open-set scenarios and improving the robustness of models against outliers. The proposed DAC framework builds upon these contributions by introducing a novel approach that leverages prediction disagreements among multiple models to enhance robustness in open-set SSL \[[Martha Dais Ferreira' 2022-07-12](http://arxiv.org/abs/2207.05514v2)\].

### References

1. Document 1: OpenMatch: Open-set Consistency Regularization for Semi-supervised Learning with Outliers
2. Document 2: Learning Bounds for Open-Set Learning
3. Document 6: OpenMatch: Open-set Consistency Regularization for Semi-supervised Learning with Outliers
4. Document 12: IOMatch: Simplifying Open-Set Semi-Supervised Learning with Joint Inliers and Outliers Utilization
5. Document 13: Contrastive Regularization for Semi-Supervised Learning
6. Document 14: OpenCoS: Contrastive Semi-supervised Learning for Handling Open-set Unlabeled Data
7. Document 15: Learning to Predict Gradients for Semi-supervised Continual Learning
8. Document 16: Exploring Self-Supervised Regularization for Supervised and Semi-supervised Learning
9. Document 17: SelfMatch: Combining Contrastive Self-Supervision and Consistency for Semi-supervised Learning
10. Document 18: Towards Label-efficient Automatic Diagnosis and Analysis: A Comprehensive Survey of Advanced Deep Learning-based Weakly-supervised, Semi-supervised and Self-supervised Techniques in Histopathological Image Analysis
11. Document 19: Improving Open-Set Semi-supervised Learning with Self-Supervision
12. Document 20: Adaptive Negative Evidential Deep Learning for Open-set Semi-supervised Learning
13. Document 21: Personalized Semi-Supervised Federated Learning for Human Activity Recognition
14. Document 22: A semi-supervised methodology for fishing activity detection using the geometry behind the trajectory of multiple vessels
15. Document 23: XGBOD: Improving Supervised Outlier Detection with Unsupervised Representation Learning
16. Document 24: Deep Anomaly Detection with Outlier Exposure
17. Document 25: Exploring Self-Supervised Regularization for Supervised and Semi-supervised Learning
18. Document 26: Outlier Robust Extreme Learning Machine for Multi-Target Regression
19. Document 27: Learning to Predict Gradients for Semi-supervised Continual Learning
