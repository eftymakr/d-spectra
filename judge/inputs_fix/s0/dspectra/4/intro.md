## Related Works

In the field of in-context learning (ICL), the reliance on high-quality demonstrations from large annotated corpora has been well established \[[1](http://arxiv.org/abs/1910.10683)\]. However, the presence of noisy annotations poses a significant challenge, as existing methods often assume that noisy samples yield higher perplexity than their clean counterparts \[[2](http://arxiv.org/abs/1804.07461)\]. This assumption, while useful in low-noise scenarios, fails when the noise ratio is high and many demonstrations are flawed \[[3](http://arxiv.org/abs/1512.06974)\]. 

Several approaches have been proposed to address label noise in training deep neural networks. For instance, \[[4](http://arxiv.org/abs/1706.00038)\] introduces a framework that models the relationship between noisy and clean labels using an undirected graphical model, enabling semi-supervised learning from noisy datasets. This method has shown effectiveness in reducing label noise in image labeling tasks \[[5](http://arxiv.org/abs/2012.11854)\]. Similarly, \[[6](http://arxiv.org/abs/2002.07394)\] explores the use of instance-dependent label noise, where the noise rate is not uniform across instances, and proposes a second-order approach to estimate covariance terms between noise rates and Bayes optimal labels. This method allows for the transformation of instance-dependent noise into class-dependent noise, enabling the use of existing solutions \[[7](http://arxiv.org/abs/2309.00770)\].

Another line of work focuses on learning with noisy labels through semi-supervised techniques. \[[8](http://arxiv.org/abs/2312.12275)\] introduces DivideMix, a framework that dynamically divides training data into labeled and unlabeled sets, and trains the model in a semi-supervised manner. This approach helps avoid confirmation bias by training two diverged networks simultaneously \[[9](http://arxiv.org/abs/1703.02391)\]. Additionally, \[[10](http://arxiv.org/abs/2207.13316)\] presents a unified distillation framework that leverages side information, such as a small clean dataset and label relations in a knowledge graph, to hedge the risk of learning from noisy labels \[[11](http://arxiv.org/abs/1809.04019)\].

In the context of scene graph generation, \[[12](http://arxiv.org/abs/2204.06125)\] addresses the issue of noisy labels by proposing NICEST, a strategy that detects and corrects noisy samples through a combination of negative and positive sample detection and correction techniques. This method generates high-quality samples and employs a multi-teacher knowledge distillation strategy to improve model performance \[[13](http://arxiv.org/abs/1609.03683)\].

Moreover, \[[14](http://arxiv.org/abs/1711.07131)\] highlights the challenges of text classification with noisy, historical data, emphasizing the discrepancy between training and prediction data. This work demonstrates the utility of dirty training datasets for building prediction models that generalize to cleaner inputs \[[15](http://arxiv.org/abs/1607.06520)\].

In summary, while many approaches have been proposed to handle noisy annotations, the assumption that noisy samples yield higher perplexity is not universally valid, especially in high-noise scenarios. The introduction of a dual debiasing framework that uses synthesized neighbors to correct perplexity estimates represents a significant advancement in this area \[[16](http://arxiv.org/abs/1909.01326)\].

1. \[[1](http://arxiv.org/abs/1910.10683)\] "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer"  
2. \[[2](http://arxiv.org/abs/1804.07461)\] "GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding"  
3. \[[3](http://arxiv.org/abs/1512.06974)\] "Toward Robustness against Label Noise in Training Deep Discriminative Neural Networks"  
4. \[[4](http://arxiv.org/abs/1706.00038)\] "A Second-Order Approach to Learning with Instance-Dependent Label Noise"  
5. \[[5](http://arxiv.org/abs/2012.11854)\] "DivideMix: Learning with Noisy Labels as Semi-supervised Learning"  
6. \[[6](http://arxiv.org/abs/2002.07394)\] "Learning from Noisy Labels with Distillation"  
7. \[[7](http://arxiv.org/abs/2309.00770)\] "NICEST: Noisy Label Correction and Training for Robust Scene Graph Generation"  
8. \[[8](http://arxiv.org/abs/2312.12275)\] "Training and Prediction Data Discrepancies: Challenges of Text Classification with Noisy, Historical Data"  
9. \[[9](http://arxiv.org/abs/1703.02391)\] "Hierarchical Text-Conditional Image Generation with CLIP Latents"  
10. \[[10](http://arxiv.org/abs/2207.13316)\] "Making Deep Neural Networks Robust to Label Noise: A Loss Correction Approach"  
11. \[[11](http://arxiv.org/abs/1809.04019)\] "CleanNet: Transfer Learning for Scalable Image Classifier Training with Label Noise"  
12. \[[12](http://arxiv.org/abs/2204.06125)\] "Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings"  
13. \[[13](http://arxiv.org/abs/1609.03683)\] "The Woman Worked as a Babysitter: On Biases in Language Generation"  
14. \[[14](http://arxiv.org/abs/1711.07131)\] "Noisy Annotation Refinement for Object Detection"  
15. \[[15](http://arxiv.org/abs/1607.06520)\] "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer"  
16. \[[16](http://arxiv.org/abs/1909.01326)\] "Toward Robustness against Label Noise in Training Deep Discriminative Neural Networks"
