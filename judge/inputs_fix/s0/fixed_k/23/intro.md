## Related Works

Automatic geometric calibration of radar and camera systems has been an active research area, with several notable approaches proposed in recent years. Early methods often relied on target-based calibration, which required specialized infrastructure and controlled environments \[[1](http://arxiv.org/abs/2307.15264)\]. For instance, a method proposed in \[[1](http://arxiv.org/abs/2307.15264)\] uses a single corner reflector (CR) and iteratively collects radar and camera data to obtain extrinsic calibration, achieving an AED error of 15.31 pixels. However, these methods are limited by their reliance on predefined calibration targets and complex setup procedures.

To overcome these limitations, targetless calibration methods have emerged, leveraging the common features between radar and camera data. A method introduced in \[[2](http://arxiv.org/abs/2309.00787)\] uses deep learning to extract common features from raw radar data and camera images, enabling online calibration without the need for dedicated targets. This approach implicitly utilizes common features to match objects across modalities and employs RANSAC and Levenberg-Marquardt (LM) for robustness and accuracy. Similarly, \[[3](http://arxiv.org/abs/2211.01871)\] proposes a targetless spatiotemporal calibration method that leverages radar ego-velocity measurements and does not require specialized infrastructure, demonstrating accurate calibration in real-world environments.

Another notable approach is the use of continuous-time models for extrinsic calibration. \[[4](http://arxiv.org/abs/2103.07505)\] presents a continuous-time 3D radar-to-camera calibration algorithm that utilizes radar velocity measurements and does not require specialized radar retroreflectors. This method is particularly useful for low-cost 3D millimetre-wavelength radars, which are becoming more prevalent in autonomous driving applications.

In addition to calibration, several works focus on radar-camera fusion for object detection and semantic segmentation. \[[5](http://arxiv.org/abs/1904.08743)\] introduces a data-driven method for automatic rotational radar-camera calibration without dedicated targets, using a coarse and fine convolutional neural network. This approach demonstrates robust sensor registration and generalization across different sensor alignments. \[[6](http://arxiv.org/abs/2309.15465)\] further explores radar-camera fusion in bird's-eye view (BEV) feature maps, proposing a novel fusion network that outperforms camera-only and radar-only baselines.

Recent advances in radar-camera fusion have also focused on multi-level fusion strategies. \[[7](http://arxiv.org/abs/2305.15883)\] proposes RCM-Fusion, which fuses radar and camera data at both feature and instance levels, achieving state-of-the-art performance on the nuScenes dataset. The method uses a Radar Guided BEV Encoder to transform camera features into BEV representations and a Radar Grid Point Refinement module to reduce localization errors.

Moreover, \[[8](http://arxiv.org/abs/2304.10410)\] presents ClusterFusion, an architecture that leverages the local spatial features of radar point clouds by clustering them and performing feature extraction directly on the point cloud clusters. This approach achieves state-of-the-art performance on the nuScenes dataset, demonstrating the effectiveness of spatial feature extraction in radar-camera fusion.

Finally, \[[9](http://arxiv.org/abs/2307.10249)\] introduces MVFusion, a novel Multi-View radar-camera fusion method that achieves semantic-aligned radar features and enhances cross-modal information interaction. This method uses a semantic-aligned radar encoder and a radar-guided fusion transformer to strengthen the correlation between radar and image features.

References  
\[[1](http://arxiv.org/abs/2307.15264)\] http://arxiv.org/abs/2307.15264  
\[[2](http://arxiv.org/abs/2309.00787)\] http://arxiv.org/abs/2309.00787  
\[[3](http://arxiv.org/abs/2211.01871)\] http://arxiv.org/abs/2211.01871  
\[[4](http://arxiv.org/abs/2103.07505)\] http://arxiv.org/abs/2103.07505  
\[[5](http://arxiv.org/abs/1904.08743)\] http://arxiv.org/abs/1904.08743  
\[[6](http://arxiv.org/abs/2309.15465)\] http://arxiv.org/abs/2309.15465  
\[[7](http://arxiv.org/abs/2305.15883)\] http://arxiv.org/abs/2307.10249  
\[[8](http://arxiv.org/abs/2304.10410)\] http://arxiv.org/abs/2309.03734  
\[[9](http://arxiv.org/abs/2307.10249)\] http://arxiv.org/abs/2302.10511
