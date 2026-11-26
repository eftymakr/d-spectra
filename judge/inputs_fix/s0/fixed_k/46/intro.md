## Related Works

Cross-domain sequential recommendation (CDSR) has gained significant attention in recent years due to its ability to leverage user behavior across multiple domains to improve recommendation performance. Early approaches primarily relied on domain-specific models and transfer learning techniques, often assuming overlapping users or items between domains \[[3](http://arxiv.org/abs/2304.03891)\]. However, these methods typically struggled with data sparsity and cold-start problems, especially when dealing with non-overlapping domains \[[12](http://arxiv.org/abs/2304.04218)\]. 

Recent advances have focused on integrating domain-specific information into the self-attention mechanism of transformer-based models, which is a core component of most sequential recommendation systems \[[25](http://arxiv.org/abs/1911.06478)\]. For example, some works have introduced domain-aware modules to enhance the modeling of cross-domain interactions \[[2](http://arxiv.org/abs/2405.12473)\]. However, these approaches often overlook the inherent power of the self-attention mechanism itself, which is capable of learning complex correlations between items in a sequence \[[1](http://arxiv.org/abs/2401.04971)\]. 

To address this, several studies have proposed methods that explicitly enhance the self-attention mechanism to better capture cross-domain dependencies. For instance, \[[19](http://arxiv.org/abs/2304.09184)\] introduced a frequency-enhanced hybrid attention network that leverages the frequency domain to capture both low- and high-frequency information, improving the model's ability to distinguish periodic patterns in user behavior. Similarly, \[[20](http://arxiv.org/abs/2211.01297)\] proposed a self-attentive model based on cheap causal convolutions, which efficiently captures local context information while reducing computational overhead. 

Another line of research has focused on the challenges of non-overlapping cross-domain scenarios, where users and items are entirely distinct between domains \[[12](http://arxiv.org/abs/2304.04218)\]. In such cases, traditional methods that rely on overlapping users or items are ineffective. To overcome this, \[[12](http://arxiv.org/abs/2304.04218)\] proposed a prompt learning-based framework that learns domain-invariant and domain-specific representations without requiring explicit alignment. This approach is particularly useful in scenarios where content information is unavailable \[[12](http://arxiv.org/abs/2304.04218)\]. 

Additionally, \[[22](http://arxiv.org/abs/2302.03221)\] introduced a lightweight external attention-enhanced graph convolutional network (LEA-GCN) to address the computational inefficiencies of existing methods while maintaining accuracy. This framework uses a dual-channel external attention mechanism to efficiently capture correlations among items, making it suitable for large-scale applications. 

In the context of federated learning, \[[16](http://arxiv.org/abs/2309.08420)\] proposed FedDCSR, a framework that enables cross-domain sequential recommendation without sharing raw user data, thus preserving privacy. This is especially relevant in scenarios where data privacy regulations such as GDPR are in place \[[16](http://arxiv.org/abs/2309.08420)\]. 

Moreover, \[[21](http://arxiv.org/abs/2311.08272)\] introduced a mixed attention network (MAN) that combines local and global attention modules to extract both domain-specific and cross-domain information. This approach is particularly effective in scenarios with limited overlapping users \[[21](http://arxiv.org/abs/2311.08272)\]. 

In summary, while many recent works have focused on enhancing the self-attention mechanism or addressing domain-specific challenges, the core self-attention module remains a critical component that is often underutilized. Our approach, AutoCDSR, builds upon these insights by focusing on improving the self-attention mechanism to better capture cross-domain dependencies \[[1](http://arxiv.org/abs/2401.04971)\].

### References

1. \[[1](http://arxiv.org/abs/2401.04971)\] [Document 1](http://arxiv.org/abs/2401.04971)  
2. \[[2](http://arxiv.org/abs/2405.12473)\] [Document 2](http://arxiv.org/abs/2405.12473)  
3. \[[3](http://arxiv.org/abs/2304.03891)\] [Document 3](http://arxiv.org/abs/2304.03891)  
4. \[[4](http://arxiv.org/abs/2311.04590)\] [Document 4](http://arxiv.org/abs/2311.04590)  
5. \[[5](http://arxiv.org/abs/2410.13588)\] [Document 5](http://arxiv.org/abs/2410.13588)  
6. \[[6](http://arxiv.org/abs/2209.10163)\] [Document 6](http://arxiv.org/abs/2209.10163)  
7. \[[7](http://arxiv.org/abs/2504.18383)\] [Document 7](http://arxiv.org/abs/2504.18383)  
8. \[[8](http://arxiv.org/abs/2401.15369)\] [Document 8](http://arxiv.org/abs/2401.15369)  
9. \[[9](http://arxiv.org/abs/2206.08050)\] [Document 9](http://arxiv.org/abs/2206.08050)  
10. \[[10](http://arxiv.org/abs/2410.21048)\] [Document 10](http://arxiv.org/abs/2410.21048)  
11. \[[11](http://arxiv.org/abs/2312.10325)\] [Document 11](http://arxiv.org/abs/2312.10325)  
12. \[[12](http://arxiv.org/abs/2304.04218)\] [Document 12](http://arxiv.org/abs/2304.04218)  
13. \[[13](http://arxiv.org/abs/2502.15694)\] [Document 13](http://arxiv.org/abs/2502.15694)  
14. \[[14](http://arxiv.org/abs/2404.00268)\] [Document 14](http://arxiv.org/abs/2404.00268)  
15. \[[15](http://arxiv.org/abs/2201.06035)\] [Document 15](http://arxiv.org/abs/2201.06035)  
16. \[[16](http://arxiv.org/abs/2309.08420)\] [Document 16](http://arxiv.org/abs/2309.08420)  
17. \[[17](http://arxiv.org/abs/2209.07997)\] [Document 17](http://arxiv.org/abs/2209.07997)  
18. \[[18](http://arxiv.org/abs/1803.01542)\] [Document 18](http://arxiv.org/abs/1803.01542)  
19. \[[19](http://arxiv.org/abs/2304.09184)\] [Document 19](http://arxiv.org/abs/2304.09184)  
20. \[[20](http://arxiv.org/abs/2211.01297)\] [Document 20](http://arxiv.org/abs/2211.01297)  
21. \[[21](http://arxiv.org/abs/2311.08272)\] [Document 21](http://arxiv.org/abs/2311.08272)  
22. \[[22](http://arxiv.org/abs/2302.03221)\] [Document 22](http://arxiv.org/abs/2302.03221)  
23. \[[23](http://arxiv.org/abs/2206.08088)\] [Document 23](http://arxiv.org/abs/2206.08088)  
24. \[[24](http://arxiv.org/abs/2203.16942)\] [Document 24](http://arxiv.org/abs/2203.16942)  
25. \[[25](http://arxiv.org/abs/1911.06478)\] [Document 25](http://arxiv.org/abs/1911.06478)  
26. \[[26](http://arxiv.org/abs/2504.15085)\] [Document 26](http://arxiv.org/abs/2504.15085)  
27. \[[27](http://arxiv.org/abs/2402.09784)\] [Document 27](http://arxiv.org/abs/2402.09784)  
28. \[[28](http://arxiv.org/abs/2108.11333)\] [Document 28](http://arxiv.org/abs/2108.11333)  
29. \[[29](http://arxiv.org/abs/2310.04633)\] [Document 29](http://arxiv.org/abs/2310.04633)  
30. \[[30](http://arxiv.org/abs/2012.00485)\] [Document 30](http://arxiv.org/abs/2012.00485)
