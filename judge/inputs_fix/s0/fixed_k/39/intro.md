## Related Works

De novo genome assembly is a fundamental challenge in computational genomics, requiring the reconstruction of genomic sequences from short, overlapping, and potentially erroneous DNA reads without a reference genome \[[1](http://arxiv.org/abs/1705.11147)\]. This process is computationally intensive, especially with the exponential growth of genomic data, necessitating scalable and high-performance approaches \[[3](http://arxiv.org/abs/2207.04350)\]. Early methods relied on de Bruijn graph-based algorithms, which, while effective, suffered from high memory consumption due to the storage of all k-mers \[[7](http://arxiv.org/abs/1106.2603)\]. To address this, sparse de Bruijn graph structures were introduced, significantly reducing memory usage while maintaining comparable assembly quality \[[7](http://arxiv.org/abs/1106.2603)\]. These approaches laid the groundwork for more memory-efficient and scalable genome assemblers.

Recent advancements have focused on distributed-memory parallel algorithms to improve the efficiency of de novo assembly, particularly for large genomes. For example, the PPA-assembler leverages the Pregel framework to enable distributed de novo assembly with strong performance guarantees \[[2](http://arxiv.org/abs/1801.04453)\]. Similarly, the diBELLA 2D pipeline introduces new distributed-memory algorithms for overlap detection and layout simplification, achieving near-linear scaling and significant performance improvements over existing methods \[[5](http://arxiv.org/abs/2010.10055)\]. These developments highlight the importance of parallelism and efficient memory management in handling the computational demands of de novo assembly.

The use of long-read sequencing technologies has further complicated the assembly process, as these reads provide long-range evidence that helps resolve repetitive regions but also introduce higher error rates \[[6](http://arxiv.org/abs/2301.08785)\]. Tools like Minimap and miniasm have been developed to efficiently map and assemble long reads without an error correction stage, demonstrating the feasibility of fast and accurate assembly for bacterial and eukaryotic genomes \[[20](http://arxiv.org/abs/1512.01801)\]. Additionally, the ntLink tool utilizes minimizer-based mappings to improve genome scaffolding and mapping, offering a resource-efficient solution for long-read data \[[6](http://arxiv.org/abs/2301.08785)\].

Efforts to integrate machine learning and reinforcement learning into genome assembly have also emerged, aiming to automate and improve the accuracy of the assembly process \[[21](http://arxiv.org/abs/2102.02649)\]. While these approaches show promise, they often face challenges related to the high dimensionality of state and action spaces, limiting their practical applicability in real-world scenarios.

Quantum computing has also been explored as a potential solution for de novo assembly, with quantum algorithms based on graph walks showing potential for solving NP-hard problems in genome reconstruction \[[13](http://arxiv.org/abs/2308.03532)\]. However, these methods remain largely theoretical and have not yet been widely implemented or validated in practice.

In addition to algorithmic improvements, hardware-software co-design has been proposed to address the computational bottlenecks in de novo assembly. For instance, the SeGraM accelerator combines hardware and software optimizations to efficiently support both sequence-to-graph and sequence-to-sequence mapping, significantly improving performance and reducing power consumption \[[23](http://arxiv.org/abs/2205.05883)\]. These innovations underscore the need for integrated solutions that combine algorithmic efficiency with hardware capabilities to meet the growing demands of genome assembly.

In summary, while significant progress has been made in de novo genome assembly, challenges remain in terms of computational efficiency, memory usage, and scalability. The proposed NMP-PaK framework addresses these challenges through a hardware-software co-design that leverages near-memory processing to achieve superior performance and reduced memory footprint \[[1](http://arxiv.org/abs/1705.11147)\].

### References

1. \[[1](http://arxiv.org/abs/1705.11147)\] http://arxiv.org/abs/1705.11147  
2. \[[2](http://arxiv.org/abs/1801.04453)\] http://arxiv.org/abs/1801.04453  
3. \[[3](http://arxiv.org/abs/2207.04350)\] http://arxiv.org/abs/2207.04350  
4. \[[4](http://arxiv.org/abs/2011.05013)\] http://arxiv.org/abs/2011.05013  
5. \[[5](http://arxiv.org/abs/2010.10055)\] http://arxiv.org/abs/2010.10055  
6. \[[6](http://arxiv.org/abs/2301.08785)\] http://arxiv.org/abs/2301.08785  
7. \[[7](http://arxiv.org/abs/1106.2603)\] http://arxiv.org/abs/1106.2603  
8. \[[8](http://arxiv.org/abs/1108.3556)\] http://arxiv.org/abs/1108.3556  
9. \[[9](http://arxiv.org/abs/2004.06719)\] http://arxiv.org/abs/2004.06719  
10. \[[10](http://arxiv.org/abs/2111.01916)\] http://arxiv.org/abs/2111.01916  
11. \[[11](http://arxiv.org/abs/2309.07270)\] http://arxiv.org/abs/2309.07270  
12. \[[12](http://arxiv.org/abs/2308.07877)\] http://arxiv.org/abs/2308.07877  
13. \[[13](http://arxiv.org/abs/2308.03532)\] http://arxiv.org/abs/2308.03532  
14. \[[14](http://arxiv.org/abs/2407.07718)\] http://arxiv.org/abs/2407.07718  
15. \[[15](http://arxiv.org/abs/2212.01385)\] http://arxiv.org/abs/2212.01385  
16. \[[16](http://arxiv.org/abs/1308.2012)\] http://arxiv.org/abs/1308.2012  
17. \[[17](http://arxiv.org/abs/1506.05538)\] http://arxiv.org/abs/1506.05538  
18. \[[18](http://arxiv.org/abs/1305.6760)\] http://arxiv.org/abs/1305.6760  
19. \[[19](http://arxiv.org/abs/1310.1653)\] http://arxiv.org/abs/1310.1653  
20. \[[20](http://arxiv.org/abs/1512.01801)\] http://arxiv.org/abs/1512.01801  
21. \[[21](http://arxiv.org/abs/2102.02649)\] http://arxiv.org/abs/2102.02649  
22. \[[22](http://arxiv.org/abs/2404.07164)\] http://arxiv.org/abs/2404.07164  
23. \[[23](http://arxiv.org/abs/2205.05883)\] http://arxiv.org/abs/2205.05883  
24. \[[24](http://arxiv.org/abs/1207.2424)\] http://arxiv.org/abs/1207.2424
