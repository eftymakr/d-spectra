## Related Works

The proliferation of open-source machine learning (ML) resources, particularly on platforms like Hugging Face, has spurred interest in understanding and managing the lifecycle, reuse, and documentation of ML models and datasets. However, these platforms often lack structured, semantically rich representations that facilitate advanced information retrieval (IR) tasks such as model evolution tracing and dataset recommendation.

Several studies have examined the characteristics and challenges of the Hugging Face ecosystem. Repository mining efforts have quantified the carbon footprint of ML models, revealing correlations between model attributes and emissions, and highlighting the need for improved transparency and sustainability in reporting practices \[[2305.11164](http://arxiv.org/abs/2305.11164)\]. Large-scale empirical analyses of model evolution and maintenance have shown iterative development patterns aligned with data science methodologies, emphasizing the importance of continuous documentation and release management for model quality \[[2311.1338](http://arxiv.org/abs/2311.13380)\]\[[2411.09645](http://arxiv.org/abs/2411.09645)\]. Additionally, the reuse of pretrained models (PTMs) within the Hugging Face community has been explored, identifying key challenges such as discrepancies between claimed and actual performance, provenance issues, and risks associated with model adoption, which complicate reuse and dependability \[[2303.02552](http://arxiv.org/abs/2303.02552)\]\[[2401.13177](http://arxiv.org/abs/2401.13177)\].

The documentation of ML datasets, critical for reproducibility and transparency, has also been scrutinized. Analysis of dataset cards on Hugging Face revealed uneven completion rates and highlighted which sections—such as dataset description and structure—receive more practitioner attention, while usage considerations and social impact disclosures remain underrepresented \[[2401.13822](http://arxiv.org/abs/2401.13822)\]. This underscores a broader challenge in ML supply chains: inconsistent documentation quality that impedes effective resource discovery and evaluation \[[2502.04484](http://arxiv.org/abs/2502.04484)\]. Relatedly, research on the licensing and supply chain relationships of models and datasets on Hugging Face points to complexities in compliance and security, reinforcing the need for automated consistency checks and improved metadata management \[[2502.04484](http://arxiv.org/abs/2502.04484)\].

Efforts to formalize and standardize model reporting have introduced frameworks like model cards, which provide structured documentation of model performance, intended use, and evaluation contexts to promote transparency and responsible deployment \[[1810.03993](http://arxiv.org/abs/1810.03993)\]. These frameworks support better understanding and selection of ML resources but remain underutilized or inconsistently applied in open repositories, presenting an opportunity for integration with structured knowledge representations.

From a broader software engineering perspective, the emergence of Pre-Trained Model Registries (PTMRs) like Hugging Face parallels traditional software package registries but exhibits unique dynamics such as higher turnover rates and distinct collaboration patterns \[[2406.08205](http://arxiv.org/abs/2406.08205)\]\[[2405.13058](http://arxiv.org/abs/2405.13058)\]. Studies characterizing the development activity and social network structures on Hugging Face reveal a core-periphery community with a small subset of highly active contributors driving the majority of model usage and updates, which influences model maintenance and evolution strategies \[[2405.13058](http://arxiv.org/abs/2405.13058)\]\[[2311.1338](http://arxiv.org/abs/2311.13380)\].

Security concerns have also been raised regarding the ML supply chain on Hugging Face. Unsafe serialization methods in shared models pose risks of malicious exploits, highlighting vulnerabilities in the ecosystem and the necessity for robust detection and mitigation mechanisms within model repositories \[[2410.0449](http://arxiv.org/abs/2410.04490)\].

While the importance of similarity search and efficient indexing for large-scale datasets has been well-established in other domains \[[1702.08734](http://arxiv.org/abs/1702.08734)\], these techniques have not yet been fully integrated with ML resource platforms to support enhanced IR functionalities, such as semantic search and relationship discovery among models and datasets.

Collectively, these bodies of work demonstrate the pressing need for structured, comprehensive knowledge representations that capture the complex relationships, attributes, and provenance of ML models and datasets. Such representations can enable advanced IR tasks including resource recommendation, classification, and tracing of model evolution, which are currently limited by the largely unstructured metadata and documentation on platforms like Hugging Face. The construction of a large-scale knowledge graph such as HuggingKG, coupled with benchmarking efforts like HuggingBench, directly addresses these gaps by providing structured, domain-specific relations and rich textual attributes to facilitate improved management and retrieval of ML resources.

References  
\[[2305.11164](http://arxiv.org/abs/2305.11164)\]  
\[[2311.1338](http://arxiv.org/abs/2311.13380)\]  
\[[2303.02552](http://arxiv.org/abs/2303.02552)\]  
\[[2401.13822](http://arxiv.org/abs/2401.13822)\]  
\[[2406.08205](http://arxiv.org/abs/2406.08205)\]  
\[[2401.13177](http://arxiv.org/abs/2401.13177)\]  
\[[1810.03993](http://arxiv.org/abs/1810.03993)\]  
\[[1702.08734](http://arxiv.org/abs/1702.08734)\]  
\[[2410.0449](http://arxiv.org/abs/2410.04490)\]  
\[[2502.04484](http://arxiv.org/abs/2502.04484)\]  
\[[2405.13058](http://arxiv.org/abs/2405.13058)\]  
\[[2411.09645](http://arxiv.org/abs/2411.09645)\]