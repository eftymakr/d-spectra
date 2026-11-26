## Related Works

Federated unlearning has emerged as a critical research area in response to the "right to be forgotten" legislation, which mandates that users can request the removal of their data from machine learning models \[[1](http://arxiv.org/abs/2203.07320)\]. This has spurred the development of various unlearning methods aimed at efficiently removing the influence of specific data points or clients from a global model without requiring full retraining \[[2](https://www.semanticscholar.org/paper/eadeffdec9fac8fd7f9aea732ca410eb082b7dcf)\]. Early approaches focused on centralized settings, where the server had access to all training data, but these methods are not directly applicable to federated learning (FL) due to the decentralized nature of data \[[3](http://arxiv.org/abs/2310.20448)\]. 

In the context of FL, several studies have proposed techniques to enable efficient data removal. For instance, FedEraser introduces a method that leverages historical parameter updates retained by the central server to reconstruct an unlearned model, significantly reducing the time required compared to retraining from scratch \[[4](http://arxiv.org/abs/2207.05521)\]. Similarly, the paper titled *Federated Unlearning: How to Efficiently Erase a Client in FL?* proposes a two-step approach: local unlearning at the client level followed by a few rounds of federated learning with the remaining clients to obtain the unlearned global model \[[5](http://arxiv.org/abs/2201.09441)\]. This method avoids the need for storing historical updates or retraining from scratch, making it more efficient \[[6](https://www.semanticscholar.org/paper/39da2d48f2132b919405e3bb6df6ece44ac6e15a)\].

Another notable work, *Federated Unlearning with Knowledge Distillation*, introduces a method that subtracts accumulated historical updates from the model and uses knowledge distillation to restore model performance without relying on client data \[[7](https://www.semanticscholar.org/paper/06edb1f6eadb6c141d720fcca4c854578dc5d670)\]. This approach is particularly useful in scenarios where client participation is limited or where data access is restricted \[[8](http://arxiv.org/abs/2205.12709)\]. Additionally, *Communication Efficient and Provable Federated Unlearning* presents a framework that ensures exact unlearning and communication efficiency, with theoretical guarantees for the statistical indistinguishability of the unlearned model from the one trained without the deleted data \[[9](http://arxiv.org/abs/2209.02299)\].

The importance of verifiable unlearning has also been highlighted, with *VeriFi* introducing a framework that allows users to independently verify the effectiveness of unlearning by marking and checking the global model's performance on specific fingerprints \[[10](http://arxiv.org/abs/2401.05146)\]. This addresses a critical gap in current unlearning methods, where verification of the unlearning effect is often overlooked \[[11](https://www.semanticscholar.org/paper/a52c3ec7325e81bd87fdf8d74bf9acfd1e1ffe5f)\]. Furthermore, *Federated Unlearning via Class-Discriminative Pruning* explores selective forgetting of categories by pruning channels with high discriminative power, achieving significant speedups compared to retraining from scratch \[[12](http://arxiv.org/abs/2210.10958)\].

Lastly, *Advances and Open Problems in Federated Learning* provides a broad overview of FL, emphasizing the need for mechanisms that support the right to be forgotten and the challenges associated with implementing such mechanisms in distributed settings \[[13](http://arxiv.org/abs/2110.11794)\]. These studies collectively highlight the growing interest in federated unlearning and the need for robust, efficient, and verifiable methods to support data privacy in FL systems.

1. \[[1](http://arxiv.org/abs/2203.07320)\] \[[1](http://arxiv.org/abs/2203.07320)\]  
2. \[[2](https://www.semanticscholar.org/paper/eadeffdec9fac8fd7f9aea732ca410eb082b7dcf)\]  
3. \[[3](http://arxiv.org/abs/2310.20448)\]  
4. \[[4](http://arxiv.org/abs/2207.05521)\]  
5. \[[5](http://arxiv.org/abs/2201.09441)\]  
6. \[[6](https://www.semanticscholar.org/paper/39da2d48f2132b919405e3bb6df6ece44ac6e15a)\]  
7. \[[7](https://www.semanticscholar.org/paper/06edb1f6eadb6c141d720fcca4c854578dc5d670)\]  
8. \[[8](http://arxiv.org/abs/2205.12709)\]  
9. \[[9](http://arxiv.org/abs/2209.02299)\]  
10. \[[10](http://arxiv.org/abs/2401.05146)\]  
11. \[[11](https://www.semanticscholar.org/paper/a52c3ec7325e81bd87fdf8d74bf9acfd1e1ffe5f)\]  
12. \[[12](http://arxiv.org/abs/2210.10958)\]  
13. \[[13](http://arxiv.org/abs/2110.11794)\]
