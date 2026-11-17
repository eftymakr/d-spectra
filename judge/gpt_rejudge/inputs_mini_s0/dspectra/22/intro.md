## Related Works

Unsupervised domain adaptation (UDA) for semantic segmentation (UDA-SS) addresses the challenge of transferring knowledge from a labeled source domain to an unlabeled target domain, aiming to reduce the costly requirement for pixel-level annotations in the target domain \[[https://www.semanticscholar.org/paper/5f9ce93f82dcd9b0f9ffe4274b81682f40d86253](https://www.semanticscholar.org/paper/5f9ce93f82dcd9b0f9ffe4274b81682f40d86253)\]\[[2005.10876](http://arxiv.org/abs/2005.10876)\]. Traditional UDA-SS methods generally assume that the source and target domains share identical category sets, an assumption often violated in real-world applications where private classes may exist in either domain, leading to significant performance degradation \[[https://www.semanticscholar.org/paper/6518b0e6334c6ffb9b94c551c57ad79c7008cbb5](https://www.semanticscholar.org/paper/6518b0e6334c6ffb9b94c551c57ad79c7008cbb5)\]\[[https://www.semanticscholar.org/paper/a2e433da83c6e1eb4f4486c900fdfbf1951c4d30](https://www.semanticscholar.org/paper/a2e433da83c6e1eb4f4486c900fdfbf1951c4d30)\].

### Conventional UDA-SS Approaches

Many UDA methods focus on minimizing the domain gap by aligning feature distributions or outputs across domains. Strategies include adversarial learning to reduce domain discrepancy \[[2005.10876](http://arxiv.org/abs/2005.10876)\], self-training with pseudo-labels to iteratively refine target predictions \[[2103.16372](http://arxiv.org/abs/2103.16372)\]\[[2008.12197](http://arxiv.org/abs/2008.12197)\], and entropy minimization to encourage confident predictions on the target domain \[[https://www.semanticscholar.org/paper/6518b0e6334c6ffb9b94c551c57ad79c7008cbb5](https://www.semanticscholar.org/paper/6518b0e6334c6ffb9b94c551c57ad79c7008cbb5)\]\[[2004.08878](http://arxiv.org/abs/2004.08878)\]. Some approaches further incorporate domain-specific priors, such as geometric or depth cues, to enhance adaptation \[[1904.01886](http://arxiv.org/abs/1904.01886)\]\[[2104.13613](http://arxiv.org/abs/2104.13613)\]. For instance, leveraging self-supervised depth estimation has proven effective in refining pseudo-label quality and addressing domain shift in semantic segmentation \[[2104.13613](http://arxiv.org/abs/2104.13613)\].

Advances in network architectures, notably transformer-based encoders combined with multi-level feature fusion, have also contributed to improved UDA performance by better capturing context and reducing source bias \[[2111.14887](http://arxiv.org/abs/2111.14887)\]. Complementary techniques, such as cross-domain mixed sampling \[[2007.08702](http://arxiv.org/abs/2007.08702)\] and category-aware feature alignment \[[1910.13049](http://arxiv.org/abs/1910.13049)\], have been proposed to ameliorate the class imbalance and improve the alignment of semantic categories between domains.

### Source-Free and Model Adaptation Methods

Addressing privacy and data-sharing concerns, source-free domain adaptation methods have emerged, which only require access to a pretrained source model rather than the source data itself. These methods adapt the model to the target domain by reducing uncertainty and leveraging self-supervised learning on unlabeled target data \[[https://www.semanticscholar.org/paper/5f9ce93f82dcd9b0f9ffe4274b81682f40d86253](https://www.semanticscholar.org/paper/5f9ce93f82dcd9b0f9ffe4274b81682f40d86253)\]\[[https://www.semanticscholar.org/paper/6518b0e6334c6ffb9b94c551c57ad79c7008cbb5](https://www.semanticscholar.org/paper/6518b0e6334c6ffb9b94c551c57ad79c7008cbb5)\]\[[2103.16372](http://arxiv.org/abs/2103.16372)\]\[[https://www.semanticscholar.org/paper/2647f5eb86e074bb0300f3ce26b7e1c7ef4e8db3](https://www.semanticscholar.org/paper/2647f5eb86e074bb0300f3ce26b7e1c7ef4e8db3)\]. Techniques like batch normalization statistics adaptation \[[2011.08502](http://arxiv.org/abs/2011.08502)\] and dynamic teacher-student training mechanisms \[[https://www.semanticscholar.org/paper/2647f5eb86e074bb0300f3ce26b7e1c7ef4e8db3](https://www.semanticscholar.org/paper/2647f5eb86e074bb0300f3ce26b7e1c7ef4e8db3)\] have demonstrated state-of-the-art results comparable to traditional UDA that requires source data.

### Handling Unknown and Partial Category Sets

A critical limitation of many UDA-SS approaches is the presumption of known and shared label spaces. In practice, the target domain may contain private classes absent in the source domain, or vice versa, leading to misclassification and confusion. Universal domain adaptation (UniDA) has been proposed to overcome this by enabling models to handle unknown target classes and partial overlap of categories \[[https://www.semanticscholar.org/paper/a2e433da83c6e1eb4f4486c900fdfbf1951c4d30](https://www.semanticscholar.org/paper/a2e433da83c6e1eb4f4486c900fdfbf1951c4d30)\]\[[https://www.semanticscholar.org/paper/d291f7ce81164a2c5a0b9f71ef9227617fbe100c](https://www.semanticscholar.org/paper/d291f7ce81164a2c5a0b9f71ef9227617fbe100c)\]. UniDA methods often focus on discovering common classes between domains and identifying private classes, using strategies such as sample-level transferability estimation and domain consensus clustering to segregate common and private categories effectively \[[https://www.semanticscholar.org/paper/a2e433da83c6e1eb4f4486c900fdfbf1951c4d30](https://www.semanticscholar.org/paper/a2e433da83c6e1eb4f4486c900fdfbf1951c4d30)\]\[[https://www.semanticscholar.org/paper/d291f7ce81164a2c5a0b9f71ef9227617fbe100c](https://www.semanticscholar.org/paper/d291f7ce81164a2c5a0b9f71ef9227617fbe100c)\].

### Prototype-Based and Contrastive Learning Approaches

Prototype learning has gained attention for its ability to capture class-wise representations that support better discrimination between shared and private classes. Category anchor-guided feature alignment \[[1910.13049](http://arxiv.org/abs/1910.13049)\] and contrastive adaptation networks \[[1901.00976](http://arxiv.org/abs/1901.00976)\] enforce intra-class compactness and inter-class separability, which are vital for robust domain adaptation, especially under category shifts.

Additionally, incorporating intra-domain structural knowledge through pixel- and patch-wise self-supervised learning enhances feature robustness and semantic consistency within the target domain \[[2211.07609](http://arxiv.org/abs/2211.07609)\]. Contrastive methods have also been adapted for panoramic semantic segmentation, addressing domain gaps caused by image distortion and style differences by leveraging distortion-aware attention and dual-path feature alignment \[[2308.05493](http://arxiv.org/abs/2308.05493)\]\[[2303.14360](http://arxiv.org/abs/2303.14360)\].

### Pseudo-Label Refinement and Uncertainty Estimation

The quality of pseudo-labels is central to self-training-based UDA-SS methods. Recent work emphasizes rectifying pseudo-label learning by explicitly modeling prediction uncertainty and dynamically setting confidence thresholds to mitigate noise propagation during adaptation \[[2003.03773](http://arxiv.org/abs/2003.03773)\]. Uncertainty-aware consistency regularization further enhances the reliability of pseudo-labels by transferring knowledge from a teacher to a student model under perturbations, improving adaptation stability \[[2004.08878](http://arxiv.org/abs/2004.08878)\].

### Summary

While existing UDA-SS methods have made significant progress, most rely on knowledge of the shared category set, limiting their robustness in the presence of private classes. Universal domain adaptation frameworks address this gap by explicitly handling unknown categories and category mismatches \[[https://www.semanticscholar.org/paper/a2e433da83c6e1eb4f4486c900fdfbf1951c4d30](https://www.semanticscholar.org/paper/a2e433da83c6e1eb4f4486c900fdfbf1951c4d30)\]\[[https://www.semanticscholar.org/paper/d291f7ce81164a2c5a0b9f71ef9227617fbe100c](https://www.semanticscholar.org/paper/d291f7ce81164a2c5a0b9f71ef9227617fbe100c)\]. Prototype-based distinction and image matching strategies, as proposed in UniMAP, align well with recent trends emphasizing fine-grained class separation and dynamic target-guided adaptation, which have shown promising results in advancing domain adaptation robustness under realistic, category-agnostic conditions.

---

**References**

\[[https://www.semanticscholar.org/paper/5f9ce93f82dcd9b0f9ffe4274b81682f40d86253](https://www.semanticscholar.org/paper/5f9ce93f82dcd9b0f9ffe4274b81682f40d86253)\] http://arxiv.org/abs/2103.15467v2  
\[[2308.05493](http://arxiv.org/abs/2308.05493)\] http://arxiv.org/abs/2308.05493v1  
\[[https://www.semanticscholar.org/paper/6518b0e6334c6ffb9b94c551c57ad79c7008cbb5](https://www.semanticscholar.org/paper/6518b0e6334c6ffb9b94c551c57ad79c7008cbb5)\] http://arxiv.org/abs/2103.15467v2  
\[[1910.13049](http://arxiv.org/abs/1910.13049)\] http://arxiv.org/abs/1910.13049v1  
\[[2007.08702](http://arxiv.org/abs/2007.08702)\] http://arxiv.org/abs/2007.08702v1  
\[[2103.16372](http://arxiv.org/abs/2103.16372)\] http://arxiv.org/abs/2409.18340v1  
\[[2111.14887](http://arxiv.org/abs/2111.14887)\] http://arxiv.org/abs/2111.14887v1  
\[[1904.01886](http://arxiv.org/abs/1904.01886)\] http://arxiv.org/abs/2104.13613v1  
\[[2211.07609](http://arxiv.org/abs/2211.07609)\] http://arxiv.org/abs/2211.07609v1  
\[[2004.08878](http://arxiv.org/abs/2004.08878)\] http://arxiv.org/abs/2004.08878v1  
\[[https://www.semanticscholar.org/paper/2647f5eb86e074bb0300f3ce26b7e1c7ef4e8db3](https://www.semanticscholar.org/paper/2647f5eb86e074bb0300f3ce26b7e1c7ef4e8db3)\] https://www.semanticscholar.org/paper/2647f5eb86e074bb0300f3ce26b7e1c7ef4e8db3  
\[[2011.08502](http://arxiv.org/abs/2011.08502)\] http://arxiv.org/abs/2011.08502v1  
\[[1901.00976](http://arxiv.org/abs/1901.00976)\] http://arxiv.org/abs/1901.00976v1  
\[[2303.14360](http://arxiv.org/abs/2303.14360)\] http://arxiv.org/abs/2303.14360v1  
\[[2005.10876](http://arxiv.org/abs/2005.10876)\] http://arxiv.org/abs/2005.10876v1  
\[[2008.12197](http://arxiv.org/abs/2008.12197)\] http://arxiv.org/abs/2008.12197v1  
\[[2003.03773](http://arxiv.org/abs/2003.03773)\] http://arxiv.org/abs/2003.03773v1  
\[[2104.13613](http://arxiv.org/abs/2104.13613)\] http://arxiv.org/abs/2104.13613v1  
\[[https://www.semanticscholar.org/paper/a2e433da83c6e1eb4f4486c900fdfbf1951c4d30](https://www.semanticscholar.org/paper/a2e433da83c6e1eb4f4486c900fdfbf1951c4d30)\] https://www.semanticscholar.org/paper/a2e433da83c6e1eb4f4486c900fdfbf1951c4d30  
\[[https://www.semanticscholar.org/paper/d291f7ce81164a2c5a0b9f71ef9227617fbe100c](https://www.semanticscholar.org/paper/d291f7ce81164a2c5a0b9f71ef9227617fbe100c)\] https://www.semanticscholar.org/paper/d291f7ce81164a2c5a0b9f71ef9227617fbe100c  