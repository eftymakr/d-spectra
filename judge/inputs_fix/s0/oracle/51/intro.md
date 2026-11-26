## Related Works

Federated Online Learning to Rank (FOLTR) has emerged as a privacy-preserving approach to ranking tasks, where models are trained across decentralized data sources without sharing raw user data \[[10](http://arxiv.org/abs/2401.13410)\]. This paradigm aligns with increasing data privacy concerns and regulatory frameworks such as the General Data Protection Regulation (GDPR), which introduces the "right to be forgotten" \[[10](http://arxiv.org/abs/2401.13410)\]. This right necessitates that users can request the removal of their data contributions from learned models, prompting the development of unlearning methods in federated learning \[[6](http://arxiv.org/abs/2203.07320)\]. 

Unlearning in federated settings is particularly challenging due to the distributed nature of training, where each client trains a local model on their private data and only shares model updates with a central server \[[3](http://arxiv.org/abs/2307.01565)\]. Existing unlearning methods often rely on retraining the global model from scratch or require access to historical parameter updates \[[7](http://arxiv.org/abs/2207.05521)\]. However, these approaches are computationally expensive and may not be feasible in real-time or resource-constrained environments \[[8](http://arxiv.org/abs/2210.10958)\]. 

Recent work has explored efficient unlearning strategies that eliminate a client's contribution without retraining the entire model. For example, \[[7](http://arxiv.org/abs/2207.05521)\] proposes a method that performs local unlearning at the client level and uses the locally unlearned model as initialization for a few rounds of federated learning. This approach avoids the need for global access to data or stored parameter updates, making it more practical for deployment. Similarly, \[[8](http://arxiv.org/abs/2210.10958)\] introduces a method for federated recommendation systems that enables users to remove their contributions by rolling back historical parameter updates and recalibrating the model. This method is inspired by transaction rollback mechanisms in database systems and is designed to be efficient on resource-constrained devices \[[8](http://arxiv.org/abs/2210.10958)\].

In the context of FOLTR, \[[10](http://arxiv.org/abs/2401.13410)\] investigates the effectiveness of unlearning strategies that remove a client's contribution without compromising the global ranker's performance. The paper introduces a method where the client performs a poisoning attack to measure the impact of its contribution, and the unlearning process is evaluated by checking if the attack's effect is reduced \[[10](http://arxiv.org/abs/2401.13410)\]. This approach allows for a verifiable assessment of unlearning success without retraining from scratch \[[10](http://arxiv.org/abs/2401.13410)\].

Additionally, \[[3](http://arxiv.org/abs/2307.01565)\] discusses the challenges of non-IID data in federated learning and how it affects the performance of FOLTR systems. Non-IID data distributions can lead to biased model updates and degrade the effectiveness of federated learning approaches \[[3](http://arxiv.org/abs/2307.01565)\]. This highlights the importance of robust unlearning methods that can handle such data distribution challenges \[[3](http://arxiv.org/abs/2307.01565)\].

Finally, \[[9](http://arxiv.org/abs/2302.02069)\] explores the integration of knowledge distillation and cognitive neuroscience principles to enable unlearning in federated knowledge graph embedding tasks. This work demonstrates that unlearning can be achieved by erasing specific knowledge from local clients and propagating the changes to the global model through knowledge distillation \[[9](http://arxiv.org/abs/2302.02069)\].

In summary, recent efforts in unlearning for federated learning have focused on improving efficiency and verifiability, with applications in various domains including recommendation systems and knowledge graph embeddings. These methods aim to balance data privacy with system performance while adhering to regulatory requirements \[[6](http://arxiv.org/abs/2203.07320)\]\[[7](http://arxiv.org/abs/2207.05521)\]\[[8](http://arxiv.org/abs/2210.10958)\]\[[9](http://arxiv.org/abs/2302.02069)\]\[[10](http://arxiv.org/abs/2401.13410)\].

### References

1. \[[1](http://arxiv.org/abs/1809.08415)\] http://arxiv.org/abs/1809.08415  
2. \[[2](http://arxiv.org/abs/2204.09272)\] http://arxiv.org/abs/2204.09272  
3. \[[3](http://arxiv.org/abs/2307.01565)\] http://arxiv.org/abs/2307.01565  
4. \[[4](http://arxiv.org/abs/2201.06658)\] http://arxiv.org/abs/2201.06658  
5. \[[5](http://arxiv.org/abs/2201.09441)\] http://arxiv.org/abs/2201.09441  
6. \[[6](http://arxiv.org/abs/2203.07320)\] http://arxiv.org/abs/2203.07320  
7. \[[7](http://arxiv.org/abs/2207.05521)\] http://arxiv.org/abs/2207.05521  
8. \[[8](http://arxiv.org/abs/2210.10958)\] http://arxiv.org/abs/2210.10958  
9. \[[9](http://arxiv.org/abs/2302.02069)\] http://arxiv.org/abs/2302.02069  
10. \[[10](http://arxiv.org/abs/2401.13410)\] http://arxiv.org/abs/2401.13410
