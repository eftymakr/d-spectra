## Related Works

Personalized outfit generation has garnered significant attention in recent years, driven by the increasing demand for fashion recommendation systems that can produce both compatible and personalized fashion items \[[1](http://arxiv.org/abs/2305.18290)\]. Early approaches focused on item-item compatibility, often using rule-based systems or simple similarity metrics \[[2](http://arxiv.org/abs/1905.01866)\]. However, these methods lacked the ability to capture complex user preferences and generate diverse outfit combinations \[[3](http://arxiv.org/abs/1608.03016)\].

Recent advances in deep learning have enabled more sophisticated approaches to outfit generation and recommendation. For example, \[[4](https://www.semanticscholar.org/paper/ca3ad34ff2652cd922c3476514a758674bc7e76b)\] introduced a system that uses a feature network and a matching network to recommend compatible outfits, leveraging deep convolutional networks for feature extraction and multi-layer fully-connected networks for compatibility computation. This work demonstrated the effectiveness of deep learning in capturing both item-level and outfit-level compatibility \[[5](http://arxiv.org/abs/1810.02443)\].

The use of reinforcement learning for fashion recommendation has also been explored. \[[6](http://arxiv.org/abs/1904.00741)\] proposed a method that fine-tunes large-scale language models using direct preference optimization (DPO), which simplifies the training process by eliminating the need for complex reward models. This approach has shown promise in aligning models with human preferences while maintaining stability and computational efficiency \[[7](http://arxiv.org/abs/1712.02662)\]. Similarly, \[[8](http://arxiv.org/abs/1710.07346)\] introduced a framework for generating outfits based on user preferences, using generative adversarial networks (GANs) to create new fashion items that match both the user's style and the compatibility requirements of the outfit \[[9](https://www.semanticscholar.org/paper/0157c94e753958610c732d3cbf753d9f640dee7c)\].

Another line of research focuses on the integration of user feedback and personalization. \[[10](https://www.semanticscholar.org/paper/255f90cd765d90e602cd35ab7e22c3a8db1acefa)\] proposed a system that uses a combination of visual and textual features to learn embeddings of fashion items in a latent style space, enabling the recommendation of compatible items. This approach was validated using the ASOS outfits dataset, showing strong performance in compatibility prediction \[[11](http://arxiv.org/abs/1906.07273)\]. Additionally, \[[12](http://arxiv.org/abs/1806.08977)\] introduced a method that uses self-attention mechanisms to learn outfit representations, allowing for the prediction of compatibility and the retrieval of complementary items \[[13](http://arxiv.org/abs/1807.03133)\].

The importance of interpretability in fashion recommendation has also been highlighted. \[[14](https://www.semanticscholar.org/paper/b1db62044adca574e4cf88b23c170f3cc089d513)\] proposed a partitioned embedding network that enables interpretable and customizable outfit composition by learning embeddings that correspond to different attributes of the fashion items \[[15](http://arxiv.org/abs/1804.09979)\]. This approach allows for better understanding of the factors influencing outfit recommendations \[[16](http://arxiv.org/abs/1205.2618)\].

In summary, while existing methods have made significant strides in outfit generation and recommendation, there remains a need for frameworks that can effectively balance personalization, compatibility, and diversity in generated outfits. The proposed framework, FashionDPO, addresses these challenges by leveraging direct preference optimization and multi-expert feedback generation, as detailed in the paper \[[17](https://www.semanticscholar.org/paper/30fb5c24cc15eb8cde5e389bf368d65fb96513e4)\].

References:
1. \[[1](http://arxiv.org/abs/2305.18290)\] [Document 1]
2. \[[2](http://arxiv.org/abs/1905.01866)\] [Document 2]
3. \[[3](http://arxiv.org/abs/1608.03016)\] [Document 3]
4. \[[4](https://www.semanticscholar.org/paper/ca3ad34ff2652cd922c3476514a758674bc7e76b)\] [Document 4]
5. \[[5](http://arxiv.org/abs/1810.02443)\] [Document 5]
6. \[[6](http://arxiv.org/abs/1904.00741)\] [Document 6]
7. \[[7](http://arxiv.org/abs/1712.02662)\] [Document 7]
8. \[[8](http://arxiv.org/abs/1710.07346)\] [Document 8]
9. \[[9](https://www.semanticscholar.org/paper/0157c94e753958610c732d3cbf753d9f640dee7c)\] [Document 9]
10. \[[10](https://www.semanticscholar.org/paper/255f90cd765d90e602cd35ab7e22c3a8db1acefa)\] [Document 10]
11. \[[11](http://arxiv.org/abs/1906.07273)\] [Document 11]
12. \[[12](http://arxiv.org/abs/1806.08977)\] [Document 12]
13. \[[13](http://arxiv.org/abs/1807.03133)\] [Document 13]
14. \[[14](https://www.semanticscholar.org/paper/b1db62044adca574e4cf88b23c170f3cc089d513)\] [Document 14]
15. \[[15](http://arxiv.org/abs/1804.09979)\] [Document 15]
16. \[[16](http://arxiv.org/abs/1205.2618)\] [Document 16]
17. \[[17](https://www.semanticscholar.org/paper/30fb5c24cc15eb8cde5e389bf368d65fb96513e4)\] [Document 23]
