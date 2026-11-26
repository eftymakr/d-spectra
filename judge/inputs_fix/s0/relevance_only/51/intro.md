## Related Works

Federated unlearning has emerged as a critical research area in response to the "right to be forgotten" legislation, which mandates that users can request the removal of their data from machine learning models \[[1](http://arxiv.org/abs/2412.19069)\]. This has spurred the development of unlearning techniques that aim to remove the influence of specific data points or clients from federated learning (FL) models without requiring full retraining \[[2](http://arxiv.org/abs/2401.05146)\]. In the context of Federated Online Learning to Rank (FOLTR), where ranking models are continuously updated using implicit user feedback, the need for efficient and verifiable unlearning strategies is particularly pressing \[[3](http://arxiv.org/abs/2310.20448)\]. 

Several approaches have been proposed to address federated unlearning. FedEraser \[[4](http://arxiv.org/abs/2310.19218)\] was one of the first methods to enable efficient client-level data removal by leveraging historical parameter updates and calibrating them to reconstruct the unlearned model. This method significantly reduces the time required for unlearning compared to retraining from scratch, achieving a 4× speed-up on realistic datasets. Similarly, Ferrari \[[5](http://arxiv.org/abs/2406.03078)\] introduces a framework for federated feature unlearning, minimizing feature sensitivity to ensure that sensitive or biased features are effectively removed. This approach is grounded in Lipschitz continuity and is evaluated across various feature unlearning scenarios.

In the realm of federated recommendation systems, FRU \[[6](http://arxiv.org/abs/2403.02437)\] proposes an efficient unlearning method inspired by transactional rollback mechanisms. It enables the removal of a user's contribution by rolling back and calibrating historical parameter updates, which is particularly useful in privacy-sensitive applications. The method also introduces a small-sized negative sampling technique to reduce the storage burden on resource-constrained devices.

The importance of verifiable unlearning has also been emphasized, as unlearning itself may not be sufficient to implement the right to be forgotten unless the effect can be independently verified \[[7](http://arxiv.org/abs/2210.10958)\]. VeriFi \[[8](http://arxiv.org/abs/2308.12502)\] introduces a framework that allows for systematic analysis of federated unlearning and quantification of its effect, incorporating both unlearning and verification methods. This work demonstrates that unlearning verification is particularly challenging in FL due to the potential for unlearning effects to be canceled by other participants' contributions.

Incentive mechanisms have also been explored to encourage user participation in federated unlearning \[[9](https://www.semanticscholar.org/paper/a52c3ec7325e81bd87fdf8d74bf9acfd1e1ffe5f)\]. These mechanisms aim to retain valuable users by providing them with incentives, thereby improving the performance of the unlearned model. The proposed methods reduce server costs by up to 53.91% compared to state-of-the-art benchmarks.

Efforts have also focused on improving the efficiency and accuracy of unlearning in FL. FedRecovery \[[10](https://www.semanticscholar.org/paper/39da2d48f2132b919405e3bb6df6ece44ac6e15a)\] introduces a differentially private machine unlearning algorithm that removes the impact of a client by adjusting gradient residuals and adding Gaussian noise to ensure statistical indistinguishability between the unlearned and retrained models. This method does not require retraining-based fine-tuning or convexity assumptions, making it suitable for complex models like neural networks.

In summary, while many methods have been proposed for federated unlearning, there remains a need for more rigorous evaluation frameworks and verifiable mechanisms to ensure the effectiveness and privacy of unlearning processes in FL systems.

References:
1. \[[1](http://arxiv.org/abs/2412.19069)\] [http://arxiv.org/abs/2401.05146]
2. \[[2](http://arxiv.org/abs/2401.05146)\] [http://arxiv.org/abs/2403.02437]
3. \[[3](http://arxiv.org/abs/2310.20448)\] [http://arxiv.org/abs/2412.19069]
4. \[[4](http://arxiv.org/abs/2310.19218)\] [http://arxiv.org/abs/2210.10958]
5. \[[5](http://arxiv.org/abs/2406.03078)\] [http://arxiv.org/abs/2201.09441]
6. \[[6](http://arxiv.org/abs/2403.02437)\] [http://arxiv.org/abs/2210.10958]
7. \[[7](http://arxiv.org/abs/2210.10958)\] [https://www.semanticscholar.org/paper/a52c3ec7325e81bd87fdf8d74bf9acfd1e1ffe5f]
8. \[[8](http://arxiv.org/abs/2308.12502)\] [http://arxiv.org/abs/2205.12709]
9. \[[9](https://www.semanticscholar.org/paper/a52c3ec7325e81bd87fdf8d74bf9acfd1e1ffe5f)\] [https://www.semanticscholar.org/paper/a08f1c5c9f0bdb24f0dc75c0d969eb353899156b]
10. \[[10](https://www.semanticscholar.org/paper/39da2d48f2132b919405e3bb6df6ece44ac6e15a)\] [https://www.semanticscholar.org/paper/06edb1f6eadb6c141d720fcca4c854578dc5d670]
