## Related Works

Protein dynamics are essential for understanding biological functions and properties, yet traditional methods such as molecular dynamics (MD) simulations are computationally expensive and time-consuming \[[1](https://www.semanticscholar.org/paper/21a4afa74caf78e28880b7fe4c30a09a5f9c14e3)\]. Recent advances in generative modeling have introduced new approaches for protein structure prediction and conformation sampling, particularly through denoising diffusion models \[[2](http://arxiv.org/abs/2304.02198)\]. These models learn distributions over crystallographic structures, enabling efficient and accurate prediction of protein conformations \[[3](https://www.semanticscholar.org/paper/2eb1ed9d4baf548391d8220c0a8a3d0be79845ed)\]. However, integrating physical supervision into these data-driven models remains a challenge, as standard energy-based objectives often lead to intractable optimization \[[4](https://www.semanticscholar.org/paper/2cfc26b4af99f195b433fa7aa00f221b111c7cd4)\].

Several studies have explored the use of deep learning for protein conformational sampling. For instance, Boltzmann generators combine deep learning and statistical mechanics to generate unbiased equilibrium samples of many-body systems \[[5](http://arxiv.org/abs/2402.04845)\]. These models use invertible neural networks to learn coordinate transformations that enable sampling from the equilibrium distribution \[[6](https://www.semanticscholar.org/paper/dc32a984b651256a8ec282be52310e6bd33d9815)\]. Similarly, EigenFold employs diffusion models to sample a distribution of structures from a given protein sequence, providing a more comprehensive picture of model uncertainty \[[7](http://arxiv.org/abs/2403.14088)\]. These approaches demonstrate the potential of deep learning to capture conformational ensembles and flexibility, which are crucial for biological function \[[8](http://arxiv.org/abs/2209.15611)\].

Another line of research focuses on the use of generative adversarial networks (GANs) for protein conformational sampling. The idpGAN model, trained on coarse-grained simulations of intrinsically disordered peptides, demonstrates the ability to predict sequence-dependent ensembles for sequences not present in the training set \[[9](https://www.semanticscholar.org/paper/18a93dc1558bf9d7534d0b416633cebaf75c1145)\]. This transferability highlights the potential of GANs to generate diverse and physically plausible conformations \[[10](https://www.semanticscholar.org/paper/c49a0912595a1cc70aab63524f64ed08c92194a8)\]. Similarly, the Str2Str framework leverages a score-based approach to enable zero-shot conformation sampling, showing significant improvements over previous state-of-the-art methods \[[11](http://arxiv.org/abs/2306.03117)\].

Recent work has also focused on improving the physical plausibility of generated structures by incorporating force fields and energy-based objectives. For example, the ConfDiff model integrates a force-guided network with a mixture of data-based score models to generate protein conformations with high fidelity and diversity \[[12](https://www.semanticscholar.org/paper/8fa4f6b5232868c2e400670716540f6877068439)\]. This approach addresses the limitations of existing score-based diffusion methods, which often fail to incorporate physical prior knowledge \[[13](http://arxiv.org/abs/2205.15019)\].

In addition, the development of diffusion models over rigid body motions in 3D (SE(3)) has enabled more accurate modeling of protein backbones. The FoldFlow series of models, based on the flow-matching paradigm, demonstrates the ability to generate high-quality protein structures with greater stability and efficiency compared to diffusion-based approaches \[[14](http://arxiv.org/abs/2306.05445)\]. These models leverage the group invariance of SE(3) to ensure accurate and diverse conformational sampling \[[15](http://arxiv.org/abs/2310.02391)\].

The integration of physical supervision into generative models has also been explored in the context of protein structure prediction. The EBA method aligns generative models with feedback from physical models, efficiently calibrating them to balance conformational states based on energy differences \[[16](https://www.semanticscholar.org/paper/74d37f4ad2c017067c4da89059be1eee823b5da9)\]. This approach improves the physical plausibility of generated structures, enhancing model predictions and holding promise for applications in structural biology and drug discovery \[[17](https://www.semanticscholar.org/paper/4244065522c28c9a075d145ad1970a6fb7811f78)\].

References  
\[[1](https://www.semanticscholar.org/paper/21a4afa74caf78e28880b7fe4c30a09a5f9c14e3)\] Document 1  
\[[2](http://arxiv.org/abs/2304.02198)\] Document 5  
\[[3](https://www.semanticscholar.org/paper/2eb1ed9d4baf548391d8220c0a8a3d0be79845ed)\] Document 8  
\[[4](https://www.semanticscholar.org/paper/2cfc26b4af99f195b433fa7aa00f221b111c7cd4)\] Document 11  
\[[5](http://arxiv.org/abs/2402.04845)\] Document 3  
\[[6](https://www.semanticscholar.org/paper/dc32a984b651256a8ec282be52310e6bd33d9815)\] Document 3  
\[[7](http://arxiv.org/abs/2403.14088)\] Document 2  
\[[8](http://arxiv.org/abs/2209.15611)\] Document 2  
\[[9](https://www.semanticscholar.org/paper/18a93dc1558bf9d7534d0b416633cebaf75c1145)\] Document 1  
\[[10](https://www.semanticscholar.org/paper/c49a0912595a1cc70aab63524f64ed08c92194a8)\] Document 1  
\[[11](http://arxiv.org/abs/2306.03117)\] Document 11  
\[[12](https://www.semanticscholar.org/paper/8fa4f6b5232868c2e400670716540f6877068439)\] Document 7  
\[[13](http://arxiv.org/abs/2205.15019)\] Document 7  
\[[14](http://arxiv.org/abs/2306.05445)\] Document 15  
\[[15](http://arxiv.org/abs/2310.02391)\] Document 15  
\[[16](https://www.semanticscholar.org/paper/74d37f4ad2c017067c4da89059be1eee823b5da9)\] Document 21  
\[[17](https://www.semanticscholar.org/paper/4244065522c28c9a075d145ad1970a6fb7811f78)\] Document 21
