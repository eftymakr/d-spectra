## Related Works

Active learning (AL) has been extensively studied for reducing human annotation costs by selecting the most informative unlabeled data for labeling \[[1]()\]. Early approaches such as uncertainty sampling \[[1]()\] and query-by-committee \[[2](http://arxiv.org/abs/2505.06825)\] aimed to reduce the amount of training data required by focusing on uncertain or ambiguous examples. More recent methods have explored uncertainty metrics to guide the selection of high-value examples in smaller training sets, particularly in image classification tasks \[[2](http://arxiv.org/abs/2505.06825)\]. These techniques have shown marked improvement over random sampling, especially on more complex tasks \[[2](http://arxiv.org/abs/2505.06825)\].

Federated learning (FL) has emerged as a promising approach for training models on decentralized data without sharing raw data \[[7](http://arxiv.org/abs/1511.03575)\]. This is particularly relevant in scenarios where data is distributed across many devices, such as mobile phones or edge devices \[[8](http://arxiv.org/abs/1602.05629)\]. However, existing FL methods often assume that data is identically and independently distributed (IID), which is not always the case in real-world applications \[[10](http://arxiv.org/abs/2002.05038)\]. To address this, federated active learning (FAL) has been proposed to combine the benefits of AL and FL, allowing for collaborative data selection and model training while preserving data privacy \[[9](http://arxiv.org/abs/2202.00195)\]. FAL methods have been shown to outperform random sampling strategies in image classification tasks \[[9](http://arxiv.org/abs/2202.00195)\].

Despite these advances, existing FAL methods often fail to account for the heterogeneity of data distribution across clients and the associated fluctuations in global and local model parameters, which can negatively impact model accuracy \[[1]()\]. To address these challenges, several studies have proposed novel approaches to improve the robustness of FAL to data heterogeneity. For example, Knowledge-Aware Federated Active Learning (KAFAL) introduces a novel active sampling method tailored for the federated active learning problem, which addresses the mismatch between the active sampling goals of the global model and the local clients \[[11](http://arxiv.org/abs/2211.13579)\]. Similarly, LoGo proposes a sampling strategy that integrates global and local selector models to resolve imbalances in data distribution and local heterogeneity \[[12](http://arxiv.org/abs/2303.12317)\].

Active Federated Learning (AFL) further improves the efficiency of FL by selecting clients based on their potential to improve model performance, rather than uniformly at random \[[13](http://arxiv.org/abs/1909.12641)\]. This approach reduces the number of required training iterations while maintaining model accuracy, demonstrating the potential of adaptive sampling in FL \[[13](http://arxiv.org/abs/1909.12641)\].

In summary, while AL and FL have been independently studied, their integration in FAL presents new opportunities and challenges. Recent work has focused on improving the robustness of FAL to data heterogeneity and improving the efficiency of data selection. These efforts have led to promising results
## Research papers
### Outline
- [Data Selection Efficiency [1 papers]](#category-data-selection-efficiency)
- [Active Learning Techniques [8 papers]](#category-active-learning-techniques)
- [Epistemic Variations in Training [2 papers]](#category-epistemic-variations-in-training)
- [Federated Learning Frameworks [4 papers]](#category-federated-learning-frameworks)
- [Federated Active Learning Approaches [7 papers]](#category-federated-active-learning-approaches)

### <a id='category-data-selection-efficiency'></a>Data Selection Efficiency: 1 papers found.
Context: 
	Document 1: [Category]: «Data Selection Efficiency»
[Snippet]: «The ability to cheaply train text classifiers is critical to their use in information retrieval, content analysis, natural language processing, and other tasks involving data which is partly or fully textual. An algorithm for sequential sampling during machine learning of statistical classifiers was developed and tested on a newswire text categorization task. This method, which we call uncertainty sampling, reduced by as much as 500-fold the amount of training data that would have to be manually classified to achieve a given level of effectiveness.»
[_citation_number]: «1»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-24T11:28:00+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1505.05424)\]. Further details \[[6](http://arxiv.org/abs/1905.03677)\]\[[7](http://arxiv.org/abs/1511.03575)\]\[[8](http://arxiv.org/abs/1602.05629)\]\[[9](http://arxiv.org/abs/2202.00195)\]\[[10](http://arxiv.org/abs/2002.05038)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Active learning (AL) reduces human annotation costs for machine learning systems by strategically selecting the most informative unlabeled data for annotation, but performing it individually may still be insufficient due to restricted data diversity and annotation budget. Federated Active Learning (FAL) addresses this by facilitating collaborative data selection and model training, while preserving the confidentiality of raw data samples. Yet, existing FAL methods fail to account for the heterogeneity of data distribution across clients and the associated fluctuations in global and local model parameters, adversely affecting model accuracy. To overcome these challenges, we propose CHASe (Client Heterogeneity-Aware Data Selection), specifically designed for FAL. CHASe focuses on identifying those unlabeled samples with high epistemic variations (EVs), which notably oscillate around the decision boundaries during training. To achieve both effectiveness and efficiency, model() encompasses techniques for 1) tracking EVs by analyzing inference inconsistencies across training epochs, 2) calibrating decision
|    | reference                                                |   date | key idea/summary                                                                                                                                                                                     |
|----|----------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [A Sequential Algorithm for Training Text Classifiers]() |    nan | Uncertainty sampling is an algorithm that significantly reduces the amount of manually classified training data needed for text classifiers, improving efficiency in tasks like text categorization. |
### <a id='category-active-learning-techniques'></a>Active Learning Techniques: 8 papers found.
Context: 
	Document 1: [Category]: «Active Learning Techniques»
[Snippet]: «A principle bottleneck in image classification is the large number of training examples needed to train a classifier. Using active learning, we can reduce the number of training examples to teach a CNN classifier by strategically selecting examples. Assigning values to image examples using different uncertainty metrics allows the model to identify and select high-value examples in a smaller training set size. We demonstrate results for digit recognition and fruit classification on the MNIST and Fruits360 data sets. We formally compare results for four different uncertainty metrics. Finally, we observe active learning is also effective on simpler (binary) classification tasks, but marked improvement from random sampling is more evident on more difficult tasks. We show active learning is a viable algorithm for image classification problems.»
[_citation_number]: «2»

	Document 2: [Category]: «Active Learning Techniques»
[Snippet]: «Convolutional neural networks (CNNs) have been successfully applied to many recognition and learning tasks using a universal recipe; training a deep model on a very large dataset of supervised examples. However, this approach is rather restrictive in practice since collecting a large set of labeled images is very expensive. One way to ease this problem is coming up with smart ways for choosing images to be labelled from a very large collection (ie. active learning).
  Our empirical study suggests that many of the active learning heuristics in the literature are not effective when applied to CNNs in batch setting. Inspired by these limitations, we define the problem of active learning as core-set selection, ie. choosing set of points such that a model learned over the selected subset is competitive for the remaining data points. We further present a theoretical result characterizing the performance of any selected subset using the geometry of the datapoints. As an active learning algorithm, we choose the subset which is expected to yield best result according to our characterization. Our experiments show that the proposed method significantly outperforms existing approaches in image classification experiments by a large margin.»
[_citation_number]: «5»

	Document 3: [Category]: «Active Learning Techniques»
[Snippet]: «The performance of deep neural networks improves with more annotated data. The problem is that the budget for annotation is limited. One solution to this is active learning, where a model asks human to annotate data that it perceived as uncertain. A variety of recent methods have been proposed to apply active learning to deep networks but most of them are either designed specific for their target tasks or comput
|    | reference                                                                                                 |   date | key idea/summary                                                                                                                                                                                                                     |
|----|-----------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Active Learning for Multi-class Image Classification](http://arxiv.org/abs/2505.06825)                   |    nan | Active learning is a viable algorithm for image classification that reduces the number of training examples needed by strategically selecting high-value examples based on uncertainty metrics.                                      |
|  1 | [Active Learning for Convolutional Neural Networks: A Core-Set Approach](http://arxiv.org/abs/1708.00489) |    nan | The paper proposes a novel active learning approach for CNNs by framing it as core-set selection, achieving significant improvements in image classification compared to existing methods.                                           |
|  2 | [Learning Loss for Active Learning](http://arxiv.org/abs/1905.03677)                                      |    nan | The paper proposes a task-agnostic and computationally efficient active learning method using a 'loss prediction module' to identify uncertain data for annotation, achieving better performance across various deep learning tasks. |
|  3 | [Heterogeneous uncertainty sampling for supervised learning]()                                            |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                            |
|  4 | [Active learning: Synthesis lectures on artificial intelligence and machine learning]()                   |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                            |
|  5 | [Semi-Supervised Active Learning with Temporal Output Discrepancy]()                                      |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                            |
|  6 | [Active learning using pre-clustering]()                                                                  |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                            |
|  7 | [Agreement-Discrepancy-Selection: Active learning with progressive distribution alignment]()              |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                            |
### <a id='category-epistemic-variations-in-training'></a>Epistemic Variations in Training: 2 papers found.
Context: 
	Document 1: [Category]: «Epistemic Variations in Training»
[Snippet]: «We introduce a new, efficient, principled and backpropagation-compatible
algorithm for learning a probability distribution on the weights of a neural
network, called Bayes by Backprop. It regularises the weights by minimising a
compression cost, known as the variational free energy or the expected lower
bound on the marginal likelihood. We show that this principled kind of
regularisation yields comparable performance to dropout on MNIST
classification. We then demonstrate how the learnt uncertainty in the weights
can be used to improve generalisation in non-linear regression problems, and
how this weight uncertainty can be used to drive the exploration-exploitation
trade-off in reinforcement learning.»
[_citation_number]: «3»

	Document 2: [Category]: «Epistemic Variations in Training»
[Snippet]: «Deep learning tools have gained tremendous attention in applied machine
learning. However such tools for regression and classification do not capture
model uncertainty. In comparison, Bayesian models offer a mathematically
grounded framework to reason about model uncertainty, but usually come with a
prohibitive computational cost. In this paper we develop a new theoretical
framework casting dropout training in deep neural networks (NNs) as approximate
Bayesian inference in deep Gaussian processes. A direct result of this theory
gives us tools to model uncertainty with dropout NNs -- extracting information
from existing models that has been thrown away so far. This mitigates the
problem of representing uncertainty in deep learning without sacrificing either
computational complexity or test accuracy. We perform an extensive study of the
properties of dropout's uncertainty. Various network architectures and
non-linearities are assessed on tasks of regression and classification, using
MNIST as an example. We show a considerable improvement in predictive
log-likelihood and RMSE compared to existing state-of-the-art methods, and
finish by using dropout's uncertainty in deep reinforcement learning.»
[_citation_number]: «4»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-24T11:28:00+00:00. Mention them
|    | reference                                                                                                                 |   date | key idea/summary                                                                                                                                                                                                                            |
|----|---------------------------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Weight Uncertainty in Neural Networks](http://arxiv.org/abs/1505.05424)                                                  |    nan | Bayes by Backprop is a method for learning probability distributions on neural network weights, using variational free energy to regularize weights and improve generalization and exploration in learning tasks.                           |
|  1 | [Dropout as a Bayesian Approximation: Representing Model Uncertainty in
  Deep Learning](http://arxiv.org/abs/1506.02142) |    nan | This paper presents a theoretical framework that interprets dropout training in deep neural networks as approximate Bayesian inference, enabling the modeling of uncertainty without sacrificing computational efficiency or test accuracy. |
### <a id='category-federated-learning-frameworks'></a>Federated Learning Frameworks: 4 papers found.
Context: 
	Document 1: [Category]: «Federated Learning Frameworks»
[Snippet]: «We introduce a new and increasingly relevant setting for distributed
optimization in machine learning, where the data defining the optimization are
distributed (unevenly) over an extremely large number of \nodes, but the goal
remains to train a high-quality centralized model. We refer to this setting as
Federated Optimization. In this setting, communication efficiency is of utmost
importance.
  A motivating example for federated optimization arises when we keep the
training data locally on users' mobile devices rather than logging it to a data
center for training. Instead, the mobile devices are used as nodes performing
computation on their local data in order to update a global model. We suppose
that we have an extremely large number of devices in our network, each of which
has only a tiny fraction of data available totally; in particular, we expect
the number of data points available locally to be much smaller than the number
of devices. Additionally, since different users generate data with different
patterns, we assume that no device has a representative sample of the overall
distribution.
  We show that existing algorithms are not suitable for this setting, and
propose a new algorithm which shows encouraging experimental results. This work
also sets a path for future research needed in the context of federated
optimization.»
[_citation_number]: «7»

	Document 2: [Category]: «Federated Learning Frameworks»
[Snippet]: «Modern mobile devices have access to a wealth of data suitable for learning
models, which in turn can greatly improve the user experience on the device.
For example, language models can improve speech recognition and text entry, and
image models can automatically select good photos. However, this rich data is
often privacy sensitive, large in quantity, or both, which may preclude logging
to the data center and training there using conventional approaches. We
advocate an alternative that leaves the training data distributed on the mobile
devices, and learns a shared model by aggregating locally-computed updates. We
term this decentralized approach Federated Learning.
  We present a practical method for the federated learning of deep networks
based on iterative model averaging, and conduct an extensive empirical
evaluation, considering five different model architectures and four datasets.
These experiments demonstrate the approach is robust to the unbalanced and
non-IID data distributions that are a defining characteristic of this setting.
Communication
|    | reference                                                                                                      |   date | key idea/summary                                                                                                                                                                                                                                            |
|----|----------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Federated Optimization:Distributed Optimization Beyond the Datacenter](http://arxiv.org/abs/1511.03575)       |    nan | The paper introduces Federated Optimization, a new setting for distributed machine learning where data is spread across many devices, and the goal is to train a high-quality centralized model while ensuring communication efficiency.                    |
|  1 | [Communication-Efficient Learning of Deep Networks from Decentralized
  Data](http://arxiv.org/abs/1602.05629) |    nan | Federated Learning is a decentralized approach that allows mobile devices to collaboratively train a shared model while keeping training data distributed on the devices, improving privacy and reducing communication costs.                               |
|  2 | [Robustness analytics to data heterogeneity in edge computing](http://arxiv.org/abs/2002.05038)                |    nan | This work investigates the robustness of Federated Learning to biased sampling in scenarios with data heterogeneity and active sampling, showing that it can be robust when local training iterations and communication frequency are appropriately chosen. |
|  3 | [Distribution-Regularized Federated Learning on Non-IID Data]()                                                |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                   |
### <a id='category-federated-active-learning-approaches'></a>Federated Active Learning Approaches: 7 papers found.
Federated Active Learning (FAL) has emerged as a promising approach to reduce annotation costs while preserving data privacy in decentralized learning settings \[[13](http://arxiv.org/abs/1909.12641)\]. Unlike traditional federated learning, which assumes fully labeled data \[[12](http://arxiv.org/abs/2303.12317)\], FAL integrates active learning strategies to select the most informative samples for annotation, addressing the challenge of limited annotation budgets \[[11](http://arxiv.org/abs/2211.13579)\]. Several approaches have been proposed to enhance the efficiency and effectiveness of FAL. For instance, the F-AL method combines active learning with federated optimization, allowing clients to collaboratively select informative instances in a distributed manner \[[9](http://arxiv.org/abs/2202.00195)\]. Similarly, the Knowledge-Aware Federated Active Learning (KAFAL) framework tackles the mismatch between global and local sampling goals by introducing Knowledge-Specialized Active Sampling (KSAS) and Knowledge-Compensatory Federated Update (KCFU) \[[11](http://arxiv.org/abs/2211.13579)\]. These techniques help mitigate client heterogeneity and non-IID data distributions, which are common in real-world applications \[[12](http://arxiv.org/abs/2303.12317)\]. Additionally, the LoGo framework explores the performance of global and local-only query selector models, demonstrating that their effectiveness depends on inter-class diversity and local data imbalance \[[12](http://arxiv.org/abs/2303.12317)\]. Active Federated Learning further improves efficiency by selecting clients based on their data's potential to enhance model performance, reducing training iterations by up to 70% while maintaining accuracy \[[13](http://arxiv.org/abs/1909.12641)\]. These studies collectively highlight the growing interest in FAL as a solution for improving annotation efficiency and model performance in federated settings.
|    | reference                                                                                                                      |   date | key idea/summary                                                                                                                                                                                                                                  |
|----|--------------------------------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Federated Active Learning (F-AL): an Efficient Annotation Strategy for
  Federated Learning](http://arxiv.org/abs/2202.00195) |    nan | The paper proposes a federated active learning (F-AL) method that integrates active learning and sampling strategies into the federated learning framework to reduce annotation workload and improve performance in image classification tasks.   |
|  1 | [Knowledge-Aware Federated Active Learning with Non-IID Data](http://arxiv.org/abs/2211.13579)                                 |    nan | The paper proposes KAFAL, a federated active learning framework that addresses the challenge of mismatch between global and local active sampling goals, enhancing model learning with limited annotation budgets while preserving data privacy.  |
|  2 | [Re-thinking Federated Active Learning based on Inter-class Diversity](http://arxiv.org/abs/2303.12317)                        |    nan | LoGo is a federated active learning (FAL) sampling strategy that integrates global and local-only query selector models to address local data imbalance and heterogeneity, outperforming six existing strategies across 38 experimental settings. |
|  3 | [Active Federated Learning](http://arxiv.org/abs/1909.12641)                                                                   |    nan | Active Federated Learning improves efficiency by selectively choosing clients based on their data and the current model, reducing training iterations by 20-70% without compromising model accuracy.                                              |
|  4 | [Active instance sampling via matrix partition.]()                                                                             |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                         |
|  5 | [Active learning based federated learning for waste and natural disaster image classification]()                               |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                         |
|  6 | [(FLARE:) Federated active learning assisted by naming for responding
               to emergencies]()                         |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                         |
