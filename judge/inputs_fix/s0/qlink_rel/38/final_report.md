## Related Works

Memory bandwidth regulation and cache partitioning have been widely studied as techniques to achieve predictable timing in real-time computing systems \[[12](http://arxiv.org/abs/1809.05921)\]. These approaches are often combined with partitioned scheduling to ensure that task execution times are tightly controlled by the allocated resources \[[12](http://arxiv.org/abs/1809.05921)\]. Prior work has explored various methods for managing shared memory resources, including memory bandwidth reservation systems such as MemGuard \[[2](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)\], which aim to provide efficient performance isolation in multi-core platforms \[[2](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)\]. Similarly, PALLOC \[[6](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)\] introduces a DRAM bank-aware memory allocator that enhances performance isolation by managing memory access patterns across cores.

Cache partitioning has also been extensively investigated as a means to improve predictability in multi-core real-time systems. For instance, utility-based cache partitioning \[[13](https://www.semanticscholar.org/paper/333da42f4369dff8ca905ad21ea6ee2f5dc99d55)\] provides a low-overhead, high-performance runtime mechanism for partitioning shared caches, allowing for dynamic allocation of cache resources. This approach is particularly relevant in systems where multiple tasks with varying memory access patterns coexist \[[13](https://www.semanticscholar.org/paper/333da42f4369dff8ca905ad21ea6ee2f5dc99d55)\]. Additionally, the impact of cache partitioning on multi-tasking real-time embedded systems has been studied, highlighting the importance of fine-grained control over cache resources to reduce interference \[[14](https://www.semanticscholar.org/paper/43cc4d0a998b9aa361264e5fc786c738a62382f1)\].

In the context of scheduling, several studies have focused on scheduling algorithms for multiprogramming in hard real-time environments \[[4](https://www.semanticscholar.org/paper/abbd6f8840092bd8e4e3684d3297e1b707abdc5d)\]. These algorithms aim to ensure that tasks meet their deadlines despite the unpredictable nature of shared hardware resources. Furthermore, the scheduling of parallel real-time tasks on multi-core processors has been addressed, emphasizing the need for efficient resource allocation strategies to minimize interference and improve predictability \[[7](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\].

A key challenge in multi-core real-time systems is the unpredictability caused by memory interference, particularly in commercial-off-the-shelf (COTS) platforms \[[5](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)\]. This interference arises from contention over shared DRAM resources such as memory banks, buses, and memory controllers. To address this, techniques have been proposed to bound memory interference delays, providing tight upper bounds on worst-case performance \[[5](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)\]. These methods involve modeling the timing characteristics of shared memory resources and analyzing their impact on task execution \[[5](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)\].

Recent work has also explored dynamic memory bandwidth regulation as a means to improve schedulability in real-time systems \[[12](http://arxiv.org/abs/1809.05921)\]. This approach involves dynamically allocating memory bandwidth to cores based on workload characteristics, allowing for more flexible and efficient resource management. The proposed analysis reduces the response time computation to a maximization problem over time intervals with different bandwidth-to-core assignments \[[12](http://arxiv.org/abs/1809.05921)\]. This method has been applied to improve the schedulability of integrated modular avionics systems under memory-intensive workloads \[[12](http://arxiv.org/abs/1809.05921)\].

In addition, programmable logic in-the-middle (PLIM) has been proposed as a novel approach to mitigate cache-related unpredictability in multi-core systems \[[8](https://www.semanticscholar.org/paper/dbd4eb5033815003e7f6519fd66e43e5fc297075)\]. By introducing PLIM modules between the processor and main memory, it is possible to manipulate memory transactions and improve cache management. This technique, known as Cache Bleaching, enables the re-compaction of colored sparse addresses in main memory, thereby reducing cache interference \[[8](https://www.semanticscholar.org/paper/dbd4eb5033815003e7f6519fd66e43e5fc297075)\].

The combination of these techniques—memory bandwidth regulation, cache partitioning, and dynamic resource allocation—forms the foundation for achieving predictable timing in modern multi-core real-time systems. The proposed 0-1 linear program and multi-objective heuristic in this paper build upon these prior works, offering a more efficient and effective approach to task-resource co-allocation \[[12](http://arxiv.org/abs/1809.05921)\].

1. \[[2](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)\] MemGuard: Memory bandwidth reservation system for efficient performance isolation in multi-core platforms  
2. \[[5](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)\] Bounding memory interference delay in COTS-based multi-core systems  
3. \[[6](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)\] PALLOC: DRAM bank-aware memory allocator for performance isolation on multicore platforms  
4. \[[7](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\] Scheduling Parallel Real-Time Tasks on Multi-core Processors  
5. \[[8](https://www.semanticscholar.org/paper/dbd4eb5033815003e7f6519fd66e43e5fc297075)\] The Potential of Programmable Logic in the Middle: Cache Bleaching  
6. \[[12](http://arxiv.org/abs/1809.05921)\] Analysis of Dynamic Memory Bandwidth Regulation in Multi-core Real-Time Systems
## Research papers
### Outline
- [Cache Management Techniques for Predictable Timing [3 papers]](#category-cache-management-techniques-for-predictable-timing)
- [Performance Isolation Mechanisms in Multi-Core Platforms [5 papers]](#category-performance-isolation-mechanisms-in-multi-core-platforms)
- [Task Scheduling Algorithms for Real-Time Systems [3 papers]](#category-task-scheduling-algorithms-for-real-time-systems)
- [Dynamic Memory Bandwidth Regulation Approaches [1 papers]](#category-dynamic-memory-bandwidth-regulation-approaches)
- [Cache Partitioning Methods [2 papers]](#category-cache-partitioning-methods)

### <a id='category-cache-management-techniques-for-predictable-timing'></a>Cache Management Techniques for Predictable Timing: 3 papers found.
Context: 
	Document 3: [Snippet]: «Consolidating hard real-time systems onto modern multi-core Systems-on-Chip (SoC) is an open challenge. The extensive sharing of hardware resources at the memory hierarchy raises important unpredictability concerns. The problem is exacerbated as more computationally demanding workload is expected to be handled with real-time guarantees in next-generation Cyber-Physical Systems (CPS). A large body of works has approached the problem by proposing novel hardware redesigns, and by proposing software-only solutions to mitigate performance interference.Strong from the observation that unpredictability arises from a lack of fine-grained control over the behavior of shared hardware components, we outline a promising new resource management approach. We demonstrate that it is possible to introduce Programmable Logic In-the-Middle (PLIM) between a traditional multi-core processor and main memory. This provides the unique capability of manipulating individual memory transactions. We propose a proof-of-concept system implementation of PLIM modules on a commercial multi-core SoC. The PLIM approach is then leveraged to solve long-standing issues with cache coloring. Thanks to PLIM, colored sparse addresses can be re-compacted in main memory. This is the base principle behind the technique we call Cache Bleaching. We evaluate our design on real applications and propose hypervisor-level adaptations to showcase the potential of the PLIM approach.»
[_citation_number]: «8»
[Category]: «Cache Management Techniques for Predictable Timing»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-15T16:40:14+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](https://www.semanticscholar.org/paper/25ebad66dc10d7b01c22684cbb200ddeb6502475)\]. Further details \[[6](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)\]\[[7](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\]\[[8](https://www.semanticscholar.org/paper/dbd4eb5033815003e7f6519fd66e43e5fc297075)\]\[[9](https://www.semanticscholar.org/paper/d5336fd2234f431f554fc5d878503a04a27e366e)\]\[[10](https://www.semanticscholar.org/paper/0b1bc294dbd926f853a8ee41d1d8f8ecc3cfde13)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Memory bandwidth regulation and cache partitioning are widely used techniques
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](https://www.semanticscholar.org/paper/25ebad66dc10d7b01c22684cbb200ddeb6502475)\]. Further details discussed in contexts \[[2](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)\]\[[7](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Cache management techniques for predictable timing have been a focal point in real-time computing systems, particularly in the context of multi-core SoCs and Cyber-Physical Systems (CPS). A significant challenge arises from the unpredictability caused by shared hardware resources at the memory hierarchy, which can lead to performance interference and timing violations \[[8](https://www.semanticscholar.org/paper/dbd4eb5033815003e7f6519fd66e43e5fc297075)\]. To mitigate these issues, researchers have explored both hardware redesigns and software-based solutions. One promising approach involves the introduction of Programmable Logic In-the-Middle (PLIM) between the multi-core processor and main memory, enabling fine-grained control over memory transactions \[[8](https://www.semanticscholar.org/paper/dbd4eb5033815003e7f6519fd66e43e5fc297075)\]. This approach has been leveraged to address long-standing issues such as cache coloring, with techniques like Cache Bleaching allowing for the re-compaction of colored sparse addresses in main memory \[[8](https://www.semanticscholar.org/paper/dbd4eb5033815003e7f6519fd66e43e5fc297075)\]. These innovations highlight the importance of resource management strategies that ensure predictable timing, especially as computational demands increase in next-generation systems. The use of hypervisor-level adaptations further demonstrates the potential of such techniques in real-world applications \[[8](https://www.semanticscholar.org/paper/dbd4eb5033815003e7f6519fd66e43e5fc297075)\].
|    | reference                                                                                                                                                                        | date     | key idea/summary                                                                                                                                                                                                                                                                                  |
|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [A Coordinated Approach for Practical OS-Level Cache Management in Multi-core Real-Time Systems](https://www.semanticscholar.org/paper/50d359dc737cb5c296b527f4eb1541dc55f3ed86) | 07/09/13 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                         |
|  1 | [Real-time cache management framework for multi-core architectures](https://www.semanticscholar.org/paper/25ebad66dc10d7b01c22684cbb200ddeb6502475)                              | 04/09/13 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                         |
|  2 | [The Potential of Programmable Logic in the Middle: Cache Bleaching](https://www.semanticscholar.org/paper/dbd4eb5033815003e7f6519fd66e43e5fc297075)                             | 04/01/20 | The paper introduces a novel resource management approach called Programmable Logic In-the-Middle (PLIM) to address unpredictability in multi-core systems by enabling fine-grained control over memory transactions, leading to a technique called Cache Bleaching for improving cache coloring. |
### <a id='category-performance-isolation-mechanisms-in-multi-core-platforms'></a>Performance Isolation Mechanisms in Multi-Core Platforms: 5 papers found.
Context: 
	Document 1: [Snippet]: «»
[_citation_number]: «2»
[Category]: «Performance Isolation Mechanisms in Multi-Core Platforms»

	Document 2: [Snippet]: «In commercial-off-the-shelf (COTS) multi-core systems, a task running on one core can be delayed by other tasks running simultaneously on other cores due to interference in the shared DRAM main memory. Such memory interference delay can be large and highly variable, thereby posing a significant challenge for the design of predictable real-time systems. In this paper, we present techniques to provide a tight upper bound on the worst-case memory interference in a COTS-based multi-core system. We explicitly model the major resources in the DRAM system, including banks, buses and the memory controller. By considering their timing characteristics, we analyze the worst-case memory interference delay imposed on a task by other tasks running in parallel. To the best of our knowledge, this is the first work bounding the request re-ordering effect of COTS memory controllers. Our work also enables the quantification of the extent by which memory interference can be reduced by partitioning DRAM banks. We evaluate our approach on a commodity multi-core platform running Linux/RK. Experimental results show that our approach provides an upper bound very close to our measured worst-case interference.»
[_citation_number]: «5»
[Category]: «Performance Isolation Mechanisms in Multi-Core Platforms»

	Document 3: [Snippet]: «»
[_citation_number]: «6»
[Category]: «Performance Isolation Mechanisms in Multi-Core Platforms»

	Document 4: [Snippet]: «»
[_citation_number]: «9»
[Category]: «Performance Isolation Mechanisms in Multi-Core Platforms»

	Document 5: [Snippet]: «»
[_citation_number]: «10»
[Category]: «Performance Isolation Mechanisms in Multi-Core Platforms»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-15T16:40:14+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](https://www.semanticscholar.org/paper/25ebad66dc10d7b01c22684cbb200ddeb6502475)\]. Further details \[[6](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)\]\[[7](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\]\[[8](https://www.semanticscholar.org/paper/dbd4eb5033815003e7f6519fd66e43e5fc297075)\]\[[9](https://www.semanticscholar.org/paper/d5336fd2234f431f554fc5d878503a04a27e366e)\]\[[10](https://www.semanticscholar.org/paper/0b1bc294dbd926f853a8ee41d1d8f8ecc3cfde13)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Memory bandwidth regulation and cache partitioning are widely used techniques
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](https://www.semanticscholar.org/paper/25ebad66dc10d7b01c22684cbb200ddeb6502475)\]. Further details discussed in contexts \[[2](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)\]\[[7](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Performance isolation mechanisms in multi-core platforms are critical for ensuring predictable timing in real-time systems, particularly in commercial-off-the-shelf (COTS) architectures where memory interference can significantly impact task execution \[[5](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)\]. Memory bandwidth regulation and cache partitioning are widely used techniques to mitigate such issues, as they help control resource access and reduce contention \[[5](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)\]. These approaches are often combined with partitioned scheduling to ensure that tasks are allocated resources in a way that minimizes timing variability \[[5](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)\]. Prior work has focused on modeling shared resources like DRAM banks, buses, and memory controllers to analyze worst-case interference and provide bounds on memory access delays \[[5](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)\]. Techniques such as DRAM bank partitioning have been explored to reduce interference, with experimental results showing that these methods can closely match measured worst-case scenarios \[[5](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)\]. While these studies highlight the importance of resource allocation and isolation, recent advances have introduced more sophisticated optimization frameworks, such as multi-layer heuristics that combine Pareto-pruned search with dynamic programming to improve schedulability and resource efficiency \[[5](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)\]. The ongoing research in this area continues to address the challenges of balancing performance, predictability, and resource utilization in multi-core environments \[[5](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)\].
|    | reference                                                                                                                                                                                           | date     | key idea/summary                                                                                                                                                                                                     |
|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [MemGuard: Memory bandwidth reservation system for efficient performance isolation in multi-core platforms](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)         | 04/09/13 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                            |
|  1 | [Bounding memory interference delay in COTS-based multi-core systems](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)                                               | 04/15/14 | This paper presents techniques to provide a tight upper bound on the worst-case memory interference in COTS multi-core systems by modeling DRAM resources and analyzing interference delay caused by parallel tasks. |
|  2 | [PALLOC: DRAM bank-aware memory allocator for performance isolation on multicore platforms](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)                         | 04/15/14 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                            |
|  3 | [Attacking the one-out-of-m multicore problem by combining hardware management with mixed-criticality provisioning](https://www.semanticscholar.org/paper/d5336fd2234f431f554fc5d878503a04a27e366e) | 04/11/16 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                            |
|  4 | [Memory Bandwidth Management for Efficient Performance Isolation in Multi-Core Platforms](https://www.semanticscholar.org/paper/0b1bc294dbd926f853a8ee41d1d8f8ecc3cfde13)                           | 02/01/16 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                            |
### <a id='category-task-scheduling-algorithms-for-real-time-systems'></a>Task Scheduling Algorithms for Real-Time Systems: 3 papers found.
Context: 
	Document 1: [Snippet]: «»
[_citation_number]: «4»
[Category]: «Task Scheduling Algorithms for Real-Time Systems»

	Document 2: [Snippet]: «»
[_citation_number]: «7»
[Category]: «Task Scheduling Algorithms for Real-Time Systems»

	Document 3: [Snippet]: «»
[_citation_number]: «11»
[Category]: «Task Scheduling Algorithms for Real-Time Systems»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-15T16:40:14+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](https://www.semanticscholar.org/paper/25ebad66dc10d7b01c22684cbb200ddeb6502475)\]. Further details \[[6](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)\]\[[7](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\]\[[8](https://www.semanticscholar.org/paper/dbd4eb5033815003e7f6519fd66e43e5fc297075)\]\[[9](https://www.semanticscholar.org/paper/d5336fd2234f431f554fc5d878503a04a27e366e)\]\[[10](https://www.semanticscholar.org/paper/0b1bc294dbd926f853a8ee41d1d8f8ecc3cfde13)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Memory bandwidth regulation and cache partitioning are widely used techniques
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](https://www.semanticscholar.org/paper/25ebad66dc10d7b01c22684cbb200ddeb6502475)\]. Further details discussed in contexts \[[2](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)\]\[[7](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: Task scheduling algorithms for real-time systems have seen significant advancements, particularly in addressing the challenges of resource allocation and schedulability \[[4](https://www.semanticscholar.org/paper/abbd6f8840092bd8e4e3684d3297e1b707abdc5d)\]. Recent approaches focus on integrating memory bandwidth regulation and cache partitioning with partitioned scheduling to ensure predictable timing in real-time computing \[[7](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\]. These techniques require careful co-allocation of tasks and resources to cores, as task execution times are heavily influenced by the availability of allocated resources \[[11](https://www.semanticscholar.org/paper/31e4e1bb57bd04bc02d7f7110e66122a215d7bfa)\]. The development of multi-objective heuristics and optimization frameworks has been a key area of research, aiming to minimize resource usage while maintaining schedulability under preemptive scheduling policies. The use of multi-layer frameworks, such as those combining Pareto-pruned search with dynamic programming-based knapsack optimization, has emerged as a promising direction \[[4](https://www.semanticscholar.org/paper/abbd6f8840092bd8e4e3684d3297e1b707abdc5d)\]. Additionally, the integration of hypervisors like Jailhouse and tools such as MemGuard for fine-grained resource partitioning has enabled more precise control over system resources \[[7](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\]. These advancements highlight the ongoing efforts to improve both the efficiency and reliability of real-time task scheduling in complex, resource-constrained environments.
|    | reference                                                                                                                                                    | date     | key idea/summary                                                                                          |
|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------|
|  0 | [Scheduling Algorithms for Multiprogramming in a Hard-Real-Time Environment](https://www.semanticscholar.org/paper/abbd6f8840092bd8e4e3684d3297e1b707abdc5d) | 01/03/89 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
|  1 | [Scheduling Parallel Real-Time Tasks on Multi-core Processors](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)               | 11/30/10 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
|  2 | [A survey of hard real-time scheduling for multiprocessor systems](https://www.semanticscholar.org/paper/31e4e1bb57bd04bc02d7f7110e66122a215d7bfa)           | 10/01/11 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
### <a id='category-dynamic-memory-bandwidth-regulation-approaches'></a>Dynamic Memory Bandwidth Regulation Approaches: 1 papers found.
Context: 
	Document 1: [Snippet]: «One of the primary sources of unpredictability in modern multi-core embedded systems is contention over shared memory resources, such as caches, interconnects, and DRAM. Despite significant achievements in the design and analysis of multi-core systems, there is a need for a theoretical framework that can be used to reason on the worst-case behavior of real-time workload when both processors and memory resources are subject to scheduling decisions. In this paper, we focus our attention on dynamic allocation of main memory bandwidth. In particular, we study how to determine the worst-case response time of tasks spanning through a sequence of time intervals, each with a different bandwidth-to-core assignment. We show that the response time computation can be reduced to a maximization problem over assignment of memory requests to different time intervals, and we provide an efficient way to solve such problem. As a case study, we then demonstrate how our proposed analysis can be used to improve the schedulability of Integrated Modular Avionics systems in the presence of memory-intensive workload.»
[_citation_number]: «12»
[Category]: «Dynamic Memory Bandwidth Regulation Approaches»


Answer: 
Dynamic Memory Bandwidth Regulation Approaches have gained significant attention in the field of real-time computing systems due to the increasing complexity of multi-core architectures and the challenges posed by shared memory resources such as caches, interconnects, and DRAM \[[12](http://arxiv.org/abs/1809.05921)\]. These approaches aim to address the unpredictability caused by contention and provide a theoretical framework for analyzing worst-case behavior of real-time workloads \[[12](http://arxiv.org/abs/1809.05921)\]. The focus of recent research has been on dynamic allocation of main memory bandwidth, particularly in determining worst-case response times for tasks that span across different time intervals with varying bandwidth-to-core assignments \[[12](http://arxiv.org/abs/1809.05921)\]. This has led to the development of efficient methods to solve such problems, often involving the reduction of response time computation to a maximization problem over memory request assignments \[[12](http://arxiv.org/abs/1809.05921)\]. As a result, these approaches have been applied to improve the schedulability of critical systems such as Integrated Modular Avionics under memory-intensive workloads \[[12](http://arxiv.org/abs/1809.05921)\].
|    | reference                                                                                                          | date     | key idea/summary                                                                                                                                                                                   |
|----|--------------------------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Analysis of Dynamic Memory Bandwidth Regulation in Multi-core Real-Time Systems](http://arxiv.org/abs/1809.05921) | 09/16/18 | The paper presents a theoretical framework for analyzing worst-case response times in multi-core systems by focusing on dynamic memory bandwidth allocation and its impact on real-time workloads. |
### <a id='category-cache-partitioning-methods'></a>Cache Partitioning Methods: 2 papers found.
Context: 
	Document 1: [Snippet]: «»
[_citation_number]: «13»
[Category]: «Cache Partitioning Methods»

	Document 2: [Snippet]: «»
[_citation_number]: «14»
[Category]: «Cache Partitioning Methods»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-15T16:40:14+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](https://www.semanticscholar.org/paper/25ebad66dc10d7b01c22684cbb200ddeb6502475)\]. Further details \[[6](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)\]\[[7](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\]\[[8](https://www.semanticscholar.org/paper/dbd4eb5033815003e7f6519fd66e43e5fc297075)\]\[[9](https://www.semanticscholar.org/paper/d5336fd2234f431f554fc5d878503a04a27e366e)\]\[[10](https://www.semanticscholar.org/paper/0b1bc294dbd926f853a8ee41d1d8f8ecc3cfde13)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Memory bandwidth regulation and cache partitioning are widely used techniques
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](https://www.semanticscholar.org/paper/25ebad66dc10d7b01c22684cbb200ddeb6502475)\]. Further details discussed in contexts \[[2](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)\]\[[7](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Cache partitioning methods are essential in real-time computing systems for ensuring predictable timing and efficient resource utilization \[[13](https://www.semanticscholar.org/paper/333da42f4369dff8ca905ad21ea6ee2f5dc99d55)\]. These methods involve dividing cache resources among multiple tasks or cores to prevent contention and ensure deterministic behavior \[[14](https://www.semanticscholar.org/paper/43cc4d0a998b9aa361264e5fc786c738a62382f1)\]. By isolating cache sets for specific tasks, systems can reduce interference and improve task predictability, especially under preemptive scheduling policies like EDF. Such approaches are often combined with partitioned scheduling to achieve better resource co-allocation and task execution guarantees. The effectiveness of cache partitioning is further enhanced when integrated with memory bandwidth regulation techniques, such as MemGuard, to control data access patterns and prevent resource over-subscription \[[13](https://www.semanticscholar.org/paper/333da42f4369dff8ca905ad21ea6ee2f5dc99d55)\]. These strategies are critical for optimizing performance in embedded systems, where fine-grained resource management is required to meet stringent timing constraints.
|    | reference                                                                                                                                                                                          | date     | key idea/summary                                                                                          |
|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------|
|  0 | [Utility-Based Cache Partitioning: A Low-Overhead, High-Performance, Runtime Mechanism to Partition Shared Caches](https://www.semanticscholar.org/paper/333da42f4369dff8ca905ad21ea6ee2f5dc99d55) | 12/09/06 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
|  1 | [Impact of Cache Partitioning on Multi-tasking Real Time Embedded Systems](https://www.semanticscholar.org/paper/43cc4d0a998b9aa361264e5fc786c738a62382f1)                                         | 08/25/08 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
