## Related Works

Federated unlearning has emerged as a critical research area in the context of privacy-preserving machine learning, particularly in response to the "right to be forgotten" (RTBF) legislation \[[1](https://www.semanticscholar.org/paper/eadeffdec9fac8fd7f9aea732ca410eb082b7dcf)\]. This concept allows users to request the removal of their data from a trained model, a process that is especially challenging in federated learning (FL) due to the decentralized nature of data and model training \[[2](http://arxiv.org/abs/2203.07320)\]. Several recent works have explored methods for achieving this goal, each with varying approaches and trade-offs.

Early efforts in federated unlearning focused on retraining the model from scratch after removing the target data \[[3](https://www.semanticscholar.org/paper/39da2d48f2132b919405e3bb6df6ece44ac6e15a)\]. While effective, this method is computationally expensive and impractical for large-scale systems \[[4](http://arxiv.org/abs/2210.10958)\]. To address this, researchers have proposed alternative strategies, such as leveraging historical parameter updates to reconstruct the unlearned model without full retraining \[[5](https://www.semanticscholar.org/paper/06edb1f6eadb6c141d720fcca4c854578dc5d670)\]. This approach significantly reduces the time required for unlearning while maintaining model efficacy \[[6](http://arxiv.org/abs/2205.12709)\]. For instance, FedEraser \[[7](https://www.semanticscholar.org/paper/a52c3ec7325e81bd87fdf8d74bf9acfd1e1ffe5f)\] introduces a novel calibration method to speed up the reconstruction of the unlearned model using retained updates, achieving a 4× speed-up compared to retraining from scratch.

Another line of work focuses on improving the efficiency and accuracy of unlearning in federated settings. For example, the paper \[[8](http://arxiv.org/abs/2207.05521)\] proposes a method that first performs local unlearning at the client and then uses the locally unlearned model as initialization for a few rounds of federated learning. This approach avoids the need for global access to training data or storage of historical updates, making it more scalable \[[9](http://arxiv.org/abs/2209.02299)\]. Similarly, the work \[[10](https://www.semanticscholar.org/paper/a08f1c5c9f0bdb24f0dc75c0d969eb353899156b)\] introduces a framework that enables the removal of a client's contribution without requiring additional storage, by performing gradient ascent in an orthogonal space formed by other clients' gradients \[[11](https://www.semanticscholar.org/paper/a5f39bcd6198b26997b77233ff81a14e6bc8a32d)\].

In addition to efficiency, verifiability has become an important consideration in federated unlearning. The VeriFi framework \[[12](https://www.semanticscholar.org/paper/efab3b30d6f67f55c68f9dc7c65b2b54b1789030)\] introduces a system that allows users to verify the effectiveness of unlearning, ensuring that the model no longer retains the influence of the removed data \[[13](http://arxiv.org/abs/2110.11794)\]. This is crucial for compliance with privacy regulations, as it provides a mechanism for independently confirming that unlearning has occurred \[[14](http://arxiv.org/abs/2201.09441)\]. Furthermore, the paper \[[15](https://www.semanticscholar.org/paper/70954dd11d1463bc665f803d84b15a4d83805ec0)\] explores the use of differential privacy to ensure that the unlearning process does not introduce new privacy risks, making it suitable for sensitive applications \[[16](http://arxiv.org/abs/2302.12448)\].

Several studies have also examined the challenges of unlearning in the presence of malicious clients or data poisoning attacks. For instance, the work \[[17](https://www.semanticscholar.org/paper/4e26fc4fe687c7471e44f2a5e6feef0facfc4be1)\] investigates how unlearning can be used to remove backdoors from federated models, ensuring that the model does not retain harmful patterns \[[18](http://arxiv.org/abs/2304.10638)\]. Additionally, the paper \[[19](https://www.semanticscholar.org/paper/eff2be3b3ccfb1fc0650432b9b611ebd11ba0feb)\] proposes a method that decouples the unlearning and training processes, enabling efficient and accurate removal of specific data points or clients \[[20](http://arxiv.org/abs/1912.04977)\].

In summary, federated unlearning remains an active and evolving research area, with ongoing efforts to improve efficiency, accuracy, and verifiability. These advancements are essential for ensuring compliance with privacy regulations and maintaining trust in federated learning systems.

### References

1. \[[2](http://arxiv.org/abs/2203.07320)\]  
2. \[[3](https://www.semanticscholar.org/paper/39da2d48f2132b919405e3bb6df6ece44ac6e15a)\]  
3. \[[4](http://arxiv.org/abs/2210.10958)\]  
4. \[[5](https://www.semanticscholar.org/paper/06edb1f6eadb6c141d720fcca4c854578dc5d670)\]  
5. \[[6](http://arxiv.org/abs/2205.12709)\]  
6. \[[7](https://www.semanticscholar.org/paper/a52c3ec7325e81bd87fdf8d74bf9acfd1e1ffe5f)\]  
7. \[[8](http://arxiv.org/abs/2207.05521)\]  
8. \[[9](http://arxiv.org/abs/2209.02299)\]  
9. \[[10](https://www.semanticscholar.org/paper/a08f1c5c9f0bdb24f0dc75c0d969eb353899156b)\]  
10. \[[11](https://www.semanticscholar.org/paper/a5f39bcd6198b26997b77233ff81a14e6bc8a32d)\]  
11. \[[12](https://www.semanticscholar.org/paper/efab3b30d6f67f55c68f9dc7c65b2b54b1789030)\]  
12. \[[13](http://arxiv.org/abs/2110.11794)\]  
13. \[[14](http://arxiv.org/abs/2201.09441)\]  
14. \[[15](https://www.semanticscholar.org/paper/70954dd11d1463bc665f803d84b15a4d83805ec0)\]  
15. \[[16](http://arxiv.org/abs/2302.12448)\]  
16. \[[17](https://www.semanticscholar.org/paper/4e26fc4fe687c7471e44f2a5e6feef0facfc4be1)\]  
17. \[[18](http://arxiv.org/abs/2304.10638)\]  
18. \[[19](https://www.semanticscholar.org/paper/eff2be3b3ccfb1fc0650432b9b611ebd11ba0feb)\]  
19. \[[20](http://arxiv.org/abs/1912.04977)\]
