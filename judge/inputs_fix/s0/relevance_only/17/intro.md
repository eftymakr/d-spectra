## Related Works

Semi-supervised learning (SSL) has been widely studied for its ability to leverage unlabeled data to improve model performance when labeled data is scarce \[[1](http://arxiv.org/abs/2311.10572)\]. However, conventional SSL methods assume that both labeled and unlabeled data share the same class distribution \[[2](http://arxiv.org/abs/2303.12091)\], which is often violated in real-world applications where unlabeled data may contain out-of-distribution (OOD) samples, i.e., outliers \[[3](http://arxiv.org/abs/2401.07551)\]. These outliers, often treated as noise, significantly degrade the performance of SSL models \[[4](http://arxiv.org/abs/2308.13168)\]. To address this challenge, various open-set SSL approaches have been proposed, aiming to detect and mitigate the negative impact of outliers \[[5](http://arxiv.org/abs/2412.18256)\].

Early methods, such as FixMatch \[[6](http://arxiv.org/abs/2105.14148)\], assume that unlabeled data are from the same distribution as labeled data, which limits their applicability in open-world scenarios \[[7](http://arxiv.org/abs/2109.00650)\]. To handle open-set scenarios, methods like OpenMatch \[[8](http://arxiv.org/abs/2107.08943)\] introduce novelty detection to distinguish inliers from outliers, while also incorporating soft-consistency regularization to improve outlier detection \[[9](http://arxiv.org/abs/2007.08844)\]. Similarly, IOMatch \[[10](http://arxiv.org/abs/2007.11330)\] proposes a framework that jointly utilizes inliers and outliers by combining a multi-binary classifier with a standard closed-set classifier, treating all outliers as a single new class \[[11](https://www.semanticscholar.org/paper/f3df804a7eef204b0c4fc4b81166dec9b4abc073)\]. This approach helps avoid the performance degradation caused by unreliable outlier detectors when labeled data is scarce \[[12](http://arxiv.org/abs/2203.02261)\].

Another line of research focuses on improving the robustness of SSL in the presence of class distribution mismatch \[[13](http://arxiv.org/abs/2308.11874)\]. For example, UASD \[[14](https://www.semanticscholar.org/paper/cfcdf167b3756735f230e72e4d2713bb063587b2)\] introduces uncertainty-aware self-distillation to avoid catastrophic error propagation and improve generalization under class distribution mismatch \[[15](http://arxiv.org/abs/2308.14119)\]. Similarly, WAD \[[16](http://arxiv.org/abs/2110.10368)\] proposes a framework that selectively transfers knowledge from unsupervised contrastive representations to the target classifier, using adaptive weights to filter unknown categories \[[17](https://www.semanticscholar.org/paper/9e4376e0572de32236e408469ffb2173d89eaab5)\]. These methods demonstrate that robust SSL is possible even when labeled and unlabeled data come from different distributions \[[18](http://arxiv.org/abs/2405.16093)\].

Additionally, methods like OpenCoS \[[19](http://arxiv.org/abs/2405.06979)\] utilize contrastive learning to identify out-of-class samples in unlabeled data, enabling the use of both inlier and outlier data for training \[[20](http://arxiv.org/abs/2403.15567)\]. Similarly, SAFER-STUDENT \[[21](https://www.semanticscholar.org/paper/1c952a381a5175f9dd936435b8f1a2bd706c8ffb)\] introduces a teacher-student framework to improve the identification of seen and unseen classes, using discrepancy-based scoring and energy-bounded calibration to enhance performance \[[22](http://arxiv.org/abs/2306.17699)\]. These approaches highlight the importance of distinguishing between inliers and outliers while leveraging the full potential of unlabeled data \[[23](http://arxiv.org/abs/2303.08978)\].

In contrast to these methods, our proposed framework, Diversify and Conquer (DAC), leverages prediction disagreements among multiple models with different biases toward the unlabeled distribution \[[24](http://arxiv.org/abs/2002.06815)\]. This approach enables robust outlier detection even when labeled data is insufficient \[[25](http://arxiv.org/abs/2310.16412)\]. By encouraging divergent heads to be differently biased toward outliers while maintaining consistent predictions for inliers, DAC exploits the disagreement among these heads to identify unknown concepts \[[26](http://arxiv.org/abs/2308.14058)\].

1. \[[1](http://arxiv.org/abs/2311.10572)\] http://arxiv.org/abs/2311.10572  
2. \[[2](http://arxiv.org/abs/2303.12091)\] http://arxiv.org/abs/2303.12091  
3. \[[3](http://arxiv.org/abs/2401.07551)\] http://arxiv.org/abs/2401.07551  
4. \[[4](http://arxiv.org/abs/2308.13168)\] http://arxiv.org/abs/2308.13168  
5. \[[5](http://arxiv.org/abs/2412.18256)\] http://arxiv.org/abs/2308.13168  
6. \[[6](http://arxiv.org/abs/2105.14148)\] http://arxiv.org/abs/2105.14148  
7. \[[7](http://arxiv.org/abs/2109.00650)\] http://arxiv.org/abs/2109.00650  
8. \[[8](http://arxiv.org/abs/2107.08943)\] http://arxiv.org/abs/2107.08943  
9. \[[9](http://arxiv.org/abs/2007.08844)\] http://arxiv.org/abs/2105.14148  
10. \[[10](http://arxiv.org/abs/2007.11330)\] http://arxiv.org/abs/2308.13168  
11. \[[11](https://www.semanticscholar.org/paper/f3df804a7eef204b0c4fc4b81166dec9b4abc073)\] http://arxiv.org/abs/2308.13168  
12. \[[12](http://arxiv.org/abs/2203.02261)\] http://arxiv.org/abs/2403.15567  
13. \[[13](http://arxiv.org/abs/2308.11874)\] http://arxiv.org/abs/2412.18256  
14. \[[14](https://www.semanticscholar.org/paper/cfcdf167b3756735f230e72e4d2713bb063587b2)\] http://arxiv.org/abs/2110.10368  
15. \[[15](http://arxiv.org/abs/2308.14119)\] http://arxiv.org/abs/2308.14119  
16. \[[16](http://arxiv.org/abs/2110.10368)\] http://arxiv.org/abs/2405.16093  
17. \[[17](https://www.semanticscholar.org/paper/9e4376e0572de32236e408469ffb2173d89eaab5)\] http://arxiv.org/abs/2405.06979  
18. \[[18](http://arxiv.org/abs/2405.16093)\] http://arxiv.org/abs/2306.17699  
19. \[[19](http://arxiv.org/abs/2405.06979)\] http://arxiv.org/abs/2303.08978  
20. \[[20](http://arxiv.org/abs/2403.15567)\] http://arxiv.org/abs/2002.06815  
21. \[[21](https://www.semanticscholar.org/paper/1c952a381a5175f9dd936435b8f1a2bd706c8ffb)\] http://arxiv.org/abs/2310.16412  
22. \[[22](http://arxiv.org/abs/2306.17699)\] http://arxiv.org/abs/2308.14058  
23. \[[23](http://arxiv.org/abs/2303.08978)\] http://arxiv.org/abs/2301.10127  
24. \[[24](http://arxiv.org/abs/2002.06815)\] http://arxiv.org/abs/2308.14058  
25. \[[25](http://arxiv.org/abs/2310.16412)\] http://arxiv.org/abs/2308.14058  
26. \[[26](http://arxiv.org/abs/2308.14058)\] http://arxiv.org/abs/2308.14058  
27. \[[27](http://arxiv.org/abs/2301.10127)\] http://arxiv.org/abs/2308.14058  
28. \[[28](https://www.semanticscholar.org/paper/11da6c90c29fbb8ddff6eaeeea40212b6624c226)\] http://arxiv.org/abs/2308.14058  
29. \[[29](http://arxiv.org/abs/2301.06010)\] http://arxiv.org/abs/2308.14058  
30. \[[30](http://arxiv.org/abs/2407.05370)\] http://arxiv.org/abs/2308.14058
