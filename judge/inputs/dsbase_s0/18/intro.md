## Related Works

Anomaly detection has become a critical component in modern manufacturing and industrial settings, where maintaining quality control is essential. Traditional approaches often rely on supervised learning, where models are trained on labeled normal and abnormal data to detect deviations from expected patterns \[[Joao P C Bertoldo' 2023-07-12](http://arxiv.org/abs/2307.06052v1)\]. However, these methods typically require large amounts of labeled data and may not generalize well to unseen anomalies \[[Erik Rodner' 2016-10-21](http://arxiv.org/abs/1610.06761v1)\]. Moreover, many state-of-the-art models are too large and computationally intensive to be deployed on resource-constrained embedded devices, which are common in small and medium enterprises (SMEs) \[[Gregor Kasieczka' 2021-07-06](http://arxiv.org/abs/2107.02821v1)\].

Several recent works have addressed the limitations of traditional anomaly detection methods. For instance, \[[Mathis Kruse' 2024-04-10](http://arxiv.org/abs/2404.06832v1)\] proposed a multivariate Gaussian-based anomaly detection framework that fits a single distribution to feature vectors extracted from a CNN and uses Mahalanobis distance as the anomaly score. This approach is particularly useful in industrial settings where visual validation of anomalies is critical \[[Aodong Li' 2024-06-24](http://arxiv.org/abs/2406.16308v1)\]. Similarly, \[[Benyamin Ghojogh' 2019-08-25](http://arxiv.org/abs/1908.09288v1)\] introduced methods for batch anomaly detection in multivariate time series based on maximizing the Kullback-Leibler divergence between the data distribution within and outside an interval. This work emphasizes the importance of optimizing over all possible intervals to improve detection accuracy \[[Ming-Chang Lee' 2024-07-26](http://arxiv.org/abs/2407.18439v1)\].

In the context of embedded systems, \[[Parastoo Kamranfar' 2022-10-04](http://arxiv.org/abs/2210.01707v1)\] presented a lightweight anomaly detection framework that reduces model size and computational load while maintaining detection accuracy. This work is closely related to the current paper, as it shares the goal of deploying anomaly detection on resource-constrained devices. Additionally, \[[Ziyu Ye' 2021-05-16](http://arxiv.org/abs/2105.07346v1)\] proposed a memory-efficient framework for anomaly detection in time series data, which is particularly relevant for industrial IoT applications. This work emphasizes the importance of optimizing both model size and inference speed for real-time deployment \[[Chathurangi Shyalika' 2024-12-26](http://arxiv.org/abs/2412.19286v1)\].

Another important line of research focuses on the use of pre-trained models for anomaly detection. For example, \[[Jianheng Tang' 2022-05-31](http://arxiv.org/abs/2205.15508v1)\] explored the use of large language models (LLMs) for detecting anomalies in tabular data, demonstrating that pre-trained models can be zero-shot batch-level anomaly detectors. This aligns with the current work, which leverages the Mobile Segment Anything Model (MobileSAM) for image-based anomaly detection. However, unlike \[[Jianheng Tang' 2022-05-31](http://arxiv.org/abs/2205.15508v1)\], which focuses on tabular data, the current work is tailored for image-based anomaly detection in industrial settings \[[Shuhan Yuan' 2022-02-15](http://arxiv.org/abs/2202.07787v1)\].

Furthermore, \[[Yibao Sun' 2021-06-25](http://arxiv.org/abs/2106.13556v1)\] introduced a framework for detecting anomalies in vehicle trajectories, emphasizing the importance of temporal and spatial context in anomaly detection. This work is relevant to the current paper as both focus on real-time anomaly detection in dynamic environments. However, \[[Yibao Sun' 2021-06-25](http://arxiv.org/abs/2106.13556v1)\] is primarily concerned with trajectory data, whereas the current work focuses on image-based detection \[[Anindya Bhattacharjee' 2025-02-15](http://arxiv.org/abs/2502.10682v3)\].

In summary, while many recent works have made progress in anomaly detection, the challenge of deploying these models on embedded devices remains a critical issue. The current work addresses this by proposing KairosAD, a novel supervised approach that leverages the MobileSAM model to achieve high detection accuracy with reduced computational requirements .

### References

1. [Document 1]  
2. [Document 2]  
3. [Document 3]  
4. [Document 4]  
5. [Document 5]  
6. [Document 6]  
7. [Document 7]  
8. [Document 8]  
9. [Document 9]  
10. [Document 10]  
11. [Document 11]  
12. [Document 12]  
13. [Document 13]  
14. [Document 14]  
15. [Document 15]
