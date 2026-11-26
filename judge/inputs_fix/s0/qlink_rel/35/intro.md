## Related Works

Protein dynamics are essential for understanding biological functions and properties, yet traditional methods for studying these dynamics, such as molecular dynamics (MD) simulations, are computationally expensive and time-consuming \[[1](http://arxiv.org/abs/2304.02198)\]. Recent advances in generative modeling, particularly denoising diffusion models, have enabled efficient and accurate protein structure prediction and conformation sampling by learning distributions over crystallographic structures \[[2](https://www.semanticscholar.org/paper/21a4afa74caf78e28880b7fe4c30a09a5f9c14e3)\]. However, integrating physical supervision into these data-driven approaches remains a challenge, as standard energy-based objectives often lead to intractable optimization \[[3](https://www.semanticscholar.org/paper/2cfc26b4af99f195b433fa7aa00f221b111c7cd4)\]. 

Several studies have explored the use of deep learning for protein conformation generation. For instance, EigenFold employs a diffusion process that models the structure as a system of harmonic oscillators, naturally inducing a cascading-resolution generative process along the eigenmodes of the system \[[4](https://www.semanticscholar.org/paper/2eb1ed9d4baf548391d8220c0a8a3d0be79845ed)\]. Similarly, the idpGAN model, based on a transformer architecture, generates physically realistic conformational ensembles of intrinsically disordered peptides by training on simulation data \[[5](http://arxiv.org/abs/2402.04845)\]. These models demonstrate the potential of machine learning to generate conformational ensembles without the need for extensive sampling \[[6](http://arxiv.org/abs/2403.14088)\].

The Chroma model introduces a diffusion process that respects the conformational statistics of polymer ensembles, enabling the direct sampling of novel protein structures and sequences \[[7](http://arxiv.org/abs/2209.15611)\]. It also allows for conditioning the generative process to steer towards desired properties and functions \[[8](https://www.semanticscholar.org/paper/dc32a984b651256a8ec282be52310e6bd33d9815)\]. This approach has been validated experimentally, with the crystal structures of two designed proteins exhibiting atomistic agreement with Chroma samples \[[9](https://www.semanticscholar.org/paper/c49a0912595a1cc70aab63524f64ed08c92194a8)\]. 

Boltzmann generators, another approach, use neural networks to learn a coordinate transformation of the complex configurational equilibrium distribution to a distribution that can be easily sampled \[[10](http://arxiv.org/abs/2306.03117)\]. This method enables the generation of unbiased equilibrium samples of many-body systems and proteins, overcoming rare event sampling problems \[[11](https://www.semanticscholar.org/paper/98926d43356e87c22c82efc132dcaaac1ff40ebe)\]. These models have been applied to various tasks, including computing free-energy differences and discovering new configurations \[[12](http://arxiv.org/abs/2205.15019)\].

AlphaFold and its variants, such as AlphaFlow and ESMFlow, have also contributed significantly to the field. AlphaFold has achieved atomic accuracy in protein structure prediction, even in cases where no similar structure is known \[[13](https://www.semanticscholar.org/paper/18a93dc1558bf9d7534d0b416633cebaf75c1145)\]. AlphaFlow and ESMFlow further extend these capabilities by generating conformational ensembles and capturing conformational flexibility \[[14](https://www.semanticscholar.org/paper/7572ba7f604ef95d7acdd657ebac458106bd35df)\]. These models are trained on large datasets and can generate diverse, high-quality protein structures \[[15](http://arxiv.org/abs/2302.00600)\].

In addition, the SE(3) diffusion model and related approaches have been developed to generate protein backbones with high fidelity and diversity \[[16](https://www.semanticscholar.org/paper/1446b534858fc3fc6d9406920450b5c3ca87ee13)\]. These models leverage the SE(3) group structure to ensure invariance and accuracy in backbone generation \[[17](http://arxiv.org/abs/2306.05445)\]. The FoldFlow framework, based on the flow-matching paradigm, has also been introduced to model protein backbones with increased modeling power and efficiency \[[18](http://arxiv.org/abs/2302.02277)\].

Finally, the SPEACH_AF method enables the sampling of protein ensembles and conformational heterogeneity using AlphaFold2 by manipulating multiple sequence alignments \[[19](http://arxiv.org/abs/2310.02391)\]. This approach allows for the generation of multiple conformations and has been validated on various protein systems \[[20](https://www.semanticscholar.org/paper/867d80c8779e1d301a5fc6e267e263f7e4c4c5c7)\].

1. \[[1](http://arxiv.org/abs/2304.02198)\] Document 1  
2. \[[2](https://www.semanticscholar.org/paper/21a4afa74caf78e28880b7fe4c30a09a5f9c14e3)\] Document 2  
3. \[[3](https://www.semanticscholar.org/paper/2cfc26b4af99f195b433fa7aa00f221b111c7cd4)\] Document 5  
4. \[[4](https://www.semanticscholar.org/paper/2eb1ed9d4baf548391d8220c0a8a3d0be79845ed)\] Document 1  
5. \[[5](http://arxiv.org/abs/2402.04845)\] Document 2  
6. \[[6](http://arxiv.org/abs/2403.14088)\] Document 2  
7. \[[7](http://arxiv.org/abs/2209.15611)\] Document 3  
8. \[[8](https://www.semanticscholar.org/paper/dc32a984b651256a8ec282be52310e6bd33d9815)\] Document 3  
9. \[[9](https://www.semanticscholar.org/paper/c49a0912595a1cc70aab63524f64ed08c92194a8)\] Document 3  
10. \[[10](http://arxiv.org/abs/2306.03117)\] Document 4  
11. \[[11](https://www.semanticscholar.org/paper/98926d43356e87c22c82efc132dcaaac1ff40ebe)\] Document 4  
12. \[[12](http://arxiv.org/abs/2205.15019)\] Document 4  
13. \[[13](https://www.semanticscholar.org/paper/18a93dc1558bf9d7534d0b416633cebaf75c1145)\] Document 8  
14. \[[14](https://www.semanticscholar.org/paper/7572ba7f604ef95d7acdd657ebac458106bd35df)\] Document 5  
15. \[[15](http://arxiv.org/abs/2302.00600)\] Document 5  
16. \[[16](https://www.semanticscholar.org/paper/1446b534858fc3fc6d9406920450b5c3ca87ee13)\] Document 18  
17. \[[17](http://arxiv.org/abs/2306.05445)\] Document 19  
18. \[[18](http://arxiv.org/abs/2302.02277)\] Document 19  
19. \[[19](http://arxiv.org/abs/2310.02391)\] Document 23  
20. \[[20](https://www.semanticscholar.org/paper/867d80c8779e1d301a5fc6e267e263f7e4c4c5c7)\] Document 25
