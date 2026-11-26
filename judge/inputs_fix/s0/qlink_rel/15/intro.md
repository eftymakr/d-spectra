## Related Works

Brain tumor segmentation remains a challenging task in medical image analysis due to the high variability in tumor shapes, sizes, and intensities across different modalities \[[1](https://www.semanticscholar.org/paper/420f3f1078a6d8e0696572c032877079286051c6)\]. Early approaches relied on manual segmentation, which is time-consuming and prone to human error \[[12](https://www.semanticscholar.org/paper/580062407427236ced45253a2ff7df2e147a81e2)\]. With the advent of deep learning, several studies have proposed convolutional neural networks (CNNs) for automated segmentation, leading to significant improvements in accuracy and efficiency \[[14](http://arxiv.org/abs/2110.02519)\]. 

A notable work by Ronneberger et al. introduced the U-Net architecture, which combines an encoder-decoder structure with skip connections to capture both local and global features \[[14](http://arxiv.org/abs/2110.02519)\]. This design has become a foundational model for many subsequent studies in medical image segmentation. For instance, the 3D U-Net \[[20](http://arxiv.org/abs/1606.06650)\] extended the U-Net framework to handle volumetric data, enabling dense 3D segmentation from sparse annotations. This approach was validated on the BraTS challenge datasets, demonstrating its effectiveness in handling complex 3D structures \[[20](http://arxiv.org/abs/1606.06650)\]. 

Several studies have explored the use of pre-trained models to improve segmentation performance, particularly in scenarios with limited annotated data \[[24](http://arxiv.org/abs/2011.11052)\]. For example, the work by \[[24](http://arxiv.org/abs/2011.11052)\] proposed an asymmetric U-Net architecture that incorporates the EfficientNet model, allowing for efficient transfer learning from 2D classification networks to 3D segmentation tasks. This approach reduced the computational burden while maintaining high accuracy. Similarly, the HDC-Net \[[25](https://www.semanticscholar.org/paper/9bf1c55d5441b29acf35c2193342723187dbe896)\] introduced a hierarchical decoupled convolution module to replace expensive 3D convolutions, achieving high accuracy with reduced computational complexity. 

The use of ensemble methods has also been explored to enhance segmentation performance. For example, the EMMA approach \[[29](http://arxiv.org/abs/1711.01468)\] combined predictions from multiple models and architectures, leading to robust performance and winning the BRATS 2017 competition. This method reduced the influence of individual model configurations and improved generalization across different datasets. 

In addition to CNNs, transformer-based models have recently gained attention for their ability to capture long-range dependencies in 3D medical images \[[21](http://arxiv.org/abs/2103.04430)\]. The TransBTS model \[[21](http://arxiv.org/abs/2103.04430)\] combined 3D CNNs with transformers to exploit both local and global features, achieving competitive results on the BraTS 2019 and 2020 datasets. This approach demonstrated the potential of hybrid architectures in improving segmentation accuracy for complex 3D structures.

Moreover, the nnU-Net framework \[[16](http://arxiv.org/abs/2011.00848)\] has emerged as a self-configuring method for biomedical image segmentation, adapting to different datasets and tasks. This model was further refined with BraTS-specific modifications, leading to improved performance in the BraTS 2020 challenge \[[16](http://arxiv.org/abs/2011.00848)\]. The integration of pre-trained weights from ImageNet into the nnU-Net framework has also been explored to reduce training requirements and improve efficiency \[[1](https://www.semanticscholar.org/paper/420f3f1078a6d8e0696572c032877079286051c6)\]. 

In summary, the field of brain tumor segmentation has seen significant advancements through the development of deep learning models, including U-Net variants, transformer-based architectures, and ensemble methods. These approaches have addressed key challenges such as computational efficiency, class imbalance, and the need for robust generalization across diverse datasets \[[1](https://www.semanticscholar.org/paper/420f3f1078a6d8e0696572c032877079286051c6)\]\[[14](http://arxiv.org/abs/2110.02519)\]\[[20](http://arxiv.org/abs/1606.06650)\]\[[21](http://arxiv.org/abs/2103.04430)\]\[[24](http://arxiv.org/abs/2011.11052)\]\[[25](https://www.semanticscholar.org/paper/9bf1c55d5441b29acf35c2193342723187dbe896)\]\[[29](http://arxiv.org/abs/1711.01468)\].

References  
\[[1](https://www.semanticscholar.org/paper/420f3f1078a6d8e0696572c032877079286051c6)\] https://www.semanticscholar.org/paper/420f3f1078a6d8e0696572c032877079286051c6  
\[[2](http://arxiv.org/abs/1505.03540)\] http://arxiv.org/abs/1505.03540  
\[[3](http://arxiv.org/abs/1810.11654)\] http://arxiv.org/abs/1505.04597  
\[[4](http://arxiv.org/abs/1505.04597)\] http://arxiv.org/abs/1603.05959  
\[[5](http://arxiv.org/abs/1603.05959)\] http://arxiv.org/abs/1606.04797  
\[[6](http://arxiv.org/abs/1705.03820)\] http://arxiv.org/abs/1705.03820  
\[[7](http://arxiv.org/abs/1812.01049)\] http://arxiv.org/abs/1709.00382  
\[[8](http://arxiv.org/abs/1606.04797)\] http://arxiv.org/abs/1802.10508  
\[[9](http://arxiv.org/abs/1709.00382)\] http://arxiv.org/abs/1810.11654  
\[[10](http://arxiv.org/abs/2001.02040)\] http://arxiv.org/abs/1812.01049  
\[[11](http://arxiv.org/abs/1802.10508)\] http://arxiv.org/abs/1812.11588  
\[[12](https://www.semanticscholar.org/paper/580062407427236ced45253a2ff7df2e147a81e2)\] https://www.semanticscholar.org/paper/580062407427236ced45253a2ff7df2e147a81e2  
\[[13](http://arxiv.org/abs/2201.01266)\] http://arxiv.org/abs/2011.00848  
\[[14](http://arxiv.org/abs/2110.02519)\] http://arxiv.org/abs/2103.04430  
\[[15](http://arxiv.org/abs/2010.13082)\] http://arxiv.org/abs/2110.02519  
\[[16](http://arxiv.org/abs/2011.00848)\] http://arxiv.org/abs/2110.03352  
\[[17](http://arxiv.org/abs/1811.02629)\] http://arxiv.org/abs/2110.03352  
\[[18](https://www.semanticscholar.org/paper/f28e387d4229c5f690ce4570a391c0f47e7155c7)\] http://arxiv.org/abs/2110.03352  
\[[19](http://arxiv.org/abs/2107.02314)\] http://arxiv.org/abs/2107.02314  
\[[20](http://arxiv.org/abs/1606.06650)\] http://arxiv.org/abs/2110.03352  
\[[21](http://arxiv.org/abs/2103.04430)\] http://arxiv.org/abs/2103.04430  
\[[22](http://arxiv.org/abs/1807.07716)\] http://arxiv.org/abs/2110.03352  
\[[23](http://arxiv.org/abs/2110.03352)\] http://arxiv.org/abs/2110.03352  
\[[24](http://arxiv.org/abs/2011.11052)\] http://arxiv.org/abs/2110.03352  
\[[25](https://www.semanticscholar.org/paper/9bf1c55d5441b29acf35c2193342723187dbe896)\] http://arxiv.org/abs/2110.03352  
\[[26](https://www.semanticscholar.org/paper/b9c3631120c171570b94f946273b98c32505fc9a)\] http://arxiv.org/abs/2110.03352  
\[[27](http://arxiv.org/abs/1411.4038)\] http://arxiv.org/abs/2110.03352  
\[[28](https://www.semanticscholar.org/paper/b72771c316d60190aff053ef8a216ba57d62f541)\] http://arxiv.org/abs/2110.03352  
\[[29](http://arxiv.org/abs/1711.01468)\] http://arxiv.org/abs/2110.03352
