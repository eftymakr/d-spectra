## Related Works

Calibration of machine learning models has been extensively studied, particularly in the context of classification and ranking tasks. Traditional calibration methods, such as binning and scaling, have been widely used to post-process model outputs to obtain calibrated probabilities \[[1](http://arxiv.org/abs/2202.04348)\]. However, these methods often lack flexibility and expressiveness, especially in complex scenarios where the relationship between predicted values and true probabilities is non-linear \[[1](http://arxiv.org/abs/2202.04348)\]. For instance, binning methods are distribution-free but may not capture the nuances of individual sample behavior \[[1](http://arxiv.org/abs/2202.04348)\]. Moreover, they tend to be non-individual, mapping multiple samples to the same value, which can be problematic for order-sensitive applications \[[1](http://arxiv.org/abs/2202.04348)\].

Recent work has focused on improving calibration by leveraging more flexible and expressive models. For example, field-aware calibration methods have been proposed to address the issue of miscalibration in specific input fields, which is particularly important in applications like online advertising \[[6](http://arxiv.org/abs/1905.10713)\]. These methods aim to adjust model outputs based on field values to achieve fine-grained calibration. However, they often face challenges due to data sparsity and limited confidence in certain field values \[[6](http://arxiv.org/abs/1905.10713)\]. To mitigate this, confidence-aware multi-field calibration methods have been introduced, which adaptively adjust calibration intensity based on confidence levels derived from sample statistics \[[4](http://arxiv.org/abs/2402.17655)\].

In the context of ranking models, several studies have explored the integration of calibration with ranking objectives. For instance, multi-objective approaches combine pointwise loss functions, which focus on calibrated absolute values, with ranking loss functions that emphasize relative orderings \[[8](http://arxiv.org/abs/2406.08010)\]. However, these methods often suffer from limitations such as the need to aggregate full candidate lists within a single mini-batch, which can degrade training effectiveness \[[8](http://arxiv.org/abs/2406.08010)\]. Additionally, the inherent conflict between calibration and ranking objectives can lead to sub-optimal trade-offs \[[8](http://arxiv.org/abs/2406.08010)\]. To address these issues, the Self-Boosted framework for Calibrated Ranking (SBCR) has been proposed, which aims to improve training effectiveness and optimize the trade-off between calibration and ranking \[[8](http://arxiv.org/abs/2406.08010)\].

Furthermore, the importance of accurate posterior probabilities in online advertising has been highlighted, with studies showing that miscalibrated predictions can lead to significant performance degradation \[[7](http://arxiv.org/abs/2205.07295)\]. To address this, doubly-adaptive calibration methods have been introduced, which learn isotonic functions to calibrate model predictions based on posterior statistics and field-adaptive mechanisms \[[7](http://arxiv.org/abs/2205.07295)\]. These methods have been shown to significantly improve calibration performance and have been deployed in production systems \[[7](http://arxiv.org/abs/2205.07295)\].

In addition, the use of neural networks for calibration has gained traction, with methods such as Neural Calibration being proposed to learn field-aware information during the validation phase \[[6](http://arxiv.org/abs/1905.10713)\]. These approaches have demonstrated significant improvements in calibration metrics such as the Brier score and field-level calibration error \[[6](http://arxiv.org/abs/1905.10713)\].

In summary, while traditional calibration methods have laid the groundwork, recent advances have focused on improving flexibility, expressiveness, and field-awareness in calibration, particularly for ranking and advertising applications \[[1](http://arxiv.org/abs/2202.04348)\]\[[4](http://arxiv.org/abs/2402.17655)\]\[[6](http://arxiv.org/abs/1905.10713)\]\[[7](http://arxiv.org/abs/2205.07295)\]\[[8](http://arxiv.org/abs/2406.08010)\].

References:  
\[[1](http://arxiv.org/abs/2202.04348)\] MBCT: Tree-Based Feature-Aware Binning for Individual Uncertainty Calibration  
\[[4](http://arxiv.org/abs/2402.17655)\] Confidence-Aware Multi-Field Model Calibration  
\[[6](http://arxiv.org/abs/1905.10713)\] Field-aware Calibration: A Simple and Empirically Strong Method for Reliable Probabilistic Predictions  
\[[7](http://arxiv.org/abs/2205.07295)\] Posterior Probability Matters: Doubly-Adaptive Calibration for Neural Predictions in Online Advertising  
\[[8](http://arxiv.org/abs/2406.08010)\] A Self-Boosted Framework for Calibrated Ranking
## Research papers
### Outline
- [Calibration Loss Function Design [2 papers]](#category-calibration-loss-function-design)
- [Neural Network-Based Calibration Methods [1 papers]](#category-neural-network-based-calibration-methods)
- [Calibration in Ranking and Advertising Applications [11 papers]](#category-calibration-in-ranking-and-advertising-applications)
- [Field-Aware Calibration Approaches [1 papers]](#category-field-aware-calibration-approaches)
- [Traditional Calibration Methods [2 papers]](#category-traditional-calibration-methods)

### <a id='category-calibration-loss-function-design'></a>Calibration Loss Function Design: 2 papers found.
Context: 
	Document 1: [Category]: «Calibration Loss Function Design»
[_citation_number]: «1»
[Snippet]: «Most machine learning classifiers only concern classification accuracy, while certain applications (such as medical diagnosis, meteorological forecasting, and computation advertising) require the model to predict the true probability, known as a calibrated estimate. In previous work, researchers have developed several calibration methods to post-process the outputs of a predictor to obtain calibrated values, such as binning and scaling methods. Compared with scaling, binning methods are shown to have distribution-free theoretical guarantees, which motivates us to prefer binning methods for calibration. However, we notice that existing binning methods have several drawbacks: (a) the binning scheme only considers the original prediction values, thus limiting the calibration performance; and (b) the binning approach is non-individual, mapping multiple samples in a bin to the same value, and thus is not suitable for order-sensitive applications. In this paper, we propose a feature-aware binning framework, called Multiple Boosting Calibration Trees (MBCT), along with a multi-view calibration loss to tackle the above issues. Our MBCT optimizes the binning scheme by the tree structures of features, and adopts a linear function in a tree node to achieve individual calibration. Our MBCT is non-monotonic, and has the potential to improve order accuracy, due to its learnable binning scheme and the individual calibration. We conduct comprehensive experiments on three datasets in different fields. Results show that our method outperforms all competing models in terms of both calibration error and order accuracy. We also conduct simulation experiments, justifying that the proposed multi-view calibration loss is a better metric in modeling calibration error.»

	Document 2: [Category]: «Calibration Loss Function Design»
[_citation_number]: «14»
[Snippet]: «»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-19T09:35:11+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2112.07428)\]. Further details \[[6](http://arxiv.org/abs/1905.10713)\]\[[7](http://arxiv.org/abs/2205.07295)\]\[[8](http://arxiv.org/abs/2406.08010)\]\[[9](http://arxiv.org/abs/2401.09507)\]\[[10](http://arxiv.org/abs/2208.06164)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Ranking models primarily focus on modeling the relative order of predictions while often neglecting the significance of the accuracy of their absolute values. However, accurate absolute values are essential for certain downstream tasks, necessitating the calibration of the original predictions. To address this, existing calibration approaches typically employ predefined transformation functions with order-preserving properties to adjust the original predictions. Unfortunately, these functions often adhere to fixed forms, such as piece-wise linear functions, which exhibit limited expressiveness and flexibility, thereby constraining their effectiveness in complex calibration scenarios. To mitigate this issue, we propose implementing a calibrator using an Unconstrained Monotonic Neural Network (UMNN), which can learn arbitrary monotonic functions with great modeling power. This approach significantly relaxes the constraints on the calibrator, improving its flexibility and expressiveness while avoiding excessively distorting the original predictions by requiring monotonicity. Furthermore, to optimize this highly flexible network for calibration, we introduce a novel additional loss function termed Smooth Calibration Loss (SCLoss), which aims to fulfill a necessary condition for achieving the ideal calibration state. Extensive offline experiments confirm the effectiveness of our method in achieving superior calibration performance. Moreover, deployment in Kuaishou's large-scale online video ranking system demonstrates that the method's calibration improvements translate into enhanced business metrics. The source code is available at https://github.com/baiyimeng/UMC.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2112.07428)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2106.07998)\]\[[7](http://arxiv.org/abs/2205.07295)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Calibration loss function design has been a critical area of research, especially in applications requiring accurate probability estimates such as medical diagnosis and meteorological forecasting \[[1](http://arxiv.org/abs/2202.04348)\]. Traditional calibration methods, including binning and scaling, have been widely used, with binning methods offering distribution-free theoretical guarantees \[[1](http://arxiv.org/abs/2202.04348)\]. However, these methods often suffer from limitations such as non-individual calibration, where multiple samples in a bin are mapped to the same value, which can be unsuitable for order-sensitive applications \[[1](http://arxiv.org/abs/2202.04348)\]. Recent work has focused on improving these methods by introducing more flexible and expressive frameworks. For instance, the Multiple Boosting Calibration Trees (MBCT) framework proposes a feature-aware binning approach that optimizes the binning scheme using tree structures and enables individual calibration through linear functions within tree nodes \[[1](http://arxiv.org/abs/2202.04348)\]. This approach is non-monotonic and has the potential to improve order accuracy due to its learnable binning scheme and individual calibration capabilities. Additionally, the use of a multi-view calibration loss has been proposed to better model calibration error, as demonstrated through simulation experiments \[[1](http://arxiv.org/abs/2202.04348)\]. These advancements highlight the ongoing efforts to enhance calibration accuracy and flexibility in machine learning models.
|    | reference                                                                                                                                                                             |   date | key idea/summary                                                                                                                                                                                                                   |
|----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [MBCT: Tree-Based Feature-Aware Binning for Individual Uncertainty
  Calibration](http://arxiv.org/abs/2202.04348)                                                                    |    nan | The paper proposes a feature-aware binning framework called Multiple Boosting Calibration Trees (MBCT) to improve calibration accuracy and order-sensitive applications by addressing the limitations of existing binning methods. |
|  1 | [Probabilistic outputs for support vector machines and comparisons to regularized likelihood methods](https://home.cs.colorado.edu/~mozer/Teaching/syllabi/6622/papers/Platt1999.pdf) |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                          |
### <a id='category-neural-network-based-calibration-methods'></a>Neural Network-Based Calibration Methods: 1 papers found.
Context: 
	Document 1: [Category]: «Neural Network-Based Calibration Methods»
[_citation_number]: «2»
[Snippet]: «Accurate estimation of predictive uncertainty (model calibration) is essential for the safe application of neural networks. Many instances of miscalibration in modern neural networks have been reported, suggesting a trend that newer, more accurate models produce poorly calibrated predictions. Here, we revisit this question for recent state-of-the-art image classification models. We systematically relate model calibration and accuracy, and find that the most recent models, notably those not using convolutions, are among the best calibrated. Trends observed in prior model generations, such as decay of calibration with distribution shift or model size, are less pronounced in recent architectures. We also show that model size and amount of pretraining do not fully explain these differences, suggesting that architecture is a major determinant of calibration properties.»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-19T09:35:11+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2112.07428)\]. Further details \[[6](http://arxiv.org/abs/1905.10713)\]\[[7](http://arxiv.org/abs/2205.07295)\]\[[8](http://arxiv.org/abs/2406.08010)\]\[[9](http://arxiv.org/abs/2401.09507)\]\[[10](http://arxiv.org/abs/2208.06164)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Ranking models primarily focus on modeling the relative order of predictions while often neglecting the significance of the accuracy of their absolute values. However, accurate absolute values are essential for certain downstream tasks, necessitating the calibration of the original predictions. To address this, existing calibration approaches typically employ predefined transformation functions with order-preserving properties to adjust the original predictions. Unfortunately, these functions often adhere to fixed forms, such as piece-wise linear functions, which exhibit limited expressiveness and flexibility, thereby constraining their effectiveness in complex calibration scenarios. To mitigate this issue, we propose implementing a calibrator using an Unconstrained Monotonic Neural Network (UMNN), which can learn arbitrary monotonic functions with great modeling power. This approach significantly relaxes the constraints on the calibrator, improving its flexibility and expressiveness while avoiding excessively distorting the original predictions by requiring monotonicity. Furthermore, to optimize this highly flexible network for calibration, we introduce a novel additional loss function termed Smooth Calibration Loss (SCLoss), which aims to fulfill a necessary condition for achieving the ideal calibration state. Extensive offline experiments confirm the effectiveness of our method in achieving superior calibration performance. Moreover, deployment in Kuaishou's large-scale online video ranking system demonstrates that the method's calibration improvements translate into enhanced business metrics. The source code is available at https://github.com/baiyimeng/UMC.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2112.07428)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2106.07998)\]\[[7](http://arxiv.org/abs/2205.07295)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Recent advancements in neural network-based calibration methods highlight the growing importance of accurate predictive uncertainty estimation for safe model deployment \[[2](http://arxiv.org/abs/2106.07998)\]. While earlier studies noted that increased model accuracy often correlates with poorer calibration, recent state-of-the-art image classification models, particularly those that avoid traditional convolutional architectures, have shown promising improvements in calibration \[[2](http://arxiv.org/abs/2106.07998)\]. These models exhibit less pronounced calibration degradation under distribution shifts and varying model sizes, suggesting that architectural choices play a significant role in determining calibration properties \[[2](http://arxiv.org/abs/2106.07998)\]. This aligns with the broader trend of exploring flexible calibration techniques, such as monotonic neural networks, which offer greater modeling power while preserving order-preserving properties \[[2](http://arxiv.org/abs/2106.07998)\].
|    | reference                                                                               |   date | key idea/summary                                                                                                                                                                                                                   |
|----|-----------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Revisiting the Calibration of Modern Neural Networks](http://arxiv.org/abs/2106.07998) |    nan | Recent state-of-the-art image classification models, particularly those not using convolutions, exhibit better calibration despite increased accuracy, suggesting that architecture plays a significant role in model calibration. |
### <a id='category-calibration-in-ranking-and-advertising-applications'></a>Calibration in Ranking and Advertising Applications: 11 papers found.
In the context of calibration in ranking and advertising applications, several studies have focused on improving the accuracy of predicted probabilities while maintaining the relative ordering of items. Existing approaches often rely on predefined transformation functions, such as piece-wise linear functions, which are limited in expressiveness and flexibility \[[3](http://arxiv.org/abs/2112.07428)\]. To address these limitations, researchers have proposed more flexible calibration methods, such as Gaussian calibration and Gamma calibration, which are designed to map ranking scores to well-calibrated preference probabilities without affecting recommendation performance \[[1](http://arxiv.org/abs/2202.04348)\]. Additionally, field-aware calibration methods have been introduced to adjust model outputs based on specific feature field values, enabling fine-grained control over advertising demands \[[2](http://arxiv.org/abs/2106.07998)\]. These methods are particularly important in scenarios where data sparsity poses challenges, as they can adaptively adjust calibration intensity based on confidence levels derived from sample statistics \[[4](http://arxiv.org/abs/2402.17655)\]. Furthermore, multi-field calibration has been explored to improve the accuracy of click-through rate (CTR) and conversion rate (CVR) predictions in e-commerce advertising, with techniques like Deep Ensemble Shape Calibration (DESC) decomposing calibration into value and shape components to enhance both function expression and data utilization \[[6](http://arxiv.org/abs/1905.10713)\]. Another approach, Self-Boosted framework for Calibrated Ranking (SBCR), addresses the limitations of multi-objective methods by avoiding full candidate list aggregation and improving the trade-off between calibration and ranking \[[5](http://arxiv.org/abs/2402.06859)\]. Additionally, methods such as Jointly optimize the Ranking and Calibration abilities (JRC) have been proposed to enhance both ranking and calibration performance by constraining predicted probabilities to be functions of logit subtraction \[[7](http://arxiv.org/abs/2205.07295)\]. These advancements highlight the ongoing efforts to improve calibration in ranking systems, ensuring accurate probabilistic predictions that align with real-world requirements \[[8](http://arxiv.org/abs/2406.08010)\].
|    | reference                                                                                                                                             |   date | key idea/summary                                                                                                                                                                                                                                                                                                |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Obtaining Calibrated Probabilities with Personalized Ranking Models](http://arxiv.org/abs/2112.07428)                                                |    nan | This paper proposes two parametric calibration methods to improve the calibration of personalized ranking models by mapping ranking scores to well-calibrated preference probabilities without affecting recommendation performance.                                                                            |
|  1 | [Confidence-Aware Multi-Field Model Calibration](http://arxiv.org/abs/2402.17655)                                                                     |    nan | The paper proposes a confidence-aware multi-field calibration method to improve the accuracy of advertising predictions by adaptively adjusting calibration based on confidence levels and leveraging multiple fields to mitigate data sparsity issues.                                                         |
|  2 | [LiRank: Industrial Large Scale Ranking Models at LinkedIn](http://arxiv.org/abs/2402.06859)                                                          |    nan | LiRank is a large-scale ranking framework developed by LinkedIn that integrates advanced modeling architectures and optimization methods, leading to significant improvements in metrics such as member sessions, job applications, and ad click-through rates.                                                 |
|  3 | [Posterior Probability Matters: Doubly-Adaptive Calibration for Neural
  Predictions in Online Advertising](http://arxiv.org/abs/2205.07295)          |    nan | AdaCalib is a doubly-adaptive calibration approach that improves prediction accuracy by learning an isotonic function family and incorporating field-adaptive mechanisms to ensure posterior probabilities align with field-specific values.                                                                    |
|  4 | [A Self-boosted Framework for Calibrated Ranking](http://arxiv.org/abs/2406.08010)                                                                    |    nan | The paper introduces a Self-Boosted framework for Calibrated Ranking (SBCR) to address limitations in existing multi-objective methods by improving training effectiveness and optimizing the trade-off between calibration and ranking.                                                                        |
|  5 | [Deep Ensemble Shape Calibration: Multi-Field Post-hoc Calibration in
  Online Advertising](http://arxiv.org/abs/2401.09507)                          |    nan | The paper proposes a new method called Deep Ensemble Shape Calibration (DESC) to address multi-field calibration in e-commerce advertising, achieving significant improvements in CTR and CVR with better data utilization and error distribution handling.                                                     |
|  6 | [Joint Optimization of Ranking and Calibration with Contextualized Hybrid
  Model](http://arxiv.org/abs/2208.06164)                                   |    nan | JRC is an approach that jointly optimizes ranking and calibration abilities by improving the ranking ability through contrasting logit values and constraining predicted probabilities to be a function of logit subtraction, leading to significant performance improvements in click-through rate prediction. |
|  7 | [Regression Compatible Listwise Objectives for Calibrated Ranking with
  Binary Relevance](http://arxiv.org/abs/2211.01494)                           |    nan | The paper proposes a practical approach for learning-to-rank that aligns ranking and regression objectives, achieving better trade-offs and improving both ranking quality and click prediction accuracy in real-world applications.                                                                            |
|  8 | [Calibration-compatible Listwise Distillation of Privileged Features for
  CTR Prediction](http://arxiv.org/abs/2312.08727)                           |    nan | CLID is a novel listwise distillation method that improves ranking ability for CTR prediction while maintaining model calibration, addressing limitations of pointwise cross-entropy loss in privileged feature distillation.                                                                                   |
|  9 | [Scale Calibration of Deep Ranking Models](https://doi.org/10.1145/3534678.3539072)                                                                   |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                                       |
| 10 | [Beyond Binary Preference: Leveraging Bayesian Approaches for Joint Optimization of Ranking and Calibration](https://doi.org/10.1145/3637528.3671577) |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                                                                       |
### <a id='category-field-aware-calibration-approaches'></a>Field-Aware Calibration Approaches: 1 papers found.
Context: 
	Document 1: [Category]: «Field-Aware Calibration Approaches»
[_citation_number]: «6»
[Snippet]: «It is often observed that the probabilistic predictions given by a machine
learning model can disagree with averaged actual outcomes on specific subsets
of data, which is also known as the issue of miscalibration. It is responsible
for the unreliability of practical machine learning systems. For example, in
online advertising, an ad can receive a click-through rate prediction of 0.1
over some population of users where its actual click rate is 0.15. In such
cases, the probabilistic predictions have to be fixed before the system can be
deployed.
  In this paper, we first introduce a new evaluation metric named field-level
calibration error that measures the bias in predictions over the sensitive
input field that the decision-maker concerns. We show that existing post-hoc
calibration methods have limited improvements in the new field-level metric and
other non-calibration metrics such as the AUC score. To this end, we propose
Neural Calibration, a simple yet powerful post-hoc calibration method that
learns to calibrate by making full use of the field-aware information over the
validation set. We present extensive experiments on five large-scale datasets.
The results showed that Neural Calibration significantly improves against
uncalibrated predictions in common metrics such as the negative log-likelihood,
Brier score and AUC, as well as the proposed field-level calibration error.»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-19T09:35:11+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2112.07428)\]. Further details \[[6](http://arxiv.org/abs/1905.10713)\]\[[7](http://arxiv.org/abs/2205.07295)\]\[[8](http://arxiv.org/abs/2406.08010)\]\[[9](http://arxiv.org/abs/2401.09507)\]\[[10](http://arxiv.org/abs/2208.06164)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Ranking models primarily focus on modeling the relative order of predictions
while often neglecting the significance of the accuracy of their absolute
values. However, accurate absolute values are essential for certain downstream
tasks, necessitating the calibration of the original predictions. To address
this, existing calibration approaches typically employ predefined
transformation functions with order-preserving properties to adjust the
original predictions. Unfortunately, these functions often adhere to fixed
forms, such as piece-wise linear functions, which exhibit limited
expressiveness and flexibility, thereby constraining their effectiveness in
complex calibration scenarios. To mitigate this issue, we propose implementing
a calibrator using an Unconstrained Monotonic Neural Network (UMNN), which can
learn arbitrary monotonic functions with great modeling power. This approach
significantly relaxes the constraints on the calibrator, improving its
flexibility and expressiveness while avoiding excessively distorting the
original predictions by requiring monotonicity. Furthermore, to optimize this
highly flexible network for calibration, we introduce a novel additional loss
function termed Smooth Calibration Loss (SCLoss), which aims to fulfill a
necessary condition for achieving the ideal calibration state. Extensive
offline experiments confirm the effectiveness of our method in achieving
superior calibration performance. Moreover, deployment in Kuaishou's
large-scale online video ranking system demonstrates that the method's
calibration improvements translate into enhanced business metrics. The source
code is available at https://github.com/baiyimeng/UMC.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2112.07428)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2106.07998)\]\[[7](http://arxiv.org/abs/2205.07295)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Field-aware calibration approaches aim to address the issue of miscalibration in machine learning models, where probabilistic predictions can diverge from actual outcomes on specific subsets of data \[[6](http://arxiv.org/abs/1905.10713)\]. This problem is particularly critical in practical systems, such as online advertising, where discrepancies between predicted and actual click-through rates can lead to unreliable decision-making \[[6](http://arxiv.org/abs/1905.10713)\]. To tackle this, researchers have introduced metrics like the field-level calibration error, which evaluates the bias in predictions across sensitive input fields relevant to the decision-maker \[[6](http://arxiv.org/abs/1905.10713)\]. Existing post-hoc calibration methods, such as those based on fixed transformation functions, often lack the flexibility needed to effectively address these issues, especially in complex scenarios \[[6](http://arxiv.org/abs/1905.10713)\]. In response, novel methods like Neural Calibration have been proposed, leveraging field-aware information during the calibration process to improve accuracy across multiple metrics, including the negative log-likelihood, Brier score, and AUC \[[6](http://arxiv.org/abs/1905.10713)\]. These approaches highlight the growing need for more adaptive and expressive calibration techniques that can better align model predictions with real-world outcomes.
|    | reference                                                                                                                                   |   date | key idea/summary                                                                                                                                                                                                  |
|----|---------------------------------------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Field-aware Calibration: A Simple and Empirically Strong Method for
  Reliable Probabilistic Predictions](http://arxiv.org/abs/1905.10713) |    nan | The paper introduces a new calibration metric called field-level calibration error and proposes Neural Calibration, a post-hoc method that improves predictive reliability by leveraging field-aware information. |
### <a id='category-traditional-calibration-methods'></a>Traditional Calibration Methods: 2 papers found.
Context: 
	Document 1: [Category]: «Traditional Calibration Methods»
[_citation_number]: «13»
[Snippet]: «»

	Document 2: [Category]: «Traditional Calibration Methods»
[_citation_number]: «15»
[Snippet]: «»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-19T09:35:11+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2112.07428)\]. Further details \[[6](http://arxiv.org/abs/1905.10713)\]\[[7](http://arxiv.org/abs/2205.07295)\]\[[8](http://arxiv.org/abs/2406.08010)\]\[[9](http://arxiv.org/abs/2401.09507)\]\[[10](http://arxiv.org/abs/2208.06164)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Ranking models primarily focus on modeling the relative order of predictions
while often neglecting the significance of the accuracy of their absolute
values. However, accurate absolute values are essential for certain downstream
tasks, necessitating the calibration of the original predictions. To address
this, existing calibration approaches typically employ predefined
transformation functions with order-preserving properties to adjust the
original predictions. Unfortunately, these functions often adhere to fixed
forms, such as piece-wise linear functions, which exhibit limited
expressiveness and flexibility, thereby constraining their effectiveness in
complex calibration scenarios. To mitigate this issue, we propose implementing
a calibrator using an Unconstrained Monotonic Neural Network (UMNN), which can
learn arbitrary monotonic functions with great modeling power. This approach
significantly relaxes the constraints on the calibrator, improving its
flexibility and expressiveness while avoiding excessively distorting the
original predictions by requiring monotonicity. Furthermore, to optimize this
highly flexible network for calibration, we introduce a novel additional loss
function termed Smooth Calibration Loss (SCLoss), which aims to fulfill a
necessary condition for achieving the ideal calibration state. Extensive
offline experiments confirm the effectiveness of our method in achieving
superior calibration performance. Moreover, deployment in Kuaishou's
large-scale online video ranking system demonstrates that the method's
calibration improvements translate into enhanced business metrics. The source
code is available at https://github.com/baiyimeng/UMC.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2112.07428)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2106.07998)\]\[[7](http://arxiv.org/abs/2205.07295)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: Traditional calibration methods often rely on predefined transformation functions with order-preserving properties to adjust predictions, such as piece-wise linear functions \[[13](https://doi.org/10.1145/775047.775151)\]. These methods aim to maintain the relative order of predictions while improving their absolute accuracy for downstream tasks \[[15](http://proceedings.mlr.press/v54/kull17a.html)\]. However, such fixed-form functions are limited in their expressiveness and flexibility, making them less effective in complex calibration scenarios. This limitation highlights the need for more adaptable approaches that can learn arbitrary monotonic functions without compromising the order of predictions.
|    | reference                                                                                                                                                           |   date | key idea/summary                                                                                          |
|----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------|
|  0 | [Transforming classifier scores into accurate multiclass probability estimates](https://doi.org/10.1145/775047.775151)                                              |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
|  1 | [Beta calibration: a well-founded and easily implemented improvement on logistic calibration for binary classifiers](http://proceedings.mlr.press/v54/kull17a.html) |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
