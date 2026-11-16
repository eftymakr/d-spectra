## Related Works

Memory bandwidth regulation and cache partitioning have been widely studied as techniques to achieve predictable timing in real-time computing systems \[[12](http://arxiv.org/abs/1809.05921)\]. These approaches are often combined with partitioned scheduling to ensure that task execution times are tightly controlled by the allocated resources \[[12](http://arxiv.org/abs/1809.05921)\]. Prior work has explored various methods for managing shared memory resources, including memory bandwidth reservation systems such as MemGuard \[[2](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)\], which aim to provide efficient performance isolation in multi-core platforms \[[2](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)\]. Similarly, PALLOC \[[6](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)\] introduces a DRAM bank-aware memory allocator that enhances performance isolation by managing memory access patterns across cores.

Cache partitioning has also been extensively investigated as a means to improve predictability in multi-core real-time systems. For instance, utility-based cache partitioning \[[13](https://www.semanticscholar.org/paper/333da42f4369dff8ca905ad21ea6ee2f5dc99d55)\] provides a low-overhead, high-performance runtime mechanism for partitioning shared caches, allowing for dynamic allocation of cache resources. This approach is particularly relevant in systems where multiple tasks with varying memory access patterns coexist \[[13](https://www.semanticscholar.org/paper/333da42f4369dff8ca905ad21ea6ee2f5dc99d55)\]. Additionally, the impact of cache partitioning on multi-tasking real-time embedded systems has been studied, highlighting the importance of fine-grained control over cache resources to reduce interference \[[14](https://www.semanticscholar.org/paper/43cc4d0a998b9aa361264e5fc786c738a62382f1)\].

In the context of scheduling, several studies have focused on scheduling algorithms for multiprogramming in hard real-time environments \[[4](https://www.semanticscholar.org/paper/abbd6f8840092bd8e4e3684d3297e1b707abdc5d)\]. These algorithms aim to ensure that tasks meet their deadlines despite the unpredictable nature of shared hardware resources. Furthermore, the scheduling of parallel real-time tasks on multi-core processors has been addressed, emphasizing the need for efficient resource allocation strategies to minimize interference and improve predictability \[[7](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\].

A key challenge in multi-core real-time systems is the unpredictability caused by memory interference, particularly in commercial-off-the-shelf (COTS) platforms \[[5](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)\]. This interference arises from contention over shared DRAM resources such as memory banks, buses, and memory controllers. To address this, techniques have been proposed to bound memory interference delays, providing tight upper bounds on worst-case performance \[[5](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)\]. These methods involve modeling the timing characteristics of shared memory resources and analyzing their impact on task execution \[[5](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b)\].

Recent work has also explored dynamic memory bandwidth regulation as a means to improve schedulability in real-time systems \[[12](http://arxiv.org/abs/1809.05921)\]. This approach involves dynamically allocating memory bandwidth to cores based on workload characteristics, allowing for more flexible and efficient resource management. The proposed analysis reduces the response time computation to a maximization problem over time intervals with different bandwidth-to-core assignments \[[12](http://arxiv.org/abs/1809.05921)\]. This method has been applied to improve the schedulability of integrated modular avionics systems under memory-intensive
## Research papers
### Outline
- [Cache Partitioning Methods [3 papers]](#category-cache-partitioning-methods)
- [Performance Isolation Mechanisms [5 papers]](#category-performance-isolation-mechanisms)
- [Optimization Frameworks for Real-Time Systems [1 papers]](#category-optimization-frameworks-for-real-time-systems)
- [Partitioned Scheduling Algorithms [1 papers]](#category-partitioned-scheduling-algorithms)
- [Memory Interference Analysis [1 papers]](#category-memory-interference-analysis)
- [Multi-Core Real-Time Scheduling Challenges [2 papers]](#category-multi-core-real-time-scheduling-challenges)
- [Dynamic Resource Allocation Strategies [1 papers]](#category-dynamic-resource-allocation-strategies)

### <a id='category-cache-partitioning-methods'></a>Cache Partitioning Methods: 3 papers found.
Context: 
	Document 1: [Snippet]: «»
[Category]: «Cache Partitioning Methods»
[_citation_number]: «1»

	Document 2: [Snippet]: «»
[Category]: «Cache Partitioning Methods»
[_citation_number]: «13»

	Document 3: [Snippet]: «»
[Category]: «Cache Partitioning Methods»
[_citation_number]: «14»


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
the benchmarking results show that the proposed 0-1 linear program
|    | reference                                                                                                                                                                                          | date     | key idea/summary                                                                                          |
|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------|
|  0 | [A Coordinated Approach for Practical OS-Level Cache Management in Multi-core Real-Time Systems](https://www.semanticscholar.org/paper/50d359dc737cb5c296b527f4eb1541dc55f3ed86)                   | 07/09/13 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
|  1 | [Utility-Based Cache Partitioning: A Low-Overhead, High-Performance, Runtime Mechanism to Partition Shared Caches](https://www.semanticscholar.org/paper/333da42f4369dff8ca905ad21ea6ee2f5dc99d55) | 12/09/06 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
|  2 | [Impact of Cache Partitioning on Multi-tasking Real Time Embedded Systems](https://www.semanticscholar.org/paper/43cc4d0a998b9aa361264e5fc786c738a62382f1)                                         | 08/25/08 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
### <a id='category-performance-isolation-mechanisms'></a>Performance Isolation Mechanisms: 5 papers found.
Context: 
	Document 3: [Snippet]: «Consolidating hard real-time systems onto modern multi-core Systems-on-Chip (SoC) is an open challenge. The extensive sharing of hardware resources at the memory hierarchy raises important unpredictability concerns. The problem is exacerbated as more computationally demanding workload is expected to be handled with real-time guarantees in next-generation Cyber-Physical Systems (CPS). A large body of works has approached the problem by proposing novel hardware redesigns, and by proposing software-only solutions to mitigate performance interference.Strong from the observation that unpredictability arises from a lack of fine-grained control over the behavior of shared hardware components, we outline a promising new resource management approach. We demonstrate that it is possible to introduce Programmable Logic In-the-Middle (PLIM) between a traditional multi-core processor and main memory. This provides the unique capability of manipulating individual memory transactions. We propose a proof-of-concept system implementation of PLIM modules on a commercial multi-core SoC. The PLIM approach is then leveraged to solve long-standing issues with cache coloring. Thanks to PLIM, colored sparse addresses can be re-compacted in main memory. This is the base principle behind the technique we call Cache Bleaching. We evaluate our design on real applications and propose hypervisor-level adaptations to showcase the potential of the PLIM approach.»
[Category]: «Performance Isolation Mechanisms»
[_citation_number]: «8»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-15T16:40:14+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](https://www.semanticscholar.org/paper/25ebad66dc10d7b01c22684cbb200ddeb6502475)\]. Further details \[[6](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)\]\[[7](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\]\[[8](https://www.semanticscholar.org/paper/dbd4eb5033815003e7f6519fd66e43e5fc297075)\]\[[9](https://www.semanticscholar.org/paper/d5336fd2234f431f554fc5d878503a04a27e366e)\]\[[10](https://www.semanticscholar.org/paper/0b1bc294dbd926f853a8ee41d1d8f8ecc3cfde13)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Memory bandwidth regulation and cache partitioning are widely used techniques
for achieving predictable timing in real-time computing systems. Combined with
partitioned scheduling
|    | reference                                                                                                                                                                                           | date     | key idea/summary                                                                                                                                                                                                                                                                                  |
|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [MemGuard: Memory bandwidth reservation system for efficient performance isolation in multi-core platforms](https://www.semanticscholar.org/paper/bbebaeb1b00fdcde2aeb192543835d3ec1518f8d)         | 04/09/13 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                         |
|  1 | [PALLOC: DRAM bank-aware memory allocator for performance isolation on multicore platforms](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)                         | 04/15/14 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                         |
|  2 | [The Potential of Programmable Logic in the Middle: Cache Bleaching](https://www.semanticscholar.org/paper/dbd4eb5033815003e7f6519fd66e43e5fc297075)                                                | 04/01/20 | The paper introduces a novel resource management approach called Programmable Logic In-the-Middle (PLIM) to address unpredictability in multi-core systems by enabling fine-grained control over memory transactions, leading to a technique called Cache Bleaching for improving cache coloring. |
|  3 | [Attacking the one-out-of-m multicore problem by combining hardware management with mixed-criticality provisioning](https://www.semanticscholar.org/paper/d5336fd2234f431f554fc5d878503a04a27e366e) | 04/11/16 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                         |
|  4 | [Memory Bandwidth Management for Efficient Performance Isolation in Multi-Core Platforms](https://www.semanticscholar.org/paper/0b1bc294dbd926f853a8ee41d1d8f8ecc3cfde13)                           | 02/01/16 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                         |
### <a id='category-optimization-frameworks-for-real-time-systems'></a>Optimization Frameworks for Real-Time Systems: 1 papers found.
Context: 
	Document 1: [Snippet]: «»
[Category]: «Optimization Frameworks for Real-Time Systems»
[_citation_number]: «3»


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
co-allocation algorithm in
|    | reference                                                                                                                                           | date     | key idea/summary                                                                                          |
|----|-----------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------|
|  0 | [Real-time cache management framework for multi-core architectures](https://www.semanticscholar.org/paper/25ebad66dc10d7b01c22684cbb200ddeb6502475) | 04/09/13 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
### <a id='category-partitioned-scheduling-algorithms'></a>Partitioned Scheduling Algorithms: 1 papers found.
Context: 
	Document 1: [Snippet]: «»
[Category]: «Partitioned Scheduling Algorithms»
[_citation_number]: «4»


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
co-allocation algorithm in terms of sched
|    | reference                                                                                                                                                    | date     | key idea/summary                                                                                          |
|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------|
|  0 | [Scheduling Algorithms for Multiprogramming in a Hard-Real-Time Environment](https://www.semanticscholar.org/paper/abbd6f8840092bd8e4e3684d3297e1b707abdc5d) | 01/03/89 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
### <a id='category-memory-interference-analysis'></a>Memory Interference Analysis: 1 papers found.
Context: 
	Document 1: [Snippet]: «In commercial-off-the-shelf (COTS) multi-core systems, a task running on one core can be delayed by other tasks running simultaneously on other cores due to interference in the shared DRAM main memory. Such memory interference delay can be large and highly variable, thereby posing a significant challenge for the design of predictable real-time systems. In this paper, we present techniques to provide a tight upper bound on the worst-case memory interference in a COTS-based multi-core system. We explicitly model the major resources in the DRAM system, including banks, buses and the memory controller. By considering their timing characteristics, we analyze the worst-case memory interference delay imposed on a task by other tasks running in parallel. To the best of our knowledge, this is the first work bounding the request re-ordering effect of COTS memory controllers. Our work also enables the quantification of the extent by which memory interference can be reduced by partitioning DRAM banks. We evaluate our approach on a commodity multi-core platform running Linux/RK. Experimental results show that our approach provides an upper bound very close to our measured worst-case interference.»
[Category]: «Memory Interference Analysis»
[_citation_number]: «5»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-15T16:40:14+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](https://www.semanticscholar.org/paper/25ebad66dc10d7b01c22684cbb200ddeb6502475)\]. Further details \[[6](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)\]\[[7](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\]\[[8](https://www.semanticscholar.org/paper/dbd4eb5033815003e7f6519fd66e43e5fc297075)\]\[[9](https://www.semanticscholar.org/paper/d5336fd2234f431f554fc5d878503a04a27e366e)\]\[[10](https://www.semanticscholar.org/paper/0b1bc294dbd926f853a8ee41d1d8f8ecc3cfde13)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Memory bandwidth regulation and cache partitioning are widely used techniques
for achieving predictable timing in real-time computing systems. Combined with
partitioned scheduling, these methods require careful co-allocation of tasks
and resources to cores, as task execution times strongly depend on available
allocated resources. To address this challenge, this paper presents a 0
|    | reference                                                                                                                                             | date     | key idea/summary                                                                                                                                                                                                     |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Bounding memory interference delay in COTS-based multi-core systems](https://www.semanticscholar.org/paper/afca4afaaaa543a1da02b266e9b2ac46eb94793b) | 04/15/14 | This paper presents techniques to provide a tight upper bound on the worst-case memory interference in COTS multi-core systems by modeling DRAM resources and analyzing interference delay caused by parallel tasks. |
### <a id='category-multi-core-real-time-scheduling-challenges'></a>Multi-Core Real-Time Scheduling Challenges: 2 papers found.
Context: 
	Document 1: [Snippet]: «»
[Category]: «Multi-Core Real-Time Scheduling Challenges»
[_citation_number]: «7»

	Document 2: [Snippet]: «»
[Category]: «Multi-Core Real-Time Scheduling Challenges»
[_citation_number]: «11»


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
same time limit.
|    | reference                                                                                                                                          | date     | key idea/summary                                                                                          |
|----|----------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------|
|  0 | [Scheduling Parallel Real-Time Tasks on Multi-core Processors](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)     | 11/30/10 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
|  1 | [A survey of hard real-time scheduling for multiprocessor systems](https://www.semanticscholar.org/paper/31e4e1bb57bd04bc02d7f7110e66122a215d7bfa) | 10/01/11 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
### <a id='category-dynamic-resource-allocation-strategies'></a>Dynamic Resource Allocation Strategies: 1 papers found.
Context: 
	Document 1: [Snippet]: «One of the primary sources of unpredictability in modern multi-core embedded systems is contention over shared memory resources, such as caches, interconnects, and DRAM. Despite significant achievements in the design and analysis of multi-core systems, there is a need for a theoretical framework that can be used to reason on the worst-case behavior of real-time workload when both processors and memory resources are subject to scheduling decisions. In this paper, we focus our attention on dynamic allocation of main memory bandwidth. In particular, we study how to determine the worst-case response time of tasks spanning through a sequence of time intervals, each with a different bandwidth-to-core assignment. We show that the response time computation can be reduced to a maximization problem over assignment of memory requests to different time intervals, and we provide an efficient way to solve such problem. As a case study, we then demonstrate how our proposed analysis can be used to improve the schedulability of Integrated Modular Avionics systems in the presence of memory-intensive workload.»
[Category]: «Dynamic Resource Allocation Strategies»
[_citation_number]: «12»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-15T16:40:14+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](https://www.semanticscholar.org/paper/25ebad66dc10d7b01c22684cbb200ddeb6502475)\]. Further details \[[6](https://www.semanticscholar.org/paper/6e925ae85e385ac0e8810441d84be97c079f6b22)\]\[[7](https://www.semanticscholar.org/paper/cf5b78d3e292fda8f6a8aa132da468f6d8e6a730)\]\[[8](https://www.semanticscholar.org/paper/dbd4eb5033815003e7f6519fd66e43e5fc297075)\]\[[9](https://www.semanticscholar.org/paper/d5336fd2234f431f554fc5d878503a04a27e366e)\]\[[10](https://www.semanticscholar.org/paper/0b1bc294dbd926f853a8ee41d1d8f8ecc3cfde13)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Memory bandwidth regulation and cache partitioning are widely used techniques
for achieving predictable timing in real-time computing systems. Combined with
partitioned scheduling, these methods require careful co-allocation of tasks
and resources to cores, as task execution times strongly depend on available
allocated resources. To address this challenge, this paper presents a 0-1
linear program for task-resource co-allocation, along with a multi-objective
heuristic designed
|    | reference                                                                                                          | date     | key idea/summary                                                                                                                                                                                   |
|----|--------------------------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Analysis of Dynamic Memory Bandwidth Regulation in Multi-core Real-Time Systems](http://arxiv.org/abs/1809.05921) | 09/16/18 | The paper presents a theoretical framework for analyzing worst-case response times in multi-core systems by focusing on dynamic memory bandwidth allocation and its impact on real-time workloads. |
