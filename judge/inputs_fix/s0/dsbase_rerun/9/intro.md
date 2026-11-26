## Related Works

Quantitative susceptibility mapping (QSM) has emerged as a powerful tool for characterizing tissue properties in magnetic resonance imaging (MRI), particularly in the context of multiple sclerosis (MS). QSM provides high-contrast images that distinguish between different lesion types, such as "rim" lesions and "non-rim" lesions, which are critical for monitoring disease progression \[[16' 2022-11-09](http://arxiv.org/abs/2211.04764v1)\]. However, the rarity of paramagnetic rim lesions (PRLs) poses significant challenges for segmentation and classification due to class imbalance \[[16' 2022-11-09](http://arxiv.org/abs/2211.04764v1)\]. Several studies have explored deep learning-based approaches to address these challenges.

Early work on QSM focused on traditional methods such as dipole inversion and regularization techniques to handle the ill-posed nature of the field-to-source problem \[[16' 2022-11-09](http://arxiv.org/abs/2211.04764v1)\]. More recently, deep learning methods have been introduced to improve the accuracy and robustness of QSM. For example, QSMnet was developed to generate high-quality susceptibility maps from single orientation data, outperforming conventional methods like TKD and MEDI in terms of image quality and consistency across orientations \[[9' 2018-03-15](http://arxiv.org/abs/1803.05627v2)\]. Similarly, the use of probabilistic dipole inversion (PDI) has been proposed to estimate susceptibility maps with uncertainty quantification, enhancing the reliability of QSM in clinical settings \[[13' 2020-09-07](http://arxiv.org/abs/2009.04251v6)\].

The challenge of class imbalance in PRL segmentation has also been addressed through synthetic data generation. Generative adversarial networks (GANs) have been used to synthesize quantitative susceptibility maps, allowing for the augmentation of minority class samples \[[28' 2021-05-04](http://arxiv.org/abs/2105.01800v1)\]. This approach has been applied to improve classifier performance and enable more robust segmentation of rare lesion types. Additionally, the use of denoising techniques, such as noise propagation and MP-PCA, has been explored to enhance the quality of QSM maps and reduce artifacts caused by low signal-to-noise ratios \[[14' 2024-04-30](http://arxiv.org/abs/2404.19309v1)\].

In the context of MS lesion segmentation, several deep learning architectures have been proposed to improve the accuracy of lesion detection and segmentation. For example, the use of multi-branch convolutional neural networks (CNNs) has enabled the integration of information from multiple modalities, leading to improved segmentation performance \[[3' 2018-11-07](http://arxiv.org/abs/1811.02942v4)\]. Similarly, the development of recurrent slice-wise attention networks (RSANet) has demonstrated the ability to capture long-range dependencies in 3D MRI data, resulting in better lesion segmentation \[[8' 2020-02-27](http://arxiv.org/abs/2002.12470v1)\]. These methods have been evaluated on various benchmark datasets, including the ISBI 2015 challenge dataset and private datasets, showing significant improvements over traditional approaches \[[3' 2018-11-07](http://arxiv.org/abs/1811.02942v4)\]\[[8' 2020-02-27](http://arxiv.org/abs/2002.12470v1)\].

Moreover, the integration of uncertainty estimation in deep learning models has been explored to improve the reliability of lesion segmentation in clinical settings. Techniques such as Monte Carlo dropout have been used to generate uncertainty maps, allowing clinicians to assess the confidence of segmentation results \[[11' 2018-08-03](http://arxiv.org/abs/1808.01200v2)\]. This is particularly important for rare lesion types like PRLs, where the model's confidence can significantly impact diagnostic decisions.

In summary, the field of QSM and MS lesion segmentation has seen significant advancements through the integration of deep learning techniques, synthetic data generation, and uncertainty estimation. These approaches have addressed key challenges such as class imbalance, low signal-to-noise ratios, and the need for robust and reliable segmentation in clinical settings.

References  
\[[1' 2023-04-21](http://arxiv.org/abs/2304.10790v1)\] http://arxiv.org/abs/2304.10790v1  
\[[2' 2018-03-24](http://arxiv.org/abs/1803.09172v1)\] http://arxiv.org/abs/1803.09172v1  
\[[3' 2018-11-07](http://arxiv.org/abs/1811.02942v4)\] http://arxiv.org/abs/1811.02942v4  
\[[4' 2024-10-25](http://arxiv.org/abs/2410.19623v1)\] http://arxiv.org/abs/2410.19623v1  
\[[5' 2024-10-10](http://arxiv.org/abs/2410.07924v1)\] http://arxiv.org/abs/2410.07924v1  
\[[6' 2023-07-10](http://arxiv.org/abs/2307.04513v2)\] http://arxiv.org/abs/2307.04513v2  
\[[7' 2020-09-29](http://arxiv.org/abs/2009.13755v1)\] http://arxiv.org/abs/2009.13755v1  
\[[8' 2020-02-27](http://arxiv.org/abs/2002.12470v1)\] http://arxiv.org/abs/2002.12470v1  
\[[9' 2018-03-15](http://arxiv.org/abs/1803.05627v2)\] http://arxiv.org/abs/1803.05627v2  
\[[10' 2024-07-23](http://arxiv.org/abs/2407.16477v2)\] http://arxiv.org/abs/2407.16477v2  
\[[11' 2018-08-03](http://arxiv.org/abs/1808.01200v2)\] http://arxiv.org/abs/1808.01200v2  
\[[12' 2021-04-23](http://arxiv.org/abs/2104.11797v1)\] http://arxiv.org/abs/2104.11797v1  
\[[13' 2020-09-07](http://arxiv.org/abs/2009.04251v6)\] http://arxiv.org/abs/2009.04251v6  
\[[14' 2024-04-30](http://arxiv.org/abs/2404.19309v1)\] http://arxiv.org/abs/2404.19309v1  
\[[15' 2022-07-29](http://arxiv.org/abs/2207.14709v3)\] http://arxiv.org/abs/2207.14709v3  
\[[16' 2022-11-09](http://arxiv.org/abs/2211.04764v1)\] http://arxiv.org/abs/2211.04764v1
