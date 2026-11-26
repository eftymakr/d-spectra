## Related Works

Recent advancements in Text-to-Speech (TTS) systems have significantly improved speech naturalness, particularly through the development of end-to-end models that generate high-quality speech directly from text \[[18](http://arxiv.org/abs/1703.10135)\]. These models, such as Tacotron \[[18](http://arxiv.org/abs/1703.10135)\], FastSpeech \[[1](http://arxiv.org/abs/2006.04558)\], and Fastpitch \[[5](http://arxiv.org/abs/2006.06873)\], have enabled parallel processing and faster inference compared to autoregressive models. However, these systems often lack fine-grained control over prosody, which is essential for generating expressive and contextually appropriate speech \[[29](http://arxiv.org/abs/2008.03388)\]. 

Prosody control in TTS has been a major research focus, with several approaches focusing on explicit modeling of prosodic features such as pitch, energy, and duration \[[14](http://arxiv.org/abs/1803.09047)\]. For example, the work by \[[26](http://arxiv.org/abs/2106.08352)\] proposes a model that generates speech conditioned on these acoustic correlates, allowing for flexible and interpretable control over prosody. This approach enables the generation of multiple distinct renditions of a text by modifying the acoustic features during inference. However, these methods often require additional training or specialized modules, limiting their applicability in post-hoc scenarios \[[26](http://arxiv.org/abs/2106.08352)\].

Traditional approaches to mispronunciation correction rely on grapheme-to-phoneme (G2P) dictionaries, which are not practical in low-resource settings due to the lack of annotated data \[[29](http://arxiv.org/abs/2008.03388)\]. Recent work has explored alternative methods, such as using neural prosody generators to model prosody from text \[[14](http://arxiv.org/abs/1803.09047)\]. These models, however, often fail to capture the full variability of natural speech, resulting in flat and less expressive output \[[28](http://arxiv.org/abs/1906.04233)\].

To address these limitations, several studies have proposed controllable TTS systems that allow for post-hoc adjustments of prosody and pronunciation. For example, the work by \[[23](http://arxiv.org/abs/1803.09017)\] introduces "global style tokens" (GSTs), which enable the modeling of acoustic expressiveness without explicit labels. These embeddings can be used to control synthesis in novel ways, such as varying speed and speaking style independently of the text content \[[23](http://arxiv.org/abs/1803.09017)\]. Similarly, \[[29](http://arxiv.org/abs/2008.03388)\] proposes a user-controllable, context-aware neural prosody generator that allows for the modification of prosody constraints during inference, enhancing the flexibility of TTS systems.

Another line of research focuses on the use of variational autoencoders (VAEs) to model the distribution of prosodic features, enabling the generation of varied intonation while maintaining naturalness \[[28](http://arxiv.org/abs/1906.04233)\]. This approach allows for the exploration of the tails of the prior distribution, leading to more idiosyncratic and varied renditions of speech \[[28](http://arxiv.org/abs/1906.04233)\]. Additionally, \[[13](http://arxiv.org/abs/2002.03788)\] proposes a sequential prior in a discrete latent space to generate more naturally sounding samples, improving the quality of speech synthesis.

In summary, while existing TTS systems have made significant strides in speech naturalness, there remains a gap in the ability to perform post-hoc adjustments of prosody and pronunciation without retraining. The proposed method, Counterfactual Activation Editing, addresses this gap by enabling inference-time refinement of TTS outputs, offering a model-agnostic approach to post-hoc control \[[1](http://arxiv.org/abs/2006.04558)\].

References:
1. \[[1](http://arxiv.org/abs/2006.04558)\] http://arxiv.org/abs/2006.04558
2. \[[2](http://arxiv.org/abs/1909.10302)\] http://arxiv.org/abs/1909.10302
3. \[[3](http://arxiv.org/abs/1811.02122)\] http://arxiv.org/abs/1811.02122
4. \[[4](http://arxiv.org/abs/2009.06775)\] http://arxiv.org/abs/2009.06775
5. \[[5](http://arxiv.org/abs/2006.06873)\] http://arxiv.org/abs/2006.06873
6. \[[6](http://arxiv.org/abs/2110.02952)\] http://arxiv.org/abs/2110.02952
7. \[[7](http://arxiv.org/abs/2011.06465)\] http://arxiv.org/abs/2011.06465
8. \[[8](http://arxiv.org/abs/2008.01490)\] http://arxiv.org/abs/2008.01490
9. \[[9](http://arxiv.org/abs/2206.14643)\] http://arxiv.org/abs/2206.14643
10. \[[10](http://arxiv.org/abs/2106.06103)\] http://arxiv.org/abs/2106.06103
11. \[[11](http://arxiv.org/abs/1810.07217)\] http://arxiv.org/abs/1810.07217
12. \[[12](http://arxiv.org/abs/2002.03785)\] http://arxiv.org/abs/2002.03785
13. \[[13](http://arxiv.org/abs/2002.03788)\] http://arxiv.org/abs/2002.03788
14. \[[14](http://arxiv.org/abs/1803.09047)\] http://arxiv.org/abs/1803.09047
15. \[[15](http://arxiv.org/abs/2011.05161)\] http://arxiv.org/abs/2011.05161
16. \[[16](http://arxiv.org/abs/2005.11129)\] http://arxiv.org/abs/2005.11129
17. \[[17](http://arxiv.org/abs/1808.01410)\] http://arxiv.org/abs/1808.01410
18. \[[18](http://arxiv.org/abs/1703.10135)\] http://arxiv.org/abs/1703.10135
19. \[[19](http://arxiv.org/abs/2010.04301)\] http://arxiv.org/abs/2010.04301
20. \[[20](http://arxiv.org/abs/1712.05884)\] http://arxiv.org/abs/1712.05884
21. \[[21](http://arxiv.org/abs/2006.03575)\] http://arxiv.org/abs/2006.03575
22. \[[22](http://arxiv.org/abs/2209.06484)\] http://arxiv.org/abs/2209.06484
23. \[[23](http://arxiv.org/abs/1803.09017)\] http://arxiv.org/abs/1803.09017
24. \[[24](http://arxiv.org/abs/1705.08947)\] http://arxiv.org/abs/1705.08947
25. \[[25](http://arxiv.org/abs/1710.07654)\] http://arxiv.org/abs/1710.07654
26. \[[26](http://arxiv.org/abs/2106.08352)\] http://arxiv.org/abs/2106.08352
27. \[[27](http://arxiv.org/abs/1907.02479)\] http://arxiv.org/abs/1907.02479
28. \[[28](http://arxiv.org/abs/1906.04233)\] http://arxiv.org/abs/1906.04233
29. \[[29](http://arxiv.org/abs/2008.03388)\] http://arxiv.org/abs/2008.03388
30. \[[30](http://arxiv.org/abs/1905.07195)\] http://arxiv.org/abs/1905.07195
