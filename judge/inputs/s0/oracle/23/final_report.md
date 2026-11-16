## Related Works

Extrinsic calibration between radar and camera systems has been a challenging task due to the inherent sparsity and uncertainty in radar data. Early methods often relied on manual calibration targets or required extensive data collection \[[1](http://arxiv.org/abs/1707.03167)\]. For instance, classical approaches typically involve feature extraction, feature matching, and global regression, which are time-consuming and require human intervention \[[1](http://arxiv.org/abs/1707.03167)\]. Recent efforts have aimed to automate this process, particularly for LiDAR and camera systems, with methods such as RegNet \[[1](http://arxiv.org/abs/1707.03167)\], which integrates all three calibration steps into a single CNN, and CalibNet \[[2](http://arxiv.org/abs/1803.08181)\], which uses self-supervised learning to estimate the 6-DoF transformation without calibration targets. These methods have demonstrated significant improvements in accuracy and efficiency, reducing the need for manual calibration and enabling real-time operation.

However, the integration of radar and camera remains less explored. A notable work is the Targetless Rotational Auto-Calibration of Radar and Camera for Intelligent Transportation Systems \[[4](http://arxiv.org/abs/1904.08743)\], which introduces a coarse and fine CNN approach to address the challenge of automatic calibration without dedicated targets. This method leverages a boosting-inspired training algorithm to refine the calibration process iteratively. Similarly, the Continuous-Time Approach for 3D Radar-to-Camera Extrinsic Calibration \[[5](http://arxiv.org/abs/2103.07505)\] proposes a method that utilizes radar velocity measurements and does not require specialized radar retroreflectors, making it suitable for real-world deployment.

The spatiotemporal calibration of 3D millimetre-wavelength radar-camera pairs \[[6](http://arxiv.org/abs/2211.01871)\] further extends the calibration problem by considering both spatial and temporal misalignments, which are critical for long-term reliable operation of autonomous vehicles. This work highlights the importance of in-situ calibration and the necessity of infrastructure-free solutions. Additionally, LCCNet \[[3](http://arxiv.org/abs/2012.13901)\] presents a novel online self-calibration approach for LiDAR and camera, using a cost volume network for feature matching and an additional point cloud loss to improve calibration accuracy.

The proposed method in this paper addresses the specific challenges of radar-camera calibration by introducing a Dual-Perspective representation and a Selective Fusion Mechanism to mitigate the effects of height uncertainty. This is a significant advancement over existing methods, which often struggle with the sparsity and measurement uncertainty in radar data \[[1](http://arxiv.org/abs/1707.03167)\]\[[2](http://arxiv.org/abs/1803.08181)\]\[[3](http://arxiv.org/abs/2012.13901)\]\[[4](http://arxiv.org/abs/1904.08743)\]\[[5](http://arxiv.org/abs/2103.07505)\]\[[6](http://arxiv.org/abs/2211.01871)\].

Further details on the challenges of radar-camera calibration \[[7]()\], the use of radar and vision sensor fusion for object detection \[[8]()\], and the survey on automatic targetless LiDAR-camera calibration \[[9]()\] provide additional context for the importance of this research. The method of automatic
## Research papers
### Outline
- [Extrinsic Calibration Frameworks [3 papers]](#category-extrinsic-calibration-frameworks)
- [LiDAR-Camera Calibration Techniques [3 papers]](#category-lidar-camera-calibration-techniques)
- [Online Self-Calibration Techniques [2 papers]](#category-online-self-calibration-techniques)
- [Radar-Camera Calibration Approaches [3 papers]](#category-radar-camera-calibration-approaches)
- [Sensor Fusion for Object Detection [2 papers]](#category-sensor-fusion-for-object-detection)

### <a id='category-extrinsic-calibration-frameworks'></a>Extrinsic Calibration Frameworks: 3 papers found.
Context: 
	Document 1: [Snippet]: «In this paper, we present RegNet, the first deep convolutional neural network
(CNN) to infer a 6 degrees of freedom (DOF) extrinsic calibration between
multimodal sensors, exemplified using a scanning LiDAR and a monocular camera.
Compared to existing approaches, RegNet casts all three conventional
calibration steps (feature extraction, feature matching and global regression)
into a single real-time capable CNN. Our method does not require any human
interaction and bridges the gap between classical offline and target-less
online calibration approaches as it provides both a stable initial estimation
as well as a continuous online correction of the extrinsic parameters. During
training we randomly decalibrate our system in order to train RegNet to infer
the correspondence between projected depth measurements and RGB image and
finally regress the extrinsic calibration. Additionally, with an iterative
execution of multiple CNNs, that are trained on different magnitudes of
decalibration, our approach compares favorably to state-of-the-art methods in
terms of a mean calibration error of 0.28 degrees for the rotational and 6 cm
for the translation components even for large decalibrations up to 1.5 m and 20
degrees.»
[Category]: «Extrinsic Calibration Frameworks»
[_citation_number]: «1»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-28T14:52:31+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2012.13901)\]. Further details \[[6](http://arxiv.org/abs/2211.01871)\]\[[7]()\]\[[8]()\]\[[9]()\]\[[10]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: This paper presents a groundbreaking approach - the first online automatic
geometric calibration method for radar and camera systems. Given the
significant data sparsity and measurement uncertainty in radar
|    | reference                                                                                                |   date | key idea/summary                                                                                                                                                                                                                         |
|----|----------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [RegNet: Multimodal Sensor Registration Using Deep Neural Networks](http://arxiv.org/abs/1707.03167)     |    nan | RegNet is the first deep convolutional neural network to perform real-time 6 DOF extrinsic calibration between multimodal sensors, integrating feature extraction, matching, and regression into a single CNN without human interaction. |
|  1 | [Automatic targetless extrinsic calibration of a 3d lidar and camera by maximizing mutual information]() |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                |
|  2 | [Motion-based calibration of multimodal sensor arrays]()                                                 |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                |
### <a id='category-lidar-camera-calibration-techniques'></a>LiDAR-Camera Calibration Techniques: 3 papers found.
Context: 
	Document 1: [Snippet]: «3D LiDARs and 2D cameras are increasingly being used alongside each other in sensor rigs for perception tasks. Before these sensors can be used to gather meaningful data, however, their extrinsics (and intrinsics) need to be accurately calibrated, as the performance of the sensor rig is extremely sensitive to these calibration parameters. A vast majority of existing calibration techniques require significant amounts of data and/or calibration targets and human effort, severely impacting their applicability in large-scale production systems. We address this gap with CalibNet: a self-supervised deep network capable of automatically estimating the 6-DoF rigid body transformation between a 3D LiDAR and a 2D camera in real-time. CalibNet alleviates the need for calibration targets, thereby resulting in significant savings in calibration efforts. During training, the network only takes as input a LiDAR point cloud, the corresponding monocular image, and the camera calibration matrix K. At train time, we do not impose direct supervision (i.e., we do not directly regress to the calibration parameters, for example). Instead, we train the network to predict calibration parameters that maximize the geometric and photometric consistency of the input images and point clouds. CalibNet learns to iteratively solve the underlying geometric problem and accurately predicts extrinsic calibration parameters for a wide range of mis-calibrations, without requiring retraining or domain adaptation. The project page is hosted at https://epiception.github.io/CalibNet»
[Category]: «LiDAR-Camera Calibration Techniques»
[_citation_number]: «2»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-28T14:52:31+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2012.13901)\]. Further details \[[6](http://arxiv.org/abs/2211.01871)\]\[[7]()\]\[[8]()\]\[[9]()\]\[[10]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words
|    | reference                                                                                                                           |   date | key idea/summary                                                                                                                                                                                                                 |
|----|-------------------------------------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [CalibNet: Geometrically Supervised Extrinsic Calibration using 3D
  Spatial Transformer Networks](http://arxiv.org/abs/1803.08181) |    nan | CalibNet is a self-supervised deep learning approach that automatically estimates the 6-DoF transformation between a 3D LiDAR and a 2D camera without requiring calibration targets, significantly reducing calibration efforts. |
|  1 | [Automatic targetless LiDAR--camera calibration: a survey]()                                                                        |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                        |
|  2 | [Calibrcnn: Calibrating camera and lidar by recurrent convolutional neural network and geometric constraints]()                     |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                        |
### <a id='category-online-self-calibration-techniques'></a>Online Self-Calibration Techniques: 2 papers found.
Context: 
	Document 1: [Snippet]: «In this paper, we propose a novel online self-calibration approach for Light Detection and Ranging (LiDAR) and camera sensors. Compared to the previous CNN-based methods that concatenate the feature maps of the RGB image and decalibrated depth image, we exploit the cost volume inspired by the PWC-Net for feature matching. Besides the smooth L1-Loss of the predicted extrinsic calibration parameters, an additional point cloud loss is applied. Instead of regress the extrinsic parameters between LiDAR and camera directly, we predict the decalibrated deviation from initial calibration to the ground truth. During inference, the calibration error decreases further with the usage of iterative refinement and the temporal filtering approach. The evaluation results on the KITTI dataset illustrate that our approach outperforms CNN-based state-of-the-art methods in terms of a mean absolute calibration error of 0.297cm in translation and 0.017(\deg) in rotation with miscalibration magnitudes of up to 1.5m and 20(\deg).»
[Category]: «Online Self-Calibration Techniques»
[_citation_number]: «3»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-28T14:52:31+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2012.13901)\]. Further details \[[6](http://arxiv.org/abs/2211.01871)\]\[[7]()\]\[[8]()\]\[[9]()\]\[[10]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: This paper presents a groundbreaking approach - the first online automatic geometric calibration method for radar and camera systems. Given the significant data sparsity and measurement uncertainty in radar height data, achieving automatic calibration during system operation has long been a challenge. To address the sparsity issue, we propose a Dual-Perspective representation that gathers features from both frontal and bird's-eye views. The frontal view contains
|    | reference                                                                                              |   date | key idea/summary                                                                                                                                                                                       |
|----|--------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [LCCNet: LiDAR and Camera Self-Calibration using Cost Volume Network](http://arxiv.org/abs/2012.13901) |    nan | This paper proposes a novel online self-calibration approach for LiDAR and camera sensors, using a cost volume inspired by PWC-Net and an additional point cloud loss to improve calibration accuracy. |
|  1 | [Online multi-sensor calibration based on moving object tracking]()                                    |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                              |
### <a id='category-radar-camera-calibration-approaches'></a>Radar-Camera Calibration Approaches: 3 papers found.
Context: 
	Document 1: [Snippet]: «Most intelligent transportation systems use a combination of radar sensors and cameras for robust vehicle perception. The calibration of these heterogeneous sensor types in an automatic fashion during system operation is challenging due to differing physical measurement principles and the high sparsity of traffic radars. We propose - to the best of our knowledge - the first data-driven method for automatic rotational radar-camera calibration without dedicated calibration targets. Our approach is based on a coarse and a fine convolutional neural network. We employ a boosting-inspired training algorithm, where we train the fine network on the residual error of the coarse network. Due to the unavailability of public datasets combining radar and camera measurements, we recorded our own real-world data. We demonstrate that our method is able to reach precise and robust sensor registration and show its generalization capabilities to different sensor alignments and perspectives.»
[Category]: «Radar-Camera Calibration Approaches»
[_citation_number]: «4»

	Document 2: [Snippet]: «Reliable operation in inclement weather is essential to the deployment of safe autonomous vehicles (AVs). Robustness and reliability can be achieved by fusing data from the standard AV sensor suite (i.e., lidars, cameras) with weather robust sensors, such as millimetre-wavelength radar. Critically, accurate sensor data fusion requires knowledge of the rigid-body transform between sensor pairs, which can be determined through the process of extrinsic calibration. A number of extrinsic calibration algorithms have been designed for 2D (planar) radar sensors - however, recently-developed, low-cost 3D millimetre-wavelength radars are set to displace their 2D counterparts in many applications. In this paper, we present a continuous-time 3D radar-to-camera extrinsic calibration algorithm that utilizes radar velocity measurements and, unlike the majority of existing techniques, does not require specialized radar retroreflectors to be present in the environment. We derive the observability properties of our formulation and demonstrate the efficacy of our algorithm through synthetic and real-world experiments.»
[Category]: «Radar-Camera Calibration Approaches»
[_citation_number]: «5»

	Document 3: [Snippet]: «Autonomous vehicles (AVs) fuse data from multiple sensors and sensing modalities to impart a measure of robustness when operating in adverse conditions. Radars and cameras are popular choices for use in sensor fusion; although radar measurements are sparse in comparison to camera images, radar scans penetrate fog, rain, and snow. However
|    | reference                                                                                                                              |   date | key idea/summary                                                                                                                                                                                                                    |
|----|----------------------------------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Targetless Rotational Auto-Calibration of Radar and Camera for
  Intelligent Transportation Systems](http://arxiv.org/abs/1904.08743) |    nan | The paper introduces a data-driven method for automatic rotational radar-camera calibration without dedicated calibration targets, using a coarse and fine convolutional neural network trained with a boosting-inspired algorithm. |
|  1 | [A Continuous-Time Approach for 3D Radar-to-Camera Extrinsic Calibration](http://arxiv.org/abs/2103.07505)                             |    nan | This paper introduces a continuous-time 3D radar-to-camera extrinsic calibration algorithm that does not require specialized radar retroreflectors, enhancing the reliability of autonomous vehicles in inclement weather.          |
|  2 | [Spatiotemporal Calibration of 3D Millimetre-Wavelength Radar-Camera
  Pairs](http://arxiv.org/abs/2211.01871)                         |    nan | This paper presents a targetless spatiotemporal calibration algorithm for autonomous vehicles that leverages radar's ability to measure ego-velocity, enabling accurate calibration without specialized infrastructure.             |
### <a id='category-sensor-fusion-for-object-detection'></a>Sensor Fusion for Object Detection: 2 papers found.
Context: 
	Document 1: [Snippet]: «»
[Category]: «Sensor Fusion for Object Detection»
[_citation_number]: «7»

	Document 2: [Snippet]: «»
[Category]: «Sensor Fusion for Object Detection»
[_citation_number]: «8»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-28T14:52:31+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2012.13901)\]. Further details \[[6](http://arxiv.org/abs/2211.01871)\]\[[7]()\]\[[8]()\]\[[9]()\]\[[10]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: This paper presents a groundbreaking approach - the first online automatic
geometric calibration method for radar and camera systems. Given the
significant data sparsity and measurement uncertainty in radar height data,
achieving automatic calibration during system operation has long been a
challenge. To address the sparsity issue, we propose a Dual-Perspective
representation that gathers features from both frontal and bird's-eye views.
The frontal view contains rich but sensitive height information, whereas the
bird's-eye view provides robust features against height uncertainty. We thereby
propose a novel Selective Fusion Mechanism to identify and fuse reliable
features from both perspectives, reducing the effect of height uncertainty.
Moreover, for each view, we incorporate a Multi-Modal Cross-Attention Mechanism
to explicitly find location correspondences through cross-modal matching.
During the training phase, we also design a Noise-Resistant Matcher to provide
better supervision and enhance the robustness of the matching mechanism against
sparsity and height uncertainty. Our experimental results, tested on the
nuScenes dataset, demonstrate that our method significantly outperforms
previous radar-camera auto-calibration methods, as well as existing
state-of-the-art LiDAR-camera calibration techniques, establishing a new
benchmark for future research. The code is available at
https://github
|    | reference                                                                                  |   date | key idea/summary                                                                                          |
|----|--------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------|
|  0 | [Obstacle detection using millimeter-wave radar and its visualization on image sequence]() |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
|  1 | [Radar and vision sensor fusion for object detection in autonomous vehicle surroundings]() |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
