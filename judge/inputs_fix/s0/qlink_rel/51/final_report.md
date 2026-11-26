## Related Works

Federated unlearning has emerged as a critical research area in response to the "right to be forgotten" legislation, which mandates that users can request the removal of their data from machine learning models \[[1](http://arxiv.org/abs/2203.07320)\]. This has spurred the development of various unlearning methods aimed at efficiently removing the influence of specific data points or clients from a global model without requiring full retraining \[[2](https://www.semanticscholar.org/paper/eadeffdec9fac8fd7f9aea732ca410eb082b7dcf)\]. Early approaches focused on centralized settings, where the server had access to all training data, but these methods are not directly applicable to federated learning (FL) due to the decentralized nature of data \[[3](http://arxiv.org/abs/2310.20448)\]. 

In the context of FL, several studies have proposed techniques to enable efficient data removal. For instance, FedEraser introduces a method that leverages historical parameter updates retained by the central server to reconstruct an unlearned model, significantly reducing the time required compared to retraining from scratch \[[4](http://arxiv.org/abs/2207.05521)\]. Similarly, the paper titled *Federated Unlearning: How to Efficiently Erase a Client in FL?* proposes a two-step approach: local unlearning at the client level followed by a few rounds of federated learning with the remaining clients to obtain the unlearned global model \[[5](http://arxiv.org/abs/2201.09441)\]. This method avoids the need for storing historical updates or retraining from scratch, making it more efficient \[[6](https://www.semanticscholar.org/paper/39da2d48f2132b919405e3bb6df6ece44ac6e15a)\].

Another notable work, *Federated Unlearning with Knowledge Distillation*, introduces a method that subtracts accumulated historical updates from the model and uses knowledge distillation to restore model performance without relying on client data \[[7](https://www.semanticscholar.org/paper/06edb1f6eadb6c141d720fcca4c854578dc5d670)\]. This approach is particularly useful in scenarios where client participation is limited or where data access is restricted \[[8](http://arxiv.org/abs/2205.12709)\]. Additionally, *Communication Efficient and Provable Federated Unlearning* presents a framework that ensures exact unlearning and communication efficiency, with theoretical guarantees for the statistical indistinguishability of the unlearned model from the one trained without the deleted data \[[9](http://arxiv.org/abs/2209.02299)\].

The importance of verifiable unlearning has also been highlighted, with *VeriFi* introducing a framework that allows users to independently verify the effectiveness of unlearning by marking and checking the global model's performance on specific fingerprints \[[10](http://arxiv.org/abs/2401.05146)\]. This addresses a critical gap in current unlearning methods, where verification of the unlearning effect is often overlooked \[[11](https://www.semanticscholar.org/paper/a52c3ec7325e81bd87fdf8d74bf9acfd1e1ffe5f)\]. Furthermore, *Federated Unlearning via Class-Discriminative Pruning* explores selective forgetting of categories by pruning channels with high discriminative power, achieving significant speedups compared to retraining from scratch \[[12](http://arxiv.org/abs/2210.10958)\].

Lastly, *Advances and Open Problems in Federated Learning* provides a broad overview of FL, emphasizing the need for mechanisms that support the right to be forgotten and the challenges associated with implementing such mechanisms in distributed settings \[[13](http://arxiv.org/abs/2110.11794)\]. These studies collectively highlight the growing interest in federated unlearning and the need for robust, efficient, and verifiable methods to support data privacy in FL systems.

1. \[[1](http://arxiv.org/abs/2203.07320)\] \[[1](http://arxiv.org/abs/2203.07320)\]  
2. \[[2](https://www.semanticscholar.org/paper/eadeffdec9fac8fd7f9aea732ca410eb082b7dcf)\]  
3. \[[3](http://arxiv.org/abs/2310.20448)\]  
4. \[[4](http://arxiv.org/abs/2207.05521)\]  
5. \[[5](http://arxiv.org/abs/2201.09441)\]  
6. \[[6](https://www.semanticscholar.org/paper/39da2d48f2132b919405e3bb6df6ece44ac6e15a)\]  
7. \[[7](https://www.semanticscholar.org/paper/06edb1f6eadb6c141d720fcca4c854578dc5d670)\]  
8. \[[8](http://arxiv.org/abs/2205.12709)\]  
9. \[[9](http://arxiv.org/abs/2209.02299)\]  
10. \[[10](http://arxiv.org/abs/2401.05146)\]  
11. \[[11](https://www.semanticscholar.org/paper/a52c3ec7325e81bd87fdf8d74bf9acfd1e1ffe5f)\]  
12. \[[12](http://arxiv.org/abs/2210.10958)\]  
13. \[[13](http://arxiv.org/abs/2110.11794)\]
## Research papers
### Outline
- [Unlearning Methodologies in FL [17 papers]](#category-unlearning-methodologies-in-fl)
- [Challenges in Federated Unlearning [2 papers]](#category-challenges-in-federated-unlearning)
- [Knowledge Distillation in Unlearning [1 papers]](#category-knowledge-distillation-in-unlearning)
- [Verification of Unlearning Effect [1 papers]](#category-verification-of-unlearning-effect)
- [Legislative Context of Data Privacy [1 papers]](#category-legislative-context-of-data-privacy)
- [Communication Efficiency in Unlearning [1 papers]](#category-communication-efficiency-in-unlearning)
- [Federated Learning Overview [2 papers]](#category-federated-learning-overview)
- [Efficient Data Removal Techniques [3 papers]](#category-efficient-data-removal-techniques)
- [Selective Forgetting Approaches [2 papers]](#category-selective-forgetting-approaches)

### <a id='category-unlearning-methodologies-in-fl'></a>Unlearning Methodologies in FL: 17 papers found.
The category "Unlearning Methodologies in FL" explores the challenges and solutions for enabling efficient and effective data removal from federated learning (FL) models, particularly in response to the "right to be forgotten" and privacy regulations. Existing unlearning techniques in centralized machine learning are not directly applicable to FL due to its distributed nature and the lack of global data access \[[1](http://arxiv.org/abs/2203.07320)\]. To address this, several approaches have been proposed, such as FedEraser, which leverages historical parameter updates to reconstruct an unlearned model without requiring full retraining \[[2](https://www.semanticscholar.org/paper/eadeffdec9fac8fd7f9aea732ca410eb082b7dcf)\]. Similarly, the method proposed in \[[3](http://arxiv.org/abs/2310.20448)\] suggests a two-step process: local unlearning at the client and subsequent federated learning with remaining clients to obtain the unlearned global model, significantly improving efficiency. Another approach, Knot, introduces a clustered aggregation mechanism tailored for asynchronous FL, reducing retraining costs by limiting the scope of affected clients \[[12](http://arxiv.org/abs/2210.10958)\]. Additionally, methods like FedRecovery utilize differential privacy to erase a client's influence by adjusting gradient residuals and adding noise, ensuring statistical indistinguishability between the unlearned and retrained models \[[7](https://www.semanticscholar.org/paper/06edb1f6eadb6c141d720fcca4c854578dc5d670)\]. The concept of federated unlearning has also been extended to specific tasks such as category removal, where methods like the one described in \[[13](http://arxiv.org/abs/2110.11794)\] employ channel pruning and fine-tuning to selectively forget categories without retraining from scratch. These methodologies collectively highlight the growing interest in developing efficient, privacy-preserving unlearning strategies that align with legal and ethical standards in FL systems \[[14](https://www.semanticscholar.org/paper/efab3b30d6f67f55c68f9dc7c65b2b54b1789030)\].
|    | reference                                                                                                                                                                  | date     | key idea/summary                                                                                                                                                                                                                                                                                                           |
|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [The Right to be Forgotten in Federated Learning: An Efficient Realization with Rapid Retraining](http://arxiv.org/abs/2203.07320)                                         | 03/14/22 | This paper addresses the challenge of machine unlearning in Federated Learning systems, proposing a rapid retraining approach that allows data holders to efficiently erase their data from a trained model while keeping training data locally.                                                                           |
|  1 | [FedEraser: Enabling Efficient Client-Level Data Removal from Federated Learning Models](https://www.semanticscholar.org/paper/eadeffdec9fac8fd7f9aea732ca410eb082b7dcf)   | 06/25/21 | FedEraser is the first federated unlearning methodology that efficiently removes a client’s data influence from a global FL model by reconstructing the unlearned model using retained historical parameter updates, achieving a significant speed-up compared to retraining from scratch.                                 |
|  2 | [Federated Unlearning: How to Efficiently Erase a Client in FL?](http://arxiv.org/abs/2207.05521)                                                                          | 07/12/22 | This paper proposes an efficient federated unlearning method that allows erasing a client's influence from a global model by performing local unlearning and minimal subsequent federated learning rounds, without requiring global data access or parameter history.                                                      |
|  3 | [Federated Unlearning: Guarantee the Right of Clients to Forget](https://www.semanticscholar.org/paper/39da2d48f2132b919405e3bb6df6ece44ac6e15a)                           | 09/01/22 | The paper introduces federated unlearning as a method to efficiently remove data influence from FL models, proposing a general pipeline and techniques like reverse stochastic gradient ascent and elastic weight consolidation to address unlearning challenges.                                                          |
|  4 | [FedRecovery: Differentially Private Machine Unlearning for Federated Learning Frameworks](https://www.semanticscholar.org/paper/06edb1f6eadb6c141d720fcca4c854578dc5d670) | nan      | FedRecovery is an efficient machine unlearning algorithm for federated learning that removes the impact of specific data samples without retraining, using differential privacy to ensure statistical indistinguishability between the unlearned and retrained models.                                                     |
|  5 | [Federated Unlearning: A Survey on Methods, Design Guidelines, and Evaluation Metrics](http://arxiv.org/abs/2401.05146)                                                    | 01/10/24 | This paper addresses the need for federated unlearning (FU) algorithms that enable efficient removal of specific clients' contributions from a global model in federated learning, while preserving privacy and mitigating malicious updates.                                                                              |
|  6 | [Federated Unlearning for On-Device Recommendation](http://arxiv.org/abs/2210.10958)                                                                                       | 10/20/22 | The paper introduces FRU, an efficient unlearning method for federated recommendation systems, enabling users to remove their contributions while maintaining system robustness and compliance with data protection regulations.                                                                                           |
|  7 | [Federated Unlearning via Class-Discriminative Pruning](http://arxiv.org/abs/2110.11794)                                                                                   | 10/22/21 | This paper proposes a method to selectively unlearn specific categories from CNN models in federated learning without retraining from scratch, using TF-IDF to quantify channel discrimination and pruning followed by fine-tuning to maintain accuracy.                                                                   |
|  8 | [BFU: Bayesian Federated Unlearning with Parameter Self-Sharing](https://www.semanticscholar.org/paper/efab3b30d6f67f55c68f9dc7c65b2b54b1789030)                           | 07/10/23 | This paper addresses machine unlearning in federated learning by proposing a Bayesian Federated Unlearning (BFU) approach that enables data erasure without sharing raw data, while maintaining model accuracy through parameter self-sharing.                                                                             |
|  9 | [Federated Unlearning With Momentum Degradation](https://www.semanticscholar.org/paper/eff2be3b3ccfb1fc0650432b9b611ebd11ba0feb)                                           | 03/01/24 | This paper proposes an efficient method for unlearning in federated learning systems, addressing data privacy concerns by enabling client revocation and category removal through knowledge erasure and memory guidance strategies.                                                                                        |
| 10 | [Ferrari: Federated Feature Unlearning via Optimizing Feature Sensitivity](http://arxiv.org/abs/2405.17462)                                                                | 05/23/24 | The paper introduces Ferrari, a federated feature unlearning framework that minimizes feature sensitivity using Lipschitz continuity, addressing the limitations of existing methods in federated learning environments.                                                                                                   |
| 11 | [Asynchronous Federated Unlearning](https://www.semanticscholar.org/paper/70954dd11d1463bc665f803d84b15a4d83805ec0)                                                        | 05/17/23 | Knot is a new clustered aggregation mechanism designed for asynchronous federated learning that enables efficient machine unlearning by limiting retraining to specific client clusters, outperforming existing methods by up to 85%.                                                                                      |
| 12 | [FAST: Adopting Federated Unlearning to Eliminating Malicious Terminals at Server Side](https://www.semanticscholar.org/paper/2f69d7e9a7428a7e31de83b993a2142d0c2cde67)    | 03/01/24 | The paper proposes FAST, a federated unlearning framework that addresses the challenge of removing user contributions from malicious clients, achieving high accuracy and efficiency through three main components: eliminating malicious contributions, assessing unlearning efficiency, and remedying model performance. |
| 13 | [Exact-Fun: An Exact and Efficient Federated Unlearning Approach](https://www.semanticscholar.org/paper/a5f39bcd6198b26997b77233ff81a14e6bc8a32d)                          | 12/01/23 | This paper addresses the challenge of machine unlearning in federated learning, proposing Q-FL and Exact-Fun algorithms to enable efficient and exact data deletion while maintaining high performance.                                                                                                                    |
| 14 | [Unlearning during Learning: An Efficient Federated Machine Unlearning Method](http://arxiv.org/abs/2405.15474)                                                            | 05/24/24 | FedAU is an efficient and versatile federated machine unlearning framework that enables quick and comprehensive unlearning without additional time-consuming steps, supporting multiple levels of granularity in FL scenarios.                                                                                             |
| 15 | [Privacy-Preserving Federated Unlearning With Certified Client Removal](http://arxiv.org/abs/2404.09724)                                                                   | 04/15/24 | Starfish is a privacy-preserving federated unlearning scheme that uses Two-Party Computation (2PC) techniques to securely remove a client’s influence from the global model while minimizing information leakage and maintaining efficiency.                                                                               |
| 16 | [Federated Unlearning](http://arxiv.org/abs/2012.13891)                                                                                                                    | 12/27/20 | FedEraser is the first federated unlearning methodology that efficiently removes a client's data influence from a global FL model by reconstructing the unlearned model using retained historical parameter updates, achieving a significant speed-up compared to retraining from scratch.                                 |
### <a id='category-challenges-in-federated-unlearning'></a>Challenges in Federated Unlearning: 2 papers found.
The category "Challenges in Federated Unlearning" highlights the unique difficulties faced in implementing federated unlearning (FU) within federated learning (FL) frameworks. These challenges stem from the distributed and privacy-preserving nature of FL, which complicates the design and execution of unlearning mechanisms that allow for the removal of specific user data while maintaining model performance \[[3](http://arxiv.org/abs/2310.20448)\]. Existing FU approaches often struggle with ensuring complete data erasure without compromising the overall accuracy of the model, as the removal of data from one client can have cascading effects on the global model \[[11](https://www.semanticscholar.org/paper/a52c3ec7325e81bd87fdf8d74bf9acfd1e1ffe5f)\]. Furthermore, the discrepancy between pre- and post-unlearning models introduces risks of information leakage, which can undermine the privacy guarantees of FL systems \[[11](https://www.semanticscholar.org/paper/a52c3ec7325e81bd87fdf8d74bf9acfd1e1ffe5f)\]. This issue is exacerbated by the lack of standardized evaluation metrics, as most prior work relies on single metrics rather than a comprehensive assessment of unlearning effectiveness \[[3](http://arxiv.org/abs/2310.20448)\]. As a result, the development of robust and privacy-preserving FU algorithms remains an active area of research, with a growing emphasis on addressing these challenges through tailored algorithmic designs and enhanced security measures \[[3](http://arxiv.org/abs/2310.20448)\].
|    | reference                                                                                                                      | date     | key idea/summary                                                                                                                                                                                                                          |
|----|--------------------------------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [A Survey on Federated Unlearning: Challenges, Methods, and Future Directions](http://arxiv.org/abs/2310.20448)                | 10/31/23 | This survey provides an overview of federated unlearning techniques, evaluates existing algorithms, and discusses challenges, applications, and future research directions in the context of federated learning.                          |
|  1 | [Federated Unlearning and Its Privacy Threats](https://www.semanticscholar.org/paper/a52c3ec7325e81bd87fdf8d74bf9acfd1e1ffe5f) | 03/01/24 | This paper reviews federated unlearning and its privacy leakage risks, proposes new taxonomies for existing algorithms, identifies vulnerabilities to inference attacks, and suggests a privacy-preserving framework for future research. |
### <a id='category-knowledge-distillation-in-unlearning'></a>Knowledge Distillation in Unlearning: 1 papers found.
Context: 
	Document 1: [Snippet]: «Federated Learning (FL) is designed to protect the data privacy of each client during the training process by transmitting only models instead of the original data. However, the trained model may memorize certain information about the training data. With the recent legislation on right to be forgotten, it is crucially essential for the FL model to possess the ability to forget what it has learned from each client. We propose a novel federated unlearning method to eliminate a client's contribution by subtracting the accumulated historical updates from the model and leveraging the knowledge distillation method to restore the model's performance without using any data from the clients. This method does not have any restrictions on the type of neural networks and does not rely on clients' participation, so it is practical and efficient in the FL system. We further introduce backdoor attacks in the training process to help evaluate the unlearning effect. Experiments on three canonical datasets demonstrate the effectiveness and efficiency of our method.»
[_citation_number]: «5»
[Category]: «Knowledge Distillation in Unlearning»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-19T07:23:46+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2310.20448)\]. Further details \[[6](https://www.semanticscholar.org/paper/39da2d48f2132b919405e3bb6df6ece44ac6e15a)\]\[[7](https://www.semanticscholar.org/paper/06edb1f6eadb6c141d720fcca4c854578dc5d670)\]\[[8](http://arxiv.org/abs/2205.12709)\]\[[9](http://arxiv.org/abs/2209.02299)\]\[[10](http://arxiv.org/abs/2401.05146)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: This paper reports on findings from a comparative study on the effectiveness
and efficiency of federated unlearning strategies within Federated Online
Learning to Rank (FOLTR), with specific attention to systematically analysing
the unlearning capabilities of methods in a verifiable manner.
  Federated approaches to ranking of search results have recently garnered
attention to address users privacy concerns. In FOLTR, privacy is safeguarded
by collaboratively training ranking models across decentralized data sources,
preserving individual user data while optimizing search results based on
implicit feedback, such as clicks.
  Recent legislation introduced across numerous countries is establishing the
so called "the right to be forgotten", according to which services based on
machine learning models like those in FOLTR should provide capabilities that
allow users to remove their own data from those used to train models. This has
sparked the development of unlearning methods, along with evaluation practices
to measure whether unlearning of a user data successfully occurred. Current
evaluation practices are however often controversial, necessitating the use of
multiple metrics for a more comprehensive assessment -- but previous proposals
of unlearning methods only used single evaluation metrics.
  This paper addresses this limitation: our study rigorously assesses the
effectiveness of unlearning strategies in managing both under-unlearning and
over-unlearning scenarios using adapted, and newly proposed evaluation metrics.
Thanks to our detailed analysis, we uncover the strengths and limitations of
five unlearning strategies, offering valuable insights into optimizing
federated unlearning to balance data privacy and system performance within
FOLTR. We publicly release our code and complete results at
https://github.com/Iris1026/Unlearning-for-FOLTR.git.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2310.20448)\]. Further details discussed in contexts \[[2](https://www.semanticscholar.org/paper/eadeffdec9fac8fd7f9aea732ca410eb082b7dcf)\]\[[7](https://www.semanticscholar.org/paper/06edb1f6eadb6c141d720fcca4c854578dc5d670)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Knowledge distillation has emerged as a promising technique in federated unlearning, particularly for efficiently restoring model performance after removing a client's contribution \[[5](http://arxiv.org/abs/2201.09441)\]. This approach leverages the knowledge from a global model to distill relevant information into a smaller, more efficient model, ensuring that the unlearning process does not compromise the overall utility of the system \[[5](http://arxiv.org/abs/2201.09441)\]. By avoiding the need for direct access to client data, knowledge distillation enables the unlearning process to be both privacy-preserving and practical, especially in decentralized environments like Federated Learning \[[5](http://arxiv.org/abs/2201.09441)\]. This method is particularly useful in scenarios where clients may not be able or willing to participate actively in the unlearning process, making it a valuable tool for maintaining system efficiency while adhering to data privacy regulations \[[5](http://arxiv.org/abs/2201.09441)\].
|    | reference                                                                           | date     | key idea/summary                                                                                                                                                                                                                      |
|----|-------------------------------------------------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Federated Unlearning with Knowledge Distillation](http://arxiv.org/abs/2201.09441) | 01/24/22 | The paper proposes a novel federated unlearning method that allows FL models to forget specific client data contributions without requiring client participation or data access, using historical updates and knowledge distillation. |
### <a id='category-verification-of-unlearning-effect'></a>Verification of Unlearning Effect: 1 papers found.
Context: 
	Document 1: [Snippet]: «Federated learning (FL) has emerged as a privacy-aware collaborative learning paradigm where participants jointly train a powerful model without sharing their private data. One desirable property for FL is the implementation of the <italic>right to be forgotten (RTBF)</italic>, i.e., a leaving participant has the right to request the deletion of its private data from the global model. However, <italic>unlearning itself may not be enough to implement RTBF unless the unlearning effect can be independently verified</italic>, an important aspect that has been overlooked in the current literature. Unlearning verification is particularly challenging in FL as the unlearning effect on one participant's data could be canceled by the contribution of other participants. In this work, we prompt the concept of <italic>verifiable federated unlearning</italic> and propose <sc>VeriFi</sc>, a unified framework that allows systematic analysis of federated unlearning and quantification of its effect, with different combinations of various unlearning and verification methods. In <sc>VeriFi</sc>, the leaving participant is granted the <italic>right to verify (RTV)</italic> to actively verify the unlearning effect in the next few rounds immediately after notifying the server of its intention to leave, along with local verification done through two steps: 1) <italic>marking</italic> that fingerprints the leaving participant by specially-designed <italic>markers</italic> and 2) <italic>checking</italic> that examines the global model's performance change on the markers. Based on <sc>VeriFi</sc>, we have conducted so far the most systematic study on verifiable federated unlearning, covering six unlearning methods and five verification methods. Our study sheds light on the existing drawbacks and potential alternatives for both unlearning and verification methods. During the study, we also propose a more efficient and FL-friendly unlearning method <inline-formula><tex-math notation="LaTeX">$^(u)$</tex-math><alternatives><mml:math><mml:msup><mml:mrow/><mml:mi>u</mml:mi></mml:msup></mml:math><inline-graphic xlink:href="chen-ieq1-3382321.gif"/></alternatives></inline-formula>S2U, and two more effective and robust non-invasive (without training controllability, external data, white-box model access nor introducing new security risks) verification methods <inline-formula><tex-math notation="LaTeX">$^(v)$</tex-math><alternatives><mml:math><mml:msup><mml:mrow/><mml:mi>v</mml:mi></mml:msup></mml:math><inline-graphic xlink:href="chen-ieq2-3382321.gif"/></alternatives></inline-formula>FM and <inline-formula><tex-math notation="LaTeX">$^(v)$</tex-math><alternatives><mml:math><mml:msup><mml:mrow/><mml:mi>v</mml:mi></mml:msup></mml:math><inline-graphic xlink:href="chen-ieq3-3382321.gif"/></alternatives></inline-formula>EM. While the proposed methods may not be a panacea for all the challenges, they address several key drawbacks of existing methods and represent a promising step toward effective, efficient, robust, and more importantly, non-invasive federated unlearning and verification. We extensively evaluate <sc>VeriFi</sc> on seven datasets, including natural/facial/medical images and audios, and four types of deep learning models, including both Convolutional Neural Networks (CNNs) and Recurrent Neural Networks (RNNs). We hope, such an extensive and holistic experimental evaluation, although admittedly complex and challenging, could help establish important empirical understandings, evidence, and insights for trustworthy federated unlearning.»
[_citation_number]: «8»
[Category]: «Verification of Unlearning Effect»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-19T07:23:46+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2310.20448)\]. Further details \[[6](https://www.semanticscholar.org/paper/39da2d48f2132b919405e3bb6df6ece44ac6e15a)\]\[[7](https://www.semanticscholar.org/paper/06edb1f6eadb6c141d720fcca4c854578dc5d670)\]\[[8](http://arxiv.org/abs/2205.12709)\]\[[9](http://arxiv.org/abs/2209.02299)\]\[[10](http://arxiv.org/abs/2401.05146)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: This paper reports on findings from a comparative study on the effectiveness
and efficiency of federated unlearning strategies within Federated Online
Learning to Rank (FOLTR), with specific attention to systematically analysing
the unlearning capabilities of methods in a verifiable manner.
  Federated approaches to ranking of search results have recently garnered
attention to address users privacy concerns. In FOLTR, privacy is safeguarded
by collaboratively training ranking models across decentralized data sources,
preserving individual user data while optimizing search results based on
implicit feedback, such as clicks.
  Recent legislation introduced across numerous countries is establishing the
so called "the right to be forgotten", according to which services based on
machine learning models like those in FOLTR should provide capabilities that
allow users to remove their own data from those used to train models. This has
sparked the development of unlearning methods, along with evaluation practices
to measure whether unlearning of a user data successfully occurred. Current
evaluation practices are however often controversial, necessitating the use of
multiple metrics for a more comprehensive assessment -- but previous proposals
of unlearning methods only used single evaluation metrics.
  This paper addresses this limitation: our study rigorously assesses the
effectiveness of unlearning strategies in managing both under-unlearning and
over-unlearning scenarios using adapted, and newly proposed evaluation metrics.
Thanks to our detailed analysis, we uncover the strengths and limitations of
five unlearning strategies, offering valuable insights into optimizing
federated unlearning to balance data privacy and system performance within
FOLTR. We publicly release our code and complete results at
https://github.com/Iris1026/Unlearning-for-FOLTR.git.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2310.20448)\]. Further details discussed in contexts \[[2](https://www.semanticscholar.org/paper/eadeffdec9fac8fd7f9aea732ca410eb082b7dcf)\]\[[7](https://www.semanticscholar.org/paper/06edb1f6eadb6c141d720fcca4c854578dc5d670)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The verification of unlearning effect in federated learning has gained significant attention due to the increasing demand for privacy-preserving mechanisms, particularly in light of the "right to be forgotten" legislation \[[8](http://arxiv.org/abs/2205.12709)\]. This concept emphasizes the necessity of ensuring that when a participant requests the removal of their data, the unlearning process is not only executed but also independently verified to confirm its success \[[8](http://arxiv.org/abs/2205.12709)\]. This is crucial because unlearning alone may not suffice for implementing the right to be forgotten, as the effects can be undermined by contributions from other participants \[[8](http://arxiv.org/abs/2205.12709)\]. To address this, the paper introduces the concept of verifiable federated unlearning, proposing a framework called VeriFi that enables systematic analysis and quantification of unlearning effects through a combination of unlearning and verification methods \[[8](http://arxiv.org/abs/2205.12709)\]. The framework grants the leaving participant the right to verify (RTV) the unlearning effect, allowing them to actively verify the results in the subsequent rounds after notifying the server of their intention to leave \[[8](http://arxiv.org/abs/2205.12709)\]. This verification is conducted through two steps: marking, which involves fingerprinting the leaving participant using specially designed markers, and checking, which examines the global model's performance change on these markers \[[8](http://arxiv.org/abs/2205.12709)\]. The study also introduces new unlearning and verification methods, such as S2U for unlearning and FM and EM for verification, which are non-invasive and robust \[[8](http://arxiv.org/abs/2205.12709)\]. These methods aim to address existing challenges and provide a more efficient and secure approach to federated unlearning and verification \[[8](http://arxiv.org/abs/2205.12709)\].
|    | reference                                                                          | date     | key idea/summary                                                                                                                                                                                                                     |
|----|------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [VeriFi: Towards Verifiable Federated Unlearning](http://arxiv.org/abs/2205.12709) | 05/25/22 | This paper introduces VeriFi, a framework for verifiable federated unlearning that enables participants to verify the unlearning effect of their data, addressing the challenge of ensuring privacy and trust in federated learning. |
### <a id='category-legislative-context-of-data-privacy'></a>Legislative Context of Data Privacy: 1 papers found.
Context: 
	Document 1: [Snippet]: «Today, computer systems hold large amounts of personal data. Yet while such an abundance of data allows breakthroughs in AI, and especially machine learning, its existence can be a threat to user privacy, and it can weaken the bonds of trust between humans and AI. Recent regulations now require that, on request, private information about a user must be removed both from computer systems and from machine learning models—this legislation is more colloquially called “the right to be forgotten.” While removing data from back-end databases should be straightforward, it is not sufficient in the AI context as machine learning models often “remember” the old data. Contemporary adversarial attacks on trained models have proven that we can learn whether an instance or an attribute belonged to the training data. This phenomenon calls for a new paradigm, namely machine unlearning, to make machine learning models forget about particular data. It turns out that recent works on machine unlearning have not been able to completely solve the problem due to the lack of common frameworks and resources. Therefore, this article aspires to present a comprehensive examination of machine unlearning’s concepts, designs, methods, and applications. Specifically, as a category collection of cutting-edge studies, the intention behind this article is to serve as a comprehensive resource for researchers and practitioners seeking an introduction to machine unlearning and its formulations, design criteria, removal requests, algorithms, and applications. In addition, we aim to highlight the key findings, current trends, and new research areas that have not yet featured the use of machine unlearning but could benefit greatly from it. We hope that this survey serves as a valuable resource for machine learning researchers and those seeking to innovate privacy technologies. Our resources are publicly available at https://github.com/tamlhp/awesome-machine-unlearning.»
[_citation_number]: «9»
[Category]: «Legislative Context of Data Privacy»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-19T07:23:46+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2310.20448)\]. Further details \[[6](https://www.semanticscholar.org/paper/39da2d48f2132b919405e3bb6df6ece44ac6e15a)\]\[[7](https://www.semanticscholar.org/paper/06edb1f6eadb6c141d720fcca4c854578dc5d670)\]\[[8](http://arxiv.org/abs/2205.12709)\]\[[9](http://arxiv.org/abs/2209.02299)\]\[[10](http://arxiv.org/abs/2401.05146)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: This paper reports on findings from a comparative study on the effectiveness
and efficiency of federated unlearning strategies within Federated Online
Learning to Rank (FOLTR), with specific attention to systematically analysing
the unlearning capabilities of methods in a verifiable manner.
  Federated approaches to ranking of search results have recently garnered
attention to address users privacy concerns. In FOLTR, privacy is safeguarded
by collaboratively training ranking models across decentralized data sources,
preserving individual user data while optimizing search results based on
implicit feedback, such as clicks.
  Recent legislation introduced across numerous countries is establishing the
so called "the right to be forgotten", according to which services based on
machine learning models like those in FOLTR should provide capabilities that
allow users to remove their own data from those used to train models. This has
sparked the development of unlearning methods, along with evaluation practices
to measure whether unlearning of a user data successfully occurred. Current
evaluation practices are however often controversial, necessitating the use of
multiple metrics for a more comprehensive assessment -- but previous proposals
of unlearning methods only used single evaluation metrics.
  This paper addresses this limitation: our study rigorously assesses the
effectiveness of unlearning strategies in managing both under-unlearning and
over-unlearning scenarios using adapted, and newly proposed evaluation metrics.
Thanks to our detailed analysis, we uncover the strengths and limitations of
five unlearning strategies, offering valuable insights into optimizing
federated unlearning to balance data privacy and system performance within
FOLTR. We publicly release our code and complete results at
https://github.com/Iris1026/Unlearning-for-FOLTR.git.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2310.20448)\]. Further details discussed in contexts \[[2](https://www.semanticscholar.org/paper/eadeffdec9fac8fd7f9aea732ca410eb082b7dcf)\]\[[7](https://www.semanticscholar.org/paper/06edb1f6eadb6c141d720fcca4c854578dc5d670)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The legislative context of data privacy has increasingly emphasized the need for users to have control over their personal data, particularly through the "right to be forgotten" \[[9](http://arxiv.org/abs/2209.02299)\]. This right, now enshrined in various national and international regulations, mandates that users can request the removal of their data from both computer systems and machine learning models \[[9](http://arxiv.org/abs/2209.02299)\]. While removing data from databases is relatively straightforward, the challenge lies in ensuring that machine learning models, which often retain memory of past data, can also be made to forget specific instances \[[9](http://arxiv.org/abs/2209.02299)\]. This has led to the emergence of machine unlearning as a critical research area, aiming to develop methods that enable models to remove specific data points without compromising performance \[[9](http://arxiv.org/abs/2209.02299)\]. The need for such capabilities is underscored by the growing concern over privacy and trust in AI systems, particularly in decentralized environments like Federated Online Learning to Rank (FOLTR), where user data is preserved while optimizing search results \[[9](http://arxiv.org/abs/2209.02299)\].
|    | reference                                                         | date     | key idea/summary                                                                                                                                                                                                     |
|----|-------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [A Survey of Machine Unlearning](http://arxiv.org/abs/2209.02299) | 09/06/22 | The paper presents a comprehensive survey on machine unlearning, addressing the challenge of making machine learning models forget specific data, and highlights its importance for privacy and trust in AI systems. |
### <a id='category-communication-efficiency-in-unlearning'></a>Communication Efficiency in Unlearning: 1 papers found.
Context: 
	Document 1: [Snippet]: «
 We study federated unlearning, a novel problem to eliminate the impact of specific clients or data points on the global model learned via federated learning (FL). This problem is driven by the right to be forgotten and the privacy challenges in FL. We introduce a new framework for exact federated unlearning that meets two essential criteria:
 communication efficiency
 and
 exact unlearning provability.
 To our knowledge, this is the first work to tackle both aspects coherently. We start by giving a rigorous definition of
 exact
 federated unlearning, which guarantees that the unlearned model is statistically indistinguishable from the one trained without the deleted data. We then pinpoint the key property that enables fast exact federated unlearning: total variation (TV) stability, which measures the sensitivity of the model parameters to slight changes in the dataset. Leveraging this insight, we develop a TV-stable FL algorithm called FATS, which modifies the classical FedAvg algorithm for TV Stability and employs local SGD with periodic averaging to lower the communication round. We also design efficient unlearning algorithms for FATS under two settings: client-level and sample-level unlearning. We provide theoretical guarantees for our learning and unlearning algorithms, proving that they achieve exact federated unlearning with reasonable convergence rates for both the original and unlearned models. We empirically validate our framework on 6 benchmark datasets, and show its superiority over state-of-the-art methods in terms of accuracy, communication cost, computation cost, and unlearning efficacy.
»
[_citation_number]: «16»
[Category]: «Communication Efficiency in Unlearning»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-19T07:23:46+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2310.20448)\]. Further details \[[6](https://www.semanticscholar.org/paper/39da2d48f2132b919405e3bb6df6ece44ac6e15a)\]\[[7](https://www.semanticscholar.org/paper/06edb1f6eadb6c141d720fcca4c854578dc5d670)\]\[[8](http://arxiv.org/abs/2205.12709)\]\[[9](http://arxiv.org/abs/2209.02299)\]\[[10](http://arxiv.org/abs/2401.05146)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: This paper reports on findings from a comparative study on the effectiveness
and efficiency of federated unlearning strategies within Federated Online
Learning to Rank (FOLTR), with specific attention to systematically analysing
the unlearning capabilities of methods in a verifiable manner.
  Federated approaches to ranking of search results have recently garnered
attention to address users privacy concerns. In FOLTR, privacy is safeguarded
by collaboratively training ranking models across decentralized data sources,
preserving individual user data while optimizing search results based on
implicit feedback, such as clicks.
  Recent legislation introduced across numerous countries is establishing the
so called "the right to be forgotten", according to which services based on
machine learning models like those in FOLTR should provide capabilities that
allow users to remove their own data from those used to train models. This has
sparked the development of unlearning methods, along with evaluation practices
to measure whether unlearning of a user data successfully occurred. Current
evaluation practices are however often controversial, necessitating the use of
multiple metrics for a more comprehensive assessment -- but previous proposals
of unlearning methods only used single evaluation metrics.
  This paper addresses this limitation: our study rigorously assesses the
effectiveness of unlearning strategies in managing both under-unlearning and
over-unlearning scenarios using adapted, and newly proposed evaluation metrics.
Thanks to our detailed analysis, we uncover the strengths and limitations of
five unlearning strategies, offering valuable insights into optimizing
federated unlearning to balance data privacy and system performance within
FOLTR. We publicly release our code and complete results at
https://github.com/Iris1026/Unlearning-for-FOLTR.git.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2310.20448)\]. Further details discussed in contexts \[[2](https://www.semanticscholar.org/paper/eadeffdec9fac8fd7f9aea732ca410eb082b7dcf)\]\[[7](https://www.semanticscholar.org/paper/06edb1f6eadb6c141d720fcca4c854578dc5d670)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The category of communication efficiency in federated unlearning focuses on reducing the communication overhead during the unlearning process while ensuring the model remains statistically indistinguishable from the original model after unlearning \[[16](http://arxiv.org/abs/2401.11018)\]. This is critical in federated learning (FL) settings where multiple clients contribute data to train a global model, and the need to remove specific data points or clients raises privacy concerns \[[16](http://arxiv.org/abs/2401.11018)\]. Existing methods often face a trade-off between the accuracy of unlearning and the communication cost, as frequent model updates between clients and the server can be resource-intensive \[[16](http://arxiv.org/abs/2401.11018)\]. To address this, recent work has introduced frameworks that leverage properties like total variation (TV) stability, which measures how sensitive model parameters are to changes in the dataset \[[16](http://arxiv.org/abs/2401.11018)\]. By incorporating TV-stability into FL algorithms, such as modifying the classical FedAvg algorithm, researchers have developed more efficient unlearning strategies that minimize communication rounds while maintaining model performance \[[16](http://arxiv.org/abs/2401.11018)\]. These approaches often employ techniques like local stochastic gradient descent (SGD) with periodic averaging to further reduce the communication burden \[[16](http://arxiv.org/abs/2401.11018)\]. The emphasis on communication efficiency is particularly relevant in large-scale FL systems, where minimizing bandwidth usage is essential for scalability and practical deployment \[[16](http://arxiv.org/abs/2401.11018)\].
|    | reference                                                                                    | date     | key idea/summary                                                                                                                                                                                                                                |
|----|----------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Communication Efficient and Provable Federated Unlearning](http://arxiv.org/abs/2401.11018) | 01/01/24 | This paper introduces a framework for federated unlearning that ensures exact removal of specific client or data point impacts from a global model, achieving communication efficiency and provable unlearning through TV-stable FL algorithms. |
### <a id='category-federated-learning-overview'></a>Federated Learning Overview: 2 papers found.
Context: 
	Document 1: [Snippet]: «Federated learning (FL) is a machine learning setting where many clients (e.g. mobile devices or whole organizations) collaboratively train a model under the orchestration of a central server (e.g. service provider), while keeping the training data decentralized. FL embodies the principles of focused data collection and minimization, and can mitigate many of the systemic privacy risks and costs resulting from traditional, centralized machine learning and data science approaches. Motivated by the explosive growth in FL research, this paper discusses recent advances and presents an extensive collection of open problems and challenges.»
[_citation_number]: «20»
[Category]: «Federated Learning Overview»

	Document 2: [Snippet]: «Federated learning enables thousands of participants to construct a deep learning model without sharing their private training data with each other. For example, multiple smartphones can jointly train a next-word predictor for keyboards without revealing what individual users type. We demonstrate that any participant in federated learning can introduce hidden backdoor functionality into the joint global model, e.g., to ensure that an image classifier assigns an attacker-chosen label to images with certain features, or that a word predictor completes certain sentences with an attacker-chosen word. 
We design and evaluate a new model-poisoning methodology based on model replacement. An attacker selected in a single round of federated learning can cause the global model to immediately reach 100% accuracy on the backdoor task. We evaluate the attack under different assumptions for the standard federated-learning tasks and show that it greatly outperforms data poisoning. Our generic constrain-and-scale technique also evades anomaly detection-based defenses by incorporating the evasion into the attacker's loss function during training.»
[_citation_number]: «26»
[Category]: «Federated Learning Overview»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-19T07:23:46+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2310.20448)\]. Further details \[[6](https://www.semanticscholar.org/paper/39da2d48f2132b919405e3bb6df6ece44ac6e15a)\]\[[7](https://www.semanticscholar.org/paper/06edb1f6eadb6c141d720fcca4c854578dc5d670)\]\[[8](http://arxiv.org/abs/2205.12709)\]\[[9](http://arxiv.org/abs/2209.02299)\]\[[10](http://arxiv.org/abs/2401.05146)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: This paper reports on findings from a comparative study on the effectiveness
and efficiency of federated unlearning strategies within Federated Online
Learning to Rank (FOLTR), with specific attention to systematically analysing
the unlearning capabilities of methods in a verifiable manner.
  Federated approaches to ranking of search results have recently garnered
attention to address users privacy concerns. In FOLTR, privacy is safeguarded
by collaboratively training ranking models across decentralized data sources,
preserving individual user data while optimizing search results based on
implicit feedback, such as clicks.
  Recent legislation introduced across numerous countries is establishing the
so called "the right to be forgotten", according to which services based on
machine learning models like those in FOLTR should provide capabilities that
allow users to remove their own data from those used to train models. This has
sparked the development of unlearning methods, along with evaluation practices
to measure whether unlearning of a user data successfully occurred. Current
evaluation practices are however often controversial, necessitating the use of
multiple metrics for a more comprehensive assessment -- but previous proposals
of unlearning methods only used single evaluation metrics.
  This paper addresses this limitation: our study rigorously assesses the
effectiveness of unlearning strategies in managing both under-unlearning and
over-unlearning scenarios using adapted, and newly proposed evaluation metrics.
Thanks to our detailed analysis, we uncover the strengths and limitations of
five unlearning strategies, offering valuable insights into optimizing
federated unlearning to balance data privacy and system performance within
FOLTR. We publicly release our code and complete results at
https://github.com/Iris1026/Unlearning-for-FOLTR.git.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2310.20448)\]. Further details discussed in contexts \[[2](https://www.semanticscholar.org/paper/eadeffdec9fac8fd7f9aea732ca410eb082b7dcf)\]\[[7](https://www.semanticscholar.org/paper/06edb1f6eadb6c141d720fcca4c854578dc5d670)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Federated learning (FL) has emerged as a critical paradigm for training machine learning models while preserving data privacy by keeping training data decentralized \[[20](http://arxiv.org/abs/1912.04977)\]. This approach allows multiple clients, such as mobile devices or organizations, to collaboratively train a model under the orchestration of a central server without sharing raw data \[[20](http://arxiv.org/abs/1912.04977)\]. FL aligns with principles of focused data collection and minimization, addressing systemic privacy risks and costs associated with traditional centralized approaches \[[20](http://arxiv.org/abs/1912.04977)\]. However, FL is not without challenges, as demonstrated by recent research highlighting vulnerabilities such as the potential for model poisoning and backdoor attacks \[[26](http://arxiv.org/abs/1807.00459)\]. For instance, attackers can introduce hidden functionalities into the global model, enabling them to manipulate outputs based on specific features, such as forcing an image classifier to assign attacker-chosen labels \[[26](http://arxiv.org/abs/1807.00459)\]. These findings underscore the need for robust security mechanisms and anomaly detection strategies in FL systems. The growing interest in FL is further fueled by its applicability in scenarios like Federated Online Learning to Rank (FOLTR), where privacy is safeguarded by training ranking models across decentralized data sources while optimizing search results based on implicit feedback \[[20](http://arxiv.org/abs/1912.04977)\]. As FL continues to evolve, addressing both security and efficiency remains a central focus of ongoing research.
|    | reference                                                                           | date     | key idea/summary                                                                                                                                                                                                      |
|----|-------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Advances and Open Problems in Federated Learning](http://arxiv.org/abs/1912.04977) | 12/10/19 | Federated learning enables collaborative model training across decentralized data sources while preserving data privacy, addressing challenges in traditional centralized approaches.                                 |
|  1 | [How To Backdoor Federated Learning](http://arxiv.org/abs/1807.00459)               | 07/02/18 | Federated learning allows participants to collaboratively train a model without sharing data, but it is vulnerable to backdoor attacks where an attacker can manipulate the global model to perform unintended tasks. |
### <a id='category-efficient-data-removal-techniques'></a>Efficient Data Removal Techniques: 3 papers found.
Context: 
	Document 1: [Snippet]: «Once users have shared their data online, it is generally difficult for them to revoke access and ask for the data to be deleted. Machine learning (ML) exacerbates this problem because any model trained with said data may have memorized it, putting users at risk of a successful privacy attack exposing their information. Yet, having models unlearn is notoriously difficult. We introduce SISA training, a framework that expedites the unlearning process by strategically limiting the influence of a data point in the training procedure. While our framework is applicable to any learning algorithm, it is designed to achieve the largest improvements for stateful algorithms like stochastic gradient descent for deep neural networks. SISA training reduces the computational overhead associated with unlearning, even in the worst-case setting where unlearning requests are made uniformly across the training set. In some cases, the service provider may have a prior on the distribution of unlearning requests that will be issued by users. We may take this prior into account to partition and order data accordingly, and further decrease overhead from unlearning. Our evaluation spans several datasets from different domains, with corresponding motivations for unlearning. Under no distributional assumptions, for simple learning tasks, we observe that SISA training improves time to unlearn points from the Purchase dataset by 4.63×, and 2.45× for the SVHN dataset, over retraining from scratch. SISA training also provides a speed-up of 1.36× in retraining for complex learning tasks such as ImageNet classification; aided by transfer learning, this results in a small degradation in accuracy. Our work contributes to practical data governance in machine unlearning.»
[_citation_number]: «21»
[Category]: «Efficient Data Removal Techniques»

	Document 2: [Snippet]: «Machine Unlearning (MU) has recently gained considerable attention due to its potential to achieve Safe AI by removing the influence of specific data from trained Machine Learning (ML) models. This process, known as knowledge removal, addresses AI governance concerns of training data such as quality, sensitivity, copyright restrictions, obsolescence, and compliance with privacy regulations. Efforts have been made to design efficient unlearning approaches, with MU services being examined for integration with existing machine learning as a service (MLaaS), allowing users to submit requests to remove specific data from the training corpus. However, recent research highlights vulnerabilities in machine unlearning systems that can lead to significant security and privacy concerns. Moreover, extensive research indicates that unlearning methods and prevalent attacks fulfill diverse roles within MU systems. This underscores the intricate relationship and complex interplay among these mechanisms in maintaining system functionality and safety. This survey aims to fill the gap between the extensive number of studies on threats, attacks, and defenses in machine unlearning and the absence of a comprehensive review that categorizes their taxonomy, methods, and solutions, thus offering valuable insights for future research directions and practical implementations.»
[_citation_number]: «28»
[Category]: «Efficient Data Removal Techniques»

	Document 3: [Snippet]: «Many online platforms have widely deployed machine learning models as a service. Many of these applications require users to upload their data for model training, but it also induces privacy risks. Once the user wants to leave the application, how to make the application unlearn the uploaded data, which is called machine unlearning, is worthy of study. In this article, we provide a survey of machine unlearning with an approximate and exact guarantee. We summarize the existing machine unlearning approaches and discuss their merits and drawbacks in this field.»
[_citation_number]: «30»
[Category]: «Efficient Data Removal Techniques»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-19T07:23:46+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2310.20448)\]. Further details \[[6](https://www.semanticscholar.org/paper/39da2d48f2132b919405e3bb6df6ece44ac6e15a)\]\[[7](https://www.semanticscholar.org/paper/06edb1f6eadb6c141d720fcca4c854578dc5d670)\]\[[8](http://arxiv.org/abs/2205.12709)\]\[[9](http://arxiv.org/abs/2209.02299)\]\[[10](http://arxiv.org/abs/2401.05146)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: This paper reports on findings from a comparative study on the effectiveness
and efficiency of federated unlearning strategies within Federated Online
Learning to Rank (FOLTR), with specific attention to systematically analysing
the unlearning capabilities of methods in a verifiable manner.
  Federated approaches to ranking of search results have recently garnered
attention to address users privacy concerns. In FOLTR, privacy is safeguarded
by collaboratively training ranking models across decentralized data sources,
preserving individual user data while optimizing search results based on
implicit feedback, such as clicks.
  Recent legislation introduced across numerous countries is establishing the
so called "the right to be forgotten", according to which services based on
machine learning models like those in FOLTR should provide capabilities that
allow users to remove their own data from those used to train models. This has
sparked the development of unlearning methods, along with evaluation practices
to measure whether unlearning of a user data successfully occurred. Current
evaluation practices are however often controversial, necessitating the use of
multiple metrics for a more comprehensive assessment -- but previous proposals
of unlearning methods only used single evaluation metrics.
  This paper addresses this limitation: our study rigorously assesses the
effectiveness of unlearning strategies in managing both under-unlearning and
over-unlearning scenarios using adapted, and newly proposed evaluation metrics.
Thanks to our detailed analysis, we uncover the strengths and limitations of
five unlearning strategies, offering valuable insights into optimizing
federated unlearning to balance data privacy and system performance within
FOLTR. We publicly release our code and complete results at
https://github.com/Iris1026/Unlearning-for-FOLTR.git.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2310.20448)\]. Further details discussed in contexts \[[2](https://www.semanticscholar.org/paper/eadeffdec9fac8fd7f9aea732ca410eb082b7dcf)\]\[[7](https://www.semanticscholar.org/paper/06edb1f6eadb6c141d720fcca4c854578dc5d670)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Efficient data removal techniques have gained significant attention in the field of machine unlearning, driven by the increasing demand for data privacy and compliance with regulations such as the "right to be forgotten" \[[3](http://arxiv.org/abs/2310.20448)\]. This category focuses on methods that aim to reduce the computational overhead associated with unlearning, particularly in scenarios where users request the removal of their data from trained models \[[21](http://arxiv.org/abs/1912.03817)\]. Techniques like SISA training have been introduced to expedite the unlearning process by strategically limiting the influence of specific data points during training, offering improvements over traditional retraining methods \[[21](http://arxiv.org/abs/1912.03817)\]. These approaches are especially beneficial for stateful algorithms such as stochastic gradient descent, where unlearning can be computationally intensive \[[21](http://arxiv.org/abs/1912.03817)\]. Additionally, research has highlighted the need for robust evaluation practices to ensure that unlearning is both effective and verifiable, with recent studies proposing multiple metrics to address the limitations of single-evaluation approaches \[[28](http://arxiv.org/abs/2403.13682)\]. Surveys in this area also emphasize the importance of understanding the trade-offs between privacy and system performance, particularly in decentralized environments where federated learning is employed \[[30](https://www.semanticscholar.org/paper/8b4103d09a1cb32ffb4dfba90e04698ea553a80c)\]. Overall, these works underscore the growing interest in developing practical and efficient solutions for data removal in machine learning systems.
|    | reference                                                                                                   | date     | key idea/summary                                                                                                                                                                                                                                 |
|----|-------------------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Machine Unlearning](http://arxiv.org/abs/1912.03817)                                                       | 12/09/19 | SISA training is a framework that accelerates the unlearning process in machine learning by limiting the influence of specific data points during training, thereby reducing computational overhead and improving efficiency in data governance. |
|  1 | [Threats, Attacks, and Defenses in Machine Unlearning: A Survey](http://arxiv.org/abs/2403.13682)           | 03/20/24 | This survey aims to address the lack of a comprehensive review on machine unlearning by categorizing threats, attacks, and defenses, providing insights for future research and practical implementations.                                       |
|  2 | [Machine unlearning survey](https://www.semanticscholar.org/paper/8b4103d09a1cb32ffb4dfba90e04698ea553a80c) | 12/16/22 | The paper provides a survey of machine unlearning techniques, discussing existing approaches with approximate and exact guarantees, and their merits and drawbacks.                                                                              |
### <a id='category-selective-forgetting-approaches'></a>Selective Forgetting Approaches: 2 papers found.
Context: 
	Document 1: [Snippet]: «The right to be forgotten states that a data owner has the right to erase their data from an entity storing it. In the context of machine learning (ML), the right to be forgotten requires an ML model owner to remove the data owner's data from the training set used to build the ML model, a process known as machine unlearning. While originally designed to protect the privacy of the data owner, we argue that machine unlearning may leave some imprint of the data in the ML model and thus create unintended privacy risks. In this paper, we perform the first study on investigating the unintended information leakage caused by machine unlearning. We propose a novel membership inference attack that leverages the different outputs of an ML model's two versions to infer whether a target sample is part of the training set of the original model but out of the training set of the corresponding unlearned model. Our experiments demonstrate that the proposed membership inference attack achieves strong performance. More importantly, we show that our attack in multiple cases outperforms the classical membership inference attack on the original ML model, which indicates that machine unlearning can have counterproductive effects on privacy. We notice that the privacy degradation is especially significant for well-generalized ML models where classical membership inference does not perform well. We further investigate four mechanisms to mitigate the newly discovered privacy risks and show that releasing the predicted label only, temperature scaling, and differential privacy are effective.»
[_citation_number]: «23»
[Category]: «Selective Forgetting Approaches»

	Document 2: [Snippet]: «Machine unlearning has become an important area of research due to an increasing need for machine learning (ML) applications to comply with the emerging data privacy regulations. It facilitates the provision for removal of certain set or class of data from an already trained ML model without requiring retraining from scratch. Recently, several efforts have been put in to make unlearning to be effective and efficient. We propose a novel machine unlearning method by exploring the utility of competent and incompetent teachers in a student-teacher framework to induce forgetfulness. The knowledge from the competent and incompetent teachers is selectively transferred to the student to obtain a model that doesn't contain any information about the forget data. We experimentally show that this method generalizes well, is fast and effective. Furthermore, we introduce the zero retrain forgetting (ZRF) metric to evaluate any unlearning method. Unlike the existing unlearning metrics, the ZRF score does not depend on the availability of the expensive retrained model. This makes it useful for analysis of the unlearned model after deployment as well. We present results of experiments conducted for random subset forgetting and class forgetting on various deep networks and across different application domains. Code is at: https://github.com/vikram2000b/bad-teaching- unlearning»
[_citation_number]: «29»
[Category]: «Selective Forgetting Approaches»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-19T07:23:46+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2310.20448)\]. Further details \[[6](https://www.semanticscholar.org/paper/39da2d48f2132b919405e3bb6df6ece44ac6e15a)\]\[[7](https://www.semanticscholar.org/paper/06edb1f6eadb6c141d720fcca4c854578dc5d670)\]\[[8](http://arxiv.org/abs/2205.12709)\]\[[9](http://arxiv.org/abs/2209.02299)\]\[[10](http://arxiv.org/abs/2401.05146)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: This paper reports on findings from a comparative study on the effectiveness
and efficiency of federated unlearning strategies within Federated Online
Learning to Rank (FOLTR), with specific attention to systematically analysing
the unlearning capabilities of methods in a verifiable manner.
  Federated approaches to ranking of search results have recently garnered
attention to address users privacy concerns. In FOLTR, privacy is safeguarded
by collaboratively training ranking models across decentralized data sources,
preserving individual user data while optimizing search results based on
implicit feedback, such as clicks.
  Recent legislation introduced across numerous countries is establishing the
so called "the right to be forgotten", according to which services based on
machine learning models like those in FOLTR should provide capabilities that
allow users to remove their own data from those used to train models. This has
sparked the development of unlearning methods, along with evaluation practices
to measure whether unlearning of a user data successfully occurred. Current
evaluation practices are however often controversial, necessitating the use of
multiple metrics for a more comprehensive assessment -- but previous proposals
of unlearning methods only used single evaluation metrics.
  This paper addresses this limitation: our study rigorously assesses the
effectiveness of unlearning strategies in managing both under-unlearning and
over-unlearning scenarios using adapted, and newly proposed evaluation metrics.
Thanks to our detailed analysis, we uncover the strengths and limitations of
five unlearning strategies, offering valuable insights into optimizing
federated unlearning to balance data privacy and system performance within
FOLTR. We publicly release our code and complete results at
https://github.com/Iris1026/Unlearning-for-FOLTR.git.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2310.20448)\]. Further details discussed in contexts \[[2](https://www.semanticscholar.org/paper/eadeffdec9fac8fd7f9aea732ca410eb082b7dcf)\]\[[7](https://www.semanticscholar.org/paper/06edb1f6eadb6c141d720fcca4c854578dc5d670)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Selective forgetting approaches have gained significant attention in the field of machine unlearning, particularly in the context of data privacy regulations such as the "right to be forgotten." These approaches aim to remove specific data from trained models without requiring full retraining, thereby improving efficiency \[[23](http://arxiv.org/abs/2005.02205)\]. For instance, recent methods have explored the use of student-teacher frameworks, where knowledge is selectively transferred to induce forgetfulness, ensuring the resulting model does not retain information about the data to be removed \[[29](http://arxiv.org/abs/2205.08096)\]. This is crucial for applications like federated learning, where models are trained across decentralized data sources, and users expect control over their data \[[23](http://arxiv.org/abs/2005.02205)\]. Additionally, new evaluation metrics, such as the zero retrain forgetting (ZRF) score, have been introduced to assess unlearning effectiveness without relying on expensive retrained models \[[29](http://arxiv.org/abs/2205.08096)\]. These advancements highlight the growing focus on balancing privacy preservation with model performance in unlearning strategies.
|    | reference                                                                                                                       | date     | key idea/summary                                                                                                                                                                                                                                                               |
|----|---------------------------------------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [When Machine Unlearning Jeopardizes Privacy](http://arxiv.org/abs/2005.02205)                                                  | 05/05/20 | This paper investigates the unintended privacy risks of machine unlearning, proposing a novel membership inference attack that demonstrates privacy degradation and suggests mitigation strategies like differential privacy.                                                  |
|  1 | [Can Bad Teaching Induce Forgetting? Unlearning in Deep Networks using an Incompetent Teacher](http://arxiv.org/abs/2205.08096) | 05/17/22 | The paper proposes a novel machine unlearning method using competent and incompetent teachers in a student-teacher framework to effectively remove specific data from a trained model without retraining, and introduces the ZRF metric for evaluating unlearning performance. |
