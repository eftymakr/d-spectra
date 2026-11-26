## Related Works

Label noise is a pervasive issue in deep learning, affecting the performance of models trained on imperfectly annotated data. Several approaches have been proposed to address this challenge. Early work focused on modifying network architectures or estimating true labels from noisy ones \[[10](http://arxiv.org/abs/1712.09482)\]. For instance, \[[10](http://arxiv.org/abs/1712.09482)\] proposed loss functions that are inherently robust to label noise, showing that mean absolute error (MAE) can be used for risk minimization under noisy labels. This approach avoids the need for explicit label correction, relying instead on the robustness of the loss function itself. However, these methods often assume uniform noise distributions and may not generalize well to complex, real-world scenarios \[[15](http://arxiv.org/abs/1805.07836)\].

More recently, researchers have explored the use of semi-supervised learning to improve robustness against noisy labels. For example, \[[7](http://arxiv.org/abs/2002.07394)\] introduced DivideMix, a framework that leverages semi-supervised techniques to dynamically separate clean and noisy samples during training. This approach models the per-sample loss distribution using a mixture model, allowing the model to learn from both labeled and unlabeled data in a semi-supervised manner. Similarly, \[[11](http://arxiv.org/abs/1901.04215)\] proposed Co-teaching+, which builds upon the Co-teaching framework by incorporating disagreement-based learning to avoid confirmation bias. This method trains two diverged networks, where each network uses the dataset division from the other to improve robustness against noisy labels.

Another line of research focuses on loss correction and noise estimation. \[[1](http://arxiv.org/abs/1609.03683)\] introduced a loss correction approach that accounts for class-dependent label noise, proposing two procedures that amount to matrix inversion and multiplication, provided the probability of each class being corrupted is known. They also developed a method to estimate these probabilities, enabling an end-to-end framework for training robust models. This work was later extended in \[[14](http://arxiv.org/abs/2012.11854)\], which addressed instance-dependent label noise by leveraging second-order statistics to estimate noise rates and adjust the loss function accordingly. This approach allows for more accurate modeling of real-world label noise, which often depends on the difficulty of the task.

In addition to loss-based methods, some works have focused on reweighting examples to improve robustness. \[[12](http://arxiv.org/abs/1803.09050)\] proposed a meta-learning algorithm that learns to assign weights to training examples based on their gradient directions, without requiring additional hyperparameter tuning. This method can be applied to any deep network and is particularly effective in handling class imbalance and corrupted labels. Similarly, \[[16](http://arxiv.org/abs/1909.03388)\] introduced a novel information-theoretic loss function, $\mathcal(L)_(DMI)$, which is provably robust to instance-independent label noise. This loss function is based on mutual information and can be applied to any classification neural network without requiring auxiliary information.

Finally, \[[15](http://arxiv.org/abs/1805.07836)\] proposed generalized cross entropy loss as a noise-robust alternative to categorical cross entropy, showing that it can be applied to a wide range of noisy label scenarios. This work builds on earlier findings that MAE can be used for risk minimization under noisy labels, but extends the idea to more general settings.

\[[1](http://arxiv.org/abs/1609.03683)\] Making Deep Neural Networks Robust to Label Noise: A Loss Correction Approach  
\[[2](http://arxiv.org/abs/1711.07131)\] CleanNet: Transfer Learning for Scalable Image Classifier Training with Label Noise  
\[[3](http://arxiv.org/abs/1804.06872)\] Co-teaching: Robust training of deep neural networks with extremely noisy labels  
\[[4](http://arxiv.org/abs/1706.00038)\] Toward Robustness against Label Noise in Training Deep Discriminative Neural Networks  
\[[5](http://arxiv.org/abs/1806.02612)\] Dimensionality-Driven Learning with Noisy Labels  
\[[6](http://arxiv.org/abs/1703.02391)\] Learning from Noisy Labels with Distillation  
\[[7](http://arxiv.org/abs/2002.07394)\] DivideMix: Learning with Noisy Labels as Semi-supervised Learning  
\[[8](http://arxiv.org/abs/1908.06112)\] Symmetric Cross Entropy for Robust Learning With Noisy Labels  
\[[9](https://www.semanticscholar.org/paper/5d6ae67e569f974360b107060c23cbb8a13b0687)\] Learning from massive noisy labeled data for image classification  
\[[10](http://arxiv.org/abs/1712.09482)\] Robust Loss Functions under Label Noise for Deep Neural Networks  
\[[11](http://arxiv.org/abs/1901.04215)\] How does Disagreement Help Generalization against Label Corruption?  
\[[12](http://arxiv.org/abs/1803.09050)\] Learning to Reweight Examples for Robust Deep Learning  
\[[13](http://arxiv.org/abs/1611.03530)\] Understanding deep learning requires rethinking generalization  
\[[14](http://arxiv.org/abs/2012.11854)\] A Second-Order Approach to Learning with Instance-Dependent Label Noise  
\[[15](http://arxiv.org/abs/1805.07836)\] Generalized Cross Entropy Loss for Training Deep Neural Networks with Noisy Labels  
\[[16](http://arxiv.org/abs/1909.03388)\] L_DMI: An Information-theoretic Noise-robust Loss Function
## Research papers
### Outline
- [Loss Correction and Noise Estimation [1 papers]](#category-loss-correction-and-noise-estimation)
- [Label Noise in Deep Learning [10 papers]](#category-label-noise-in-deep-learning)
- [Semi-Supervised Learning for Noise [1 papers]](#category-semi-supervised-learning-for-noise)
- [Cross Entropy and Generalized Losses [2 papers]](#category-cross-entropy-and-generalized-losses)
- [Loss Function Robustness [1 papers]](#category-loss-function-robustness)
- [Example Reweighting Techniques [1 papers]](#category-example-reweighting-techniques)
- [Information-Theoretic Loss Functions [1 papers]](#category-information-theoretic-loss-functions)

### <a id='category-loss-correction-and-noise-estimation'></a>Loss Correction and Noise Estimation: 1 papers found.
Context: 
	Document 1: [_citation_number]: «1»
[Snippet]: «We present a theoretically grounded approach to train deep neural networks, including recurrent networks, subject to class-dependent label noise. We propose two procedures for loss correction that are agnostic to both application domain and network architecture. They simply amount to at most a matrix inversion and multiplication, provided that we know the probability of each class being corrupted into another. We further show how one can estimate these probabilities, adapting a recent technique for noise estimation to the multi-class setting, and thus providing an end-to-end framework. Extensive experiments on MNIST, IMDB, CIFAR-10, CIFAR-100 and a large scale dataset of clothing images employing a diversity of architectures &#x2014; stacking dense, convolutional, pooling, dropout, batch normalization, word embedding, LSTM and residual layers &#x2014; demonstrate the noise robustness of our proposals. Incidentally, we also prove that, when ReLU is the only non-linearity, the loss curvature is immune to class-dependent label noise.»
[Category]: «Loss Correction and Noise Estimation»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T06:44:48+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1804.06872)\]. Further details \[[6](http://arxiv.org/abs/1703.02391)\]\[[7](http://arxiv.org/abs/2002.07394)\]\[[8](http://arxiv.org/abs/1908.06112)\]\[[9](https://www.semanticscholar.org/paper/5d6ae67e569f974360b107060c23cbb8a13b0687)\]\[[10](http://arxiv.org/abs/1712.09482)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In context learning (ICL) relies heavily on high quality demonstrations drawn
from large annotated corpora. Existing approaches detect noisy annotations by
ranking local perplexities, presuming that noisy samples yield higher
perplexities than their clean counterparts. However, this assumption breaks
down when the noise ratio is high and many demonstrations are flawed. We
reexamine the perplexity based paradigm for text generation under noisy
annotations, highlighting two sources of bias in perplexity: the annotation
itself and the domain specific knowledge inherent in large language models
(LLMs). To overcome these biases, we introduce a dual debiasing framework that
uses synthesized neighbors to explicitly correct perplexity estimates, yielding
a robust Sample Cleanliness Score. This metric uncovers absolute sample
cleanliness regardless of the overall corpus noise level. Extensive experiments
demonstrate our method's superior noise detection capabilities and show that
its final ICL performance is comparable to that of a fully clean demonstration
corpus. Moreover, our approach remains robust even when noise ratios are
extremely high.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1804.06872)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1711.07131)\]\[[7](http://arxiv.org/abs/2002.07394)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The category of "Loss Correction and Noise Estimation" focuses on improving the robustness of deep learning models in the presence of label noise, particularly class-dependent noise. This area has seen significant advancements, including the development of loss correction techniques that are agnostic to network architecture and application domain \[[1](http://arxiv.org/abs/1609.03683)\]. These methods typically involve matrix inversion and multiplication, provided that the probability of class corruption is known \[[1](http://arxiv.org/abs/1609.03683)\]. Furthermore, recent work has addressed the challenge of estimating these corruption probabilities by adapting noise estimation techniques to the multi-class setting, enabling an end-to-end framework for training robust models \[[1](http://arxiv.org/abs/1609.03683)\]. This approach has been validated through extensive experiments on diverse datasets such as MNIST, IMDB, CIFAR-10, CIFAR-100, and large-scale clothing image datasets, demonstrating the effectiveness of these methods across a variety of architectures \[[1](http://arxiv.org/abs/1609.03683)\]. Additionally, theoretical insights have been provided, such as the proof that loss curvature is immune to class-dependent label noise when ReLU is the only non-linearity \[[1](http://arxiv.org/abs/1609.03683)\]. These contributions highlight the importance of addressing noise in training data to enhance model performance and reliability.
|    | reference                                                                                                        | date     | key idea/summary                                                                                                                                                                                                                       |
|----|------------------------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Making Deep Neural Networks Robust to Label Noise: A Loss Correction Approach](http://arxiv.org/abs/1609.03683) | 09/13/16 | The paper introduces a theoretically grounded approach to train deep neural networks with class-dependent label noise, proposing loss correction methods and demonstrating their robustness across various architectures and datasets. |
### <a id='category-label-noise-in-deep-learning'></a>Label Noise in Deep Learning: 10 papers found.
Label Noise in Deep Learning has been a focal point in recent research, with multiple approaches proposed to address the challenges posed by noisy labels. Existing methods often rely on human supervision, which is time-consuming and not scalable, while unsupervised methods, though scalable, tend to be less effective \[[1](http://arxiv.org/abs/1609.03683)\]. To mitigate this, CleanNet was introduced as a joint neural embedding network that requires only a fraction of manually verified labels to infer label noise patterns, which can then be transferred to other classes \[[1](http://arxiv.org/abs/1609.03683)\]. Similarly, Co-teaching was proposed as a paradigm where two neural networks are trained simultaneously, with each network teaching the other by selecting potentially clean data and updating parameters based on the peer's selection \[[2](http://arxiv.org/abs/1711.07131)\]. This approach has shown superior robustness compared to state-of-the-art methods \[[2](http://arxiv.org/abs/1711.07131)\]. Another framework, based on an undirected graphical model, was developed to train deep convolutional neural networks from noisy datasets by modeling the relationship between noisy and clean labels, with regularization using auxiliary information \[[3](http://arxiv.org/abs/1804.06872)\]. Additionally, a dimensionality-driven learning strategy was introduced to monitor and adapt the loss function during training, enabling models to tolerate significant proportions of noisy labels by learning low-dimensional subspaces \[[4](http://arxiv.org/abs/1706.00038)\]. The real-world noisy labels were also found to exhibit multimodal characteristics, prompting the development of a unified distillation framework that leverages side information such as clean datasets and label relations in knowledge graphs to reduce the risk of learning from noisy labels \[[5](http://arxiv.org/abs/1806.02612)\]. Furthermore, the issue of instance-dependent label noise was addressed by proposing a second-order approach that estimates covariance terms between noise rates and Bayes optimal labels, leading to a new loss function that effectively handles imbalanced noise \[[9](https://www.semanticscholar.org/paper/5d6ae67e569f974360b107060c23cbb8a13b0687)\]. These methods collectively highlight the diverse strategies being explored to improve the robustness of deep learning models in the presence of label noise.
|    | reference                                                                                                                                           | date     | key idea/summary                                                                                                                                                                                                                                                         |
|----|-----------------------------------------------------------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [CleanNet: Transfer Learning for Scalable Image Classifier Training with Label Noise](http://arxiv.org/abs/1711.07131)                              | 11/20/17 | CleanNet is a joint neural embedding network that reduces the need for human supervision in label noise cleaning by transferring knowledge from verified classes to others, achieving significant performance gains with minimal manual verification.                    |
|  1 | [Co-teaching: Robust training of deep neural networks with extremely noisy labels](http://arxiv.org/abs/1804.06872)                                 | 04/18/18 | The paper introduces Co-teaching, a new deep learning paradigm that trains two neural networks to teach each other using noisy labels, leading to more robust models compared to existing methods.                                                                       |
|  2 | [Toward Robustness against Label Noise in Training Deep Discriminative Neural Networks](http://arxiv.org/abs/1706.00038)                            | 05/31/17 | The paper introduces a framework for training deep convolutional neural networks using noisy labeled datasets, effectively reducing label noise and improving performance on image labeling tasks.                                                                       |
|  3 | [Dimensionality-Driven Learning with Noisy Labels](http://arxiv.org/abs/1806.02612)                                                                 | 06/07/18 | The paper introduces a dimensionality-driven learning strategy for DNNs to improve generalization in the presence of noisy labels by adapting the loss function based on the dimensionality of deep representation subspaces.                                            |
|  4 | [Learning from Noisy Labels with Distillation](http://arxiv.org/abs/1703.02391)                                                                     | 03/07/17 | The paper proposes a unified distillation framework that leverages side information, such as a small clean dataset and label relations in a knowledge graph, to effectively learn from noisy labels in practical settings.                                               |
|  5 | [Learning from massive noisy labeled data for image classification](https://www.semanticscholar.org/paper/5d6ae67e569f974360b107060c23cbb8a13b0687) | 06/07/15 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                |
|  6 | [How does Disagreement Help Generalization against Label Corruption?](http://arxiv.org/abs/1901.04215)                                              | 01/14/19 | Co-teaching+ is a robust learning paradigm that improves upon the Co-teaching method by incorporating the 'Update by Disagreement' strategy, leading to better performance in handling noisy labels.                                                                     |
|  7 | [Understanding deep learning requires rethinking generalization](http://arxiv.org/abs/1611.03530)                                                   | 11/04/16 | Large neural networks can generalize well despite their size and training data fitting random labelings, challenging traditional explanations based on model properties or regularization.                                                                               |
|  8 | [A Second-Order Approach to Learning with Instance-Dependent Label Noise](http://arxiv.org/abs/2012.11854)                                          | 12/22/20 | The paper addresses instance-dependent label noise in deep neural networks by proposing a second-order approach that leverages covariance terms to capture imbalances caused by heterogeneous noise, enabling the use of existing class-dependent label noise solutions. |
|  9 | [A Closer Look at Memorization in Deep Networks](http://arxiv.org/abs/1706.05394)                                                                   | 06/16/17 | The paper explores how deep learning models prioritize learning simple patterns over memorizing noise, and shows that explicit regularization can improve generalization on real data without sacrificing performance on noise datasets.                                 |
### <a id='category-semi-supervised-learning-for-noise'></a>Semi-Supervised Learning for Noise: 1 papers found.
Context: 
	Document 1: [_citation_number]: «7»
[Snippet]: «Deep neural networks are known to be annotation-hungry. Numerous efforts have been devoted to reducing the annotation cost when learning with deep networks. Two prominent directions include learning with noisy labels and semi-supervised learning by exploiting unlabeled data. In this work, we propose DivideMix, a novel framework for learning with noisy labels by leveraging semi-supervised learning techniques. In particular, DivideMix models the per-sample loss distribution with a mixture model to dynamically divide the training data into a labeled set with clean samples and an unlabeled set with noisy samples, and trains the model on both the labeled and unlabeled data in a semi-supervised manner. To avoid confirmation bias, we simultaneously train two diverged networks where each network uses the dataset division from the other network. During the semi-supervised training phase, we improve the MixMatch strategy by performing label co-refinement and label co-guessing on labeled and unlabeled samples, respectively. Experiments on multiple benchmark datasets demonstrate substantial improvements over state-of-the-art methods. Code is available at this https URL .»
[Category]: «Semi-Supervised Learning for Noise»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T06:44:48+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1804.06872)\]. Further details \[[6](http://arxiv.org/abs/1703.02391)\]\[[7](http://arxiv.org/abs/2002.07394)\]\[[8](http://arxiv.org/abs/1908.06112)\]\[[9](https://www.semanticscholar.org/paper/5d6ae67e569f974360b107060c23cbb8a13b0687)\]\[[10](http://arxiv.org/abs/1712.09482)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In context learning (ICL) relies heavily on high quality demonstrations drawn
from large annotated corpora. Existing approaches detect noisy annotations by
ranking local perplexities, presuming that noisy samples yield higher
perplexities than their clean counterparts. However, this assumption breaks
down when the noise ratio is high and many demonstrations are flawed. We
reexamine the perplexity based paradigm for text generation under noisy
annotations, highlighting two sources of bias in perplexity: the annotation
itself and the domain specific knowledge inherent in large language models
(LLMs). To overcome these biases, we introduce a dual debiasing framework that
uses synthesized neighbors to explicitly correct perplexity estimates, yielding
a robust Sample Cleanliness Score. This metric uncovers absolute sample
cleanliness regardless of the overall corpus noise level. Extensive experiments
demonstrate our method's superior noise detection capabilities and show that
its final ICL performance is comparable to that of a fully clean demonstration
corpus. Moreover, our approach remains robust even when noise ratios are
extremely high.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1804.06872)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1711.07131)\]\[[7](http://arxiv.org/abs/2002.07394)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Recent research has focused on reducing annotation costs in deep learning, particularly through semi-supervised learning and handling noisy labels \[[7](http://arxiv.org/abs/2002.07394)\]. A notable approach is DivideMix, which leverages semi-supervised techniques to dynamically partition training data into clean and noisy subsets using a mixture model \[[7](http://arxiv.org/abs/2002.07394)\]. This framework improves upon existing methods by incorporating label co-refinement and co-guessing strategies during training, thereby mitigating confirmation bias \[[7](http://arxiv.org/abs/2002.07394)\]. Such methods are crucial for scenarios where labeled data is scarce or unreliable, as they enable effective learning from both labeled and unlabeled samples.
|    | reference                                                                                            | date     | key idea/summary                                                                                                                                                                                                                                     |
|----|------------------------------------------------------------------------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [DivideMix: Learning with Noisy Labels as Semi-supervised Learning](http://arxiv.org/abs/2002.07394) | 02/18/20 | DivideMix is a novel framework that reduces annotation cost by leveraging semi-supervised learning and mixture models to dynamically divide training data into clean and noisy sets, while avoiding confirmation bias through dual network training. |
### <a id='category-cross-entropy-and-generalized-losses'></a>Cross Entropy and Generalized Losses: 2 papers found.
Context: 
	Document 1: [_citation_number]: «8»
[Snippet]: «Training accurate deep neural networks (DNNs) in the presence of noisy labels is an important and challenging task. Though a number of approaches have been proposed for learning with noisy labels, many open issues remain. In this paper, we show that DNN learning with Cross Entropy (CE) exhibits overfitting to noisy labels on some classes (``easy" classes), but more surprisingly, it also suffers from significant under learning on some other classes (``hard" classes). Intuitively, CE requires an extra term to facilitate learning of hard classes, and more importantly, this term should be noise tolerant, so as to avoid overfitting to noisy labels. Inspired by the symmetric KL-divergence, we propose the approach of Symmetric cross entropy Learning (SL), boosting CE symmetrically with a noise robust counterpart Reverse Cross Entropy (RCE). Our proposed SL approach simultaneously addresses both the under learning and overfitting problem of CE in the presence of noisy labels. We provide a theoretical analysis of SL and also empirically show, on a range of benchmark and real-world datasets, that SL outperforms state-of-the-art methods. We also show that SL can be easily incorporated into existing methods in order to further enhance their performance.»
[Category]: «Cross Entropy and Generalized Losses»

	Document 2: [_citation_number]: «15»
[Snippet]: «Deep neural networks (DNNs) have achieved tremendous success in a variety of applications across many disciplines. Yet, their superior performance comes with the expensive cost of requiring correctly annotated large-scale datasets. Moreover, due to DNNs’ rich capacity, errors in training labels can hamper performance. To combat this problem, mean absolute error (MAE) has recently been proposed as a noise-robust alternative to the commonly-used categorical cross entropy (CCE) loss. However, as we show in this paper, MAE can perform poorly with DNNs and challenging datasets. Here, we present a theoretically grounded set of noise-robust loss functions that can be seen as a generalization of MAE and CCE. Proposed loss functions can be readily applied with any existing DNN architecture and algorithm, while yielding good performance in a wide range of noisy label scenarios. We report results from experiments conducted with CIFAR-10, CIFAR-100 and FASHION-MNIST datasets and synthetically generated noisy labels.»
[Category]: «Cross Entropy and Generalized Losses»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T06:44:48+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1804.06872)\]. Further details \[[6](http://arxiv.org/abs/1703.02391)\]\[[7](http://arxiv.org/abs/2002.07394)\]\[[8](http://arxiv.org/abs/1908.06112)\]\[[9](https://www.semanticscholar.org/paper/5d6ae67e569f974360b107060c23cbb8a13b0687)\]\[[10](http://arxiv.org/abs/1712.09482)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In context learning (ICL) relies heavily on high quality demonstrations drawn
from large annotated corpora. Existing approaches detect noisy annotations by
ranking local perplexities, presuming that noisy samples yield higher
perplexities than their clean counterparts. However, this assumption breaks
down when the noise ratio is high and many demonstrations are flawed. We
reexamine the perplexity based paradigm for text generation under noisy
annotations, highlighting two sources of bias in perplexity: the annotation
itself and the domain specific knowledge inherent in large language models
(LLMs). To overcome these biases, we introduce a dual debiasing framework that
uses synthesized neighbors to explicitly correct perplexity estimates, yielding
a robust Sample Cleanliness Score. This metric uncovers absolute sample
cleanliness regardless of the overall corpus noise level. Extensive experiments
demonstrate our method's superior noise detection capabilities and show that
its final ICL performance is comparable to that of a fully clean demonstration
corpus. Moreover, our approach remains robust even when noise ratios are
extremely high.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1804.06872)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1711.07131)\]\[[7](http://arxiv.org/abs/2002.07394)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
The category of Cross Entropy and Generalized Losses focuses on the challenges of training deep neural networks with noisy labels and the development of alternative loss functions to improve robustness. Existing methods, such as the standard categorical cross entropy (CCE), suffer from overfitting to noisy labels on easy classes and under learning on hard classes \[[8](http://arxiv.org/abs/1908.06112)\]. To address these issues, researchers have proposed noise-robust alternatives, such as the mean absolute error (MAE), which has been shown to be a viable alternative to CCE \[[15](http://arxiv.org/abs/1805.07836)\]. However, MAE also has limitations, particularly in its performance with DNNs on challenging datasets. This has led to the development of generalized loss functions that extend both MAE and CCE, offering a more theoretically grounded approach to noise-robust learning \[[15](http://arxiv.org/abs/1805.07836)\]. These loss functions are designed to be flexible, applicable to a wide range of DNN architectures, and effective in various noisy label scenarios \[[15](http://arxiv.org/abs/1805.07836)\]. Additionally, approaches like the Symmetric cross entropy Learning (SL) method, which combines cross entropy with a noise-robust counterpart (Reverse Cross Entropy), have been introduced to simultaneously address under learning and overfitting issues \[[8](http://arxiv.org/abs/1908.06112)\]. These methods demonstrate improved performance across benchmark and real-world datasets, highlighting the ongoing efforts to enhance the robustness of deep learning models in the presence of noisy annotations.
|    | reference                                                                                                             | date     | key idea/summary                                                                                                                                                                                                              |
|----|-----------------------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Symmetric Cross Entropy for Robust Learning With Noisy Labels](http://arxiv.org/abs/1908.06112)                      | 08/16/19 | The paper introduces Symmetric Cross Entropy Learning (SL), which addresses both overfitting to noisy labels and under learning in deep neural networks by combining Cross Entropy with a noise-robust Reverse Cross Entropy. |
|  1 | [Generalized Cross Entropy Loss for Training Deep Neural Networks with Noisy Labels](http://arxiv.org/abs/1805.07836) | 05/20/18 | This paper introduces theoretically grounded noise-robust loss functions that generalize mean absolute error (MAE) and categorical cross entropy (CCE) to improve performance in DNNs with noisy labels.                      |
### <a id='category-loss-function-robustness'></a>Loss Function Robustness: 1 papers found.
Context: 
	Document 1: [_citation_number]: «10»
[Snippet]: «
 
 In many applications of classifier learning, training data suffers from label noise. Deep networks are learned using huge training data where the problem of noisy labels is particularly relevant. The current techniques proposed for learning deep networks under label noise focus on modifying the network architecture and on algorithms for estimating true labels from noisy labels. An alternate approach would be to look for loss functions that are inherently noise-tolerant. For binary classification there exist theoretical results on loss functions that are robust to label noise. In this paper, we provide some sufficient conditions on a loss function so that risk minimization under that loss function would be inherently tolerant to label noise for multiclass classification problems. These results generalize the existing results on noise-tolerant loss functions for binary classification. We study some of the widely used loss functions in deep networks and show that the loss function based on mean absolute value of error is inherently robust to label noise. Thus standard back propagation is enough to learn the true classifier even under label noise. Through experiments, we illustrate the robustness of risk minimization with such loss functions for learning neural networks.
 
»
[Category]: «Loss Function Robustness»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T06:44:48+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1804.06872)\]. Further details \[[6](http://arxiv.org/abs/1703.02391)\]\[[7](http://arxiv.org/abs/2002.07394)\]\[[8](http://arxiv.org/abs/1908.06112)\]\[[9](https://www.semanticscholar.org/paper/5d6ae67e569f974360b107060c23cbb8a13b0687)\]\[[10](http://arxiv.org/abs/1712.09482)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In context learning (ICL) relies heavily on high quality demonstrations drawn
from large annotated corpora. Existing approaches detect noisy annotations by
ranking local perplexities, presuming that noisy samples yield higher
perplexities than their clean counterparts. However, this assumption breaks
down when the noise ratio is high and many demonstrations are flawed. We
reexamine the perplexity based paradigm for text generation under noisy
annotations, highlighting two sources of bias in perplexity: the annotation
itself and the domain specific knowledge inherent in large language models
(LLMs). To overcome these biases, we introduce a dual debiasing framework that
uses synthesized neighbors to explicitly correct perplexity estimates, yielding
a robust Sample Cleanliness Score. This metric uncovers absolute sample
cleanliness regardless of the overall corpus noise level. Extensive experiments
demonstrate our method's superior noise detection capabilities and show that
its final ICL performance is comparable to that of a fully clean demonstration
corpus. Moreover, our approach remains robust even when noise ratios are
extremely high.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1804.06872)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1711.07131)\]\[[7](http://arxiv.org/abs/2002.07394)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Recent research has focused on developing loss functions that are inherently robust to label noise, particularly in the context of deep learning. This is especially relevant given the prevalence of noisy labels in large training datasets \[[10](http://arxiv.org/abs/1712.09482)\]. While existing approaches often modify network architectures or employ algorithms to estimate true labels from noisy ones, an alternative approach is to design loss functions that are theoretically noise-tolerant \[[10](http://arxiv.org/abs/1712.09482)\]. For binary classification, theoretical results have already established certain loss functions as robust to label noise \[[10](http://arxiv.org/abs/1712.09482)\]. This paper extends those findings to multiclass classification by providing sufficient conditions for loss functions that enable risk minimization to be inherently tolerant to label noise \[[10](http://arxiv.org/abs/1712.09482)\]. The study examines widely used loss functions in deep networks and identifies the mean absolute value of error as a loss function that is robust to label noise, suggesting that standard back propagation can be sufficient for learning the true classifier even under label noise \[[10](http://arxiv.org/abs/1712.09482)\]. Experimental results further demonstrate the robustness of risk minimization with such loss functions in learning neural networks \[[10](http://arxiv.org/abs/1712.09482)\].
|    | reference                                                                                           | date     | key idea/summary                                                                                                                                                                                                                                                                        |
|----|-----------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Robust Loss Functions under Label Noise for Deep Neural Networks](http://arxiv.org/abs/1712.09482) | 02/13/17 | The paper introduces sufficient conditions for loss functions to be inherently robust to label noise in multiclass classification, showing that the mean absolute value of error loss is robust and allows standard back propagation to learn the true classifier despite noisy labels. |
### <a id='category-example-reweighting-techniques'></a>Example Reweighting Techniques: 1 papers found.
Context: 
	Document 1: [_citation_number]: «12»
[Snippet]: «Deep neural networks have been shown to be very powerful modeling tools for many supervised learning tasks involving complex input patterns. However, they can also easily overfit to training set biases and label noises. In addition to various regularizers, example reweighting algorithms are popular solutions to these problems, but they require careful tuning of additional hyperparameters, such as example mining schedules and regularization hyperparameters. In contrast to past reweighting methods, which typically consist of functions of the cost value of each example, in this work we propose a novel meta-learning algorithm that learns to assign weights to training examples based on their gradient directions. To determine the example weights, our method performs a meta gradient descent step on the current mini-batch example weights (which are initialized from zero) to minimize the loss on a clean unbiased validation set. Our proposed method can be easily implemented on any type of deep network, does not require any additional hyperparameter tuning, and achieves impressive performance on class imbalance and corrupted label problems where only a small amount of clean validation data is available.»
[Category]: «Example Reweighting Techniques»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T06:44:48+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1804.06872)\]. Further details \[[6](http://arxiv.org/abs/1703.02391)\]\[[7](http://arxiv.org/abs/2002.07394)\]\[[8](http://arxiv.org/abs/1908.06112)\]\[[9](https://www.semanticscholar.org/paper/5d6ae67e569f974360b107060c23cbb8a13b0687)\]\[[10](http://arxiv.org/abs/1712.09482)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In context learning (ICL) relies heavily on high quality demonstrations drawn
from large annotated corpora. Existing approaches detect noisy annotations by
ranking local perplexities, presuming that noisy samples yield higher
perplexities than their clean counterparts. However, this assumption breaks
down when the noise ratio is high and many demonstrations are flawed. We
reexamine the perplexity based paradigm for text generation under noisy
annotations, highlighting two sources of bias in perplexity: the annotation
itself and the domain specific knowledge inherent in large language models
(LLMs). To overcome these biases, we introduce a dual debiasing framework that
uses synthesized neighbors to explicitly correct perplexity estimates, yielding
a robust Sample Cleanliness Score. This metric uncovers absolute sample
cleanliness regardless of the overall corpus noise level. Extensive experiments
demonstrate our method's superior noise detection capabilities and show that
its final ICL performance is comparable to that of a fully clean demonstration
corpus. Moreover, our approach remains robust even when noise ratios are
extremely high.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1804.06872)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1711.07131)\]\[[7](http://arxiv.org/abs/2002.07394)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Example reweighting techniques have been widely explored to address overfitting and label noise in deep learning models \[[12](http://arxiv.org/abs/1803.09050)\]. These methods aim to assign appropriate weights to training examples to improve generalization, particularly in scenarios with imbalanced classes or corrupted labels. Traditional approaches often rely on functions of the cost value of each example, requiring careful tuning of hyperparameters such as example mining schedules and regularization parameters \[[12](http://arxiv.org/abs/1803.09050)\]. However, recent work proposes more adaptive strategies, such as meta-learning algorithms that dynamically adjust example weights based on gradient directions during training \[[12](http://arxiv.org/abs/1803.09050)\]. This approach eliminates the need for manual hyperparameter tuning and leverages a clean validation set to guide the weighting process, making it particularly effective in low-resource settings where only a small amount of clean data is available \[[12](http://arxiv.org/abs/1803.09050)\]. Such innovations highlight the ongoing evolution of reweighting techniques, emphasizing their importance in enhancing model robustness and performance under challenging data conditions.
|    | reference                                                                                 | date     | key idea/summary                                                                                                                                                                                                                                     |
|----|-------------------------------------------------------------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Learning to Reweight Examples for Robust Deep Learning](http://arxiv.org/abs/1803.09050) | 03/24/18 | The paper proposes a novel meta-learning algorithm that assigns weights to training examples based on gradient directions, achieving performance on class imbalance and corrupted label problems without requiring additional hyperparameter tuning. |
### <a id='category-information-theoretic-loss-functions'></a>Information-Theoretic Loss Functions: 1 papers found.
Context: 
	Document 1: [_citation_number]: «16»
[Snippet]: «Accurately annotating large scale dataset is notoriously expensive both in time and in money. Although acquiring low-quality-annotated dataset can be much cheaper, it often badly damages the performance of trained models when using such dataset without particular treatment. Various methods have been proposed for learning with noisy labels. However, most methods only handle limited kinds of noise patterns, require auxiliary information or steps (e.g. , knowing or estimating the noise transition matrix), or lack theoretical justification. In this paper, we propose a novel information-theoretic loss function, $\mathcal(L)_(DMI)$, for training deep neural networks robust to label noise. The core of $\mathcal(L)_(DMI)$ is a generalized version of mutual information, termed Determinant based Mutual Information (DMI), which is not only information-monotone but also relatively invariant. \emph(To the best of our knowledge, $\mathcal(L)_(DMI)$ is the first loss function that is provably robust to instance-independent label noise, regardless of noise pattern, and it can be applied to any existing classification neural networks straightforwardly without any auxiliary information). In addition to theoretical justification, we also empirically show that using $\mathcal(L)_(DMI)$ outperforms all other counterparts in the classification task on both image dataset and natural language dataset include Fashion-MNIST, CIFAR-10, Dogs vs. Cats, MR with a variety of synthesized noise patterns and noise amounts, as well as a real-world dataset Clothing1M. Codes are available at this https URL .»
[Category]: «Information-Theoretic Loss Functions»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T06:44:48+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1804.06872)\]. Further details \[[6](http://arxiv.org/abs/1703.02391)\]\[[7](http://arxiv.org/abs/2002.07394)\]\[[8](http://arxiv.org/abs/1908.06112)\]\[[9](https://www.semanticscholar.org/paper/5d6ae67e569f974360b107060c23cbb8a13b0687)\]\[[10](http://arxiv.org/abs/1712.09482)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In context learning (ICL) relies heavily on high quality demonstrations drawn
from large annotated corpora. Existing approaches detect noisy annotations by
ranking local perplexities, presuming that noisy samples yield higher
perplexities than their clean counterparts. However, this assumption breaks
down when the noise ratio is high and many demonstrations are flawed. We
reexamine the perplexity based paradigm for text generation under noisy
annotations, highlighting two sources of bias in perplexity: the annotation
itself and the domain specific knowledge inherent in large language models
(LLMs). To overcome these biases, we introduce a dual debiasing framework that
uses synthesized neighbors to explicitly correct perplexity estimates, yielding
a robust Sample Cleanliness Score. This metric uncovers absolute sample
cleanliness regardless of the overall corpus noise level. Extensive experiments
demonstrate our method's superior noise detection capabilities and show that
its final ICL performance is comparable to that of a fully clean demonstration
corpus. Moreover, our approach remains robust even when noise ratios are
extremely high.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1804.06872)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1711.07131)\]\[[7](http://arxiv.org/abs/2002.07394)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
The field of learning with noisy labels has seen significant advancements, particularly in the development of information-theoretic loss functions that enhance model robustness. One such approach is the Determinant based Mutual Information (DMI) loss function, which addresses the challenges of instance-independent label noise by leveraging a generalized version of mutual information \[[16](http://arxiv.org/abs/1909.03388)\]. This method is notable for its theoretical guarantees and practical effectiveness, as it is designed to be invariant to noise patterns and does not require auxiliary information such as noise transition matrices \[[16](http://arxiv.org/abs/1909.03388)\]. The DMI loss function has been validated across various datasets, including image and natural language datasets like Fashion-MNIST, CIFAR-10, and Clothing1M, demonstrating superior performance under different noise conditions \[[16](http://arxiv.org/abs/1909.03388)\]. This aligns with broader efforts to improve the reliability of machine learning models in the presence of noisy data, emphasizing the importance of robust loss functions in real-world applications.
|    | reference                                                                                     | date     | key idea/summary                                                                                                                                                                                       |
|----|-----------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [L_DMI: An Information-theoretic Noise-robust Loss Function](http://arxiv.org/abs/1909.03388) | 09/08/19 | The paper introduces a novel information-theoretic loss function, DMI, which is robust to label noise and can be applied to any classification neural network without requiring auxiliary information. |
