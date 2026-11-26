## Related Works

Serverless computing has emerged as a transformative paradigm in cloud computing, offering automatic scaling, efficient resource utilization, and cost-effective pricing models \[[16](http://arxiv.org/abs/1911.01296)\]. However, a significant challenge persists in the form of cold-start latency, which introduces delays during the initialization of function containers and negatively impacts end-to-end performance \[[16](http://arxiv.org/abs/1911.01296)\]. Several studies have explored strategies to mitigate this issue, ranging from optimizing container pre-warming to reducing initialization overhead through code-level optimizations.

Early work on cold starts focused on reducing the time required to launch new function instances. For instance, the *Adaptive Warm-Up Strategy (AWUS)* \[[3](https://www.semanticscholar.org/paper/81b8db7a20f1aa859143c716b38a1443e3eca9a0)\] predicts function invocation times and pre-warms containers to reduce cold start latency. Similarly, *Adaptive Container Pool Scaling Strategy (ACPSS)* \[[3](https://www.semanticscholar.org/paper/81b8db7a20f1aa859143c716b38a1443e3eca9a0)\] dynamically adjusts container pool capacity to minimize resource waste. These approaches aim to balance latency reduction with resource efficiency, but they often rely on static or fixed policies that may not adapt well to varying workloads.

More recent approaches leverage machine learning and reinforcement learning to better predict and manage cold starts. *WLEC* \[[10](https://www.semanticscholar.org/paper/fde534d033dea54e1b9066bad32d7330febe54f3)\] introduces a container management architecture that uses a modified S2LRU structure to minimize cold start time, achieving up to 31% average reduction in cold start duration. *FaaSLight* \[[6](http://arxiv.org/abs/2207.08175)\] focuses on application-level optimizations, such as loading only necessary code, to reduce cold-start latency by up to 78.95%. This approach is platform- and language-agnostic, making it broadly applicable to different serverless environments.

Another line of research explores the use of snapshots and prebaking techniques to accelerate function startup. *Prebaking Functions to Warm the Serverless Cold Start* \[[9](https://www.semanticscholar.org/paper/ab1c0062964a2df3d7f8d11da4a774530286b801)\] restores snapshots from previously executed function processes, improving startup times by up to 71% for certain workloads. This technique, based on the CRIU tool, demonstrates the potential of state restoration to reduce cold start overhead.

Additionally, *FaasCache* \[[14](https://www.semanticscholar.org/paper/3c05fec4087d94c61233a482e59b613388b2c3ae)\] introduces a caching-inspired keep-alive policy that maintains functions in a warm state, reducing cold start overhead by more than 3× compared to current approaches. This method leverages caching principles such as reuse distances and hit-ratio curves to optimize both keep-alive and resource provisioning, leading to a 30% reduction in resource requirements for real-world workloads.

The *Catalyzer* system \[[1](https://www.semanticscholar.org/paper/f14446970a5ed7145a6d350e1aff07ca203cece8)\] takes a novel approach by restoring virtualization-based function instances from checkpoint images, effectively eliminating the initialization step. This results in sub-millisecond startup latencies, significantly outperforming traditional methods. The system also introduces a new OS primitive, *sfork*, to further reduce startup latency by reusing the state of running sandbox instances.

In contrast to these methods, the proposed *SLIMSTART* tool \[[17](https://www.semanticscholar.org/paper/36338d869d7589b01c3707d70bece8c320e439e2)\] focuses on identifying and mitigating inefficient library usage patterns in serverless applications. By leveraging statistical sampling and call-path profiling, it collects runtime library usage data and applies automated code transformations to reduce cold-start overhead. This approach is particularly effective in eliminating unnecessary initialization of rarely used libraries, which is a common source of inefficiency in serverless environments.

In summary, while many existing approaches focus on reducing cold start latency through container pre-warming, resource scaling, or state restoration, *SLIMSTART* introduces a profile-guided optimization tool that addresses the root cause of inefficiencies in serverless function initialization. This approach not only reduces initialization and end-to-end latency but also optimizes memory usage, demonstrating its effectiveness in improving the overall performance of serverless applications.

References:
1. Catalyzer: Sub-millisecond Startup for Serverless Computing with Initialization-less Booting
2. Cold Start in Serverless Computing: Current Trends and Mitigation Strategies
3. Adaptive Function Launching Acceleration in Serverless Computing Platforms
4. A Reinforcement Learning Approach to Reduce Serverless Function Cold Start Frequency
5. Mitigating Cold-Start Delay using Warm-Start Containers in Serverless Platform
6. FaaSLight: General Application-level Cold-start Latency Optimization for Function-as-a-Service in Serverless Computing
7. Serverless in the Wild: Characterizing and Optimizing the Serverless Workload at a Large Cloud Provider
8. Agile Cold Starts for Scalable Serverless
9. Prebaking Functions to Warm the Serverless Cold Start
10. WLEC: A Not So Cold Architecture to Mitigate Cold Start Problem in Serverless Computing
11. Using application knowledge to reduce cold starts in FaaS services
12. Mitigating Cold Start Problem in Serverless Computing: A Reinforcement Learning Approach
13. Xanadu: Mitigating cascading cold starts in serverless function chain deployments
14. FaasCache: keeping serverless computing alive with greedy-dual caching
15. SAND: Towards High-Performance Serverless Computing
16. Serverless Computing: A Survey of Opportunities, Challenges, and Applications
17. Mitigating Cold Start Problem in Serverless Computing with Function Fusion
