## Related Works

Federated Learning (FL) has emerged as a promising paradigm for training machine learning models on decentralized data while preserving privacy \[[4](http://arxiv.org/abs/1912.04977)\]. In FL, a central server coordinates the training of a global model using updates from multiple clients, each holding their own private data \[[2](http://arxiv.org/abs/1610.05492)\]. This approach is particularly useful in scenarios where data is distributed across mobile devices, IoT devices, or other edge computing environments \[[7](http://arxiv.org/abs/1602.05629)\]. However, FL faces several challenges, including the heterogeneity of client data distributions and the resulting fluctuations in global and local model parameters, which can negatively impact model accuracy \[[12](http://arxiv.org/abs/2102.02079)\].

Several works have addressed these challenges. For instance, FedProx \[[10](http://arxiv.org/abs/1812.06127)\] introduces a framework that generalizes and re-parameterizes FedAvg, allowing for more robust convergence in heterogeneous settings. This method provides convergence guarantees for non-identical data distributions and device-level constraints, making it suitable for real-world FL scenarios. Similarly, SCAFFOLD \[[17](http://arxiv.org/abs/1910.06378)\] introduces a new algorithm that uses control variates to reduce drift between clients, leading to faster convergence and fewer communication rounds. These methods highlight the importance of addressing client heterogeneity in FL.

The issue of non-IID data distribution has also been extensively studied. The work by \[[13](http://arxiv.org/abs/1806.00582)\] shows that non-IID data significantly reduces the accuracy of FL models, with some cases experiencing up to a 55% drop. To mitigate this, they propose a strategy of sharing a small subset of data globally, which can improve accuracy by up to 30%. This underscores the need for more effective strategies to handle non-IID data in FL. Additionally, \[[12](http://arxiv.org/abs/2102.02079)\] conducts an experimental study on federated learning under non-IID data settings, revealing that no existing algorithm outperforms others in all cases, emphasizing the need for further research.

To enhance personalization in FL, \[[11](http://arxiv.org/abs/1909.12488)\] explores the use of Model Agnostic Meta Learning (MAML), suggesting that FL can be viewed as a natural application of MAML. They argue that Federated Averaging, a popular FL algorithm, can be interpreted as a meta-learning algorithm, and that careful fine-tuning can lead to more personalized models. This work highlights the potential of meta-learning techniques in improving FL performance.

Furthermore, \[[16](http://arxiv.org/abs/2102.07078)\] proposes a framework for personalized federated learning, where a shared representation is learned across clients, and each client has a unique local head. This approach leverages distributed computational power to perform local updates efficiently, leading to linear convergence and improved performance on heterogeneous data. These methods demonstrate the potential of personalized FL approaches in addressing the challenges of data heterogeneity.

In summary, while existing FL methods have made significant strides, they still face challenges related to data heterogeneity, communication efficiency, and personalization. The proposed CHASe method aims to address these issues by focusing on identifying high-epistemic variation samples and improving data selection efficiency \[[1](http://arxiv.org/abs/1812.01097)\]. 

References:  
\[[1](http://arxiv.org/abs/1812.01097)\] http://arxiv.org/abs/2102.07078  
\[[2](http://arxiv.org/abs/1610.05492)\] http://arxiv.org/abs/1610.05492  
\[[4](http://arxiv.org/abs/1912.04977)\] http://arxiv.org/abs/1812.01097  
\[[7](http://arxiv.org/abs/1602.05629)\] http://arxiv.org/abs/1602.05629  
\[[10](http://arxiv.org/abs/1812.06127)\] http://arxiv.org/abs/1812.06127  
\[[11](http://arxiv.org/abs/1909.12488)\] http://arxiv.org/abs/1909.12488  
\[[12](http://arxiv.org/abs/2102.02079)\] http://arxiv.org/abs/2102.02079  
\[[13](http://arxiv.org/abs/1806.00582)\] http://arxiv.org/abs/1806.00582  
\[[16](http://arxiv.org/abs/2102.07078)\] http://arxiv.org/abs/2102.07078  
\[[17](http://arxiv.org/abs/1910.06378)\] http://arxiv.org/abs/1910.06378
