## Related Works

Speech-driven 3D facial animation has been a focal point in recent research, with numerous approaches aiming to generate realistic and synchronized facial expressions from audio inputs. Early methods primarily relied on phoneme-based models, where phoneme sequences were used to drive facial animations \[[1](https://www.semanticscholar.org/paper/435b15745fb279db4ff8daf9d5facb9b21d58f3b)\]. However, these approaches often suffered from limited expressiveness and poor synchronization due to the lack of contextual and semantic information \[[2](http://arxiv.org/abs/2312.02781)\]. 

Recent advances have introduced deep learning techniques that leverage audio-visual data to improve the realism and accuracy of facial animations. For instance, Voice2Face employs a conditional Variational Autoencoder (cVAE) to generate face and tongue animations directly from speech, achieving significant improvements in perceived animation quality \[[3](http://arxiv.org/abs/2301.06059)\]. Similarly, PMMTalk introduces a framework that integrates visual and textual cues to enhance the accuracy of facial animation, demonstrating superior performance compared to state-of-the-art methods \[[4](https://www.semanticscholar.org/paper/e80391ba7a62bd8db2f7e7c529182fa916b7d918)\]. 

The importance of semantic information in speech-driven animation has also been emphasized. For example, the work in \[[5](http://arxiv.org/abs/2408.07005)\] proposes a method that disentangles content and style representations from audio inputs, enabling more flexible and controllable facial animations. This aligns with the approach in \[[6](http://arxiv.org/abs/2404.12888)\], which uses a non-autoregressive seq2seq formulation to model sentence-level dependencies and improve mouth articulations. 

In addition to content and style disentanglement, several studies have focused on improving lip synchronization and facial expression fidelity. For example, \[[7](http://arxiv.org/abs/2503.09852)\] presents a method that learns viseme dynamics from speech videos, producing animator-friendly viseme curves that support multilingual speech inputs. This is further enhanced in \[[8](https://www.semanticscholar.org/paper/ebf164c1d4f942e50d3515689b9c095350f207e2)\], where a viseme scanning approach is introduced to acquire high-fidelity viseme assets for efficient speech animation production. 

The challenge of generalization across speakers and handling diverse speaking styles has also been addressed. StyleSpeaker explicitly extracts speaking styles based on speaker characteristics and accounts for style biases caused by different speech conditions, leading to more robust style modeling \[[9](http://arxiv.org/abs/2112.02214)\]. Similarly, \[[10](http://arxiv.org/abs/2312.10877)\] proposes a two-stage transfer-learning framework that pretrains on large-scale pseudo-3D facial data and finetunes on smaller high-fidelity 3D datasets, achieving state-of-the-art performance in lip synchronization and expression fidelity \[[11](https://www.semanticscholar.org/paper/012c8325a4dbf2479462d685b48564a96717f0c1)\]. 

Furthermore, the integration of multimodal information has been explored to improve the realism and expressiveness of facial animations. For example, \[[12](http://arxiv.org/abs/2407.12501)\] introduces a joint audio-text model that leverages contextual text embeddings to disambiguate variations in upper face expressions, resulting in more accurate and natural facial animations. This is further extended in \[[13](http://arxiv.org/abs/2407.01034)\], where a joint audio-text model is used to capture contextual information for expressive speech-driven 3D facial animation, demonstrating superior performance compared to existing methods \[[14](http://arxiv.org/abs/2409.01113)\]. 

In summary, the field of speech-driven 3D facial animation has seen significant advancements, with a growing emphasis on semantic understanding, style disentanglement, and multimodal integration to achieve more realistic and expressive facial animations.

References:
1. \[[1](https://www.semanticscholar.org/paper/435b15745fb279db4ff8daf9d5facb9b21d58f3b)\] \[[15](http://arxiv.org/abs/1807.07860)\]
2. \[[2](http://arxiv.org/abs/2312.02781)\] \[[16](http://arxiv.org/abs/2409.19143)\]
3. \[[3](http://arxiv.org/abs/2301.06059)\] \[[17](http://arxiv.org/abs/2104.11116)\]
4. \[[4](https://www.semanticscholar.org/paper/e80391ba7a62bd8db2f7e7c529182fa916b7d918)\] \[[18](http://arxiv.org/abs/2303.11089)\]
5. \[[5](http://arxiv.org/abs/2408.07005)\] \[[19](https://www.semanticscholar.org/paper/82663b1bece4d1c21136b8a2048d7b977cba16bf)\]
6. \[[6](http://arxiv.org/abs/2404.12888)\] \[[20](http://arxiv.org/abs/2310.17011)\]
7. \[[7](http://arxiv.org/abs/2503.09852)\] \[[21](http://arxiv.org/abs/2301.00023)\]
8. \[[8](https://www.semanticscholar.org/paper/ebf164c1d4f942e50d3515689b9c095350f207e2)\] \[[22](http://arxiv.org/abs/2306.10799)\]
9. \[[9](http://arxiv.org/abs/2112.02214)\] \[[23](https://www.semanticscholar.org/paper/c55de775aabf4cfe18c58c8dbdac3677d80dfbae)\]
10. \[[10](http://arxiv.org/abs/2312.10877)\] \[[24](http://arxiv.org/abs/2401.08655)\]
11. \[[11](https://www.semanticscholar.org/paper/012c8325a4dbf2479462d685b48564a96717f0c1)\] \[[25](http://arxiv.org/abs/2407.18595)\]
12. \[[12](http://arxiv.org/abs/2407.12501)\] \[[26](https://www.semanticscholar.org/paper/0e15c827494535ff7d39000187ccbabcfb5666c4)\]
13. \[[13](http://arxiv.org/abs/2407.01034)\] \[[27](http://arxiv.org/abs/2112.05329)\]
14. \[[14](http://arxiv.org/abs/2409.01113)\] \[[28](http://arxiv.org/abs/2402.16124)\]
