## Related Works

Modern databases often adopt weak isolation levels to achieve high throughput and partition tolerance, sacrificing strong transactional guarantees for performance \[[1]()\]. This trade-off has led to the emergence of isolation bugs in production systems, where databases fail to uphold their data-consistency contracts \[[1]()\]. Black-box testing has become a critical technique for detecting such bugs by verifying whether transactional histories adhere to prescribed isolation levels \[[1]()\]. 

The complexity of isolation testing has been a subject of extensive study. While testing strong isolation levels, such as serializability, is known to be NP-complete \[[2](http://arxiv.org/abs/1908.04509)\], recent research has shown that weak isolation levels, including Read Committed (RC), Read Atomic (RA), and Causal Consistency (CC), can be tested in polynomial time \[[2](http://arxiv.org/abs/1908.04509)\]. This has enabled the development of scalable testing tools, although existing testers often suffer from high polynomial complexity, limiting their applicability to moderate-sized workloads \[[1]()\]. 

Several works have explored the verification of weak isolation levels. For instance, PolySI is a black-box checker designed to efficiently verify Snapshot Isolation (SI) in databases, demonstrating its ability to reproduce known anomalies and detect novel violations in production cloud databases \[[3](http://arxiv.org/abs/2301.07313)\]. Similarly, Viper is a fast SI checker that leverages efficient algorithms to validate SI properties \[[13]()\]. These tools highlight the importance of efficient verification techniques for weak isolation levels. 

The complexity of checking transactional consistency has also been investigated. For example, it has been shown that consistency models like RC, RA, and causal consistency are polynomial time checkable, while prefix consistency and SI are NP-complete \[[2](http://arxiv.org/abs/1908.04509)\]. This complexity classification has informed the design of algorithms that can handle large-scale workloads under certain parameterized constraints \[[2](http://arxiv.org/abs/1908.04509)\]. 

In the context of memory models, the problem of consistency testing has been studied extensively. For instance, it has been shown that the problem of checking whether an execution is consistent with a memory model remains NP-complete even in bounded settings \[[5](http://arxiv.org/abs/2311.04302)\]. This highlights the inherent difficulty of verifying consistency across various models, including C11-style memory models \[[6](http://arxiv.org/abs/2304.03714)\]. 

Efforts to improve the efficiency of consistency checking have led to the development of algorithms that provide nearly-linear-time performance for certain variants of memory models \[[6](http://arxiv.org/abs/2304.03714)\]. These advancements have been implemented in tools like TruSt and C11Tester, demonstrating significant improvements in consistency checking \[[6](http://arxiv.org/abs/2304.03714)\]. 

In summary, the landscape of isolation testing and consistency verification is rich and evolving, with ongoing efforts to improve efficiency and scalability. The development of AWDIT represents a significant step forward, offering a provably optimal tester for weak isolation levels with improved performance over existing tools \[[1]()\]. 

References:  
\[[1]()\] A Critique of ANSI SQL Isolation Levels  
\[[2](http://arxiv.org/abs/1908.04509)\] On the Complexity of Checking Transactional Consistency  
\[[3](http://arxiv.org/abs/2301.07313)\] Efficient Black-box Checking of Snapshot Isolation in Databases  
\[[5](http://arxiv.org/abs/2311.04302)\] How Hard is Weak-Memory Testing?  
\[[6](http://arxiv.org/abs/2304.03714)\] Optimal Reads-From Consistency Checking for C11-Style Memory Models
