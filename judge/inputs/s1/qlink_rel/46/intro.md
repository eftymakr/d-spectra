## Related Works

Cross-domain sequential recommendation (CDSR) has gained significant attention in recent years due to its ability to alleviate data sparsity and cold-start problems in traditional sequential recommendation systems \[[1](http://arxiv.org/abs/2304.03891)\]. Several approaches have been proposed to address these challenges, often leveraging domain-specific information or cross-domain knowledge transfer. For instance, C2DSR \[[1](http://arxiv.org/abs/2304.03891)\] introduces a framework that simultaneously leverages intra- and inter-sequence item relationships to capture precise user preferences across domains. It utilizes graph neural networks to mine collaborative relationships between items and sequential attentive encoders to capture sequential dependencies, followed by a contrastive cross-domain infomax objective to enhance the correlation between single- and cross-domain user representations.

Similarly, the Dual Attentive Sequential Learning (DASL) model \[[2](http://arxiv.org/abs/2106.02768)\] employs a dual learning mechanism to iteratively transfer information between two domains, improving click-through rate (CTR) prediction performance. This model introduces dual embeddings and dual attention mechanisms to jointly establish a two-stage learning process, enhancing cross-domain recommendations by matching latent embeddings with candidate items.

In the context of shared-account cross-domain sequential recommendation (SCSR), DA-GCN \[[3](http://arxiv.org/abs/2105.03300)\] proposes a domain-aware graph convolutional network to learn user-specific node representations, incorporating attention mechanisms to guide message passing and account for domain-specific preferences. This approach effectively handles the challenges of shared accounts and cross-domain interactions.

Self-attentive sequential recommendation models, such as SASRec \[[4](http://arxiv.org/abs/1808.09781)\], have also been explored to capture long-term user preferences by using self-attention mechanisms. These models allow for efficient prediction based on relevant items from a user's action history, outperforming traditional methods like Markov Chains and RNNs.

Recent work on contrastive learning for sequential recommendation \[[5](http://arxiv.org/abs/2311.04590)\] introduces a multi-task framework, CL4SRec, which combines next item prediction with contrastive learning to derive self-supervision signals from user behavior sequences. This approach enhances user representation learning by leveraging both task-specific and contrastive objectives.

The DDTCDR model \[[6](http://arxiv.org/abs/1910.05189)\] employs a dual transfer mechanism to extract user preferences across multiple domains while preserving relations between users in different latent spaces. It integrates autoencoder techniques to extract latent features, achieving significant improvements over existing baselines.

The CoNet model \[[7](http://arxiv.org/abs/1804.06769)\] proposes a collaborative cross network approach using neural networks for cross-domain recommendation, enabling dual knowledge transfer across domains through cross connections and joint loss functions. This model outperforms traditional matrix factorization methods by capturing complex user-item interactions.

DDGHM \[[8](http://arxiv.org/abs/2209.10163)\] introduces a dual dynamic graph with
