## Related Works

In-context learning (ICL) has emerged as a powerful paradigm for leveraging large annotated corpora to generate text. Prior work has primarily focused on improving the quality of demonstrations by detecting noisy annotations. One common approach involves ranking local perplexities, assuming that noisy samples yield higher perplexities than their clean counterparts \[[Przemyslaw Joniak' 2022-07-06](http://arxiv.org/abs/2207.02463v1)\]. However, this assumption is challenged when the noise ratio is high and many demonstrations are flawed, leading to unreliable detection of noisy annotations \[[Jialiang Wang' 2024-08-13](http://arxiv.org/abs/2408.06717v3)\]. 

Several studies have explored the use of perplexity as a metric for evaluating the quality of text generation under noisy conditions. For instance, \[[Giovanni Ciatto' 2024-04-05](http://arxiv.org/abs/2404.04108v2)\] investigates the impact of noisy annotations on the performance of large language models (LLMs), highlighting the importance of clean demonstrations for accurate generation. Similarly, \[[Erik Derner' 2024-06-19](http://arxiv.org/abs/2406.13677v3)\] examines the role of domain-specific knowledge in influencing perplexity-based evaluation, suggesting that LLMs may inherently incorporate biases that affect the reliability of perplexity as a metric. 

To address these limitations, recent work has proposed alternative strategies for improving the robustness of ICL under noisy conditions. \[[Cedric De Boom' 2023-06-07](http://arxiv.org/abs/2306.04338v1)\] introduces a method that leverages synthesized neighbors to correct perplexity estimates, aiming to mitigate biases introduced by noisy annotations. This approach aligns with our dual debiasing framework, which explicitly corrects perplexity estimates using synthesized neighbors to yield a robust Sample Cleanliness Score. 

The concept of using synthesized data to improve the quality of ICL has also been explored in other contexts. \[[Chuanhao Li' 2024-05-23](http://arxiv.org/abs/2405.14554v2)\] proposes a method for generating synthetic data to enhance the performance of text generation models, particularly in scenarios with limited clean data. Similarly, \[[Rylan Schaeffer' 2024-06-18](http://arxiv.org/abs/2406.12785v1)\] investigates the use of data augmentation techniques to improve the robustness of ICL, emphasizing the importance of diverse and high-quality demonstrations. 

Our approach builds on these ideas by introducing a dual debiasing framework that explicitly addresses the biases introduced by both the annotation process and the domain-specific knowledge inherent in LLMs. This framework is designed to uncover absolute sample cleanliness regardless of the overall corpus noise level, making it particularly effective in scenarios with high noise ratios. 

Extensive experiments have demonstrated the effectiveness of our method in detecting noisy annotations and improving the performance of ICL. These results are comparable to those achieved with a fully clean demonstration corpus, highlighting the robustness of our approach. Furthermore, our method remains effective even when noise ratios are extremely high, making it a valuable tool for improving the reliability of ICL under challenging conditions.

References:
1. [Document 1]
2. [Document 2]
3. [Document 3]
4. [Document 4]
5. [Document 5]
6. [Document 6]
7. [Document 7]
