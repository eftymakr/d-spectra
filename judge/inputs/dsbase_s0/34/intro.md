## Related Works

Fund allocation in financial contexts has been extensively studied, with a growing emphasis on integrating forecasting with optimization to mitigate the limitations of naive approaches. Traditional methods such as prediction-only or predict-then-optimize (PnO) often suffer from goal mismatch, where the forecasting and optimization objectives are not aligned \[[Harshavardhan Kamarthi' 2024-07-02](http://arxiv.org/abs/2407.02641v1)\]. This issue is further exacerbated by the inherent uncertainty introduced by state-of-the-art time series forecasting models \[[Adèle Gouttes' 2021-07-08](http://arxiv.org/abs/2107.03743v1)\]. To address these challenges, recent works have explored hybrid frameworks that integrate forecasting and allocation in a unified manner.

A notable approach is the Predict-then-Optimize (PnO) framework, which decouples forecasting from optimization, often leading to suboptimal results due to the misalignment of objectives \[[Peru Muniain' 2018-10-19](http://arxiv.org/abs/1810.08418v2)\]. To improve this, some studies have proposed end-to-end training strategies that align the forecasting and optimization objectives \[[Chiyu Zhang' 2023-06-21](http://arxiv.org/abs/2306.12086v2)\]. These methods typically involve training a single model to jointly learn both tasks, which can lead to better performance compared to separate models \[[Dimitri O. Ledenyov' 2012-11-17](http://arxiv.org/abs/1211.4108v1)\]. However, these approaches often assume specific forecasting models, limiting their adaptability \[[Md Khairul Islam' 2024-10-24](http://arxiv.org/abs/2410.19025v1)\].

Another line of research focuses on uncertainty calibration in forecasting models, which is crucial for reliable decision-making in financial contexts \[[Yangyang Yu' 2024-07-09](http://arxiv.org/abs/2407.06567v3)\]. Techniques such as Monte Carlo dropout and Bayesian neural networks have been used to estimate uncertainty in forecasts \[[David Criens' 2018-09-25](http://arxiv.org/abs/1809.09588v5)\]. However, these methods may not be suitable for all forecasting models and can be computationally intensive \[[Minhao Liu' 2021-06-17](http://arxiv.org/abs/2106.09305v3)\]. More recently, methods like conformal prediction have been introduced to provide valid uncertainty quantification for time series forecasts \[[Young-Chae Hong' 2025-02-25](http://arxiv.org/abs/2502.18410v2)\].

In the context of financial applications, several studies have explored the use of deep learning models for time series forecasting and allocation. For instance, the work by \[[Yukun Zhang' 2019-12-16](http://arxiv.org/abs/1912.07211v1)\] introduces a framework that combines deep learning with optimization to handle the uncertainty in financial forecasts. Similarly, \[[Ziad Hatab' 2022-06-21](http://arxiv.org/abs/2206.10209v2)\] proposes a method that integrates forecasting and allocation by using a unified loss function that encourages both accurate forecasts and optimal allocation. These approaches demonstrate the potential of integrating forecasting and allocation in financial contexts.

Additionally, the use of large language models (LLMs) for financial time series analysis has gained traction, with studies showing their potential to capture complex temporal dependencies and provide accurate forecasts \[[Florian Huber' 2024-10-21](http://arxiv.org/abs/2410.16214v1)\]. However, the integration of LLMs into financial allocation frameworks remains an open research question \[[Luca Butera' 2024-10-18](http://arxiv.org/abs/2410.14630v2)\].

In summary, while there are several approaches to integrating forecasting and allocation in financial contexts, there is a need for more robust and adaptable frameworks that can handle the uncertainty inherent in time series forecasting. The proposed RTS-PnO framework addresses these challenges by providing a risk-aware approach that is agnostic to the underlying forecasting model \[[Jean Lee' 2023-01-23](http://arxiv.org/abs/2301.09279v2)\].

### References

1. \[[Harshavardhan Kamarthi' 2024-07-02](http://arxiv.org/abs/2407.02641v1)\] Document 1  
2. \[[Adèle Gouttes' 2021-07-08](http://arxiv.org/abs/2107.03743v1)\] Document 2  
3. \[[Peru Muniain' 2018-10-19](http://arxiv.org/abs/1810.08418v2)\] Document 3  
4. \[[Chiyu Zhang' 2023-06-21](http://arxiv.org/abs/2306.12086v2)\] Document 4  
5. \[[Dimitri O. Ledenyov' 2012-11-17](http://arxiv.org/abs/1211.4108v1)\] Document 5  
6. \[[Md Khairul Islam' 2024-10-24](http://arxiv.org/abs/2410.19025v1)\] Document 6  
7. \[[Yangyang Yu' 2024-07-09](http://arxiv.org/abs/2407.06567v3)\] Document 7  
8. \[[David Criens' 2018-09-25](http://arxiv.org/abs/1809.09588v5)\] Document 8  
9. \[[Minhao Liu' 2021-06-17](http://arxiv.org/abs/2106.09305v3)\] Document 9  
10. \[[Young-Chae Hong' 2025-02-25](http://arxiv.org/abs/2502.18410v2)\] Document 10  
11. \[[Yukun Zhang' 2019-12-16](http://arxiv.org/abs/1912.07211v1)\] Document 11  
12. \[[Ziad Hatab' 2022-06-21](http://arxiv.org/abs/2206.10209v2)\] Document 12  
13. \[[Florian Huber' 2024-10-21](http://arxiv.org/abs/2410.16214v1)\] Document 13  
14. \[[Luca Butera' 2024-10-18](http://arxiv.org/abs/2410.14630v2)\] Document 14  
15. \[[Jean Lee' 2023-01-23](http://arxiv.org/abs/2301.09279v2)\] Document 15
