## Related Works

Model calibration has been a focal point in improving the reliability and interpretability of machine learning predictions, particularly in ranking models where the emphasis is often on relative orderings rather than absolute accuracy. This section reviews existing approaches and highlights their limitations, particularly in the context of calibration for ranking models.

Traditional calibration methods typically employ predefined transformation functions, such as piece-wise linear functions, to adjust predictions while preserving their order \[[Antoine Wehenkel' 2019-08-14](http://arxiv.org/abs/1908.05164v3)\]. These methods are order-preserving but lack flexibility, limiting their effectiveness in complex scenarios where the relationship between predicted and true values is non-linear \[[Shunyu Zhang' 2024-06-12](http://arxiv.org/abs/2406.08010v1)\]. Furthermore, such methods may not adequately address the calibration needs of ranking models, where both relative and absolute accuracy are crucial \[[Wonbin Kweon' 2021-12-09](http://arxiv.org/abs/2112.07428v2)\].

Recent work has explored the use of neural networks for calibration, leveraging their ability to learn complex, non-linear mappings. For instance, the use of monotonic neural networks has been proposed to ensure that the calibration process maintains the relative order of predictions while allowing for greater flexibility \[[Adrien LeCoz' 2024-11-05](http://arxiv.org/abs/2411.02988v2)\]. This approach is particularly relevant to our work, as it aligns with the idea of using an Unconstrained Monotonic Neural Network (UMNN) to learn arbitrary monotonic functions \[[Maja Pavlovic' 2025-01-31](http://arxiv.org/abs/2501.19047v5)\]. The UMNN has been shown to be effective in modeling monotonic relationships, which is essential for maintaining the relative order of predictions during calibration \[[Harish G. Ramaswamy' 2014-08-12](http://arxiv.org/abs/1408.2764v2)\].

In addition to the UMNN, other neural network-based calibration methods have been explored. For example, the use of Bayesian neural networks has been proposed to provide uncertainty estimates alongside predictions, which can be useful in calibration tasks \[[Xinshao Wang' 2019-03-08](http://arxiv.org/abs/1903.03238v8)\]. However, these methods often require additional computational resources and may not be suitable for large-scale applications \[[Changwon Seo' 2021-08-19](http://arxiv.org/abs/2108.08735v2)\].

The importance of calibration in ranking models has also been highlighted in the context of recommendation systems. Several studies have shown that calibrated rankings can lead to better user engagement and satisfaction \[[Sebastián Basterrech' 2016-09-15](http://arxiv.org/abs/1609.04846v1)\]. However, these studies often focus on the calibration of individual predictions rather than the overall ranking structure \[[A. K. Ojha' 2010-02-05](http://arxiv.org/abs/1002.1164v1)\].

In the context of personalized ranking models, the need for calibrated probabilities has been emphasized, as the well-calibrated probability of an item being preferred by a user has great practical value \[[Anton Chernyavskiy' 2021-10-10](http://arxiv.org/abs/2110.15725v1)\]. While existing work shows promising results in image classification, probability calibration has not been much explored for personalized ranking \[[L. Decin' 2001-05-03](http://arxiv.org/abs/astro-ph/0105045v1)\].

Moreover, for classification models based on neural networks, the maximum predicted class probability is often used as a confidence score. This score rarely predicts well the probability of making a correct prediction and requires a post-processing calibration step \[[Thang H. L.' 2010-12-13](http://arxiv.org/abs/1012.2631v2)\]. However, many confidence calibration methods fail for problems with many classes \[[Ruby Byrne' 2020-04-17](http://arxiv.org/abs/2004.08463v2)\].

In summary, while existing calibration methods have made significant contributions, they often lack the flexibility and expressiveness needed to handle complex calibration scenarios. The use of neural networks, particularly monotonic neural networks, offers a promising direction for improving calibration in ranking models. Our approach builds on these ideas, leveraging the flexibility of the UMNN to achieve superior calibration performance \[[Hideaki Hayashi' 2019-11-14](http://arxiv.org/abs/1911.06009v1)\].

### References

1. [Document 2](http://arxiv.org/abs/2406.08010v1)  
2. [Document 1](http://arxiv.org/abs/1908.05164v3)  
3. [Document 3](http://arxiv.org/abs/2112.07428v2)  
4. [Document 5](http://arxiv.org/abs/2501.19047v5)  
5. [Document 1](http://arxiv.org/abs/1908.05164v3)  
6. [Document 1](http://arxiv.org/abs/1908.05164v3)  
7. [Document 4](http://arxiv.org/abs/2411.02988v2)  
8. [Document 4](http://arxiv.org/abs/2411.02988v2)  
9. [Document 8](http://arxiv.org/abs/2108.08735v2)  
10. [Document 9](http://arxiv.org/abs/1609.04846v1)  
11. [Document 3](http://arxiv.org/abs/2112.07428v2)  
12. [Document 3](http://arxiv.org/abs/2112.07428v2)  
13. [Document 4](http://arxiv.org/abs/2411.02988v2)  
14. [Document 4](http://arxiv.org/abs/2411.02988v2)  
15. [Document 1](http://arxiv.org/abs/1908.05164v3)
