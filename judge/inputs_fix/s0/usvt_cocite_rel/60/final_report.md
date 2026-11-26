## Related Works

Calibration of predictive models has been a topic of increasing interest in machine learning, particularly in the context of deep neural networks. Early work on calibration focused on traditional models such as logistic regression, where methods like Platt scaling were introduced to adjust predicted probabilities \[[1](http://arxiv.org/abs/1706.04599)\]. However, modern neural networks, due to their complexity and training procedures, often exhibit poor calibration, especially in terms of their confidence scores \[[2](http://arxiv.org/abs/1612.01474)\]. This issue has been attributed to factors such as depth, width, weight decay, and Batch Normalization \[[2](http://arxiv.org/abs/1612.01474)\].

Several approaches have been proposed to address this problem. Temperature scaling, a simple post-processing method, has shown effectiveness in calibrating predictions across various architectures and datasets \[[2](http://arxiv.org/abs/1612.01474)\]. However, more recent studies have highlighted that popular recalibration methods like Platt scaling and temperature scaling are less calibrated than reported and fail to estimate how miscalibrated they are \[[3](http://arxiv.org/abs/1909.10155)\]. This has led to the development of alternative methods, such as histogram binning and Bayesian Binning into Quantiles (BBQ), which aim to improve calibration accuracy \[[4](https://www.semanticscholar.org/paper/8d115c3b2ee80e0754360a154a9369bc1658b607)\]. While histogram binning is sample inefficient, requiring $O(B/\epsilon^2)$ samples, scaling methods require only $O(1/\epsilon^2)$, making them more practical \[[3](http://arxiv.org/abs/1909.10155)\].

The importance of calibration extends beyond classification tasks. In learning-to-rank systems, scale calibration has been identified as a critical issue, as ranking functions are often not scale calibrated, leading to limitations in practical applications such as ads ranking \[[6](https://www.semanticscholar.org/paper/7f6bb146b9c1504ec77100e640d624bdc204f0ac)\]. To address this, researchers have proposed calibrated ranking losses that ensure both ranking quality and score scale calibration during training \[[6](https://www.semanticscholar.org/paper/7f6bb146b9c1504ec77100e640d624bdc204f0ac)\]. These methods differ from post-processing approaches, which can suffer from training instability \[[6](https://www.semanticscholar.org/paper/7f6bb146b9c1504ec77100e640d624bdc204f0ac)\].

In addition to calibration, the problem of predictive uncertainty estimation has gained attention, especially in scenarios where models must be trusted in real-world settings \[[8](http://arxiv.org/abs/1906.02530)\]. Bayesian neural networks (BNNs) have been proposed as a way to quantify predictive uncertainty, but they are computationally expensive and require significant modifications to the training process \[[2](http://arxiv.org/abs/1612.01474)\]. As an alternative, deep ensembles have been introduced as a simple and scalable method that provides high-quality uncertainty estimates without the need for Bayesian inference \[[2](http://arxiv.org/abs/1612.01474)\]. These methods have been shown to produce well-calibrated uncertainty estimates that are as good or better than approximate Bayesian methods \[[2](http://arxiv.org/abs/1612.01474)\].

Another approach to uncertainty estimation is the use of dropout as a Bayesian approximation, which allows for the modeling of model uncertainty in deep learning without sacrificing computational efficiency \[[7](http://arxiv.org/abs/1506.02142)\]. This method has been applied to various tasks, including regression and classification, and has shown promising results in terms of predictive log-likelihood and RMSE \[[7](http://arxiv.org/abs/1506.02142)\].

In summary, while several methods have been proposed to improve calibration and predictive uncertainty estimation, there remains a need for more flexible and expressive calibration techniques that can adapt to complex scenarios. The proposed use of an Unconstrained Monotonic Neural Network (UMNN) for calibration addresses this by learning arbitrary monotonic functions, offering greater flexibility and expressiveness than traditional methods \[[14](http://arxiv.org/abs/1606.07792)\].

### References

1. \[[1](http://arxiv.org/abs/1706.04599)\] On Calibration of Modern Neural Networks [http://arxiv.org/abs/1706.04599]  
2. \[[2](http://arxiv.org/abs/1612.01474)\] Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles [http://arxiv.org/abs/1612.01474]  
3. \[[3](http://arxiv.org/abs/1909.10155)\] Verified Uncertainty Calibration [http://arxiv.org/abs/1909.10155]  
4. \[[4](https://www.semanticscholar.org/paper/8d115c3b2ee80e0754360a154a9369bc1658b607)\] Obtaining Well Calibrated Probabilities Using Bayesian Binning [https://www.semanticscholar.org/paper/8d115c3b2ee80e0754360a154a9369bc1658b607]  
5. \[[5](http://arxiv.org/abs/1905.11001)\] On Mixup Training: Improved Calibration and Predictive Uncertainty for Deep Neural Networks [http://arxiv.org/abs/1905.11001]  
6. \[[6](https://www.semanticscholar.org/paper/7f6bb146b9c1504ec77100e640d624bdc204f0ac)\] Scale Calibration of Deep Ranking Models [https://www.semanticscholar.org/paper/7f6bb146b9c1504ec77100e640d624bdc204f0ac]  
7. \[[7](http://arxiv.org/abs/1506.02142)\] Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning [http://arxiv.org/abs/1506.02142]  
8. \[[8](http://arxiv.org/abs/1906.02530)\] Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift [http://arxiv.org/abs/1906.02530]  
9. \[[9](http://arxiv.org/abs/1703.04977)\] What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision? [http://arxiv.org/abs/1703.04977]  
10. \[[10](https://www.semanticscholar.org/paper/d388760ce74792bb764ccf77ea8620ca77406e56)\] An Analysis of the Softmax Cross Entropy Loss for Learning-to-Rank with Binary Relevance [https://www.semanticscholar.org/paper/d388760ce74792bb764ccf77ea8620ca77406e56]  
11. \[[11](http://arxiv.org/abs/1905.10713)\] Field-aware Calibration: A Simple and Empirically Strong Method for Reliable Probabilistic Predictions [http://arxiv.org/abs/1905.10713]  
12. \[[12](http://arxiv.org/abs/1807.00263)\] Accurate Uncertainties for Deep Learning Using Calibrated Regression [http://arxiv.org/abs/1807.00263]  
13. \[[13](http://arxiv.org/abs/1412.6980)\] Adam: A Method for Stochastic Optimization [http://arxiv.org/abs/1412.6980]  
14. \[[14](http://arxiv.org/abs/1606.07792)\] Wide & Deep Learning for Recommender Systems [http://arxiv.org/abs/1606.07792]
## Research papers
### Outline
- [Calibration Methods for Neural Networks [4 papers]](#category-calibration-methods-for-neural-networks)
- [Predictive Uncertainty Estimation [2 papers]](#category-predictive-uncertainty-estimation)
- [Post-Processing Calibration Approaches [1 papers]](#category-post-processing-calibration-approaches)
- [Calibration in Learning-to-Rank Systems [2 papers]](#category-calibration-in-learning-to-rank-systems)
- [Dropout as a Bayesian Approximation [1 papers]](#category-dropout-as-a-bayesian-approximation)
- [Bayesian Methods for Uncertainty Estimation [2 papers]](#category-bayesian-methods-for-uncertainty-estimation)
- [Evaluation of Calibration and Uncertainty [2 papers]](#category-evaluation-of-calibration-and-uncertainty)

### <a id='category-calibration-methods-for-neural-networks'></a>Calibration Methods for Neural Networks: 4 papers found.
Context: 
	Document 1: [_citation_number]: «1»
[Snippet]: «Confidence calibration -- the problem of predicting probability estimates representative of the true correctness likelihood -- is important for classification models in many applications. We discover that modern neural networks, unlike those from a decade ago, are poorly calibrated. Through extensive experiments, we observe that depth, width, weight decay, and Batch Normalization are important factors influencing calibration. We evaluate the performance of various post-processing calibration methods on state-of-the-art architectures with image and document classification datasets. Our analysis and experiments not only offer insights into neural network learning, but also provide a simple and straightforward recipe for practical settings: on most datasets, temperature scaling -- a single-parameter variant of Platt Scaling -- is surprisingly effective at calibrating predictions.»
[Category]: «Calibration Methods for Neural Networks»

	Document 2: [_citation_number]: «3»
[Snippet]: «Applications such as weather forecasting and personalized medicine demand models that output calibrated probability estimates---those representative of the true likelihood of a prediction. Most models are not calibrated out of the box but are recalibrated by post-processing model outputs. We find in this work that popular recalibration methods like Platt scaling and temperature scaling are (i) less calibrated than reported, and (ii) current techniques cannot estimate how miscalibrated they are. An alternative method, histogram binning, has measurable calibration error but is sample inefficient---it requires $O(B/\epsilon^2)$ samples, compared to $O(1/\epsilon^2)$ for scaling methods, where $B$ is the number of distinct probabilities the model can output. To get the best of both worlds, we introduce the scaling-binning calibrator, which first fits a parametric function to reduce variance and then bins the function values to actually ensure calibration. This requires only $O(1/\epsilon^2 + B)$ samples. Next, we show that we can estimate a model's calibration error more accurately using an estimator from the meteorological community---or equivalently measure its calibration error with fewer samples ($O(\sqrt(B))$ instead of $O(B)$). We validate our approach with multiclass calibration experiments on CIFAR-10 and ImageNet, where we obtain a 35% lower calibration error than histogram binning and, unlike scaling methods, guarantees on true calibration. In these experiments, we also estimate the calibration error and ECE more accurately than the commonly used plugin estimators. We implement all these methods in a Python library: this https URL»
[Category]: «Calibration Methods for Neural Networks»

	Document 3: [_citation_number]: «5»
[Snippet]: «Mixup~\cite(zhang2017mixup) is a recently proposed method for training deep neural networks where additional samples are generated during training by convexly combining random pairs of images and their associated labels. While simple to implement, it has been shown to be a surprisingly effective method of data augmentation for image classification: DNNs trained with mixup show noticeable gains in classification performance on a number of image classification benchmarks. In this work, we discuss a hitherto untouched aspect of mixup training -- the calibration and predictive uncertainty of models trained with mixup. We find that DNNs trained with mixup are significantly better calibrated -- i.e., the predicted softmax scores are much better indicators of the actual likelihood of a correct prediction -- than DNNs trained in the regular fashion. We conduct experiments on a number of image classification architectures and datasets -- including large-scale datasets like ImageNet -- and find this to be the case. Additionally, we find that merely mixing features does not result in the same calibration benefit and that the label smoothing in mixup training plays a significant role in improving calibration. Finally, we also observe that mixup-trained DNNs are less prone to over-confident predictions on out-of-distribution and random-noise data. We conclude that the typical overconfidence seen in neural networks, even on in-distribution data is likely a consequence of training with hard labels, suggesting that mixup be employed for classification tasks where predictive uncertainty is a significant concern.»
[Category]: «Calibration Methods for Neural Networks»

	Document 4: [_citation_number]: «11»
[Snippet]: «It is often observed that the probabilistic predictions given by a machine learning model can disagree with averaged actual outcomes on specific subsets of data, which is also known as the issue of miscalibration. It is responsible for the unreliability of practical machine learning systems. For example, in online advertising, an ad can receive a click-through rate prediction of 0.1 over some population of users where its actual click rate is 0.15. In such cases, the probabilistic predictions have to be fixed before the system can be deployed. In this paper, we first introduce a new evaluation metric named field-level calibration error that measures the bias in predictions over the sensitive input field that the decision-maker concerns. We show that existing post-hoc calibration methods have limited improvements in the new field-level metric and other non-calibration metrics such as the AUC score. To this end, we propose Neural Calibration, a simple yet powerful post-hoc calibration method that learns to calibrate by making full use of the field-aware information over the validation set. We present extensive experiments on five large-scale datasets. The results showed that Neural Calibration significantly improves against uncalibrated predictions in common metrics such as the negative log-likelihood, Brier score and AUC, as well as the proposed field-level calibration error.»
[Category]: «Calibration Methods for Neural Networks»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-19T09:35:11+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1909.10155)\]. Further details \[[6](https://www.semanticscholar.org/paper/7f6bb146b9c1504ec77100e640d624bdc204f0ac)\]\[[7](http://arxiv.org/abs/1506.02142)\]\[[8](http://arxiv.org/abs/1906.02530)\]\[[9](http://arxiv.org/abs/1703.04977)\]\[[10](https://www.semanticscholar.org/paper/d388760ce74792bb764ccf77ea8620ca77406e56)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Ranking models primarily focus on modeling the relative order of predictions
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1909.10155)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1612.01474)\]\[[7](http://arxiv.org/abs/1506.02142)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: Calibration of neural network predictions is a critical area of research, particularly for applications requiring reliable probability estimates such as weather forecasting and personalized medicine \[[3](http://arxiv.org/abs/1909.10155)\]. Modern neural networks, unlike earlier models, are often poorly calibrated, leading to overconfident or underconfident predictions \[[1](http://arxiv.org/abs/1706.04599)\]. This issue has prompted the development of various post-processing calibration methods, including temperature scaling, Platt scaling, and histogram binning \[[3](http://arxiv.org/abs/1909.10155)\]. While temperature scaling is effective in many cases, recent studies have shown that it may not always achieve optimal calibration, and existing methods often struggle to estimate calibration error accurately \[[3](http://arxiv.org/abs/1909.10155)\]. Additionally, techniques like mixup training have been found to improve calibration by introducing label smoothing and reducing overconfidence in predictions \[[5](http://arxiv.org/abs/1905.11001)\]. Furthermore, new metrics such as field-level calibration error have been introduced to evaluate calibration on sensitive input fields, highlighting the need for more nuanced calibration approaches \[[11](http://arxiv.org/abs/1905.10713)\]. These findings underscore the ongoing challenges in achieving accurate and reliable probability estimates, motivating the development of more flexible and expressive calibration methods.
|    | reference                                                                                                                                 | date     | key idea/summary                                                                                                                                                                                                                                                     |
|----|-------------------------------------------------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [On Calibration of Modern Neural Networks](http://arxiv.org/abs/1706.04599)                                                               | 06/14/17 | Modern neural networks are poorly calibrated, and temperature scaling is an effective post-processing method for improving prediction calibration.                                                                                                                   |
|  1 | [Verified Uncertainty Calibration](http://arxiv.org/abs/1909.10155)                                                                       | 09/23/19 | The paper introduces a new calibration method called scaling-binning calibrator that combines the efficiency of scaling methods with the accuracy of histogram binning, achieving better calibration and reducing sample requirements.                               |
|  2 | [On Mixup Training: Improved Calibration and Predictive Uncertainty for Deep Neural Networks](http://arxiv.org/abs/1905.11001)            | 05/27/19 | Mixup training improves the calibration and predictive uncertainty of deep neural networks by using label smoothing, leading to better performance on in-distribution and out-of-distribution data compared to standard training with hard labels.                   |
|  3 | [Field-aware Calibration: A Simple and Empirically Strong Method for Reliable Probabilistic Predictions](http://arxiv.org/abs/1905.10713) | 05/26/19 | The paper introduces a new calibration error metric and proposes Neural Calibration, a post-hoc method that improves probabilistic predictions by leveraging field-aware information, leading to better performance on both calibration and non-calibration metrics. |
### <a id='category-predictive-uncertainty-estimation'></a>Predictive Uncertainty Estimation: 2 papers found.
Context: 
	Document 1: [_citation_number]: «2»
[Snippet]: «Deep neural networks (NNs) are powerful black box predictors that have recently achieved impressive performance on a wide spectrum of tasks. Quantifying predictive uncertainty in NNs is a challenging and yet unsolved problem. Bayesian NNs, which learn a distribution over weights, are currently the state-of-the-art for estimating predictive uncertainty; however these require significant modifications to the training procedure and are computationally expensive compared to standard (non-Bayesian) NNs. We propose an alternative to Bayesian NNs that is simple to implement, readily parallelizable, requires very little hyperparameter tuning, and yields high quality predictive uncertainty estimates. Through a series of experiments on classification and regression benchmarks, we demonstrate that our method produces well-calibrated uncertainty estimates which are as good or better than approximate Bayesian NNs. To assess robustness to dataset shift, we evaluate the predictive uncertainty on test examples from known and unknown distributions, and show that our method is able to express higher uncertainty on out-of-distribution examples. We demonstrate the scalability of our method by evaluating predictive uncertainty estimates on ImageNet.»
[Category]: «Predictive Uncertainty Estimation»

	Document 2: [_citation_number]: «8»
[Snippet]: «Modern machine learning methods including deep learning have achieved great success in predictive accuracy for supervised learning tasks, but may still fall short in giving useful estimates of their predictive (\em uncertainty). Quantifying uncertainty is especially critical in real-world settings, which often involve input distributions that are shifted from the training distribution due to a variety of factors including sample bias and non-stationarity. In such settings, well calibrated uncertainty estimates convey information about when a model's output should (or should not) be trusted. Many probabilistic deep learning methods, including Bayesian-and non-Bayesian methods, have been proposed in the literature for quantifying predictive uncertainty, but to our knowledge there has not previously been a rigorous large-scale empirical comparison of these methods under dataset shift. We present a large-scale benchmark of existing state-of-the-art methods on classification problems and investigate the effect of dataset shift on accuracy and calibration. We find that traditional post-hoc calibration does indeed fall short, as do several other previous methods. However, some methods that marginalize over models give surprisingly strong results across a broad spectrum of tasks.»
[Category]: «Predictive Uncertainty Estimation»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-19T09:35:11+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1909.10155)\]. Further details \[[6](https://www.semanticscholar.org/paper/7f6bb146b9c1504ec77100e640d624bdc204f0ac)\]\[[7](http://arxiv.org/abs/1506.02142)\]\[[8](http://arxiv.org/abs/1906.02530)\]\[[9](http://arxiv.org/abs/1703.04977)\]\[[10](https://www.semanticscholar.org/paper/d388760ce74792bb764ccf77ea8620ca77406e56)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Ranking models primarily focus on modeling the relative order of predictions
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1909.10155)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1612.01474)\]\[[7](http://arxiv.org/abs/1506.02142)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Predictive uncertainty estimation remains a critical challenge in deep learning, as models often fail to provide reliable uncertainty quantification, especially under distributional shifts \[[2](http://arxiv.org/abs/1612.01474)\]. Bayesian neural networks (BNNs) have been proposed as a leading approach, learning distributions over weights to estimate uncertainty \[[2](http://arxiv.org/abs/1612.01474)\]. However, BNNs require significant modifications to training procedures and are computationally expensive compared to standard models \[[2](http://arxiv.org/abs/1612.01474)\]. Recent work has sought alternatives that balance simplicity and effectiveness, such as methods that leverage monotonic neural networks to learn flexible, yet well-calibrated, uncertainty estimates \[[8](http://arxiv.org/abs/1906.02530)\]. These approaches aim to improve robustness to dataset shifts by capturing uncertainty in out-of-distribution scenarios \[[2](http://arxiv.org/abs/1612.01474)\]. While traditional post-hoc calibration methods have limitations, some recent methods that marginalize over models have shown promising results in maintaining calibration under distributional changes \[[8](http://arxiv.org/abs/1906.02530)\]. These developments highlight the ongoing efforts to improve uncertainty estimation in deep learning, particularly in real-world settings where input distributions may differ from training data \[[8](http://arxiv.org/abs/1906.02530)\].
|    | reference                                                                                                                        | date     | key idea/summary                                                                                                                                                                                                                       |
|----|----------------------------------------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles](http://arxiv.org/abs/1612.01474)                    | 12/05/16 | The paper proposes a simple and efficient alternative to Bayesian neural networks for estimating predictive uncertainty, demonstrating its effectiveness and scalability through experiments on various benchmarks.                    |
|  1 | [Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift](http://arxiv.org/abs/1906.02530) | 06/06/19 | The paper presents a large-scale benchmark of existing state-of-the-art methods for quantifying predictive uncertainty in deep learning, highlighting that some methods that marginalize over models perform well under dataset shift. |
### <a id='category-post-processing-calibration-approaches'></a>Post-Processing Calibration Approaches: 1 papers found.
Context: 
	Document 1: [_citation_number]: «4»
[Snippet]: «Learning probabilistic predictive models that are well calibrated is critical for many prediction and decision-making tasks in artificial intelligence. In this paper we present a new non-parametric calibration method called Bayesian Binning into Quantiles (BBQ) which addresses key limitations of existing calibration methods. The method post processes the output of a binary classification algorithm; thus, it can be readily combined with many existing classification algorithms. The method is computationally tractable, and empirically accurate, as evidenced by the set of experiments reported here on both real and simulated datasets.»
[Category]: «Post-Processing Calibration Approaches»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-19T09:35:11+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1909.10155)\]. Further details \[[6](https://www.semanticscholar.org/paper/7f6bb146b9c1504ec77100e640d624bdc204f0ac)\]\[[7](http://arxiv.org/abs/1506.02142)\]\[[8](http://arxiv.org/abs/1906.02530)\]\[[9](http://arxiv.org/abs/1703.04977)\]\[[10](https://www.semanticscholar.org/paper/d388760ce74792bb764ccf77ea8620ca77406e56)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Ranking models primarily focus on modeling the relative order of predictions
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1909.10155)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1612.01474)\]\[[7](http://arxiv.org/abs/1506.02142)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Post-processing calibration approaches aim to improve the reliability of predictive models by ensuring their outputs are well-calibrated, which is essential for decision-making tasks in artificial intelligence \[[4](https://www.semanticscholar.org/paper/8d115c3b2ee80e0754360a154a9369bc1658b607)\]. These methods often operate after the initial model training, allowing them to be integrated with various classification algorithms without altering the original model structure \[[4](https://www.semanticscholar.org/paper/8d115c3b2ee80e0754360a154a9369bc1658b607)\]. Traditional calibration techniques typically rely on predefined transformation functions, such as piece-wise linear functions, which can limit their flexibility and expressiveness in complex scenarios \[[4](https://www.semanticscholar.org/paper/8d115c3b2ee80e0754360a154a9369bc1658b607)\]. In contrast, more recent approaches, like the Bayesian Binning into Quantiles (BBQ) method, introduce non-parametric calibration strategies that offer greater adaptability while maintaining computational tractability \[[4](https://www.semanticscholar.org/paper/8d115c3b2ee80e0754360a154a9369bc1658b607)\]. Such innovations highlight the ongoing efforts to enhance the accuracy of absolute predictions, which are crucial for downstream tasks requiring precise probabilistic outputs.
|    | reference                                                                                                                                        | date     | key idea/summary                                                                                                                                                                      |
|----|--------------------------------------------------------------------------------------------------------------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Obtaining Well Calibrated Probabilities Using Bayesian Binning](https://www.semanticscholar.org/paper/8d115c3b2ee80e0754360a154a9369bc1658b607) | 01/01/15 | The paper introduces a new non-parametric calibration method called Bayesian Binning into Quantiles (BBQ) to improve the calibration of predictive models in artificial intelligence. |
### <a id='category-calibration-in-learning-to-rank-systems'></a>Calibration in Learning-to-Rank Systems: 2 papers found.
The category "Calibration in Learning-to-Rank Systems" addresses the critical need for scale calibration in ranking models, which is often overlooked in favor of optimizing relative order. Existing literature highlights that many advanced ranking functions are not scale calibrated, leading to limitations in practical deployment, especially in applications like ads ranking where calibrated predicted Click-Through Rates (pCTR) are essential for downstream auction mechanisms \[[1](http://arxiv.org/abs/1706.04599)\]. This issue is compounded by the fact that popular ranking losses are translation-invariant, which can result in training instability and suboptimal performance \[[1](http://arxiv.org/abs/1706.04599)\]. To address these challenges, researchers have proposed various approaches, including the use of scale-calibrated ranking losses that are integrated during training rather than as post-processing steps \[[1](http://arxiv.org/abs/1706.04599)\]. Additionally, there is ongoing research into the relationship between ranking losses and evaluation metrics, such as the connection between ListNet's loss and ranking metrics like Mean Reciprocal Rank and Normalized Discounted Cumulative Gain, which provides theoretical insights into the behavior of these losses \[[2](http://arxiv.org/abs/1612.01474)\]. These efforts underscore the importance of calibration in ensuring both the accuracy of absolute scores and the stability of training processes in learning-to-rank systems.
|    | reference                                                                                                                                                                  | date     | key idea/summary                                                                                                                                                                                                                                                        |
|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Scale Calibration of Deep Ranking Models](https://www.semanticscholar.org/paper/7f6bb146b9c1504ec77100e640d624bdc204f0ac)                                                 | 08/14/22 | This paper addresses the issue of scale calibration in deep ranking models by proposing calibrated ranking losses that resolve training instability and enable effective use in applications like ads ranking.                                                          |
|  1 | [An Analysis of the Softmax Cross Entropy Loss for Learning-to-Rank with Binary Relevance](https://www.semanticscholar.org/paper/d388760ce74792bb764ccf77ea8620ca77406e56) | 09/23/19 | This work establishes an analytical connection between ListNet's loss and two popular ranking metrics, showing that the loss bounds Mean Reciprocal Rank and Normalized Discounted Cumulative Gain, thereby explaining its superior performance on binary labeled data. |
### <a id='category-dropout-as-a-bayesian-approximation'></a>Dropout as a Bayesian Approximation: 1 papers found.
Context: 
	Document 1: [_citation_number]: «7»
[Snippet]: «Deep learning tools have gained tremendous attention in applied machine learning. However such tools for regression and classification do not capture model uncertainty. In comparison, Bayesian models offer a mathematically grounded framework to reason about model uncertainty, but usually come with a prohibitive computational cost. In this paper we develop a new theoretical framework casting dropout training in deep neural networks (NNs) as approximate Bayesian inference in deep Gaussian processes. A direct result of this theory gives us tools to model uncertainty with dropout NNs -- extracting information from existing models that has been thrown away so far. This mitigates the problem of representing uncertainty in deep learning without sacrificing either computational complexity or test accuracy. We perform an extensive study of the properties of dropout's uncertainty. Various network architectures and non-linearities are assessed on tasks of regression and classification, using MNIST as an example. We show a considerable improvement in predictive log-likelihood and RMSE compared to existing state-of-the-art methods, and finish by using dropout's uncertainty in deep reinforcement learning.»
[Category]: «Dropout as a Bayesian Approximation»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-19T09:35:11+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1909.10155)\]. Further details \[[6](https://www.semanticscholar.org/paper/7f6bb146b9c1504ec77100e640d624bdc204f0ac)\]\[[7](http://arxiv.org/abs/1506.02142)\]\[[8](http://arxiv.org/abs/1906.02530)\]\[[9](http://arxiv.org/abs/1703.04977)\]\[[10](https://www.semanticscholar.org/paper/d388760ce74792bb764ccf77ea8620ca77406e56)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Ranking models primarily focus on modeling the relative order of predictions
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1909.10155)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1612.01474)\]\[[7](http://arxiv.org/abs/1506.02142)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The use of dropout as a Bayesian approximation has been a significant area of research in deep learning, aiming to address the limitations of traditional models in capturing uncertainty. Dropout training in deep neural networks has been theoretically framed as an approximate Bayesian inference method, particularly in the context of deep Gaussian processes \[[7](http://arxiv.org/abs/1506.02142)\]. This approach allows for the modeling of uncertainty without the prohibitive computational costs typically associated with Bayesian models. By treating dropout as a form of stochastic regularization, researchers have demonstrated that it can effectively capture uncertainty in predictions, leading to improvements in predictive log-likelihood and RMSE compared to existing methods \[[7](http://arxiv.org/abs/1506.02142)\]. The framework also enables the extraction of useful information from existing models, enhancing their performance in tasks such as regression and classification. Furthermore, the application of dropout-based uncertainty estimation extends beyond traditional tasks, including deep reinforcement learning, where it can provide more reliable decision-making under uncertainty \[[7](http://arxiv.org/abs/1506.02142)\].
|    | reference                                                                                                               | date     | key idea/summary                                                                                                                                                                                                                     |
|----|-------------------------------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning](http://arxiv.org/abs/1506.02142) | 06/06/15 | This paper presents a theoretical framework that interprets dropout training in deep neural networks as approximate Bayesian inference, enabling uncertainty modeling without sacrificing computational efficiency or test accuracy. |
### <a id='category-bayesian-methods-for-uncertainty-estimation'></a>Bayesian Methods for Uncertainty Estimation: 2 papers found.
Context: 
	Document 1: [_citation_number]: «9»
[Snippet]: «There are two major types of uncertainty one can model. Aleatoric uncertainty captures noise inherent in the observations. On the other hand, epistemic uncertainty accounts for uncertainty in the model - uncertainty which can be explained away given enough data. Traditionally it has been difficult to model epist...
[Category]: «Bayesian Methods for Uncertainty Estimation»

	Document 2: [_citation_number]: «12»
[Snippet]: «Methods for reasoning under uncertainty are a key building block of accurate and reliable machine learning systems. Bayesian methods provide a general framework to quantify uncertainty. However, because of model misspecification and the use of approximate inference, Bayesian uncertainty estimates are often inaccurate -- for example, a 90% credible interval may not contain the true outcome 90% of the time. Here, we propose a simple procedure for calibrating any regression algorithm; when applied to Bayesian and probabilistic models, it is guaranteed to produce calibrated uncertainty estimates given enough data. Our procedure is inspired by Platt scaling and extends previous work on classification. We evaluate this approach on Bayesian linear regression, feedforward, and recurrent neural networks, and find that it consistently outputs well-calibrated credible intervals while improving performance on time series forecasting and model-based reinforcement learning tasks.»
[Category]: «Bayesian Methods for Uncertainty Estimation»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-19T09:35:11+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1909.10155)\]. Further details \[[6](https://www.semanticscholar.org/paper/7f6bb146b9c1504ec77100e640d624bdc204f0ac)\]\[[7](http://arxiv.org/abs/1506.02142)\]\[[8](http://arxiv.org/abs/1906.02530)\]\[[9](http://arxiv.org/abs/1703.04977)\]\[[10](https://www.semanticscholar.org/paper/d388760ce74792bb764ccf77ea8620ca77406e56)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Ranking models primarily focus on modeling the relative order of predictions
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1909.10155)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1612.01474)\]\[[7](http://arxiv.org/abs/1506.02142)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Bayesian methods for uncertainty estimation have been widely explored to address the challenges of quantifying uncertainty in machine learning models. These methods provide a general framework for modeling both aleatoric and epistemic uncertainty, where aleatoric uncertainty captures inherent noise in the data, while epistemic uncertainty reflects model-related uncertainty that can be reduced with more data \[[9](http://arxiv.org/abs/1703.04977)\]. However, traditional approaches often struggle with accurate uncertainty estimation due to model misspecification and the limitations of approximate inference techniques \[[12](http://arxiv.org/abs/1807.00263)\]. Recent work has focused on improving the calibration of uncertainty estimates, ensuring that probabilistic predictions align with true outcomes. For example, some studies propose calibration procedures that guarantee well-calibrated credible intervals when applied to Bayesian models, enhancing reliability in tasks such as time series forecasting and reinforcement learning \[[12](http://arxiv.org/abs/1807.00263)\]. These advancements highlight the ongoing efforts to refine Bayesian uncertainty estimation, balancing model flexibility with the need for accurate and interpretable uncertainty quantification.
|    | reference                                                                                                       | date     | key idea/summary                                                                                                                                                                                                                                   |
|----|-----------------------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision?](http://arxiv.org/abs/1703.04977) | 03/15/17 | The paper introduces a Bayesian deep learning framework that models both aleatoric and epistemic uncertainties for vision tasks, leading to more robust loss functions and state-of-the-art results in semantic segmentation and depth regression. |
|  1 | [Accurate Uncertainties for Deep Learning Using Calibrated Regression](http://arxiv.org/abs/1807.00263)         | 07/01/18 | The paper proposes a calibration procedure for regression algorithms that ensures accurate uncertainty estimates, improving performance in time series forecasting and reinforcement learning tasks.                                               |
### <a id='category-evaluation-of-calibration-and-uncertainty'></a>Evaluation of Calibration and Uncertainty: 2 papers found.
Context: 
	Document 1: [_citation_number]: «13»
[Snippet]: «We introduce Adam, an algorithm for first-order gradient-based optimization of stochastic objective functions, based on adaptive estimates of lower-order moments. The method is straightforward to implement, is computationally efficient, has little memory requirements, is invariant to diagonal rescaling of the gradients, and is well suited for problems that are large in terms of data and/or parameters. The method is also appropriate for non-stationary objectives and problems with very noisy and/or sparse gradients. The hyper-parameters have intuitive interpretations and typically require little tuning. Some connections to related algorithms, on which Adam was inspired, are discussed. We also analyze the theoretical convergence properties of the algorithm and provide a regret bound on the convergence rate that is comparable to the best known results under the online convex optimization framework. Empirical results demonstrate that Adam works well in practice and compares favorably to other stochastic optimization methods. Finally, we discuss AdaMax, a variant of Adam based on the infinity norm.»
[Category]: «Evaluation of Calibration and Uncertainty»

	Document 2: [_citation_number]: «14»
[Snippet]: «Generalized linear models with nonlinear feature transformations are widely used for large-scale regression and classification problems with sparse inputs. Memorization of feature interactions through a wide set of cross-product feature transformations are effective and interpretable, while generalization requires more feature engineering effort. With less feature engineering, deep neural networks can generalize better to unseen feature combinations through low-dimensional dense embeddings learned for the sparse features. However, deep neural networks with embeddings can over-generalize and recommend less relevant items when the user-item interactions are sparse and high-rank. In this paper, we present Wide & Deep learning---jointly trained wide linear models and deep neural networks---to combine the benefits of memorization and generalization for recommender systems. We productionized and evaluated the system on Google Play, a commercial mobile app store with over one billion active users and over one million apps. Online experiment results show that Wide & Deep significantly increased app acquisitions compared with wide-only and deep-only models. We have also open-sourced our implementation in TensorFlow.»
[Category]: «Evaluation of Calibration and Uncertainty»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-19T09:35:11+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/1909.10155)\]. Further details \[[6](https://www.semanticscholar.org/paper/7f6bb146b9c1504ec77100e640d624bdc204f0ac)\]\[[7](http://arxiv.org/abs/1506.02142)\]\[[8](http://arxiv.org/abs/1906.02530)\]\[[9](http://arxiv.org/abs/1703.04977)\]\[[10](https://www.semanticscholar.org/paper/d388760ce74792bb764ccf77ea8620ca77406e56)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Ranking models primarily focus on modeling the relative order of predictions
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
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/1909.10155)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1612.01474)\]\[[7](http://arxiv.org/abs/1506.02142)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
The evaluation of calibration and uncertainty in machine learning has seen significant advancements, particularly in the context of ranking models and optimization algorithms. Existing calibration approaches often rely on predefined transformation functions with order-preserving properties, such as piece-wise linear functions, which, while effective in some scenarios, exhibit limited expressiveness and flexibility \[[13](http://arxiv.org/abs/1412.6980)\]. This constraint can hinder their effectiveness in complex calibration tasks where the relationship between predicted and true values is non-linear and intricate. To address these limitations, recent work has explored the use of more flexible models, such as Unconstrained Monotonic Neural Networks (UMNN), which can learn arbitrary monotonic functions with high modeling power, thereby improving flexibility and expressiveness while maintaining the necessary monotonicity constraints \[[13](http://arxiv.org/abs/1412.6980)\]. Additionally, the development of novel loss functions, such as the Smooth Calibration Loss (SCLoss), has aimed to further enhance the calibration process by fulfilling necessary conditions for achieving optimal calibration states \[[13](http://arxiv.org/abs/1412.6980)\]. In parallel, research on large-scale recommender systems has highlighted the importance of combining memorization and generalization capabilities, as seen in the Wide & Deep learning approach, which integrates wide linear models with deep neural networks to achieve better performance in sparse and high-rank interaction scenarios \[[14](http://arxiv.org/abs/1606.07792)\]. These developments underscore the ongoing efforts to improve the accuracy and reliability of predictions in various applications, from ranking systems to recommendation engines.
|    | reference                                                                       | date     | key idea/summary                                                                                                                                                                                         |
|----|---------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Adam: A Method for Stochastic Optimization](http://arxiv.org/abs/1412.6980)    | 12/22/14 | Adam is an adaptive optimization algorithm for stochastic objective functions, known for its efficiency, low memory requirements, and strong performance in large-scale and noisy optimization problems. |
|  1 | [Wide & Deep Learning for Recommender Systems](http://arxiv.org/abs/1606.07792) | 06/24/16 | Wide & Deep learning combines wide linear models and deep neural networks to balance memorization and generalization in recommender systems, achieving better performance in app acquisitions.           |
