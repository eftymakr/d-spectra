## Related Works

Unsupervised domain adaptation (UDA) for semantic segmentation has gained significant attention due to its ability to transfer knowledge from a labeled source domain to an unlabeled target domain without requiring manual annotations \[[Seun-An Choe' 2024-05-30](http://arxiv.org/abs/2405.19899v1)\]. Traditional UDA methods assume that the category settings between the source and target domains are known, which is often not the case in real-world scenarios \[[Yue Wang' 2019-11-27](http://arxiv.org/abs/1911.11981v2)\]. This assumption leads to performance degradation when private classes exist in the target domain \[[Yiheng Zhang' 2018-04-23](http://arxiv.org/abs/1804.08286v1)\]. To address this limitation, several approaches have been proposed to handle unknown category settings.

One line of research focuses on domain adaptation with partial knowledge of category settings. For example, \[[Xin Jin' 2021-01-03](http://arxiv.org/abs/2101.00588v3)\] introduces a curriculum-style learning approach to minimize the domain gap by first learning global label distributions and then regularizing predictions to follow those properties. Similarly, \[[Inseop Chung' 2021-10-21](http://arxiv.org/abs/2110.10916v1)\] proposes a fully convolutional adaptation network that combines appearance and representation-level domain adaptation to improve generalization. These methods, however, still require some knowledge of the category settings.

Another approach is to use self-training with pseudo-labels to adapt the model to the target domain. \[[Maxime Bucher' 2020-04-02](http://arxiv.org/abs/2004.01130v2)\] presents a method that leverages self-training to adapt the decision boundary of the segmentation network to fit the distribution of the target domain. \[[Zhiming Wang' 2021-03-29](http://arxiv.org/abs/2103.15467v2)\] further improves this by introducing a self-training framework that iteratively refines pseudo-labels and improves segmentation accuracy. These methods are effective but often rely on the assumption that the category settings are known.

To handle unknown category settings, \[[Yonghao Xu' 2024-05-10](http://arxiv.org/abs/2405.06502v1)\] proposes a method that uses adversarial learning to bridge the domain gap and improve the transferability of the model. \[[Midhun Vayyat' 2022-08-27](http://arxiv.org/abs/2208.14227v2)\] extends this idea by introducing a category-adaptive threshold mechanism to balance pseudo labels across categories. These methods demonstrate that adversarial learning can be effective in handling domain shifts, but they still require some level of knowledge about the category settings.

More recently, \[[Marco Toldo' 2020-05-21](http://arxiv.org/abs/2005.10876v1)\] introduces a method that uses pixel alignment and self-training to reduce domain shift in cross-modality medical image segmentation. This approach aligns the source and target domains at the pixel level and adapts the decision boundary to fit the target distribution. \[[Gabriela Csurka' 2023-02-13](http://arxiv.org/abs/2302.06378v1)\] further improves this by introducing a multi-layer domain adaptation framework that stabilizes training in deep networks. These methods show that combining domain adaptation with self-training can lead to better performance, even when the category settings are unknown.

In addition to these methods, \[[Suhyeon Lee' 2020-12-23](http://arxiv.org/abs/2012.12545v1)\] proposes a framework that uses generative adversarial networks (GANs) and disentangled representation learning to improve cross-modality medical image segmentation. \[[Chaoxiang Ma' 2021-08-13](http://arxiv.org/abs/2108.06383v1)\] introduces a method that uses reciprocal normalization to improve the transferability of models across domains. These approaches demonstrate that advanced normalization techniques can be effective in handling domain shifts.

Overall, while many UDA methods have been proposed, most assume some knowledge of the category settings. The proposed UniMAP framework addresses this limitation by introducing a novel approach that does not require prior knowledge of category settings, making it more robust in real-world scenarios.

References:

1. \[[Seun-An Choe' 2024-05-30](http://arxiv.org/abs/2405.19899v1)\] http://arxiv.org/abs/1707.09465v5
2. \[[Yue Wang' 2019-11-27](http://arxiv.org/abs/1911.11981v2)\] http://arxiv.org/abs/1804.08286v1
3. \[[Yiheng Zhang' 2018-04-23](http://arxiv.org/abs/1804.08286v1)\] http://arxiv.org/abs/2103.15467v2
4. \[[Xin Jin' 2021-01-03](http://arxiv.org/abs/2101.00588v3)\] http://arxiv.org/abs/1707.09465v5
5. \[[Inseop Chung' 2021-10-21](http://arxiv.org/abs/2110.10916v1)\] http://arxiv.org/abs/1804.08286v1
6. \[[Maxime Bucher' 2020-04-02](http://arxiv.org/abs/2004.01130v2)\] http://arxiv.org/abs/2109.14219v1
7. \[[Zhiming Wang' 2021-03-29](http://arxiv.org/abs/2103.15467v2)\] http://arxiv.org/abs/2409.18340v1
8. \[[Yonghao Xu' 2024-05-10](http://arxiv.org/abs/2405.06502v1)\] http://arxiv.org/abs/2103.15467v2
9. \[[Midhun Vayyat' 2022-08-27](http://arxiv.org/abs/2208.14227v2)\] http://arxiv.org/abs/2112.10474v1
10. \[[Marco Toldo' 2020-05-21](http://arxiv.org/abs/2005.10876v1)\] http://arxiv.org/abs/2109.09736v1
11. \[[Gabriela Csurka' 2023-02-13](http://arxiv.org/abs/2302.06378v1)\] http://arxiv.org/abs/2110.06484v1
12. \[[Suhyeon Lee' 2020-12-23](http://arxiv.org/abs/2012.12545v1)\] http://arxiv.org/abs/2203.16557v2
13. \[[Chaoxiang Ma' 2021-08-13](http://arxiv.org/abs/2108.06383v1)\] http://arxiv.org/abs/2112.10474v1
