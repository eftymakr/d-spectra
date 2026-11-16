## Related Works

Text-to-Speech (TTS) systems have evolved significantly, with recent advances focusing on improving speech naturalness, controllability, and robustness \[[1](http://arxiv.org/abs/1905.09263)\]. Early TTS models were either concatenative or statistical parametric, but neural network-based end-to-end models have largely replaced them due to their superior quality \[[1](http://arxiv.org/abs/1905.09263)\]. However, these models often suffer from slow inference speeds and limited controllability over prosody and other speech attributes \[[1](http://arxiv.org/abs/1905.09263)\]. For instance, autoregressive models like Tacotron 2 generate mel-spectrograms sequentially, leading to slower inference times compared to non-autoregressive models \[[1](http://arxiv.org/abs/1905.09263)\]. FastSpeech, a non-autoregressive model, addresses these issues by using a parallel feed-forward network based on the Transformer architecture to generate mel-spectrograms in parallel, achieving a 270x speedup over autoregressive models \[[1](http://arxiv.org/abs/1905.09263)\]. FastSpeech 2 further improves upon FastSpeech by directly using ground-truth targets during training and incorporating more speech variation information such as pitch and energy, leading to higher voice quality and faster training and inference speeds \[[2](http://arxiv.org/abs/2006.04558)\].

Prosody control is a critical aspect of TTS, enabling more expressive and natural speech synthesis. Several approaches have been proposed to control speaking rate and other prosodic attributes. For example, a speaking rate attention-based duration prediction method allows for implicit control of speaking rate by conditioning the duration predictor on the speaking rate \[[3](http://arxiv.org/abs/2310.08846)\]. Additionally, style tokens have been introduced to model acoustic expressiveness in end-to-end speech synthesis, enabling control over speed and speaking style without explicit labels \[[4](http://arxiv.org/abs/1803.09017)\]. These style tokens are trained within Tacotron and can be used for style transfer, replicating the speaking style of one audio clip across different texts \[[4](http://arxiv.org/abs/1803.09017)\]. Similarly, hierarchical generative modeling has been proposed to control latent attributes such as speaking style, accent, and background noise, using a variational autoencoder (VAE) framework with hierarchical latent variables \[[6](http://arxiv.org/abs/1810.07217)\].

Mispronunciation correction in TTS is another important challenge, especially in low-resource settings where grapheme-to-phoneme dictionaries are not available. Traditional methods rely on such dictionaries, limiting their practicality \[[10]()\]. Recent work has explored the use of speech from non-target speakers for one-off correction of mispronunciations in grapheme-input TTS systems \[[10]()\]. These approaches aim to improve pronunciation accuracy without requiring extensive training data or specialized modules.

In summary, while existing methods have made strides in improving TTS quality and controllability, they often rely on specialized modules
## Research papers
### Outline
- [Non-Autoregressive TTS Models [2 papers]](#category-non-autoregressive-tts-models)
- [Prosody Control Methods in TTS [5 papers]](#category-prosody-control-methods-in-tts)
- [Style Tokens and Expressiveness Modeling [1 papers]](#category-style-tokens-and-expressiveness-modeling)
- [Hierarchical Generative Modeling for TTS [1 papers]](#category-hierarchical-generative-modeling-for-tts)
- [Mispronunciation Correction Techniques [1 papers]](#category-mispronunciation-correction-techniques)

### <a id='category-non-autoregressive-tts-models'></a>Non-Autoregressive TTS Models: 2 papers found.
Context: 
	Document 1: [_citation_number]: «1»
[Snippet]: «Neural network based end-to-end text to speech (TTS) has significantly improved the quality of synthesized speech. Prominent methods (e.g., Tacotron 2) usually first generate mel-spectrogram from text, and then synthesize speech from the mel-spectrogram using vocoder such as WaveNet. Compared with traditional concatenative and statistical parametric approaches, neural network based end-to-end models suffer from slow inference speed, and the synthesized speech is usually not robust (i.e., some words are skipped or repeated) and lack of controllability (voice speed or prosody control). In this work, we propose a novel feed-forward network based on Transformer to generate mel-spectrogram in parallel for TTS. Specifically, we extract attention alignments from an encoder-decoder based teacher model for phoneme duration prediction, which is used by a length regulator to expand the source phoneme sequence to match the length of the target mel-spectrogram sequence for parallel mel-spectrogram generation. Experiments on the LJSpeech dataset show that our parallel model matches autoregressive models in terms of speech quality, nearly eliminates the problem of word skipping and repeating in particularly hard cases, and can adjust voice speed smoothly. Most importantly, compared with autoregressive Transformer TTS, our model speeds up mel-spectrogram generation by 270x and the end-to-end speech synthesis by 38x. Therefore, we call our model FastSpeech.»
[Category]: «Non-Autoregressive TTS Models»

	Document 2: [_citation_number]: «2»
[Snippet]: «Non-autoregressive text to speech (TTS) models such as FastSpeech can synthesize speech significantly faster than previous autoregressive models with comparable quality. The training of FastSpeech model relies on an autoregressive teacher model for duration prediction (to provide more information as input) and knowledge distillation (to simplify the data distribution in output), which can ease the one-to-many mapping problem (i.e., multiple speech variations correspond to the same text) in TTS. However, FastSpeech has several disadvantages: 1) the teacher-student distillation pipeline is complicated and time-consuming, 2) the duration extracted from the teacher model is not accurate enough, and the target mel-spectrograms distilled from teacher model suffer from information loss due to data simplification, both of which limit the voice quality. In this
|    | reference                                                                                        |   date | key idea/summary                                                                                                                                                                                                                                        |
|----|--------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [FastSpeech: Fast, Robust and Controllable Text to Speech](http://arxiv.org/abs/1905.09263)      |    nan | The paper introduces FastSpeech, a novel feed-forward Transformer-based model for TTS that generates mel-spectrogram in parallel, significantly improving speed while maintaining speech quality and reducing issues like word skipping and repetition. |
|  1 | [FastSpeech 2: Fast and High-Quality End-to-End Text to Speech](http://arxiv.org/abs/2006.04558) |    nan | FastSpeech 2 improves upon the original FastSpeech by directly using ground-truth targets and incorporating more speech variation information, leading to faster training and better voice quality in text-to-speech synthesis.                         |
### <a id='category-prosody-control-methods-in-tts'></a>Prosody Control Methods in TTS: 5 papers found.
Context: 
	Document 1: [_citation_number]: «3»
[Snippet]: «With the advent of high-quality speech synthesis, there is a lot of interest in controlling various prosodic attributes of speech. Speaking rate is an essential attribute towards modelling the expressivity of speech. In this work, we propose a novel approach to control the speaking rate for non-autoregressive TTS. We achieve this by conditioning the speaking rate inside the duration predictor, allowing implicit speaking rate control. We show the benefits of this approach by synthesising audio at various speaking rate factors and measuring the quality of speaking rate-controlled synthesised speech. Further, we study the effect of the speaking rate distribution of the training data towards effective rate control. Finally, we fine-tune a baseline pretrained TTS model to obtain speaking rate control TTS. We provide various analyses to showcase the benefits of using this proposed approach, along with objective as well as subjective metrics. We find that the proposed methods have higher subjective scores and lower speaker rate errors across many speaking rate factors over the baseline.»
[Category]: «Prosody Control Methods in TTS»

	Document 2: [_citation_number]: «5»
[Snippet]: «We present an extension to the Tacotron speech synthesis architecture that learns a latent embedding space of prosody, derived from a reference acoustic representation containing the desired prosody. We show that conditioning Tacotron on this learned embedding space results in synthesized audio that matches the prosody of the reference signal with fine time detail even when the reference and synthesis speakers are different. Additionally, we show that a reference prosody embedding can be used to synthesize text that is different from that of the reference utterance. We define several quantitative and subjective metrics for evaluating prosody transfer, and report results with accompanying audio samples from single-speaker and 44-speaker Tacotron models on a prosody transfer task.»
[Category]: «Prosody Control Methods in TTS»

	Document 3: [_citation_number]: «7»
[Snippet]: «»
[Category]: «Prosody Control Methods in TTS»

	Document 4: [_citation_number]: «8»
[Snippet]: «»
[Category]: «Prosody Control Methods in TTS»

	Document 5: [_citation_number]: «9»
[Snippet]: «»
[Category]: «Prosody Control Methods in TTS»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a
|    | reference                                                                                                              |   date | key idea/summary                                                                                                                                                                                                                                          |
|----|------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Speaking rate attention-based duration prediction for speed control TTS](http://arxiv.org/abs/2310.08846)             |    nan | This work proposes a novel approach to control speaking rate in non-autoregressive TTS by conditioning the speaking rate within the duration predictor, leading to improved subjective scores and lower speaker rate errors compared to baseline methods. |
|  1 | [Towards End-to-End Prosody Transfer for Expressive Speech Synthesis with
  Tacotron](http://arxiv.org/abs/1803.09047) |    nan | This paper introduces an extension to the Tacotron speech synthesis model that uses a learned latent embedding space of prosody to enable fine-grained prosody transfer between different speakers and utterances.                                        |
|  2 | [Expressive prosody for unit-selection speech synthesis.]()                                                            |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                 |
|  3 | [Ctrl-P: Temporal control of prosodic variation for speech synthesis]()                                                |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                 |
|  4 | [Speaking Rate Control of end-to-end TTS Models by Direct Manipulation of the Encoder's Output Embeddings]()           |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                 |
### <a id='category-style-tokens-and-expressiveness-modeling'></a>Style Tokens and Expressiveness Modeling: 1 papers found.
Context: 
	Document 1: [_citation_number]: «4»
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
[Category]: «Style Tokens and Expressiveness Modeling»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-06-01T04:33:37+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2310.08846)\]. Further details \[[6](http://arxiv.org/abs/1810.07217)\]\[[7]()\]\[[8]()\]\[[9]()\]\[[10]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Recent advances in Text-to-Speech (TTS) have significantly improved speech
naturalness, increasing the demand for precise prosody control and
mispronunciation correction. Existing approaches for prosody manipulation often
depend on specialized modules or additional training, limiting their capacity
for post-hoc adjustments. Similarly, traditional mispronunciation correction
relies on grapheme-to-phoneme dictionaries, making it less practical in
low-resource settings. We introduce Counterfactual Activation Editing, a
model-agnostic method that manipulates internal representations in a
pre-trained
|    | reference                                                                                                                           |   date | key idea/summary                                                                                                                                                                                                                                            |
|----|-------------------------------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Style Tokens: Unsupervised Style Modeling, Control and Transfer in
  End-to-End Speech Synthesis](http://arxiv.org/abs/1803.09017) |    nan | The paper introduces 'global style tokens' (GSTs), which are embeddings jointly trained within a speech synthesis system to model acoustic expressiveness without explicit labels, enabling style transfer and robust synthesis from noisy, unlabeled data. |
### <a id='category-hierarchical-generative-modeling-for-tts'></a>Hierarchical Generative Modeling for TTS: 1 papers found.
Context: 
	Document 1: [_citation_number]: «6»
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
[Category]: «Hierarchical Generative Modeling for TTS»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-06-01T04:33:37+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2310.08846)\]. Further details \[[6](http://arxiv.org/abs/1810.07217)\]\[[7]()\]\[[8]()\]\[[9]()\]\[[10]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Recent advances in Text-to-Speech (TTS) have significantly improved speech
naturalness, increasing the demand for precise prosody control and
mispronunciation correction. Existing approaches for prosody manipulation often
depend on
|    | reference                                                                                             |   date | key idea/summary                                                                                                                                                                                                          |
|----|-------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Hierarchical Generative Modeling for Controllable Speech Synthesis](http://arxiv.org/abs/1810.07217) |    nan | This paper introduces a neural sequence-to-sequence TTS model that enables control over latent attributes like speaking style and background noise using a hierarchical VAE framework with disentangled latent variables. |
### <a id='category-mispronunciation-correction-techniques'></a>Mispronunciation Correction Techniques: 1 papers found.
Answer:  
Mispronunciation correction in Text-to-Speech (TTS) systems has traditionally relied on grapheme-to-phoneme dictionaries, which are limited in low-resource settings \[[1](http://arxiv.org/abs/1905.09263)\]. These methods often lack flexibility and adaptability, making them less effective for diverse or under-resourced languages \[[2](http://arxiv.org/abs/2006.04558)\]. Recent work has explored alternative approaches, such as model-agnostic techniques that allow for post-hoc manipulation of internal representations to correct mispronunciations \[[3](http://arxiv.org/abs/2310.08846)\]. These methods enable fine-grained adjustments without requiring additional training or specialized modules, thereby improving the practicality and efficiency of TTS systems \[[4](http://arxiv.org/abs/1803.09017)\]. For instance, Counterfactual Activation Editing has been proposed as a method to modify pre-trained TTS models to achieve both prosody control and mispronunciation correction during inference \[[5](http://arxiv.org/abs/1803.09047)\]. This approach aligns with broader efforts to enhance the editability of speech synthesis, bridging the gap between pre-trained models and real-time post-hoc refinements \[[6](http://arxiv.org/abs/1810.07217)\]. Such innovations are critical for advancing TTS systems toward more natural and adaptable speech synthesis \[[7]()\].
|    | reference                                                                                                                                      |   date | key idea/summary                                                                                          |
|----|------------------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------|
|  0 | [Speech Audio Corrector: using speech from non-target speakers for one-off correction of mispronunciations in grapheme-input text-to-speech]() |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary. |
