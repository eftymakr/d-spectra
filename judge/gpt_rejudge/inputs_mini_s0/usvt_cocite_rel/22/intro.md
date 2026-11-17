## Related Works

Unsupervised domain adaptation (UDA) for semantic segmentation aims to transfer knowledge from labeled source domains—often synthetic datasets—to unlabeled target domains, typically real-world images, without requiring expensive annotations \[[2004.07703](http://arxiv.org/abs/2004.07703)\]. Traditional UDA approaches generally assume that the source and target domains share the same category sets, which is often unrealistic in practical applications where private classes exclusive to either domain may exist. This mismatch can cause significant performance degradation due to confusion between shared (common) and private classes \[[2007.08702](http://arxiv.org/abs/2007.08702)\].

### Domain Adaptation with Known Category Settings

Early works in UDA for semantic segmentation mainly focus on reducing the domain gap via adversarial learning or self-training. Adversarial domain adaptation methods align feature distributions globally or at multiple levels, including pixel-level, feature-level, or output space, to encourage domain-invariant representations \[[1802.10349](http://arxiv.org/abs/1802.10349)\]\[[1612.02649](http://arxiv.org/abs/1612.02649)\]\[[1811.12833](http://arxiv.org/abs/1811.12833)\]. For example, methods like ADVENT use entropy minimization combined with adversarial training to improve adaptation \[[1811.12833](http://arxiv.org/abs/1811.12833)\], while approaches such as CyCADA perform cycle-consistent image translation to reduce low-level appearance differences \[[1711.03213](http://arxiv.org/abs/1711.03213)\]. Other works enhance category-level alignment to avoid misalignment of well-aligned classes, employing category-aware adversarial losses or fine-grained domain discriminators to preserve semantic consistency \[[1809.09478](http://arxiv.org/abs/1809.09478)\]\[[2007.09222](http://arxiv.org/abs/2007.09222)\].

Self-training methods leverage pseudo-labels generated on the target domain to iteratively refine the segmentation model. Techniques like instance adaptive self-training and maximum squares loss mitigate the imbalance between easy and hard samples to improve pseudo-label quality and class balance \[[1909.13589](http://arxiv.org/abs/1909.13589)\]\[[2008.12197](http://arxiv.org/abs/2008.12197)\]. Moreover, uncertainty-aware methods explicitly model prediction uncertainty to rectify noisy pseudo-labels, thereby enhancing robustness during adaptation \[[2003.03773](http://arxiv.org/abs/2003.03773)\]\[[2004.08878](http://arxiv.org/abs/2004.08878)\]. Prototypical learning approaches further exploit feature centroids to denoise pseudo-labels and compact target feature space representations \[[2101.10979](http://arxiv.org/abs/2101.10979)\].

Recent advances integrate multiple complementary strategies, such as depth-aware adaptation that leverages privileged source domain information \[[1904.01886](http://arxiv.org/abs/1904.01886)\], and Fourier domain adaptation which aligns low-frequency components of source and target images to reduce domain shifts without complex adversarial training \[[2004.05498](http://arxiv.org/abs/2004.05498)\]. Additionally, architectural improvements using Transformer-based encoders and context-aware decoders have shown substantial gains in UDA performance \[[2111.14887](http://arxiv.org/abs/2111.14887)\].

### Handling Category Discrepancies and Unknown Categories

While most UDA methods assume shared category sets, this assumption fails when private classes exist in the target domain. Some works address this by employing curriculum learning that first infers global and local label distributions in the target domain to guide adaptation \[[1707.09465](http://arxiv.org/abs/1707.09465)\]\[[1908.09547](http://arxiv.org/abs/1908.09547)\]. These approaches gradually introduce harder adaptation tasks to improve generalization without explicit category knowledge.

Other methods explicitly handle class imbalance and category-level adaptation through semantic feature disentanglement, separated semantic feature adaptation, or instance-level alignment strategies that treat "stuff" and "things" categories differently to avoid over-alignment \[[https://www.semanticscholar.org/paper/3f9f801aec1f87ae81524f1928407673805927cb](https://www.semanticscholar.org/paper/3f9f801aec1f87ae81524f1928407673805927cb)\]\[[2003.08040](http://arxiv.org/abs/2003.08040)\]. Category anchor-guided models and patch-level discriminative representations have been proposed to align features at finer granularity while preserving intra-class structure \[[1910.13049](http://arxiv.org/abs/1910.13049)\]\[[1901.05427](http://arxiv.org/abs/1901.05427)\].

Furthermore, adversarial perturbation-based methods train domain-invariant classifiers by exposing models to adversarial feature perturbations at each spatial location, improving adaptation of tail classes and small objects \[[1912.08954](http://arxiv.org/abs/1912.08954)\]. Cross-domain consistency losses enforce prediction consistency over translated images to handle pixel-level domain shifts effectively \[[2001.03182](http://arxiv.org/abs/2001.03182)\].

### Limitations and Emerging Directions

Despite these advances, most existing UDA methods require prior knowledge of shared category sets or rely heavily on confident pseudo-labels, which limits their applicability in universal domain adaptation scenarios where category overlap is unknown or partial. The challenge lies in correctly distinguishing common classes from private ones in the target domain, especially when the model produces low confidence scores for shared classes due to domain discrepancies.

The proposed UniMAP framework, which introduces domain-specific prototype-based distinction and target-based image matching, addresses this limitation by enabling finer separation of domain-specific features and promoting learning of common classes without prior category knowledge. This approach builds on the strengths of prototype learning and self-training while explicitly tackling the challenge of unknown category settings, thereby advancing the frontier of UDA for semantic segmentation beyond traditional assumptions.

---

References:

\[[2004.07703](http://arxiv.org/abs/2004.07703)\] http://arxiv.org/abs/1707.09465  
\[[1909.13589](http://arxiv.org/abs/1909.13589)\] http://arxiv.org/abs/1909.13589  
\[[2007.08702](http://arxiv.org/abs/2007.08702)\] http://arxiv.org/abs/2103.15467  
\[[1904.01886](http://arxiv.org/abs/1904.01886)\] http://arxiv.org/abs/1904.01886  
\[[2004.05498](http://arxiv.org/abs/2004.05498)\] http://arxiv.org/abs/2004.05498  
\[[1809.09478](http://arxiv.org/abs/1809.09478)\] http://arxiv.org/abs/1809.09478  
\[[2003.03773](http://arxiv.org/abs/2003.03773)\] http://arxiv.org/abs/2003.03773  
\[[2008.12197](http://arxiv.org/abs/2008.12197)\] http://arxiv.org/abs/2008.12197  
\[[1910.13049](http://arxiv.org/abs/1910.13049)\] http://arxiv.org/abs/1910.13049  
\[[1802.10349](http://arxiv.org/abs/1802.10349)\] http://arxiv.org/abs/1802.10349  
\[[https://www.semanticscholar.org/paper/3f9f801aec1f87ae81524f1928407673805927cb](https://www.semanticscholar.org/paper/3f9f801aec1f87ae81524f1928407673805927cb)\] https://www.semanticscholar.org/paper/3f9f801aec1f87ae81524f1928407673805927cb  
\[[1612.02649](http://arxiv.org/abs/1612.02649)\] http://arxiv.org/abs/1612.02649  
\[[2004.08878](http://arxiv.org/abs/2004.08878)\] http://arxiv.org/abs/2004.08878  
\[[1811.12833](http://arxiv.org/abs/1811.12833)\] http://arxiv.org/abs/1811.12833  
\[[2101.10979](http://arxiv.org/abs/2101.10979)\] http://arxiv.org/abs/2101.10979  
\[[2111.14887](http://arxiv.org/abs/2111.14887)\] http://arxiv.org/abs/2111.14887  
\[[1901.05427](http://arxiv.org/abs/1901.05427)\] http://arxiv.org/abs/1901.05427  
\[[1912.08954](http://arxiv.org/abs/1912.08954)\] http://arxiv.org/abs/1912.08954  
\[[2003.08040](http://arxiv.org/abs/2003.08040)\] http://arxiv.org/abs/2003.08040  
\[[1711.03213](http://arxiv.org/abs/1711.03213)\] http://arxiv.org/abs/1711.03213  
\[[2001.03182](http://arxiv.org/abs/2001.03182)\] http://arxiv.org/abs/2001.03182  
\[[2007.09222](http://arxiv.org/abs/2007.09222)\] http://arxiv.org/abs/2007.09222  
\[[1707.09465](http://arxiv.org/abs/1707.09465)\] http://arxiv.org/abs/1707.09465  
\[[1908.09547](http://arxiv.org/abs/1908.09547)\] http://arxiv.org/abs/1908.09547