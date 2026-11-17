## Related Works

Unsupervised domain adaptation (UDA) for semantic segmentation addresses the challenge of transferring knowledge from a labeled source domain to an unlabeled target domain, reducing the dependence on costly pixel-level annotations \[[1411.4038](http://arxiv.org/abs/1411.4038)\]. Traditional UDA methods typically assume shared and known category sets between source and target domains, an assumption that is often violated in real-world scenarios where private classes exist exclusively in the target domain. This mismatch can cause significant performance degradation due to confusion between common and private classes \[[1506.04579](http://arxiv.org/abs/1506.04579)\].

Early works on UDA for segmentation focused on aligning feature distributions or output spaces using adversarial learning \[[1802.10349](http://arxiv.org/abs/1802.10349)\]\[[1901.05427](http://arxiv.org/abs/1901.05427)\]. These methods leverage domain-invariant representations by aligning source and target feature distributions or structured output spaces, often employing multi-level adversarial networks to improve generalization across domains. However, such approaches generally assume full category overlap and do not explicitly handle unknown classes.

Self-training with pseudo-labeling has become a popular paradigm for UDA-SS, where confident predictions on the target domain serve as supervisory signals to iteratively refine the model \[[2012.1584](http://arxiv.org/abs/2012.15840)\]\[[1908.09822](http://arxiv.org/abs/1908.09822)\]\[[2101.10979](http://arxiv.org/abs/2101.10979)\]. Approaches like confidence-regularized self-training mitigate noise in pseudo-labels by employing soft labels or output smoothing \[[1908.09822](http://arxiv.org/abs/1908.09822)\], while prototype-based methods utilize class centroids to denoise pseudo-labels and align target features more compactly \[[2101.10979](http://arxiv.org/abs/2101.10979)\]. Despite their effectiveness, these methods often rely on strong assumptions about category consistency across domains.

Recent advances aim to relax the assumption of known category overlap, addressing Universal Domain Adaptation (UniDA) where the target domain may contain unknown classes absent from the source. Techniques such as entropy-based rejection and neighborhood clustering learn to separate known from unknown classes in a self-supervised manner \[[2002.07953](http://arxiv.org/abs/2002.07953)\]. Similarly, OVANet proposes one-vs-all classifiers trained on source data to learn inter-class distances and adapt thresholds for unknown class rejection without manual tuning \[[2104.03344](http://arxiv.org/abs/2104.03344)\]. These methods demonstrate promising results in open-set or partial domain adaptation settings but are primarily designed for classification tasks rather than dense segmentation.

For semantic segmentation, curriculum learning approaches like PyCDA construct multi-level label distribution constraints to guide adaptation from synthetic to real domains, improving robustness against category shifts \[[1908.09547](http://arxiv.org/abs/1908.09547)\]. Other methods integrate pixel-level style transfer or image-level translation techniques to reduce texture and appearance discrepancies, enhancing domain-invariant feature learning \[[2003.00867](http://arxiv.org/abs/2003.00867)\]\[[1904.1062](http://arxiv.org/abs/1904.10620)\]. Additionally, multi-resolution training strategies combining high and low-resolution inputs help preserve fine object details while capturing long-range context, crucial for domain-adaptive segmentation \[[2204.13132](http://arxiv.org/abs/2204.13132)\].

Architectural innovations have also played a critical role. Transformer-based models such as DAFormer combine a Transformer encoder with context-aware decoders, improving feature extraction and adaptation capability in UDA-SS \[[2111.14887](http://arxiv.org/abs/2111.14887)\]. SegFormer and SETR explore sequence-to-sequence and hierarchical Transformer designs for robust segmentation, highlighting the growing importance of global context modeling in domain adaptation \[[2105.15203](http://arxiv.org/abs/2105.15203)\]\[[2012.1584](http://arxiv.org/abs/2012.15840)\]. These architectures facilitate more effective domain alignment and semantic representation learning.

Furthermore, hybrid approaches synergizing image translation and feature adaptation simultaneously have shown improved performance in cross-modality segmentation tasks, demonstrating the benefit of combining multiple adaptation perspectives \[[1901.08211](http://arxiv.org/abs/1901.08211)\]. Cross-domain mixed sampling techniques like DACS train on mixed source-target samples and their labels/pseudo-labels to stabilize learning and improve generalization \[[2007.08702](http://arxiv.org/abs/2007.08702)\]. Non-adversarial methods that enforce pixelwise consistency under input perturbations also yield strong results with simpler training procedures \[[2105.08128](http://arxiv.org/abs/2105.08128)\].

Despite these advances, few methods explicitly integrate prototype-based distinctions and image-level matching to enhance common class identification in universal domain adaptation for semantic segmentation. The proposed UniMAP framework addresses this gap by introducing domain-specific prototypes to better separate domain features and a target-driven image matching strategy to promote learning of shared classes, enabling robust UniDA-SS without prior knowledge of category overlap.

References:

\[[1411.4038](http://arxiv.org/abs/1411.4038)\] http://arxiv.org/abs/1707.09465  
\[[1506.04579](http://arxiv.org/abs/1506.04579)\] http://arxiv.org/abs/2103.15467v2  
\[[2105.15203](http://arxiv.org/abs/2105.15203)\] http://arxiv.org/abs/2105.15203  
\[[2012.1584](http://arxiv.org/abs/2012.15840)\] http://arxiv.org/abs/2012.15840  
\[[1802.10349](http://arxiv.org/abs/1802.10349)\] http://arxiv.org/abs/1802.10349  
\[[2003.00867](http://arxiv.org/abs/2003.00867)\] http://arxiv.org/abs/2003.00867  
\[[2204.13132](http://arxiv.org/abs/2204.13132)\] http://arxiv.org/abs/2204.13132  
\[[1901.05427](http://arxiv.org/abs/1901.05427)\] http://arxiv.org/abs/1901.05427  
\[[1901.08211](http://arxiv.org/abs/1901.08211)\] http://arxiv.org/abs/1901.08211  
\[[2105.08128](http://arxiv.org/abs/2105.08128)\] http://arxiv.org/abs/2105.08128  
\[[1904.1062](http://arxiv.org/abs/1904.10620)\] http://arxiv.org/abs/1904.10620  
\[[2111.14887](http://arxiv.org/abs/2111.14887)\] http://arxiv.org/abs/2111.14887  
\[[1908.09822](http://arxiv.org/abs/1908.09822)\] http://arxiv.org/abs/1908.09822  
\[[1908.09547](http://arxiv.org/abs/1908.09547)\] http://arxiv.org/abs/1908.09547  
\[[2101.10979](http://arxiv.org/abs/2101.10979)\] http://arxiv.org/abs/2101.10979  
\[[2007.08702](http://arxiv.org/abs/2007.08702)\] http://arxiv.org/abs/2007.08702  
\[[2002.07953](http://arxiv.org/abs/2002.07953)\] http://arxiv.org/abs/2002.07953  
\[[2104.03344](http://arxiv.org/abs/2104.03344)\] http://arxiv.org/abs/2104.03344