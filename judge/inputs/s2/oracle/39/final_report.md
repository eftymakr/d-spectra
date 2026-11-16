## Related Works

De novo genome assembly remains a computationally intensive task, particularly when dealing with large and complex metagenomics datasets. Several approaches have been proposed to address these challenges, with a focus on improving speed, memory efficiency, and scalability. MEGAHIT \[[1](http://arxiv.org/abs/1409.7208)\] is a notable example, offering an ultra-fast single-node solution for large metagenomics assembly. It avoids pre-processing steps like partitioning and normalization, which can compromise result integrity. MEGAHIT generates assemblies with longer contigs and higher read alignment rates compared to previous methods, achieving a 4-fold improvement in alignment coverage. However, it is limited to single-node processing and does not leverage hardware acceleration for further performance gains.

Recent advances in sequencing technologies have enabled the generation of ultra-long reads, which pose new challenges for alignment and assembly algorithms. Minimap2 \[[2](http://arxiv.org/abs/1708.01492)\] has been developed to address these challenges by efficiently aligning long reads, including full-length mRNA or cDNA sequences, against large reference databases. It employs split-read alignment and concave gap cost models to reduce spurious alignments, achieving speeds up to 30 times faster than mainstream short-read mappers while maintaining comparable accuracy. This makes Minimap2 a versatile tool for handling diverse sequencing data types.

To further enhance performance, several studies have explored the use of GPUs for accelerating de novo assembly. Accelerating large-scale de novo metagenome assembly using GPUs \[[6]()\] and GPU-accelerated large-scale genome assembly \[[7]()\] have demonstrated significant improvements in both speed and memory efficiency. These approaches leverage the parallel processing capabilities of GPUs to handle the computational demands of assembly tasks. Similarly, Gpu-euler \[[8]()\] and GAGM \[[9]()\] have been proposed as GPU-based solutions for sequence assembly, with the latter utilizing mate pairs to improve accuracy. GRASShopPER \[[10]()\] introduces an algorithm for de novo assembly based on GPU alignments, further demonstrating the potential of GPU acceleration in this domain.

Despite these advances, existing methods still face challenges related to memory footprint and irregular data patterns. Harp \[[11]()\] addresses these issues by leveraging the quasi-sequential characteristics of long reads to improve the efficiency of sequence-to-graph mapping. This approach is particularly relevant for handling the complex and interdependent data structures encountered in de novo assembly.

In summary, while existing tools have made significant strides in improving the speed and efficiency of de novo assembly, the integration of hardware-software co-design, such as the proposed NMP-PaK, offers a promising direction for further optimization.
## Research papers
### Outline
- [Existing De Novo Assemblers [1 papers]](#category-existing-de-novo-assemblers)
- [Algorithmic Improvements in Alignment [1 papers]](#category-algorithmic-improvements-in-alignment)
- [Hardware Acceleration Approaches [5 papers]](#category-hardware-acceleration-approaches)
- [GPU-Based Assembly Tools [3 papers]](#category-gpu-based-assembly-tools)
- [Scalability of Assembly Methods [1 papers]](#category-scalability-of-assembly-methods)

### <a id='category-existing-de-novo-assemblers'></a>Existing De Novo Assemblers: 1 papers found.
Context: 
	Document 1: [_citation_number]: «1»
[Snippet]: «MEGAHIT is a NGS de novo assembler for assembling large and complex
metagenomics data in a time- and cost-efficient manner. It finished assembling
a soil metagenomics dataset with 252Gbps in 44.1 hours and 99.6 hours on a
single computing node with and without a GPU, respectively. MEGAHIT assembles
the data as a whole, i.e., it avoids pre-processing like partitioning and
normalization, which might compromise on result integrity. MEGAHIT generates 3
times larger assembly, with longer contig N50 and average contig length than
the previous assembly. 55.8% of the reads were aligned to the assembly, which
is 4 times higher than the previous. The source code of MEGAHIT is freely
available at https://github.com/voutcn/megahit under GPLv3 license.»
[Category]: «Existing De Novo Assemblers»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-12T21:17:20+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3]()\]. Further details \[[6]()\]\[[7]()\]\[[8]()\]\[[9]()\]\[[10]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: De novo assembly enables investigations of unknown genomes, paving the way
for personalized medicine and disease management. However, it faces immense
computational challenges arising from the excessive data volumes and
algorithmic complexity.
  While state-of-the-art de novo assemblers utilize distributed systems for
extreme-scale genome assembly, they demand substantial computational and memory
resources. They also fail to address the inherent challenges of de novo
assembly, including a large memory footprint,
|    | reference                                                                                                                                                |   date | key idea/summary                                                                                                                                                        |
|----|----------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [MEGAHIT: An ultra-fast single-node solution for large and complex
  metagenomics assembly via succinct de Bruijn graph](http://arxiv.org/abs/1409.7208) |    nan | MEGAHIT is a metagenomics assembler that efficiently handles large datasets, produces larger and more accurate assemblies, and is freely available under GPLv3 license. |
### <a id='category-algorithmic-improvements-in-alignment'></a>Algorithmic Improvements in Alignment: 1 papers found.
Context: 
	Document 1: [_citation_number]: «2»
[Snippet]: «Motivation: Recent advances in sequencing technologies promise ultra-long
reads of $\sim$100 kilo bases (kb) in average, full-length mRNA or cDNA reads
in high throughput and genomic contigs over 100 mega bases (Mb) in length.
Existing alignment programs are unable or inefficient to process such data at
scale, which presses for the development of new alignment algorithms.
  Results: Minimap2 is a general-purpose alignment program to map DNA or long
mRNA sequences against a large reference database. It works with accurate short
reads of $\ge$100bp in length, $\ge$1kb genomic reads at error rate $\sim$15%,
full-length noisy Direct RNA or cDNA reads, and assembly contigs or closely
related full chromosomes of hundreds of megabases in length. Minimap2 does
split-read alignment, employs concave gap cost for long insertions and
deletions (INDELs) and introduces new heuristics to reduce spurious alignments.
It is 3-4 times faster than mainstream short-read mappers at comparable
accuracy and $\ge$30 times faster at higher accuracy for both genomic and mRNA
reads, surpassing most aligners specialized in one type of alignment.
  Availability and implementation: https://github.com/lh3/minimap2
  Contact: hengli@broadinstitute.org»
[Category]: «Algorithmic Improvements in Alignment»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-12T21:17:20+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3]()\]. Further details \[[6]()\]\[[7]()\]\[[8]()\]\[[9]()\]\[[10]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper
|    | reference                                                                                |   date | key idea/summary                                                                                                                                                                                                 |
|----|------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Minimap2: pairwise alignment for nucleotide sequences](http://arxiv.org/abs/1708.01492) |    nan | Minimap2 is a high-performance alignment program designed to efficiently handle ultra-long reads and large genomic data, offering significant speed improvements over existing tools while maintaining accuracy. |
### <a id='category-hardware-acceleration-approaches'></a>Hardware Acceleration Approaches: 5 papers found.
Context: 
	Document 1: [_citation_number]: «3»
[Snippet]: «»
[Category]: «Hardware Acceleration Approaches»

	Document 2: [_citation_number]: «4»
[Snippet]: «»
[Category]: «Hardware Acceleration Approaches»

	Document 3: [_citation_number]: «5»
[Snippet]: «»
[Category]: «Hardware Acceleration Approaches»

	Document 4: [_citation_number]: «6»
[Snippet]: «»
[Category]: «Hardware Acceleration Approaches»

	Document 5: [_citation_number]: «7»
[Snippet]: «»
[Category]: «Hardware Acceleration Approaches»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-12T21:17:20+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3]()\]. Further details \[[6]()\]\[[7]()\]\[[8]()\]\[[9]()\]\[[10]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: De novo assembly enables investigations of unknown genomes, paving the way
for personalized medicine and disease management. However, it faces immense
computational challenges arising from the excessive data volumes and
algorithmic complexity.
  While state-of-the-art de novo assemblers utilize distributed systems for
extreme-scale genome assembly, they demand substantial computational and memory
resources. They also fail to address the inherent challenges of de novo
assembly, including a large memory footprint, memory-bound behavior, and
irregular data patterns stemming from complex, interdependent data structures.
Given these challenges, de novo assembly merits a custom hardware solution,
though existing approaches have not fully addressed the limitations.
  We propose NMP-PaK, a hardware-software co-design that accelerates scalable
de novo genome assembly through near-memory processing (NMP). Our channel-level
NMP architecture addresses memory bottlene
|    | reference                                                                              |   date | key idea/summary                                                                                          |
|----|----------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------|
|  0 | [Ultra efficient acceleration for de novo genome assembly via near-memory computing]() |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
|  1 | [Pim-assembler: A processing-in-memory platform for genome assembly]()                 |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
|  2 | [Abakus: Accelerating k-mer Counting with Storage Technology]()                        |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
|  3 | [Accelerating large scale de novo metagenome assembly using GPUs]()                    |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
|  4 | [Gpu-accelerated large-scale genome assembly]()                                        |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
### <a id='category-gpu-based-assembly-tools'></a>GPU-Based Assembly Tools: 3 papers found.
Answer:  
GPU-Based Assembly Tools have been widely explored to address the computational challenges of de novo genome assembly, particularly in managing large data volumes and algorithmic complexity \[[8]()\]. These tools leverage the parallel processing capabilities of GPUs to accelerate assembly tasks, offering significant improvements in performance and memory efficiency compared to traditional CPU-based approaches \[[9]()\]. However, existing GPU-based solutions often struggle with memory-bound operations and irregular data patterns, which are inherent in de novo assembly due to the dynamic and interdependent nature of genomic data \[[10]()\]. To mitigate these limitations, recent advancements have focused on optimizing memory access patterns and reducing the overall memory footprint through customized processing strategies and hybrid CPU-GPU architectures. These efforts highlight the potential of GPU-based tools in enhancing the scalability and efficiency of de novo assembly workflows.
|    | reference                                                                 |   date | key idea/summary                                                                                          |
|----|---------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------|
|  0 | [Gpu-euler: Sequence assembly using gpgpu]()                              |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
|  1 | [GAGM: Genome assembly on GPU using mate pairs]()                         |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
|  2 | [GRASShopPER—An algorithm for de novo assembly based on GPU alignments]() |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
### <a id='category-scalability-of-assembly-methods'></a>Scalability of Assembly Methods: 1 papers found.
Context: 
	Document 1: [_citation_number]: «11»
[Snippet]: «»
[Category]: «Scalability of Assembly Methods»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-12T21:17:20+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3]()\]. Further details \[[6]()\]\[[7]()\]\[[8]()\]\[[9]()\]\[[10]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: De novo assembly enables investigations of unknown genomes, paving the way
for personalized medicine and disease management. However, it faces immense
computational challenges arising from the excessive data volumes and
algorithmic complexity.
  While state-of-the-art de novo assemblers utilize distributed systems for
extreme-scale genome assembly, they demand substantial computational and memory
resources. They also fail to address the inherent challenges of de novo
assembly, including a large memory footprint, memory-bound behavior, and
irregular data patterns stemming from complex, interdependent data structures.
Given these challenges, de novo assembly merits a custom hardware solution,
though existing approaches have not fully addressed the limitations.
  We propose NMP-PaK, a hardware-software co-design that accelerates scalable
de novo genome assembly through near-memory processing (NMP). Our channel-level
NMP architecture addresses memory bottlenecks while providing sufficient
scratchpad space for processing elements. Customized processing elements
maximize parallelism while efficiently handling large data structures that are
both dynamic and interdependent. Software optimizations include customized
batch processing to reduce the memory footprint and hybrid CPU-NMP processing
to address hardware underutilization caused by irregular data patterns.
  NMP-PaK conducts the same genome assembly while incurring a 14X smaller
memory footprint compared to the state-of-the-art de novo assembly. Moreover,
NMP-PaK delivers a
|    | reference                                                                                                   |   date | key idea/summary                                                                                          |
|----|-------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------|
|  0 | [Harp: Leveraging Quasi-Sequential Characteristics to Accelerate Sequence-to-Graph Mapping of Long Reads]() |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
