## Related Works

Serverless computing has emerged as a transformative paradigm in cloud computing, offering automatic scaling, efficient resource utilization, and cost-effective pricing models \[[1](https://www.semanticscholar.org/paper/d911b03bfda4fc6fc92f8080bb81b3a967d6a9e7)\]. However, the cold-start latency issue remains a significant challenge, adversely affecting end-to-end performance \[[2](http://arxiv.org/abs/2310.08437)\]. Several studies have explored solutions to mitigate this problem. For instance, \[[3](https://www.semanticscholar.org/paper/f14446970a5ed7145a6d350e1aff07ca203cece8)\] highlights that cold starts occur due to the delay in provisioning runtime containers, which is a critical factor in serverless platforms. This delay is exacerbated by the need to initialize containers for each function invocation, which can introduce non-negligible overhead \[[4](https://www.semanticscholar.org/paper/b99668ae35c4b6796b827657a318fe4b84a757ff)\].

To address the cold-start problem, various approaches have been proposed. One common strategy is to maintain a pool of warm containers to reduce the latency associated with cold starts \[[5](https://www.semanticscholar.org/paper/81b8db7a20f1aa859143c716b38a1443e3eca9a0)\]. This approach is widely adopted, as it allows for faster response times by keeping containers ready for immediate use \[[6](https://www.semanticscholar.org/paper/96d4fea8d034a7605af936f2e2b6a44becdf6585)\]. However, maintaining a large pool of warm containers can lead to increased resource consumption, which contradicts the scale-to-zero feature of serverless computing \[[7](https://www.semanticscholar.org/paper/27cd21426fe51167dd6ac79d1c83db55a07a2046)\]. To balance resource usage and performance, \[[8](https://www.semanticscholar.org/paper/c066cf85b94846ddc057a113ce110e045f587375)\] proposes an adaptive model that predicts the optimal length of the idle container window and the number of pre-warmed containers based on historical function invocation patterns. This model uses deep neural networks and LSTM to capture invocation patterns, improving the efficiency of cold-start mitigation \[[9](https://www.semanticscholar.org/paper/d9eaeccc9cca929af052aa362efaf83267daf614)\].

Another approach focuses on reducing the initialization time of containers. \[[10](https://www.semanticscholar.org/paper/fde534d033dea54e1b9066bad32d7330febe54f3)\] introduces a technique that restores function instances from previously executed processes, significantly reducing startup latency. This method leverages snapshot restoration, which can improve function startup times by up to 71% for certain applications \[[11](https://www.semanticscholar.org/paper/fbf4355d06ddb5f6c81e67cffadf57f6939b8940)\]. Similarly, \[[12](https://www.semanticscholar.org/paper/ab1c0062964a2df3d7f8d11da4a774530286b801)\] proposes a system that uses prebaking techniques to warm functions, thereby reducing cold start delays. This approach is particularly effective for applications with predictable workloads \[[13](https://www.semanticscholar.org/paper/891a89fad669dc7d107ad2d5a047b288b5cc9832)\].

In addition to container-level optimizations, application-level strategies have also been explored. \[[14](https://www.semanticscholar.org/paper/1cd137e77753ee6c51c97c520d64f91d484dbddc)\] presents FaaSLight, an application-level optimization tool that reduces cold-start latency by identifying and eliminating unnecessary code loading. This tool uses call-path profiling and statistical sampling to optimize library usage, leading to significant reductions in initialization and end-to-end latency \[[15](http://arxiv.org/abs/2003.03423)\]. The effectiveness of such tools is further validated by \[[16](http://arxiv.org/abs/2207.08175)\], which demonstrates that application-level optimizations can achieve up to a 42.05% reduction in total response latency \[[17](http://arxiv.org/abs/1903.12221)\].

Moreover,  introduces a reinforcement learning-based approach to predict function invocation patterns and pre-warm containers accordingly. This method dynamically adjusts the number of pre-warmed containers based on workload characteristics, leading to improved performance and resource efficiency . Similarly,  proposes a two-layer adaptive approach that combines reinforcement learning with LSTM to predict future function invocations and manage container warm-up strategies .

In summary, while existing works have made significant strides in mitigating cold-start latency, there remains a need for more adaptive and efficient solutions that balance performance with resource consumption. The proposed SLIMSTART tool addresses these challenges by leveraging profile-guided optimization and integration with CI/CD pipelines .

References:
1. \[[1](https://www.semanticscholar.org/paper/d911b03bfda4fc6fc92f8080bb81b3a967d6a9e7)\] [Document 1]
2. \[[2](http://arxiv.org/abs/2310.08437)\] [Document 2]
3. \[[3](https://www.semanticscholar.org/paper/f14446970a5ed7145a6d350e1aff07ca203cece8)\] [Document 3]
4. \[[4](https://www.semanticscholar.org/paper/b99668ae35c4b6796b827657a318fe4b84a757ff)\] [Document 4]
5. \[[5](https://www.semanticscholar.org/paper/81b8db7a20f1aa859143c716b38a1443e3eca9a0)\] [Document 5]
6. \[[6](https://www.semanticscholar.org/paper/96d4fea8d034a7605af936f2e2b6a44becdf6585)\] [Document 6]
7. \[[7](https://www.semanticscholar.org/paper/27cd21426fe51167dd6ac79d1c83db55a07a2046)\] [Document 7]
8. \[[8](https://www.semanticscholar.org/paper/c066cf85b94846ddc057a113ce110e045f587375)\] [Document 8]
9. \[[9](https://www.semanticscholar.org/paper/d9eaeccc9cca929af052aa362efaf83267daf614)\] [Document 9]
10. \[[10](https://www.semanticscholar.org/paper/fde534d033dea54e1b9066bad32d7330febe54f3)\] [Document 10]
11. \[[11](https://www.semanticscholar.org/paper/fbf4355d06ddb5f6c81e67cffadf57f6939b8940)\] [Document 11]
12. \[[12](https://www.semanticscholar.org/paper/ab1c0062964a2df3d7f8d11da4a774530286b801)\] [Document 12]
13. \[[13](https://www.semanticscholar.org/paper/891a89fad669dc7d107ad2d5a047b288b5cc9832)\] [Document 13]
14. \[[14](https://www.semanticscholar.org/paper/1cd137e77753ee6c51c97c520d64f91d484dbddc)\] [Document 14]
15. \[[15](http://arxiv.org/abs/2003.03423)\] [Document 15]
16. \[[16](http://arxiv.org/abs/2207.08175)\] [Document 16]
17. \[[17](http://arxiv.org/abs/1903.12221)\] [Document 17]
18.  [Document 18]
19.  [Document 19]
20.  [Document 20]
21.  [Document 21]
22.  [Document 22]
