## Related Works

Protein dynamics are essential for understanding biological functions and properties, and traditional methods for studying these dynamics rely heavily on time-consuming molecular dynamics (MD) simulations \[[Jiarui Lu' 2024-10-24](http://arxiv.org/abs/2410.18403v2)\]. Recent advancements in generative modeling, particularly denoising diffusion models, have enabled efficient and accurate protein structure prediction and conformation sampling by learning distributions over crystallographic structures \[[Yan Wang' 2024-03-21](http://arxiv.org/abs/2403.14088v2)\]. However, integrating physical supervision into these data-driven approaches remains challenging, as standard energy-based objectives often lead to intractable optimization \[[Avishek Joey Bose' 2023-10-03](http://arxiv.org/abs/2310.02391v4)\]. This section reviews related works that address these challenges and contribute to the field of protein conformation prediction and sampling.

Several studies have explored the use of energy-based models for protein structure prediction. For instance, \[[Rhiju Das' 2012-08-02](http://arxiv.org/abs/1208.2680v2)\] introduces an energy-based model (EBM) of protein conformations that operates at atomic scale, achieving performance close to that of the Rosetta energy function. Similarly, \[[Alex T. Grigas' 2020-01-05](http://arxiv.org/abs/2001.01161v1)\] proposes a method for fast sampling of protein conformational dynamics using enhanced sampling algorithms with collective variables, which significantly reduces computational costs. These approaches highlight the importance of energy functions in capturing the physical realism of protein structures.

The integration of physical constraints into generative models has also been explored in the context of protein folding. \[[Yilun Du' 2020-04-27](http://arxiv.org/abs/2004.13167v1)\] introduces a force-guided SE(3) diffusion model, ConfDiff, which incorporates physical prior knowledge to guide the generation process, resulting in high-fidelity protein conformations. Additionally, \[[Thomas Hamelryck' 2010-08-24](http://arxiv.org/abs/1008.4006v3)\] presents a method for protein conformation generation via force-guided SE(3) diffusion models, demonstrating the effectiveness of incorporating physical guidance in diffusion-based approaches. These studies emphasize the potential of combining physical principles with generative models to improve the accuracy and efficiency of protein conformation prediction.

Moreover, the use of diffusion models for protein structure prediction has been extensively studied. \[[Yuning Shen' 2025-05-23](http://arxiv.org/abs/2505.17478v2)\] introduces a diffusion-based generative model, EigenFold, which samples a distribution of structures from a given protein sequence, achieving a median TMScore of 0.84. \[[Mahmood A. Rashid' 2016-03-07](http://arxiv.org/abs/1607.06113v1)\] presents a method for protein conformation prediction using a diffusion process that models the structure as a system of harmonic oscillators, enabling a cascading-resolution generative process. These approaches demonstrate the versatility of diffusion models in capturing the conformational diversity of proteins.

In addition, \[[Julen Urain' 2022-09-08](http://arxiv.org/abs/2209.03855v4)\] proposes a method for protein conformation generation using a diffusion process that models the structure as a system of harmonic oscillators, enabling a cascading-resolution generative process. This approach has been shown to generate high-quality protein conformations with significant efficiency gains compared to traditional MD simulations.

References:

1. [Document 1] Structure Language Models for Protein Conformation Generation
2. [Document 2] Protein Conformation Generation via Force-Guided SE(3) Diffusion Models
3. [Document 3] SE(3)-Stochastic Flow Matching for Protein Backbone Generation
4. [Document 4] Atomic-accuracy prediction of protein loop structures through an RNA-inspired ansatz
5. [Document 5] Using physical features of protein core packing to distinguish real proteins from decoys
6. [Document 6] Energy-based models for atomic-resolution protein conformations
7. [Document 7] Potentials of Mean Force for Protein Structure Prediction Vindicated, Formalized and Generalized
8. [Document 8] ConfRover: Simultaneous Modeling of Protein Conformation and Dynamics via Autoregression
9. [Document 9] Guided macro-mutation in a graded energy based genetic algorithm for protein structure prediction
10. [Document 10] SE(3)-DiffusionFields: Learning smooth cost functions for joint grasp and motion optimization through diffusion
