## Related Works

Modern databases often trade strong transactional isolation for weaker guarantees to achieve higher availability and performance \[[14](http://arxiv.org/abs/1302.0309)\]. This shift has led to the emergence of weak isolation levels such as Read Committed (RC), Read Atomic (RA), and Causal Consistency (CC), which allow for more concurrency but introduce subtle correctness risks \[[16](http://arxiv.org/abs/1905.08406)\]. The importance of verifying these weaker isolation levels has been increasingly recognized, as several production databases have been found to suffer from isolation bugs that violate their data-consistency guarantees \[[3](https://www.semanticscholar.org/paper/cbe191bda20907994d45bc835d20446968370add)\]. 

Black-box testing has become a prominent technique for detecting such bugs, as it allows for the verification of whether a database's transaction histories adhere to a prescribed isolation level without requiring access to internal implementation details \[[3](https://www.semanticscholar.org/paper/cbe191bda20907994d45bc835d20446968370add)\]. However, existing testers often suffer from high polynomial complexity, limiting their applicability to only moderate-sized workloads \[[1](https://www.semanticscholar.org/paper/615ff2896b52bee2cbfd64ced324106a29b73397)\]. This limitation is particularly problematic given the need to test large-scale databases under realistic, high-throughput conditions \[[1](https://www.semanticscholar.org/paper/615ff2896b52bee2cbfd64ced324106a29b73397)\].

Recent work has shown that testing weak isolation levels can be done in polynomial time, which has enabled the scalability of testing tools \[[1](https://www.semanticscholar.org/paper/615ff2896b52bee2cbfd64ced324106a29b73397)\]. For example, Plume presents a black-box checker for weak isolation levels, leveraging modular, fine-grained transactional anomalous patterns to detect violations \[[3](https://www.semanticscholar.org/paper/cbe191bda20907994d45bc835d20446968370add)\]. Similarly, Elle infers isolation anomalies from experimental observations by generating client workloads and injecting faults to produce anomalies that witness a violation of a stated guarantee \[[4](http://arxiv.org/abs/2003.10554)\]. These tools, however, often lack efficiency and completeness, especially when dealing with large-scale workloads \[[4](http://arxiv.org/abs/2003.10554)\].

The complexity of checking transactional consistency has also been studied, with results showing that certain consistency models like read committed, read atomic, and causal consistency are polynomial-time checkable, while others such as snapshot isolation are NP-complete \[[2](http://arxiv.org/abs/1908.04509)\]. This has motivated the development of more efficient algorithms that can handle large workloads under fixed parameters, such as the number of sessions \[[2](http://arxiv.org/abs/1908.04509)\]. Viper, for instance, introduces BC-polygraphs to efficiently check snapshot isolation, achieving soundness, completeness, and speed \[[6](https://www.semanticscholar.org/paper/9f96a48d2bc0e77004b32960495685be6c301c63)\]. Similarly, PolySI presents a black-box checker for snapshot isolation that uses generalized polygraphs and SMT solvers to detect violations and provide understandable counterexamples \[[7](http://arxiv.org/abs/2301.07313)\].

In this context, AWDIT represents a significant advancement, as it provides a highly-efficient and provably optimal tester for weak isolation levels. AWDIT achieves time complexities of $O(n^(3/2))$, $O(n^(3/2))$, and $O(n \cdot k)$ for RC, RA, and CC, respectively, improving significantly over the state of the art \[[1](https://www.semanticscholar.org/paper/615ff2896b52bee2cbfd64ced324106a29b73397)\]. Moreover, AWDIT is shown to be essentially optimal, with a conditional lower bound of $n^(3/2)$ for any weak isolation level between RC and CC \[[1](https://www.semanticscholar.org/paper/615ff2896b52bee2cbfd64ced324106a29b73397)\]. Experimental results demonstrate that AWDIT is significantly faster than existing, highly optimized testers, achieving average speedups of up to $245\times$ for the largest histories \[[1](https://www.semanticscholar.org/paper/615ff2896b52bee2cbfd64ced324106a29b73397)\].

References  
\[[1](https://www.semanticscholar.org/paper/615ff2896b52bee2cbfd64ced324106a29b73397)\] AWDIT: A Highly-Efficient and Provably Optimal Tester for Weak Database Isolation  
\[[2](http://arxiv.org/abs/1908.04509)\] On the Complexity of Checking Transactional Consistency  
\[[3](https://www.semanticscholar.org/paper/cbe191bda20907994d45bc835d20446968370add)\] Plume: Efficient and Complete Black-Box Checking of Weak Isolation Levels  
\[[4](http://arxiv.org/abs/2003.10554)\] Elle: Inferring Isolation Anomalies from Experimental Observations  
\[[5](https://www.semanticscholar.org/paper/4f3081dbb68287f0d9d7bec3e7173e6c8ff035b9)\] IsoVista: Black-box Checking Database Isolation Guarantees  
\[[6](https://www.semanticscholar.org/paper/9f96a48d2bc0e77004b32960495685be6c301c63)\] Viper: A Fast Snapshot Isolation Checker  
\[[7](http://arxiv.org/abs/2301.07313)\] Efficient Black-box Checking of Snapshot Isolation in Databases  
\[[8](https://www.semanticscholar.org/paper/38c443a37914e287c42a3238ccebd7372847d5f9)\] A critique of ANSI SQL isolation levels  
\[[9](http://arxiv.org/abs/1806.08416)\] Automated Detection of Serializability Violations under Weak Consistency  
\[[10](https://www.semanticscholar.org/paper/04178561c9d8cd42904ed0a836e08e55b84703cf)\] Validating Database System Isolation Level Implementations with Version Certificate Recovery  
\[[11](https://www.semanticscholar.org/paper/e7ab23d011e5183db78cfea48e303210f6e57e2e)\] The serializability of concurrent database updates  
\[[12](https://www.semanticscholar.org/paper/f919753a96bb2804f720f30df3e73ca24f419d32)\] NOC-NOC: Towards Performance-optimal Distributed Transactions  
\[[13](https://www.semanticscholar.org/paper/405ae0ebf74cfbf5f2edec62e2966827dcdc9bef)\] IsoDiff: A Tool for Debugging Anomalies Caused by Weak Isolation  
\[[14](http://arxiv.org/abs/1302.0309)\] Highly Available Transactions: Virtues and Limitations  
\[[15](https://www.semanticscholar.org/paper/050f5d841bc838fb4eded506d2084f4b3edf304b)\] Seeing is Believing: A Client-Centric Specification of Database Isolation  
\[[16](http://arxiv.org/abs/1905.08406)\] Checking Robustness Against Snapshot Isolation
## Research papers
### Outline
- [Database Isolation Levels and Their Trade-offs [3 papers]](#category-database-isolation-levels-and-their-trade-offs)
- [Complexity of Isolation Testing and Its Implications [1 papers]](#category-complexity-of-isolation-testing-and-its-implications)
- [Tools for Detecting Isolation Anomalies [7 papers]](#category-tools-for-detecting-isolation-anomalies)
- [Theoretical Foundations of Transactional Consistency [5 papers]](#category-theoretical-foundations-of-transactional-consistency)

### <a id='category-database-isolation-levels-and-their-trade-offs'></a>Database Isolation Levels and Their Trade-offs: 3 papers found.
Context: 
	Document 1: [Category]: «Database Isolation Levels and Their Trade-offs»
[Snippet]: «Modern applications, such as social networking systems and e-commerce platforms are centered around using large-scale storage systems for storing and retrieving data. In the presence of concurrent accesses, these storage systems trade off isolation for performance. The weaker the isolation level, the more behaviors a storage system is allowed to exhibit and it is up to the developer to ensure that their application can tolerate those behaviors. However, these weak behaviors only occur rarely in practice and outside the control of the application, making it difficult for developers to test the robustness of their code against weak isolation levels. This paper presents MonkeyDB, a mock storage system for testing storage-backed applications. MonkeyDB supports a key-value interface as well as SQL queries under multiple isolation levels. It uses a logical specification of the isolation level to compute, on a read operation, the set of all possible return values. MonkeyDB then returns a value randomly from this set. We show that MonkeyDB provides good coverage of weak behaviors, which is complete in the limit. We test a variety of applications for assertions that fail only under weak isolation. MonkeyDB is able to break each of those assertions in a small number of attempts.»
[_citation_number]: «1»

	Document 2: [Category]: «Database Isolation Levels and Their Trade-offs»
[Snippet]: «ANSI SQL-92 [MS, ANSI] defines Isolation Levels in terms of phenomena: Dirty Reads, Non-Repeatable Reads, and Phantoms. This paper shows that these phenomena and the ANSI SQL definitions fail to properly characterize several popular isolation levels, including the standard locking implementations of the levels covered. Ambiguity in the statement of the phenomena is investigated and a more formal statement is arrived at; in addition new phenomena that better characterize isolation types are introduced. Finally, an important multiversion isolation type, called Snapshot Isolation, is defined.»
[_citation_number]: «8»

	Document 3: [Category]: «Database Isolation Levels and Their Trade-offs»
[Snippet]: «»
[_citation_number]: «15»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-09T15:30:09+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](https://www.semanticscholar.org/paper/cbe191bda20907994d45bc835d20446968370add)\]. Further details \[[6](https://www.semanticscholar.org/paper/9f96a48d2bc0e77004b32960495685be6c301c63)\]\[[7](http://arxiv.org/abs/2301.07313)\]\[[8](https://www.semanticscholar.org/paper/38c443a37914e287c42a3238ccebd7372847d5f9)\]\[[9](http://arxiv.org/abs/1806.08416)\]\[[10](https://www.semanticscholar.org/paper/04178561c9d8cd42904ed0a836e08e55b84703cf)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In order to achieve low latency, high throughput, and partition tolerance,
modern databases forgo strong transaction isolation for weak isolation
guarantees. However, several production databases have been found to suffer
from isolation bugs, breaking their data-consistency contract. Black-box
testing is a prominent technique for detecting isolation bugs, by checking
whether histories of database transactions adhere to a prescribed isolation
level.
  Testing databases on realistic workloads of large size requires isolation
testers to be as efficient as possible, a requirement that has initiated a
study of the complexity of isolation testing. Although testing strong isolation
has been known to be NP-complete, weak isolation levels were recently shown to
be testable in polynomial time, which has propelled the scalability of testing
tools. However, existing testers have a large polynomial complexity,
restricting testing to workloads of only moderate size, which is not typical of
large-scale databases.
  In this work, we develop AWDIT, a highly-efficient and provably optimal
tester for weak database isolation. Given a history $H$ of size $n$ and $k$
sessions, AWDIT tests whether H satisfies the most common weak isolation levels
of Read Committed (RC), Read Atomic (RA), and Causal Consistency (CC) in time
$O(n^(3/2))$, $O(n^(3/2))$, and $O(n \cdot k)$, respectively, improving
significantly over the state of the art. Moreover, we prove that AWDIT is
essentially optimal, in the sense that there is a conditional lower bound of
$n^(3/2)$ for any weak isolation level between RC and CC. Our experiments show
that AWDIT is significantly faster than existing, highly optimized testers;
e.g., for the $\sim$20% largest histories, AWDIT obtains an average speedup of
$245\times$, $193\times$, and $62\times$ for RC, RA, and CC, respectively, over
the best baseline.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](https://www.semanticscholar.org/paper/cbe191bda20907994d45bc835d20446968370add)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1908.04509)\]\[[7](http://arxiv.org/abs/2301.07313)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The trade-offs between isolation levels and performance in database systems have been extensively studied, particularly in the context of modern applications that prioritize scalability and concurrency \[[1](https://www.semanticscholar.org/paper/615ff2896b52bee2cbfd64ced324106a29b73397)\]. These systems often adopt weaker isolation levels to achieve higher throughput and lower latency, but this introduces challenges in ensuring data consistency and robustness \[[1](https://www.semanticscholar.org/paper/615ff2896b52bee2cbfd64ced324106a29b73397)\]. Researchers have highlighted the difficulty developers face in testing applications against weak isolation behaviors, which can occur unpredictably and are hard to simulate \[[1](https://www.semanticscholar.org/paper/615ff2896b52bee2cbfd64ced324106a29b73397)\]. To address this, tools like MonkeyDB have been developed to provide a mock environment for testing storage systems under various isolation levels \[[1](https://www.semanticscholar.org/paper/615ff2896b52bee2cbfd64ced324106a29b73397)\]. Additionally, the formalization of isolation levels and their associated phenomena, such as Dirty Reads, Non-Repeatable Reads, and Phantoms, has been refined to better characterize different isolation types, including Snapshot Isolation \[[8](https://www.semanticscholar.org/paper/38c443a37914e287c42a3238ccebd7372847d5f9)\]. These advancements have laid the groundwork for more accurate and efficient testing methodologies, which are crucial for identifying and mitigating isolation bugs in production databases.
|    | reference                                                                                                                                                   | date     | key idea/summary                                                                                                                                                                                                                     |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [MonkeyDB: effectively testing correctness under weak isolation levels](https://www.semanticscholar.org/paper/615ff2896b52bee2cbfd64ced324106a29b73397)     | 10/15/21 | MonkeyDB is a mock storage system designed to test storage-backed applications under weak isolation levels by simulating all possible return values for read operations, enabling developers to verify the robustness of their code. |
|  1 | [A critique of ANSI SQL isolation levels](https://www.semanticscholar.org/paper/38c443a37914e287c42a3238ccebd7372847d5f9)                                   | 05/22/95 | The paper identifies flaws in the ANSI SQL-92 definitions of isolation levels and introduces a more formal characterization, including new phenomena and the definition of Snapshot Isolation.                                       |
|  2 | [Seeing is Believing: A Client-Centric Specification of Database Isolation](https://www.semanticscholar.org/paper/050f5d841bc838fb4eded506d2084f4b3edf304b) | 07/25/17 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                            |
### <a id='category-complexity-of-isolation-testing-and-its-implications'></a>Complexity of Isolation Testing and Its Implications: 1 papers found.
Context: 
	Document 1: [Category]: «Complexity of Isolation Testing and Its Implications»
[Snippet]: «Transactions simplify concurrent programming by enabling computations on shared data that are isolated from other concurrent computations and are resilient to failures. Modern databases provide different consistency models for transactions corresponding to different tradeoffs between consistency and availability. In this work, we investigate the problem of checking whether a given execution of a transactional database adheres to some consistency model. We show that consistency models like read committed, read atomic, and causal consistency are polynomial-time checkable while prefix consistency and snapshot isolation are NP-complete in general. These results complement a previous NP-completeness result concerning serializability. Moreover, in the context of NP-complete consistency models, we devise algorithms that are polynomial time assuming that certain parameters in the input executions, e.g., the number of sessions, are fixed. We evaluate the scalability of these algorithms in the context of several production databases.»
[_citation_number]: «2»

Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-09T15:30:09+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](https://www.semanticscholar.org/paper/cbe191bda20907994d45bc835d20446968370add)\]. Further details \[[6](https://www.semanticscholar.org/paper/9f96a48d2bc0e77004b32960495685be6c301c63)\]\[[7](http://arxiv.org/abs/2301.07313)\]\[[8](https://www.semanticscholar.org/paper/38c443a37914e287c42a3238ccebd7372847d5f9)\]\[[9](http://arxiv.org/abs/1806.08416)\]\[[10](https://www.semanticscholar.org/paper/04178561c9d8cd42904ed0a836e08e55b84703cf)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In order to achieve low latency, high throughput, and partition tolerance,
modern databases forgo strong transaction isolation for weak isolation
guarantees. However, several production databases have been found to suffer
from isolation bugs, breaking their data-consistency contract. Black-box
testing is a prominent technique for detecting isolation bugs, by checking
whether histories of database transactions adhere to a prescribed isolation
level.
  Testing databases on realistic workloads of large size requires isolation
testers to be as efficient as possible, a requirement that has initiated a
study of the complexity of isolation testing. Although testing strong isolation
has been known to be NP-complete, weak isolation levels were recently shown to
be testable in polynomial time, which has propelled the scalability of testing
tools. However, existing testers have a large polynomial complexity,
restricting testing to workloads of only moderate size, which is not typical of
large-scale databases.
  In this work, we develop AWDIT, a highly-efficient and provably optimal
tester for weak database isolation. Given a history $H$ of size $n$ and $k$
sessions, AWDIT tests whether H satisfies the most common weak isolation levels
of Read Committed (RC), Read Atomic (RA), and Causal Consistency (CC) in time
$O(n^(3/2))$, $O(n^(3/2))$, and $O(n \cdot k)$, respectively, improving
significantly over the state of the art. Moreover, we prove that AWDIT is
essentially optimal, in the sense that there is a conditional lower bound of
$n^(3/2)$ for any weak isolation level between RC and CC. Our experiments show
that AWDIT is significantly faster than existing, highly optimized testers;
e.g., for the $\sim$20% largest histories, AWDIT obtains an average speedup of
$245\times$, $193\times$, and $62\times$ for RC, RA, and CC, respectively, over
the best baseline.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](https://www.semanticscholar.org/paper/cbe191bda20907994d45bc835d20446968370add)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1908.04509)\]\[[7](http://arxiv.org/abs/2301.07313)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
The complexity of isolation testing has been a central topic in the study of transactional systems, particularly in understanding the trade-offs between consistency and performance \[[2](http://arxiv.org/abs/1908.04509)\]. Recent work has shown that certain consistency models, such as read committed, read atomic, and causal consistency, can be checked in polynomial time, which is a significant improvement over earlier results that classified serializability and snapshot isolation as NP-complete \[[2](http://arxiv.org/abs/1908.04509)\]. These findings are crucial for the development of efficient testing tools, as they enable the verification of transactional histories without incurring prohibitive computational costs. However, for more complex models like prefix consistency, the problem remains NP-complete, necessitating the use of parameterized algorithms that can handle large-scale workloads under specific constraints \[[2](http://arxiv.org/abs/1908.04509)\]. This research highlights the importance of understanding the computational complexity of isolation testing, as it directly impacts the feasibility of deploying robust testing strategies in production environments.
|    | reference                                                                                  | date     | key idea/summary                                                                                                                                                                                                                                                              |
|----|--------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [On the complexity of checking transactional consistency](http://arxiv.org/abs/1908.04509) | 08/13/19 | The paper investigates the complexity of checking consistency models in transactional databases, showing some models are polynomial-time checkable while others are NP-complete, and proposes efficient algorithms for NP-complete cases under certain parameter assumptions. |
### <a id='category-tools-for-detecting-isolation-anomalies'></a>Tools for Detecting Isolation Anomalies: 7 papers found.
The category "Tools for Detecting Isolation Anomalies" encompasses a range of approaches aimed at identifying and validating transactional isolation guarantees in databases, particularly in the context of weak isolation levels such as Read Committed (RC), Snapshot Isolation (SI), and Causal Consistency (CC). These tools are crucial as they help detect bugs that may compromise data consistency, especially in production databases where isolation guarantees are often not fully realized \[[3](https://www.semanticscholar.org/paper/cbe191bda20907994d45bc835d20446968370add)\]. For instance, Plume introduces a black-box checker that leverages vectors and tree clocks to efficiently detect anomalies in weak isolation levels, offering a sound and complete characterization of these levels \[[3](https://www.semanticscholar.org/paper/cbe191bda20907994d45bc835d20446968370add)\]. Similarly, Elle focuses on generating client workloads and injecting faults to produce anomalies that witness a violation of stated guarantees, providing detailed explanations of detected issues \[[4](http://arxiv.org/abs/2003.10554)\]. IsoVista further advances this field by offering a comprehensive black-box isolation checking system that ensures both soundness and completeness, while also visualizing violation scenarios to aid in debugging \[[5](https://www.semanticscholar.org/paper/4f3081dbb68287f0d9d7bec3e7173e6c8ff035b9)\]. Viper, another notable tool, is designed to check Snapshot Isolation efficiently and soundly, using BC-polygraphs to represent transaction dependencies and enabling fast and accurate validation \[[6](https://www.semanticscholar.org/paper/9f96a48d2bc0e77004b32960495685be6c301c63)\]. PolySI extends this by providing a black-box checker for SI that can scale to large workloads and reproduce known anomalies, demonstrating its effectiveness in real-world scenarios \[[7](http://arxiv.org/abs/2301.07313)\]. Emme addresses the challenge of predicate operations by introducing a white-box approach that uses version certificate recovery and expected serialization order to enhance efficiency and accuracy \[[10](https://www.semanticscholar.org/paper/04178561c9d8cd42904ed0a836e08e55b84703cf)\]. These tools collectively highlight the ongoing efforts to improve the reliability and performance of isolation checkers, ensuring that databases adhere to their promised isolation guarantees while handling large-scale workloads \[[3](https://www.semanticscholar.org/paper/cbe191bda20907994d45bc835d20446968370add)\]\[[4](http://arxiv.org/abs/2003.10554)\]\[[5](https://www.semanticscholar.org/paper/4f3081dbb68287f0d9d7bec3e7173e6c8ff035b9)\]\[[6](https://www.semanticscholar.org/paper/9f96a48d2bc0e77004b32960495685be6c301c63)\]\[[7](http://arxiv.org/abs/2301.07313)\]\[[10](https://www.semanticscholar.org/paper/04178561c9d8cd42904ed0a836e08e55b84703cf)\].
|    | reference                                                                                                                                                                      | date     | key idea/summary                                                                                                                                                                                                                                                                         |
|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Plume: Efficient and Complete Black-Box Checking of Weak Isolation Levels](https://www.semanticscholar.org/paper/cbe191bda20907994d45bc835d20446968370add)                    | 10/08/24 | Plume is the first efficient, complete, black-box checker for weak isolation levels in databases, capable of detecting isolation bugs and validating isolation guarantees across various workloads.                                                                                      |
|  1 | [Elle: Inferring Isolation Anomalies from Experimental Observations](http://arxiv.org/abs/2003.10554)                                                                          | 03/23/20 | Elle is a novel checker that infers Adya-style dependency graphs between transactions to detect anomalies in database isolation guarantees, offering soundness, efficiency, and informative explanations.                                                                                |
|  2 | [IsoVista: Black-box Checking Database Isolation Guarantees](https://www.semanticscholar.org/paper/4f3081dbb68287f0d9d7bec3e7173e6c8ff035b9)                                   | 08/01/24 | IsoVista is the first black-box isolation checking system that effectively identifies isolation bugs, ensures accurate results, improves checking efficiency, and provides visualization and benchmarking tools for DBMSs and isolation checkers.                                        |
|  3 | [Viper: A Fast Snapshot Isolation Checker](https://www.semanticscholar.org/paper/9f96a48d2bc0e77004b32960495685be6c301c63)                                                     | 05/08/23 | Viper is a sound, complete, and fast snapshot isolation checker that supports various SI variants and improves over existing methods by 15× in workload sizes checked.                                                                                                                   |
|  4 | [Efficient Black-box Checking of Snapshot Isolation in Databases](http://arxiv.org/abs/2301.07313)                                                                             | 01/18/23 | PolySI is a black-box checker for Snapshot Isolation (SI) that efficiently identifies SI violations, provides counterexamples, and outperforms existing tools by leveraging generalized polygraphs and optimized SMT solving.                                                            |
|  5 | [Validating Database System Isolation Level Implementations with Version Certificate Recovery](https://www.semanticscholar.org/paper/04178561c9d8cd42904ed0a836e08e55b84703cf) | 04/22/24 | The paper introduces Emme, an efficient white-box checker for validating transaction isolation levels, addressing the limitations of existing checkers by handling predicate operations and improving performance through version certificate recovery and expected serialization order. |
|  6 | [IsoDiff](https://www.semanticscholar.org/paper/405ae0ebf74cfbf5f2edec62e2966827dcdc9bef)                                                                                      | 07/01/20 | IsoDiff is a tool designed to help developers debug anomalies caused by weak isolation levels in databases, by identifying representative subsets of anomalies and reducing false positives through correlation detection, timing relationship checks, and developer feedback.           |
### <a id='category-theoretical-foundations-of-transactional-consistency'></a>Theoretical Foundations of Transactional Consistency: 5 papers found.
Context: 
	Document 1: [Category]: «Theoretical Foundations of Transactional Consistency»
[Snippet]: «While a number of weak consistency mechanisms have been developed in recent years to improve performance and ensure availability in distributed, replicated systems, ensuring the correctness of transactional applications running on top of such systems remains a difficult and important problem. Serializability is a well-understood correctness criterion for transactional programs; understanding whether applications are serializable when executed in a weakly-consistent environment, however remains a challenging exercise. In this work, we combine a dependency graph-based characterization of serializability and leverage the framework of abstract executions to develop a fully-automated approach for statically finding bounded serializability violations under any weak consistency model. We reduce the problem of serializability to satisfiability of a formula in First-Order Logic (FOL), which allows us to harness the power of existing SMT solvers. We provide rules to automatically construct the FOL encoding from programs written in SQL (allowing loops and conditionals) and express consistency specifications as FOL formula. In addition to detecting bounded serializability violations, we also provide two orthogonal schemes to reason about unbounded executions by providing sufficient conditions (again, in the form of FOL formulae) whose satisfiability implies the absence of anomalies in any arbitrary execution. We have applied the proposed technique on TPC-C, a real-world database program with complex application logic, and were able to discover anomalies under Parallel Snapshot Isolation (PSI), and verify serializability for unbounded executions under Snapshot Isolation (SI), two consistency mechanisms substantially weaker than serializability.»
[_citation_number]: «9»

	Document 5: [Category]: «Theoretical Foundations of Transactional Consistency»
[Snippet]: «Transactional access to databases is an important abstraction allowing programmers to consider blocks of actions (transactions) as executing in isolation. The strongest consistency model is (\em serializability), which ensures the atomicity abstraction of transactions executing over a sequentially consistent memory. Since ensuring serializability carries a significant penalty on availability, modern databases provide weaker consistency models, one of the most prominent being \emph(snapshot isolation). In general, the correctness of a program relying on serializable transactions may be broken when using weaker models. However, certain programs may also be insensitive to consistency relaxations, i.e., all their properties holding under serializability are preserved even when they are executed over a weak consistent database and without additional synchronization. 
In this paper, we address the issue of verifying if a given program is (\em robust against snapshot isolation), i.e., all its behaviors are serializable even if it is executed over a database ensuring snapshot isolation. We show that this verification problem is polynomial time reducible to a state reachability problem in transactional programs over a sequentially consistent shared memory. This reduction opens the door to the reuse of the classic verification technology for reasoning about weakly-consistent programs. In particular, we show that it can be used to derive a proof technique based on Lipton's reduction theory that allows to prove programs robust.»
[_citation_number]: «16»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-04-09T15:30:09+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3](https://www.semanticscholar.org/paper/cbe191bda20907994d45bc835d20446968370add)\]. Further details \[[6](https://www.semanticscholar.org/paper/9f96a48d2bc0e77004b32960495685be6c301c63)\]\[[7](http://arxiv.org/abs/2301.07313)\]\[[8](https://www.semanticscholar.org/paper/38c443a37914e287c42a3238ccebd7372847d5f9)\]\[[9](http://arxiv.org/abs/1806.08416)\]\[[10](https://www.semanticscholar.org/paper/04178561c9d8cd42904ed0a836e08e55b84703cf)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: In order to achieve low latency, high throughput, and partition tolerance,
modern databases forgo strong transaction isolation for weak isolation
guarantees. However, several production databases have been found to suffer
from isolation bugs, breaking their data-consistency contract. Black-box
testing is a prominent technique for detecting isolation bugs, by checking
whether histories of database transactions adhere to a prescribed isolation
level.
  Testing databases on realistic workloads of large size requires isolation
testers to be as efficient as possible, a requirement that has initiated a
study of the complexity of isolation testing. Although testing strong isolation
has been known to be NP-complete, weak isolation levels were recently shown to
be testable in polynomial time, which has propelled the scalability of testing
tools. However, existing testers have a large polynomial complexity,
restricting testing to workloads of only moderate size, which is not typical of
large-scale databases.
  In this work, we develop AWDIT, a highly-efficient and provably optimal
tester for weak database isolation. Given a history $H$ of size $n$ and $k$
sessions, AWDIT tests whether H satisfies the most common weak isolation levels
of Read Committed (RC), Read Atomic (RA), and Causal Consistency (CC) in time
$O(n^(3/2))$, $O(n^(3/2))$, and $O(n \cdot k)$, respectively, improving
significantly over the state of the art. Moreover, we prove that AWDIT is
essentially optimal, in the sense that there is a conditional lower bound of
$n^(3/2)$ for any weak isolation level between RC and CC. Our experiments show
that AWDIT is significantly faster than existing, highly optimized testers;
e.g., for the $\sim$20% largest histories, AWDIT obtains an average speedup of
$245\times$, $193\times$, and $62\times$ for RC, RA, and CC, respectively, over
the best baseline.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3](https://www.semanticscholar.org/paper/cbe191bda20907994d45bc835d20446968370add)\]. Further details discussed in contexts \[[2](http://arxiv.org/abs/1908.04509)\]\[[7](http://arxiv.org/abs/2301.07313)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Theoretical Foundations of Transactional Consistency has seen significant advancements in addressing the challenges of ensuring correctness in weakly consistent environments. Research has focused on the verification of serializability in such systems, where traditional strong consistency models like serializability are often relaxed to improve performance and availability \[[16](http://arxiv.org/abs/1905.08406)\]. For instance, the work on snapshot isolation highlights how programs may still maintain correctness even under weaker consistency models, provided they are robust against such relaxations \[[16](http://arxiv.org/abs/1905.08406)\]. This has led to the development of automated approaches that leverage formal methods, such as First-Order Logic (FOL), to detect violations of bounded serializability and reason about unbounded executions \[[9](http://arxiv.org/abs/1806.08416)\]. These techniques are crucial for ensuring correctness in distributed systems where weak consistency is a necessity for scalability and fault tolerance. Additionally, the study of weak isolation levels, such as Read Committed (RC), Read Atomic (RA), and Causal Consistency (CC), has revealed that testing these models can be done in polynomial time, offering a scalable alternative to traditional strong isolation testing \[[16](http://arxiv.org/abs/1905.08406)\]. Theoretical work has also explored the trade-offs between consistency and availability, emphasizing the need for systems that can maintain transactional guarantees without sacrificing performance or fault tolerance \[[14](http://arxiv.org/abs/1302.0309)\]. These contributions form the foundation for modern approaches to ensuring correctness in weakly consistent transactional systems.
|    | reference                                                                                                                                       | date     | key idea/summary                                                                                                                                                                                                                                               |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Automated Detection of Serializability Violations under Weak Consistency](http://arxiv.org/abs/1806.08416)                                     | 06/01/18 | This work presents an automated approach to detect bounded serializability violations in weakly consistent distributed systems by reducing the problem to First-Order Logic satisfiability, enabling the use of SMT solvers for verification.                  |
|  1 | [The serializability of concurrent database updates](https://www.semanticscholar.org/paper/e7ab23d011e5183db78cfea48e303210f6e57e2e)            | 10/01/79 | The provided snippet does not contain any meaningful content or context to extract a key idea or summary.                                                                                                                                                      |
|  2 | [NOC-NOC: Towards Performance-optimal Distributed Transactions](https://www.semanticscholar.org/paper/f919753a96bb2804f720f30df3e73ca24f419d32) | 03/12/24 | The paper addresses the performance optimality of distributed database transactions by introducing a new design objective that optimizes both reads and writes, leading to the development of two new transaction algorithms that outperform existing methods. |
|  3 | [Highly Available Transactions: Virtues and Limitations](http://arxiv.org/abs/1302.0309)                                                        | 02/01/13 | This work introduces Highly Available Transactions (HATs), which provide transactional guarantees without unavailability during system partitions or high network latency, and analyzes their availability and performance benefits.                           |
|  4 | [Checking Robustness Against Snapshot Isolation](http://arxiv.org/abs/1905.08406)                                                               | 05/21/19 | The paper presents a method to verify if a program is robust against snapshot isolation, reducing the problem to a state reachability problem in transactional programs.                                                                                       |
