## Related Works

Video frame interpolation has been a focal point in video processing, with recent advances leveraging deep learning to achieve high-quality results. Traditional methods often rely on optical flow estimation and motion compensation, but these approaches are limited in their ability to handle complex motion and occlusion \[[24](https://www.semanticscholar.org/paper/bb4a9650ca3946c70a7e92007cc61dc0dfd75522)\]. For instance, the Super SloMo method \[[1](http://arxiv.org/abs/1712.00080)\] proposes an end-to-end convolutional neural network for variable-length multi-frame interpolation, combining motion interpretation and occlusion reasoning. This approach uses a U-Net to compute bi-directional optical flow and refines the results using another U-Net to predict visibility maps, which helps avoid artifacts in occluded regions. However, these methods typically require high computational resources and may not scale well to high-resolution videos \[[3](https://www.semanticscholar.org/paper/089f2072c95c244f3b7f4df404562bb4afe24448)\].

More recently, methods such as Zoom-In-To-Check \[[2](http://arxiv.org/abs/1812.01210)\] have introduced instance-level supervision to improve the quality of interpolated frames by leveraging high-resolution object details. This method uses a cascade network with a flow-warping module and an image synthesis module to generate intermediate frames. It also employs object detection proposals and adversarial losses to refine the details of objects in the interpolated frames. While effective, such methods may still be computationally intensive and may not generalize well to different scenarios \[[4](http://arxiv.org/abs/1711.07566)\].

The IM-Net \[[3](https://www.semanticscholar.org/paper/089f2072c95c244f3b7f4df404562bb4afe24448)\] addresses the challenge of high-resolution video frame interpolation by using an economic structured architecture and end-to-end training with multi-scale tailored losses. This method formulates interpolated motion estimation as a classification task rather than regression, leading to improved performance on high-resolution datasets. Additionally, it achieves fast inference times, making it suitable for real-time applications. However, the performance of these methods may degrade when dealing with complex motion patterns \[[5](https://www.semanticscholar.org/paper/a285a442317f24068f7cc262531976e82a5c41d6)\].

Unsupervised video interpolation techniques, such as those proposed in \[[6](http://arxiv.org/abs/1906.05928)\], have also gained traction. These methods aim to synthesize high frame rate videos directly from low frame rate videos using cycle consistency. By optimizing models to minimize the discrepancy between the center frame and its cycle reconstruction, these methods achieve results comparable to supervised approaches. The introduction of a pseudo supervised loss term further enhances the adaptation of pre-trained models to new domains, improving performance on benchmark datasets \[[7](http://arxiv.org/abs/1604.00449)\].

Another approach, the Video Frame Interpolation Transformer \[[9](http://arxiv.org/abs/2111.13817)\], leverages the self-attention mechanism of Transformers to capture long-range dependencies and content-aware aggregation weights. This allows for more accurate and visually pleasing frame interpolation compared to traditional CNN-based methods. The method also introduces local attention and a space-time separation strategy to reduce computational costs and improve performance \[[10](https://www.semanticscholar.org/paper/23c9b2b3d315dd81563f57bbec8fda28d53700a6)\].

In summary, while many methods have been proposed for video frame interpolation, there remains a need for efficient and high-quality solutions that can handle complex motion and occlusion. The proposed method in this paper, PS4PRO, addresses these challenges by leveraging video frame interpolation as a data augmentation technique for neural rendering, thereby improving the reconstruction quality of 3D scenes \[[11](http://arxiv.org/abs/1506.06825)\].

References:
\[[1](http://arxiv.org/abs/1712.00080)\] http://arxiv.org/abs/1712.00080
\[[2](http://arxiv.org/abs/1812.01210)\] http://arxiv.org/abs/1812.01210
\[[3](https://www.semanticscholar.org/paper/089f2072c95c244f3b7f4df404562bb4afe24448)\] https://www.semanticscholar.org/paper/089f2072c95c244f3b7f4df404562bb4afe24448
\[[4](http://arxiv.org/abs/1711.07566)\] http://arxiv.org/abs/1711.07566
\[[5](https://www.semanticscholar.org/paper/a285a442317f24068f7cc262531976e82a5c41d6)\] http://arxiv.org/abs/1906.05928
\[[6](http://arxiv.org/abs/1906.05928)\] http://arxiv.org/abs/2007.11762
\[[7](http://arxiv.org/abs/1604.00449)\] http://arxiv.org/abs/2111.13817
\[[8](http://arxiv.org/abs/2007.11762)\] https://www.semanticscholar.org/paper/23c9b2b3d315dd81563f57bbec8fda28d53700a6
\[[9](http://arxiv.org/abs/2111.13817)\] http://arxiv.org/abs/2003.07514
\[[10](https://www.semanticscholar.org/paper/23c9b2b3d315dd81563f57bbec8fda28d53700a6)\] http://arxiv.org/abs/2004.00779
\[[11](http://arxiv.org/abs/1506.06825)\] http://arxiv.org/abs/2203.00137
