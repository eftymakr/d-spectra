## Related Works

Unsupervised domain adaptation (UDA) for semantic segmentation (SS) has been extensively studied to transfer knowledge from a labeled source domain to an unlabeled target domain, reducing costly annotation efforts in new environments \[[2005.10876](http://arxiv.org/abs/2005.10876)\]\[[2112.03241](http://arxiv.org/abs/2112.03241)\]. Traditional UDA-SS methods generally assume that the source and target domains share the same category set, which is unrealistic in many practical scenarios where the target domain may contain private or unknown classes absent in the source domain. This mismatch often leads to degraded performance due to confusion between shared and private categories \[[2405.19899](http://arxiv.org/abs/2405.19899)\]\[[2012.12545](http://arxiv.org/abs/2012.12545)\].

### Standard UDA for Semantic Segmentation

Conventional UDA approaches address the domain gap mainly by aligning distributions at different levels: input image style, feature representations, and output predictions. Adversarial learning-based methods aim to align feature distributions across domains \[[2103.15467](http://arxiv.org/abs/2103.15467)\]\[[1910.13049](http://arxiv.org/abs/1910.13049)\], while self-training with pseudo-labels refines target domain predictions iteratively to improve segmentation accuracy \[[2110.10916](http://arxiv.org/abs/2110.10916)\]\[[2103.16372](http://arxiv.org/abs/2103.16372)\]. Other methods incorporate entropy minimization \[[2208.10716](http://arxiv.org/abs/2208.10716)\] or curriculum learning strategies \[[2005.10876](http://arxiv.org/abs/2005.10876)\]\[[2103.13041](http://arxiv.org/abs/2103.13041)\] to stabilize training and promote domain-invariant features. Recent advances have introduced contrastive learning to enforce class-wise feature alignment, enhancing discriminability in target domains \[[2208.14227](http://arxiv.org/abs/2208.14227)\]. Furthermore, geometric cues such as monocular depth estimation have been leveraged as auxiliary tasks to bridge the synthetic-to-real gap \[[2103.16694](http://arxiv.org/abs/2103.16694)\].

Despite these progresses, these approaches largely rely on the assumption of a shared label space, limiting their robustness when unknown classes emerge in the target domain.

### Adaptation under Unknown or Partial Category Settings

To address scenarios where the category sets differ or are partially known, several specialized frameworks have been proposed. Open-Set Domain Adaptation methods for semantic segmentation explicitly consider unknown classes in the target domain and aim to detect and separate them from known classes using boundary-aware losses and domain mixing augmentations \[[2405.19899](http://arxiv.org/abs/2405.19899)\]. Boundless UDA further extends this by combining domain adaptation with zero-shot learning techniques to explicitly predict never-seen classes at test time \[[2004.0113](http://arxiv.org/abs/2004.01130)\].

Category-adaptive mechanisms have been introduced to manage class imbalance and domain-specific discrepancies at a finer granularity. For example, category-adaptive thresholding selectively balances pseudo-labels across classes to reduce bias towards dominant categories \[[2103.15467](http://arxiv.org/abs/2103.15467)\]\[[2208.10716](http://arxiv.org/abs/2208.10716)\]. Category-conditional alignment employs multi-scale discriminators to encourage class-wise feature alignment, mitigating the issue of low-probability classes being overshadowed \[[1911.11981](http://arxiv.org/abs/1911.11981)\]. Prototype-based methods leverage class centroids or anchors learned from source data to guide feature alignment and pseudo-label refinement, enhancing robustness to domain shifts \[[1910.13049](http://arxiv.org/abs/1910.13049)\]\[[2305.02693](http://arxiv.org/abs/2305.02693)\]\[[2309.1495](http://arxiv.org/abs/2309.14950)\].

Semi-supervised domain adaptation (SSDA) frameworks utilize a small amount of labeled target data alongside abundant labeled source data to reduce both cross-domain and intra-domain gaps. Dual-domain mixing strategies and student-teacher networks have been effective in this setting to exploit unlabeled target data while respecting object boundaries \[[2110.10639](http://arxiv.org/abs/2110.10639)\]\[[2305.02693](http://arxiv.org/abs/2305.02693)\].

### Source-Free and Multi-Target Adaptation

Practical constraints such as privacy or storage often prevent access to source domain data during adaptation. Source-free domain adaptation methods adapt pre-trained source models solely using unlabeled target data, employing self-supervised objectives and normalization statistics adaptation to preserve source knowledge without accessing raw data \[[2103.16372](http://arxiv.org/abs/2103.16372)\]\[[2011.08502](http://arxiv.org/abs/2011.08502)\]\[[2110.06484](http://arxiv.org/abs/2110.06484)\]. Multi-target UDA extends adaptation to multiple target domains, addressing continual or sequential domain shifts by maintaining domain-specific memories and carefully designed adversarial losses to prevent forgetting and promote generalization \[[2405.06502](http://arxiv.org/abs/2405.06502)\]\[[2010.09236](http://arxiv.org/abs/2010.09236)\].

### Techniques for Improved Boundary and Shape Awareness

Accurate delineation of class boundaries is critical for semantic segmentation. Methods incorporating low-level adaptation to sharpen predictions along edges and boundaries have shown improved performance in synthetic-to-real adaptation \[[2110.02833](http://arxiv.org/abs/2110.02833)\]. Contrastive learning and inter-pixel correlation transfer further reinforce spatial consistency and structural knowledge from the source domain to the target \[[2208.14227](http://arxiv.org/abs/2208.14227)\]\[[2110.10916](http://arxiv.org/abs/2110.10916)\]. Image mixing augmentations that combine source and target samples at pixel or region levels help the model learn domain-invariant and shape-consistent features \[[2405.19899](http://arxiv.org/abs/2405.19899)\]\[[2208.10716](http://arxiv.org/abs/2208.10716)\]\[[2110.10639](http://arxiv.org/abs/2110.10639)\].

### Applications Beyond 2D Segmentation

Domain adaptation techniques have also been explored in 3D and LiDAR semantic segmentation, where the domain gap is compounded by sensor differences. Prototype-based pseudo-labeling combined with reconstruction-based pre-training has demonstrated effectiveness in LiDAR UDA \[[2205.11419](http://arxiv.org/abs/2205.11419)\]\[[2107.09783](http://arxiv.org/abs/2107.09783)\]. Multi-view projection and 2D ensemble models have been applied to generate pseudo-labels for 3D point clouds, enabling fine-tuning of 3D segmentation models in the target domain \[[2505.15545](http://arxiv.org/abs/2505.15545)\]\[[2208.0451](http://arxiv.org/abs/2208.04510)\].

### Summary

While extensive research exists for UDA in semantic segmentation, most methods assume known and shared category sets, limiting their applicability in real-world scenarios with unknown or private classes. The UniDA-SS problem setting addresses this gap by handling unknown target categories without prior knowledge. The proposed UniMAP framework innovates by leveraging domain-specific prototypes for class distinction and target-guided source image matching, advancing beyond prior category-adaptive and prototype-based approaches \[[2405.19899](http://arxiv.org/abs/2405.19899)\]\[[2103.15467](http://arxiv.org/abs/2103.15467)\]\[[1910.13049](http://arxiv.org/abs/1910.13049)\]\[[2305.02693](http://arxiv.org/abs/2305.02693)\]. This allows more robust and fine-grained alignment between source and target domains, effectively mitigating confusion caused by private classes and improving common class identification.

---

References:

\[[2405.19899](http://arxiv.org/abs/2405.19899)\] http://arxiv.org/abs/2405.19899  
\[[2110.10639](http://arxiv.org/abs/2110.10639)\] http://arxiv.org/abs/2110.10639  
\[[2012.12545](http://arxiv.org/abs/2012.12545)\] http://arxiv.org/abs/2103.15467  
\[[2103.15467](http://arxiv.org/abs/2103.15467)\] http://arxiv.org/abs/2103.15467  
\[[2005.10876](http://arxiv.org/abs/2005.10876)\] http://arxiv.org/abs/2005.10876  
\[[2103.16372](http://arxiv.org/abs/2103.16372)\] http://arxiv.org/abs/2103.16372  
\[[2405.06502](http://arxiv.org/abs/2405.06502)\] http://arxiv.org/abs/2405.06502  
\[[1910.13049](http://arxiv.org/abs/1910.13049)\] http://arxiv.org/abs/1910.13049  
\[[2208.10716](http://arxiv.org/abs/2208.10716)\] http://arxiv.org/abs/2208.10716  
\[[2205.11419](http://arxiv.org/abs/2205.11419)\] http://arxiv.org/abs/2205.11419  
\[[1911.11981](http://arxiv.org/abs/1911.11981)\] http://arxiv.org/abs/1911.11981  
\[[2107.09783](http://arxiv.org/abs/2107.09783)\] http://arxiv.org/abs/2107.09783  
\[[2110.10916](http://arxiv.org/abs/2110.10916)\] http://arxiv.org/abs/2110.10916  
\[[2208.0451](http://arxiv.org/abs/2208.04510)\] http://arxiv.org/abs/2208.04510  
\[[2103.16694](http://arxiv.org/abs/2103.16694)\] http://arxiv.org/abs/2103.16694  
\[[2011.08502](http://arxiv.org/abs/2011.08502)\] http://arxiv.org/abs/2011.08502  
\[[2208.14227](http://arxiv.org/abs/2208.14227)\] http://arxiv.org/abs/2208.14227  
\[[2004.0113](http://arxiv.org/abs/2004.01130)\] http://arxiv.org/abs/2004.01130  
\[[2010.09236](http://arxiv.org/abs/2010.09236)\] http://arxiv.org/abs/2010.09236  
\[[2103.13041](http://arxiv.org/abs/2103.13041)\] http://arxiv.org/abs/2103.13041  
\[[2112.03241](http://arxiv.org/abs/2112.03241)\] http://arxiv.org/abs/2112.03241  
\[[2110.02833](http://arxiv.org/abs/2110.02833)\] http://arxiv.org/abs/2110.02833  
\[[2505.15545](http://arxiv.org/abs/2505.15545)\] http://arxiv.org/abs/2505.15545  
\[[2110.06484](http://arxiv.org/abs/2110.06484)\] http://arxiv.org/abs/2110.06484  
\[[2305.02693](http://arxiv.org/abs/2305.02693)\] http://arxiv.org/abs/2305.02693  
\[[2309.1495](http://arxiv.org/abs/2309.14950)\] http://arxiv.org/abs/2309.14950