## Related Works

Unsupervised domain adaptation for semantic segmentation (UDA-SS) aims to transfer knowledge from a labeled source domain to an unlabeled target domain, addressing the costly nature of pixel-level annotation in real-world applications. Early methods primarily focus on reducing the domain gap by aligning feature distributions or output spaces between the source and target domains. For instance, adversarial learning has been widely adopted for global and category-specific feature alignment, improving cross-domain generalization by encouraging domain-invariant representations \[[1612.02649](http://arxiv.org/abs/1612.02649)\]\[[1811.12833](http://arxiv.org/abs/1811.12833)\]\[[1809.09478](http://arxiv.org/abs/1809.09478)\]. Some approaches extend this by incorporating multi-level adversarial networks or output space adaptation to better capture spatial structures and semantic consistency \[[1802.10349](http://arxiv.org/abs/1802.10349)\]\[[1901.05427](http://arxiv.org/abs/1901.05427)\].

To further mitigate domain shift, pixel-level adaptation techniques using generative adversarial networks (GANs) or image translation have been proposed, enabling synthetic-to-real transformations that preserve semantic content \[[1711.03213](http://arxiv.org/abs/1711.03213)\]\[[1904.10620](http://arxiv.org/abs/1904.10620)\]\[[https://www.semanticscholar.org/paper/9d5a5517650d5f9a7d9818bcc1eb59ba65d316e1](https://www.semanticscholar.org/paper/9d5a5517650d5f9a7d9818bcc1eb59ba65d316e1)\]. These pixel-level adaptations complement feature-level alignment and have been shown to improve segmentation performance on real-world benchmarks.

Self-training with pseudo-labels has emerged as a powerful paradigm in UDA-SS, iteratively refining the model using confident predictions on unlabeled target data \[[2101.10979](http://arxiv.org/abs/2101.10979)\]\[[2007.08702](http://arxiv.org/abs/2007.08702)\]. However, noisy pseudo-labels and dispersed target features due to domain discrepancy remain challenges. Prototype-based methods address these issues by leveraging class centroids to denoise pseudo-labels and encourage compact target feature clustering, enhancing the reliability of self-training \[[2101.10979](http://arxiv.org/abs/2101.10979)\]\[[1910.13049](http://arxiv.org/abs/1910.13049)\].

Recent work also explores the integration of auxiliary tasks, such as depth estimation, to bridge domain gaps by exploiting task correlations and structural information \[[1904.01886](http://arxiv.org/abs/1904.01886)\]\[[2104.13613](http://arxiv.org/abs/2104.13613)\]\[[1903.12212](http://arxiv.org/abs/1903.12212)\]. Depth-aware domain adaptation frameworks and self-supervised depth estimation have demonstrated improved segmentation accuracy by leveraging complementary geometric cues available in both domains.

Addressing intra-domain variations within the target data itself, some methods propose splitting the target domain into easy and hard subsets based on entropy measures and applying self-supervised adaptation across these splits \[[2004.07703](http://arxiv.org/abs/2004.07703)\]. This intra-domain adaptation complements the inter-domain alignment and further stabilizes training.

Class imbalance and category-agnostic alignment issues have been tackled by category-level adversarial strategies and class-wise feature alignment, which focus adaptation efforts on poorly aligned or rare classes \[[https://www.semanticscholar.org/paper/3f9f801aec1f87ae81524f1928407673805927cb](https://www.semanticscholar.org/paper/3f9f801aec1f87ae81524f1928407673805927cb)\]\[[1809.09478](http://arxiv.org/abs/1809.09478)\]\[[https://www.semanticscholar.org/paper/3f9f801aec1f87ae81524f1928407673805927cb](https://www.semanticscholar.org/paper/3f9f801aec1f87ae81524f1928407673805927cb)\]. Such methods help reduce negative transfer and improve class-wise segmentation quality.

Data augmentation techniques tailored for semi-supervised and domain adaptation settings, like ClassMix and cross-domain mixed sampling, have been shown to enhance pseudo-label quality and overall adaptation performance by generating more diverse and representative training samples \[[2007.07936](http://arxiv.org/abs/2007.07936)\]\[[2007.08702](http://arxiv.org/abs/2007.08702)\]\[[2103.04705](http://arxiv.org/abs/2103.04705)\]. These augmentations promote better learning of common classes and reduce confirmation bias.

The challenge of unknown or private classes in the target domain, which violates the closed-set assumption of traditional UDA, has recently motivated universal domain adaptation approaches. Universal domain adaptation methods explicitly handle the presence of private classes and category gaps without prior knowledge of category sets. They quantify sample-level transferability to identify common and private classes, enabling rejection or separate treatment of unknown classes \[[https://www.semanticscholar.org/paper/a2e433da83c6e1eb4f4486c900fdfbf1951c4d30](https://www.semanticscholar.org/paper/a2e433da83c6e1eb4f4486c900fdfbf1951c4d30)\]\[[2004.01130](http://arxiv.org/abs/2004.01130)\]. These approaches represent a significant step towards more practical and robust domain adaptation in real-world scenarios.

Advances in network architectures, particularly the adoption of Transformer-based encoders and multi-level context fusion, have also contributed to improvements in UDA-SS by enhancing feature representation and training stability \[[2111.14887](http://arxiv.org/abs/2111.14887)\]. Complementary training strategies such as rare class sampling and feature distance regularization further improve adaptation for difficult classes.

In summary, while significant progress has been made in unsupervised domain adaptation for semantic segmentation through adversarial learning, self-training, auxiliary task integration, and data augmentation, most existing methods assume shared category sets between source and target domains. Universal domain adaptation frameworks, such as the proposed UniMAP, address this critical limitation by enabling robust adaptation without prior category knowledge, effectively separating common from private classes via domain-specific prototypes and targeted image matching strategies.

---

References:

\[[2004.07703](http://arxiv.org/abs/2004.07703)\] http://arxiv.org/abs/2004.07703  
\[[1904.01886](http://arxiv.org/abs/1904.01886)\] http://arxiv.org/abs/1904.01886  
\[[1910.13049](http://arxiv.org/abs/1910.13049)\] http://arxiv.org/abs/1910.13049  
\[[1904.10620](http://arxiv.org/abs/1904.10620)\] http://arxiv.org/abs/1904.10620  
\[[2007.08702](http://arxiv.org/abs/2007.08702)\] http://arxiv.org/abs/2007.08702  
\[[2101.10979](http://arxiv.org/abs/2101.10979)\] http://arxiv.org/abs/2101.10979  
\[[1809.09478](http://arxiv.org/abs/1809.09478)\] http://arxiv.org/abs/1809.09478  
\[[https://www.semanticscholar.org/paper/3f9f801aec1f87ae81524f1928407673805927cb](https://www.semanticscholar.org/paper/3f9f801aec1f87ae81524f1928407673805927cb)\] http://arxiv.org/abs/1910.13049  
\[[2104.13613](http://arxiv.org/abs/2104.13613)\] http://arxiv.org/abs/2104.13613  
\[[1802.10349](http://arxiv.org/abs/1802.10349)\] http://arxiv.org/abs/1802.10349  
\[[2007.07936](http://arxiv.org/abs/2007.07936)\] http://arxiv.org/abs/2007.07936  
\[[2004.01130](http://arxiv.org/abs/2004.01130)\] http://arxiv.org/abs/2004.01130  
\[[1811.12833](http://arxiv.org/abs/1811.12833)\] http://arxiv.org/abs/1811.12833  
\[[1612.02649](http://arxiv.org/abs/1612.02649)\] http://arxiv.org/abs/1612.02649  
\[[1901.05427](http://arxiv.org/abs/1901.05427)\] http://arxiv.org/abs/1901.05427  
\[[1903.12212](http://arxiv.org/abs/1903.12212)\] http://arxiv.org/abs/1903.12212  
\[[1711.03213](http://arxiv.org/abs/1711.03213)\] http://arxiv.org/abs/1711.03213  
\[[https://www.semanticscholar.org/paper/9d5a5517650d5f9a7d9818bcc1eb59ba65d316e1](https://www.semanticscholar.org/paper/9d5a5517650d5f9a7d9818bcc1eb59ba65d316e1)\] https://www.semanticscholar.org/paper/9d5a5517650d5f9a7d9818bcc1eb59ba65d316e1  
\[[https://www.semanticscholar.org/paper/a2e433da83c6e1eb4f4486c900fdfbf1951c4d30](https://www.semanticscholar.org/paper/a2e433da83c6e1eb4f4486c900fdfbf1951c4d30)\] https://www.semanticscholar.org/paper/a2e433da83c6e1eb4f4486c900fdfbf1951c4d30  
\[[2111.14887](http://arxiv.org/abs/2111.14887)\] http://arxiv.org/abs/2111.14887  
\[[2103.04705](http://arxiv.org/abs/2103.04705)\] http://arxiv.org/abs/2103.04705