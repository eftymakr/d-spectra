## Related Works

Differential privacy (DP) has become the de facto standard for achieving privacy in data analysis \[[20](https://www.semanticscholar.org/paper/e4ce10063cd25447dcde75c2d9ce327446ced952)\]. However, its implementation is vulnerable to malicious behaviors by servers, especially in distributed settings \[[1](http://arxiv.org/abs/1811.12469)\]. For instance, servers may sample noise from incorrect distributions or generate correlated noise while appearing to follow established protocols \[[1](http://arxiv.org/abs/1811.12469)\]. This issue has been explored in several works that examine the robustness of DP mechanisms against adversarial manipulation \[[3](http://arxiv.org/abs/1909.09630)\]. 

In the local differential privacy (LDP) model, each user perturbs their data locally before sending it to an untrusted data collector \[[14](http://arxiv.org/abs/1606.05053)\]. While LDP provides strong privacy guarantees, it is vulnerable to manipulation attacks where a small fraction of users can obscure the distribution of honest users' inputs \[[3](http://arxiv.org/abs/1909.09630)\]. This vulnerability has led to the development of countermeasures such as verifiable randomization mechanisms that allow the data collector to verify the completeness of the randomization process \[[4](http://arxiv.org/abs/2104.06569)\]. These mechanisms prevent malicious data providers from manipulating their output before sending it to the collector \[[4](http://arxiv.org/abs/2104.06569)\].

Several studies have focused on improving the utility of LDP protocols while ensuring robustness against adversarial attacks. For example, the paper \[[6](http://arxiv.org/abs/1905.08320)\] discusses the use of frequency oracle (FO) protocols to estimate frequencies of values, and shows that adding post-processing steps can significantly improve accuracy. Similarly, \[[7](https://www.semanticscholar.org/paper/25b7fe2ac81189952c72c5b869a6be1c5fcf410c)\] introduces PrivKV, a system for key-value data collection under LDP, which improves estimation accuracy through iterative refinement. These works highlight the ongoing efforts to enhance both the utility and robustness of LDP protocols.

The shuffled model of differential privacy, which lies between the local and central models, has also been explored as a way to achieve the accuracy of the central model without requiring a trusted server \[[17](http://arxiv.org/abs/1808.01394)\]. This model introduces an anonymous channel that randomly permutes user-supplied messages, enabling more accurate statistical analysis while preserving privacy. This approach has been shown to provide the power of the central model while avoiding the need to trust a central server \[[17](http://arxiv.org/abs/1808.01394)\].

In addition to these technical contributions, there have been studies that examine the broader implications of DP in real-world applications. For example, \[[18](http://arxiv.org/abs/2005.11753)\] discusses the challenges of publishing streaming data under both centralized and local DP, emphasizing the need for efficient noise calibration techniques to maintain utility. These studies underscore the importance of balancing privacy guarantees with the practicality of deploying DP mechanisms in real-world systems.

In summary, the related works highlight the challenges and opportunities in implementing DP in distributed settings, with a focus on improving robustness against adversarial manipulation and enhancing the utility of privacy-preserving mechanisms. These contributions form the foundation for the proposed Verifiable Distributed Differential Privacy (VDDP) framework \[[1](http://arxiv.org/abs/1811.12469)\]. 

References:  
\[[1](http://arxiv.org/abs/1811.12469)\] http://arxiv.org/abs/2005.11753  
\[[3](http://arxiv.org/abs/1909.09630)\] http://arxiv.org/abs/1909.09630  
\[[4](http://arxiv.org/abs/2104.06569)\] http://arxiv.org/abs/2104.06569  
\[[6](http://arxiv.org/abs/1905.08320)\] http://arxiv.org/abs/1905.08320  
\[[7](https://www.semanticscholar.org/paper/25b7fe2ac81189952c72c5b869a6be1c5fcf410c)\] https://www.semanticscholar.org/paper/25b7fe2ac81189952c72c5b869a6be1c5fcf410c  
\[[17](http://arxiv.org/abs/1808.01394)\] http://arxiv.org/abs/1808.01394  
\[[18](http://arxiv.org/abs/2005.11753)\] http://arxi.org/abs/2005.11753
