## Related Works

Federated unlearning has emerged as a critical research area in the context of privacy-preserving machine learning, particularly in response to the "right to be forgotten" regulation \[[1](http://arxiv.org/abs/2412.19069)\]. This concept allows users to request the removal of their data from the global model trained across distributed clients, without requiring full retraining \[[2](http://arxiv.org/abs/2401.05146)\]. Federated Learning (FL) enables collaborative training of models across multiple parties while preserving data privacy by keeping raw data local \[[3](http://arxiv.org/abs/2310.20448)\]. However, the challenge lies in efficiently and securely unlearning the impact of specific clients or data points from the global model \[[4](http://arxiv.org/abs/2310.19218)\].

Several approaches have been proposed to address federated unlearning. For instance, FedEraser \[[5](http://arxiv.org/abs/2406.03078)\] was the first method to enable efficient data removal from FL models by reconstructing the unlearned model using historical parameter updates stored at the central server. This method significantly reduces the time required to construct the unlearned model compared to retraining from scratch \[[5](http://arxiv.org/abs/2406.03078)\]. Similarly, the work in \[[6](http://arxiv.org/abs/2403.02437)\] introduced a framework for verifiable federated unlearning, where the leaving participant can verify the unlearning effect through a combination of marking and checking steps \[[6](http://arxiv.org/abs/2403.02437)\]. This ensures that the unlearning process is transparent and verifiable, which is crucial for regulatory compliance \[[6](http://arxiv.org/abs/2403.02437)\].

Another significant contribution is the development of unlearning strategies that are both efficient and secure. For example, the paper \[[7](http://arxiv.org/abs/2308.12502)\] proposed a method that allows the server to unlearn a target client without requiring client communication or additional storage, thereby improving efficiency and security \[[7](http://arxiv.org/abs/2308.12502)\]. Additionally, the work in \[[8](http://arxiv.org/abs/2306.02216)\] introduced a novel training and unlearning strategy for deep neural networks, termed forgettable federated linear learning, which enables certified and efficient unlearning \[[8](http://arxiv.org/abs/2306.02216)\]. This approach leverages pretrained models to approximate deep neural networks linearly, allowing for efficient unlearning while maintaining model performance \[[8](http://arxiv.org/abs/2306.02216)\].

The importance of evaluation metrics in federated unlearning has also been emphasized. The paper \[[9](http://arxiv.org/abs/2012.13891)\] introduced a comprehensive framework for evaluating federated unlearning methods, highlighting the trade-offs between privacy, accuracy, and efficiency \[[9](http://arxiv.org/abs/2012.13891)\]. This work also proposed the OPENFEDERATEDUNLEARNING framework, which serves as a benchmark for evaluating federated unlearning methods \[[9](http://arxiv.org/abs/2012.13891)\]. Similarly, the paper \[[10](http://arxiv.org/abs/2205.12709)\] introduced a set of evaluation metrics to assess the effectiveness of unlearning in FL, emphasizing the need for multiple metrics to provide a more comprehensive assessment \[[10](http://arxiv.org/abs/2205.12709)\].

In summary, the field of federated unlearning has seen significant advancements, with various methods proposed to address the challenges of data removal, verification, and efficiency. These contributions have laid the groundwork for further research and development in this area.

References:
1. \[[2](http://arxiv.org/abs/2401.05146)\] 
2. \[[3](http://arxiv.org/abs/2310.20448)\] 
3. \[[4](http://arxiv.org/abs/2310.19218)\] 
4. \[[5](http://arxiv.org/abs/2406.03078)\] 
5. \[[6](http://arxiv.org/abs/2403.02437)\] 
6. \[[7](http://arxiv.org/abs/2308.12502)\] 
7. \[[8](http://arxiv.org/abs/2306.02216)\] 
8. \[[9](http://arxiv.org/abs/2012.13891)\] 
9. \[[10](http://arxiv.org/abs/2205.12709)\]
