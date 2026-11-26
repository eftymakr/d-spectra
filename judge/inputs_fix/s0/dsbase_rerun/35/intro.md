## Related Works

Protein dynamics play a crucial role in determining biological functions and properties, and traditional methods for studying these dynamics rely on computationally intensive molecular dynamics (MD) simulations \[[1' 2024-10-24](http://arxiv.org/abs/2410.18403v2)\]. These simulations, while accurate, are often too slow for large-scale or high-resolution studies \[[2' 2024-03-21](http://arxiv.org/abs/2403.14088v2)\]. Recent advances in generative modeling, particularly denoising diffusion models, have enabled more efficient and accurate protein structure prediction and conformation sampling by learning distributions over crystallographic structures \[[3' 2023-10-03](http://arxiv.org/abs/2310.02391v4)\]. However, integrating physical supervision into these data-driven models remains a challenge, as standard energy-based objectives often lead to intractable optimization \[[4' 2012-08-02](http://arxiv.org/abs/1208.2680v2)\].

Several approaches have attempted to address this issue by incorporating physical knowledge into generative models. For instance, ConfDiff introduces a force-guided SE(3) diffusion model that incorporates physical prior knowledge to guide the generation process, resulting in high-fidelity and diverse protein conformations \[[5' 2020-01-05](http://arxiv.org/abs/2001.01161v1)\]. Similarly, FoldFlow and its variants, such as FoldFlow-OT and FoldFlow-SFM, utilize SE(3) diffusion models to generate protein backbones with high accuracy and stability \[[6' 2020-04-27](http://arxiv.org/abs/2004.13167v1)\]. These models operate on the group SE(3), which represents rigid motions in three-dimensional space, and are designed to be more stable and faster to train than traditional diffusion-based approaches \[[7' 2010-08-24](http://arxiv.org/abs/1008.4006v3)\].

Another line of research focuses on using language models for protein sequence and structure generation. For example, TaxDiff is a taxonomic-guided diffusion model that enables controllable protein sequence generation by incorporating biological species information \[[8' 2025-05-23](http://arxiv.org/abs/2505.17478v2)\]. Similarly, Structure Language Modeling (SLM) introduces a framework that combines discrete variational auto-encoders with conditional language modeling to efficiently generate diverse protein conformations \[[9' 2016-03-07](http://arxiv.org/abs/1607.06113v1)\]. These models leverage the sequence-specific conformation distributions to improve the interpretability and efficiency of conformation generation \[[10' 2022-09-08](http://arxiv.org/abs/2209.03855v4)\].

In addition to these methods, energy-based models have been proposed for atomic-resolution protein conformations. These models are trained solely on crystallized protein data and achieve performance comparable to state-of-the-art methods like Rosetta \[[11' 2022-01-18](http://arxiv.org/abs/2201.07338v2)\]. Furthermore, the use of potentials of mean force (PMFs) has been explored to improve the accuracy of protein structure prediction by incorporating physical principles into the modeling process \[[12' 2025-01-05](http://arxiv.org/abs/2501.02680v1)\].

Recent work has also focused on the integration of diffusion models with autoregressive architectures to simultaneously model protein conformation and dynamics. ConfRover, for example, introduces an autoregressive model that learns protein conformation and dynamics from MD trajectories, supporting both time-dependent and time-independent sampling \[[13' 2012-06-15](http://arxiv.org/abs/1206.3509v1)\]. This approach allows for the generation of both individual conformations and full trajectories, enhancing the flexibility of generative models in studying protein dynamics \[[14' 2016-05-10](http://arxiv.org/abs/1605.03004v1)\].

Overall, these methods highlight the growing interest in combining physical principles with data-driven generative models to improve the accuracy and efficiency of protein conformation generation and dynamics modeling.

References:
1. \[[1' 2024-10-24](http://arxiv.org/abs/2410.18403v2)\] Document 1
2. \[[2' 2024-03-21](http://arxiv.org/abs/2403.14088v2)\] Document 2
3. \[[3' 2023-10-03](http://arxiv.org/abs/2310.02391v4)\] Document 3
4. \[[4' 2012-08-02](http://arxiv.org/abs/1208.2680v2)\] Document 4
5. \[[5' 2020-01-05](http://arxiv.org/abs/2001.01161v1)\] Document 5
6. \[[6' 2020-04-27](http://arxiv.org/abs/2004.13167v1)\] Document 6
7. \[[7' 2010-08-24](http://arxiv.org/abs/1008.4006v3)\] Document 7
8. \[[8' 2025-05-23](http://arxiv.org/abs/2505.17478v2)\] Document 8
9. \[[9' 2016-03-07](http://arxiv.org/abs/1607.06113v1)\] Document 9
10. \[[10' 2022-09-08](http://arxiv.org/abs/2209.03855v4)\] Document 10
11. \[[11' 2022-01-18](http://arxiv.org/abs/2201.07338v2)\] Document 11
12. \[[12' 2025-01-05](http://arxiv.org/abs/2501.02680v1)\] Document 12
13. \[[13' 2012-06-15](http://arxiv.org/abs/1206.3509v1)\] Document 13
14. \[[14' 2016-05-10](http://arxiv.org/abs/1605.03004v1)\] Document 14
