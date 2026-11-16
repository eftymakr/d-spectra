## Related Works

The field of cloud-native computing and container orchestration has seen significant advancements, particularly in the areas of cost optimization, resource management, and network efficiency. Early research focused on the integration of containerization technologies with orchestration systems like Kubernetes, highlighting the challenges of scheduling and resource allocation \[[Saurabh Deochake' 2024-12-22](http://arxiv.org/abs/2501.14753v1)\]. The introduction of FinOps as a discipline has further emphasized the need for financial and operational considerations in cloud environments . This section reviews relevant works that contribute to the understanding of network costs in Kubernetes clusters and the broader FinOps domain.

Several studies have explored the performance and efficiency of Kubernetes in managing containerized workloads. KubeAdaptor was introduced as a framework to align workflow scheduling with Kubernetes, ensuring consistency in task execution order and improving performance metrics such as average execution time and resource usage \[[Saurabh Deochake' 2024-12-22](http://arxiv.org/abs/2501.14753v1)\]. This work laid the foundation for optimizing containerized workflows on Kubernetes, which is critical for cost-effective deployments.

In the realm of Kubernetes security, researchers have identified vulnerabilities and proposed mitigation strategies, such as role-based access control and network policies \[[Md. Shazibul Islam Shamim' 2020-06-27](http://arxiv.org/abs/2006.15275v1)\]. While security is essential, it is distinct from the focus on cost and network efficiency discussed in this paper. However, these security practices are integral to the overall management of cloud-native applications, including networked containerized systems.

The concept of FinOps emerged as a response to the growing complexity of managing cloud costs. This discipline combines financial management with cloud operations to optimize costs and improve resource efficiency . Prior research has explored system-level optimization strategies, but the analysis of network costs in Kubernetes clusters remains underexplored . This paper addresses this gap by investigating the network usage and cost implications of containerized applications running on Kubernetes clusters.

Recent studies have also focused on optimizing cloud infrastructure costs through various techniques, such as model quantization, GPU instance selection, and inference optimization . These strategies are relevant to the broader context of cost optimization in cloud environments but are not directly applicable to the specific focus on network costs in Kubernetes clusters.

The development of tools like ABACUS, an automated budget analysis and cloud usage surveillance system, has contributed to the FinOps discipline by providing mechanisms for cost tracking and enforcement . These tools are essential for achieving the financial and operational goals of managing network costs in cloud-native environments.

In addition, the paper by  provides a comprehensive review of strategies for optimizing cloud and AI infrastructure costs, including techniques such as model quantization and GPU instance selection. These approaches are relevant to the broader context of cost optimization in cloud environments but are not directly applicable to the specific focus on network costs in Kubernetes clusters.

The work by  introduces ABACUS, a FinOps service for cloud cost optimization, which provides mechanisms for setting budgets, enforcing them through blocking new deployments, and alerting appropriate teams if spending breaches a budget threshold. These features are essential for achieving the financial and operational goals of managing network costs in cloud-native environments.

In summary, while existing works have made significant contributions to the fields of container orchestration, Kubernetes security, and FinOps, the specific focus on network costs in Kubernetes clusters remains a critical area for further research. This paper addresses this gap by providing actionable insights into network cost optimization for containerized applications in cloud-native environments.

### References

1. \[[Saurabh Deochake' 2024-12-22](http://arxiv.org/abs/2501.14753v1)\] KubeAdaptor: A Docking Framework for Workflow Containerization on Kubernetes  
2. \[[Md. Shazibul Islam Shamim' 2020-06-27](http://arxiv.org/abs/2006.15275v1)\] XI Commandments of Kubernetes Security: A Systematization of Knowledge Related to Kubernetes Security Practices  
3.  Cloud and AI Infrastructure Cost Optimization: A Comprehensive Review of Strategies and Case Studies  
4.  ABACUS: A FinOps Service for Cloud Cost Optimization
