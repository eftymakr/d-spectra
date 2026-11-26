## Related Works

Brain tumor segmentation remains a critical challenge in medical image analysis due to the complexity of tumor morphology, limited data availability, and the need for accurate and efficient segmentation methods \[[1](http://arxiv.org/abs/2011.11052)\]. Recent advances in deep learning have significantly improved the performance of segmentation models, with U-Net-based architectures dominating the field \[[2](https://www.semanticscholar.org/paper/1bcdc3823fea644a507075b933912fa82167c887)\]. The U-Net architecture, originally designed for biomedical image segmentation, has been widely adapted for brain tumor segmentation tasks due to its symmetric encoder-decoder structure and skip connections \[[3](http://arxiv.org/abs/1812.01049)\]. However, training 3D U-Net models often requires extensive computational resources and large datasets, limiting their practical application in clinical settings \[[4](https://www.semanticscholar.org/paper/8689d964b3d1acacfa698c9d81314a9571819757)\].

Several studies have explored ways to improve the efficiency of 3D U-Net models by integrating pre-trained weights from other domains, such as ImageNet, to reduce training time and improve performance \[[5](https://www.semanticscholar.org/paper/237e15ea6558e45e544cf2efc68e675cf1c44547)\]. For instance, the EfficientNet model has been combined with U-Net to create hybrid architectures that leverage the strengths of both models \[[6](https://www.semanticscholar.org/paper/281ede296764b95c329a7093e3b40b0b0c3ddee8)\]. Similarly, the use of transfer learning with pre-trained models like ResNet50, DenseNet169, and EfficientNet-B7 has shown promising results in brain tumor segmentation tasks \[[7](https://www.semanticscholar.org/paper/e7485173b124c2b5a86f6cd00a871b9c1fa8a028)\]. These models have been trained and validated on the BraTS datasets, which include multimodal MRI scans of brain tumors \[[8](http://arxiv.org/abs/2504.13200)\].

The nnU-Net framework has also been proposed as a more efficient alternative to traditional U-Net models, with modifications to the network structure and training strategy to improve performance while reducing computational costs \[[9](https://www.semanticscholar.org/paper/c4ccda0585b7f8040923ab86270d9b7ff2f4e03e)\]. This framework has been further enhanced by incorporating depthwise separable convolutions and attention mechanisms to improve feature extraction and reduce parameter count \[[10](https://www.semanticscholar.org/paper/6c9c65db8099038733cc0644265764c0570d4fbe)\]. Additionally, some studies have introduced novel architectures such as the 3D-Znet model, which uses variational autoencoder–autodecoder structures to improve segmentation accuracy \[[11](http://arxiv.org/abs/1907.00281)\].

Another approach to improving segmentation performance involves the use of attention mechanisms and multi-scale feature fusion. For example, the 3D attention-based U-Net architecture has been proposed to enhance segmentation accuracy by emphasizing malignant tissues and reducing the influence of healthy tissues \[[12](http://arxiv.org/abs/2402.07008)\]. Similarly, the Dilated Inception U-Net (DIU-Net) integrates Inception modules and dilated convolutions to extract both local and global contextual information, leading to improved segmentation results \[[13](http://arxiv.org/abs/2210.13336)\].

The proposed methods in this paper build upon these advancements by integrating axial-coronal-sagittal convolutions and pre-trained weights from ImageNet into the nnU-Net framework, reducing training epochs and improving efficiency \[[14](http://arxiv.org/abs/1709.02967)\]. Additionally, the paper explores a joint classification and segmentation model that leverages pre-trained encoders from a brain glioma grade classification proxy task, further enhancing segmentation performance \[[15](https://www.semanticscholar.org/paper/bccbc57c2b9a995a1cd387c45fc21f12af3182ba)\].

\[[1](http://arxiv.org/abs/2011.11052)\] Document 1  
\[[2](https://www.semanticscholar.org/paper/1bcdc3823fea644a507075b933912fa82167c887)\] Document 2  
\[[3](http://arxiv.org/abs/1812.01049)\] Document 3  
\[[4](https://www.semanticscholar.org/paper/8689d964b3d1acacfa698c9d81314a9571819757)\] Document 4  
\[[5](https://www.semanticscholar.org/paper/237e15ea6558e45e544cf2efc68e675cf1c44547)\] Document 5  
\[[6](https://www.semanticscholar.org/paper/281ede296764b95c329a7093e3b40b0b0c3ddee8)\] Document 6  
\[[7](https://www.semanticscholar.org/paper/e7485173b124c2b5a86f6cd00a871b9c1fa8a028)\] Document 7  
\[[8](http://arxiv.org/abs/2504.13200)\] Document 8  
\[[9](https://www.semanticscholar.org/paper/c4ccda0585b7f8040923ab86270d9b7ff2f4e03e)\] Document 9  
\[[10](https://www.semanticscholar.org/paper/6c9c65db8099038733cc0644265764c0570d4fbe)\] Document 10  
\[[11](http://arxiv.org/abs/1907.00281)\] Document 11  
\[[12](http://arxiv.org/abs/2402.07008)\] Document 12  
\[[13](http://arxiv.org/abs/2210.13336)\] Document 13  
\[[14](http://arxiv.org/abs/1709.02967)\] Document 14  
\[[15](https://www.semanticscholar.org/paper/bccbc57c2b9a995a1cd387c45fc21f12af3182ba)\] Document 15
