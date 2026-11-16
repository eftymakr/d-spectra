## Related Works

Federated Learning (FL) has emerged as a promising paradigm for training machine learning models while preserving user privacy by keeping data decentralized \[[Youming Tao' 2024-01-19](http://arxiv.org/abs/2401.11018v1)\]. Recent advancements have focused on extending FL to address the "right to be forgotten," a legal requirement that mandates the ability to remove user data from training sets \[[Ruinan Jin' 2023-06-03](http://arxiv.org/abs/2306.02216v3)\]. This has led to the development of Federated Unlearning (FU), a subfield of FL that enables the removal of specific data points or clients from the global model without retraining the entire system \[[Hyejun Jeong' 2024-03-04](http://arxiv.org/abs/2403.02437v3)\].

Several approaches have been proposed to implement FU. For instance, \[[Nicolò Romandini' 2024-01-10](http://arxiv.org/abs/2401.05146v3)\] introduces a method for label unlearning in Vertical Federated Learning (VFL), where synthetic embeddings are generated to facilitate gradient-based forgetting. This approach ensures that the model can effectively remove the influence of specific labels while maintaining performance on retained data. Similarly, \[[Hanlin Gu' 2024-05-24](http://arxiv.org/abs/2405.15474v2)\] presents a framework for federated feature unlearning that minimizes feature sensitivity using Lipschitz continuity, enabling the removal of sensitive or biased features from the model.

Another notable work, \[[Ziyao Liu' 2023-10-31](http://arxiv.org/abs/2310.20448v4)\], focuses on the challenge of unlearning in FL with the goal of achieving certified data unlearning. The authors propose a method that allows the server to remove a target client's influence without additional communication or storage, enhancing both efficiency and security. This work is particularly relevant to FOLTR, as it aligns with the need for verifiable unlearning in decentralized settings.

In addition to unlearning, the field of federated learning has also seen advancements in privacy-preserving techniques. \[[Kahou Tam' 2024-06-05](http://arxiv.org/abs/2406.03078v1)\] explores the use of differential privacy to protect against data leakage during federated training, while \[[Yang Zhao' 2023-10-30](http://arxiv.org/abs/2310.19218v5)\] introduces a framework for secure aggregation in vertical FL, significantly improving efficiency compared to homomorphic encryption. These methods are crucial for ensuring that unlearning processes in FOLTR are both secure and efficient.

The integration of online learning to rank (OLTR) with FL has also been explored. \[[Gaoyang Liu' 2020-12-27](http://arxiv.org/abs/2012.13891v3)\] presents a framework for Federated Online Learning to Rank (FOLTR), which optimizes ranking models using implicit user feedback while preserving privacy. This work highlights the potential of FOLTR in applications such as search engines, where user privacy is paramount. However, FOLTR faces challenges in terms of ranking effectiveness and robustness, which are addressed in subsequent studies \[[Shuyi Wang' 2024-12-26](http://arxiv.org/abs/2412.19069v1)\].

In the context of unlearning, \[[Hanlin Gu' 2024-05-23](http://arxiv.org/abs/2405.17462v4)\] evaluates the effectiveness of different unlearning strategies in managing under-unlearning and over-unlearning scenarios. The authors propose new evaluation metrics to provide a more comprehensive assessment of unlearning success. This aligns with the current study, which rigorously assesses the effectiveness of five unlearning strategies in a verifiable manner.

References:

1. http://arxiv.org/abs/2207.02337v1  
2. http://arxiv.org/abs/2410.10922v4  
3. http://arxiv.org/abs/2306.02216v3  
4. http://arxiv.org/abs/2410.09947v1  
5. http://arxiv.org/abs/2405.17462v4  
6. http://arxiv.org/abs/2305.11236v1  
7. http://arxiv.org/abs/2206.02535v2  
8. http://arxiv.org/abs/2209.05395v1  
9. http://arxiv.org/abs/2412.19069v1  
10. http://arxiv.org/abs/2408.09545v2  
11. http://arxiv.org/abs/2410.09947v1
