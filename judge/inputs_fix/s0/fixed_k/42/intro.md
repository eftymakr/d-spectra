## Related Works

The growing adoption of cloud-native applications has led to increased reliance on managed cloud services and containerization technologies such as Kubernetes \[[1](http://arxiv.org/abs/2501.14753)\]. These technologies enable rapid deployment and scalability, but they also introduce new challenges in cost management, particularly in the context of network usage and expenditures \[[2](http://arxiv.org/abs/1901.04946)\]. FinOps, an emerging discipline that integrates financial management with cloud operations, has gained traction as a framework for optimizing cloud costs \[[3](http://arxiv.org/abs/2104.02423)\]. However, prior research has primarily focused on system-level optimization strategies for resource efficiency, with limited attention given to network cost analysis in Kubernetes clusters \[[4](http://arxiv.org/abs/2307.12479)\].

Several studies have explored cost optimization techniques for cloud environments. For instance, ABACUS presents a FinOps solution that sets budgets, enforces them through blocking new deployments, and alerts teams when spending thresholds are breached \[[5](http://arxiv.org/abs/2405.12311)\]. Similarly, SpotKube leverages Kubernetes and spot pricing to minimize deployment costs while maintaining performance \[[6](http://arxiv.org/abs/2006.15275)\]. These approaches highlight the importance of cost-aware strategies in cloud-native environments. However, they do not directly address the specific challenges of network cost optimization in Kubernetes clusters \[[7](http://arxiv.org/abs/2207.01222)\].

Kubernetes, as a leading container orchestration platform, has been extensively studied for its capabilities in managing microservices and ensuring availability \[[8](http://arxiv.org/abs/2401.07417)\]. While Kubernetes provides robust mechanisms for deploying and maintaining containerized applications, its performance and availability can be impacted by factors such as etcd scalability and write request latency \[[9](http://arxiv.org/abs/2301.01178)\]. These limitations have prompted research into alternative consistency models to improve performance at the edge \[[10](http://arxiv.org/abs/1507.05492)\]. Additionally, the integration of Kubernetes with advanced networking technologies, such as Segment Routing over IPv6 (SRv6), has been explored to enhance large-scale and distributed network scenarios \[[11](http://arxiv.org/abs/2502.02842)\].

In the context of network cost optimization, the paper under review contributes by investigating the network usage and cost implications of containerized applications running on Kubernetes clusters. This work builds on existing research that has examined the broader challenges of cloud cost management \[[12](http://arxiv.org/abs/2412.15778)\]. For example, the paper "Cloud and AI Infrastructure Cost Optimization" highlights the significant portion of technical budgets allocated to GPU compute for AI/ML workloads and explores techniques such as model quantization and GPU instance selection to reduce costs \[[13](http://arxiv.org/abs/1207.2799)\]. These strategies, while effective for AI/ML workloads, do not directly address the network cost implications of Kubernetes-based deployments \[[14](http://arxiv.org/abs/2105.01939)\].

Moreover, the paper aligns with broader efforts to improve the efficiency and cost-effectiveness of cloud-native applications. For instance, the study on 5G network slice isolation emphasizes the importance of resource allocation mechanisms to ensure service isolation and performance \[[15](http://arxiv.org/abs/2501.05323)\]. Similarly, the research on distributed learning and inference systems underscores the need for robust network infrastructure to support decentralized AI operations \[[16](http://arxiv.org/abs/2002.10992)\]. These studies collectively highlight the growing interest in optimizing both computational and network resources in cloud-native environments.

In summary, the current paper extends the body of knowledge by focusing specifically on network cost optimization in Kubernetes clusters, addressing a gap in the existing literature. This work contributes to the FinOps discipline by providing actionable insights into managing network expenditures in cloud-native environments.

References:  
\[[1](http://arxiv.org/abs/2501.14753)\] http://arxiv.org/abs/2501.14753  
\[[2](http://arxiv.org/abs/1901.04946)\] http://arxiv.org/abs/1901.04946  
\[[3](http://arxiv.org/abs/2104.02423)\] http://arxiv.org/abs/2501.14753  
\[[4](http://arxiv.org/abs/2307.12479)\] http://arxiv.org/abs/2501.14753  
\[[5](http://arxiv.org/abs/2405.12311)\] http://arxiv.org/abs/2501.14753  
\[[6](http://arxiv.org/abs/2006.15275)\] http://arxiv.org/abs/2405.12311  
\[[7](http://arxiv.org/abs/2207.01222)\] http://arxiv.org/abs/2405.12311  
\[[8](http://arxiv.org/abs/2401.07417)\] http://arxiv.org/abs/1901.04946  
\[[9](http://arxiv.org/abs/2301.01178)\] http://arxiv.org/abs/2104.02423  
\[[10](http://arxiv.org/abs/1507.05492)\] http://arxiv.org/abs/2104.02423  
\[[11](http://arxiv.org/abs/2502.02842)\] http://arxiv.org/abs/2301.01178  
\[[12](http://arxiv.org/abs/2412.15778)\] http://arxiv.org/abs/2307.12479  
\[[13](http://arxiv.org/abs/1207.2799)\] http://arxiv.org/abs/2307.12479  
\[[14](http://arxiv.org/abs/2105.01939)\] http://arxiv.org/abs/2307.12479  
\[[15](http://arxiv.org/abs/2501.05323)\] http://arxiv.org/abs/2502.02842  
\[[16](http://arxiv.org/abs/2002.10992)\] http://arxiv.org/abs/2501.05323
