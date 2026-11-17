## Related Works

Vision Transformers (ViTs) have revolutionized computer vision by leveraging self-attention mechanisms to capture global context, surpassing traditional CNNs in many tasks \[[2503.02891](http://arxiv.org/abs/2503.02891)\]. Despite their effectiveness, ViTs pose significant challenges for hardware acceleration, especially on resource-constrained platforms like FPGAs. This is largely due to the complex arithmetic operations inherent in ViTs, such as Softmax and LayerNorm, which are sensitive to precision and difficult to implement efficiently in low-precision hardware \[[2211.0811](http://arxiv.org/abs/2211.08110)\]. Existing accelerators typically focus on optimizing matrix multiplications while offloading these complex functions to CPUs, incurring costly communication overhead and limiting overall performance \[[2407.12736](http://arxiv.org/abs/2407.12736)\].

### Hardware Acceleration Approaches

Multiple efforts have targeted improving ViT inference efficiency through algorithm-hardware co-design. For instance, HeatViT employs adaptive token pruning on embedded FPGAs, dynamically removing non-informative tokens to reduce computation without degrading accuracy. It combines 8-bit fixed-point quantization and polynomial approximations for nonlinear functions, achieving substantial speedups (3.5×–4.9×) and computation reductions (up to 65%) with minimal hardware overhead \[[2205.11397](http://arxiv.org/abs/2205.11397)\]. Similarly, ViTA proposes a configurable hardware accelerator designed specifically for edge devices, optimizing pipeline and memory accesses to reach nearly 90% hardware utilization at low power consumption (~0.88W) \[[2211.05109](http://arxiv.org/abs/2211.05109)\].

Dedicated algorithm-hardware frameworks such as ViTCoD further advance ViT acceleration by pruning and polarizing attention maps into sparser and denser fixed patterns, significantly reducing expensive data movements. Integrating auto-encoder modules for computation-data trade-offs, ViTCoD achieves up to 235× speedup over CPUs and notable gains over prior Transformer accelerators \[[2210.09573](http://arxiv.org/abs/2210.09573)\]. Another innovative approach, VITALITY, approximates the softmax attention with a linear Taylor expansion combined with sparsity regularization, enabling a hardware accelerator that improves end-to-end efficiency by 3× in speed and energy while maintaining accuracy \[[2211.05109](http://arxiv.org/abs/2211.05109)\].

Beyond pruning and approximation, row-wise scheduling accelerators decompose ViT operations into unified dot products with weight sharing to reduce memory usage, achieving high throughput with modest hardware resources \[[2205.03998](http://arxiv.org/abs/2205.03998)\]. Additionally, N:M sparse Transformer acceleration frameworks exploit structured sparsity patterns for flexible model compression and efficient FPGA deployment, delivering speedups of over 14× relative to CPUs and outperforming prior FPGA accelerators \[[2208.06118](http://arxiv.org/abs/2208.06118)\].

### Quantization and Arithmetic Optimizations

Quantization plays a critical role in balancing accuracy and hardware efficiency for ViT deployment. Recent surveys highlight model quantization techniques tailored for ViTs, emphasizing algorithm-hardware co-design that adapts quantization schemes to hardware capabilities. This includes low-bit precision formats and hardware-friendly nonlinear function approximations, crucial for mapping softmax and layer normalization to accelerators \[[2405.00314](http://arxiv.org/abs/2405.00314)\]. HeatViT’s use of 8-bit fixed-point quantization combined with polynomial approximations exemplifies this trend \[[2205.11397](http://arxiv.org/abs/2205.11397)\].

Alternative numeric formats and quantization-aware training paradigms have also been explored. SuperViT introduces a versatile training approach enabling a single ViT model to adapt to multiple computational budgets by dynamically adjusting token keeping rates and patch sizes, achieving improved accuracy at reduced FLOPs \[[2108.0139](http://arxiv.org/abs/2108.01390)\]. Vicinity Vision Transformer integrates 2D locality bias with linear attention mechanisms, reducing computational complexity while maintaining high accuracy, demonstrating the importance of inductive biases to optimize ViT performance in hardware-constrained settings \[[2206.10552](http://arxiv.org/abs/2206.10552)\].

### Challenges in Mapping Complex Operations

The Softmax function and LayerNorm remain bottlenecks for efficient hardware implementation due to their nonlinear and precision-sensitive nature. Prior works proposing hardware-friendly alternatives include ConSmax, which replaces maximum searching and denominator summation with differentiable normalization parameters to enable parallelism \[[2501.07825](http://arxiv.org/abs/2501.07825)\], and Softermax, which uses base replacement and low-precision computations alongside online normalization to improve energy efficiency \[[2402.04563](http://arxiv.org/abs/2402.04563)\]. However, these methods have primarily targeted NLP transformers, with fewer solutions fully integrating such optimizations into ViT accelerators.

### Comprehensive ViT FPGA Frameworks

CHOSEN represents a comprehensive software-hardware co-design framework targeting FPGA deployment of ViTs. It optimizes memory bandwidth via multi-kernel designs exploiting multi-bank DDR memory, uses approximate nonlinear functions with minimal accuracy loss, and implements a compiler for design space exploration to maximize throughput and minimize latency. CHOSEN achieves 1.5× throughput gains on popular ViT variants, illustrating the benefits of holistic optimization strategies \[[2407.12736](http://arxiv.org/abs/2407.12736)\].

HeatViT and ViTA further demonstrate the feasibility and performance gains of fully mapping ViT operations, including complex arithmetic, onto FPGA hardware, though with trade-offs in resource utilization and accuracy \[[2205.11397](http://arxiv.org/abs/2205.11397)\]\[[2211.05109](http://arxiv.org/abs/2211.05109)\]. These advances underscore the importance of novel numeric formats and hardware-centric algorithm modifications to close the gap between accuracy and efficiency.

---

Collectively, these works reveal that while significant progress has been made in accelerating matrix operations and pruning tokens or attention maps, efficiently mapping complex nonlinear functions remains an open challenge. The introduction of new arithmetic formats like Microscaling Integer (MXInt), as proposed in this work, represents a promising direction to fully integrate all ViT operations on hardware, reducing communication overhead and achieving substantial speedups with minimal accuracy loss.

### References

\[[2503.02891](http://arxiv.org/abs/2503.02891)\] http://arxiv.org/abs/2503.02891  
\[[2211.0811](http://arxiv.org/abs/2211.08110)\] http://arxiv.org/abs/2405.00314  
\[[2407.12736](http://arxiv.org/abs/2407.12736)\] http://arxiv.org/abs/2407.12736  
\[[2210.09573](http://arxiv.org/abs/2210.09573)\] http://arxiv.org/abs/2210.09573  
\[[2205.11397](http://arxiv.org/abs/2205.11397)\] http://arxiv.org/abs/2211.08110  
\[[2211.05109](http://arxiv.org/abs/2211.05109)\] http://arxiv.org/abs/2302.09108  
\[[2108.0139](http://arxiv.org/abs/2108.01390)\] http://arxiv.org/abs/2205.11397  
\[[2501.07825](http://arxiv.org/abs/2501.07825)\] http://arxiv.org/abs/2402.10930  
\[[2402.04563](http://arxiv.org/abs/2402.04563)\] http://arxiv.org/abs/2103.09301  
\[[2405.00314](http://arxiv.org/abs/2405.00314)\] http://arxiv.org/abs/2405.00314  
\[[2205.03998](http://arxiv.org/abs/2205.03998)\] http://arxiv.org/abs/2205.03998  
\[[2208.06118](http://arxiv.org/abs/2208.06118)\] http://arxiv.org/abs/2208.06118  
\[[2206.10552](http://arxiv.org/abs/2206.10552)\] http://arxiv.org/abs/2206.10552