## Related Works

Memory bandwidth regulation and cache partitioning have been widely studied for achieving predictable timing in real-time computing systems \[[12' 2014-05-12](http://arxiv.org/abs/1405.2916v1)\]. These techniques, when combined with partitioned scheduling, require careful co-allocation of tasks and resources to cores, as task execution times strongly depend on available allocated resources \[[12' 2014-05-12](http://arxiv.org/abs/1405.2916v1)\]. Prior work has explored various methods for managing resource allocation and scheduling in real-time systems, including heuristic approaches and optimization-based frameworks \[[12' 2014-05-12](http://arxiv.org/abs/1405.2916v1)\].

A significant body of research has focused on the use of integer linear programming (ILP) for resource allocation and scheduling problems. For instance, the work by Balas and Mazzola on linearization techniques for quadratic 0-1 programs has been instrumental in developing cutting plane algorithms for such problems \[[1' 2012-04-21](http://arxiv.org/abs/1204.4829v1)\]. This approach has been further refined to improve the primal and dual formulations, enabling more efficient solutions \[[1' 2012-04-21](http://arxiv.org/abs/1204.4829v1)\]. Similarly, the paper by D. Pisinger introduces a new class of knapsack problems, known as spanner knapsack instances, which are challenging for traditional dynamic programming and branch-and-bound methods \[[3' 2019-02-15](http://arxiv.org/abs/1903.03494v1)\]. A genetic algorithm is proposed to address these instances, showing promising results in delivering optimal solutions within reasonable computational time \[[3' 2019-02-15](http://arxiv.org/abs/1903.03494v1)\].

The 0-1 integer linear programming problem with a linear number of constraints has also been studied, with an exact algorithm proposed that improves over exhaustive search by an exponential factor \[[4' 2014-01-21](http://arxiv.org/abs/1401.5512v2)\]. This algorithm reduces the problem to the Vector Domination problem and introduces a new method for solving this subproblem \[[4' 2014-01-21](http://arxiv.org/abs/1401.5512v2)\]. Additionally, the paper by D. Pisinger discusses the computational complexity of knapsack problems and highlights the challenges posed by spanner instances \[[3' 2019-02-15](http://arxiv.org/abs/1903.03494v1)\].

In the context of constraint satisfaction and optimization, the Lagrangian Dual Framework has been applied to approximate solutions to the Knapsack Problem, with neural network models developed to improve constraint satisfaction \[[6' 2023-12-06](http://arxiv.org/abs/2312.03413v1)\]. This approach leverages the method of Lagrangian Relaxation to model the constraints explicitly, leading to better performance in terms of constraint satisfaction \[[6' 2023-12-06](http://arxiv.org/abs/2312.03413v1)\].

The concept of consistency in 0-1 programming has also been explored, with the introduction of LP-consistency as a form of consistency that can reduce backtracking and improve the efficiency of cutting plane methods \[[7' 2018-12-05](http://arxiv.org/abs/1812.02215v1)\]. This consistency is defined in terms of the linear programming relaxation and is shown to be related to Chvatal-Gomory cuts and the integer hull \[[7' 2018-12-05](http://arxiv.org/abs/1812.02215v1)\].

Finally, the use of random walks to bridge between 0-1 and linear programming has been proposed, offering a runtime improvement that smoothly transitions from exponential to polynomial time as the domain expands \[[5' 2019-04-09](http://arxiv.org/abs/1904.04860v1)\]. This approach has implications for solving CSPs like $k$-SAT and has been shown to yield fast exponential algorithms under certain conditions \[[5' 2019-04-09](http://arxiv.org/abs/1904.04860v1)\].

### References

1. Balas and Mazzola Linearization for Quadratic 0-1 Programs [http://arxiv.org/abs/1204.4829v1]  
2. Nonnegative partial s-goodness for the equivalence of a 0-1 linear program to weighted linear programming [http://arxiv.org/abs/2212.04268v1]  
3. Genetic Algorithm for a class of Knapsack Problems [http://arxiv.org/abs/1903.03494v1]  
4. 0-1 Integer Linear Programming with a Linear Number of Constraints [http://arxiv.org/abs/1401.5512v2]  
5. Bridging between 0/1 and Linear Programming via Random Walks [http://arxiv.org/abs/1904.04860v1]  
6. Approximating Solutions to the Knapsack Problem using the Lagrangian Dual Framework [http://arxiv.org/abs/2312.03413v1]  
7. Consistency for 0-1 Programming [http://arxiv.org/abs/1812.02215v1]  
8. Automatic Detection of Performance Anomalies in Task-Parallel Programs [http://arxiv.org/abs/1405.2916v1]
## Research papers
### Outline
- [Computational Efficiency in Optimization Algorithms [4 papers]](#category-computational-efficiency-in-optimization-algorithms)
- [Integer Linear Programming (ILP) for Resource Allocation [3 papers]](#category-integer-linear-programming-(ilp)-for-resource-allocation)
- [Knapsack Problem Variants and Solutions [4 papers]](#category-knapsack-problem-variants-and-solutions)
- [Heuristic Optimization Frameworks [3 papers]](#category-heuristic-optimization-frameworks)
- [Real-Time System Benchmarking and Evaluation [1 papers]](#category-real-time-system-benchmarking-and-evaluation)

### <a id='category-computational-efficiency-in-optimization-algorithms'></a>Computational Efficiency in Optimization Algorithms: 4 papers found.
Context: 
	Document 1: [Snippet]: «Balas and Mazzola linearization (BML) is widely used in devising cutting plane algorithms for quadratic 0-1 programs. In this article, we improve BML by first strengthening the primal formulation of BML and then considering the dual formulation. Additionally, a new cutting plane algorithm is proposed.»
[_citation_number]: «1»
[Category]: «Computational Efficiency in Optimization Algorithms»

	Document 2: [Snippet]: «Under the Strong Exponential Time Hypothesis, an integer linear program with $n$ Boolean-valued variables and $m$ equations cannot be solved in $c^n$ time for any constant $c < 2$. If the domain of the variables is relaxed to $[0,1]$, the associated linear program can of course be solved in polynomial time. In this work, we give a natural algorithmic bridging between these extremes of $0$-$1$ and linear programming. Specifically, for any subset (finite union of intervals) $E \subset [0,1]$ containing $\(0,1\)$, we give a random-walk based algorithm with runtime $O_E((2-\text(measure)(E))^n\text(poly)(n,m))$ that finds a solution in $E^n$ to any $n$-variable linear program with $m$ constraints that is feasible over $\(0,1\)^n$. Note that as $E$ expands from $\(0,1\)$ to $[0,1]$, the runtime improves smoothly from $2^n$ to polynomial.»
[_citation_number]: «5»
[Category]: «Computational Efficiency in Optimization Algorithms»

	Document 3: [Snippet]: «This note explains how to obtain, install, and use the ratpoints program. The program finds rational points up to a specified height on hyperelliptic curves using a highly optimized quadratic sieving algorithm.»
[_citation_number]: «9»
[Category]: «Computational Efficiency in Optimization Algorithms»

	Document 4: [Snippet]: «Let $\mathscr(A)$ be a unital $C^*$-algebra and let $Φ: \mathscr(A) \to (\mathbb B)((\mathscr H))$ be a unital $n$-positive linear map between $C^*$-algebras for some $n \geq 3$. We show that $$\|Φ(AB)-Φ(A)Φ(B)\| \leq Δ(A,||\cdot||)\,Δ(B,||\cdot||)$$ for all operators $A, B \in \mathscr(A)$, where $Δ(C,\|\cdot\|)$ denotes the operator norm distance of $C$ from the scalar operators.»
[_citation_number]: «15»
[Category]: «Computational Efficiency in Optimization Algorithms»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-15T16:40:14+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3' 2019-02-15](http://arxiv.org/abs/1903.03494v1)\]. Further details \[[6' 2023-12-06](http://arxiv.org/abs/2312.03413v1)\]\[[7' 2018-12-05](http://arxiv.org/abs/1812.02215v1)\]\[[8' 2021-10-23](http://arxiv.org/abs/2110.12115v2)\]\[[9' 2008-03-21](http://arxiv.org/abs/0803.3165v6)\]\[[10' 2017-04-01](http://arxiv.org/abs/1704.00145v1)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Memory bandwidth regulation and cache partitioning are widely used techniques
for achieving predictable timing in real-time computing systems. Combined with
partitioned scheduling, these methods require careful co-allocation of tasks
and resources to cores, as task execution times strongly depend on available
allocated resources. To address this challenge, this paper presents a 0-1
linear program for task-resource co-allocation, along with a multi-objective
heuristic designed to minimize resource usage while guaranteeing schedulability
under a preemptive EDF scheduling policy. Our heuristic employs a multi-layer
framework, where an outer layer explores resource allocations using
Pareto-pruned search, and an inner layer optimizes task allocation by solving a
knapsack problem using dynamic programming. To evaluate the performance of the
proposed optimization algorithm, we profile real-world benchmarks on an
embedded AMD UltraScale+ ZCU102 platform, with fine-grained resource
partitioning enabled by the Jailhouse hypervisor, leveraging cache set
partitioning and MemGuard for memory bandwidth regulation. Experiments based on
the benchmarking results show that the proposed 0-1 linear program outperforms
existing mixed-integer programs by finding more optimal solutions within the
same time limit. Moreover, the proposed multi-objective multi-layer heuristic
performs consistently better than the state-of-the-art multi-resource-task
co-allocation algorithm in terms of schedulability, resource usage, number of
non-dominated solutions, and computational efficiency.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3' 2019-02-15](http://arxiv.org/abs/1903.03494v1)\]. Further details discussed in contexts \[[2' 2022-12-08](http://arxiv.org/abs/2212.04268v1)\]\[[7' 2018-12-05](http://arxiv.org/abs/1812.02215v1)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Computational efficiency in optimization algorithms has been a focal point in recent research, particularly in the context of improving methods for solving complex optimization problems. The Balas and Mazzola linearization (BML) approach, which is widely used for quadratic 0-1 programs, has been further refined by strengthening its primal formulation and incorporating dual formulations, leading to improved cutting plane algorithms \[[1' 2012-04-21](http://arxiv.org/abs/1204.4829v1)\]. Additionally, there is ongoing work on bridging the gap between 0-1 integer programming and linear programming, with algorithms that leverage random walks and sophisticated potential functions to achieve faster runtime improvements as the domain expands from binary to continuous values \[[5' 2019-04-09](http://arxiv.org/abs/1904.04860v1)\]. These advancements are critical for applications requiring efficient resource allocation and scheduling, such as real-time computing systems, where task execution times are highly sensitive to resource availability. The use of optimized algorithms, such as quadratic sieving for finding rational points on hyperelliptic curves, also highlights the importance of computational efficiency in solving complex mathematical problems \[[9' 2008-03-21](http://arxiv.org/abs/0803.3165v6)\]. These studies collectively emphasize the need for innovative approaches to enhance the performance of optimization algorithms, particularly in scenarios where computational resources are constrained and real-time results are essential.
|    | reference                                                                                                                                                 | date     | key idea/summary                                                                                                                                                                                                                           |
|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Improved Balas and Mazzola Linearization for Quadratic 0-1 Programs with Application in a New Cutting Plane Algorithm](http://arxiv.org/abs/1204.4829v1) | 04/21/12 | The paper improves the Balas and Mazzola linearization by strengthening its primal formulation, considering the dual formulation, and proposing a new cutting plane algorithm for quadratic 0-1 programs.                                  |
|  1 | [Bridging between 0/1 and Linear Programming via Random Walks](http://arxiv.org/abs/1904.04860v1)                                                         | 04/09/19 | The paper presents a random-walk based algorithm that bridges the gap between 0-1 integer linear programming and linear programming over [0,1], achieving faster exponential time algorithms for certain constraint satisfaction problems. |
|  2 | [Documentation for the ratpoints program](http://arxiv.org/abs/0803.3165v6)                                                                               | 03/21/08 | The note explains how to obtain, install, and use the ratpoints program, which finds rational points on hyperelliptic curves using a quadratic sieving algorithm.                                                                          |
|  3 | [A Gruss inequality for n-positive linear maps](http://arxiv.org/abs/1006.1021v1)                                                                         | 06/05/10 | The paper establishes an inequality bounding the norm of the difference between the image of a product under a linear map and the product of the images, in terms of the operator norm distance from scalar operators.                     |
### <a id='category-integer-linear-programming-(ilp)-for-resource-allocation'></a>Integer Linear Programming (ILP) for Resource Allocation: 3 papers found.
The category "Integer Linear Programming (ILP) for Resource Allocation" encompasses several approaches to solving complex optimization problems, particularly in the context of real-time computing systems. Research in this area focuses on developing efficient algorithms for 0-1 integer linear programming, which is crucial for tasks such as memory bandwidth regulation and cache partitioning. One study introduces a 0-1 linear program for task-resource co-allocation, aiming to minimize resource usage while ensuring schedulability under a preemptive EDF scheduling policy \[[1' 2012-04-21](http://arxiv.org/abs/1204.4829v1)\]. Another work presents an exact algorithm for the 0-1 ILP problem with a linear number of constraints, significantly improving over exhaustive search by an exponential factor, achieving a time complexity of $2^((1-\text(poly))(1/c))n$ \[[2' 2022-12-08](http://arxiv.org/abs/2212.04268v1)\]. Additionally, there is a focus on consistency in integer programming, particularly in 0-1 programming, where LP-consistency is defined as a property that ensures any partial assignment consistent with the linear programming relaxation is also consistent with the original 0-1 constraint set \[[3' 2019-02-15](http://arxiv.org/abs/1903.03494v1)\]. This concept is further explored in relation to cutting planes and the integer hull, showing that a weak form of LP-consistency can reduce backtracking and improve the effectiveness of valid inequalities \[[4' 2014-01-21](http://arxiv.org/abs/1401.5512v2)\]. These studies collectively highlight the importance of theoretical advancements and practical algorithms in ILP for resource allocation, emphasizing both computational efficiency and solution quality.
|    | reference                                                                                                                                      | date     | key idea/summary                                                                                                                                                                                                                                    |
|----|------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Nonnegative partial s-goodness for the equivalence of a 0-1 linear program to weighted linear programming](http://arxiv.org/abs/2212.04268v1) | 12/08/22 | The paper addresses the 0-1 linear programming problem by transforming it into a sparse optimization problem and establishes conditions for the consistency of its optimal solution using nonnegative partial s-goodness.                           |
|  1 | [0-1 Integer Linear Programming with a Linear Number of Constraints](http://arxiv.org/abs/1401.5512v2)                                         | 01/21/14 | The paper presents an exact algorithm for the 0-1 Integer Linear Programming problem that runs in time $2^((1-	ext(poly))(1/c))n)$, improving over exhaustive search by an exponential factor through a reduction to the Vector Domination problem. |
|  2 | [Consistency for 0-1 Programming](http://arxiv.org/abs/1812.02215v1)                                                                           | 12/05/18 | The paper introduces a new concept of consistency, called LP-consistency, specifically for 0-1 integer programming, which can reduce backtracking and improve the effectiveness of valid inequalities over traditional cutting planes.              |
### <a id='category-knapsack-problem-variants-and-solutions'></a>Knapsack Problem Variants and Solutions: 4 papers found.
The category "Knapsack Problem Variants and Solutions" encompasses a range of approaches to solving and extending the classic knapsack problem, including traditional methods like dynamic programming and branch and bound, as well as more recent innovations such as genetic algorithms and deep learning techniques. The 0/1 knapsack problem is known to be weakly NP-hard, with pseudo-polynomial time algorithms available for exact solutions \[[3' 2019-02-15](http://arxiv.org/abs/1903.03494v1)\]. However, certain variants, such as spanner knapsack instances, pose greater challenges, even for dynamic programming-based approaches, due to their increased complexity and size \[[3' 2019-02-15](http://arxiv.org/abs/1903.03494v1)\]. In response, genetic algorithms have been proposed to deliver optimal solutions within reasonable computational durations \[[3' 2019-02-15](http://arxiv.org/abs/1903.03494v1)\]. Meanwhile, the use of deep learning methods, particularly within the Lagrangian Dual Framework, has gained traction for approximating solutions to constrained optimization problems, with experimental results showing strong constraint satisfaction at the cost of minor reductions in optimality \[[6' 2023-12-06](http://arxiv.org/abs/2312.03413v1)\]. Additionally, the inverse fractional knapsack problem has been explored, where the goal is to adjust parameters to make a given solution optimal under specific norms, with NP-hardness proven under the $l_1$-norm and quadratic-time algorithms developed for certain cases \[[10' 2017-04-01](http://arxiv.org/abs/1704.00145v1)\]. These developments highlight the ongoing evolution of knapsack problem solutions, addressing both theoretical challenges and practical applications in areas such as resource allocation and scheduling \[[3' 2019-02-15](http://arxiv.org/abs/1903.03494v1)\]\[[6' 2023-12-06](http://arxiv.org/abs/2312.03413v1)\]\[[10' 2017-04-01](http://arxiv.org/abs/1704.00145v1)\].
|    | reference                                                                                                                | date     | key idea/summary                                                                                                                                                                                                                                            |
|----|--------------------------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Genetic Algorithm for a class of Knapsack Problems](http://arxiv.org/abs/1903.03494v1)                                  | 02/15/19 | The paper introduces a genetic algorithm for solving spanner knapsack instances, which are difficult for traditional methods like dynamic programming and branch and bound, and demonstrates its effectiveness in delivering optimal solutions efficiently. |
|  1 | [Approximating Solutions to the Knapsack Problem using the Lagrangian Dual Framework](http://arxiv.org/abs/2312.03413v1) | 12/06/23 | This paper develops neural network models using the Lagrangian Dual Framework to approximate solutions to the Knapsack Problem, improving constraint satisfaction with a minor trade-off in optimality compared to unconstrained baseline models.           |
|  2 | [Inverse Fractional Knapsack Problem with Profits and Costs Modification](http://arxiv.org/abs/1704.00145v1)             | 04/01/17 | The paper addresses the inverse fractional knapsack problem, proving it is NP-hard under the $l_1$-norm but solvable in quadratic time under specific modifications and the $l_/infty$-norm.                                                                |
|  3 | [Knapsack problems in products of groups](http://arxiv.org/abs/1408.6509v2)                                              | 08/27/14 | The paper explores how free and direct products affect the time complexity of knapsack-type problems in groups, showing that free products preserve complexity while direct products may increase it.                                                       |
### <a id='category-heuristic-optimization-frameworks'></a>Heuristic Optimization Frameworks: 3 papers found.
Context: 
	Document 1: [Snippet]: «Incorporating mobile edge computing (MEC) in the Internet of Things (IoT) enables resource-limited IoT devices to offload their computation tasks to a nearby edge server. In this paper, we investigate an IoT system assisted by the MEC technique with its computation task subjected to sequential task dependency, which is critical for video stream processing and other intelligent applications. To minimize energy consumption per IoT device while limiting task processing delay, task offloading strategy, communication resource, and computation resource are optimized jointly under both slow and fast fading channels. In slow fading channels, an optimization problem is formulated, which is mixed-integer and non-convex. To solve this challenging problem, we decompose it as a one-dimensional search of task offloading decision problem and a non-convex optimization problem with task offloading decision given. Through mathematical manipulations, the non-convex problem is transformed to be a convex one, which is shown to be solvable only with the simple Golden search method. In fast fading channels, optimal online policy depending on instant channel state is derived. In addition, it is proved that the derived policy will converge to the offline policy when channel coherence time is low, which can help to save extra computation complexity. Numerical results verify the correctness of our analysis and the effectiveness of our proposed strategies over existing methods.»
[_citation_number]: «8»
[Category]: «Heuristic Optimization Frameworks»

	Document 2: [Snippet]: «People are remarkably capable of generating their own goals, beginning with child's play and continuing into adulthood. Despite considerable empirical and computational work on goals and goal-oriented behavior, models are still far from capturing the richness of everyday human goals. Here, we bridge this gap by collecting a dataset of human-generated playful goals (in the form of scorable, single-player games), modeling them as reward-producing programs, and generating novel human-like goals through program synthesis. Reward-producing programs capture the rich semantics of goals through symbolic operations that compose, add temporal constraints, and allow for program execution on behavioral traces to evaluate progress. To build a generative model of goals, we learn a fitness function over the infinite set of possible goal programs and sample novel goals with a quality-diversity algorithm. Human evaluators found that model-generated goals, when sampled from partitions of program space occupied by human examples, were indistinguishable from human-created games. We also discovered that our model's internal fitness scores predict games that are evaluated as more fun to play and more human-like.»
[_citation_number]: «11»
[Category]: «Heuristic Optimization Frameworks»

	Document 3: [Snippet]: «To efficiently exploit the resources of new many-core architectures, integrating dozens or even hundreds of cores per chip, parallel programming models have evolved to expose massive amounts of parallelism, often in the form of fine-grained tasks. Task-parallel languages, such as OpenStream, X10, Habanero Java and C or StarSs, simplify the development of applications for new architectures, but tuning task-parallel applications remains a major challenge. Performance bottlenecks can occur at any level of the implementation, from the algorithmic level (e.g., lack of parallelism or over-synchronization), to interactions with the operating and runtime systems (e.g., data placement on NUMA architectures), to inefficient use of the hardware (e.g., frequent cache misses or misaligned memory accesses); detecting such issues and determining the exact cause is a difficult task.
  In previous work, we developed Aftermath, an interactive tool for trace-based performance analysis and debugging of task-parallel programs and run-time systems. In contrast to other trace-based analysis tools, such as Paraver or Vampir, Aftermath offers native support for tasks, i.e., visualization, statistics and analysis tools adapted for performance debugging at task granularity. However, the tool currently does not provide support for the automatic detection of performance bottlenecks and it is up to the user to investigate the relevant aspects of program execution by focusing the inspection on specific slices of a trace file. In this paper, we present ongoing work on two extensions that guide the user through this process.»
[_citation_number]: «12»
[Category]: «Heuristic Optimization Frameworks»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-15T16:40:14+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3' 2019-02-15](http://arxiv.org/abs/1903.03494v1)\]. Further details \[[6' 2023-12-06](http://arxiv.org/abs/2312.03413v1)\]\[[7' 2018-12-05](http://arxiv.org/abs/1812.02215v1)\]\[[8' 2021-10-23](http://arxiv.org/abs/2110.12115v2)\]\[[9' 2008-03-21](http://arxiv.org/abs/0803.3165v6)\]\[[10' 2017-04-01](http://arxiv.org/abs/1704.00145v1)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Memory bandwidth regulation and cache partitioning are widely used techniques
for achieving predictable timing in real-time computing systems. Combined with
partitioned scheduling, these methods require careful co-allocation of tasks
and resources to cores, as task execution times strongly depend on available
allocated resources. To address this challenge, this paper presents a 0-1
linear program for task-resource co-allocation, along with a multi-objective
heuristic designed to minimize resource usage while guaranteeing schedulability
under a preemptive EDF scheduling policy. Our heuristic employs a multi-layer
framework, where an outer layer explores resource allocations using
Pareto-pruned search, and an inner layer optimizes task allocation by solving a
knapsack problem using dynamic programming. To evaluate the performance of the
proposed optimization algorithm, we profile real-world benchmarks on an
embedded AMD UltraScale+ ZCU102 platform, with fine-grained resource
partitioning enabled by the Jailhouse hypervisor, leveraging cache set
partitioning and MemGuard for memory bandwidth regulation. Experiments based on
the benchmarking results show that the proposed 0-1 linear program outperforms
existing mixed-integer programs by finding more optimal solutions within the
same time limit. Moreover, the proposed multi-objective multi-layer heuristic
performs consistently better than the state-of-the-art multi-resource-task
co-allocation algorithm in terms of schedulability, resource usage, number of
non-dominated solutions, and computational efficiency.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3' 2019-02-15](http://arxiv.org/abs/1903.03494v1)\]. Further details discussed in contexts \[[2' 2022-12-08](http://arxiv.org/abs/2212.04268v1)\]\[[7' 2018-12-05](http://arxiv.org/abs/1812.02215v1)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer: 
Heuristic optimization frameworks have been extensively explored to address complex resource allocation and scheduling challenges in modern computing systems \[[11' 2024-05-21](http://arxiv.org/abs/2405.13242v3)\]. These frameworks often involve multi-objective approaches that balance multiple conflicting goals, such as minimizing resource usage while ensuring system schedulability \[[8' 2021-10-23](http://arxiv.org/abs/2110.12115v2)\]. For instance, in the context of real-time computing, techniques like memory bandwidth regulation and cache partitioning are commonly used to achieve predictable timing, and heuristic methods are employed to co-allocate tasks and resources efficiently \[[12' 2014-05-12](http://arxiv.org/abs/1405.2916v1)\]. The proposed multi-layer framework, which combines Pareto-pruned search with dynamic programming-based knapsack optimization, aligns with these heuristic strategies by enabling efficient exploration of resource allocations while optimizing task execution \[[8' 2021-10-23](http://arxiv.org/abs/2110.12115v2)\]. Additionally, similar to the use of program synthesis to generate human-like goals \[[11' 2024-05-21](http://arxiv.org/abs/2405.13242v3)\], heuristic optimization methods often rely on adaptive strategies that evolve through iterative refinement, such as the Golden search method used in mobile edge computing for task offloading \[[8' 2021-10-23](http://arxiv.org/abs/2110.12115v2)\]. These approaches highlight the importance of integrating both analytical and heuristic techniques to solve complex optimization problems in resource-constrained environments.
|    | reference                                                                                                                                 | date     | key idea/summary                                                                                                                                                                                                                  |
|----|-------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [Joint Task Offloading and Resource Allocation for IoT Edge Computing with Sequential Task Dependency](http://arxiv.org/abs/2110.12115v2) | 10/23/21 | This paper proposes an optimized task offloading strategy for IoT systems assisted by mobile edge computing, focusing on minimizing energy consumption and task processing delay under both slow and fast fading channels.        |
|  1 | [Goals as Reward-Producing Programs](http://arxiv.org/abs/2405.13242v3)                                                                   | 05/21/24 | The paper introduces a method to generate human-like goals by modeling them as reward-producing programs and using a generative model to create novel, fun, and diverse goals that are indistinguishable from human-created ones. |
|  2 | [Automatic Detection of Performance Anomalies in Task-Parallel Programs](http://arxiv.org/abs/1405.2916v1)                                | 05/12/14 | The paper introduces two extensions to the Aftermath tool to guide users in automatically detecting performance bottlenecks in task-parallel programs by analyzing trace data.                                                    |
### <a id='category-real-time-system-benchmarking-and-evaluation'></a>Real-Time System Benchmarking and Evaluation: 1 papers found.
Context: 
	Document 1: [Snippet]: «We develop a robust translation model for four low-resource Indic languages: Khasi, Mizo, Manipuri, and Assamese. Our approach includes a comprehensive pipeline from data collection and preprocessing to training and evaluation, leveraging data from WMT task datasets, BPCC, PMIndia, and OpenLanguageData. To address the scarcity of bilingual data, we use back-translation techniques on monolingual datasets for Mizo and Khasi, significantly expanding our training corpus. We fine-tune the pre-trained NLLB 3.3B model for Assamese, Mizo, and Manipuri, achieving improved performance over the baseline. For Khasi, which is not supported by the NLLB model, we introduce special tokens and train the model on our Khasi corpus. Our training involves masked language modelling, followed by fine-tuning for English-to-Indic and Indic-to-English translations.»
[_citation_number]: «13»
[Category]: «Real-Time System Benchmarking and Evaluation»


Instruction:  You are writing a single subsection of a larger report answering the user's query: Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before 2025-05-15T16:40:14+00:00. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source \[[3' 2019-02-15](http://arxiv.org/abs/1903.03494v1)\]. Further details \[[6' 2023-12-06](http://arxiv.org/abs/2312.03413v1)\]\[[7' 2018-12-05](http://arxiv.org/abs/1812.02215v1)\]\[[8' 2021-10-23](http://arxiv.org/abs/2110.12115v2)\]\[[9' 2008-03-21](http://arxiv.org/abs/0803.3165v6)\]\[[10' 2017-04-01](http://arxiv.org/abs/1704.00145v1)\].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: Memory bandwidth regulation and cache partitioning are widely used techniques
for achieving predictable timing in real-time computing systems. Combined with
partitioned scheduling, these methods require careful co-allocation of tasks
and resources to cores, as task execution times strongly depend on available
allocated resources. To address this challenge, this paper presents a 0-1
linear program for task-resource co-allocation, along with a multi-objective
heuristic designed to minimize resource usage while guaranteeing schedulability
under a preemptive EDF scheduling policy. Our heuristic employs a multi-layer
framework, where an outer layer explores resource allocations using
Pareto-pruned search, and an inner layer optimizes task allocation by solving a
knapsack problem using dynamic programming. To evaluate the performance of the
proposed optimization algorithm, we profile real-world benchmarks on an
embedded AMD UltraScale+ ZCU102 platform, with fine-grained resource
partitioning enabled by the Jailhouse hypervisor, leveraging cache set
partitioning and MemGuard for memory bandwidth regulation. Experiments based on
the benchmarking results show that the proposed 0-1 linear program outperforms
existing mixed-integer programs by finding more optimal solutions within the
same time limit. Moreover, the proposed multi-objective multi-layer heuristic
performs consistently better than the state-of-the-art multi-resource-task
co-allocation algorithm in terms of schedulability, resource usage, number of
non-dominated solutions, and computational efficiency.
Your job is to write a single body paragraph of the full report, focused on introducing the specific Category.
The paragraph should summarize the key themes that relate to the category, based on relevant sources, given their Snippet. Make sure to cite the sources.
You should write a short paragraph, specifically focusing on the given category.
Write your answer as a single body paragraph focused on the category, with nothing else.
<Citation Guidelines>
- Use [X] format where X is the _citation_number
- Place citations immediately after the sentence or paragraph they are referencing (e.g., information from context \[[3' 2019-02-15](http://arxiv.org/abs/1903.03494v1)\]. Further details discussed in contexts \[[2' 2022-12-08](http://arxiv.org/abs/2212.04268v1)\]\[[7' 2018-12-05](http://arxiv.org/abs/1812.02215v1)\].).
- If urls are given in existing section content, rewrite them exactly if using information related to the url.
- Make sure to provide citations whenever you are using information from the source material. This is a MUST.
- Cite as many sources as possible.
- Make sure to retain the citation numbers from the input context.
- Provide in-line citations only. You do not need a reference section at the end.
<Citation Guidelines>



Answer:
The category "Real-Time System Benchmarking and Evaluation" focuses on techniques for achieving predictable timing in real-time computing systems, particularly through memory bandwidth regulation and cache partitioning \[[13' 2024-11-01](http://arxiv.org/abs/2411.00727v2)\]. These methods are often combined with partitioned scheduling to ensure that task execution times remain consistent, as they are heavily influenced by the allocated resources \[[13' 2024-11-01](http://arxiv.org/abs/2411.00727v2)\]. Existing research has explored various approaches to optimize resource allocation, including the use of 0-1 linear programs and multi-objective heuristics that aim to minimize resource usage while maintaining schedulability under preemptive EDF policies \[[13' 2024-11-01](http://arxiv.org/abs/2411.00727v2)\]. The effectiveness of these techniques is often evaluated using real-world benchmarks on embedded platforms, such as the AMD UltraScale+ ZCU102, where fine-grained resource partitioning is enabled through hypervisors like Jailhouse, along with tools like MemGuard for memory bandwidth control \[[13' 2024-11-01](http://arxiv.org/abs/2411.00727v2)\]. These evaluations highlight the importance of both algorithmic innovation and hardware-software co-design in achieving reliable performance in real-time systems.
|    | reference                                                                                                                | date     | key idea/summary                                                                                                                                                                                                                 |
|----|--------------------------------------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | [SPRING Lab IITM's submission to Low Resource Indic Language Translation Shared Task](http://arxiv.org/abs/2411.00727v2) | 11/01/24 | The paper presents a robust translation model for four low-resource Indic languages, utilizing data from various sources, back-translation techniques, and fine-tuning of pre-trained models to improve translation performance. |
