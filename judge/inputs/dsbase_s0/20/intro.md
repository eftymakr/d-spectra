## Related Works

Single-pixel imaging (SPI) has attracted significant attention due to its ability to capture images with a single-pixel detector using structured illumination patterns . Early methods relied on random patterns for measurement, but these often resulted in high sampling rates and poor reconstruction quality . To address these challenges, various approaches have been proposed, including the use of deterministic patterns such as Hadamard and Fourier masks . These deterministic patterns offer better control over the imaging process and can lead to improved reconstruction performance .

Deep-unrolling and plug-and-play (PnP) approaches have emerged as dominant solvers for SPI inverse problems \[[Olivier Leblanc' 2023-06-22](http://arxiv.org/abs/2306.12698v3)\]. PnP methods integrate off-the-shelf deep denoisers into iterative optimization schemes, offering flexibility in handling varying compression ratios (CRs) \[[Olivier Leblanc' 2023-06-22](http://arxiv.org/abs/2306.12698v3)\]. However, they often suffer from limitations in reconstruction accuracy and speed \[[Olivier Leblanc' 2023-06-22](http://arxiv.org/abs/2306.12698v3)\]. On the other hand, unrolling approaches transform truncated iterative optimization processes into end-to-end trainable networks, typically achieving better accuracy and faster inference \[[Olivier Leblanc' 2023-06-22](http://arxiv.org/abs/2306.12698v3)\]. Yet, these methods require fine-tuning or retraining when CR changes, limiting their adaptability \[[Olivier Leblanc' 2023-06-22](http://arxiv.org/abs/2306.12698v3)\].

Several studies have explored the integration of deep learning with traditional iterative algorithms for SPI. For example, the work by  proposed a single-pixel imaging method based on origami pattern construction, which reduces the sampling ratio and improves imaging quality. Similarly,  demonstrated Fourier single-pixel imaging in the terahertz regime, achieving high-quality image reconstruction with fewer measurements. These methods highlight the potential of combining structured illumination with deep learning for improved performance.

The use of deep learning for SPI has also been extended to other domains, such as medical imaging and computational photography. For instance,  introduced a deep convolutional neural network for automatic landmark correspondence detection in medical images, enhancing deformable image registration. Additionally,  proposed complementary Fourier single-pixel imaging (CFSI), which reduces measurements while retaining robustness, offering a balance between efficiency and quality .

In the context of unrolling approaches,  proposed a convergent unrolling technique for image deconvolution, ensuring the network retains the convergence properties of the underlying iterative algorithm. This approach was validated through extensive experiments on benchmark datasets, demonstrating competitive performance compared to state-of-the-art unrolling methods . Similarly,  introduced JotlasNet, a deep unrolling network for dynamic MRI reconstruction that jointly utilizes tensor low-rank and attention-based sparse priors, achieving superior performance on multiple datasets .

The integration of deep learning with iterative algorithms has also been explored in other imaging modalities, such as holographic microscopy  and electron microscopy . These studies demonstrate the versatility of deep unrolling and PnP approaches in addressing diverse imaging challenges .

In summary, the field of single-pixel imaging has seen significant advancements through the integration of deep learning with traditional iterative algorithms. While PnP methods offer flexibility, unrolling approaches provide better accuracy and speed. The proposed work aims to combine the strengths of both classes of solvers, offering a flexible and efficient solution for SPI \[[Olivier Leblanc' 2023-06-22](http://arxiv.org/abs/2306.12698v3)\].

References:
1. \[[Olivier Leblanc' 2023-06-22](http://arxiv.org/abs/2306.12698v3)\] Document 6: Hadamard single-pixel imaging versus Fourier single-pixel imaging
2.  Document 63: Single-pixel imaging with origami pattern construction
3.  Document 65: Fourier single-pixel imaging in the terahertz regime
4.  Document 57: Automatic Landmarks Correspondence Detection in Medical Images with an Application to Deformable Image Registration
5.  Document 61: Complementary Fourier single-pixel imaging
6.  Document 48: Deep, convergent, unrolled half-quadratic splitting for image deconvolution
7.  Document 55: JotlasNet: Joint Tensor Low-Rank and Attention-based Sparse Unrolling Network for Accelerating Dynamic MRI
8.  Document 64: Single-Pixel Imaging Technology in Holographic Microscopy
9.  Document 68: Single-Pixel Imaging in Space and Time with Optically-Modulated Free Electrons
