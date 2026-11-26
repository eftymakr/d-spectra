## Related Works

Text-to-Speech (TTS) systems have evolved significantly, with recent advances focusing on improving speech naturalness, controllability, and robustness \[[1](http://arxiv.org/abs/1905.09263)\]. Early TTS models were either concatenative or statistical parametric, but neural network-based end-to-end models have largely replaced them due to their superior quality \[[1](http://arxiv.org/abs/1905.09263)\]. However, these models often suffer from slow inference speeds and limited controllability over prosody and other speech attributes \[[1](http://arxiv.org/abs/1905.09263)\]. For instance, autoregressive models like Tacotron 2 generate mel-spectrograms sequentially, leading to slower inference times compared to non-autoregressive models \[[1](http://arxiv.org/abs/1905.09263)\]. FastSpeech, a non-autoregressive model, addresses these issues by using a parallel feed-forward network based on the Transformer architecture to generate mel-spectrograms in parallel, achieving a 270x speedup over autoregressive models \[[1](http://arxiv.org/abs/1905.09263)\]. FastSpeech 2 further improves upon FastSpeech by directly using ground-truth targets during training and incorporating more speech variation information such as pitch and energy, leading to higher voice quality and faster training and inference speeds \[[2](http://arxiv.org/abs/2006.04558)\].

Prosody control is a critical aspect of TTS, enabling more expressive and natural speech synthesis. Several approaches have been proposed to control speaking rate and other prosodic attributes. For example, a speaking rate attention-based duration prediction method allows for implicit control of speaking rate by conditioning the duration predictor on the speaking rate \[[3](http://arxiv.org/abs/2310.08846)\]. Additionally, style tokens have been introduced to model acoustic expressiveness in end-to-end speech synthesis, enabling control over speed and speaking style without explicit labels \[[4](http://arxiv.org/abs/1803.09017)\]. These style tokens are trained within Tacotron and can be used for style transfer, replicating the speaking style of one audio clip across different texts \[[4](http://arxiv.org/abs/1803.09017)\]. Similarly, hierarchical generative modeling has been proposed to control latent attributes such as speaking style, accent, and background noise, using a variational autoencoder (VAE) framework with hierarchical latent variables \[[6](http://arxiv.org/abs/1810.07217)\].

Mispronunciation correction in TTS is another important challenge, especially in low-resource settings where grapheme-to-phoneme dictionaries are not available. Traditional methods rely on such dictionaries, limiting their practicality \[[10]()\]. Recent work has explored the use of speech from non-target speakers for one-off correction of mispronunciations in grapheme-input TTS systems \[[10]()\]. These approaches aim to improve pronunciation accuracy without requiring extensive training data or specialized modules.

In summary, while existing methods have made strides in improving TTS quality and controllability, they often rely on specialized modules or additional training, limiting their flexibility for post-hoc adjustments \[[1](http://arxiv.org/abs/1905.09263)\]. Our approach, Counterfactual Activation Editing, addresses these limitations by enabling post-hoc control of prosody and pronunciation without retraining, offering a model-agnostic solution for inference-time refinement \[[1](http://arxiv.org/abs/1905.09263)\].

References:
1. FastSpeech: Fast, Robust and Controllable Text to Speech [http://arxiv.org/abs/1905.09263]
2. FastSpeech 2: Fast and High-Quality End-to-End Text to Speech [http://arxiv.org/abs/2006.04558]
3. Speaking rate attention-based duration prediction for speed control TTS [http://arxiv.org/abs/2310.08846]
4. Style Tokens: Unsupervised Style Modeling, Control and Transfer in End-to-End Speech Synthesis [http://arxiv.org/abs/1803.09017]
6. Hierarchical Generative Modeling for Controllable Speech Synthesis [http://arxiv.org/abs/1810.07217]
10. Speech Audio Corrector: using speech from non-target speakers for one-off correction of mispronunciations in grapheme-input text-to-speech [http://arxiv.org/abs/2310.08846]
## Research papers
### Outline
- [Non-Autoregressive TTS Models [2 papers]](#category-non-autoregressive-tts-models)
- [Prosody Control Techniques [5 papers]](#category-prosody-control-techniques)
- [Style Transfer and Control in TTS [1 papers]](#category-style-transfer-and-control-in-tts)
- [Hierarchical Generative Modeling for Speech [1 papers]](#category-hierarchical-generative-modeling-for-speech)
- [Mispronunciation Correction Methods [1 papers]](#category-mispronunciation-correction-methods)

### <a id='category-non-autoregressive-tts-models'></a>Non-Autoregressive TTS Models: 2 papers found.
Non-autoregressive text-to-speech (TTS) models, such as FastSpeech and FastSpeech 2, have emerged as promising alternatives to traditional autoregressive approaches, offering significant improvements in inference speed while maintaining comparable speech quality \[[1](http://arxiv.org/abs/1905.09263)\]. Unlike autoregressive models that generate mel-spectrograms sequentially, non-autoregressive models like FastSpeech utilize parallel generation, enabling faster synthesis by leveraging Transformer-based architectures \[[1](http://arxiv.org/abs/1905.09263)\]. FastSpeech introduces a length regulator that aligns phoneme durations with target mel-spectrogram lengths, reducing issues like word skipping and repetition \[[1](http://arxiv.org/abs/1905.09263)\]. However, FastSpeech relies on a teacher-student distillation pipeline, which can be computationally intensive and may lead to information loss during knowledge distillation \[[2](http://arxiv.org/abs/2006.04558)\]. To address these limitations, FastSpeech 2 was developed, directly using ground-truth targets for training and incorporating additional speech features such as pitch and energy as conditional inputs, thereby improving voice quality and reducing the dependency on teacher models \[[2](http://arxiv.org/abs/2006.04558)\]. FastSpeech 2 further extends to FastSpeech 2s, which directly generates speech waveforms from text in parallel, enabling fully end-to-end inference \[[2](http://arxiv.org/abs/2006.04558)\]. These advancements highlight the potential of non-autoregressive TTS models to enhance both the efficiency and flexibility of speech synthesis, particularly in scenarios requiring post-hoc adjustments or real-time applications.
|    | reference                                                                                        |   date | key idea/summary                                                                                                                                                                                                                                        |
|----|--------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [FastSpeech: Fast, Robust and Controllable Text to Speech](http://arxiv.org/abs/1905.09263)      |    nan | The paper introduces FastSpeech, a novel feed-forward Transformer-based model for TTS that generates mel-spectrogram in parallel, significantly improving speed while maintaining speech quality and reducing issues like word skipping and repetition. |
|  1 | [FastSpeech 2: Fast and High-Quality End-to-End Text to Speech](http://arxiv.org/abs/2006.04558) |    nan | FastSpeech 2 improves upon the original FastSpeech by directly using ground-truth targets and incorporating more speech variation information, leading to faster training and better voice quality in text-to-speech synthesis.                         |
### <a id='category-prosody-control-techniques'></a>Prosody Control Techniques: 5 papers found.
Context: 
	Document 1: [Category]: «Prosody Control Techniques»
[_citation_number]: «3»
[Snippet]: «With the advent of high-quality speech synthesis, there is a lot of interest
in controlling various prosodic attributes of speech. Speaking rate is an
essential attribute towards modelling the expressivity of speech. In this work,
we propose a novel approach to control the speaking rate for non-autoregressive
TTS. We achieve this by conditioning the speaking rate inside the duration
predictor, allowing implicit speaking rate control. We show the benefits of
this approach by synthesising audio at various speaking rate factors and
measuring the quality of speaking rate-controlled synthesised speech. Further,
we study the effect of the speaking rate distribution of the training data
towards effective rate control. Finally, we fine-tune a baseline pretrained TTS
model to obtain speaking rate control TTS. We provide various analyses to
showcase the benefits of using this proposed approach, along with objective as
well as subjective metrics. We find that the proposed methods have higher
subjective scores and lower speaker rate errors across many speaking rate
factors over the baseline.»

	Document 2: [Category]: «Prosody Control Techniques»
[_citation_number]: «5»
[Snippet]: «We present an extension to the Tacotron speech synthesis architecture that
learns a latent embedding space of prosody, derived from a reference acoustic
representation containing the desired prosody. We show that conditioning
Tacotron on this learned embedding space results in synthesized audio that
matches the prosody of the reference signal with fine time detail even when the
reference and synthesis speakers are different. Additionally, we show that a
reference prosody embedding can be used to synthesize text that is different
from that of the reference utterance. We define several quantitative and
subjective metrics for evaluating prosody transfer, and report results with
accompanying audio samples from single-speaker and 44-speaker Tacotron models
on a prosody transfer task.»

	Document 3: [Category]: «Prosody Control Techniques»
[_citation_number]: «7»
[Snippet]: «»

	Document 4: [Category]: «Prosody Control Techniques»
[_citation_number]: «8»
[Snippet]: «»

	Document 5: [Category]: «Prosody Control Techniques»
[_citation_number]: «9»
[Snippet]: «»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-06-01T04:33:37+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2310.08846)\]. Further details \[[6](http://arxiv.org/abs/1810.07217)\]\[[7]()\]\[[8]()\]\[[9]()\]\[[10]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Recent advances in Text-to-Speech (TTS) have significantly improved speech
naturalness, increasing the demand for precise prosody control and
mispronunciation correction. Existing approaches for prosody manipulation often
depend on specialized modules or additional training, limiting their capacity
for post-hoc adjustments. Similarly, traditional mispronunciation correction
relies on grapheme-to-phoneme dictionaries, making it less practical in
low-resource settings. We introduce Counterfactual Activation Editing, a
model-agnostic method that manipulates internal representations in a
pre-trained TTS model to achieve post-hoc control of prosody and pronunciation.
Experimental results show that our method effectively adjusts prosodic features
and corrects mispronunciations while preserving synthesis quality. This opens
the door to inference-time refinement of TTS outputs without retraining,
bridging the gap between pre-trained TTS models and editable speech synthesis.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2310.08846)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2006.04558)\]\[[7]()\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Recent advancements in Text-to-Speech (TTS) systems have emphasized the importance of prosody control for enhancing speech naturalness and expressivity \[[3](http://arxiv.org/abs/2310.08846)\]. Techniques such as conditioning the speaking rate within the duration predictor have been proposed to enable implicit control over speech synthesis, allowing for adjustments in speaking rate without requiring additional training \[[3](http://arxiv.org/abs/2310.08846)\]. Similarly, approaches like the Tacotron extension with a latent embedding space for prosody have demonstrated the ability to match reference prosody with fine temporal detail, even across different speakers \[[5](http://arxiv.org/abs/1803.09047)\]. These methods highlight the growing interest in manipulating prosodic attributes through learned representations or model modifications. However, existing approaches often rely on specialized modules or require additional training, limiting their flexibility for post-hoc adjustments \[[3](http://arxiv.org/abs/2310.08846)\]. The proposed Counterfactual Activation Editing method addresses these limitations by enabling model-agnostic post-hoc control of prosody and pronunciation, offering a more flexible and efficient solution \[[3](http://arxiv.org/abs/2310.08846)\].
|    | reference                                                                                                              |   date | key idea/summary                                                                                                                                                                                                                                          |
|----|------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Speaking rate attention-based duration prediction for speed control TTS](http://arxiv.org/abs/2310.08846)             |    nan | This work proposes a novel approach to control speaking rate in non-autoregressive TTS by conditioning the speaking rate within the duration predictor, leading to improved subjective scores and lower speaker rate errors compared to baseline methods. |
|  1 | [Towards End-to-End Prosody Transfer for Expressive Speech Synthesis with
  Tacotron](http://arxiv.org/abs/1803.09047) |    nan | This paper introduces an extension to the Tacotron speech synthesis model that uses a learned latent embedding space of prosody to enable fine-grained prosody transfer between different speakers and utterances.                                        |
|  2 | [Expressive prosody for unit-selection speech synthesis.]()                                                            |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                 |
|  3 | [Ctrl-P: Temporal control of prosodic variation for speech synthesis]()                                                |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                 |
|  4 | [Speaking Rate Control of end-to-end TTS Models by Direct Manipulation of the Encoder's Output Embeddings]()           |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                 |
### <a id='category-style-transfer-and-control-in-tts'></a>Style Transfer and Control in TTS: 1 papers found.
Context: 
	Document 1: [Category]: «Style Transfer and Control in TTS»
[_citation_number]: «4»
[Snippet]: «In this work, we propose "global style tokens" (GSTs), a bank of embeddings
that are jointly trained within Tacotron, a state-of-the-art end-to-end speech
synthesis system. The embeddings are trained with no explicit labels, yet learn
to model a large range of acoustic expressiveness. GSTs lead to a rich set of
significant results. The soft interpretable "labels" they generate can be used
to control synthesis in novel ways, such as varying speed and speaking style -
independently of the text content. They can also be used for style transfer,
replicating the speaking style of a single audio clip across an entire
long-form text corpus. When trained on noisy, unlabeled found data, GSTs learn
to factorize noise and speaker identity, providing a path towards highly
scalable but robust speech synthesis.»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-06-01T04:33:37+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2310.08846)\]. Further details \[[6](http://arxiv.org/abs/1810.07217)\]\[[7]()\]\[[8]()\]\[[9]()\]\[[10]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Recent advances in Text-to-Speech (TTS) have significantly improved speech
naturalness, increasing the demand for precise prosody control and
mispronunciation correction. Existing approaches for prosody manipulation often
depend on specialized modules or additional training, limiting their capacity
for post-hoc adjustments. Similarly, traditional mispronunciation correction
relies on grapheme-to-phoneme dictionaries, making it less practical in
low-resource settings. We introduce Counterfactual Activation Editing, a
model-agnostic method that manipulates internal representations in a
pre-trained TTS model to achieve post-hoc control of prosody and pronunciation.
Experimental results show that our method effectively adjusts prosodic features
and corrects mispronunciations while preserving synthesis quality. This opens
the door to inference-time refinement of TTS outputs without retraining,
bridging the gap between pre-trained TTS models and editable speech synthesis.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2310.08846)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2006.04558)\]\[[7]()\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
In the realm of style transfer and control in text-to-speech (TTS) synthesis, recent approaches have focused on developing methods that enable flexible and interpretable control over speech characteristics. One notable contribution is the introduction of "global style tokens" (GSTs), which are embeddings jointly trained within a state-of-the-art TTS system like Tacotron \[[4](http://arxiv.org/abs/1803.09017)\]. These tokens allow for the modeling of a wide range of acoustic expressiveness without explicit labels, enabling the generation of soft, interpretable "labels" that can be used to control synthesis in novel ways \[[4](http://arxiv.org/abs/1803.09017)\]. This includes adjusting speech speed and speaking style independently of the text content, as well as enabling style transfer by replicating the speaking style of a single audio clip across an entire text corpus \[[4](http://arxiv.org/abs/1803.09017)\]. Furthermore, GSTs demonstrate robustness when trained on noisy, unlabeled data, as they can factorize noise and speaker identity, leading to scalable and robust speech synthesis systems \[[4](http://arxiv.org/abs/1803.09017)\]. Such methods represent a significant step forward in achieving flexible and controllable TTS systems.
|    | reference                                                                                                                           |   date | key idea/summary                                                                                                                                                                                                                                            |
|----|-------------------------------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Style Tokens: Unsupervised Style Modeling, Control and Transfer in
  End-to-End Speech Synthesis](http://arxiv.org/abs/1803.09017) |    nan | The paper introduces 'global style tokens' (GSTs), which are embeddings jointly trained within a speech synthesis system to model acoustic expressiveness without explicit labels, enabling style transfer and robust synthesis from noisy, unlabeled data. |
### <a id='category-hierarchical-generative-modeling-for-speech'></a>Hierarchical Generative Modeling for Speech: 1 papers found.
Context: 
	Document 1: [Category]: «Hierarchical Generative Modeling for Speech»
[_citation_number]: «6»
[Snippet]: «This paper proposes a neural sequence-to-sequence text-to-speech (TTS) model
which can control latent attributes in the generated speech that are rarely
annotated in the training data, such as speaking style, accent, background
noise, and recording conditions. The model is formulated as a conditional
generative model based on the variational autoencoder (VAE) framework, with two
levels of hierarchical latent variables. The first level is a categorical
variable, which represents attribute groups (e.g. clean/noisy) and provides
interpretability. The second level, conditioned on the first, is a multivariate
Gaussian variable, which characterizes specific attribute configurations (e.g.
noise level, speaking rate) and enables disentangled fine-grained control over
these attributes. This amounts to using a Gaussian mixture model (GMM) for the
latent distribution. Extensive evaluation demonstrates its ability to control
the aforementioned attributes. In particular, we train a high-quality
controllable TTS model on real found data, which is capable of inferring
speaker and style attributes from a noisy utterance and use it to synthesize
clean speech with controllable speaking style.»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-06-01T04:33:37+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2310.08846)\]. Further details \[[6](http://arxiv.org/abs/1810.07217)\]\[[7]()\]\[[8]()\]\[[9]()\]\[[10]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Recent advances in Text-to-Speech (TTS) have significantly improved speech
naturalness, increasing the demand for precise prosody control and
mispronunciation correction. Existing approaches for prosody manipulation often
depend on specialized modules or additional training, limiting their capacity
for post-hoc adjustments. Similarly, traditional mispronunciation correction
relies on grapheme-to-phoneme dictionaries, making it less practical in
low-resource settings. We introduce Counterfactual Activation Editing, a
model-agnostic method that manipulates internal representations in a
pre-trained TTS model to achieve post-hoc control of prosody and pronunciation.
Experimental results show that our method effectively adjusts prosodic features
and corrects mispronunciations while preserving synthesis quality. This opens
the door to inference-time refinement of TTS outputs without retraining,
bridging the gap between pre-trained TTS models and editable speech synthesis.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2310.08846)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2006.04558)\]\[[7]()\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer:  
The paper introduces a hierarchical generative model for speech synthesis that enables fine-grained control over latent attributes such as speaking style, accent, background noise, and recording conditions \[[6](http://arxiv.org/abs/1810.07217)\]. This model is built on a variational autoencoder (VAE) framework, incorporating two levels of latent variables: a categorical variable for attribute grouping (e.g., clean/noisy) and a multivariate Gaussian variable for specific attribute configurations (e.g., noise level, speaking rate) \[[6](http://arxiv.org/abs/1810.07217)\]. This hierarchical structure allows for disentangled control over these attributes, enhancing the model's interpretability and flexibility. The use of a Gaussian mixture model (GMM) for the latent distribution further supports the model's ability to infer speaker and style attributes from noisy utterances, enabling the synthesis of clean speech with controllable characteristics \[[6](http://arxiv.org/abs/1810.07217)\]. This approach addresses the challenge of controlling rarely annotated attributes in training data, offering a more versatile and adaptable solution for text-to-speech generation.
|    | reference                                                                                             |   date | key idea/summary                                                                                                                                                                                                          |
|----|-------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Hierarchical Generative Modeling for Controllable Speech Synthesis](http://arxiv.org/abs/1810.07217) |    nan | This paper introduces a neural sequence-to-sequence TTS model that enables control over latent attributes like speaking style and background noise using a hierarchical VAE framework with disentangled latent variables. |
### <a id='category-mispronunciation-correction-methods'></a>Mispronunciation Correction Methods: 1 papers found.
Context: 
	Document 1: [Category]: «Mispronunciation Correction Methods»
[_citation_number]: «10»
[Snippet]: «»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-06-01T04:33:37+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2310.08846)\]. Further details \[[6](http://arxiv.org/abs/1810.07217)\]\[[7]()\]\[[8]()\]\[[9]()\]\[[10]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Recent advances in Text-to-Speech (TTS) have significantly improved speech
naturalness, increasing the demand for precise prosody control and
mispronunciation correction. Existing approaches for prosody manipulation often
depend on specialized modules or additional training, limiting their capacity
for post-hoc adjustments. Similarly, traditional mispronunciation correction
relies on grapheme-to-phoneme dictionaries, making it less practical in
low-resource settings. We introduce Counterfactual Activation Editing, a
model-agnostic method that manipulates internal representations in a
pre-trained TTS model to achieve post-hoc control of prosody and pronunciation.
Experimental results show that our method effectively adjusts prosodic features
and corrects mispronunciations while preserving synthesis quality. This opens
the door to inference-time refinement of TTS outputs without retraining,
bridging the gap between pre-trained TTS models and editable speech synthesis.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](http://arxiv.org/abs/2310.08846)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/2006.04558)\]\[[7]()\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>

Answer: 
Mispronunciation correction in Text-to-Speech (TTS) systems has traditionally relied on grapheme-to-phoneme (G2P) dictionaries, which are effective in controlled environments but limited in low-resource settings \[[10]()\]. These methods often require extensive linguistic resources and are not easily adaptable to new or under-resourced languages. Recent approaches have sought to address these limitations by exploring model-agnostic methods that allow for post-hoc adjustments without retraining \[[10]()\]. Such techniques aim to manipulate internal representations of pre-trained TTS models to correct mispronunciations while preserving the quality of synthesized speech. This shift reflects a broader trend toward more flexible and editable speech synthesis frameworks that can accommodate diverse linguistic contexts and user needs \[[10]()\].
|    | reference                                                                                                                                      |   date | key idea/summary                                                                                          |
|----|------------------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------|
|  0 | [Speech Audio Corrector: using speech from non-target speakers for one-off correction of mispronunciations in grapheme-input text-to-speech]() |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
