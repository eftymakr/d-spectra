## Related Works

Deep learning model compression and acceleration have been extensively studied, with a focus on quantization techniques to reduce computational and memory costs while maintaining model accuracy. Quantization methods such as narrow-precision floating-point and block floating-point have been widely explored for their ability to reduce the bitwidth of neural network parameters \[[1](http://arxiv.org/abs/2302.08007)\]. However, these approaches often fail to fully exploit the potential of hardware-specific optimizations, especially for complex operations like Softmax and LayerNorm, which are critical for Vision Transformers (ViTs) . 

Recent work has attempted to address these limitations by introducing hardware-aware quantization frameworks. For example, HAQ leverages reinforcement learning to automatically determine optimal bitwidths for each layer of a neural network, taking into account hardware constraints such as latency and energy consumption \[[2](http://arxiv.org/abs/1811.08886)\]. This approach enables more efficient quantization policies tailored to specific hardware architectures, which is a key step toward improving the performance of quantized models on specialized accelerators. 

Another notable effort is GOBO, which focuses on quantizing attention-based models like BERT with minimal accuracy loss. GOBO achieves this by compressing 99.9% of the 32-bit floating-point parameters to 3 bits without requiring fine-tuning or retraining \[[3](http://arxiv.org/abs/2005.03842)\]. This method significantly reduces memory storage, inference latency, and energy consumption, making it suitable for deployment on resource-constrained devices. Additionally, GOBO introduces a co-designed hardware architecture that further optimizes computation by maintaining low-precision weights during inference, reducing the need for expensive multiply-accumulate operations \[[3](http://arxiv.org/abs/2005.03842)\].

The challenge of efficiently mapping ViT operations onto hardware has also been explored in the context of FPGA-based accelerators. HeatViT introduces an adaptive token pruning framework that dynamically identifies and removes non-informative tokens during inference, reducing both computation and memory usage \[[4](http://arxiv.org/abs/2211.08110)\]. This approach is complemented by 8-bit fixed-point quantization and polynomial approximations to minimize quantization error, leading to significant improvements in accuracy and speed compared to existing ViT pruning methods \[[4](http://arxiv.org/abs/2211.08110)\]. 

In addition to these efforts, the concept of shared microexponents has been proposed to enable more flexible and efficient quantization formats. Block Data Representations (BDR) explore narrow-precision formats and demonstrate that shared microexponents can lead to better performance than traditional quantization approaches \[[1](http://arxiv.org/abs/2302.08007)\]. This idea is further extended in the context of MXInt, a new arithmetic format designed specifically for ViT accelerators, which allows for efficient mapping of complex operations onto hardware while maintaining high accuracy [10
## Research papers
### Outline
- [Microexponent-Based Quantization [1 papers]](#category-microexponent-based-quantization)
- [Hardware-Aware Quantization Frameworks [1 papers]](#category-hardware-aware-quantization-frameworks)
- [Quantization Techniques for Neural Networks [3 papers]](#category-quantization-techniques-for-neural-networks)
- [Token Pruning and Compression Methods [1 papers]](#category-token-pruning-and-compression-methods)

### <a id='category-microexponent-based-quantization'></a>Microexponent-Based Quantization: 1 papers found.
Context: 
	Document 1: [Category]: «Microexponent-Based Quantization»
[Snippet]: «This paper introduces Block Data Representations (BDR), a framework for
exploring and evaluating a wide spectrum of narrow-precision formats for deep
learning. It enables comparison of popular quantization standards, and through
BDR, new formats based on shared microexponents (MX) are identified, which
outperform other state-of-the-art quantization approaches, including
narrow-precision floating-point and block floating-point. MX utilizes multiple
levels of quantization scaling with ultra-fine scaling factors based on shared
microexponents in the hardware. The effectiveness of MX is demonstrated on
real-world models including large-scale generative pretraining and inferencing,
and production-scale recommendation systems.»
[_citation_number]: «1»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-28T10:15:37+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2005.03842)\]. Further details \[[6]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Vision Transformers (ViTs) leverage the transformer architecture to
effectively capture global context, demonstrating strong performance in
computer vision tasks. A major challenge in ViT hardware acceleration is that
the model family contains complex arithmetic operations that are sensitive to
model accuracy, such as the Softmax and LayerNorm operations, which cannot be
mapped onto efficient hardware with low precision. Existing methods only
exploit parallelism in the matrix multiplication operations of the model on
hardware and keep these complex operations on the CPU. This results in
suboptimal performance due to the communication overhead between the CPU and
accelerator. Can new data formats solve this problem?
  In this work, we present the first ViT accelerator that maps all operations
|    | reference                                                                                        |   date | key idea/summary                                                                                                                                                                                                                                          |
|----|--------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [With Shared Microexponents, A Little Shifting Goes a Long Way](http://arxiv.org/abs/2302.08007) |    nan | This paper introduces Block Data Representations (BDR) to evaluate narrow-precision formats for deep learning, leading to the identification of MX, a new quantization approach that outperforms existing methods in terms of efficiency and performance. |
### <a id='category-hardware-aware-quantization-frameworks'></a>Hardware-Aware Quantization Frameworks: 1 papers found.
Context: 
	Document 1: [Category]: «Hardware-Aware Quantization Frameworks»
[Snippet]: «Model quantization is a widely used technique to compress and accelerate deep
neural network (DNN) inference. Emergent DNN hardware accelerators begin to
support mixed precision (1-8 bits) to further improve the computation
efficiency, which raises a great challenge to find the optimal bitwidth for
each layer: it requires domain experts to explore the vast design space trading
off among accuracy, latency, energy, and model size, which is both
time-consuming and sub-optimal. Conventional quantization algorithm ignores the
different hardware architectures and quantizes all the layers in a uniform way.
In this paper, we introduce the Hardware-Aware Automated Quantization (HAQ)
framework which leverages the reinforcement learning to automatically determine
the quantization policy, and we take the hardware accelerator's feedback in the
design loop. Rather than relying on proxy signals such as FLOPs and model size,
we employ a hardware simulator to generate direct feedback signals (latency and
energy) to the RL agent. Compared with conventional methods, our framework is
fully automated and can specialize the quantization policy for different neural
network architectures and hardware architectures. Our framework effectively
reduced the latency by 1.4-1.95x and the energy consumption by 1.9x with
negligible loss of accuracy compared with the fixed bitwidth (8 bits)
quantization. Our framework reveals that the optimal policies on different
hardware architectures (i.e., edge and cloud architectures) under different
resource constraints (i.e., latency, energy and model size) are drastically
different. We interpreted the implication of different quantization policies,
which offer insights for both neural network architecture design and hardware
architecture design.»
[_citation_number]: «2»


Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-28T10:15:37+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description
|    | reference                                                                                          |   date | key idea/summary                                                                                                                                                                                                                                         |
|----|----------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [HAQ: Hardware-Aware Automated Quantization with Mixed Precision](http://arxiv.org/abs/1811.08886) |    nan | The HAQ framework uses reinforcement learning to automatically determine optimal bitwidths for neural network layers, considering hardware constraints, leading to significant improvements in latency and energy efficiency with minimal accuracy loss. |
### <a id='category-quantization-techniques-for-neural-networks'></a>Quantization Techniques for Neural Networks: 3 papers found.
Context: 
	Document 1: [Category]: «Quantization Techniques for Neural Networks»
[Snippet]: «Attention-based models have demonstrated remarkable success in various
natural language understanding tasks. However, efficient execution remains a
challenge for these models which are memory-bound due to their massive number
of parameters. We present GOBO, a model quantization technique that compresses
the vast majority (typically 99.9%) of the 32-bit floating-point parameters of
state-of-the-art BERT models and their variants to 3 bits while maintaining
their accuracy. Unlike other quantization methods, GOBO does not require
fine-tuning nor retraining to compensate for the quantization error. We present
two practical hardware applications of GOBO. In the first GOBO reduces memory
storage and traffic and as a result inference latency and energy consumption.
This GOBO memory compression mechanism is plug-in compatible with many
architectures; we demonstrate it with the TPU, Eyeriss, and an architecture
using Tensor Cores-like units. Second, we present a co-designed hardware
architecture that also reduces computation. Uniquely, the GOBO architecture
maintains most of the weights in 3b even during computation, a property that:
(1) makes the processing elements area efficient, allowing us to pack more
compute power per unit area, (2) replaces most multiply-accumulations with
additions, and (3) reduces the off-chip traffic by amplifying on-chip memory
capacity.»
[_citation_number]: «3»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-28T10:15:37+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](http://arxiv.org/abs/2005.03842)\]. Further details \[[6]()\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper
|    | reference                                                                                                                       |   date | key idea/summary                                                                                                                                                                                                                        |
|----|---------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [GOBO: Quantizing Attention-Based NLP Models for Low Latency and Energy
  Efficient Inference](http://arxiv.org/abs/2005.03842) |    nan | GOBO is a model quantization technique that compresses BERT models to 3 bits with high accuracy, without requiring fine-tuning, and enables efficient hardware implementations for reduced memory, computation, and energy consumption. |
|  1 | [LQ-Nets: Learned Quantization for Highly Accurate and Compact Deep Neural Networks]()                                          |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                               |
|  2 | [Quantizing deep convolutional networks for efficient inference: A whitepaper]()                                                |    nan | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                               |
### <a id='category-token-pruning-and-compression-methods'></a>Token Pruning and Compression Methods: 1 papers found.
Context: 
	Document 1: [Category]: «Token Pruning and Compression Methods»
[Snippet]: «While vision transformers (ViTs) have continuously achieved new milestones in
the field of computer vision, their sophisticated network architectures with
high computation and memory costs have impeded their deployment on
resource-limited edge devices. In this paper, we propose a hardware-efficient
image-adaptive token pruning framework called HeatViT for efficient yet
accurate ViT acceleration on embedded FPGAs. By analyzing the inherent
computational patterns in ViTs, we first design an effective attention-based
multi-head token selector, which can be progressively inserted before
transformer blocks to dynamically identify and consolidate the non-informative
tokens from input images. Moreover, we implement the token selector on hardware
by adding miniature control logic to heavily reuse existing hardware components
built for the backbone ViT. To improve the hardware efficiency, we further
employ 8-bit fixed-point quantization, and propose polynomial approximations
with regularization effect on quantization error for the frequently used
nonlinear functions in ViTs. Finally, we propose a latency-aware multi-stage
training strategy to determine the transformer blocks for inserting token
selectors and optimize the desired (average) pruning rates for inserted token
selectors, in order to improve both the model accuracy and inference latency on
hardware. Compared to existing ViT pruning studies, under the similar
computation cost, HeatViT can achieve 0.7%$\sim$8.9% higher accuracy; while
under the similar model accuracy, HeatViT can achieve more than
28.4%$\sim$65.3% computation reduction, for various widely used ViTs, including
DeiT-T, DeiT-S, DeiT-B, LV-ViT-S, and LV-ViT-M, on the ImageNet dataset.
Compared to the baseline hardware accelerator, our implementations of HeatViT
on the Xilinx ZCU102 FPGA achieve 3.46$\times$$\sim$4.89$\times$ speedup.»
[_citation_number]: «4»

Instruction: You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-28T10
|    | reference                                                                                                       |   date | key idea/summary                                                                                                                                                                                                    |
|----|-----------------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [HeatViT: Hardware-Efficient Adaptive Token Pruning for Vision
  Transformers](http://arxiv.org/abs/2211.08110) |    nan | HeatViT is a hardware-efficient image-adaptive token pruning framework for accelerating ViT models on embedded FPGAs, achieving higher accuracy and significant computation reduction compared to existing methods. |
