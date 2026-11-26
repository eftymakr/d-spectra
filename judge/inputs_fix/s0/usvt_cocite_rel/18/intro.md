## Related Works

Anomaly detection in industrial settings has garnered significant attention due to its critical role in quality control and system reliability. Early approaches relied on rule-based methods and statistical models, which were limited in their ability to generalize across complex, dynamic environments \[[1](http://arxiv.org/abs/2012.03586)\]. With the advent of deep learning, numerous methods have been proposed to improve detection accuracy and adaptability. 

One line of research focuses on process-based anomaly detection for Industrial Control Systems (ICSs). A systematic analysis of such schemes revealed that many are vulnerable to adversarial spoofing attacks, which can reduce recall and compromise detection reliability \[[1](http://arxiv.org/abs/2012.03586)\]. This highlights the need for more robust models that can learn and enforce physical properties of the system \[[1](http://arxiv.org/abs/2012.03586)\]. 

Unsupervised anomaly detection has also been extensively explored, particularly for 3D data. The MVTec 3D-AD dataset was introduced to evaluate models for detecting geometric anomalies in manufactured products \[[2](http://arxiv.org/abs/2112.09045)\]. This dataset includes precise ground-truth annotations, enabling rigorous evaluation of detection and localization performance \[[2](http://arxiv.org/abs/2112.09045)\]. Similarly, the MVTec AD dataset has been widely used to benchmark methods for image-based anomaly detection \[[3](http://arxiv.org/abs/2106.08265)\]. 

To address the cold-start problem in industrial anomaly detection, where models are trained only on normal data, PatchCore was proposed. This method uses a memory bank of representative patch features to achieve state-of-the-art performance on the MVTec AD benchmark, with an AUROC score of 99.6% \[[3](http://arxiv.org/abs/2106.08265)\]. Another approach, CFLOW-AD, introduces a real-time model based on conditional normalizing flows, achieving faster inference times and better localization performance than prior methods \[[4](http://arxiv.org/abs/2107.12571)\]. 

For time-series data, LSTM-based encoder-decoder models have shown robustness in detecting anomalies from both predictable and unpredictable time-series \[[7](http://arxiv.org/abs/1607.00148)\]. Similarly, MAD-GAN leverages Generative Adversarial Networks (GANs) to capture spatial-temporal correlations in multivariate time series, improving detection accuracy on real-world datasets like SWaT and WADI \[[13](http://arxiv.org/abs/1901.04997)\]. 

Recent advances in anomaly detection have also focused on localization. PaDiM introduces a patch distribution modeling framework that outperforms existing methods on both detection and localization tasks \[[6](http://arxiv.org/abs/2011.08785)\]. DRÆM, another recent approach, treats anomaly detection as a discriminative problem, achieving superior performance on the MVTec dataset \[[8](http://arxiv.org/abs/2108.07610)\]. 

Additionally, methods such as FastFlow and RIAD have been proposed to improve the efficiency and accuracy of anomaly detection by leveraging normalizing flows and inpainting techniques \[[10](http://arxiv.org/abs/2111.07677)\]\[[12](https://www.semanticscholar.org/paper/2c89b183df320c3ef698989bdc5d1d4731c4d65d)\]. These approaches aim to address limitations of traditional auto-encoders, which often fail to distinguish between normal and anomalous regions due to their ability to reconstruct anomalies \[[12](https://www.semanticscholar.org/paper/2c89b183df320c3ef698989bdc5d1d4731c4d65d)\].

In summary, while many existing methods show promising performance, they often suffer from high computational demands or limited generalization capabilities. Recent works such as PatchCore, CFLOW-AD, and MAD-GAN have made strides in improving efficiency and accuracy, particularly for resource-constrained environments \[[3](http://arxiv.org/abs/2106.08265)\]\[[4](http://arxiv.org/abs/2107.12571)\]\[[13](http://arxiv.org/abs/1901.04997)\].

References:  
\[[1](http://arxiv.org/abs/2012.03586)\] No Need to Know Physics: Resilience of Process-based Model-free Anomaly Detection for Industrial Control Systems [http://arxiv.org/abs/2012.03586]  
\[[2](http://arxiv.org/abs/2112.09045)\] The MVTec 3D-AD Dataset for Unsupervised 3D Anomaly Detection and Localization [http://arxiv.org/abs/2112.09045]  
\[[3](http://arxiv.org/abs/2106.08265)\] Towards Total Recall in Industrial Anomaly Detection [http://arxiv.org/abs/2106.08265]  
\[[4](http://arxiv.org/abs/2107.12571)\] CFLOW-AD: Real-Time Unsupervised Anomaly Detection with Localization via Conditional Normalizing Flows [http://arxiv.org/abs/2107.12571]  
\[[6](http://arxiv.org/abs/2011.08785)\] PaDiM: a Patch Distribution Modeling Framework for Anomaly Detection and Localization [http://arxiv.org/abs/2011.08785]  
\[[7](http://arxiv.org/abs/1607.00148)\] LSTM-based Encoder-Decoder for Multi-sensor Anomaly Detection [http://arxiv.org/abs/1607.00148]  
\[[8](http://arxiv.org/abs/2108.07610)\] DRÆM – A discriminatively trained reconstruction embedding for surface anomaly detection [http://arxiv.org/abs/2108.07610]  
\[[10](http://arxiv.org/abs/2111.07677)\] FastFlow: Unsupervised Anomaly Detection and Localization via 2D Normalizing Flows [http://arxiv.org/abs/2111.07677]  
\[[12](https://www.semanticscholar.org/paper/2c89b183df320c3ef698989bdc5d1d4731c4d65d)\] Reconstruction by inpainting for visual anomaly detection [https://www.semanticscholar.org/paper/2c89b183df320c3ef698989bdc5d1d4731c4d65d]  
\[[13](http://arxiv.org/abs/1901.04997)\] MAD-GAN: Multivariate Anomaly Detection for Time Series Data with Generative Adversarial Networks [http://arxiv.org/abs/1901.04997]
