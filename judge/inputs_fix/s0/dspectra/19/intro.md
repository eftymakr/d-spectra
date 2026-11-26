## Related Works

Speech-driven facial animation has been a focal point of research in computer vision and audio processing, with numerous approaches aiming to synthesize realistic 3D facial animations from speech signals. Early methods often relied on handcrafted features and rule-based systems, which were limited in their ability to capture the complex dynamics of facial expressions and lip movements \[[1](http://arxiv.org/abs/1807.07860)\]. More recent approaches have leveraged deep learning to improve the accuracy and realism of generated animations. For instance, WaveNet \[[2](http://arxiv.org/abs/1609.03499)\] introduced a deep neural network for generating raw audio waveforms, which has since been adapted for speech synthesis tasks, offering high-quality, natural-sounding outputs. Similarly, the use of GANs has enabled the generation of realistic talking head videos with lip synchronization \[[3](http://arxiv.org/abs/2104.11116)\].

Several works have focused on improving the synchronization between audio and visual features. For example, the Temporal GAN approach \[[4](http://arxiv.org/abs/2004.12992)\] was designed to generate videos of talking heads using a still image and an audio clip, without relying on handcrafted intermediate features. This method achieved significant improvements in lip synchronization and natural facial expressions. Similarly, the work by \[[5](http://arxiv.org/abs/2104.08223)\] proposed a system that generates videos of talking heads using a single reference image and audio input, achieving high-quality results with realistic lip movements and facial expressions.

The challenge of disentangling audio-visual representations has also been a key area of research. The Talking Face Generation by Adversarially Disentangled Audio-Visual Representation \[[6](http://arxiv.org/abs/2112.05329)\] introduced a method to disentangle subject-related and speech-related information, enabling arbitrary-subject talking face generation. This approach has been further refined in subsequent works, such as Pose-Controllable Talking Face Generation by Implicitly Modularized Audio-Visual Representation \[[7](http://arxiv.org/abs/1906.06337)\], which focuses on generating pose-controllable talking faces with accurate lip synchronization.

Another important direction is the integration of 3D facial models with audio-driven animation. MeshTalk \[[8](http://arxiv.org/abs/2107.09293)\] proposed a method for generating full facial 3D animation from speech, addressing issues such as uncanny or static upper face animation. This work demonstrated that a categorical latent space could effectively disentangle audio-correlated and audio-uncorrelated information, leading to more realistic facial animations.

Recent advances have also focused on improving the realism and expressiveness of generated animations. For example, FaceFormer \[[9](https://www.semanticscholar.org/paper/435b15745fb279db4ff8daf9d5facb9b21d58f3b)\] introduced a Transformer-based autoregressive model for speech-driven 3D facial animation, which addresses the limitations of prior methods by encoding long-term audio context and autoregressively predicting 3D face meshes. This approach has shown promising results in terms of lip synchronization and facial expression realism.

In addition, works such as SadTalker \[[10](http://arxiv.org/abs/2112.02214)\] and Imitator \[[11](http://arxiv.org/abs/2002.10137)\] have focused on generating realistic 3D motion coefficients for stylized audio-driven talking face animation, addressing issues such as unnatural head movement and distorted expressions. These methods have demonstrated significant improvements in motion realism and video quality.

Finally, the integration of emotional and contextual information into speech-driven facial animation has also been explored. For instance, the work by \[[12](http://arxiv.org/abs/2306.10799)\] introduced a method for generating emotional talking face videos by disentangling content and emotion in the audio signal, leading to more expressive and realistic animations.

In summary, while existing methods have made significant progress in generating realistic speech-driven facial animations, challenges remain in accurately capturing the complex dynamics of facial expressions, lip movements, and emotional content. The proposed Wav2Sem module addresses these challenges by introducing a semantic decorrelation mechanism that enhances the precision and naturalness of facial animations.

References:
\[[1](http://arxiv.org/abs/1807.07860)\] http://arxiv.org/abs/1807.07860
\[[2](http://arxiv.org/abs/1609.03499)\] http://arxiv.org/abs/1609.03499
\[[3](http://arxiv.org/abs/2104.11116)\] http://arxiv.org/abs/1805.09313
\[[4](http://arxiv.org/abs/2004.12992)\] http://arxiv.org/abs/1807.07860
\[[5](http://arxiv.org/abs/2104.08223)\] http://arxiv.org/abs/2104.08223
\[[6](http://arxiv.org/abs/2112.05329)\] http://arxiv.org/abs/1807.07860
\[[7](http://arxiv.org/abs/1906.06337)\] http://arxiv.org/abs/2104.11116
\[[8](http://arxiv.org/abs/2107.09293)\] http://arxiv.org/abs/2104.08223
\[[9](https://www.semanticscholar.org/paper/435b15745fb279db4ff8daf9d5facb9b21d58f3b)\] http://arxiv.org/abs/2112.05329
\[[10](http://arxiv.org/abs/2112.02214)\] http://arxiv.org/abs/2211.12194
\[[11](http://arxiv.org/abs/2002.10137)\] http://arxiv.org/abs/2301.00023
