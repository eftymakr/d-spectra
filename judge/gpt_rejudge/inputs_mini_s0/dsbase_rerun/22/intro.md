## Related Works

Unsupervised domain adaptation (UDA) for semantic segmentation (SS) has been extensively studied to transfer knowledge from a labeled source domain to an unlabeled target domain, addressing the challenge of costly pixel-level annotations \[[2005.10876v1](http://arxiv.org/abs/2005.10876v1)\]\[[2112.03241v1](http://arxiv.org/abs/2112.03241v1)\]. Conventional UDA-SS methods generally assume a shared and known category space between source and target domains, which limits their effectiveness in real-world scenarios where private or unknown classes may exist exclusively in the target domain. This assumption often leads to significant performance degradation due to misclassification of unknown classes as common ones \[[2405.19899v1](http://arxiv.org/abs/2405.19899v1)\]\[[2004.01130v2](http://arxiv.org/abs/2004.01130v2)\].

### Domain Adaptation with Known or Partial Category Overlap

Initial UDA approaches focused on reducing domain discrepancy through image-level and feature-level alignment. For example, Fully Convolutional Adaptation Networks (FCAN) combine appearance adaptation via image translation and adversarial learning for domain-invariant feature learning \[[2206.03600v2](http://arxiv.org/abs/2206.03600v2)\]. Similarly, category-conditional domain adaptation methods employ class-wise discriminators to balance adaptation performance across classes, addressing class imbalance issues \[[1911.11981v2](http://arxiv.org/abs/1911.11981v2)\]\[[2103.15467v2](http://arxiv.org/abs/2103.15467v2)\]. Self-training approaches that generate pseudo-labels for the target domain have also become popular by iteratively refining target predictions to improve adaptation \[[2103.16372v1](http://arxiv.org/abs/2103.16372v1)\]\[[2110.10916v1](http://arxiv.org/abs/2110.10916v1)\]. These methods often rely on assumed knowledge of category sets or partial overlap, which limits their generalization to open or universal domain adaptation scenarios.

### Open-Set and Universal Domain Adaptation

To handle unknown or private classes in the target domain, open-set and universal domain adaptation (UniDA) methods have recently emerged. Open-Set Domain Adaptation for Semantic Segmentation (OSDA-SS) recognizes the challenge of identifying unknown classes and proposes boundary- and shape-aware contrastive losses to better separate known and unknown classes \[[2405.19899v1](http://arxiv.org/abs/2405.19899v1)\]. Other works introduce domain mixing augmentations and contrastive learning to enhance unknown class detection and feature disentanglement \[[2208.14227v2](http://arxiv.org/abs/2208.14227v2)\]\[[2405.19899v1](http://arxiv.org/abs/2405.19899v1)\]. Unlike traditional open-set methods that group all unknown classes into a single "unknown" category, some frameworks explicitly predict novel classes by leveraging zero-shot learning techniques combined with domain adaptation \[[2004.01130v2](http://arxiv.org/abs/2004.01130v2)\].

Source-free adaptation methods, which do not require access to source data during target adaptation, have also been proposed to address privacy and scalability concerns. These approaches typically update a pretrained source model with unlabeled target data using entropy minimization or self-supervision while modeling unknown classes explicitly \[[2103.16372v1](http://arxiv.org/abs/2103.16372v1)\]\[[2206.03600v2](http://arxiv.org/abs/2206.03600v2)\]. Multi-target adaptation without external data further extends this by enabling adaptation to multiple unseen target domains without retraining from scratch, leveraging self-distillation and adversarial learning to preserve source knowledge \[[2405.06502v1](http://arxiv.org/abs/2405.06502v1)\].

### Advanced Techniques for Robust Adaptation

Several methods explore disentangled representation learning to separate content (semantics) from style (domain-specific variations), thereby reducing domain gaps more effectively. For example, content transfer frameworks extract domain-invariant content features while transferring tail-class content to handle class imbalance \[[2012.12545v1](http://arxiv.org/abs/2012.12545v1)\]. Style normalization and restitution approaches filter out style variations while preserving task-relevant discriminative features to improve both domain generalization and adaptation \[[2101.00588v3](http://arxiv.org/abs/2101.00588v3)\].

Attention mechanisms and transformer-based architectures have also been integrated into UDA frameworks to capture long-range dependencies and improve feature alignment. Robust core-periphery constrained transformers have been shown to enhance transferable representations by modeling structured attention patterns inspired by brain networks \[[2308.13515v5](http://arxiv.org/abs/2308.13515v5)\]. Contrastive learning incorporated into student-teacher paradigms further boosts cross-domain feature discrimination and adaptation \[[2208.14227v2](http://arxiv.org/abs/2208.14227v2)\].

### Semantic Segmentation in Challenging Settings

Domain adaptation has been extended to challenging scenarios such as cross-modality medical image segmentation and 3D LiDAR semantic segmentation. Cross-modality UDA often combines generative adversarial networks with disentangled representations and self-training to bridge modality gaps \[[2409.18340v1](http://arxiv.org/abs/2409.18340v1)\]\[[2109.14219v1](http://arxiv.org/abs/2109.14219v1)\]. In LiDAR semantic segmentation, aligning class distributions and leveraging multi-view projections to generate 2D views for ensemble learning have been effective in mitigating domain shifts and segmenting rare or unseen classes \[[2010.12239v3](http://arxiv.org/abs/2010.12239v3)\]\[[2505.15545v3](http://arxiv.org/abs/2505.15545v3)\]\[[2107.09783v3](http://arxiv.org/abs/2107.09783v3)\].

### Summary

Despite the rich literature on UDA for semantic segmentation, most existing works assume known or partially known category sets between source and target domains, which limits their real-world applicability. Recent advances in open-set and universal domain adaptation explicitly address unknown target classes, employing prototype-based distinctions, boundary-aware losses, and image matching strategies to improve class separation and reduce confusion between common and private classes \[[2405.19899v1](http://arxiv.org/abs/2405.19899v1)\]\[[2004.01130v2](http://arxiv.org/abs/2004.01130v2)\]. Source-free and multi-target adaptation methods enhance scalability and privacy compliance. Moreover, disentangled representations, contrastive learning, and transformer-based models contribute to more robust and transferable adaptation. The proposed UniMAP framework builds upon these insights by introducing domain-specific prototype distinctions and target-based image matching to improve universal domain adaptation performance without prior category knowledge.

---

### References

\[[2005.10876v1](http://arxiv.org/abs/2005.10876v1)\] http://arxiv.org/abs/1707.09465v5  
\[[2405.19899v1](http://arxiv.org/abs/2405.19899v1)\] http://arxiv.org/abs/2405.19899v1  
\[[2004.01130v2](http://arxiv.org/abs/2004.01130v2)\] http://arxiv.org/abs/2004.01130v2  
\[[2012.12545v1](http://arxiv.org/abs/2012.12545v1)\] http://arxiv.org/abs/2012.12545v1  
\[[2206.03600v2](http://arxiv.org/abs/2206.03600v2)\] http://arxiv.org/abs/1804.08286v1  
\[[2103.16372v1](http://arxiv.org/abs/2103.16372v1)\] http://arxiv.org/abs/2109.14219v1  
\[[2103.15467v2](http://arxiv.org/abs/2103.15467v2)\] http://arxiv.org/abs/2103.15467v2  
\[[2405.06502v1](http://arxiv.org/abs/2405.06502v1)\] http://arxiv.org/abs/2405.06502v1  
\[[2208.14227v2](http://arxiv.org/abs/2208.14227v2)\] http://arxiv.org/abs/2208.14227v2  
\[[1911.11981v2](http://arxiv.org/abs/1911.11981v2)\] http://arxiv.org/abs/1911.11981v2  
\[[2110.10916v1](http://arxiv.org/abs/2110.10916v1)\] http://arxiv.org/abs/2110.10916v1  
\[[2101.00588v3](http://arxiv.org/abs/2101.00588v3)\] http://arxiv.org/abs/2101.00588v3  
\[[2308.13515v5](http://arxiv.org/abs/2308.13515v5)\] http://arxiv.org/abs/2308.13515v5  
\[[2010.12239v3](http://arxiv.org/abs/2010.12239v3)\] http://arxiv.org/abs/2010.12239v3  
\[[2107.09783v3](http://arxiv.org/abs/2107.09783v3)\] http://arxiv.org/abs/2107.09783v3  
\[[2505.15545v3](http://arxiv.org/abs/2505.15545v3)\] http://arxiv.org/abs/2505.15545v3  
\[[2409.18340v1](http://arxiv.org/abs/2409.18340v1)\] http://arxiv.org/abs/2409.18340v1  
\[[2112.03241v1](http://arxiv.org/abs/2112.03241v1)\] http://arxiv.org/abs/2112.03241v1