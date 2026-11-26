## Related Works

Federated learning (FL) has emerged as a promising paradigm for training machine learning models on decentralized data while preserving privacy \[[2](http://arxiv.org/abs/1912.04977)\]. It enables multiple clients to collaboratively train a model without sharing raw data, with a central server aggregating model updates \[[2](http://arxiv.org/abs/1912.04977)\]. However, FL faces significant challenges due to the heterogeneity of client data distributions and communication constraints \[[8](http://arxiv.org/abs/1812.06127)\]. This section reviews related works that address these challenges, particularly those focusing on communication efficiency, data heterogeneity, and model personalization.

Early works in FL, such as FedAvg, assume that data across clients is independently and identically distributed (IID), which is often not the case in real-world scenarios \[[6](http://arxiv.org/abs/1806.00582)\]. Non-IID data can lead to significant accuracy degradation, as demonstrated in experiments where accuracy reduced by up to 55% for neural networks trained on highly skewed data \[[6](http://arxiv.org/abs/1806.00582)\]. To address this, researchers have proposed strategies such as creating a small subset of globally shared data to improve training performance \[[6](http://arxiv.org/abs/1806.00582)\]. Additionally, FedProx was introduced to handle statistical and system heterogeneity by allowing devices to perform variable amounts of work and improving convergence behavior in non-IID settings \[[8](http://arxiv.org/abs/1812.06127)\].

Communication efficiency is another critical challenge in FL, especially for mobile devices with limited bandwidth \[[3](http://arxiv.org/abs/1610.05492)\]. Techniques such as structured and sketched updates have been proposed to reduce uplink communication costs by compressing model updates before sending them to the server \[[3](http://arxiv.org/abs/1610.05492)\]. Adaptive optimization methods, including FedAdam and FedYogi, have also been introduced to improve performance in heterogeneous settings by adjusting learning rates dynamically \[[4](http://arxiv.org/abs/2003.00295)\].

Model personalization has gained attention as a way to address the limitations of a single global model in FL. FedPer introduces a base + personalization layer approach, allowing clients to learn personalized models while maintaining a shared global model \[[17](http://arxiv.org/abs/1912.00818)\]. Similarly, pFedMe uses Moreau envelopes to decouple personalized model optimization from global learning, achieving state-of-the-art convergence rates \[[19](http://arxiv.org/abs/2006.08848)\]. These approaches demonstrate the importance of personalization in improving model performance on heterogeneous data.

In addition to these, clustered FL (CFL) has been proposed to group clients with similar data distributions, enabling more efficient and accurate model training \[[5](http://arxiv.org/abs/1910.01991)\]. This approach does not require modifications to the FL communication protocol and can be applied to nonconvex objectives, such as deep neural networks \[[5](http://arxiv.org/abs/1910.01991)\]. Furthermore, client selection strategies, such as Power-of-Choice, have been introduced to improve convergence speed by biasing selection towards clients with higher local loss \[[15](http://arxiv.org/abs/2010.01243)\].

The concept of federated active learning (FAL), which combines active learning with FL, has also been explored to reduce annotation costs while preserving data privacy \[[1](http://arxiv.org/abs/1812.01097)\]. CHASe, the proposed method in this paper, builds upon these prior works by addressing the challenges of client heterogeneity and model parameter fluctuations through epistemic variation tracking and decision boundary alignment \[[1](http://arxiv.org/abs/1812.01097)\].

---

**References**  
\[[1](http://arxiv.org/abs/1812.01097)\] http://arxiv.org/abs/1912.01097  
\[[2](http://arxiv.org/abs/1912.04977)\] http://arxiv.org/abs/1912.04977  
\[[3](http://arxiv.org/abs/1610.05492)\] http://arxiv.org/abs/1610.05492  
\[[4](http://arxiv.org/abs/2003.00295)\] http://arxiv.org/abs/2003.00295  
\[[5](http://arxiv.org/abs/1910.01991)\] http://arxiv.org/abs/1910.01991  
\[[6](http://arxiv.org/abs/1806.00582)\] http://arxiv.org/abs/1806.00582  
\[[8](http://arxiv.org/abs/1812.06127)\] http://arxiv.org/abs/1812.06127  
\[[15](http://arxiv.org/abs/2010.01243)\] http://arxiv.org/abs/2010.01243  
\[[17](http://arxiv.org/abs/1912.00818)\] http://arxiv.org/abs/1912.00818  
\[[19](http://arxiv.org/abs/2006.08848)\] http://arxiv.org/abs/2006.08848
