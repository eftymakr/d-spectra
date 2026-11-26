## Related Works

Human pose estimation has been a focal point in computer vision, with significant advancements in both 2D and 3D estimation. Early approaches relied on hand-crafted features and graphical models, such as Markov Random Fields (MRFs) \[[1](http://arxiv.org/abs/1406.2984)\], to model spatial relationships between body joints. However, these methods often lacked the flexibility and accuracy required for complex human motion. The introduction of deep convolutional neural networks (ConvNets) marked a paradigm shift, enabling more robust and accurate estimation of 2D joint locations \[[2](http://arxiv.org/abs/1411.4280)\]. These networks, however, faced challenges in localization accuracy due to pooling layers that reduced spatial precision \[[2](http://arxiv.org/abs/1411.4280)\].

To address these limitations, researchers introduced refinement models that estimate joint offsets within small image regions, improving localization accuracy \[[2](http://arxiv.org/abs/1411.4280)\]. This approach was further enhanced by integrating pyramid structures to handle scale variations in human body parts \[[3](http://arxiv.org/abs/1708.01101)\]. The Pyramid Residual Module (PRMs) was designed to learn convolutional filters on various scales, enhancing scale invariance in deep convolutional neural networks (DCNNs) \[[3](http://arxiv.org/abs/1708.01101)\]. This method was validated on standard benchmarks, achieving state-of-the-art results \[[3](http://arxiv.org/abs/1708.01101)\].

In parallel, the problem of 3D human pose estimation from 2D images has been tackled using regression-based methods that map 2D joint positions to 3D space. These methods often represent poses using distance matrices, allowing for more precise regression of 3D coordinates \[[7](http://arxiv.org/abs/1611.09010)\]. Additionally, structured feature learning frameworks have been proposed to capture correlations between body joints at the feature level, improving the accuracy of pose estimation \[[5](http://arxiv.org/abs/1603.09065)\]. These frameworks leverage geometrical transform kernels implemented via convolutional layers to model joint relationships \[[5](http://arxiv.org/abs/1603.09065)\].

Another line of research focuses on modeling spatial and temporal dependencies in 3D pose estimation. Graph convolutional networks (GCNs) have been used to incorporate domain knowledge about human body configurations, improving the accuracy of 3D pose estimation \[[10](https://www.semanticscholar.org/paper/50167a9e6bdc1f64a58fe8a3c990105fec0bd2bc)\]. These models explicitly model spatial relationships and temporal consistency across frames, leading to more coherent and accurate pose estimates \[[10](https://www.semanticscholar.org/paper/50167a9e6bdc1f64a58fe8a3c990105fec0bd2bc)\]. Furthermore, transformer-based architectures have been introduced to model both spatial and temporal dependencies in a unified framework, achieving state-of-the-art performance on benchmark datasets \[[16](http://arxiv.org/abs/2103.10455)\].

Recent work has also emphasized the importance of modeling long-range dependencies between body parts. This has led to the development of graph-based models that capture both local and global interactions, such as the proposed Pyramid Graph Attention (PGA) module \[[30](http://arxiv.org/abs/1905.05754)\]. These models leverage pyramid structures to better learn long-range dependencies, capturing correlations across joints and groups in a cross-scale manner \[[30](http://arxiv.org/abs/1905.05754)\]. The integration of graph attention mechanisms with convolutional modules has enabled the development of lightweight, multi-scale transformer architectures, such as the Pyramid Graph Transformer (PGFormer), which achieves lower error and smaller model size compared to existing methods \[[30](http://arxiv.org/abs/1905.05754)\].

In summary, the field of human pose estimation has evolved from traditional graphical models and hand-crafted features to deep learning-based approaches that leverage convolutional networks, graph convolutions, and transformers. These advancements have significantly improved the accuracy and robustness of pose estimation, particularly in challenging scenarios involving scale variations, occlusions, and depth ambiguity \[[3](http://arxiv.org/abs/1708.01101)\]\[[5](http://arxiv.org/abs/1603.09065)\]\[[7](http://arxiv.org/abs/1611.09010)\]\[[10](https://www.semanticscholar.org/paper/50167a9e6bdc1f64a58fe8a3c990105fec0bd2bc)\]\[[16](http://arxiv.org/abs/2103.10455)\]\[[30](http://arxiv.org/abs/1905.05754)\].

References:
1. \[[1](http://arxiv.org/abs/1406.2984)\] Joint Training of a Convolutional Network and a Graphical Model for Human Pose Estimation
2. \[[2](http://arxiv.org/abs/1411.4280)\] Efficient object localization using Convolutional Networks
3. \[[3](http://arxiv.org/abs/1708.01101)\] Learning Feature Pyramids for Human Pose Estimation
4. \[[4](https://www.semanticscholar.org/paper/ec3eddefc3c658ed8de35ed18bfa7e6ce675019a)\] Reconstructing 3D Human Pose from 2D Image Landmarks
5. \[[5](http://arxiv.org/abs/1603.09065)\] Structured Feature Learning for Pose Estimation
6. \[[6](http://arxiv.org/abs/1407.3399)\] Articulated Pose Estimation by a Graphical Model with Image Dependent Pairwise Relations
7. \[[7](http://arxiv.org/abs/1611.09010)\] 3D Human Pose Estimation from a Single Image via Distance Matrix Regression
8. \[[8](https://www.semanticscholar.org/paper/db466d02ec9f7f47ee11590d0feeb6330256c98d)\] Learning Pose Grammar to Encode Human Body Configuration for 3D Pose Estimation
9. \[[9](http://arxiv.org/abs/1312.4659)\] DeepPose: Human Pose Estimation via Deep Neural Networks
10. \[[10](https://www.semanticscholar.org/paper/50167a9e6bdc1f64a58fe8a3c990105fec0bd2bc)\] Exploiting Spatial-Temporal Relationships for 3D Pose Estimation via Graph Convolutional Networks
11. \[[11](http://arxiv.org/abs/1704.00159)\] Compositional Human Pose Regression
12. \[[12](http://arxiv.org/abs/1406.2282)\] Robust Estimation of 3D Human Poses from a Single Image
13. \[[13](http://arxiv.org/abs/1711.08585)\] Exploiting Temporal Information for 3D Human Pose Estimation
14. \[[14](http://arxiv.org/abs/1705.03098)\] A Simple Yet Effective Baseline for 3d Human Pose Estimation
15. \[[15](http://arxiv.org/abs/1511.09439)\] Sparseness Meets Deepness: 3D Human Pose Estimation from Monocular Video
16. \[[16](http://arxiv.org/abs/2103.10455)\] 3D Human Pose Estimation with Spatial and Temporal Transformers
17. \[[17](http://arxiv.org/abs/1605.05180)\] Structured Prediction of 3D Human Pose with Deep Neural Networks
18. \[[18](http://arxiv.org/abs/2307.05853)\] GLA-GCN: Global-local Adaptive Graph Convolutional Network for 3D Human Pose Estimation from Monocular Video
19. \[[19](http://arxiv.org/abs/2308.05298)\] Double-chain Constraints for 3D Human Pose Estimation in Images and Videos
20. \[[20](http://arxiv.org/abs/2111.12707)\] MHFormer: Multi-Hypothesis Transformer for 3D Human Pose Estimation
21. \[[21](http://arxiv.org/abs/2008.09047)\] Pose2Mesh: Graph Convolutional Network for 3D Human Pose and Mesh Recovery from a 2D Human Pose
22. \[[22](http://arxiv.org/abs/1904.04812)\] Unsupervised 3D Pose Estimation With Geometric Self-Supervision
23. \[[23](https://www.semanticscholar.org/paper/555a23a05777a0b03614b195c7c72f7c626a97e9)\] Anatomy-Aware 3D Human Pose Estimation With Bone-Based Pose Decomposition
24. \[[24](http://arxiv.org/abs/2109.02303)\] Encoder-decoder with Multi-level Attention for 3D Human Shape and Pose Estimation
25. \[[25](http://arxiv.org/abs/1803.04775)\] Learning Monocular 3D Human Pose Estimation from Multi-view Images
26. \[[26](http://arxiv.org/abs/2007.07053)\] Unsupervised 3D Human Pose Representation with Viewpoint and Pose Disentanglement
27. \[[27](http://arxiv.org/abs/2111.00950)\] Higher-Order Implicit Fairing Networks for 3D Human Pose Estimation
28. \[[28](http://arxiv.org/abs/2206.06420)\] GraphMLP: A Graph MLP-Like Architecture for 3D Human Pose Estimation
29. \[[29](http://arxiv.org/abs/1909.12828)\] Learning to Reconstruct 3D Human Pose and Shape via Model-Fitting in the Loop
30. \[[30](http://arxiv.org/abs/1905.05754)\] Learnable Triangulation of Human Pose
