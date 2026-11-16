## Related Works

Speech-driven 3D facial animation has seen significant advancements, particularly in improving lip synchronization, emotional expressiveness, and handling phonetically similar syllables that lead to averaging effects in feature spaces. Early approaches relied on handcrafted features and rule-based systems, which lacked the flexibility and expressiveness required for realistic animation \[[Yihong Lin' 2024-08-03](http://arxiv.org/abs/2408.01826v5)\]. More recently, deep learning techniques have been employed to improve the accuracy and realism of these animations. For instance, FaceXHuBERT \[[Haozhe Wu' 2023-08-10](http://arxiv.org/abs/2308.05428v1)\] introduced a text-less speech-driven 3D facial animation generation method that allows for capturing personalized and subtle cues in speech, such as identity, emotion, and hesitation. This approach leverages self-supervised pretrained HuBERT models to incorporate both lexical and non-lexical information in the audio without using a large lexicon, enhancing the realism of the generated animations.

Similarly, FaceFormer \[[Kazi Injamamul Haque' 2023-03-09](http://arxiv.org/abs/2303.05416v1)\] proposed a Transformer-based autoregressive model that encodes long-term audio context and autoregressively predicts a sequence of animated 3D face meshes. This model integrates self-supervised pre-trained speech representations to address data scarcity issues and introduces biased attention mechanisms to align audio-motion modalities and generalize to longer audio sequences. This work highlights the importance of leveraging pre-trained models for better performance in speech-driven facial animation.

The work by VividTalker \[[Haohe Liu' 2023-08-10](http://arxiv.org/abs/2308.05734v3)\] addressed the limitations of existing methods by explicitly disentangling facial animation into head pose and mouth movement, encoding them separately into discrete latent spaces. This framework enabled more natural facial details and flexible head poses, significantly improving the quality of the generated animations. The method also constructed a new 3D dataset with detailed shapes, enhancing the training process.

Another notable contribution is the work by Saikat et al. \[[Qingju Liu' 2024-08-13](http://arxiv.org/abs/2408.07005v2)\], which focused on the composite and regional nature of facial movements. They introduced an adaptive modulation module to dynamically adjust speech-driven facial movements across frames and ensured that each facial feature focused on local spatial movements. This approach improved the realism of the generated animations by considering both global and local movement patterns.

In addition, the paper by EmoFace \[[Sreyan Ghosh' 2022-03-25](http://arxiv.org/abs/2203.13628v3)\] introduced a novel methodology for generating emotionally expressive talking heads, emphasizing the importance of emotional dynamics in facial animations. This work proposed independent speech and emotion encoders to learn the relationship between audio, emotion, and facial controller rigs, leading to more natural and emotionally rich animations.

These works collectively highlight the challenges and advancements in the field of speech-driven 3D facial animation. While many approaches have focused on improving lip synchronization and identity control, there remains a need for more expressive and emotionally rich animations. The proposed Wav2Sem module addresses these gaps by introducing a semantic decorrelation mechanism that effectively decouples audio features, thereby enhancing the precision and naturalness of facial animations.

### References

1. [Document 1]  
2. [Document 3]  
3. [Document 15]  
4. [Document 8]  
5. [Document 12]  
6. [Document 19]
