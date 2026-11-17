## Related Works

Generative retrieval (GR) has recently emerged as a compelling alternative to traditional index-retrieve paradigms in information retrieval (IR). Unlike classical methods that rely on static sparse or dense indexes, GR approaches directly generate document identifiers (docids) from queries using autoregressive language models, enabling an end-to-end retrieval process \[[2204.10628](http://arxiv.org/abs/2204.10628)\]\[[2202.06991](http://arxiv.org/abs/2202.06991)\]. This shift simplifies retrieval pipelines by embedding corpus knowledge into model parameters, removing the need for explicit indexing structures and allowing joint optimization of retrieval components \[[2208.07652](http://arxiv.org/abs/2208.07652)\]\[[2206.02743](http://arxiv.org/abs/2206.02743)\]\[[2208.09257](http://arxiv.org/abs/2208.09257)\].

Early GR models leveraged text-based docids such as document titles or distinctive n-grams, which capture semantic content and align well with the pre-trained language models’ knowledge. For example, SEAL uses n-grams as document identifiers, enabling effective passage-level retrieval with a lighter memory footprint than traditional methods \[[2204.10628](http://arxiv.org/abs/2204.10628)\]. Similarly, GENRE generates entities autoregressively by producing their unique textual names, which reduces memory requirements and improves retrieval quality \[[2010.00904](http://arxiv.org/abs/2010.00904)\]. These text-based identifiers provide fine-grained semantics and high lexical diversity, facilitating better generalization to unseen documents and dynamic corpora \[[2304.04171](http://arxiv.org/abs/2304.04171)\]\[[2305.16675](http://arxiv.org/abs/2305.16675)\].

Conversely, numeric-based docids, often constructed via clustering or hashing techniques, emphasize retrieval efficiency but suffer from limited semantic expressiveness. Such identifiers tend to overfit to the initial corpus distribution, negatively impacting performance in evolving or dynamic document collections where new documents continuously arrive \[[2203.00537](http://arxiv.org/abs/2203.00537)\]\[[2308.14968](http://arxiv.org/abs/2308.14968)\]. This phenomenon has been empirically observed, showing that numeric-based GR models degrade in effectiveness over dynamic corpora, largely due to their insufficient adaptability and over-reliance on static training data \[[2203.00537](http://arxiv.org/abs/2203.00537)\].

Addressing the challenges posed by dynamic corpora, recent works have introduced continual learning frameworks and hybrid docid designs. CLEVER proposes an incremental product quantization method combined with a memory-augmented learning mechanism to incorporate new documents dynamically while preventing catastrophic forgetting of prior knowledge \[[2308.14968](http://arxiv.org/abs/2308.14968)\]. This enables GR models to maintain retrieval accuracy across evolving datasets without full retraining. Furthermore, multiview docid strategies integrate both text-based and numeric-based identifiers, leveraging the semantic richness of text tokens and the efficiency of numeric codes to balance effectiveness and computational cost in dynamic settings \[[2305.16675](http://arxiv.org/abs/2305.16675)\].

The importance of semantic docid design has also been explored through learning-based tokenization methods. GenRet formulates docid learning as a discrete autoencoding problem, allowing the model to generate semantically meaningful and compact docids end-to-end, which improves robustness on unseen documents and dynamic benchmarks \[[2304.04171](http://arxiv.org/abs/2304.04171)\]. Similarly, RIPOR introduces relevance-based document ID construction and prefix-oriented ranking optimization, significantly improving large-scale generative retrieval performance on standard benchmarks such as MS MARCO \[[2311.09134](http://arxiv.org/abs/2311.09134)\].

While GR approaches have demonstrated strong performance on static corpora, their extension to multi-graded relevance settings has been less studied. GR² addresses this by jointly optimizing relevance and distinctness of docids, employing constrained contrastive training that respects graded relevance relationships, thereby enhancing retrieval fidelity beyond binary relevance assumptions \[[2409.18409](http://arxiv.org/abs/2409.18409)\].

In sum, the literature highlights three critical factors for effective generative retrieval in dynamic corpora: (i) semantic alignment of docids with pretrained language models, typically achieved via text-based or learned identifiers; (ii) fine-grained docid construction to capture document-level nuances; and (iii) strategies to maintain retrieval performance as the corpus evolves, including continual learning and multi-docid fusion. These insights underpin the development of more generalized and efficient GR models capable of robust performance in real-world, continuously changing information environments \[[2204.10628](http://arxiv.org/abs/2204.10628)\]\[[2203.00537](http://arxiv.org/abs/2203.00537)\]\[[2208.07652](http://arxiv.org/abs/2208.07652)\]\[[2308.14968](http://arxiv.org/abs/2308.14968)\]\[[2311.09134](http://arxiv.org/abs/2311.09134)\]\[[2304.04171](http://arxiv.org/abs/2304.04171)\]\[[2305.16675](http://arxiv.org/abs/2305.16675)\].

---

### References

1. http://arxiv.org/abs/2204.10628  
2. http://arxiv.org/abs/2308.14968  
4. http://arxiv.org/abs/2010.00904  
5. http://arxiv.org/abs/2202.06991  
7. http://arxiv.org/abs/2208.07652  
8. http://arxiv.org/abs/2308.14968  
9. http://arxiv.org/abs/2206.02743  
10. http://arxiv.org/abs/2311.09134  
11. http://arxiv.org/abs/2304.04171  
12. http://arxiv.org/abs/2409.18409  
13. http://arxiv.org/abs/2208.09257  
14. http://arxiv.org/abs/2305.16675