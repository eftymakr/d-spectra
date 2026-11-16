## Related Works

Instruction-following text embedding is a critical area of research, aiming to generate dynamic text embeddings that adapt to user instructions by highlighting specific attributes of text. Several recent works have explored this task, focusing on improving the efficiency and effectiveness of instruction-aware embeddings. However, existing methods often suffer from significant computational overhead, as they require re-encoding the entire corpus for each new instruction \[[Letian Peng' 2024-02-15](http://arxiv.org/abs/2402.09642v1)\]. 

One line of research has focused on instruction-tuning models using large-scale datasets. For instance, \[[Yuchen Zhuang' 2025-05-27](http://arxiv.org/abs/2505.21439v1)\] introduces InBedder, which treats instructions as questions about the input text and encodes the expected answers to obtain the representation. This approach significantly improves instruction-following capabilities, as demonstrated by experiments on both large language models and smaller encoder-based models. However, InBedder still requires re-encoding the entire corpus for each instruction, leading to high computational costs \[[Yuchen Zhuang' 2025-05-27](http://arxiv.org/abs/2505.21439v1)\].

Another approach is to use instruction-following speech recognition, which enables models to understand and execute a diverse set of free-form text instructions without relying on predefined command sets \[[Renze Lou' 2023-03-18](http://arxiv.org/abs/2303.10475v8)\]. This work trains a Listen-Attend-Spell model to interpret and execute simple instructions without requiring LLMs or pre-trained speech modules. While this method is promising, it is limited to speech recognition tasks and does not directly address the challenge of instruction-following text embedding \[[Renze Lou' 2023-03-18](http://arxiv.org/abs/2303.10475v8)\].

To reduce computational overhead, some studies have proposed lightweight transformation mechanisms. For example, \[[Aditi Jha' 2023-11-22](http://arxiv.org/abs/2311.13133v1)\] introduces a method that uses a small amount of text data with instruction-focused label annotation to adapt pre-computed embeddings in real time. This approach avoids re-encoding the entire corpus for each instruction, making it more efficient. However, it is limited to specific domains and does not generalize well to diverse instruction-following tasks \[[Aditi Jha' 2023-11-22](http://arxiv.org/abs/2311.13133v1)\].

In addition, \[[Juncheng Xie' 2024-08-27](http://arxiv.org/abs/2409.00096v1)\] explores the use of spherical text embeddings, which are designed to capture directional similarity in tasks such as word similarity and document clustering. While this work does not directly address instruction-following, it provides insights into how embeddings can be optimized for specific tasks, which is relevant to the broader field of instruction-aware embeddings \[[Juncheng Xie' 2024-08-27](http://arxiv.org/abs/2409.00096v1)\].

Recent work on instruction-following has also focused on improving the robustness of LLMs against prompt injection attacks \[[Bar Karov' 2025-03-05](http://arxiv.org/abs/2503.03669v1)\]. This research highlights the importance of understanding how models process and follow instructions, which is crucial for developing more reliable instruction-following systems. However, it does not directly address the computational efficiency of instruction-following text embedding \[[Bar Karov' 2025-03-05](http://arxiv.org/abs/2503.03669v1)\].

Furthermore, \[[Rob Grzywinski' 2023-11-27](http://arxiv.org/abs/2311.16338v1)\] proposes a method that uses non-instructional data to fine-tune pre-trained LLMs, enabling them to gain instruction-following capabilities without requiring explicit instruction-response pairs. This approach demonstrates that pre-trained models can be adapted to follow instructions using diverse, unlabeled data \[[Rob Grzywinski' 2023-11-27](http://arxiv.org/abs/2311.16338v1)\].

In addition, \[[Baolin Peng' 2023-04-06](http://arxiv.org/abs/2304.03277v1)\] introduces a structured reasoning approach called Attentive Reasoning Queries (ARQs), which improves instruction-following by guiding LLMs through systematic reasoning steps with targeted queries. This method is particularly effective in complex, use-case-specific scenarios where adherence to instructions is critical \[[Baolin Peng' 2023-04-06](http://arxiv.org/abs/2304.03277v1)\].

Finally, \[[Juyeon Heo' 2024-10-18](http://arxiv.org/abs/2410.14516v5)\] investigates whether LLMs encode information in their representations that correlate with instruction-following success. This work identifies a direction in the input embedding space that predicts whether a response will comply with a given instruction, providing insights into how models internally process and follow instructions \[[Juyeon Heo' 2024-10-18](http://arxiv.org/abs/2410.14516v5)\].

In summary, while several recent works have explored instruction-following text embedding, most suffer from significant computational overhead due to the need to re-encode the entire corpus for each instruction. Our approach, GSTransform, addresses this challenge by using a lightweight transformation mechanism that adapts pre-computed embeddings in real time, guided by a small amount of instruction-focused label annotation \[[Letian Peng' 2024-02-15](http://arxiv.org/abs/2402.09642v1)\].

### References

1. [Document 1]  
2. [Document 2]  
3. [Document 4]  
4. [Document 5]  
5. [Document 6]  
6. [Document 7]  
7. [Document 8]  
8. [Document 9]
