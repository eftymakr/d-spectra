## Related Works

Open-vocabulary object detection (OVD) has gained significant attention in recent years due to its ability to detect objects from a vocabulary defined by the user at inference time, without requiring extensive training \[[1' 2016-12-02](http://arxiv.org/abs/1612.00576v2)\]. This capability allows for greater flexibility and adaptability in real-world applications, where the set of target objects may not be known in advance \[[2' 2024-05-16](http://arxiv.org/abs/2405.10053v1)\]. However, the effectiveness of OVD models is often limited by the quality and specificity of the user-defined vocabulary, which may include irrelevant or overly broad categories \[[3' 2023-12-19](http://arxiv.org/abs/2312.12437v1)\]. To address this challenge, several works have explored methods to refine and adapt the vocabulary during inference, ensuring that only relevant classes are considered for detection \[[4' 2024-05-14](http://arxiv.org/abs/2405.08593v1)\].

One early approach to OVD leveraged pre-trained vision-language models to align image features with textual descriptions, enabling the detection of novel object categories \[[5' 2017-11-11](http://arxiv.org/abs/1711.05557v1)\]. However, these methods often struggled with vocabulary generalization and were sensitive to the specificity of the input prompts \[[6' 2022-06-22](http://arxiv.org/abs/2206.11134v4)\]. More recently, researchers have introduced techniques such as constrained beam search \[[7' 2024-04-14](http://arxiv.org/abs/2404.09216v1)\], semantic hierarchy integration \[[8' 2024-11-27](http://arxiv.org/abs/2411.18207v4)\], and weakly supervised learning \[[9' 2022-07-07](http://arxiv.org/abs/2207.03482v3)\] to improve the robustness and accuracy of OVD models. These approaches have shown promising results in various benchmarks, including COCO and LVIS \[[10' 2023-06-28](http://arxiv.org/abs/2306.15880v4)\].

The work in \[[11' 2024-05-30](http://arxiv.org/abs/2405.19854v1)\] introduced a framework for generating region-text pairs, which can be used to enhance the performance of OVD models by providing more accurate and semantically rich descriptions of objects. Similarly, \[[12' 2024-06-17](http://arxiv.org/abs/2406.11739v1)\] proposed a method for aligning object and image-level representations, which helped bridge the gap between visual and linguistic modalities in open-vocabulary detection tasks. This was further extended in \[[13' 2025-03-19](http://arxiv.org/abs/2503.14862v3)\], where a novel task and benchmark were introduced to evaluate fine-grained attribute detection in the open-vocabulary setting.

Another key contribution in the field is the development of efficient and scalable methods for OVD, such as the use of self-training with Web-scale image-text pairs \[[14' 2024-08-20](http://arxiv.org/abs/2408.11221v1)\]. This approach allows for the expansion of detection data without requiring extensive manual annotations, thereby improving the generalization ability of OVD models \[[15' 2023-04-03](http://arxiv.org/abs/2304.00788v2)\]. Additionally, \[[16' 2022-11-23](http://arxiv.org/abs/2211.12914v2)\] introduced a framework for open-vocabulary 3D object detection that leverages 2D-3D geometric priors and cross-modal alignment to achieve accurate localization and semantic interpretation of objects \[[17' 2024-09-14](http://arxiv.org/abs/2409.09401v2)\].

In parallel, efforts have been made to improve the interpretability and robustness of OVD models by incorporating additional constraints and regularization techniques \[[18' 2023-09-18](http://arxiv.org/abs/2309.09456v1)\]. For instance, \[[19' 2025-03-18](http://arxiv.org/abs/2503.14604v2)\] proposed a method that uses pseudo-labeling and contrastive learning to refine the detection process, while \[[20' 2023-06-16](http://arxiv.org/abs/2306.09683v3)\] introduced a framework for open-vocabulary detection in remote sensing scenarios, addressing the domain gap between natural-world and remote sensing images \[[21' 2024-08-25](http://arxiv.org/abs/2408.13936v1)\].

In summary, the field of open-vocabulary object detection has seen significant advancements, with various approaches addressing the challenges of vocabulary generalization, semantic alignment, and scalability. These contributions form the foundation for the proposed Vocabulary Adapter (VocAda), which aims to refine user-defined vocabularies in a plug-and-play manner during inference \[[22' 2024-08-17](http://arxiv.org/abs/2408.09110v3)\].

References:
1. \[[1' 2016-12-02](http://arxiv.org/abs/1612.00576v2)\] http://arxiv.org/abs/2405.10053v1
2. \[[2' 2024-05-16](http://arxiv.org/abs/2405.10053v1)\] http://arxiv.org/abs/2405.08593v1
3. \[[3' 2023-12-19](http://arxiv.org/abs/2312.12437v1)\] http://arxiv.org/abs/2405.19854v1
4. \[[4' 2024-05-14](http://arxiv.org/abs/2405.08593v1)\] http://arxiv.org/abs/2404.09216v1
5. \[[5' 2017-11-11](http://arxiv.org/abs/1711.05557v1)\] http://arxiv.org/abs/2206.11134v4
6. \[[6' 2022-06-22](http://arxiv.org/abs/2206.11134v4)\] http://arxiv.org/abs/2312.12437v1
7. \[[7' 2024-04-14](http://arxiv.org/abs/2404.09216v1)\] http://arxiv.org/abs/1612.00576v2
8. \[[8' 2024-11-27](http://arxiv.org/abs/2411.18207v4)\] http://arxiv.org/abs/2405.10053v1
9. \[[9' 2022-07-07](http://arxiv.org/abs/2207.03482v3)\] http://arxiv.org/abs/2312.12437v1
10. \[[10' 2023-06-28](http://arxiv.org/abs/2306.15880v4)\] http://arxiv.org/abs/2405.10053v1
11. \[[11' 2024-05-30](http://arxiv.org/abs/2405.19854v1)\] http://arxiv.org/abs/2405.19854v1
12. \[[12' 2024-06-17](http://arxiv.org/abs/2406.11739v1)\] http://arxiv.org/abs/2207.03482v3
13. \[[13' 2025-03-19](http://arxiv.org/abs/2503.14862v3)\] http://arxiv.org/abs/2503.14862v3
14. \[[14' 2024-08-20](http://arxiv.org/abs/2408.11221v1)\] http://arxiv.org/abs/2306.09683v3
15. \[[15' 2023-04-03](http://arxiv.org/abs/2304.00788v2)\] http://arxiv.org/abs/2304.00788v2
16. \[[16' 2022-11-23](http://arxiv.org/abs/2211.12914v2)\] http://arxiv.org/abs/2211.12914v2
17. \[[17' 2024-09-14](http://arxiv.org/abs/2409.09401v2)\] http://arxiv.org/abs/2309.09456v1
18. \[[18' 2023-09-18](http://arxiv.org/abs/2309.09456v1)\] http://arxiv.org/abs/2205.06230v2
19. \[[19' 2025-03-18](http://arxiv.org/abs/2503.14604v2)\] http://arxiv.org/abs/2408.13936v1
20. \[[20' 2023-06-16](http://arxiv.org/abs/2306.09683v3)\] http://arxiv.org/abs/2408.09110v3
21. \[[21' 2024-08-25](http://arxiv.org/abs/2408.13936v1)\] http://arxiv.org/abs/2205.06230v2
22. \[[22' 2024-08-17](http://arxiv.org/abs/2408.09110v3)\] http://arxiv.org/abs/2405.10053v1
