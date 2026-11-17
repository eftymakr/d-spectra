## Related Works

Federated Learning (FL) facilitates collaborative model training across multiple clients without sharing raw data, thereby enhancing privacy compliance with regulations like GDPR and CPRA \[[2403.02437](http://arxiv.org/abs/2403.02437)\]\[[2402.00342](http://arxiv.org/abs/2402.00342)\]. However, the emergence of the "right to be forgotten" has introduced the need for Federated Unlearning (FU), which enables selective removal of client data or contributions from a global model without full retraining \[[2401.05146](http://arxiv.org/abs/2401.05146)\]\[[2310.20448](http://arxiv.org/abs/2310.20448)\]\[[2403.02437](http://arxiv.org/abs/2403.02437)\]\[[2012.13891](http://arxiv.org/abs/2012.13891)\]. FU faces unique challenges due to FL’s distributed nature, data heterogeneity, and limited access to local data, making centralized unlearning methods insufficient in this context \[[2403.02437](http://arxiv.org/abs/2403.02437)\]\[[2207.05521](http://arxiv.org/abs/2207.05521)\].

Several FU approaches have been proposed with varying focuses on efficiency, security, and verifiability. Early methods like FedEraser rely on storing historical model updates at the server to reconstruct unlearned models more quickly than retraining from scratch \[[2012.13891](http://arxiv.org/abs/2012.13891)\]. However, this approach increases storage demands and may introduce security risks. More recent works propose certified unlearning techniques that avoid additional client communication or storage by approximating deep neural networks linearly and applying efficient removal operations on the server side, as in forgettable federated linear learning (F²L²) \[[2403.02437](http://arxiv.org/abs/2403.02437)\]\[[2306.02216](http://arxiv.org/abs/2306.02216)\]. Other methods, such as FATS, introduce algorithms that guarantee exact unlearning with provable statistical indistinguishability from retraining, emphasizing communication efficiency and theoretical rigor \[[2401.11018](http://arxiv.org/abs/2401.11018)\].

The verification of unlearning effectiveness is critical but often overlooked. VeriFi introduces a framework for verifiable federated unlearning by embedding user-specific markers into the training data and assessing model performance changes post-unlearning, providing strong empirical guarantees of unlearning success \[[2205.12709](http://arxiv.org/abs/2205.12709)\]. Complementary verification mechanisms leverage backdoor-based hypothesis testing to statistically certify data deletion, enabling high-confidence unlearning verification without compromising model utility \[[2003.04247](http://arxiv.org/abs/2003.04247)\].

Federated unlearning also contends with security threats, especially poisoning attacks targeting the unlearning process itself. BadUnlearn exemplifies malicious attempts to maintain poisoned knowledge during unlearning, while defenses like UnlearnGuard employ robust estimation and filtering of client updates to ensure the integrity of the unlearned model \[[2501.17396](http://arxiv.org/abs/2501.17396)\]. Such security considerations are pivotal for trustworthy FU deployment.

Domain and feature-specific unlearning have gained attention to prevent indiscriminate forgetting that degrades model performance across non-targeted data domains. Federated Domain Unlearning studies reveal that existing methods often erase essential representational subspaces, disproportionately affecting deeper model layers, necessitating domain-aware unlearning strategies and dedicated evaluation protocols \[[2406.03078](http://arxiv.org/abs/2406.03078)\]. Similarly, Ferrari proposes federated feature unlearning by optimizing feature sensitivity metrics to selectively remove sensitive or biased features while preserving model utility \[[2405.17462](http://arxiv.org/abs/2405.17462)\].

Efforts to balance unlearning effectiveness with fairness and incentive mechanisms have been explored. Fair machine unlearning methods aim to maintain fairness metrics alongside data removal, addressing potential disparities introduced by naive unlearning \[[2307.14754](http://arxiv.org/abs/2307.14754)\]. Incentive mechanisms model user behavior to encourage participation and retention of valuable clients, considering the costs and impacts of unlearning on global model performance \[[2308.12502](http://arxiv.org/abs/2308.12502)\]\[[2312.01235](http://arxiv.org/abs/2312.01235)\].

Recent advances also focus on unlearning granularity and efficiency. FedAU integrates an auxiliary unlearning module during training, enabling simultaneous and fine-grained unlearning at sample, class, or client levels without additional overhead \[[2405.15474](http://arxiv.org/abs/2405.15474)\]. Probabilistic approaches introduce plausible deniability frameworks, allowing servers to deny client participation within differential privacy guarantees while still performing unlearning when necessary, thus balancing privacy and operational costs \[[2410.09947](http://arxiv.org/abs/2410.09947)\].

In the context of Federated Online Learning to Rank (FOLTR), which optimizes ranking models from implicit user feedback in a privacy-preserving manner, unlearning methods remain nascent. FOLTR itself is challenged by effectiveness, robustness to client data heterogeneity, and security vulnerabilities \[[2012.13891](http://arxiv.org/abs/2012.13891)\]. Existing unlearning evaluation practices often rely on single metrics, which inadequately capture the nuanced trade-offs between under-unlearning (insufficient forgetting) and over-unlearning (excessive forgetting). Recent work advocates for multi-metric evaluations to provide comprehensive assessments of unlearning success, revealing limitations and guiding improvements in federated unlearning strategies \[[2405.17462](http://arxiv.org/abs/2405.17462)\]\[[2208.10836](http://arxiv.org/abs/2208.10836)\].

Overall, the intersection of federated unlearning and FOLTR demands approaches that are efficient, secure, verifiable, and sensitive to domain-specific ranking performance. This necessitates integrated frameworks that encompass rigorous unlearning guarantees, adversarial robustness, incentive alignment, and multi-faceted evaluation metrics to advance privacy-preserving and compliant federated ranking systems \[[2412.19069](http://arxiv.org/abs/2412.19069)\]\[[2310.20448](http://arxiv.org/abs/2310.20448)\]\[[2012.13891](http://arxiv.org/abs/2012.13891)\]\[[2205.12709](http://arxiv.org/abs/2205.12709)\]\[[2405.17462](http://arxiv.org/abs/2405.17462)\].

  
References:

\[[2412.19069](http://arxiv.org/abs/2412.19069)\] http://arxiv.org/abs/2412.19069  
\[[2401.05146](http://arxiv.org/abs/2401.05146)\] http://arxiv.org/abs/2401.05146  
\[[2310.20448](http://arxiv.org/abs/2310.20448)\] http://arxiv.org/abs/2310.20448  
\[[2406.03078](http://arxiv.org/abs/2406.03078)\] http://arxiv.org/abs/2406.03078  
\[[2403.02437](http://arxiv.org/abs/2403.02437)\] http://arxiv.org/abs/2306.02216  
\[[2308.12502](http://arxiv.org/abs/2308.12502)\] http://arxiv.org/abs/2308.12502  
\[[2306.02216](http://arxiv.org/abs/2306.02216)\] http://arxiv.org/abs/2306.02216  
\[[2012.13891](http://arxiv.org/abs/2012.13891)\] http://arxiv.org/abs/2012.13891  
\[[2205.12709](http://arxiv.org/abs/2205.12709)\] http://arxiv.org/abs/2205.12709  
\[[2405.17462](http://arxiv.org/abs/2405.17462)\] http://arxiv.org/abs/2405.17462  
\[[2207.05521](http://arxiv.org/abs/2207.05521)\] http://arxiv.org/abs/2207.05521  
\[[2405.15474](http://arxiv.org/abs/2405.15474)\] http://arxiv.org/abs/2405.15474  
\[[2410.09947](http://arxiv.org/abs/2410.09947)\] http://arxiv.org/abs/2410.09947  
\[[2401.11018](http://arxiv.org/abs/2401.11018)\] http://arxiv.org/abs/2401.11018  
\[[2312.01235](http://arxiv.org/abs/2312.01235)\] http://arxiv.org/abs/2312.01235  
\[[2003.04247](http://arxiv.org/abs/2003.04247)\] http://arxiv.org/abs/2003.04247  
\[[2501.17396](http://arxiv.org/abs/2501.17396)\] http://arxiv.org/abs/2501.17396  
\[[2307.14754](http://arxiv.org/abs/2307.14754)\] http://arxiv.org/abs/2307.14754  
\[[2208.10836](http://arxiv.org/abs/2208.10836)\] http://arxiv.org/abs/2208.10836