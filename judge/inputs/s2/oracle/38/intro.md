## Related Works

Real-time systems often rely on memory bandwidth regulation and cache partitioning to achieve predictable timing behavior \[[1](http://arxiv.org/abs/2310.02959)\]. These techniques are particularly important in multi-core environments, where task execution times can vary significantly due to resource contention \[[2]()\]. Combined with partitioned scheduling, these methods require careful co-allocation of tasks and resources to cores, as task execution times strongly depend on available allocated resources \[[3]()\]. 

Several studies have explored the co-optimization of cache partitioning and task scheduling. For instance, \[[1](http://arxiv.org/abs/2310.02959)\] proposes a hybrid multi-layer design space exploration technique to co-optimize cache partitioning and task allocation, improving the real-time schedulability of NP-FP task sets by an average of 15.2%. This work systematically interleaves three optimization layers: breadth-first search for cache partitioning, first-fit heuristic for task allocation, and recurrence relations for schedulability analysis \[[1](http://arxiv.org/abs/2310.02959)\]. Furthermore, the framework supports various scheduling policies, including NP-EDF and P-EDF, by plugging in appropriate analysis methods \[[1](http://arxiv.org/abs/2310.02959)\]. 

In addition, \[[14]()\] evaluates cache partitioning for hard real-time systems, highlighting its effectiveness in improving schedulability. Similarly, \[[15]()\] investigates the impact of cache partitioning on multi-tasking real-time embedded systems, demonstrating that it can significantly enhance system performance. \[[16]()\] further explores minimizing cache usage for real-time systems, emphasizing the trade-offs between performance and resource utilization. 

The use of memory bandwidth reservation systems, such as MemGuard \[[8]()\], has also been explored to ensure predictable performance in multi-core platforms. These systems help isolate memory bandwidth, which is critical for real-time applications. \[[18]()\] extends this idea by proposing dynamic memory bandwidth allocation for real-time GPU-based SoC platforms, demonstrating the importance of adaptive resource management. 

Recent work has also focused on holistic resource allocation strategies. For example, \[[11]()\] presents a holistic approach for multicore real-time systems, integrating cache partitioning, memory bandwidth regulation, and task scheduling. \[[23]()\] further extends this by addressing multi-resource allocation under federated scheduling for parallel real-time tasks. 

In the context of mixed-criticality systems, \[[20]()\] examines the trade-offs between cache sharing and isolation, highlighting the need for flexible resource management. \[[22]()\] introduces an interference-aware allocation algorithm for multicore hard real-time systems, which aims to reduce resource contention and improve schedulability. 

Finally, \[[21]()\] proposes a period-driven task and cache
