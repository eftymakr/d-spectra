## Related Works

In-context learning (ICL) has gained significant attention as a paradigm where large language models (LLMs) perform tasks by conditioning on a few input-output pairs, known as demonstrations \[[1](http://arxiv.org/abs/2205.12685)\]. Early studies highlighted the critical role of high-quality demonstrations in ICL, emphasizing that the performance of the model is highly dependent on the provided examples \[[5](http://arxiv.org/abs/2202.12837)\]. However, recent research has shown that the quality of these demonstrations can be compromised by noisy labels, which can significantly degrade the model's performance \[[6](http://arxiv.org/abs/2411.19581)\]. 

The assumption that noisy samples yield higher perplexity than clean ones has been widely used to detect noisy annotations \[[7](http://arxiv.org/abs/2405.17264)\]. However, this approach is not robust when the noise ratio is high and many demonstrations are flawed \[[6](http://arxiv.org/abs/2411.19581)\]. This limitation has led to the development of alternative methods that aim to improve the reliability of ICL under noisy conditions. For instance, the work by \[[7](http://arxiv.org/abs/2405.17264)\] proposed Local Perplexity Ranking (LPR), which replaces noisy candidates with their nearest neighbors in semantic space, thereby improving the performance of ICL on tasks with noisy annotations. This method is motivated by the analysis of perplexity deviation caused by noisy labels and decomposes perplexity into inherent and matching components \[[7](http://arxiv.org/abs/2405.17264)\].

Another line of research focuses on the role of demonstrations in ICL, showing that ground-truth labels are not always necessary for achieving good performance \[[5](http://arxiv.org/abs/2202.12837)\]. Instead, the format, distribution, and structure of the demonstrations play a crucial role in determining the model's ability to generalize \[[5](http://arxiv.org/abs/2202.12837)\]. This insight has led to the development of methods that aim to improve the effectiveness of ICL by focusing on the structure and content of the demonstrations rather than their correctness \[[5](http://arxiv.org/abs/2202.12837)\].

Furthermore, the importance of controlling the verbosity of prompt templates and the size of the language model has been identified as a key factor in achieving more noise-resilient ICL \[[1](http://arxiv.org/abs/2205.12685)\]. This highlights the need for a more nuanced understanding of how different components of the ICL setup affect the final performance \[[1](http://arxiv.org/abs/2205.12685)\].

In addition to improving the quality of demonstrations, recent studies have explored methods to enhance the robustness of ICL by introducing new decoding strategies. Contrastive decoding, for example, has been shown to improve reasoning tasks by maximizing the weighted difference in likelihood between strong and weak models \[[2](http://arxiv.org/abs/2309.09117)\]. This method has been applied to various tasks, including commonsense reasoning and math word problems, demonstrating its effectiveness in generating more accurate and coherent outputs \[[2](http://arxiv.org/abs/2309.09117)\].

Finally, the issue of label biases in ICL has also been addressed, with studies showing that certain design settings can bias the model towards specific predictions without reflecting a true understanding of the task \[[10](http://arxiv.org/abs/2305.19148)\]. To mitigate this, researchers have proposed methods that estimate and control for these biases, leading to improved performance across a range of tasks \[[10](http://arxiv.org/abs/2305.19148)\].

References:  
\[[1](http://arxiv.org/abs/2205.12685)\] Ground-Truth Labels Matter: A Deeper Look into Input-Label Demonstrations  
\[[2](http://arxiv.org/abs/2309.09117)\] Contrastive Decoding Improves Reasoning in Large Language Models  
\[[3](http://arxiv.org/abs/2305.04320)\] Unified Demonstration Retriever for In-Context Learning  
\[[4](http://arxiv.org/abs/2311.06668)\] In-context Vectors: Making In Context Learning More Effective and Controllable Through Latent Space Steering  
\[[5](http://arxiv.org/abs/2202.12837)\] Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?  
\[[6](http://arxiv.org/abs/2411.19581)\] In-Context Learning with Noisy Labels  
\[[7](http://arxiv.org/abs/2405.17264)\] On the Noise Robustness of In-Context Learning for Text Generation  
\[[8](http://arxiv.org/abs/2210.15097)\] Contrastive Decoding: Open-ended Text Generation as Optimization  
\[[9](http://arxiv.org/abs/2405.02750)\] Enhancing Contextual Understanding in Large Language Models through Contrastive Decoding  
\[[10](http://arxiv.org/abs/2305.19148)\] Mitigating Label Biases for In-context Learning
## Research papers
### Outline
- [Demonstration Quality and Structure [2 papers]](#category-demonstration-quality-and-structure)
- [Contrastive Decoding Techniques [3 papers]](#category-contrastive-decoding-techniques)
- [In-Context Learning (ICL) Frameworks [2 papers]](#category-in-context-learning-(icl)-frameworks)
- [Noise in Demonstrations and Its Impact [2 papers]](#category-noise-in-demonstrations-and-its-impact)
- [Label Biases in ICL [2 papers]](#category-label-biases-in-icl)

### <a id='category-demonstration-quality-and-structure'></a>Demonstration Quality and Structure: 2 papers found.
Context: 
	Document 1: [Category]: «Demonstration Quality and Structure»
[_citation_number]: «1»
[Snippet]: «Despite recent explosion of interests in in-context learning, the underlying
mechanism and the precise impact of the quality of demonstrations remain
elusive. Intuitively, ground-truth labels should have as much impact in
in-context learning (ICL) as supervised learning, but recent work reported that
the input-label correspondence is significantly less important than previously
thought. Intrigued by this counter-intuitive observation, we re-examine the
importance of ground-truth labels in in-context learning. With the introduction
of two novel metrics, namely Label-Correctness Sensitivity and Ground-truth
Label Effect Ratio (GLER), we were able to conduct quantifiable analysis on the
impact of ground-truth label demonstrations. Through extensive analyses, we
find that the correct input-label mappings can have varying impacts on the
downstream in-context learning performances, depending on the experimental
configuration. Through additional studies, we identify key components, such as
the verbosity of prompt templates and the language model size, as the
controlling factor to achieve more noise-resilient ICL.»

	Document 2: [Category]: «Demonstration Quality and Structure»
[_citation_number]: «5»
[Snippet]: «Large language models (LMs) are able to in-context learn -- perform a new
task via inference alone by conditioning on a few input-label pairs
(demonstrations) and making predictions for new inputs. However, there has been
little understanding of how the model learns and which aspects of the
demonstrations contribute to end task performance. In this paper, we show that
ground truth demonstrations are in fact not required -- randomly replacing
labels in the demonstrations barely hurts performance on a range of
classification and multi-chose tasks, consistently over 12 different models
including GPT-3. Instead, we find that other aspects of the demonstrations are
the key drivers of end task performance, including the fact that they provide a
few examples of (1) the label space, (2) the distribution of the input text,
and (3) the overall format of the sequence. Together, our analysis provides a
new way of understanding how and why in-context learning works, while opening
up new questions about how much can be learned from large language models
through inference alone.»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T06:44:48+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2305.04320)\]. Further details \[[6](http://arxiv.org/abs/2411.19581)\]\[[7](http://arxiv.org/abs/2405.17264)\]\[[8](http://arxiv.org/abs/2210.15097)\]\[[9](http://arxiv.org/abs/2405.02750)\]\[[10](http://arxiv.org/abs/2305.19148)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In context learning (ICL) relies heavily on high quality demonstrations drawn
from large annotated corpora. Existing approaches detect noisy annotations by
ranking local perplexities, presuming that noisy samples yield higher
perplexities than their clean counterparts. However, this assumption breaks
down when the noise ratio is high and many demonstrations are flawed. We
reexamine the perplexity based paradigm for text generation under noisy
annotations, highlighting two sources of bias in perplexity: the annotation
itself and the domain specific knowledge inherent in large language models
(LLMs). To overcome these biases, we introduce a dual debiasing framework that
uses synthesized neighbors to explicitly correct perplexity estimates, yielding
a robust Sample Cleanliness Score. This metric uncovers absolute sample
cleanliness regardless of the overall corpus noise level. Extensive experiments
demonstrate our method's superior noise detection capabilities and show that
its final ICL performance is comparable to that of a fully clean demonstration
corpus. Moreover, our approach remains robust even when noise ratios are
extremely high.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2305.04320)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2309.09117)\]\[[7](http://arxiv.org/abs/2405.17264)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Demonstration quality and structure play a critical role in in-context learning (ICL), with recent studies highlighting the nuanced impact of ground-truth labels and other demonstration features \[[1](http://arxiv.org/abs/2205.12685)\]. While intuitive assumptions suggest that accurate input-label mappings are essential for ICL, empirical findings challenge this view, showing that ground-truth labels may not be as crucial as previously thought \[[1](http://arxiv.org/abs/2205.12685)\]. Instead, other aspects of the demonstrations, such as the label space, input distribution, and formatting, significantly influence task performance \[[5](http://arxiv.org/abs/2202.12837)\]. This suggests that ICL relies on more than just correct labels, as models can still perform well even with noisy or randomly altered labels, provided the demonstrations provide useful structural and contextual information \[[5](http://arxiv.org/abs/2202.12837)\]. These insights underscore the importance of understanding how different components of the demonstration affect learning outcomes, particularly in the presence of noisy or imperfect data. The variability in the impact of ground-truth labels also implies that factors like prompt verbosity and model size may play a key role in determining the robustness of ICL \[[1](http://arxiv.org/abs/2205.12685)\]. Thus, the design of demonstration sets must consider not only label accuracy but also the broader structural and contextual elements that guide the model’s inferences.
|    | reference                                                                                                        |   date | key idea/summary                                                                                                                                                                                                               |
|----|------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Ground-Truth Labels Matter: A Deeper Look into Input-Label
  Demonstrations](http://arxiv.org/abs/2205.12685)   |    nan | The paper investigates the impact of ground-truth labels in in-context learning, introducing new metrics to quantify their influence and identifies factors like prompt verbosity and model size that affect noise resilience. |
|  1 | [Rethinking the Role of Demonstrations: What Makes In-Context Learning
  Work?](http://arxiv.org/abs/2202.12837) |    nan | In-context learning in large language models is effective even with randomly replaced labels, suggesting that the structure and format of demonstrations, rather than ground truth labels, are key to task performance.        |
### <a id='category-contrastive-decoding-techniques'></a>Contrastive Decoding Techniques: 3 papers found.
Contrastive decoding techniques have emerged as a promising approach to improve the quality and reasoning capabilities of language models during text generation. These methods leverage the difference in likelihood between a large, expert model and a smaller, amateur model to guide the decoding process, ensuring that outputs are both plausible and aligned with strong model predictions \[[2](http://arxiv.org/abs/2309.09117)\]. This approach is particularly effective in preventing issues such as repetition, incoherence, and failure to integrate input context, which are common in traditional decoding strategies like greedy decoding or nucleus sampling \[[2](http://arxiv.org/abs/2309.09117)\]. By incorporating a plausibility constraint, contrastive decoding not only enhances the coherence of generated text but also improves performance on reasoning tasks, such as commonsense reasoning and mathematical problem-solving \[[1](http://arxiv.org/abs/2205.12685)\]. Furthermore, the technique is training-free and adaptable across different model scales, making it a versatile tool for improving the reliability of language model outputs \[[8](http://arxiv.org/abs/2210.15097)\]. Recent work has also extended contrastive decoding to address challenges in open-domain question answering by integrating adversarial irrelevant passages as negative samples, further enhancing context grounding during generation \[[9](http://arxiv.org/abs/2405.02750)\]. These advancements highlight the growing importance of contrastive decoding in refining the capabilities of large language models for a wide range of applications.
|    | reference                                                                                                                     |   date | key idea/summary                                                                                                                                                                                                                                                     |
|----|-------------------------------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Contrastive Decoding Improves Reasoning in Large Language Models](http://arxiv.org/abs/2309.09117)                           |    nan | Contrastive Decoding is a simple, training-free text generation method that significantly improves reasoning tasks by maximizing the likelihood difference between strong and weak models, outperforming existing methods like greedy decoding and nucleus sampling. |
|  1 | [Contrastive Decoding: Open-ended Text Generation as Optimization](http://arxiv.org/abs/2210.15097)                           |    nan | Contrastive decoding (CD) is a decoding approach that improves text generation quality by optimizing a contrastive objective between a large and a small language model, ensuring plausible and high-quality outputs without additional training.                    |
|  2 | [Enhancing Contextual Understanding in Large Language Models through
  Contrastive Decoding](http://arxiv.org/abs/2405.02750) |    nan | The study introduces a novel approach using contrastive decoding with adversarial irrelevant passages to improve context grounding in large language models during open-domain question answering, without requiring further training.                               |
### <a id='category-in-context-learning-(icl)-frameworks'></a>In-Context Learning (ICL) Frameworks: 2 papers found.
In-Context Learning (ICL) has gained significant attention as a paradigm where language models leverage demonstrations to improve performance on new tasks \[[3](http://arxiv.org/abs/2305.04320)\]. Recent works have focused on improving the retrieval of relevant demonstrations, as the effectiveness of ICL is highly dependent on the quality and relevance of these examples \[[3](http://arxiv.org/abs/2305.04320)\]. However, traditional approaches often require task-specific retrievers, which are difficult to generalize across different tasks and incur high computational costs \[[3](http://arxiv.org/abs/2305.04320)\]. To address these limitations, researchers have proposed unified frameworks such as the Unified Demonstration Retriever (UDR), which enables a single model to handle a wide range of tasks by casting training signals into a unified list-wise ranking formulation \[[3](http://arxiv.org/abs/2305.04320)\]. Additionally, alternative approaches like in-context vectors (ICV) have been introduced to enhance the efficiency and controllability of ICL by modifying the latent states of the model using synthesized vectors derived from demonstration examples \[[4](http://arxiv.org/abs/2311.06668)\]. These methods aim to overcome the limitations of traditional in-context learning, such as the difficulty in controlling performance and the inefficiency of using long prompts \[[4](http://arxiv.org/abs/2311.06668)\].
|    | reference                                                                                                                                         |   date | key idea/summary                                                                                                                                                                                           |
|----|---------------------------------------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Unified Demonstration Retriever for In-Context Learning](http://arxiv.org/abs/2305.04320)                                                        |    nan | UDR is a unified demonstration retriever that can handle a wide range of tasks by using a multi-task list-wise ranking training framework, outperforming baselines across 30+ tasks and various scenarios. |
|  1 | [In-context Vectors: Making In Context Learning More Effective and
  Controllable Through Latent Space Steering](http://arxiv.org/abs/2311.06668) |    nan | The paper proposes an alternative approach to in-context learning by using in-context vectors (ICV) to improve task adaptation, control, efficiency, and performance across various tasks.                 |
### <a id='category-noise-in-demonstrations-and-its-impact'></a>Noise in Demonstrations and Its Impact: 2 papers found.
In the context of noise in demonstrations and its impact on in-context learning, recent studies have highlighted the critical role of demonstration quality in the performance of large language models (LLMs) \[[1](http://arxiv.org/abs/2205.12685)\]. While some works claim robustness to noisy annotations in text classification, others have shown that noisy labels can significantly degrade performance in text generation tasks \[[2](http://arxiv.org/abs/2309.09117)\]. This issue is exacerbated when the noise ratio is high, leading to flawed demonstrations that undermine the effectiveness of in-context learning \[[1](http://arxiv.org/abs/2205.12685)\]. To address this, researchers have proposed methods such as Local Perplexity Ranking (LPR), which leverages semantic space analysis to replace noisy candidates with more reliable, clean examples \[[2](http://arxiv.org/abs/2309.09117)\]. This approach aims to decouple the matching perplexity caused by noisy labels, thereby preserving the effectiveness of demonstration selection while mitigating performance degradation \[[2](http://arxiv.org/abs/2309.09117)\]. The challenge of handling noisy labels in in-context learning has thus become a focal point, with new methods and baselines being developed to ensure robustness in real-world scenarios where label corruption is inevitable \[[1](http://arxiv.org/abs/2205.12685)\].
|    | reference                                                                                             |   date | key idea/summary                                                                                                                                                                                                       |
|----|-------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [In-Context Learning with Noisy Labels](http://arxiv.org/abs/2411.19581)                              |    nan | The paper introduces a new task and method for in-context learning that addresses the issue of noisy labels in task demonstrations, aiming to improve robustness against performance degradation caused by such noise. |
|  1 | [On the Noise Robustness of In-Context Learning for Text Generation](http://arxiv.org/abs/2405.17264) |    nan | The paper introduces Local Perplexity Ranking (LPR), a method to improve in-context learning performance in text generation by replacing noisy demonstrations with cleaner ones using semantic space analysis.         |
### <a id='category-label-biases-in-icl'></a>Label Biases in ICL: 2 papers found.
Context: 
	Document 1: [Category]: «Label Biases in ICL»
[_citation_number]: «10»
[Snippet]: «Various design settings for in-context learning (ICL), such as the choice and
order of the in-context examples, can bias a model toward a particular
prediction without being reflective of an understanding of the task. While many
studies discuss these design choices, there have been few systematic
investigations into categorizing them and mitigating their impact. In this
work, we define a typology for three types of label biases in ICL for text
classification: vanilla-label bias, context-label bias, and domain-label bias
(which we conceptualize and detect for the first time).
  Our analysis demonstrates that prior label bias calibration methods fall
short of addressing all three types of biases. Specifically, domain-label bias
restricts LLMs to random-level performance on many tasks regardless of the
choice of in-context examples. To mitigate the effect of these biases, we
propose a simple bias calibration method that estimates a language model's
label bias using random in-domain words from the task corpus. After controlling
for this estimated bias when making predictions, our novel domain-context
calibration significantly improves the ICL performance of GPT-J and GPT-3 on a
wide range of tasks. The gain is substantial on tasks with large domain-label
bias (up to 37% in Macro-F1). Furthermore, our results generalize to models
with different scales, pretraining methods, and manually-designed task
instructions, showing the prevalence of label biases in ICL.»

	Document 2: [Category]: «Label Biases in ICL»
[_citation_number]: «11»
[Snippet]: «GPT-3 can perform numerous tasks when provided a natural language prompt that
contains a few training examples. We show that this type of few-shot learning
can be unstable: the choice of prompt format, training examples, and even the
order of the training examples can cause accuracy to vary from near chance to
near state-of-the-art. We demonstrate that this instability arises from the
bias of language models towards predicting certain answers, e.g., those that
are placed near the end of the prompt or are common in the pre-training data.
To mitigate this, we first estimate the model's bias towards each answer by
asking for its prediction when given the training prompt and a content-free
test input such as "N/A". We then fit calibration parameters that cause the
prediction for this input to be uniform across answers. On a diverse set of
tasks, this contextual calibration procedure substantially improves GPT-3 and
GPT-2's average accuracy (up to 30.0% absolute) and reduces variance across
different choices of the prompt.»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-31T06:44:48+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2305.04320)\]. Further details \[[6](http://arxiv.org/abs/2411.19581)\]\[[7](http://arxiv.org/abs/2405.17264)\]\[[8](http://arxiv.org/abs/2210.15097)\]\[[9](http://arxiv.org/abs/2405.02750)\]\[[10](http://arxiv.org/abs/2305.19148)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In context learning (ICL) relies heavily on high quality demonstrations drawn
from large annotated corpora. Existing approaches detect noisy annotations by
ranking local perplexities, presuming that noisy samples yield higher
perplexities than their clean counterparts. However, this assumption breaks
down when the noise ratio is high and many demonstrations are flawed. We
reexamine the perplexity based paradigm for text generation under noisy
annotations, highlighting two sources of bias in perplexity: the annotation
itself and the domain specific knowledge inherent in large language models
(LLMs). To overcome these biases, we introduce a dual debiasing framework that
uses synthesized neighbors to explicitly correct perplexity estimates, yielding
a robust Sample Cleanliness Score. This metric uncovers absolute sample
cleanliness regardless of the overall corpus noise level. Extensive experiments
demonstrate our method's superior noise detection capabilities and show that
its final ICL performance is comparable to that of a fully clean demonstration
corpus. Moreover, our approach remains robust even when noise ratios are
extremely high.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2305.04320)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2309.09117)\]\[[7](http://arxiv.org/abs/2405.17264)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Label biases in in-context learning (ICL) have been identified as a critical challenge, where design choices in the selection and ordering of in-context examples can lead to biased predictions without reflecting true task understanding \[[10](http://arxiv.org/abs/2305.19148)\]. This issue is further compounded by the presence of three distinct types of label biases: vanilla-label bias, context-label bias, and domain-label bias \[[10](http://arxiv.org/abs/2305.19148)\]. Vanilla-label bias occurs when the model is biased toward certain labels due to the training examples, while context-label bias is influenced by the position or structure of the examples within the prompt \[[11](http://arxiv.org/abs/2102.09690)\]. Domain-label bias, which is particularly impactful, restricts models to random-level performance on various tasks, regardless of the choice of in-context examples \[[10](http://arxiv.org/abs/2305.19148)\]. Prior methods for addressing label bias have not effectively mitigated all three types of biases, especially domain-label bias, which can severely limit the performance of large language models (LLMs) \[[10](http://arxiv.org/abs/2305.19148)\]. To address these challenges, researchers have proposed calibration methods that estimate and correct for these biases by leveraging random in-domain words from the task corpus \[[10](http://arxiv.org/abs/2305.19148)\]. These approaches have shown significant improvements in ICL performance, particularly on tasks with high domain-label bias, with gains up to 37% in Macro-F1 \[[10](http://arxiv.org/abs/2305.19148)\]. Additionally, these calibration techniques have demonstrated robustness across different model scales and pretraining methods, highlighting the widespread prevalence of label biases in ICL \[[10](http://arxiv.org/abs/2305.19148)\].
|    | reference                                                                                                  |   date | key idea/summary                                                                                                                                                                                                       |
|----|------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Mitigating Label Biases for In-context Learning](http://arxiv.org/abs/2305.19148)                         |    nan | This work identifies and mitigates three types of label biases in in-context learning (ICL) for text classification, demonstrating significant performance improvements by calibrating for domain-label bias.          |
|  1 | [Calibrate Before Use: Improving Few-Shot Performance of Language Models](http://arxiv.org/abs/2102.09690) |    nan | The paper demonstrates that few-shot learning in language models like GPT-3 can be unstable due to biases in predicting answers, and proposes a contextual calibration method to improve accuracy and reduce variance. |
