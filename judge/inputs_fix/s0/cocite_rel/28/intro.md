## Related Works

Federated Learning (FL) has emerged as a promising paradigm for collaborative model training while preserving data privacy. FL enables multiple clients to collaboratively train a shared model without sharing raw data, which is particularly useful in scenarios where data is distributed across devices or organizations \[[2](http://arxiv.org/abs/1912.04977)\]. However, FL faces significant challenges due to the heterogeneity of data distributions across clients and the associated fluctuations in global and local model parameters, which can degrade model accuracy \[[14](http://arxiv.org/abs/1806.00582)\]. This issue is further exacerbated by the non-IID (non-independent and identically distributed) nature of data in federated settings, which is a common scenario in real-world applications \[[13](http://arxiv.org/abs/2102.02079)\].

Several works have addressed the statistical heterogeneity in FL. For instance, FedProx was introduced to handle both statistical and system heterogeneity by generalizing FedAvg and allowing for variable workloads on each device \[[12](http://arxiv.org/abs/1812.06127)\]. Similarly, the paper on clustered FL (CFL) proposed a framework that groups clients based on their data distribution to improve model performance without modifying the FL communication protocol \[[4](http://arxiv.org/abs/1910.01991)\]. This approach leverages geometric properties of the loss surface to form clusters, allowing for more specialized models while maintaining privacy \[[4](http://arxiv.org/abs/1910.01991)\].

In addition to addressing data heterogeneity, there has been growing interest in personalized federated learning, where the goal is to adapt models to individual clients while maintaining a shared global model \[[10](http://arxiv.org/abs/2002.07948)\]. This is achieved through meta-learning techniques that allow clients to fine-tune the global model with their local data \[[10](http://arxiv.org/abs/2002.07948)\]. Another approach, FedMatch, tackles the problem of semi-supervised learning in FL by introducing an inter-client consistency loss and decomposing parameters into labeled and unlabeled components \[[11](http://arxiv.org/abs/2006.12097)\]. These methods demonstrate the importance of adapting models to local data while preserving the benefits of FL.

Efforts have also been made to improve communication efficiency in FL, which is crucial for mobile and edge devices with limited bandwidth \[[3](http://arxiv.org/abs/1610.05492)\]. Techniques such as structured and sketched updates have been proposed to reduce the communication cost by compressing model updates before transmission \[[3](http://arxiv.org/abs/1610.05492)\]. Furthermore, adaptive client sampling algorithms have been developed to mitigate the impact of system and statistical heterogeneity, leading to faster convergence \[[7](http://arxiv.org/abs/2112.11256)\].

In summary, existing FL methods have made significant strides in addressing data heterogeneity, communication efficiency, and personalization. However, they often fail to account for the dynamic nature of model parameters and the impact of epistemic uncertainty during active learning, which is a critical aspect of the proposed CHASe framework \[[1](http://arxiv.org/abs/1812.01097)\]. Future work should focus on integrating these advancements into more robust and efficient FL systems.

References:
\[[1](http://arxiv.org/abs/1812.01097)\] http://arxiv.org/abs/2106.05001
\[[2](http://arxiv.org/abs/1912.04977)\] http://arxiv.org/abs/1912.04977
\[[3](http://arxiv.org/abs/1610.05492)\] http://arxiv.org/abs/1610.05492
\[[4](http://arxiv.org/abs/1910.01991)\] http://arxiv.org/abs/1910.01991
\[[7](http://arxiv.org/abs/2112.11256)\] http://arxiv.org/abs/2112.11256
\[[10](http://arxiv.org/abs/2002.07948)\] http://arxiv.org/abs/2002.07948
\[[11](http://arxiv.org/abs/2006.12097)\] http://arxiv.org/abs/2006.12097
\[[12](http://arxiv.org/abs/1812.06127)\] http://arxiv.org/abs/1812.06127
\[[13](http://arxiv.org/abs/2102.02079)\] http://arxiv.org/abs/2102.02079
\[[14](http://arxiv.org/abs/1806.00582)\] http://arxiv.org/abs/1806.00582
