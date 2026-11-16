## Related Works

The task of 3D human pose estimation has attracted significant research interest due to its applications in human-computer interaction, rehabilitation, and virtual environments. Early methods primarily relied on 2D pose estimation followed by 3D reconstruction, often using depth maps or multi-view setups \[[Yang Liu' 2024-07-14](http://arxiv.org/abs/2407.10099v2)\]. However, these approaches faced challenges in handling occlusions, viewpoint variations, and depth ambiguity \[[Ti Wang' 2023-04-27](http://arxiv.org/abs/2304.14045v1)\]. More recent methods have leveraged deep learning to directly estimate 3D poses from single-view inputs, often incorporating graph-based models to capture spatial relationships between joints \[[Jianbin Jiao' 2024-01-30](http://arxiv.org/abs/2401.16700v2)\]. 

A key challenge in 3D human pose estimation is modeling long-range dependencies between body parts, which are essential for accurate pose recovery. Existing methods often use deep networks to learn these dependencies, but this approach introduces uncorrelated noise and increases model complexity \[[Mona Fathollahi Ghezelghieh' 2016-09-18](http://arxiv.org/abs/1609.05522v1)\]. For example, some studies have explored using graph convolutional networks (GCNs) to model the human skeleton as a graph, enabling the capture of spatial relationships between joints \[[Zaedul Islam' 2024-05-05](http://arxiv.org/abs/2405.03055v1)\]. However, these models typically focus on local interactions and fail to effectively model long-range dependencies \[[Tianhan Xu' 2021-03-30](http://arxiv.org/abs/2103.16385v1)\]. 

To address this, several works have proposed using attention mechanisms to better capture long-range dependencies. For instance, some methods employ self-attention to model interactions between joints across different scales, improving the ability to capture complex pose structures \[[Keze Wang' 2019-01-12](http://arxiv.org/abs/1901.03798v2)\]. Additionally, some studies have introduced multi-scale architectures to better handle the varying levels of detail in human pose estimation \[[Tanvir Hassan' 2023-05-09](http://arxiv.org/abs/2305.05785v1)\]. These approaches often combine graph-based models with attention mechanisms to improve performance. 

In particular, the use of graph attention networks has gained traction in recent years. For example, some studies have proposed using graph attention modules to model the spatial relationships between joints, enabling the capture of long-range dependencies \[[Kamel Aouaidjia' 2025-05-02](http://arxiv.org/abs/2505.01003v1)\]. These models often incorporate multi-scale processing to better handle the complexity of human pose estimation \[[Haoyu Ma' 2021-10-18](http://arxiv.org/abs/2110.09554v3)\]. However, these methods still face challenges in effectively capturing cross-scale dependencies and maintaining computational efficiency \[[Drew Linsley' 2018-05-21](http://arxiv.org/abs/1805.08315v4)\]. 

To overcome these limitations, recent work has focused on developing more efficient and effective architectures for modeling long-range dependencies in 3D human pose estimation. For example, some studies have introduced pyramid structures to better capture cross-scale dependencies, enabling the model to learn both local and global features \[[Zhe Zhang' 2020-03-25](http://arxiv.org/abs/2003.11163v2)\]. These approaches often combine graph-based models with attention mechanisms to improve performance while maintaining computational efficiency \[[Patrik Puchert' 2021-07-23](http://arxiv.org/abs/2107.11214v4)\]. 

In summary, while existing methods have made significant progress in modeling long-range dependencies for 3D human pose estimation, there remains a need for more efficient and effective architectures that can better capture cross-scale dependencies while maintaining computational efficiency. The proposed approach in this paper addresses these challenges by introducing a novel Pyramid Graph Attention (PGA) module that effectively captures long-range cross-scale dependencies, leading to improved performance and reduced model complexity \[[Lei Tian' 2021-03-29](http://arxiv.org/abs/2103.15534v2)\].

References:
1. [Context from Document 1]
2. [Context from Document 2]
3. [Context from Document 3]
4. [Context from Document 4]
5. [Context from Document 5]
6. [Context from Document 6]
7. [Context from Document 7]
8. [Context from Document 8]
9. [Context from Document 9]
10. [Context from Document 10]
11. [Context from Document 11]
12. [Context from Document 12]
13. [Context from Document 13]
14. [Context from Document 14]
