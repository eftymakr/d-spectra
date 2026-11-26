## Related Works

De novo genome assembly remains a computationally intensive task, particularly when dealing with large and complex metagenomics datasets. Several approaches have been proposed to address these challenges, with a focus on improving speed, memory efficiency, and scalability. MEGAHIT \[[1](http://arxiv.org/abs/1409.7208)\] is a notable example, offering an ultra-fast single-node solution for large metagenomics assembly. It avoids pre-processing steps like partitioning and normalization, which can compromise result integrity. MEGAHIT generates assemblies with longer contigs and higher read alignment rates compared to previous methods, achieving a 4-fold improvement in alignment coverage. However, it is limited to single-node processing and does not leverage hardware acceleration for further performance gains.

Recent advances in sequencing technologies have enabled the generation of ultra-long reads, which pose new challenges for alignment and assembly algorithms. Minimap2 \[[2](http://arxiv.org/abs/1708.01492)\] has been developed to address these challenges by efficiently aligning long reads, including full-length mRNA or cDNA sequences, against large reference databases. It employs split-read alignment and concave gap cost models to reduce spurious alignments, achieving speeds up to 30 times faster than mainstream short-read mappers while maintaining comparable accuracy. This makes Minimap2 a versatile tool for handling diverse sequencing data types.

To further enhance performance, several studies have explored the use of GPUs for accelerating de novo assembly. Accelerating large-scale de novo metagenome assembly using GPUs \[[6]()\] and GPU-accelerated large-scale genome assembly \[[7]()\] have demonstrated significant improvements in both speed and memory efficiency. These approaches leverage the parallel processing capabilities of GPUs to handle the computational demands of assembly tasks. Similarly, Gpu-euler \[[8]()\] and GAGM \[[9]()\] have been proposed as GPU-based solutions for sequence assembly, with the latter utilizing mate pairs to improve accuracy. GRASShopPER \[[10]()\] introduces an algorithm for de novo assembly based on GPU alignments, further demonstrating the potential of GPU acceleration in this domain.

Despite these advances, existing methods still face challenges related to memory footprint and irregular data patterns. Harp \[[11]()\] addresses these issues by leveraging the quasi-sequential characteristics of long reads to improve the efficiency of sequence-to-graph mapping. This approach is particularly relevant for handling the complex and interdependent data structures encountered in de novo assembly.

In summary, while existing tools have made significant strides in improving the speed and efficiency of de novo assembly, there remains a need for custom hardware solutions that can better address the inherent challenges of the task. NMP-PaK  represents a promising direction by introducing a hardware-software co-design that leverages near-memory processing to reduce memory footprint and improve performance.

References:  
\[[1](http://arxiv.org/abs/1409.7208)\] MEGAHIT: An ultra-fast single-node solution for large and complex metagenomics assembly via succinct de Bruijn graph  
\[[2](http://arxiv.org/abs/1708.01492)\] Minimap2: pairwise alignment for nucleotide sequences  
\[[6]()\] Accelerating large scale de novo metagenome assembly using GPUs  
\[[7]()\] Gpu-accelerated large-scale genome assembly  
\[[8]()\] Gpu-euler: Sequence assembly using gpgpu  
\[[9]()\] GAGM: Genome assembly on GPU using mate pairs  
\[[10]()\] GRASShopPER—An algorithm for de novo assembly based on GPU alignments  
\[[11]()\] Harp: Leveraging Quasi-Sequential Characteristics to Accelerate Sequence-to-Graph Mapping of Long Reads
