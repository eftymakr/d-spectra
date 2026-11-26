## Related Works

Speech-driven 3D facial animation has been a focal point in computer vision and graphics research, with numerous approaches aiming to synthesize realistic facial expressions that synchronize with audio inputs. Early methods primarily relied on handcrafted features and rule-based systems, which lacked the flexibility and accuracy required for complex facial animations \[[1](http://arxiv.org/abs/2312.02781)\]. With the advent of deep learning, researchers began exploring data-driven models that could learn mappings from audio signals to facial motions \[[2](http://arxiv.org/abs/2301.06059)\].

A significant body of work focuses on improving lip synchronization by leveraging phoneme-level features extracted from speech. For instance, \[[3](http://arxiv.org/abs/2408.07005)\] introduced a method that learns viseme dynamics from speech videos, producing animator-friendly viseme curves that support multilingual speech inputs. This approach utilizes phoneme priors to extract viseme parameters, which are then used to generate more controllable and realistic facial animations. Similarly, \[[4](http://arxiv.org/abs/2503.09852)\] proposed a joint audio-text model to capture contextual information for expressive speech-driven 3D facial animation, demonstrating that combining acoustic and textual modalities can synthesize realistic facial expressions while maintaining audio-lip synchronization.

Recent advances have also emphasized the importance of style modeling in speech-driven facial animation. \[[5](http://arxiv.org/abs/2112.02214)\] introduced a framework called StyleSpeaker, which explicitly extracts speaking styles based on speaker characteristics while accounting for style biases caused by different speech conditions. This approach enhances the accuracy of style modeling and enables rapid adaptation to unseen speakers without fine-tuning. Additionally, \[[6](http://arxiv.org/abs/2312.10877)\] proposed a method that disentangles speaking style from semantic content, allowing for more realistic and controllable synthesis of facial animations.

Another key challenge in speech-driven facial animation is the lack of large-scale, high-quality datasets. \[[7](http://arxiv.org/abs/2407.12501)\] addressed this by introducing a large-scale 3D Chinese Audio-Visual Facial Animation (3D-CAVFA) dataset, which is crucial for training and evaluating models. \[[8](http://arxiv.org/abs/2407.01034)\] further contributed to this area by proposing a benchmark dataset called BlendVOCA, which contains pairs of speech audio and parameters of a blendshape facial model. These datasets have been instrumental in advancing the field and enabling more robust training of models.

In addition to lip synchronization and style modeling, recent work has also focused on enhancing the realism and expressiveness of facial animations. \[[9](http://arxiv.org/abs/2409.01113)\] introduced EmoFace, a method that generates emotionally expressive talking heads with synchronized lip movements. This approach incorporates independent speech and emotion encoders to learn the relationship between audio, emotion, and facial controller rigs, enabling the generation of facial expressions with multiple emotions. \[[10](http://arxiv.org/abs/2409.19143)\] further advanced this by proposing a method that disentangles emotional expressions from speech content, allowing for more nuanced and realistic facial animations.

Overall, these works highlight the ongoing efforts to improve the accuracy, realism, and controllability of speech-driven 3D facial animation. The proposed Wav2Sem module builds upon these advancements by introducing a semantic decorrelation mechanism to address the averaging effect caused by phonetically similar syllables \[[11](http://arxiv.org/abs/2303.11089)\].

### References

1. \[[3](http://arxiv.org/abs/2408.07005)\] Learning Audio-Driven Viseme Dynamics for 3D Face Animation  
2. \[[4](http://arxiv.org/abs/2503.09852)\] Content and Style Aware Audio-Driven Facial Animation  
3. \[[5](http://arxiv.org/abs/2112.02214)\] StyleSpeaker: Audio-Enhanced Fine-Grained Style Modeling for Speech-Driven 3D Facial Animation  
4. \[[6](http://arxiv.org/abs/2312.10877)\] Mimic: Speaking Style Disentanglement for Speech-Driven 3D Facial Animation  
5. \[[7](http://arxiv.org/abs/2407.12501)\] Joint Audio-Text Model for Expressive Speech-Driven 3D Facial Animation  
6. \[[8](http://arxiv.org/abs/2407.01034)\] SAiD: Speech-driven Blendshape Facial Animation with Diffusion  
7. \[[9](http://arxiv.org/abs/2409.01113)\] EmoFace: Audio-driven Emotional 3D Face Animation  
8. \[[10](http://arxiv.org/abs/2409.19143)\] EmoTalk: Speech-Driven Emotional Disentanglement for 3D Face Animation  
9. \[[11](http://arxiv.org/abs/2303.11089)\] Wav2Sem: A Plug-and-Play Semantic Decorrelation Module for Speech-Driven Facial Animation
