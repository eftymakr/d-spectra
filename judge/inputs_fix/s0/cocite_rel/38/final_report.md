## Related Works

Memory bandwidth regulation and cache partitioning have been widely studied as techniques to achieve predictable timing in real-time computing systems \[[1](https://www.semanticscholar.org/paper/50d359dc737cb5c296b527f4eb1541dc55f3ed86)\]. These approaches are often combined with partitioned scheduling to ensure that tasks receive sufficient resources for predictable execution \[[2](https://www.semanticscholar.org/paper/25ebad66dc10d7b01c22684cbb200ddeb6502475)\]. However, the co-allocation of tasks and resources to cores remains a complex challenge, as task execution times are strongly influenced by the allocated resources \[[3](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)\]. 

Several works have explored the use of hardware and software techniques to manage memory bandwidth and cache resources. For example, MemGuard is a memory bandwidth reservation system designed to provide efficient performance isolation on multi-core platforms \[[4](https://www.semanticscholar.org/paper/dbd4eb5033815003e7f6519fd66e43e5fc297075)\]. It enables fine-grained control over memory access, which is critical for real-time applications \[[5](https://www.semanticscholar.org/paper/abbd6f8840092bd8e4e3684d3297e1b707abdc5d)\]. Similarly, PALLOC is a DRAM bank-aware memory allocator that improves performance isolation by leveraging memory bank partitioning \[[6](https://www.semanticscholar.org/paper/d5336fd2234f431f554fc5d878503a04a27e366e)\]. This approach helps reduce memory interference between tasks, which is a common issue in multi-core systems \[[7](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)\].

Cache partitioning has also been extensively studied to improve predictability in real-time embedded systems. The Impact of Cache Partitioning on Multi-tasking Real Time Embedded Systems highlights how cache partitioning can significantly reduce interference and improve timing predictability \[[8](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\]. This is particularly important in systems where cache behavior is a major source of unpredictability \[[9](https://www.semanticscholar.org/paper/0b1bc294dbd926f853a8ee41d1d8f8ecc3cfde13)\]. Cache coloring and cache bleaching techniques have also been proposed to manage cache interference. For instance, Cache Bleaching uses programmable logic to manipulate memory transactions and recompact colored sparse addresses in main memory \[[10](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)\].

In addition to hardware-based solutions, software frameworks have been developed to manage memory bandwidth and cache resources. E-WarP is a system-wide framework for memory bandwidth profiling and management that provides a profile-driven approach to analyze memory demand and predict temporal behavior \[[11](https://www.semanticscholar.org/paper/43cc4d0a998b9aa361264e5fc786c738a62382f1)\]. This framework enables workload-aware system consolidation and supports real-time applications by ensuring that memory resources are allocated efficiently \[[12](https://www.semanticscholar.org/paper/f71c848137ac1398f84e6ab7d896641f801ca192)\]. Similarly, RT-Gang introduces a real-time gang scheduling framework that enforces a one-gang-at-a-time policy to reduce contention in shared hardware resources such as cache and DRAM controller \[[13](https://www.semanticscholar.org/paper/31e4e1bb57bd04bc02d7f7110e66122a215d7bfa)\]. This approach improves predictability by ensuring that real-time tasks are not affected by interference from other tasks \[[14](http://arxiv.org/abs/1903.00999)\].

The challenge of co-allocation of tasks and resources has also been addressed in the context of scheduling algorithms. Scheduling Algorithms for Multiprogramming in a Hard-Real-Time Environment explores the design of scheduling policies that ensure predictable execution times in multi-core systems . These algorithms are essential for achieving the required timing guarantees in real-time applications .

In summary, the existing body of work demonstrates that memory bandwidth regulation, cache partitioning, and scheduling algorithms are critical for achieving predictable timing in real-time systems. These techniques are often combined to ensure that tasks receive the necessary resources for reliable execution . The proposed approach in this paper builds on these techniques by introducing a 0-1 linear program for task-resource co-allocation and a multi-objective heuristic to optimize resource usage while guaranteeing schedulability .

References:  
\[[1](https://www.semanticscholar.org/paper/50d359dc737cb5c296b527f4eb1541dc55f3ed86)\] Real-time cache management framework for multi-core architectures  
\[[2](https://www.semanticscholar.org/paper/25ebad66dc10d7b01c22684cbb200ddeb6502475)\] Scheduling Algorithms for Multiprogramming in a Hard-Real-Time Environment  
\[[3](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)\] Memory Bandwidth Management for Efficient Performance Isolation in Multi-Core Platforms  
\[[4](https://www.semanticscholar.org/paper/dbd4eb5033815003e7f6519fd66e43e5fc297075)\] MemGuard: Memory bandwidth reservation system for efficient performance isolation in multi-core platforms  
\[[5](https://www.semanticscholar.org/paper/abbd6f8840092bd8e4e3684d3297e1b707abdc5d)\] The Potential of Programmable Logic in the Middle: Cache Bleaching  
\[[6](https://www.semanticscholar.org/paper/d5336fd2234f431f554fc5d878503a04a27e366e)\] PALLOC: DRAM bank-aware memory allocator for performance isolation on multicore platforms  
\[[7](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)\] Bounding memory interference delay in COTS-based multi-core systems  
\[[8](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\] Impact of Cache Partitioning on Multi-tasking Real Time Embedded Systems  
\[[9](https://www.semanticscholar.org/paper/0b1bc294dbd926f853a8ee41d1d8f8ecc3cfde13)\] A Coordinated Approach for Practical OS-Level Cache Management in Multi-core Real-Time Systems  
\[[10](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)\] The Potential of Programmable Logic in the Middle: Cache Bleaching  
\[[11](https://www.semanticscholar.org/paper/43cc4d0a998b9aa361264e5fc786c738a62382f1)\] E-WarP: A System-wide Framework for Memory Bandwidth Profiling and Management  
\[[12](https://www.semanticscholar.org/paper/f71c848137ac1398f84e6ab7d896641f801ca192)\] Scheduling Parallel Real-Time Tasks on Multi-core Processors  
\[[13](https://www.semanticscholar.org/paper/31e4e1bb57bd04bc02d7f7110e66122a215d7bfa)\] RT-Gang: Real-Time Gang Scheduling Framework for Safety-Critical Systems  
\[[14](http://arxiv.org/abs/1903.00999)\] A survey of hard real-time scheduling for multiprocessor systems  
 Scheduling Algorithms for Multiprogramming in a Hard-Real-Time Environment  
 A Coordinated Approach for Practical OS-Level Cache Management in Multi-core Real-Time Systems  
 Memory Bandwidth Regulation and Cache Partitioning are Widely Used Techniques  
 Memory bandwidth regulation and cache partitioning are widely used techniques for achieving predictable timing in real-time computing systems.
## Research papers
### Outline
- [Cache Partitioning Methods [2 papers]](#category-cache-partitioning-methods)
- [Software Frameworks for Memory Management [1 papers]](#category-software-frameworks-for-memory-management)
- [Performance Isolation Mechanisms [3 papers]](#category-performance-isolation-mechanisms)
- [Hardware-Based Resource Management Solutions [2 papers]](#category-hardware-based-resource-management-solutions)
- [Scheduling Policies for Real-Time Systems [3 papers]](#category-scheduling-policies-for-real-time-systems)
- [Real-Time System Predictability Enhancements [3 papers]](#category-real-time-system-predictability-enhancements)

### <a id='category-cache-partitioning-methods'></a>Cache Partitioning Methods: 2 papers found.
Context: 
	Document 1: [Category]: «Cache Partitioning Methods»
[Snippet]: «»
[_citation_number]: «1»

	Document 2: [Category]: «Cache Partitioning Methods»
[Snippet]: «»
[_citation_number]: «11»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-15T16:40:14+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)\]. Further details \[[6](https://www.semanticscholar.org/paper/d5336fd2234f431f554fc5d878503a04a27e366e)\]\[[7](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)\]\[[8](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\]\[[9](https://www.semanticscholar.org/paper/0b1bc294dbd926f853a8ee41d1d8f8ecc3cfde13)\]\[[10](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Memory bandwidth regulation and cache partitioning are widely used techniques
for achieving predictable timing in real-time computing systems. Combined with
partitioned scheduling, these methods require careful co-allocation of tasks
and resources to cores, as task execution times strongly depend on available
allocated resources. To address this challenge, this paper presents a 0-1
linear program for task-resource co-allocation, along with a multi-objective
heuristic designed to minimize resource usage while guaranteeing schedulability
under a preemptive EDF scheduling policy. Our heuristic employs a multi-layer
framework, where an outer layer explores resource allocations using
Pareto-pruned search, and an inner layer optimizes task allocation by solving a
knapsack problem using dynamic programming. To evaluate the performance of the
proposed optimization algorithm, we profile real-world benchmarks on an
embedded AMD UltraScale+ ZCU102 platform, with fine-grained resource
partitioning enabled by the Jailhouse hypervisor, leveraging cache set
partitioning and MemGuard for memory bandwidth regulation. Experiments based on
the benchmarking results show that the proposed 0-1 linear program outperforms
existing mixed-integer programs by finding more optimal solutions within the
same time limit. Moreover, the proposed multi-objective multi-layer heuristic
performs consistently better than the state-of-the-art multi-resource-task
co-allocation algorithm in terms of schedulability, resource usage, number of
non-dominated solutions, and computational efficiency.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)\]. Further details discussed in contexts \[[2](https://www.semanticscholar.org/paper/25ebad66dc10d7b01c22684cbb200ddeb6502475)\]\[[7](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Cache partitioning methods are essential in real-time computing systems for ensuring predictable timing and efficient resource utilization \[[1](https://www.semanticscholar.org/paper/50d359dc737cb5c296b527f4eb1541dc55f3ed86)\]. These methods focus on dividing cache resources among multiple tasks or cores to prevent contention and ensure deterministic behavior \[[11](https://www.semanticscholar.org/paper/43cc4d0a998b9aa361264e5fc786c738a62382f1)\]. By isolating cache sets for specific tasks, systems can achieve better performance and reliability, particularly in environments where timing constraints are critical. The use of cache partitioning is often combined with memory bandwidth regulation techniques to further enhance predictability \[[1](https://www.semanticscholar.org/paper/50d359dc737cb5c296b527f4eb1541dc55f3ed86)\]. Existing approaches typically rely on heuristic or optimization-based strategies to allocate resources effectively, as the complexity of co-allocation increases with the number of tasks and resources involved \[[11](https://www.semanticscholar.org/paper/43cc4d0a998b9aa361264e5fc786c738a62382f1)\]. The integration of cache set partitioning with hypervisors like Jailhouse enables fine-grained control over resource allocation, supporting more sophisticated scheduling policies such as EDF \[[1](https://www.semanticscholar.org/paper/50d359dc737cb5c296b527f4eb1541dc55f3ed86)\]. These methods are crucial for achieving schedulability and minimizing resource usage while maintaining system performance.
|    | reference                                                                                                                                                                        | date     | key idea/summary                                                                                          |
|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------|
|  0 | [A Coordinated Approach for Practical OS-Level Cache Management in Multi-core Real-Time Systems](https://www.semanticscholar.org/paper/50d359dc737cb5c296b527f4eb1541dc55f3ed86) | 07/09/13 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
|  1 | [Impact of Cache Partitioning on Multi-tasking Real Time Embedded Systems](https://www.semanticscholar.org/paper/43cc4d0a998b9aa361264e5fc786c738a62382f1)                       | 08/25/08 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
### <a id='category-software-frameworks-for-memory-management'></a>Software Frameworks for Memory Management: 1 papers found.
Context: 
	Document 1: [Category]: «Software Frameworks for Memory Management»
[Snippet]: «»
[_citation_number]: «2»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-15T16:40:14+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)\]. Further details \[[6](https://www.semanticscholar.org/paper/d5336fd2234f431f554fc5d878503a04a27e366e)\]\[[7](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)\]\[[8](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\]\[[9](https://www.semanticscholar.org/paper/0b1bc294dbd926f853a8ee41d1d8f8ecc3cfde13)\]\[[10](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Memory bandwidth regulation and cache partitioning are widely used techniques
for achieving predictable timing in real-time computing systems. Combined with
partitioned scheduling, these methods require careful co-allocation of tasks
and resources to cores, as task execution times strongly depend on available
allocated resources. To address this challenge, this paper presents a 0-1
linear program for task-resource co-allocation, along with a multi-objective
heuristic designed to minimize resource usage while guaranteeing schedulability
under a preemptive EDF scheduling policy. Our heuristic employs a multi-layer
framework, where an outer layer explores resource allocations using
Pareto-pruned search, and an inner layer optimizes task allocation by solving a
knapsack problem using dynamic programming. To evaluate the performance of the
proposed optimization algorithm, we profile real-world benchmarks on an
embedded AMD UltraScale+ ZCU102 platform, with fine-grained resource
partitioning enabled by the Jailhouse hypervisor, leveraging cache set
partitioning and MemGuard for memory bandwidth regulation. Experiments based on
the benchmarking results show that the proposed 0-1 linear program outperforms
existing mixed-integer programs by finding more optimal solutions within the
same time limit. Moreover, the proposed multi-objective multi-layer heuristic
performs consistently better than the state-of-the-art multi-resource-task
co-allocation algorithm in terms of schedulability, resource usage, number of
non-dominated solutions, and computational efficiency.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)\]. Further details discussed in contexts \[[2](https://www.semanticscholar.org/paper/25ebad66dc10d7b01c22684cbb200ddeb6502475)\]\[[7](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
The category "Software Frameworks for Memory Management" focuses on the design and implementation of tools and systems that enable efficient and predictable memory usage in computing environments. These frameworks are particularly relevant in real-time systems where memory bandwidth regulation and cache partitioning are critical for ensuring deterministic behavior \[[2](https://www.semanticscholar.org/paper/25ebad66dc10d7b01c22684cbb200ddeb6502475)\]. They often integrate with scheduling policies such as EDF (Earliest Deadline First) to manage resource allocation dynamically \[[2](https://www.semanticscholar.org/paper/25ebad66dc10d7b01c22684cbb200ddeb6502475)\]. The use of hypervisors like Jailhouse, combined with techniques such as cache set partitioning and tools like MemGuard, allows for fine-grained control over memory resources, enhancing both performance and reliability in embedded systems \[[2](https://www.semanticscholar.org/paper/25ebad66dc10d7b01c22684cbb200ddeb6502475)\]. Such frameworks are essential for optimizing task execution times and ensuring schedulability in complex, multi-core environments.
|    | reference                                                                                                                                           | date     | key idea/summary                                                                                          |
|----|-----------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------|
|  0 | [Real-time cache management framework for multi-core architectures](https://www.semanticscholar.org/paper/25ebad66dc10d7b01c22684cbb200ddeb6502475) | 04/09/13 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
### <a id='category-performance-isolation-mechanisms'></a>Performance Isolation Mechanisms: 3 papers found.
Context: 
	Document 1: [Category]: «Performance Isolation Mechanisms»
[Snippet]: «»
[_citation_number]: «3»

	Document 2: [Category]: «Performance Isolation Mechanisms»
[Snippet]: «»
[_citation_number]: «7»

	Document 3: [Category]: «Performance Isolation Mechanisms»
[Snippet]: «»
[_citation_number]: «9»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-15T16:40:14+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)\]. Further details \[[6](https://www.semanticscholar.org/paper/d5336fd2234f431f554fc5d878503a04a27e366e)\]\[[7](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)\]\[[8](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\]\[[9](https://www.semanticscholar.org/paper/0b1bc294dbd926f853a8ee41d1d8f8ecc3cfde13)\]\[[10](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Memory bandwidth regulation and cache partitioning are widely used techniques
for achieving predictable timing in real-time computing systems. Combined with
partitioned scheduling, these methods require careful co-allocation of tasks
and resources to cores, as task execution times strongly depend on available
allocated resources. To address this challenge, this paper presents a 0-1
linear program for task-resource co-allocation, along with a multi-objective
heuristic designed to minimize resource usage while guaranteeing schedulability
under a preemptive EDF scheduling policy. Our heuristic employs a multi-layer
framework, where an outer layer explores resource allocations using
Pareto-pruned search, and an inner layer optimizes task allocation by solving a
knapsack problem using dynamic programming. To evaluate the performance of the
proposed optimization algorithm, we profile real-world benchmarks on an
embedded AMD UltraScale+ ZCU102 platform, with fine-grained resource
partitioning enabled by the Jailhouse hypervisor, leveraging cache set
partitioning and MemGuard for memory bandwidth regulation. Experiments based on
the benchmarking results show that the proposed 0-1 linear program outperforms
existing mixed-integer programs by finding more optimal solutions within the
same time limit. Moreover, the proposed multi-objective multi-layer heuristic
performs consistently better than the state-of-the-art multi-resource-task
co-allocation algorithm in terms of schedulability, resource usage, number of
non-dominated solutions, and computational efficiency.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)\]. Further details discussed in contexts \[[2](https://www.semanticscholar.org/paper/25ebad66dc10d7b01c22684cbb200ddeb6502475)\]\[[7](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: Performance isolation mechanisms are critical for ensuring predictable timing in real-time computing systems, particularly when combined with partitioned scheduling \[[3](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)\]. These mechanisms typically involve techniques such as memory bandwidth regulation and cache partitioning, which help in controlling resource access and minimizing interference between tasks \[[7](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)\]. Recent work has focused on developing efficient co-allocation strategies that balance resource usage with schedulability guarantees \[[9](https://www.semanticscholar.org/paper/0b1bc294dbd926f853a8ee41d1d8f8ecc3cfde13)\]. For instance, some approaches leverage heuristic-based multi-layer frameworks to optimize task allocation, often incorporating dynamic programming or Pareto-pruned search methods to enhance computational efficiency \[[3](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)\]. Additionally, the use of hypervisors like Jailhouse, along with tools such as MemGuard, has enabled fine-grained resource partitioning, further supporting isolation in multi-core environments \[[9](https://www.semanticscholar.org/paper/0b1bc294dbd926f853a8ee41d1d8f8ecc3cfde13)\]. These advancements highlight the growing importance of performance isolation in meeting the stringent timing requirements of real-time applications.
|    | reference                                                                                                                                                                                   | date     | key idea/summary                                                                                          |
|----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------|
|  0 | [MemGuard: Memory bandwidth reservation system for efficient performance isolation in multi-core platforms](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d) | 04/09/13 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
|  1 | [PALLOC: DRAM bank-aware memory allocator for performance isolation on multicore platforms](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)                 | 04/15/14 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
|  2 | [Memory Bandwidth Management for Efficient Performance Isolation in Multi-Core Platforms](https://www.semanticscholar.org/paper/0b1bc294dbd926f853a8ee41d1d8f8ecc3cfde13)                   | 02/01/16 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
### <a id='category-hardware-based-resource-management-solutions'></a>Hardware-Based Resource Management Solutions: 2 papers found.
Context: 
	Document 1: [Category]: «Hardware-Based Resource Management Solutions»
[Snippet]: «Consolidating hard real-time systems onto modern multi-core Systems-on-Chip (SoC) is an open challenge. The extensive sharing of hardware resources at the memory hierarchy raises important unpredictability concerns. The problem is exacerbated as more computationally demanding workload is expected to be handled with real-time guarantees in next-generation Cyber-Physical Systems (CPS). A large body of works has approached the problem by proposing novel hardware redesigns, and by proposing software-only solutions to mitigate performance interference.Strong from the observation that unpredictability arises from a lack of fine-grained control over the behavior of shared hardware components, we outline a promising new resource management approach. We demonstrate that it is possible to introduce Programmable Logic In-the-Middle (PLIM) between a traditional multi-core processor and main memory. This provides the unique capability of manipulating individual memory transactions. We propose a proof-of-concept system implementation of PLIM modules on a commercial multi-core SoC. The PLIM approach is then leveraged to solve long-standing issues with cache coloring. Thanks to PLIM, colored sparse addresses can be re-compacted in main memory. This is the base principle behind the technique we call Cache Bleaching. We evaluate our design on real applications and propose hypervisor-level adaptations to showcase the potential of the PLIM approach.»
[_citation_number]: «4»

	Document 2: [Category]: «Hardware-Based Resource Management Solutions»
[Snippet]: «»
[_citation_number]: «6»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-15T16:40:14+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)\]. Further details \[[6](https://www.semanticscholar.org/paper/d5336fd2234f431f554fc5d878503a04a27e366e)\]\[[7](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)\]\[[8](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\]\[[9](https://www.semanticscholar.org/paper/0b1bc294dbd926f853a8ee41d1d8f8ecc3cfde13)\]\[[10](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Memory bandwidth regulation and cache partitioning are widely used techniques
for achieving predictable timing in real-time computing systems. Combined with
partitioned scheduling, these methods require careful co-allocation of tasks
and resources to cores, as task execution times strongly depend on available
allocated resources. To address this challenge, this paper presents a 0-1
linear program for task-resource co-allocation, along with a multi-objective
heuristic designed to minimize resource usage while guaranteeing schedulability
under a preemptive EDF scheduling policy. Our heuristic employs a multi-layer
framework, where an outer layer explores resource allocations using
Pareto-pruned search, and an inner layer optimizes task allocation by solving a
knapsack problem using dynamic programming. To evaluate the performance of the
proposed optimization algorithm, we profile real-world benchmarks on an
embedded AMD UltraScale+ ZCU102 platform, with fine-grained resource
partitioning enabled by the Jailhouse hypervisor, leveraging cache set
partitioning and MemGuard for memory bandwidth regulation. Experiments based on
the benchmarking results show that the proposed 0-1 linear program outperforms
existing mixed-integer programs by finding more optimal solutions within the
same time limit. Moreover, the proposed multi-objective multi-layer heuristic
performs consistently better than the state-of-the-art multi-resource-task
co-allocation algorithm in terms of schedulability, resource usage, number of
non-dominated solutions, and computational efficiency.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)\]. Further details discussed in contexts \[[2](https://www.semanticscholar.org/paper/25ebad66dc10d7b01c22684cbb200ddeb6502475)\]\[[7](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer:  
Hardware-based resource management solutions have been a focal point in addressing the challenges of real-time computing systems, particularly in the context of multi-core Systems-on-Chip (SoC) \[[4](https://www.semanticscholar.org/paper/dbd4eb5033815003e7f6519fd66e43e5fc297075)\]. The increasing complexity of workloads in next-generation Cyber-Physical Systems (CPS) has highlighted the need for fine-grained control over shared hardware resources to ensure predictable timing behavior \[[4](https://www.semanticscholar.org/paper/dbd4eb5033815003e7f6519fd66e43e5fc297075)\]. Traditional approaches have relied on either hardware redesigns or software-only solutions to mitigate performance interference \[[4](https://www.semanticscholar.org/paper/dbd4eb5033815003e7f6519fd66e43e5fc297075)\]. A promising new direction involves introducing Programmable Logic In-the-Middle (PLIM) between the processor and memory, enabling the manipulation of individual memory transactions \[[4](https://www.semanticscholar.org/paper/dbd4eb5033815003e7f6519fd66e43e5fc297075)\]. This approach has been demonstrated to resolve long-standing issues such as cache coloring through a technique called Cache Bleaching, where colored sparse addresses are re-compacted in main memory \[[4](https://www.semanticscholar.org/paper/dbd4eb5033815003e7f6519fd66e43e5fc297075)\]. The PLIM concept also supports hypervisor-level adaptations, showcasing its potential for enhancing resource management in real-time environments \[[4](https://www.semanticscholar.org/paper/dbd4eb5033815003e7f6519fd66e43e5fc297075)\]. While Document 2 provides additional context, it does not offer specific details to further elaborate on these themes \[[6](https://www.semanticscholar.org/paper/d5336fd2234f431f554fc5d878503a04a27e366e)\].
|    | reference                                                                                                                                                                                           | date     | key idea/summary                                                                                                                                                                                                                                                                                  |
|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [The Potential of Programmable Logic in the Middle: Cache Bleaching](https://www.semanticscholar.org/paper/dbd4eb5033815003e7f6519fd66e43e5fc297075)                                                | 04/01/20 | The paper introduces a novel resource management approach called Programmable Logic In-the-Middle (PLIM) to address unpredictability in multi-core systems by enabling fine-grained control over memory transactions, leading to a technique called Cache Bleaching for improving cache coloring. |
|  1 | [Attacking the one-out-of-m multicore problem by combining hardware management with mixed-criticality provisioning](https://www.semanticscholar.org/paper/d5336fd2234f431f554fc5d878503a04a27e366e) | 04/11/16 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                         |
### <a id='category-scheduling-policies-for-real-time-systems'></a>Scheduling Policies for Real-Time Systems: 3 papers found.
Context: 
	Document 1: [Category]: «Scheduling Policies for Real-Time Systems»
[Snippet]: «»
[_citation_number]: «5»

	Document 2: [Category]: «Scheduling Policies for Real-Time Systems»
[Snippet]: «»
[_citation_number]: «8»

	Document 3: [Category]: «Scheduling Policies for Real-Time Systems»
[Snippet]: «»
[_citation_number]: «13»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-15T16:40:14+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)\]. Further details \[[6](https://www.semanticscholar.org/paper/d5336fd2234f431f554fc5d878503a04a27e366e)\]\[[7](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)\]\[[8](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\]\[[9](https://www.semanticscholar.org/paper/0b1bc294dbd926f853a8ee41d1d8f8ecc3cfde13)\]\[[10](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Memory bandwidth regulation and cache partitioning are widely used techniques
for achieving predictable timing in real-time computing systems. Combined with
partitioned scheduling, these methods require careful co-allocation of tasks
and resources to cores, as task execution times strongly depend on available
allocated resources. To address this challenge, this paper presents a 0-1
linear program for task-resource co-allocation, along with a multi-objective
heuristic designed to minimize resource usage while guaranteeing schedulability
under a preemptive EDF scheduling policy. Our heuristic employs a multi-layer
framework, where an outer layer explores resource allocations using
Pareto-pruned search, and an inner layer optimizes task allocation by solving a
knapsack problem using dynamic programming. To evaluate the performance of the
proposed optimization algorithm, we profile real-world benchmarks on an
embedded AMD UltraScale+ ZCU102 platform, with fine-grained resource
partitioning enabled by the Jailhouse hypervisor, leveraging cache set
partitioning and MemGuard for memory bandwidth regulation. Experiments based on
the benchmarking results show that the proposed 0-1 linear program outperforms
existing mixed-integer programs by finding more optimal solutions within the
same time limit. Moreover, the proposed multi-objective multi-layer heuristic
performs consistently better than the state-of-the-art multi-resource-task
co-allocation algorithm in terms of schedulability, resource usage, number of
non-dominated solutions, and computational efficiency.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)\]. Further details discussed in contexts \[[2](https://www.semanticscholar.org/paper/25ebad66dc10d7b01c22684cbb200ddeb6502475)\]\[[7](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer:  
Scheduling policies for real-time systems have been extensively studied to ensure predictable timing and efficient resource utilization \[[5](https://www.semanticscholar.org/paper/abbd6f8840092bd8e4e3684d3297e1b707abdc5d)\]. A key challenge in such systems is the co-allocation of tasks and resources to cores, as task execution times are highly dependent on the allocated resources \[[8](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\]. Recent approaches have focused on developing optimization techniques that balance resource usage with schedulability guarantees, particularly under preemptive EDF policies \[[13](https://www.semanticscholar.org/paper/31e4e1bb57bd04bc02d7f7110e66122a215d7bfa)\]. For instance, some studies have explored multi-objective heuristics that combine Pareto-pruned search with dynamic programming to optimize task allocation \[[8](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\]. These methods aim to minimize resource consumption while maintaining schedulability, often leveraging advanced frameworks such as the Jailhouse hypervisor for fine-grained resource partitioning \[[13](https://www.semanticscholar.org/paper/31e4e1bb57bd04bc02d7f7110e66122a215d7bfa)\]. Additionally, the integration of memory bandwidth regulation techniques, such as cache set partitioning and MemGuard, has been shown to enhance predictability in real-time environments \[[5](https://www.semanticscholar.org/paper/abbd6f8840092bd8e4e3684d3297e1b707abdc5d)\]. Overall, the field continues to evolve with a focus on improving both computational efficiency and the scalability of scheduling algorithms in complex, heterogeneous systems \[[8](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\].
|    | reference                                                                                                                                                    | date     | key idea/summary                                                                                          |
|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------|
|  0 | [Scheduling Algorithms for Multiprogramming in a Hard-Real-Time Environment](https://www.semanticscholar.org/paper/abbd6f8840092bd8e4e3684d3297e1b707abdc5d) | 01/03/89 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
|  1 | [Scheduling Parallel Real-Time Tasks on Multi-core Processors](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)               | 11/30/10 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
|  2 | [A survey of hard real-time scheduling for multiprocessor systems](https://www.semanticscholar.org/paper/31e4e1bb57bd04bc02d7f7110e66122a215d7bfa)           | 10/01/11 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
### <a id='category-real-time-system-predictability-enhancements'></a>Real-Time System Predictability Enhancements: 3 papers found.
Context: 
	Document 1: [Category]: «Real-Time System Predictability Enhancements»
[Snippet]: «In commercial-off-the-shelf (COTS) multi-core systems, a task running on one core can be delayed by other tasks running simultaneously on other cores due to interference in the shared DRAM main memory. Such memory interference delay can be large and highly variable, thereby posing a significant challenge for the design of predictable real-time systems. In this paper, we present techniques to provide a tight upper bound on the worst-case memory interference in a COTS-based multi-core system. We explicitly model the major resources in the DRAM system, including banks, buses and the memory controller. By considering their timing characteristics, we analyze the worst-case memory interference delay imposed on a task by other tasks running in parallel. To the best of our knowledge, this is the first work bounding the request re-ordering effect of COTS memory controllers. Our work also enables the quantification of the extent by which memory interference can be reduced by partitioning DRAM banks. We evaluate our approach on a commodity multi-core platform running Linux/RK. Experimental results show that our approach provides an upper bound very close to our measured worst-case interference.»
[_citation_number]: «10»

	Document 2: [Category]: «Real-Time System Predictability Enhancements»
[Snippet]: «The proliferation of multi-core, accelerator-enabled embedded systems has introduced new opportunities to consolidate real-time systems of increasing complexity. But the road to build confidence on the temporal behavior of co-running applications has presented formidable challenges. Most prominently, the main memory subsystem represents a performance bottleneck for both CPUs and accelerators. And industry-viable frameworks for full-system main memory management and performance analysis are past due.In this paper, we propose our Envelope-aWare Predictive model, or E-WarP for short. E-WarP is a methodology and technological framework to: (1) analyze the memory demand of applications following a profile-driven approach; (2) make realistic predictions on the temporal behavior of workload deployed on CPUs and accelerators; and (3) perform saturation-aware system consolidation. This work aims at providing the technological foundations as well as the theoretical grassroots for truly workload-aware analysis of real-time systems. We provide a full implementation of our techniques on a commercial platform (NXP S32V234) and make two key observations. First, we achieve, on average, a 6% overprediction on the runtime of bandwidth-regulated applications. Second, we experimentally validate that the calculated bounds hold if the main memory subsystem operates below saturation.»
[_citation_number]: «12»

	Document 3: [Category]: «Real-Time System Predictability Enhancements»
[Snippet]: «In this paper, we present RT-Gang: a novel real-time gang scheduling framework that enforces a one-gang-at-a-time policy. We find that, in a multicore platform, co-scheduling multiple parallel real-time tasks would require highly pessimistic worst-case execution time (WCET) and schedulability analysis—even when there are enough cores—due to contention in shared hardware resources such as cache and DRAM controller. In RT-Gang, all threads of a parallel real-time task form a real-time gang and the scheduler globally enforces the one-gang-at-a-time scheduling policy to guarantee tight and accurate task WCET. To minimize under-utilization, we integrate a state-of-the-art memory bandwidth throttling framework to allow safe execution of best-effort tasks. Specifically, any idle cores, if exist, are used to schedule best-effort tasks but their maximum memory bandwidth usages are strictly throttled to tightly bound interference to real-time gang tasks. We implement RT-Gang in the Linux kernel and evaluate it on two representative embedded multicore platforms using both synthetic and real-world DNN workloads. The results show that RT-Gang dramatically improves system predictability and the overhead is negligible.»
[_citation_number]: «14»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-15T16:40:14+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)\]. Further details \[[6](https://www.semanticscholar.org/paper/d5336fd2234f431f554fc5d878503a04a27e366e)\]\[[7](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)\]\[[8](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\]\[[9](https://www.semanticscholar.org/paper/0b1bc294dbd926f853a8ee41d1d8f8ecc3cfde13)\]\[[10](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Memory bandwidth regulation and cache partitioning are widely used techniques
for achieving predictable timing in real-time computing systems. Combined with
partitioned scheduling, these methods require careful co-allocation of tasks
and resources to cores, as task execution times strongly depend on available
allocated resources. To address this challenge, this paper presents a 0-1
linear program for task-resource co-allocation, along with a multi-objective
heuristic designed to minimize resource usage while guaranteeing schedulability
under a preemptive EDF scheduling policy. Our heuristic employs a multi-layer
framework, where an outer layer explores resource allocations using
Pareto-pruned search, and an inner layer optimizes task allocation by solving a
knapsack problem using dynamic programming. To evaluate the performance of the
proposed optimization algorithm, we profile real-world benchmarks on an
embedded AMD UltraScale+ ZCU102 platform, with fine-grained resource
partitioning enabled by the Jailhouse hypervisor, leveraging cache set
partitioning and MemGuard for memory bandwidth regulation. Experiments based on
the benchmarking results show that the proposed 0-1 linear program outperforms
existing mixed-integer programs by finding more optimal solutions within the
same time limit. Moreover, the proposed multi-objective multi-layer heuristic
performs consistently better than the state-of-the-art multi-resource-task
co-allocation algorithm in terms of schedulability, resource usage, number of
non-dominated solutions, and computational efficiency.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)\]. Further details discussed in contexts \[[2](https://www.semanticscholar.org/paper/25ebad66dc10d7b01c22684cbb200ddeb6502475)\]\[[7](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Recent research has focused on improving predictability in real-time systems by addressing memory interference and resource contention. Memory interference in multi-core systems, particularly in shared DRAM, has been identified as a critical challenge, where tasks running on different cores can experience significant delays due to resource contention \[[10](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)\]. To mitigate this, studies have explored modeling DRAM resources such as banks, buses, and memory controllers to derive tight upper bounds on worst-case memory interference \[[10](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)\]. This approach enables more accurate scheduling and resource allocation, as demonstrated by techniques that quantify the impact of DRAM partitioning on reducing interference \[[10](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)\]. Additionally, the integration of memory bandwidth regulation and cache partitioning has been proposed to enhance predictability, with frameworks like MemGuard and cache set partitioning being used to manage resource allocation effectively \[[12](https://www.semanticscholar.org/paper/f71c848137ac1398f84e6ab7d896641f801ca192)\]. These methods are often combined with partitioned scheduling to ensure that task execution times remain predictable \[[12](https://www.semanticscholar.org/paper/f71c848137ac1398f84e6ab7d896641f801ca192)\]. Furthermore, real-time gang scheduling has been introduced as a novel approach to enforce a one-gang-at-a-time policy, minimizing pessimistic WCET analysis by reducing contention in shared hardware resources such as cache and DRAM controllers \[[14](http://arxiv.org/abs/1903.00999)\]. This approach also integrates memory bandwidth throttling to allow safe execution of non-critical tasks without compromising the predictability of real-time tasks \[[14](http://arxiv.org/abs/1903.00999)\]. These advancements highlight the ongoing efforts to improve system predictability through sophisticated resource management and scheduling strategies.
|    | reference                                                                                                                                                       | date     | key idea/summary                                                                                                                                                                                                     |
|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Bounding memory interference delay in COTS-based multi-core systems](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)           | 04/15/14 | This paper presents techniques to provide a tight upper bound on the worst-case memory interference in COTS multi-core systems by modeling DRAM resources and analyzing interference delay caused by parallel tasks. |
|  1 | [E-WarP: A System-wide Framework for Memory Bandwidth Profiling and Management](https://www.semanticscholar.org/paper/f71c848137ac1398f84e6ab7d896641f801ca192) | 12/01/20 | The paper introduces E-WarP, a framework for analyzing memory demand, predicting temporal behavior, and enabling system consolidation in multi-core and accelerator-enabled embedded systems.                        |
|  2 | [RT-Gang: Real-Time Gang Scheduling Framework for Safety-Critical Systems](http://arxiv.org/abs/1903.00999)                                                     | 03/03/19 | RT-Gang is a real-time gang scheduling framework that enforces a one-gang-at-a-time policy to improve system predictability by minimizing WCET pessimism and interference in multicore platforms.                    |
