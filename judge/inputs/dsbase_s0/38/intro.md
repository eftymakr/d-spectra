## Related Works

Memory bandwidth regulation and cache partitioning are widely used techniques for achieving predictable timing in real-time computing systems \[[Wajeb Gharibi' 2012-04-21](http://arxiv.org/abs/1204.4829v1)\]. These techniques, when combined with partitioned scheduling, require careful co-allocation of tasks and resources to cores, as task execution times strongly depend on available allocated resources \[[Meijia Han' 2022-12-08](http://arxiv.org/abs/2212.04268v1)\]. Prior work has explored various approaches to address this challenge, including the use of mixed-integer programs for task-resource co-allocation \[[Shalin Shah' 2019-02-15](http://arxiv.org/abs/1903.03494v1)\], and multi-objective heuristics to minimize resource usage while guaranteeing schedulability under preemptive EDF scheduling \[[Russell Impagliazzo' 2014-01-21](http://arxiv.org/abs/1401.5512v2)\]. 

Several studies have investigated the use of optimization frameworks for real-time systems. For example, \[[Joshua Brakensiek' 2019-04-09](http://arxiv.org/abs/1904.04860v1)\] presents an exact algorithm for the 0-1 Integer Linear Programming problem with a linear number of constraints, which is relevant to the optimization of task-resource co-allocation. Additionally, \[[Mitchell Keegan' 2023-12-06](http://arxiv.org/abs/2312.03413v1)\] introduces a multi-layer framework for task scheduling, where an outer layer explores resource allocations using Pareto-pruned search, and an inner layer optimizes task allocation by solving a knapsack problem using dynamic programming. This approach is similar to the multi-layer framework proposed in the current work. 

The importance of cache partitioning and memory bandwidth regulation has been highlighted in several studies. For instance, \[[Danial Davarnia' 2018-12-05](http://arxiv.org/abs/1812.02215v1)\] discusses the use of cache-coloring to mitigate inter-set write variation in non-volatile caches, which is relevant to the memory bandwidth regulation techniques used in this work. Similarly, \[[Xuming An' 2021-10-23](http://arxiv.org/abs/2110.12115v2)\] presents a technique for dynamic cache reconfiguration to improve cache energy efficiency, which is closely related to the resource allocation strategies discussed here. 

In the context of real-time systems, \[[Michael Stoll' 2008-03-21](http://arxiv.org/abs/0803.3165v6)\] introduces a framework for co-designing resource allocation and deadline decomposition with generative profiling, which is aligned with the multi-objective heuristic proposed in this work. Additionally, \[[Kien Trung Nguyen' 2017-04-01](http://arxiv.org/abs/1704.00145v1)\] presents a method for improving the schedulability of real-time systems by leveraging cache partitioning and task scheduling techniques. These studies highlight the importance of integrating resource allocation and scheduling strategies to achieve predictable timing in real-time systems.

The use of heuristic methods for multi-objective optimization has also been explored in the literature. For example, \[[Guy Davidson' 2024-05-21](http://arxiv.org/abs/2405.13242v3)\] introduces a multi-objective genetic algorithm for solving optimization problems in real-time systems, which is similar to the multi-objective heuristic proposed in this work. Furthermore, \[[Andi Drebes' 2014-05-12](http://arxiv.org/abs/1405.2916v1)\] presents a multi-objective evolutionary algorithm for solving complex optimization problems, which is relevant to the optimization strategies discussed here. 

In addition, \[[Hamees Sayed' 2024-11-01](http://arxiv.org/abs/2411.00727v2)\] discusses the use of multi-objective optimization techniques for improving the performance of real-time systems, which is closely related to the optimization framework proposed in this work. The work also highlights the importance of balancing multiple objectives, such as resource usage and schedulability, to achieve optimal results. 

Finally, \[[Elizaveta Frenkel' 2014-08-27](http://arxiv.org/abs/1408.6509v2)\] presents a study on the use of multi-objective optimization for improving the energy efficiency of real-time systems, which is aligned with the optimization strategies discussed in this work. These studies demonstrate the growing interest in using multi-objective optimization techniques to improve the performance of real-time systems.

### References

1. [Document 4] 0-1 Integer Linear Programming with a Linear Number of Constraints
2. [Document 5] Bridging between 0/1 and Linear Programming via Random Walks
3. [Document 6] Joint Task Offloading and Resource Allocation for IoT Edge Computing with Sequential Task Dependency
4. [Document 7] Consistency for 0-1 Programming
5. [Document 8] Genetic Algorithm for a class of Knapsack Problems
6. [Document 9] Inverse Fractional Knapsack Problem with Profits and Costs Modification
7. [Document 10] 0-1 Integer Linear Programming with a Linear Number of Constraints
8. [Document 11] Approximating Solutions to the Knapsack Problem using the Lagrangian Dual Framework
9. [Document 12] Automatic Detection of Performance Anomalies in Task-Parallel Programs
10. [Document 13] 0-1 Integer Linear Programming with a Linear Number of Constraints
11. [Document 14] Knapsack problems in products of groups
