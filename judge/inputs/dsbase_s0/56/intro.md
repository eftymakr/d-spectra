## Related Works

Cross-domain Sequential Recommendation (CDSR) has emerged as a critical area in recommendation systems, aiming to leverage user behavior across multiple domains to improve recommendation accuracy, especially in data-scarce scenarios \[[Muyang Ma' 2020-12-01](http://arxiv.org/abs/2012.00485v3)\]. Traditional CDSR methods often rely on overlapping users to transfer knowledge between domains, which limits their applicability in real-world settings where such overlap is rare \[[Haoyi Zhang' 2024-06-17](http://arxiv.org/abs/2406.11156v4)\]. Additionally, modeling complex transition patterns from mixed behavior sequences remains a significant challenge \[[Wangyu Wu' 2024-12-31](http://arxiv.org/abs/2502.15694v2)\].

Several approaches have been proposed to address these issues. For instance, \[[Hongyu Zhang' 2023-09-15](http://arxiv.org/abs/2309.08420v7)\] introduces a reinforcement learning module to simulate the evolution of user preferences by allocating items into sub-sequences based on temporal and behavioral patterns. This method improves performance by about 8.21% on Precision, 10.08% on Recall, and 10.32% on NDCG compared to state-of-the-art methods. Similarly, \[[Yu Liu' 2025-03-17](http://arxiv.org/abs/2503.13254v1)\] proposes a Contextualized Temporal Attention Mechanism that dynamically weighs historical actions' influence based on time and context, enhancing the model's ability to capture temporal dynamics.

To tackle the overlap dilemma, \[[Shu Chen' 2024-01-10](http://arxiv.org/abs/2401.04971v4)\] focuses on Non-overlapping Cross-domain Sequential Recommendation (NCSR), where there are no shared users or items between domains. The work introduces a Prompt Learning-based Cross-domain Recommender (PLCR) that learns domain-invariant and domain-specific representations without requiring explicit domain alignment. This approach is particularly useful in scenarios where data sparsity is a major issue \[[Wangyu Wu' 2025-04-21](http://arxiv.org/abs/2504.15085v5)\].

Another notable contribution is \[[Wujiang Xu' 2023-11-08](http://arxiv.org/abs/2311.04760v3)\], which proposes a Federated Mixture-of-Expert (FMoE) framework for non-overlapped cross-domain sequential recommendation. This method leverages federated learning to train models without sharing sensitive user data, addressing privacy concerns while improving recommendation accuracy \[[Xiaolin Zheng' 2022-09-21](http://arxiv.org/abs/2209.10163v1)\]. Similarly, \[[Zongyi Xiang' 2024-10-27](http://arxiv.org/abs/2410.20580v2)\] introduces a privacy-preserving cross-domain sequential recommendation system (PriCDSR) that incorporates differential privacy to protect user data while maintaining performance.

To address transition complexity, \[[Guanyu Lin' 2023-11-14](http://arxiv.org/abs/2311.08272v1)\] proposes a Mixed Information Flow network that considers both behavioral and knowledge flows across domains. This approach enables the model to decide when and how to use cross-domain information to enrich sequence representations, leading to improved performance on multiple e-commerce datasets \[[Wujiang Xu' 2023-11-08](http://arxiv.org/abs/2311.04590v6)\]. Additionally, \[[Jiangxia Cao' 2023-04-08](http://arxiv.org/abs/2304.03891v1)\] introduces a Mixed Attention Network (MAN) with local and global attention modules to capture both domain-specific and cross-domain information, achieving superior performance on real-world datasets \[[Haipeng Li' 2024-10-17](http://arxiv.org/abs/2410.13588v1)\].

Recent work has also explored the integration of Large Language Models (LLMs) into CDSR. For example, \[[Pavan Seshadri' 2024-09-11](http://arxiv.org/abs/2409.07367v1)\] investigates the use of LLMs for cross-domain sequential recommendation, leveraging their semantic understanding to capture user preferences across domains. This approach has shown promising results in improving recommendation accuracy, especially when the source and target domains have smaller domain gaps \[[Pan Li' 2021-04-17](http://arxiv.org/abs/2104.08490v2)\].

In summary, while existing CDSR methods have made significant strides, they often face limitations in terms of data overlap and modeling complex transitions. The integration of LLMs offers a promising direction to address these challenges by leveraging their powerful representation and reasoning capabilities \[[Changshuo Zhang' 2024-08-15](http://arxiv.org/abs/2408.08209v2)\].

### References

1. http://arxiv.org/abs/2012.00485v3  
2. http://arxiv.org/abs/2002.00741v1  
3. http://arxiv.org/abs/2012.00485v3  
4. http://arxiv.org/abs/2203.16942v1  
5. http://arxiv.org/abs/2002.00741v1  
6. http://arxiv.org/abs/2304.04218v1  
7. http://arxiv.org/abs/2304.04218v1  
8. http://arxiv.org/abs/2503.13254v1  
9. http://arxiv.org/abs/2401.15369v1  
10. http://arxiv.org/abs/2401.15369v1  
11. http://arxiv.org/abs/2012.00485v3  
12. http://arxiv.org/abs/2311.08272v1  
13. http://arxiv.org/abs/2304.03891v1  
14. http://arxiv.org/abs/2311.04590v6  
15. http://arxiv.org/abs/2409.07367v1  
16. http://arxiv.org/abs/2411.19862v1  
17. http://arxiv.org/abs/2409.14810v1
