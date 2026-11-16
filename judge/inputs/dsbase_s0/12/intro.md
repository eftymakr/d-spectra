## Related Works

Event cameras, also known as dynamic vision sensors, capture asynchronous brightness changes at the pixel level, offering high temporal resolution and robustness to motion blur and low-light conditions \[[Andreas Ziegler' 2025-04-25](http://arxiv.org/abs/2504.18235v2)\]. However, the asynchronous nature of event data introduces challenges in processing and analysis, particularly due to the high bandwidth and computational demands \[[Andreas Ziegler' 2025-04-25](http://arxiv.org/abs/2504.18235v2)\]. Prior work has addressed these challenges through event downsampling techniques, which aim to reduce the volume of event data while preserving critical information for downstream tasks \[[Khadija Iddrisu' 2024-08-19](http://arxiv.org/abs/2408.10395v1)\]. 

Most existing approaches to event downsampling rely on fixed heuristics or threshold-based strategies, which lack adaptability to varying scene dynamics and application-specific requirements \[[Khadija Iddrisu' 2024-08-19](http://arxiv.org/abs/2408.10395v1)\]. For example, some methods use a fixed threshold to filter out events below a certain intensity change, while others apply uniform downsampling across the entire event stream \[[Kaustav Chanda' 2025-04-16](http://arxiv.org/abs/2504.12515v2)\]. These strategies are often suboptimal, as they do not account for the spatial and temporal structure of the scene \[[Lingdong Kong' 2025-03-25](http://arxiv.org/abs/2503.19916v1)\]. 

A few studies have explored adaptive event downsampling, but they typically require task-specific calibration or domain knowledge \[[Tobi Delbruck' 2021-05-02](http://arxiv.org/abs/2105.00409v1)\]. For instance, one approach uses a learned model to estimate the importance of events based on the task at hand, such as object detection or classification \[[Jalees Nehvi' 2021-04-30](http://arxiv.org/abs/2104.15139v1)\]. However, these methods often require retraining for each new task, which limits their generalizability \[[The HSF Physics Event Generator WG' 2020-04-28](http://arxiv.org/abs/2004.13687v4)\]. 

In contrast, our proposed framework, POLED, introduces a probabilistic approach to event importance modeling, enabling scene-specific adaptation without task-specific retraining \[[Adrian Paschke' 2008-06-06](http://arxiv.org/abs/0806.1100v1)\]. This is a significant advancement over prior methods, which are often limited to specific applications or require extensive manual tuning \[[Xiaoyu Huang' 2020-07-11](http://arxiv.org/abs/2007.05686v2)\]. The probabilistic modeling of event importance allows for more flexible and efficient downsampling, as it can be adapted to different scenarios without retraining \[[Yolo Yunlong Tang' 2023-06-17](http://arxiv.org/abs/2306.10354v2)\]. 

Additionally, the concept of zero-shot event downsampling, where downsampled events remain usable for models trained on the original event stream, has not been widely explored \[[R. G. Calland' 2013-11-29](http://arxiv.org/abs/1311.7579v3)\]. Our approach addresses this by designing a contour-preserving event importance probability density function (ePDF), which prioritizes structurally important events while maintaining compatibility with existing models . This is a novel contribution, as most prior work assumes that downsampled events must be adapted to the specific task or model . 

The evaluation of our method across multiple tasks—object classification, image interpolation, surface normal estimation, and object detection—demonstrates the importance of intelligent sampling in maintaining performance under event-budget constraints . This aligns with findings from other studies that emphasize the need for adaptive sampling strategies to ensure robustness in dynamic environments . 

### References

1. http://arxiv.org/abs/2408.10395v1  
2. http://arxiv.org/abs/2504.18235v2  
3. http://arxiv.org/abs/2105.00409v1  
4. http://arxiv.org/abs/2408.10395v1  
5. http://arxiv.org/abs/2504.12515v2  
6. http://arxiv.org/abs/2503.19916v1  
7. http://arxiv.org/abs/2408.10395v1  
8. http://arxiv.org/abs/2504.12515v2  
9. http://arxiv.org/abs/2408.10395v1  
10. http://arxiv.org/abs/2504.12515v2  
11. http://arxiv.org/abs/2503.19916v1  
12. http://arxiv.org/abs/2504.12515v2  
13. http://arxiv.org/abs/2408.10395v1  
14. http://arxiv.org/abs/2503.19916v1  
15. http://arxiv.org/abs/2504.12515v2
