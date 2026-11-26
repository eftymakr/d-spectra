## Related Works

Federated unlearning has emerged as a critical research area in the context of privacy-preserving machine learning, particularly in response to the "right to be forgotten" (RTBF) legislation \[[1](http://arxiv.org/abs/2203.07320)\]. This concept allows users to request the removal of their data from a trained model, a necessity in distributed learning frameworks like Federated Learning (FL) \[[2](http://arxiv.org/abs/2310.20448)\]. Early works focused on centralized unlearning, where full access to training data is available for the server to conduct the unlearning process \[[3](https://www.semanticscholar.org/paper/eadeffdec9fac8fd7f9aea732ca410eb082b7dcf)\]. However, FL introduces unique challenges due to the decentralized nature of data and the lack of global access to training data \[[4](http://arxiv.org/abs/2207.05521)\].

Several studies have explored unlearning in FL by proposing methods that either retrain the model from scratch or use historical parameter updates to reconstruct the unlearned model \[[5](http://arxiv.org/abs/2205.12709)\]. For instance, FedEraser leverages the historical parameter updates stored at the central server to efficiently reconstruct the unlearned model, achieving a 4× speed-up compared to retraining from scratch \[[6](https://www.semanticscholar.org/paper/06edb1f6eadb6c141d720fcca4c854578dc5d670)\]. Similarly, the paper "Federated Unlearning: How to Efficiently Erase a Client in FL?" proposes a two-step approach: local unlearning at the client and then a few rounds of federated learning with the remaining clients to obtain the unlearned global model \[[7](https://www.semanticscholar.org/paper/39da2d48f2132b919405e3bb6df6ece44ac6e15a)\].

The importance of verifiable unlearning has also been emphasized, as unlearning itself may not be sufficient without independent verification \[[8](http://arxiv.org/abs/2210.10958)\]. VeriFi introduces a framework that enables users to verify the unlearning effect through marking and checking mechanisms, ensuring the unlearning process is both effective and transparent \[[9](https://www.semanticscholar.org/paper/a52c3ec7325e81bd87fdf8d74bf9acfd1e1ffe5f)\]. Additionally, the paper "Communication Efficient and Provable Federated Unlearning" introduces a framework that guarantees the unlearned model is statistically indistinguishable from the one trained without the deleted data, ensuring both efficiency and accuracy \[[10](http://arxiv.org/abs/2209.02299)\].

Privacy-preserving techniques have also been explored, such as the use of differential privacy in FedRecovery to ensure the unlearned model and retrained model are statistically indistinguishable \[[11](http://arxiv.org/abs/2401.11018)\]. Furthermore, the paper "Federated Unlearning with Knowledge Distillation" proposes a method that leverages knowledge distillation to restore model performance without requiring any data from the clients \[[12](http://arxiv.org/abs/2401.05146)\].

In addition to these methods, recent works have focused on improving the efficiency and effectiveness of unlearning in FL by addressing specific challenges such as data poisoning and backdoor attacks \[[13](https://www.semanticscholar.org/paper/efab3b30d6f67f55c68f9dc7c65b2b54b1789030)\]. For example, the paper "Get Rid of Your Trail: Remotely Erasing Backdoors in Federated Learning" proposes a method that enables adversaries to remove backdoors from the centralized model while preserving model performance \[[14](https://www.semanticscholar.org/paper/eff2be3b3ccfb1fc0650432b9b611ebd11ba0feb)\].

The need for robust and efficient unlearning strategies has also been highlighted in the context of federated recommendation systems, where the ability to remove a user's contribution is essential for compliance with data protection regulations \[[15](https://www.semanticscholar.org/paper/a5f39bcd6198b26997b77233ff81a14e6bc8a32d)\]. The paper "Federated Unlearning for On-Device Recommendation" proposes an efficient unlearning method inspired by transaction rollback mechanisms, allowing for the removal of a user's contribution by rolling back and calibrating historical parameter updates \[[16](http://arxiv.org/abs/2201.09441)\].

Finally, the paper "Incentive and Dynamic Client Selection for Federated Unlearning" addresses the issue of incentivizing valuable users to remain engaged and preventing their data from being unlearned, highlighting the importance of designing mechanisms that balance data privacy and system performance \[[17](http://arxiv.org/abs/2302.12448)\].

1. \[[1](http://arxiv.org/abs/2203.07320)\] http://arxiv.org/abs/2203.07320  
2. \[[2](http://arxiv.org/abs/2310.20448)\] http://arxiv.org/abs/2310.20448  
3. \[[3](https://www.semanticscholar.org/paper/eadeffdec9fac8fd7f9aea732ca410eb082b7dcf)\] http://arxiv.org/abs/2207.05521  
4. \[[4](http://arxiv.org/abs/2207.05521)\] http://arxiv.org/abs/2205.12709  
5. \[[5](http://arxiv.org/abs/2205.12709)\] http://arxiv.org/abs/2203.07320  
6. \[[6](https://www.semanticscholar.org/paper/06edb1f6eadb6c141d720fcca4c854578dc5d670)\] https://www.semanticscholar.org/paper/eadeffdec9fac8fd7f9aea732ca410eb082b7dcf  
7. \[[7](https://www.semanticscholar.org/paper/39da2d48f2132b919405e3bb6df6ece44ac6e15a)\] http://arxiv.org/abs/2207.05521  
8. \[[8](http://arxiv.org/abs/2210.10958)\] http://arxiv.org/abs/2205.12709  
9. \[[9](https://www.semanticscholar.org/paper/a52c3ec7325e81bd87fdf8d74bf9acfd1e1ffe5f)\] http://arxiv.org/abs/2205.12709  
10. \[[10](http://arxiv.org/abs/2209.02299)\] http://arxiv.org/abs/2401.11018  
11. \[[11](http://arxiv.org/abs/2401.11018)\] https://www.semanticscholar.org/paper/06edb1f6eadb6c141d720fcca4c854578dc5d670  
12. \[[12](http://arxiv.org/abs/2401.05146)\] http://arxiv.org/abs/2201.09441  
13. \[[13](https://www.semanticscholar.org/paper/efab3b30d6f67f55c68f9dc7c65b2b54b1789030)\] http://arxiv.org/abs/2304.10638  
14. \[[14](https://www.semanticscholar.org/paper/eff2be3b3ccfb1fc0650432b9b611ebd11ba0feb)\] http://arxiv.org/abs/2304.10638  
15. \[[15](https://www.semanticscholar.org/paper/a5f39bcd6198b26997b77233ff81a14e6bc8a32d)\] http://arxiv.org/abs/2210.10958  
16. \[[16](http://arxiv.org/abs/2201.09441)\] http://arxiv.org/abs/2210.10958  
17. \[[17](http://arxiv.org/abs/2302.12448)\] https://www.semanticscholar.org/paper/6556402fc6d6a1ebcbf82eed07c64d89dd40f786
