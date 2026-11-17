## Related Works

Memory bandwidth regulation and cache partitioning are well-established techniques to ensure predictable timing behavior in real-time systems by mitigating interference among concurrently executing tasks on multi-core processors \[[2310.02959](http://arxiv.org/abs/2310.02959)\]. These techniques must be carefully integrated with partitioned scheduling approaches because task execution times are highly dependent on the amount and type of resources allocated to each core \[[2310.02959](http://arxiv.org/abs/2310.02959)\]. 

Several works have focused on co-optimizing task allocation and resource partitioning to improve system schedulability. Notably, mixed-integer linear programming (MILP) formulations have been proposed for task-resource co-allocation problems, aiming to optimize resource usage while maintaining schedulability guarantees under various scheduling policies . However, MILP solutions often face scalability challenges, motivating heuristic and multi-layer optimization frameworks that balance solution quality and computational efficiency .

The multi-layer framework approach, where an outer layer explores resource allocations and an inner layer performs task allocation, has shown promising results. For example, a hybrid design employing breadth-first search with pruning for cache partitioning, combined with heuristic task allocation and schedulability analysis, significantly improves real-time schedulability for cache-sensitive tasks under non-preemptive fixed-priority scheduling \[[2310.02959](http://arxiv.org/abs/2310.02959)\]. This layered methodology supports flexibility by allowing different scheduling policies (e.g., NP-FP, NP-EDF, P-EDF) to be integrated within the inner optimization layer \[[2310.02959](http://arxiv.org/abs/2310.02959)\]. 

Cache partitioning techniques such as cache coloring and set partitioning are commonly used to reduce cache interference and improve execution time predictability. Studies have demonstrated the benefits of clustering tasks by period or compatibility to enhance schedulability beyond clustering by cache sensitivity alone \[[2310.02959](http://arxiv.org/abs/2310.02959)\]. Moreover, dynamic memory bandwidth regulation strategies like MemGuard have been employed alongside cache partitioning to provide fine-grained control over resource allocation, further enhancing predictability . 

Research also highlights the importance of multi-objective optimization approaches to balance competing goals such as minimizing resource usage and maximizing schedulability. Multi-objective heuristics, including genetic and evolutionary algorithms, have been proposed to efficiently explore the design space and generate a set of Pareto-optimal solutions . These approaches address the complexity of real-time scheduling on multi-core systems with heterogeneous resource constraints and provide more flexible decision-making frameworks compared to single-objective techniques.

In addition, co-design frameworks that integrate resource allocation with deadline decomposition and generative profiling further improve the accuracy of execution time predictions and system schedulability \[[2310.02959](http://arxiv.org/abs/2310.02959)\]. These methods leverage profiling data to guide optimization, ensuring that resource partitioning aligns closely with task timing behavior. 

Overall, the intersection of cache partitioning, memory bandwidth regulation, and task scheduling continues to be a rich area of research. The state-of-the-art emphasizes hybrid optimization frameworks that combine exact methods (e.g., MILP) with heuristics and multi-layer designs to achieve scalable, high-quality solutions suitable for real-time embedded platforms \[[2310.02959](http://arxiv.org/abs/2310.02959)\]. This body of work informs the development of advanced co-allocation algorithms that simultaneously optimize resource usage and system schedulability under realistic multi-core scheduling policies.

### References

\[[2310.02959](http://arxiv.org/abs/2310.02959)\] Co-Optimizing Cache Partitioning and Multi-Core Task Scheduling: Exploit Cache Sensitivity or Not? [http://arxiv.org/abs/2310.02959]  
 CORD: Co-design of Resource Allocation and Deadline Decomposition with Generative Profiling  
 A Polynomial Time Algorithm For 0-1 Integer Linear Programmings  
 Real-Time-Data Analytics in Raw Materials Handling  
 Analysis of Dynamic Memory Bandwidth Regulation in Multi-core Real-Time Systems  
 Exact schedulability test for sporadic mixed-criticality real-time systems using antichains and oracles  
 Energy-Efficient Real-Time Scheduling for Two-Type Heterogeneous Multiprocessors  
 Real-time Inflation Forecasting Using Non-linear Dimension Reduction Techniques  
 Multi-objective evolutionary algorithms for real-time system optimization  
 Multi-objective optimization techniques for improving real-time system performance