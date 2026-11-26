## Related Works

Long-form narrative summarization, encompassing books, movies, and TV scripts, remains a challenging task for existing large language models (LLMs) due to the complexity of capturing intricate plotlines, character interactions, and thematic coherence \[[13](http://arxiv.org/abs/2310.00785)\]. Prior work has explored various approaches to address these challenges, including abstractive summarization techniques, efficient attention mechanisms, and multi-agent collaboration frameworks. For instance, \[[2](http://arxiv.org/abs/2404.03561)\] introduced a two-stage abstractive summarization approach for movie scripts, where salient scenes are first identified and then used to generate summaries. This work highlights the importance of focusing on key narrative elements to improve summary quality. Similarly, \[[12](http://arxiv.org/abs/2406.02818)\] proposed Chain-of-Agents (CoA), a framework that enables multi-agent collaboration to process long-context tasks, mitigating the limitations of input reduction and window extension strategies. CoA processes the entire input by interleaving reading and reasoning, assigning each agent a short context to maintain focus on pertinent information.

Efficient attention mechanisms have also been crucial in enabling the processing of long sequences. Models such as Longformer \[[4](http://arxiv.org/abs/2004.05150)\], Reformer \[[5](http://arxiv.org/abs/2001.04451)\], and Linformer \[[6](http://arxiv.org/abs/2006.04768)\] have been developed to reduce the computational and memory costs associated with standard self-attention mechanisms. Longformer, for example, uses a combination of local and global attention to handle long documents, while Reformer employs locality-sensitive hashing to reduce attention complexity. Linformer further simplifies the attention mechanism by approximating it with a low-rank matrix, achieving linear complexity in both time and space. These advancements have made it possible to process long documents without truncation, which is essential for narrative summarization tasks.

In addition to attention mechanisms, the use of pre-trained models and fine-tuning strategies has played a significant role in improving summarization performance. \[[11](http://arxiv.org/abs/2501.01805)\] proposed CachED, an approach that enables end-to-end training of encoder-decoder models for long document summarization without input truncation. This method uses gradient caching to manage memory consumption during training, allowing models to process extensive documents. Similarly, \[[7](http://arxiv.org/abs/2306.15595)\] introduced Position Interpolation, which extends the context window sizes of RoPE-based LLMs to up to 32768 tokens with minimal fine-tuning, demonstrating strong performance on tasks requiring long context.

The importance of structured summarization pipelines has also been emphasized in recent work. \[[13](http://arxiv.org/abs/2310.00785)\] explored the challenges of summarizing book-length documents, highlighting the need for chunking and merging strategies to maintain coherence. They introduced BooookScore, an automatic metric to evaluate the quality of LLM-generated summaries, identifying common coherence errors and measuring their impact. This work underscores the need for robust evaluation methods when assessing long-form narrative summaries.

In summary, the field of long-form narrative summarization has seen significant advancements through the development of efficient attention mechanisms, multi-agent collaboration frameworks, and structured summarization pipelines. These approaches collectively address the challenges of capturing complex narratives and maintaining coherence in summaries.

References:  
\[[1](http://arxiv.org/abs/2005.01840)\] [Document 1]  
\[[2](http://arxiv.org/abs/2404.03561)\] [Document 2]  
\[[3](http://arxiv.org/abs/2007.14062)\] [Document 3]  
\[[4](http://arxiv.org/abs/2004.05150)\] [Document 4]  
\[[5](http://arxiv.org/abs/2001.04451)\] [Document 5]  
\[[6](http://arxiv.org/abs/2006.04768)\] [Document 6]  
\[[7](http://arxiv.org/abs/2306.15595)\] [Document 7]  
\[[8](http://arxiv.org/abs/2307.03172)\] [Document 8]  
\[[9](http://arxiv.org/abs/2208.00748)\] [Document 9]  
\[[10](http://arxiv.org/abs/2305.01625)\] [Document 10]  
\[[11](http://arxiv.org/abs/2501.01805)\] [Document 11]  
\[[12](http://arxiv.org/abs/2406.02818)\] [Document 12]  
\[[13](http://arxiv.org/abs/2310.00785)\] [Document 13]
