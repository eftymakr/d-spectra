## Related Works

Zero-Knowledge Proofs (ZKPs) have emerged as a critical paradigm in verifiable computing, enabling a prover to demonstrate the validity of a statement without revealing additional information \[[1](http://arxiv.org/abs/2408.05890)\]. Despite their potential, the computational complexity of the proving process has hindered widespread adoption \[[1](http://arxiv.org/abs/2408.05890)\]. Recent efforts have focused on accelerating key primitives of ZKP protocols, particularly the Number Theoretic Transform (NTT) and Multi-Scalar Multiplication (MSM), which are computationally intensive \[[1](http://arxiv.org/abs/2408.05890)\]. 

Several works have explored hardware acceleration for these primitives. For instance, GPU-based implementations have been proposed to improve the efficiency of MSMs, which are crucial for ZKP generation \[[4](https://eprint.iacr.org/2022/1321)\]. The cuZK framework introduces a faster parallel MSM algorithm on GPUs, aiming to reduce the time required for proof generation \[[4](https://eprint.iacr.org/2022/1321)\]. Similarly, the MSMAC architecture targets the acceleration of MSMs for ZKP systems, emphasizing performance improvements through optimized hardware design \[[7](https://doi.org/10.1145/3649329.3655672)\]. 

The challenge of achieving both small proof sizes and universal setup has also been addressed in prior work. The BatchZK system presents a fully pipelined GPU-accelerated approach for batch generation of ZKPs, supporting multiple proofs simultaneously while maintaining small proof sizes \[[11](https://eprint.iacr.org/2024/1862)\]. This is particularly relevant for applications requiring frequent verification, such as blockchain technologies and verifiable machine learning \[[1](http://arxiv.org/abs/2408.05890)\]. 

Efforts to optimize NTTs have also been explored. The Myosotis architecture employs a pipelined and parameterized design for MSMs, leveraging data sharing to enhance performance \[[6]()\]. Additionally, the SZKP framework introduces an ASIC-based solution that accelerates the entire proof generation process, achieving significant speedups over CPU and GPU implementations \[[1](http://arxiv.org/abs/2408.05890)\]. This work emphasizes the importance of structured dataflows for both NTTs and MSMs, enabling efficient on-chip computation \[[1](http://arxiv.org/abs/2408.05890)\]. 

Recent advancements in hardware-algorithm co-design have further improved ZKP acceleration. The ReZK accelerator offers a highly reconfigurable solution, allowing for flexibility in adapting to different ZKP protocols \[[5]()\]. Similarly, the Elastic (MSM) technique introduces a modular preprocessing approach for MSMs, enhancing performance on GPUs by reducing memory access overhead \[[8](https://eprint.iacr.org/2024/057)\]. 

While these works demonstrate significant progress in accelerating ZKP primitives, challenges remain in achieving both high performance and flexibility across diverse applications. The zkSpeed accelerator, presented in this work, addresses these challenges by supporting a universal setup and maintaining small proof sizes, while accelerating the entire protocol, including the SumCheck and MSM primitives \[[1](http://arxiv.org/abs/2408.05890)\]. This holistic approach ensures that ZKP systems can be deployed in a wider range of scenarios, including those with strict verification time constraints \[[1](http://arxiv.org/abs/2408.05890)\].

References:  
\[[1](http://arxiv.org/abs/2408.05890)\] SZKP: A Scalable Accelerator Architecture for Zero-Knowledge Proofs  
\[[4](https://eprint.iacr.org/2022/1321)\] cuZK: Accelerating Zero-Knowledge Proof with A Faster Parallel Multi-Scalar Multiplication Algorithm on GPUs  
\[[6]()\] Myosotis: An Efficiently Pipelined and Parameterized Multi-Scalar Multiplication Architecture via Data Sharing  
\[[7](https://doi.org/10.1145/3649329.3655672)\] MSMAC: Accelerating Multi-Scalar Multiplication for Zero-Knowledge Proof  
\[[8](https://eprint.iacr.org/2024/057)\] Elastic (MSM): A Fast, Elastic and Modular Preprocessing Technique for Multi-Scalar Multiplication Algorithm on (GPUs)  
\[[11](https://eprint.iacr.org/2024/1862)\] (BatchZK): A Fully Pipelined (GPU)-Accelerated System for Batch Generation of Zero-Knowledge Proofs  
\[[5]()\] ReZK: A Highly Reconfigurable Accelerator for Zero-Knowledge Proof
