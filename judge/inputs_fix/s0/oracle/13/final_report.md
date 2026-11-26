## Related Works

The long-tailed recognition problem, where a few classes dominate the dataset while most are underrepresented, has been extensively studied in recent years. Early approaches focused on class re-balancing strategies such as re-sampling and re-weighting \[[3](http://arxiv.org/abs/1508.03422)\]. However, these methods often fail to address the deeper issues of representation learning in imbalanced data \[[18](http://arxiv.org/abs/2306.15925)\]. More recently, contrastive learning has emerged as a promising approach for learning discriminative visual representations \[[14](http://arxiv.org/abs/2002.05709)\]. 

Contrastive learning methods, such as SimCLR \[[14](http://arxiv.org/abs/2002.05709)\] and MoCo \[[13](http://arxiv.org/abs/1911.05722)\], have demonstrated strong performance on balanced datasets by learning representations that maximize the similarity between positive pairs and minimize it for negative pairs. However, these methods face significant challenges when applied to long-tailed data. For instance, supervised contrastive learning (SCL) \[[16](http://arxiv.org/abs/2004.11362)\] has been shown to struggle with class imbalance due to the need for large batches to construct contrastive pairs that cover all classes. This limitation is particularly problematic in long-tailed scenarios where minority classes are underrepresented \[[17](http://arxiv.org/abs/2403.06726)\].

To address these issues, several works have proposed modifications to contrastive learning. For example, BBN \[[5](http://arxiv.org/abs/1912.02413)\] introduces a bilateral-branch network that separately handles representation learning and classifier learning, achieving state-of-the-art results on long-tailed benchmarks. Similarly, Decoupled Training \[[7](http://arxiv.org/abs/2304.09426)\] decouples the learning of representations from the classifier, leading to improved performance on long-tailed datasets. These approaches highlight the importance of balancing both representation and classification in long-tailed recognition.

Another line of research focuses on logit adjustment techniques to mitigate the bias towards dominant classes. For example, Long-tail learning via logit adjustment \[[8](http://arxiv.org/abs/2007.07314)\] proposes simple modifications to standard softmax cross-entropy training, encouraging a larger margin between logits of rare versus dominant labels. These techniques have been shown to unify and generalize several recent proposals in the literature \[[8](http://arxiv.org/abs/2007.07314)\].

Additionally, contrastive learning has been extended to handle long-tailed data through methods such as Balanced Contrastive Learning (BCL) \[[11](http://arxiv.org/abs/2207.09052)\], which ensures that all classes appear in every mini-batch. This approach helps form a regular simplex in the embedding space, which is crucial for effective representation learning. Furthermore, Probabilistic Contrastive Learning (ProCo) \[[17](http://arxiv.org/abs/2403.06726)\] estimates the distribution of samples from each class in the feature space, enabling the sampling of contrastive pairs without requiring large batches.

In summary, while contrastive learning has shown great promise for representation learning, its application to long-tailed data remains challenging. Recent works have made significant strides in addressing these challenges through novel approaches such as decoupling representation and classifier learning, logit adjustment, and balanced contrastive learning. These methods provide a foundation for further research into long-tailed recognition.

References:  
\[[1](http://arxiv.org/abs/1710.05381)\] http://arxiv.org/abs/1710.05381  
\[[3](http://arxiv.org/abs/1508.03422)\] http://arxiv.org/abs/1901.05555  
\[[5](http://arxiv.org/abs/1912.02413)\] http://arxiv.org/abs/1912.02413  
\[[7](http://arxiv.org/abs/2304.09426)\] http://arxiv.org/abs/2304.09426  
\[[8](http://arxiv.org/abs/2007.07314)\] http://arxiv.org/abs/2007.07314  
\[[11](http://arxiv.org/abs/2207.09052)\] http://arxiv.org/abs/2207.09052  
\[[13](http://arxiv.org/abs/1911.05722)\] http://arxiv.org/abs/1911.05722  
\[[14](http://arxiv.org/abs/2002.05709)\] http://arxiv.org/abs/2002.05709  
\[[16](http://arxiv.org/abs/2004.11362)\] http://arxiv.org/abs/2004.11362  
\[[17](http://arxiv.org/abs/2403.06726)\] http://arxiv.org/abs/2403.06726
## Research papers
### Outline
- [Class Re-balancing Strategies [1 papers]](#category-class-re-balancing-strategies)
- [Long-tailed Recognition Frameworks [6 papers]](#category-long-tailed-recognition-frameworks)
- [Decoupled Training Approaches [2 papers]](#category-decoupled-training-approaches)
- [Logit Adjustment Techniques [1 papers]](#category-logit-adjustment-techniques)
- [Contrastive Learning Methods [8 papers]](#category-contrastive-learning-methods)
- [Balanced Contrastive Learning [1 papers]](#category-balanced-contrastive-learning)
- [Probabilistic Contrastive Learning [1 papers]](#category-probabilistic-contrastive-learning)
- [Representation Learning Challenges [3 papers]](#category-representation-learning-challenges)

### <a id='category-class-re-balancing-strategies'></a>Class Re-balancing Strategies: 1 papers found.
Context: 
	Document 1: [Category]: «Class Re-balancing Strategies»
[_citation_number]: «1»
[Snippet]: «In this study, we systematically investigate the impact of class imbalance on classification performance of convolutional neural networks (CNNs) and compare frequently used methods to address the issue. Class imbalance is a common problem that has been comprehensively studied in classical machine learning, yet very limited systematic research is available in the context of deep learning. In our study, we use three benchmark datasets of increasing complexity, MNIST, CIFAR-10 and ImageNet, to investigate the effects of imbalance on classification and perform an extensive comparison of several methods to address the issue: oversampling, undersampling, two-phase training, and thresholding that compensates for prior class probabilities. Our main evaluation metric is area under the receiver operating characteristic curve (ROC AUC) adjusted to multi-class tasks since overall accuracy metric is associated with notable difficulties in the context of imbalanced data. Based on results from our experiments we conclude that (i) the effect of class imbalance on classification performance is detrimental; (ii) the method of addressing class imbalance that emerged as dominant in almost all analyzed scenarios was oversampling; (iii) oversampling should be applied to the level that completely eliminates the imbalance, whereas the optimal undersampling ratio depends on the extent of imbalance; (iv) as opposed to some classical machine learning models, oversampling does not cause overfitting of CNNs; (v) thresholding should be applied to compensate for prior class probabilities when overall number of properly classified cases is of interest.»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-06-01T16:19:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1508.03422)\]. Further details \[[6](http://arxiv.org/abs/2110.04596)\]\[[7](http://arxiv.org/abs/2304.09426)\]\[[8](http://arxiv.org/abs/2007.07314)\]\[[9](http://arxiv.org/abs/2107.12028)\]\[[10](http://arxiv.org/abs/2209.12400)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In this paper, we propose an Aligned Contrastive Learning (ACL) algorithm to address the long-tailed recognition problem. Our findings indicate that while multi-view training boosts the performance, contrastive learning does not consistently enhance model generalization as the number of views increases. Through theoretical gradient analysis of supervised contrastive learning (SCL), we identify gradient conflicts, and imbalanced attraction and repulsion gradients between positive and negative pairs as the underlying issues. Our ACL algorithm is designed to eliminate these problems and demonstrates strong performance across multiple benchmarks. We validate the effectiveness of ACL through experiments on long-tailed CIFAR, ImageNet, Places, and iNaturalist datasets. Results show that ACL achieves new state-of-the-art performance.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1508.03422)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1901.05555)\]\[[7](http://arxiv.org/abs/2304.09426)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Class imbalance remains a significant challenge in deep learning, particularly in convolutional neural networks (CNNs), where it negatively impacts classification performance \[[1](http://arxiv.org/abs/1710.05381)\]. Various strategies have been proposed to address this issue, including oversampling, undersampling, two-phase training, and thresholding methods that adjust for prior class probabilities \[[1](http://arxiv.org/abs/1710.05381)\]. Among these, oversampling has emerged as a dominant approach, with studies indicating that it can effectively eliminate class imbalance without causing overfitting in CNNs \[[1](http://arxiv.org/abs/1710.05381)\]. However, the optimal level of oversampling and the appropriate undersampling ratio depend on the specific dataset and the degree of imbalance \[[1](http://arxiv.org/abs/1710.05381)\]. Additionally, thresholding methods have been suggested as a viable alternative when the goal is to maximize the number of correctly classified instances \[[1](http://arxiv.org/abs/1710.05381)\]. These findings highlight the importance of carefully selecting and tuning class re-balancing strategies to achieve robust performance in imbalanced classification tasks.
|    | reference                                                                                                               |   date | key idea/summary                                                                                                                                                                                           |
|----|-------------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [A systematic study of the class imbalance problem in convolutional
  neural networks](http://arxiv.org/abs/1710.05381) |    nan | This study investigates the impact of class imbalance on CNN classification performance and finds that oversampling is the most effective method, often eliminating imbalance without causing overfitting. |
### <a id='category-long-tailed-recognition-frameworks'></a>Long-tailed Recognition Frameworks: 6 papers found.
Context: 
	Document 1: [Category]: «Long-tailed Recognition Frameworks»
[_citation_number]: «2»
[Snippet]: «With the rapid increase of large-scale, real-world datasets, it becomes
critical to address the problem of long-tailed data distribution (i.e., a few
classes account for most of the data, while most classes are
under-represented). Existing solutions typically adopt class re-balancing
strategies such as re-sampling and re-weighting based on the number of
observations for each class. In this work, we argue that as the number of
samples increases, the additional benefit of a newly added data point will
diminish. We introduce a novel theoretical framework to measure data overlap by
associating with each sample a small neighboring region rather than a single
point. The effective number of samples is defined as the volume of samples and
can be calculated by a simple formula $(1-\beta^(n))/(1-\beta)$, where $n$ is
the number of samples and $\beta \in [0,1)$ is a hyperparameter. We design a
re-weighting scheme that uses the effective number of samples for each class to
re-balance the loss, thereby yielding a class-balanced loss. Comprehensive
experiments are conducted on artificially induced long-tailed CIFAR datasets
and large-scale datasets including ImageNet and iNaturalist. Our results show
that when trained with the proposed class-balanced loss, the network is able to
achieve significant performance gains on long-tailed datasets.»

	Document 2: [Category]: «Long-tailed Recognition Frameworks»
[_citation_number]: «3»
[Snippet]: «Class imbalance is a common problem in the case of real-world object
detection and classification tasks. Data of some classes is abundant making
them an over-represented majority, and data of other classes is scarce, making
them an under-represented minority. This imbalance makes it challenging for a
classifier to appropriately learn the discriminating boundaries of the majority
and minority classes. In this work, we propose a cost sensitive deep neural
network which can automatically learn robust feature representations for both
the majority and minority classes. During training, our learning procedure
jointly optimizes the class dependent costs and the neural network parameters.
The proposed approach is applicable to both binary and multi-class problems
without any modification. Moreover, as opposed to data level approaches, we do
not alter the original data distribution which results in a lower computational
cost during the training process. We report the results of our experiments on
six major image classification datasets and show that the proposed approach
significantly outperforms the baseline algorithms. Comparisons with popular
data sampling techniques and cost sensitive classifiers demonstrate the
superior performance of our proposed method.»

	Document 3: [Category]: «Long-tailed Recognition Frameworks»
[_citation_number]: «5»
[Snippet]: «Our work focuses on tackling the challenging but natural visual recognition
task of long-tailed data distribution (i.e., a few classes occupy most of the
data, while most classes have rarely few samples). In the literature, class
re-balancing strategies (e.g., re-weighting and re-sampling) are the prominent
and effective methods proposed to alleviate the extreme imbalance for dealing
with long-tailed problems. In this paper, we firstly discover that these
re-balancing methods achieving satisfactory recognition accuracy owe to that
they could significantly promote the classifier learning of deep networks.
However, at the same time, they will unexpectedly damage the representative
ability of the learned deep features to some extent. Therefore, we propose a
unified Bilateral-Branch Network (BBN) to take care of both representation
learning and classifier learning simultaneously, where each branch does perform
its own duty separately. In particular, our BBN model is further equipped with
a novel cumulative learning strategy, which is designed to first learn the
universal patterns and then pay attention to the tail data gradually. Extensive
experiments on four benchmark datasets, including the large-scale iNaturalist
ones, justify that the proposed BBN can significantly outperform
state-of-the-art methods. Furthermore, validation experiments can demonstrate
both our preliminary discovery and effectiveness of tailored designs in BBN for
long-tailed problems. Our method won the first place in the iNaturalist 2019
large scale species classification competition, and our code is open-source and
available at https://github.com/Megvii-Nanjing/BBN.»

	Document 4: [Category]: «Long-tailed Recognition Frameworks»
[_citation_number]: «6»
[Snippet]: «Deep long-tailed learning, one of the most challenging problems in visual
recognition, aims to train well-performing deep models from a large number of
images that follow a long-tailed class distribution. In the last decade, deep
learning has emerged as a powerful recognition model for learning high-quality
image representations and has led to remarkable breakthroughs in generic visual
recognition. However, long-tailed class imbalance, a common problem in
practical visual recognition tasks, often limits the practicality of deep
network based recognition models in real-world applications, since they can be
easily biased towards dominant classes and perform poorly on tail classes. To
address this problem, a large number of studies have been conducted in recent
years, making promising progress in the field of deep long-tailed learning.
Considering the rapid evolution of this field, this paper aims to provide a
comprehensive survey on recent advances in deep long-tailed learning. To be
specific, we group existing deep long-tailed learning studies into three main
categories (i.e., class re-balancing, information augmentation and module
improvement), and review these methods following this taxonomy in detail.
Afterward, we empirically analyze several state-of-the-art methods by
evaluating to what extent they address the issue of class imbalance via a newly
proposed evaluation metric, i.e., relative accuracy. We conclude the survey by
highlighting important applications of deep long-tailed learning and
identifying several promising directions for future research.»

	Document 5: [Category]: «Long-tailed Recognition Frameworks»
[_citation_number]: «12»
[Snippet]: «Although contrastive learning methods have shown prevailing performance on a
variety of representation learning tasks, they encounter difficulty when the
training dataset is long-tailed. Many researchers have combined contrastive
learning and a logit adjustment technique to address this problem, but the
combinations are done ad-hoc and a theoretical background has not yet been
provided. The goal of this paper is to provide the background and further
improve the performance. First, we show that the fundamental reason contrastive
learning methods struggle with long-tailed tasks is that they try to maximize
the mutual information maximization between latent features and input data. As
ground-truth labels are not considered in the maximization, they are not able
to address imbalances between class labels. Rather, we interpret the
long-tailed recognition task as a mutual information maximization between
latent features and ground-truth labels. This approach integrates contrastive
learning and logit adjustment seamlessly to derive a loss function that shows
state-of-the-art performance on long-tailed recognition benchmarks. It also
demonstrates its efficacy in image segmentation tasks, verifying its
versatility beyond image classification.»

	Document 6: [Category]: «Long-tailed Recognition Frameworks»
[_citation_number]: «18»
[Snippet]: «Long-tailed recognition with imbalanced class distribution naturally emerges
in practical machine learning applications. Existing methods such as data
reweighing, resampling, and supervised contrastive learning enforce the class
balance with a price of introducing imbalance between instances of head class
and tail class, which may ignore the underlying rich semantic substructures of
the former and exaggerate the biases in the latter. We overcome these drawbacks
by a novel ``subclass-balancing contrastive learning (SBCL)'' approach that
clusters each head class into multiple subclasses of similar sizes as the tail
classes and enforce representations to capture the two-layer class hierarchy
between the original classes and their subclasses. Since the clustering is
conducted in the representation space and updated during the course of
training, the subclass labels preserve the semantic substructures of head
classes. Meanwhile, it does not overemphasize tail class samples, so each
individual instance contribute to the representation learning equally. Hence,
our method achieves both the instance- and subclass-balance, while the original
class labels are also learned through contrastive learning among subclasses
from different classes. We evaluate SBCL over a list of long-tailed benchmark
datasets and it achieves the state-of-the-art performance. In addition, we
present extensive analyses and ablation studies of SBCL to verify its
advantages.»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-06-01T16:19:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1508.03422)\]. Further details \[[6](http://arxiv.org/abs/2110.04596)\]\[[7](http://arxiv.org/abs/2304.09426)\]\[[8](http://arxiv.org/abs/2007.07314)\]\[[9](http://arxiv.org/abs/2107.12028)\]\[[10](http://arxiv.org/abs/2209.12400)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In this paper, we propose an Aligned Contrastive Learning (ACL) algorithm to
address the long-tailed recognition problem. Our findings indicate that while
multi-view training boosts the performance, contrastive learning does not
consistently enhance model generalization as the number of views increases.
Through theoretical gradient analysis of supervised contrastive learning (SCL),
we identify gradient conflicts, and imbalanced attraction and repulsion
gradients between positive and negative pairs as the underlying issues. Our ACL
algorithm is designed to eliminate these problems and demonstrates strong
performance across multiple benchmarks. We validate the effectiveness of ACL
through experiments on long-tailed CIFAR, ImageNet, Places, and iNaturalist
datasets. Results show that ACL achieves new state-of-the-art performance.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1508.03422)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1901.05555)\]\[[7](http://arxiv.org/abs/2304.09426)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer:  
The long-tailed recognition problem, characterized by a few classes dominating the dataset while most classes are under-represented, has been extensively studied in recent years \[[6](http://arxiv.org/abs/2110.04596)\]. Existing approaches often rely on class re-balancing strategies such as re-sampling or re-weighting \[[2](http://arxiv.org/abs/1901.05555)\], but these methods can inadvertently degrade the quality of learned features \[[5](http://arxiv.org/abs/1912.02413)\]. To address these limitations, researchers have proposed advanced frameworks like the Bilateral-Branch Network (BBN), which simultaneously improves representation learning and classifier performance by introducing a cumulative learning strategy \[[5](http://arxiv.org/abs/1912.02413)\]. Additionally, contrastive learning has been explored as a promising direction, with some studies combining it with logit adjustment to mitigate class imbalance \[[12](http://arxiv.org/abs/2305.01160)\]. However, these methods often face challenges in maintaining balance between head and tail classes, leading to semantic distortion in feature learning \[[18](http://arxiv.org/abs/2306.15925)\]. Recent works have also highlighted the importance of theoretical analysis in understanding the limitations of contrastive learning, such as gradient conflicts and imbalanced attraction/repulsion gradients \[[12](http://arxiv.org/abs/2305.01160)\]. These findings underscore the need for more robust and theoretically grounded solutions, such as the proposed Aligned Contrastive Learning (ACL) algorithm, which aims to eliminate these issues and improve generalization across benchmarks \[[1](http://arxiv.org/abs/1710.05381)\].
|    | reference                                                                                                                                       |   date | key idea/summary                                                                                                                                                                                                                                                                  |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Class-Balanced Loss Based on Effective Number of Samples](http://arxiv.org/abs/1901.05555)                                                     |    nan | The paper introduces a novel theoretical framework to address long-tailed data distribution by defining an effective number of samples and using it to design a re-weighting scheme for class-balanced loss, achieving significant performance gains on long-tailed datasets.     |
|  1 | [Cost Sensitive Learning of Deep Feature Representations from Imbalanced
  Data](http://arxiv.org/abs/1508.03422)                               |    nan | The paper proposes a cost-sensitive deep neural network to address class imbalance in object detection and classification by jointly optimizing class-dependent costs and network parameters, achieving superior performance without altering data distribution.                  |
|  2 | [BBN: Bilateral-Branch Network with Cumulative Learning for Long-Tailed
  Visual Recognition](http://arxiv.org/abs/1912.02413)                  |    nan | The paper introduces a Bilateral-Branch Network (BBN) that simultaneously improves representation learning and classifier learning for long-tailed data distribution, achieving state-of-the-art results on benchmark datasets.                                                   |
|  3 | [Deep Long-Tailed Learning: A Survey](http://arxiv.org/abs/2110.04596)                                                                          |    nan | This paper provides a comprehensive survey on recent advances in deep long-tailed learning, categorizing existing methods into class re-balancing, information augmentation, and module improvement, and introduces a new evaluation metric to assess class imbalance addressing. |
|  4 | [Long-Tailed Recognition by Mutual Information Maximization between
  Latent Features and Ground-Truth Labels](http://arxiv.org/abs/2305.01160) |    nan | This paper addresses the challenge of long-tailed recognition tasks by integrating contrastive learning with logit adjustment, proposing a loss function that improves performance through a novel interpretation of mutual information maximization with ground-truth labels.    |
|  5 | [Subclass-balancing Contrastive Learning for Long-tailed Recognition](http://arxiv.org/abs/2306.15925)                                          |    nan | The paper introduces a novel subclass-balancing contrastive learning (SBCL) approach to address long-tailed recognition by clustering head classes into subclasses and enforcing a two-layer class hierarchy, achieving both instance- and subclass-level balance.                |
### <a id='category-decoupled-training-approaches'></a>Decoupled Training Approaches: 2 papers found.
Context: 
	Document 1: [Category]: «Decoupled Training Approaches»
[_citation_number]: «4»
[Snippet]: «The long-tail distribution of the visual world poses great challenges for
deep learning based classification models on how to handle the class imbalance
problem. Existing solutions usually involve class-balancing strategies, e.g.,
by loss re-weighting, data re-sampling, or transfer learning from head- to
tail-classes, but most of them adhere to the scheme of jointly learning
representations and classifiers. In this work, we decouple the learning
procedure into representation learning and classification, and systematically
explore how different balancing strategies affect them for long-tailed
recognition. The findings are surprising: (1) data imbalance might not be an
issue in learning high-quality representations; (2) with representations
learned with the simplest instance-balanced (natural) sampling, it is also
possible to achieve strong long-tailed recognition ability by adjusting only
the classifier. We conduct extensive experiments and set new state-of-the-art
performance on common long-tailed benchmarks like ImageNet-LT, Places-LT and
iNaturalist, showing that it is possible to outperform carefully designed
losses, sampling strategies, even complex modules with memory, by using a
straightforward approach that decouples representation and classification. Our
code is available at https://github.com/facebookresearch/classifier-balancing.»

	Document 2: [Category]: «Decoupled Training Approaches»
[_citation_number]: «7»
[Snippet]: «Decoupling representation learning and classifier learning has been shown to
be effective in classification with long-tailed data. There are two main
ingredients in constructing a decoupled learning scheme; 1) how to train the
feature extractor for representation learning so that it provides generalizable
representations and 2) how to re-train the classifier that constructs proper
decision boundaries by handling class imbalances in long-tailed data. In this
work, we first apply Stochastic Weight Averaging (SWA), an optimization
technique for improving the generalization of deep neural networks, to obtain
better generalizing feature extractors for long-tailed classification. We then
propose a novel classifier re-training algorithm based on stochastic
representation obtained from the SWA-Gaussian, a Gaussian perturbed SWA, and a
self-distillation strategy that can harness the diverse stochastic
representations based on uncertainty estimates to build more robust
classifiers. Extensive experiments on CIFAR10/100-LT, ImageNet-LT, and
iNaturalist-2018 benchmarks show that our proposed method improves upon
previous methods both in terms of prediction accuracy and uncertainty
estimation.»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-06-01T16:19:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1508.03422)\]. Further details \[[6](http://arxiv.org/abs/2110.04596)\]\[[7](http://arxiv.org/abs/2304.09426)\]\[[8](http://arxiv.org/abs/2007.07314)\]\[[9](http://arxiv.org/abs/2107.12028)\]\[[10](http://arxiv.org/abs/2209.12400)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In this paper, we propose an Aligned Contrastive Learning (ACL) algorithm to
address the long-tailed recognition problem. Our findings indicate that while
multi-view training boosts the performance, contrastive learning does not
consistently enhance model generalization as the number of views increases.
Through theoretical gradient analysis of supervised contrastive learning (SCL),
we identify gradient conflicts, and imbalanced attraction and repulsion
gradients between positive and negative pairs as the underlying issues. Our ACL
algorithm is designed to eliminate these problems and demonstrates strong
performance across multiple benchmarks. We validate the effectiveness of ACL
through experiments on long-tailed CIFAR, ImageNet, Places, and iNaturalist
datasets. Results show that ACL achieves new state-of-the-art performance.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1508.03422)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1901.05555)\]\[[7](http://arxiv.org/abs/2304.09426)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer:  
Decoupled training approaches have emerged as a promising strategy for addressing the challenges of long-tailed recognition. These methods aim to separate the learning of representations from the learning of classifiers, allowing for more flexible and effective handling of class imbalance \[[4](http://arxiv.org/abs/1910.09217)\]. This decoupling enables the exploration of how different balancing strategies affect each component independently. For instance, some studies suggest that data imbalance might not hinder the learning of high-quality representations, and that strong long-tailed recognition can be achieved by simply adjusting the classifier after learning representations with instance-balanced sampling \[[4](http://arxiv.org/abs/1910.09217)\]. Additionally, recent work has focused on improving the generalization of feature extractors through techniques like Stochastic Weight Averaging (SWA), which helps in obtaining more robust and generalizable representations \[[7](http://arxiv.org/abs/2304.09426)\]. These approaches highlight the potential of decoupled training to outperform traditional methods that jointly optimize both representation and classification, offering a simpler yet effective alternative for long-tailed classification tasks.
|    | reference                                                                                                              |   date | key idea/summary                                                                                                                                                                                                                                                           |
|----|------------------------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Decoupling Representation and Classifier for Long-Tailed Recognition](http://arxiv.org/abs/1910.09217)                |    nan | This work decouples representation learning and classification in long-tailed recognition, showing that simple instance-balanced sampling and adjusting the classifier can achieve state-of-the-art performance without complex strategies.                                |
|  1 | [Decoupled Training for Long-Tailed Classification With Stochastic
  Representations](http://arxiv.org/abs/2304.09426) |    nan | The paper proposes a method that decouples representation learning and classifier learning for long-tailed classification, using Stochastic Weight Averaging (SWA) and a novel classifier re-training algorithm to improve prediction accuracy and uncertainty estimation. |
### <a id='category-logit-adjustment-techniques'></a>Logit Adjustment Techniques: 1 papers found.
Context: 
	Document 1: [Category]: «Logit Adjustment Techniques»
[_citation_number]: «8»
[Snippet]: «Real-world classification problems typically exhibit an imbalanced or
long-tailed label distribution, wherein many labels are associated with only a
few samples. This poses a challenge for generalisation on such labels, and also
makes na\"ive learning biased towards dominant labels. In this paper, we
present two simple modifications of standard softmax cross-entropy training to
cope with these challenges. Our techniques revisit the classic idea of logit
adjustment based on the label frequencies, either applied post-hoc to a trained
model, or enforced in the loss during training. Such adjustment encourages a
large relative margin between logits of rare versus dominant labels. These
techniques unify and generalise several recent proposals in the literature,
while possessing firmer statistical grounding and empirical performance.»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-06-01T16:19:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1508.03422)\]. Further details \[[6](http://arxiv.org/abs/2110.04596)\]\[[7](http://arxiv.org/abs/2304.09426)\]\[[8](http://arxiv.org/abs/2007.07314)\]\[[9](http://arxiv.org/abs/2107.12028)\]\[[10](http://arxiv.org/abs/2209.12400)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In this paper, we propose an Aligned Contrastive Learning (ACL) algorithm to
address the long-tailed recognition problem. Our findings indicate that while
multi-view training boosts the performance, contrastive learning does not
consistently enhance model generalization as the number of views increases.
Through theoretical gradient analysis of supervised contrastive learning (SCL),
we identify gradient conflicts, and imbalanced attraction and repulsion
gradients between positive and negative pairs as the underlying issues. Our ACL
algorithm is designed to eliminate these problems and demonstrates strong
performance across multiple benchmarks. We validate the effectiveness of ACL
through experiments on long-tailed CIFAR, ImageNet, Places, and iNaturalist
datasets. Results show that ACL achieves new state-of-the-art performance.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1508.03422)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1901.05555)\]\[[7](http://arxiv.org/abs/2304.09426)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Logit adjustment techniques have been widely explored to address the challenges posed by imbalanced or long-tailed label distributions in real-world classification tasks \[[8](http://arxiv.org/abs/2007.07314)\]. These techniques aim to mitigate the bias towards dominant labels and improve generalization on rare labels by modifying the standard softmax cross-entropy training. Approaches such as post-hoc logit adjustment or enforcing adjustments during training have been proposed to create a larger relative margin between logits of rare and dominant labels \[[8](http://arxiv.org/abs/2007.07314)\]. Such methods not only unify and generalize several recent proposals in the literature but also offer a firmer statistical foundation and better empirical performance \[[8](http://arxiv.org/abs/2007.07314)\]. These techniques are particularly relevant in the context of long-tailed recognition problems, where the imbalance in label frequencies can significantly affect model performance.
|    | reference                                                                  |   date | key idea/summary                                                                                                                                                                                                |
|----|----------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Long-tail learning via logit adjustment](http://arxiv.org/abs/2007.07314) |    nan | The paper introduces two modifications to standard softmax cross-entropy training to address imbalanced or long-tailed label distributions, improving generalization and reducing bias towards dominant labels. |
### <a id='category-contrastive-learning-methods'></a>Contrastive Learning Methods: 8 papers found.
Contrastive learning methods have been extensively explored for improving representation learning in both supervised and unsupervised settings, with particular focus on addressing long-tailed recognition and enhancing generalization. Several approaches, such as Parametric Contrastive Learning (PaCo) \[[9](http://arxiv.org/abs/2107.12028)\], Generalized Parametric Contrastive Learning (GPaCo) \[[10](http://arxiv.org/abs/2209.12400)\], and Targeted Supervised Contrastive Learning (TSC) \[[17](http://arxiv.org/abs/2403.06726)\], have been proposed to mitigate class imbalance by introducing learnable class-wise centers or enforcing uniformity in feature space. These methods aim to rebalance the optimization process by adjusting the influence of high-frequency classes and improving the separability of minority class samples. Additionally, methods like SimCLR \[[14](http://arxiv.org/abs/2002.05709)\] and MoCo \[[13](http://arxiv.org/abs/1911.05722)\] have demonstrated the effectiveness of contrastive learning in self-supervised settings, leveraging data augmentations and dynamic dictionaries to learn robust representations. The supervised contrastive (SupCon) loss \[[16](http://arxiv.org/abs/2004.11362)\] has also been adapted to leverage label information, achieving competitive performance on ImageNet. However, challenges such as gradient conflicts and imbalanced attraction/repulsion gradients in supervised contrastive learning \[[1](http://arxiv.org/abs/1710.05381)\] remain, motivating further research into aligned contrastive learning strategies.
|    | reference                                                                                                        |   date | key idea/summary                                                                                                                                                                                                                                                                 |
|----|------------------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Parametric Contrastive Learning](http://arxiv.org/abs/2107.12028)                                               |    nan | Parametric Contrastive Learning (PaCo) addresses long-tailed recognition by introducing class-wise learnable centers to rebalance the supervised contrastive loss, achieving state-of-the-art results on multiple datasets.                                                      |
|  1 | [Generalized Parametric Contrastive Learning](http://arxiv.org/abs/2209.12400)                                   |    nan | The paper introduces GPaCo/PaCo, a parametric contrastive learning method that addresses imbalanced data by introducing class-wise learnable centers, achieving state-of-the-art results in long-tailed recognition and improved generalization across various models and tasks. |
|  2 | [Momentum Contrast for Unsupervised Visual Representation Learning](http://arxiv.org/abs/1911.05722)             |    nan | Momentum Contrast (MoCo) is an unsupervised visual representation learning method that uses a dynamic dictionary and moving-averaged encoder to achieve competitive results, often outperforming supervised pre-training in downstream tasks.                                    |
|  3 | [A Simple Framework for Contrastive Learning of Visual Representations](http://arxiv.org/abs/2002.05709)         |    nan | SimCLR is a simple contrastive learning framework that achieves state-of-the-art results in self-supervised and semi-supervised learning on ImageNet by improving data augmentation, nonlinear transformations, and training strategies.                                         |
|  4 | [Bootstrap your own latent: A new approach to self-supervised Learning](http://arxiv.org/abs/2006.07733)         |    nan | BYOL is a self-supervised image representation learning method that uses two interacting networks (online and target) to achieve state-of-the-art results without relying on negative pairs.                                                                                     |
|  5 | [Supervised Contrastive Learning](http://arxiv.org/abs/2004.11362)                                               |    nan | This work introduces a supervised contrastive loss function that outperforms cross-entropy and traditional contrastive losses, achieving state-of-the-art results on ImageNet with ResNet-200.                                                                                   |
|  6 | [Targeted Supervised Contrastive Learning for Long-Tailed Recognition](http://arxiv.org/abs/2111.13998)          |    nan | The paper introduces Targeted Supervised Contrastive Learning (TSC) to address class imbalance in long-tailed recognition by improving feature uniformity and class separability through uniformly distributed targets on a hypersphere.                                         |
|  7 | [Unsupervised Learning of Visual Features by Contrasting Cluster
  Assignments](http://arxiv.org/abs/2006.09882) |    nan | The paper introduces SwAV, an online contrastive learning method that avoids explicit pairwise feature comparisons by using a swapped prediction mechanism, enabling efficient and scalable training with improved memory efficiency and performance on transfer tasks.          |
### <a id='category-balanced-contrastive-learning'></a>Balanced Contrastive Learning: 1 papers found.
Context: 
	Document 1: [Category]: «Balanced Contrastive Learning»
[_citation_number]: «11»
[Snippet]: «Real-world data typically follow a long-tailed distribution, where a few
majority categories occupy most of the data while most minority categories
contain a limited number of samples. Classification models minimizing
cross-entropy struggle to represent and classify the tail classes. Although the
problem of learning unbiased classifiers has been well studied, methods for
representing imbalanced data are under-explored. In this paper, we focus on
representation learning for imbalanced data. Recently, supervised contrastive
learning has shown promising performance on balanced data recently. However,
through our theoretical analysis, we find that for long-tailed data, it fails
to form a regular simplex which is an ideal geometric configuration for
representation learning. To correct the optimization behavior of SCL and
further improve the performance of long-tailed visual recognition, we propose a
novel loss for balanced contrastive learning (BCL). Compared with SCL, we have
two improvements in BCL: class-averaging, which balances the gradient
contribution of negative classes; class-complement, which allows all classes to
appear in every mini-batch. The proposed balanced contrastive learning (BCL)
method satisfies the condition of forming a regular simplex and assists the
optimization of cross-entropy. Equipped with BCL, the proposed two-branch
framework can obtain a stronger feature representation and achieve competitive
performance on long-tailed benchmark datasets such as CIFAR-10-LT,
CIFAR-100-LT, ImageNet-LT, and iNaturalist2018. Our code is available at
https://github.com/FlamieZhu/BCL .»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-06-01T16:19:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1508.03422)\]. Further details \[[6](http://arxiv.org/abs/2110.04596)\]\[[7](http://arxiv.org/abs/2304.09426)\]\[[8](http://arxiv.org/abs/2007.07314)\]\[[9](http://arxiv.org/abs/2107.12028)\]\[[10](http://arxiv.org/abs/2209.12400)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In this paper, we propose an Aligned Contrastive Learning (ACL) algorithm to
address the long-tailed recognition problem. Our findings indicate that while
multi-view training boosts the performance, contrastive learning does not
consistently enhance model generalization as the number of views increases.
Through theoretical gradient analysis of supervised contrastive learning (SCL),
we identify gradient conflicts, and imbalanced attraction and repulsion
gradients between positive and negative pairs as the underlying issues. Our ACL
algorithm is designed to eliminate these problems and demonstrates strong
performance across multiple benchmarks. We validate the effectiveness of ACL
through experiments on long-tailed CIFAR, ImageNet, Places, and iNaturalist
datasets. Results show that ACL achieves new state-of-the-art performance.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1508.03422)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1901.05555)\]\[[7](http://arxiv.org/abs/2304.09426)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
The category of Balanced Contrastive Learning addresses the challenge of representation learning in imbalanced datasets, particularly those with long-tailed distributions \[[11](http://arxiv.org/abs/2207.09052)\]. In such scenarios, traditional classification models struggle to effectively represent and classify minority classes due to the imbalance in data distribution \[[11](http://arxiv.org/abs/2207.09052)\]. While supervised contrastive learning (SCL) has shown promise in balanced settings, it fails to form a regular simplex—a geometric configuration crucial for effective representation learning—when applied to long-tailed data \[[11](http://arxiv.org/abs/2207.09052)\]. This limitation leads to suboptimal performance in visual recognition tasks. To address these issues, the Balanced Contrastive Learning (BCL) method introduces two key improvements: class-averaging, which balances the gradient contributions of negative classes, and class-complement, which ensures that all classes are represented in every mini-batch \[[11](http://arxiv.org/abs/2207.09052)\]. These modifications enable the formation of a regular simplex and enhance the optimization of cross-entropy, leading to stronger feature representations and competitive performance on long-tailed benchmarks such as CIFAR-10-LT, CIFAR-100-LT, ImageNet-LT, and iNaturalist2018 \[[11](http://arxiv.org/abs/2207.09052)\].
|    | reference                                                                                           |   date | key idea/summary                                                                                                                                                                                                                                                                        |
|----|-----------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Balanced Contrastive Learning for Long-Tailed Visual Recognition](http://arxiv.org/abs/2207.09052) |    nan | The paper proposes a novel loss function called Balanced Contrastive Learning (BCL) to address the challenges of representation learning for long-tailed data, improving performance on imbalanced datasets by balancing gradient contributions and ensuring regular simplex formation. |
### <a id='category-probabilistic-contrastive-learning'></a>Probabilistic Contrastive Learning: 1 papers found.
Context: 
	Document 1: [Category]: «Probabilistic Contrastive Learning»
[_citation_number]: «17»
[Snippet]: «Long-tailed distributions frequently emerge in real-world data, where a large number of minority categories contain a limited number of samples. Such imbalance issue considerably impairs the performance of standard supervised learning algorithms, which are mainly designed for balanced training sets. Recent investigations have revealed that supervised contrastive learning exhibits promising potential in alleviating the data imbalance. However, the performance of supervised contrastive learning is plagued by an inherent challenge: it necessitates sufficiently large batches of training data to construct contrastive pairs that cover all categories, yet this requirement is difficult to meet in the context of class-imbalanced data. To overcome this obstacle, we propose a novel probabilistic contrastive (ProCo) learning algorithm that estimates the data distribution of the samples from each class in the feature space, and samples contrastive pairs accordingly. In fact, estimating the distributions of all classes using features in a small batch, particularly for imbalanced data, is not feasible. Our key idea is to introduce a reasonable and simple assumption that the normalized features in contrastive learning follow a mixture of von Mises-Fisher (vMF) distributions on unit space, which brings two-fold benefits. First, the distribution parameters can be estimated using only the first sample moment, which can be efficiently computed in an online manner across different batches. Second, based on the estimated distribution, the vMF distribution allows us to sample an infinite number of contrastive pairs and derive a closed form of the expected contrastive loss for efficient optimization. Our code is available at https://github.com/LeapLabTHU/ProCo.»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-06-01T16:19:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1508.03422)\]. Further details \[[6](http://arxiv.org/abs/2110.04596)\]\[[7](http://arxiv.org/abs/2304.09426)\]\[[8](http://arxiv.org/abs/2007.07314)\]\[[9](http://arxiv.org/abs/2107.12028)\]\[[10](http://arxiv.org/abs/2209.12400)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In this paper, we propose an Aligned Contrastive Learning (ACL) algorithm to address the long-tailed recognition problem. Our findings indicate that while multi-view training boosts the performance, contrastive learning does not consistently enhance model generalization as the number of views increases. Through theoretical gradient analysis of supervised contrastive learning (SCL), we identify gradient conflicts, and imbalanced attraction and repulsion gradients between positive and negative pairs as the underlying issues. Our ACL algorithm is designed to eliminate these problems and demonstrates strong performance across multiple benchmarks. We validate the effectiveness of ACL through experiments on long-tailed CIFAR, ImageNet, Places, and iNaturalist datasets. Results show that ACL achieves new state-of-the-art performance.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1508.03422)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1901.05555)\]\[[7](http://arxiv.org/abs/2304.09426)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Probabilistic Contrastive Learning addresses the challenges of long-tailed data distribution by improving the efficiency and effectiveness of contrastive learning in imbalanced settings \[[17](http://arxiv.org/abs/2403.06726)\]. Traditional supervised contrastive learning struggles with class imbalance due to the need for large batches to form diverse contrastive pairs, which is impractical in scenarios with minority classes \[[17](http://arxiv.org/abs/2403.06726)\]. To overcome this, probabilistic contrastive learning introduces a novel approach that estimates class-specific data distributions in the feature space, enabling the generation of contrastive pairs without requiring large batches \[[17](http://arxiv.org/abs/2403.06726)\]. This method leverages the von Mises-Fisher (vMF) distribution, assuming that normalized features follow a mixture of vMF distributions on the unit sphere, which allows for efficient parameter estimation using only the first moment of the data \[[17](http://arxiv.org/abs/2403.06726)\]. This approach not only facilitates the sampling of an infinite number of contrastive pairs but also enables the derivation of a closed-form contrastive loss for optimization \[[17](http://arxiv.org/abs/2403.06726)\]. This innovation aligns with the broader goal of enhancing contrastive learning for long-tailed recognition, as seen in methods like Aligned Contrastive Learning (ACL), which also targets gradient conflicts and imbalanced attraction/repulsion gradients \[[17](http://arxiv.org/abs/2403.06726)\].
|    | reference                                                                                                |   date | key idea/summary                                                                                                                                                                                                                                             |
|----|----------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Probabilistic Contrastive Learning for Long-Tailed Visual Recognition](http://arxiv.org/abs/2403.06726) |    nan | The paper proposes a probabilistic contrastive (ProCo) learning algorithm to address class-imbalanced data by estimating class distributions using von Mises-Fisher (vMF) distributions, enabling efficient contrastive pair sampling and loss optimization. |
### <a id='category-representation-learning-challenges'></a>Representation Learning Challenges: 3 papers found.
Context: 
	Document 1: [Category]: «Representation Learning Challenges»
[_citation_number]: «21»
[Snippet]: «In computer vision, it is standard practice to draw a single sample from the data augmentation procedure for each unique image in the mini-batch. However recent work has suggested drawing multiple samples can achieve higher test accuracies. In this work, we provide a detailed empirical evaluation of how the number of augmentation samples per unique image influences model performance on held out data when training deep ResNets. We demonstrate drawing multiple samples per image consistently enhances the test accuracy achieved for both small and large batch training. Crucially, this benefit arises even if different numbers of augmentations per image perform the same number of parameter updates and gradient evaluations (requiring the same total compute). Although prior work has found variance in the gradient estimate arising from subsampling the dataset has an implicit regularization benefit, our experiments suggest variance which arises from the data augmentation process harms generalization. We apply these insights to the highly performant NFNet-F5, achieving 86.8$\%$ top-1 w/o extra data on ImageNet.»

	Document 2: [Category]: «Representation Learning Challenges»
[_citation_number]: «22»
[Snippet]: «»

	Document 3: [Category]: «Representation Learning Challenges»
[_citation_number]: «23»
[Snippet]: «»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-06-01T16:19:30+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1508.03422)\]. Further details \[[6](http://arxiv.org/abs/2110.04596)\]\[[7](http://arxiv.org/abs/2304.09426)\]\[[8](http://arxiv.org/abs/2007.07314)\]\[[9](http://arxiv.org/abs/2107.12028)\]\[[10](http://arxiv.org/abs/2209.12400)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In this paper, we propose an Aligned Contrastive Learning (ACL) algorithm to
address the long-tailed recognition problem. Our findings indicate that while
multi-view training boosts the performance, contrastive learning does not
consistently enhance model generalization as the number of views increases.
Through theoretical gradient analysis of supervised contrastive learning (SCL),
we identify gradient conflicts, and imbalanced attraction and repulsion
gradients between positive and negative pairs as the underlying issues. Our ACL
algorithm is designed to eliminate these problems and demonstrates strong
performance across multiple benchmarks. We validate the effectiveness of ACL
through experiments on long-tailed CIFAR, ImageNet, Places, and iNaturalist
datasets. Results show that ACL achieves new state-of-the-art performance.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1508.03422)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1901.05555)\]\[[7](http://arxiv.org/abs/2304.09426)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Recent work has explored the impact of data augmentation strategies on model generalization, highlighting that drawing multiple samples per image during training can improve test accuracy, even when the total number of parameter updates and gradient evaluations remains constant \[[21](http://arxiv.org/abs/2105.13343)\]. This finding contrasts with earlier assumptions that subsampling the dataset introduces implicit regularization benefits \[[21](http://arxiv.org/abs/2105.13343)\]. Instead, the variance introduced by the data augmentation process may negatively affect generalization, suggesting that the design of augmentation procedures is critical for model performance \[[21](http://arxiv.org/abs/2105.13343)\]. These insights align with broader challenges in representation learning, where balancing exploration and exploitation during training remains a key challenge.
|    | reference                                                                                                                             |   date | key idea/summary                                                                                                                                                                                                                        |
|----|---------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Drawing Multiple Augmentation Samples Per Image During Training
  Efficiently Decreases Test Error](http://arxiv.org/abs/2105.13343) |    nan | Drawing multiple augmentation samples per unique image during training consistently improves test accuracy for deep ResNets, even with the same total compute, and this benefit is applied to achieve 86.8% top-1 accuracy on ImageNet. |
|  1 | [Learning to model the tail]()                                                                                                        |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                               |
|  2 | [Exploring balanced feature spaces for representation learning]()                                                                     |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                               |
