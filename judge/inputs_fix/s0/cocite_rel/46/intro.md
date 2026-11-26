## Related Works

Cross-domain sequential recommendation (CDSR) has gained significant attention in recent years due to its ability to alleviate data sparsity and cold-start problems in traditional sequential recommendation systems \[[1](http://arxiv.org/abs/2304.03891)\]. Several approaches have been proposed to address these challenges, often leveraging domain-specific components or attention mechanisms to enhance cross-domain learning \[[2](http://arxiv.org/abs/2105.03300)\]. However, many existing methods focus on adding domain-aware modules to pre-trained self-attention models without fully exploiting the inherent capabilities of the self-attention mechanism \[[3](http://arxiv.org/abs/2106.02768)\]. This section reviews related works that have contributed to the field of CDSR, highlighting their strengths and limitations.

Early works on CDSR primarily relied on graph-based models and transfer learning techniques to bridge the gap between domains \[[4](http://arxiv.org/abs/2311.04590)\]. For instance, CoNet \[[5](http://arxiv.org/abs/1808.09781)\] introduced a deep transfer learning approach using neural networks to enable knowledge transfer across domains. This method assumed that hidden layers in two base networks were connected via cross mappings, allowing for collaborative learning between domains \[[5](http://arxiv.org/abs/1808.09781)\]. While effective, such approaches often struggled with capturing the dynamic and sequential nature of user interactions \[[6](http://arxiv.org/abs/1804.06769)\].

More recently, researchers have explored the use of self-attention mechanisms to better model sequential patterns \[[7](http://arxiv.org/abs/2103.01696)\]. SASRec \[[8](http://arxiv.org/abs/2304.05027)\] was one of the first to apply self-attention to sequential recommendation, allowing for the modeling of long-term dependencies in user behavior. However, it primarily focused on single-domain settings and did not explicitly address cross-domain challenges \[[8](http://arxiv.org/abs/2304.05027)\]. Later works, such as BERT4Rec \[[9](http://arxiv.org/abs/2012.00485)\], extended this idea by employing bidirectional self-attention to capture both left and right context, leading to improved performance on sparse datasets \[[9](http://arxiv.org/abs/2012.00485)\].

To address cross-domain challenges, several studies have proposed hybrid models that combine domain-specific and domain-agnostic components \[[10](http://arxiv.org/abs/2311.04760)\]. For example, DASL \[[11](http://arxiv.org/abs/1904.06690)\] introduced a dual learning mechanism that iteratively transfers information between source and target domains, improving the performance of both \[[11](http://arxiv.org/abs/1904.06690)\]. Similarly, π-Net \[[12](https://www.semanticscholar.org/paper/fa990aee9a8f157b5d393f5f3eaa014e1e5c67aa)\] was designed to handle shared-account scenarios by incorporating a shared account filter unit and a cross-domain transfer unit to manage information flow between domains \[[12](https://www.semanticscholar.org/paper/fa990aee9a8f157b5d393f5f3eaa014e1e5c67aa)\]. These approaches demonstrated the potential of combining domain-specific and cross-domain modeling but often relied on overlapping users, limiting their applicability in real-world scenarios \[[13](https://www.semanticscholar.org/paper/6dd0605f7de7581c69b4acf0ab78000748a09f3e)\].

In addition to these methods, recent works have focused on addressing data sparsity and cold-start issues through contrastive learning and information flow mechanisms \[[14](http://arxiv.org/abs/2209.10163)\]. For example, Tri-CDR \[[15](http://arxiv.org/abs/2311.08272)\] proposed a framework that jointly models source, target, and mixed behavior sequences to capture global and target-specific preferences, leading to improved performance across domains \[[15](http://arxiv.org/abs/2311.08272)\]. Similarly, DDTCDR \[[16](http://arxiv.org/abs/1910.05189)\] introduced a dual transfer framework that enabled bidirectional knowledge exchange between domains, demonstrating the effectiveness of iterative learning strategies \[[16](http://arxiv.org/abs/1910.05189)\].

The proposed AutoCDSR framework builds upon these advances by focusing on enhancing the self-attention mechanism, which is a core component of transformer-based models \[[17](http://arxiv.org/abs/2108.03357)\]. By formulating cross-domain learning as a multi-objective optimization problem, AutoCDSR aims to improve recommendation performance while dynamically minimizing cross-domain attention scores \[[18](http://arxiv.org/abs/1711.04725)\]. This approach not only mitigates negative transfer but also encourages complementary knowledge exchange between domains \[[19](https://www.semanticscholar.org/paper/d1c7b8be5f3849a3fd4af780b58eb28355641206)\].

References  
\[[1](http://arxiv.org/abs/2304.03891)\] Document 1  
\[[2](http://arxiv.org/abs/2105.03300)\] Document 2  
\[[3](http://arxiv.org/abs/2106.02768)\] Document 3  
\[[4](http://arxiv.org/abs/2311.04590)\] Document 4  
\[[5](http://arxiv.org/abs/1808.09781)\] Document 5  
\[[6](http://arxiv.org/abs/1804.06769)\] Document 6  
\[[7](http://arxiv.org/abs/2103.01696)\] Document 7  
\[[8](http://arxiv.org/abs/2304.05027)\] Document 8  
\[[9](http://arxiv.org/abs/2012.00485)\] Document 9  
\[[10](http://arxiv.org/abs/2311.04760)\] Document 10  
\[[11](http://arxiv.org/abs/1904.06690)\] Document 11  
\[[12](https://www.semanticscholar.org/paper/fa990aee9a8f157b5d393f5f3eaa014e1e5c67aa)\] Document 12  
\[[13](https://www.semanticscholar.org/paper/6dd0605f7de7581c69b4acf0ab78000748a09f3e)\] Document 13  
\[[14](http://arxiv.org/abs/2209.10163)\] Document 14  
\[[15](http://arxiv.org/abs/2311.08272)\] Document 15  
\[[16](http://arxiv.org/abs/1910.05189)\] Document 16  
\[[17](http://arxiv.org/abs/2108.03357)\] Document 17  
\[[18](http://arxiv.org/abs/1711.04725)\] Document 18  
\[[19](https://www.semanticscholar.org/paper/d1c7b8be5f3849a3fd4af780b58eb28355641206)\] Document 19
