## Related Works

The problem of learning from noisy labels has been extensively studied in recent years, with a growing body of research focused on developing robust training strategies for deep neural networks. Early approaches primarily relied on modifying the loss function to mitigate the impact of label noise, such as using the mean absolute error (MAE) as a noise-robust alternative to the standard cross entropy (CE) loss \[[12](http://arxiv.org/abs/1805.07836)\]. However, MAE has been shown to perform poorly with deep neural networks on challenging datasets \[[12](http://arxiv.org/abs/1805.07836)\]. To address this, researchers have proposed generalized loss functions that extend the principles of MAE and CE, offering improved robustness to label noise \[[12](http://arxiv.org/abs/1805.07836)\]. These loss functions are theoretically grounded and can be applied to a wide range of neural network architectures \[[12](http://arxiv.org/abs/1805.07836)\].

Another line of research focuses on the memorization effects of deep neural networks, where models tend to memorize noisy labels before clean ones \[[2](http://arxiv.org/abs/1804.06872)\]. This observation has led to the development of Co-teaching, a paradigm where two neural networks are trained simultaneously, and they teach each other by selecting data with potentially clean labels \[[2](http://arxiv.org/abs/1804.06872)\]. This approach has been shown to significantly improve robustness against noisy labels \[[2](http://arxiv.org/abs/1804.06872)\]. However, Co-teaching can suffer from convergence issues as the two networks gradually reach a consensus \[[7](http://arxiv.org/abs/1901.04215)\]. To address this, Co-teaching+ was introduced, which combines the "update by disagreement" strategy with the original Co-teaching approach, leading to better performance \[[7](http://arxiv.org/abs/1901.04215)\].

In addition to loss function modifications and co-training strategies, researchers have also explored semi-supervised learning techniques to handle noisy labels. For instance, DivideMix leverages semi-supervised learning by dynamically dividing training data into clean and noisy subsets and training the model on both \[[5](http://arxiv.org/abs/2002.07394)\]. This approach avoids confirmation bias by using two diverged networks that learn from each other's data divisions \[[5](http://arxiv.org/abs/2002.07394)\]. Similarly, the use of graphical models to represent the relationship between noisy and clean labels has been proposed, allowing for semi-supervised training with auxiliary information \[[4](http://arxiv.org/abs/1706.00038)\].

Recent work has also focused on understanding the generalization behavior of deep neural networks under label noise. For example, the dimensionality-driven learning strategy monitors the dimensionality of the deep representation subspace during training and adapts the loss function accordingly, leading to improved tolerance against noisy labels \[[11](http://arxiv.org/abs/1806.02612)\]. Furthermore, the concept of information-theoretic loss functions, such as the Determinant-based Mutual Information (DMI) loss, has been introduced to provide a theoretically justified approach for robust learning under label noise \[[13](http://arxiv.org/abs/1909.03388)\]. These loss functions are designed to be invariant to noise patterns and can be applied to any classification neural network without requiring additional information \[[13](http://arxiv.org/abs/1909.03388)\].

In summary, the field has seen a variety of approaches to address label noise, ranging from loss function modifications to co-training and semi-supervised learning strategies. These methods have been evaluated on a range of benchmark and real-world datasets, demonstrating their effectiveness in improving robustness against noisy labels.

References:  
\[[1](http://arxiv.org/abs/1908.06112)\] http://arxiv.org/abs/1908.06112  
\[[2](http://arxiv.org/abs/1804.06872)\] http://arxiv.org/abs/1804.06872  
\[[3](http://arxiv.org/abs/1609.03683)\] http://arxiv.org/abs/1609.03683  
\[[4](http://arxiv.org/abs/1706.00038)\] http://arxiv.org/abs/1706.00038  
\[[5](http://arxiv.org/abs/2002.07394)\] http://arxiv.org/abs/2002.07394  
\[[6](http://arxiv.org/abs/1711.07131)\] http://arxiv.org/abs/1711.07131  
\[[7](http://arxiv.org/abs/1901.04215)\] http://arxiv.org/abs/1901.04215  
\[[8](http://arxiv.org/abs/1703.02391)\] http://arxiv.org/abs/1703.02391  
\[[9](http://arxiv.org/abs/1712.09482)\] http://arxiv.org/abs/1712.09482  
\[[10](https://www.semanticscholar.org/paper/5d6ae67e569f974360b107060c23cbb8a13b0687)\] https://www.semanticscholar.org/paper/5d6ae67e569f974360b107060c23cbb8a13b0687  
\[[11](http://arxiv.org/abs/1806.02612)\] http://arxiv.org/abs/1806.02612  
\[[12](http://arxiv.org/abs/1805.07836)\] http://arxiv.org/abs/1805.07836  
\[[13](http://arxiv.org/abs/1909.03388)\] http://arxiv.org/abs/1909.03388
