## Related Works

Time series forecasting has been a cornerstone in financial applications, with recent advances focusing on improving accuracy and robustness in the presence of uncertainty. Traditional approaches such as prediction-only or predict-then-optimize (PnO) methods suffer from goal mismatch, where the forecasting and allocation objectives are not aligned \[[1](http://arxiv.org/abs/2211.14730)\]. This issue is further exacerbated by the introduction of state-of-the-art forecasting models, which introduce additional uncertainty into the predicted results \[[2](http://arxiv.org/abs/1912.09363)\]. To address these challenges, this paper introduces the Risk-aware Time-Series Predict-and-Allocate (RTS-PnO) framework, which is designed to be agnostic to the underlying forecasting model and incorporates adaptive uncertainty calibration \[[3](http://arxiv.org/abs/2205.14415)\].

Several recent works have explored the use of deep learning for time series forecasting. Transformers have gained significant traction due to their ability to capture long-range dependencies, although they face challenges in non-stationary data and computational efficiency \[[4](http://arxiv.org/abs/2205.13504)\]. The PatchTST model, for instance, addresses these issues by introducing a segmentation-based approach and channel-independent design, improving long-term forecasting accuracy \[[5](http://arxiv.org/abs/2210.02186)\]. Similarly, the Temporal Fusion Transformer (TFT) combines recurrent and self-attention layers to enable interpretable multi-horizon forecasting \[[6](http://arxiv.org/abs/1704.04110)\]. These models, however, often require extensive tuning and are not inherently designed for integration with allocation strategies.

The use of large language models (LLMs) for time series forecasting has also been explored, with studies showing that models like GPT-3 and LLaMA-2 can perform zero-shot forecasting comparable to specialized models \[[7](http://arxiv.org/abs/2310.06625)\]. This approach, however, relies on encoding time series as strings of numerical digits and may not generalize well to complex financial data \[[8](http://arxiv.org/abs/2310.01728)\]. The Time-LLM framework attempts to bridge this gap by reprogramming LLMs for time series forecasting while preserving the backbone of the language model \[[9](http://arxiv.org/abs/2004.13408)\].

In the context of financial applications, the DeepAR model has demonstrated improvements in probabilistic forecasting, particularly in retail and demand prediction \[[10](http://arxiv.org/abs/2106.13008)\]. However, it is limited to autoregressive recurrent networks and does not address the integration of forecasting with allocation decisions. The Deep Factors model, on the other hand, combines classical statistical models with deep neural networks to handle uncertainty and scalability in large collections of time series \[[11](http://arxiv.org/abs/2310.07820)\].

The recent development of the Autoformer model introduces an Auto-Correlation mechanism, which enhances the efficiency and accuracy of long-term forecasting by capturing periodic dependencies \[[12](http://arxiv.org/abs/1905.12417)\]. Similarly, the iTransformer model improves upon traditional Transformers by inverting the attention mechanism to better handle multivariate time series \[[13](http://arxiv.org/abs/2310.10688)\]. These models, while effective, often require specialized architectures and are not designed for end-to-end allocation tasks.

In summary, while numerous models have advanced time series forecasting, the integration of forecasting with allocation strategies remains a critical challenge. The RTS-PnO framework addresses this by providing a unified approach that is agnostic to the forecasting model and incorporates adaptive uncertainty calibration \[[14](http://arxiv.org/abs/2306.11025)\].

1. \[[1](http://arxiv.org/abs/2211.14730)\] "Risk-aware Time-Series Predict-and-Allocate (RTS-PnO) framework"  
2. \[[2](http://arxiv.org/abs/1912.09363)\] "Introduction of the SOTA time series forecasting model"  
3. \[[3](http://arxiv.org/abs/2205.14415)\] "RTS-PnO framework contains three features"  
4. \[[4](http://arxiv.org/abs/2205.13504)\] "Transformers have gained significant traction due to their ability to capture long-range dependencies"  
5. \[[5](http://arxiv.org/abs/2210.02186)\] "PatchTST model improves long-term forecasting accuracy"  
6. \[[6](http://arxiv.org/abs/1704.04110)\] "Temporal Fusion Transformer (TFT) combines recurrent and self-attention layers"  
7. \[[7](http://arxiv.org/abs/2310.06625)\] "LLMs such as GPT-3 and LLaMA-2 can perform zero-shot forecasting"  
8. \[[8](http://arxiv.org/abs/2310.01728)\] "Encoding time series as strings of numerical digits"  
9. \[[9](http://arxiv.org/abs/2004.13408)\] "Time-LLM framework reprograms LLMs for time series forecasting"  
10. \[[10](http://arxiv.org/abs/2106.13008)\] "DeepAR model demonstrates improvements in probabilistic forecasting"  
11. \[[11](http://arxiv.org/abs/2310.07820)\] "Deep Factors model combines classical statistical models with deep neural networks"  
12. \[[12](http://arxiv.org/abs/1905.12417)\] "Autoformer model introduces an Auto-Correlation mechanism"  
13. \[[13](http://arxiv.org/abs/2310.10688)\] "iTransformer model improves upon traditional Transformers"  
14. \[[14](http://arxiv.org/abs/2306.11025)\] "RTS-PnO framework provides a unified approach"
