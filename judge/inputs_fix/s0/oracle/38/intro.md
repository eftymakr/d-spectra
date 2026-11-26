## Related Works

Real-time systems often rely on memory bandwidth regulation and cache partitioning to achieve predictable timing behavior \[[1](http://arxiv.org/abs/2310.02959)\]. These techniques are particularly important in multi-core environments, where task execution times can vary significantly due to resource contention \[[2]()\]. Combined with partitioned scheduling, these methods require careful co-allocation of tasks and resources to cores, as task execution times strongly depend on available allocated resources \[[3]()\]. 

Several studies have explored the co-optimization of cache partitioning and task scheduling. For instance, \[[1](http://arxiv.org/abs/2310.02959)\] proposes a hybrid multi-layer design space exploration technique to co-optimize cache partitioning and task allocation, improving the real-time schedulability of NP-FP task sets by an average of 15.2%. This work systematically interleaves three optimization layers: (i) a breadth-first search with proactive pruning for cache partitioning, (ii) a first-fit heuristic for task allocation, and (iii) a recurrence relation for schedulability analysis. The framework also supports different scheduling policies, such as NP-EDF and P-EDF, by plugging in appropriate analysis methods \[[1](http://arxiv.org/abs/2310.02959)\].

In addition to cache partitioning, memory bandwidth reservation systems like MemGuard have been developed to ensure fair and predictable resource usage in multi-core platforms \[[8]()\]. MemGuard enables fine-grained resource partitioning, which is crucial for real-time systems where timing predictability is essential \[[18]()\]. Similarly, the Resource Director Technology (RDT) provides mechanisms for managing and monitoring memory bandwidth, supporting both static and dynamic resource allocation \[[12]()\].

The importance of task clustering in improving schedulability has also been studied. For example, \[[1](http://arxiv.org/abs/2310.02959)\] found that clustering similar-period or mutually compatible tasks often leads to higher schedulability than clustering by cache sensitivity. This insight is valuable for designing efficient task allocation strategies in multi-core real-time systems.

Recent work on holistic resource allocation for multicore real-time systems \[[11]()\] emphasizes the need for integrated approaches that consider both cache and memory bandwidth constraints. This aligns with the proposed 0-1 linear program in the current work, which aims to co-optimize task-resource allocation under a preemptive EDF scheduling policy \[[1](http://arxiv.org/abs/2310.02959)\].

Furthermore, the use of heuristic-based approaches for multi-objective optimization has been explored. For instance, \[[22]()\] presents an interference-aware allocation algorithm that minimizes resource contention while ensuring schedulability. Such methods are complementary to the multi-layer framework proposed in this work, which combines Pareto-pruned search with dynamic programming for knapsack optimization \[[1](http://arxiv.org/abs/2310.02959)\].

In summary, the current work builds upon existing techniques in real-time systems, including cache partitioning, memory bandwidth regulation, and task scheduling, to propose a novel approach for co-allocation of tasks and resources. These techniques have been extensively studied and refined in prior work, providing a solid foundation for the proposed solution.

1. \[[1](http://arxiv.org/abs/2310.02959)\] Co-Optimizing Cache Partitioning and Multi-Core Task Scheduling: Exploit Cache Sensitivity or Not?  
2. \[[2]()\] Impact of cache partitioning on multi-tasking real time embedded systems  
3. \[[3]()\] Evaluation of Cache Partitioning for Hard Real-Time Systems  
4. \[[8]()\] MemGuard: Memory bandwidth reservation system for efficient performance isolation in multi-core platforms  
5. \[[11]()\] Holistic resource allocation for multicore real-time systems  
6. \[[12]()\] A Closer Look at Intel Resource Director Technology (RDT)  
7. \[[18]()\] Dynamic memory bandwidth allocation for real-time GPU-based SoC platforms  
8. \[[22]()\] $IA^3$: An Interference Aware Allocation Algorithm for Multicore Hard Real-Time Systems
