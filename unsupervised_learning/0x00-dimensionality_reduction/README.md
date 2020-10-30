<h1 class="gap">0x00. Dimensionality Reduction</h1>

<article id="description" class="gap formatted-content">
    <p><a href="https://imgbb.com/"><img src="https://i.ibb.co/WGX298k/77f77fafb61bd7249233.jpg" alt="77f77fafb61bd7249233" border="0"></a></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/EWTgkISa0fbESVFhto2tLA" title="Dimensionality Reduction For Dummies — Part 1: Intuition" target="_blank">Dimensionality Reduction For Dummies — Part 1: Intuition</a></li>
<li><a href="/rltoken/Qg_s08ni0zOWkqvvRM8ZwQ" title="Singular Value Decomposition" target="_blank">Singular Value Decomposition</a></li>
<li><a href="/rltoken/sJH8jspuR61IdC2H1a_jDQ" title="Understanding SVD (Singular Value Decomposition)" target="_blank">Understanding SVD (Singular Value Decomposition)</a></li>
<li><a href="/rltoken/WyHO8ZBDqbKmzUoD0Ukf7Q" title="Intuitively, what is the difference between Eigendecomposition and Singular Value Decomposition?" target="_blank">Intuitively, what is the difference between Eigendecomposition and Singular Value Decomposition?</a></li>
<li><a href="/rltoken/euVIN9M2jJ-PHyOEBnI1lA" title="Dimensionality Reduction: Principal Components Analysis, Part 1" target="_blank">Dimensionality Reduction: Principal Components Analysis, Part 1</a></li>
<li><a href="/rltoken/co3YVWGBIdcto2q3HPu51A" title="Dimensionality Reduction: Principal Components Analysis, Part 2" target="_blank">Dimensionality Reduction: Principal Components Analysis, Part 2</a></li>
<li><a href="/rltoken/XGKIL0TBES-GY6gO6VoSmg" title="StatQuest: t-SNE, Clearly Explained" target="_blank">StatQuest: t-SNE, Clearly Explained</a></li>
<li><a href="/rltoken/IaO5r9ba0T_flqHcQv83fA" title="t-SNE tutorial Part1" target="_blank">t-SNE tutorial Part1</a></li>
<li><a href="/rltoken/hariVnyW46RIjyXj6DefGA" title="t-SNE tutorial Part2" target="_blank">t-SNE tutorial Part2</a></li>
<li><a href="/rltoken/ZGyuMFuDwY6SzE-pM3ZrTw" title="How to Use t-SNE Effectively" target="_blank">How to Use t-SNE Effectively</a></li>
</ul>

<p><strong>Definitions to skim:</strong></p>

<ul>
<li><a href="/rltoken/3__-0sq0ymVc6rUhSUF46Q" title="Dimensionality Reduction" target="_blank">Dimensionality Reduction</a></li>
<li><a href="/rltoken/-Q1NQBRaQiPLZAlpnXDQoQ" title="Principal component analysis" target="_blank">Principal component analysis</a></li>
<li><a href="/rltoken/ZicQZ9TndU2Khb4QLnU9Rg" title="Eigendecomposition of a matrix" target="_blank">Eigendecomposition of a matrix</a></li>
<li><a href="/rltoken/pW3EQwurOaQp4f9SIFXs0w" title="Singular value decomposition" target="_blank">Singular value decomposition</a></li>
<li><a href="/rltoken/W_DWK5vN6rSRqN6jaVe7Ag" title="Manifold" target="_blank">Manifold</a> <em>check this out if you have never heard this term before</em></li>
<li><a href="/rltoken/EAzyLBFVORoaaWgWc8K9yQ" title="Kullback–Leibler divergence" target="_blank">Kullback–Leibler divergence</a></li>
<li><a href="/rltoken/EnCpSMJZOJ2E7IMdOof0Jg" title="T-distributed stochastic neighbor embedding" target="_blank">T-distributed stochastic neighbor embedding</a> </li>
</ul>

<p><strong>As references</strong>:</p>

<ul>
<li><a href="/rltoken/TUz_LerlFe9fPhMuHxJXLg" title="numpy.cumsum" target="_blank">numpy.cumsum</a></li>
<li><a href="/rltoken/2l3jXLWneQVGdNfoXsWMQQ" title="Visualizing Data using t-SNE" target="_blank">Visualizing Data using t-SNE</a> (paper)</li>
<li><a href="/rltoken/mgNNPvYr_iahfCU8hEZsHQ" title="Visualizing Data Using t-SNE" target="_blank">Visualizing Data Using t-SNE</a> (video)</li>
</ul>

<p><strong>Advanced</strong>:</p>

<ul>
<li><a href="/rltoken/61bPYClgo7vCg7FHEzSVdQ" title="Kernel principal component analysis" target="_blank">Kernel principal component analysis</a></li>
<li><a href="/rltoken/34dL3ML5vCExK-iUR9_0Rg" title="Nonlinear Dimensionality Reduction: KPCA" target="_blank">Nonlinear Dimensionality Reduction: KPCA</a></li>
</ul>

<h2>Learning Objectives</h2>

<ul>
<li>What is eigendecomposition?</li>
<li>What is singular value decomposition?</li>
<li>What is the difference between eig and svd?</li>
<li>What is dimensionality reduction and what are its purposes?</li>
<li>What is principal components analysis (PCA)?</li>
<li>What is t-distributed stochastic neighbor embedding (t-SNE)?</li>
<li>What is a manifold?</li>
<li>What is the difference between linear and non-linear dimensionality reduction?</li>
<li>Which techniques are linear/non-linear?</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 16.04 LTS using <code>python3</code> (version 3.5)</li>
<li>Your files will be executed with <code>numpy</code> (version 1.15)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.4)</li>
<li>All your modules should have documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>Unless otherwise noted, you are not allowed to import any module except <code>import numpy as np</code></li>
<li>All your files must be executable</li>
<li><strong>Your code should use the minimum number of operations to avoid floating point errors</strong></li>
</ul>

<h2>Data</h2>

<p>Please test your main files with the following data:</p>

<ul>
<li><a href="/rltoken/XXWPBYuEFBplwpcJRJ2LaQ" title="mnist2500_X.txt" target="_blank">mnist2500_X.txt</a></li>
<li><a href="/rltoken/Xp4jTT6YjHKXbmMw5NkBOA" title="mnist2500_labels.txt" target="_blank">mnist2500_labels.txt</a></li>
</ul>

<h2>Watch Out!</h2>

<p>Just like lists, <code>np.ndarray</code>s are mutable objects:</p>

<pre><code>&gt;&gt;&gt; vector = np.ones((100, 1))
&gt;&gt;&gt; m1 = vector[55]
&gt;&gt;&gt; m2 = vector[55, 0]
&gt;&gt;&gt; vector[55] = 2
&gt;&gt;&gt; m1
array([2.])
&gt;&gt;&gt; m2
1.0
</code></pre>

<h2>Performance between SVD and EIG</h2>

<p>Here a graph of execution time (Y-axis) for the number of iteration (X-axis) - red line is EIG and blue line is SVG</p>

<p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/10/df2eac7a51b56139b4a179a83398b18fbda8868c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201029%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20201029T152529Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=2eee76a3f4bbe3ce387fc75ddb305e6a525a40639bce944fa80f032ec92e2faa" alt="" style=""></p>

  </article>

## Author
* **Samir millan** - [Gaspela04](https://github.com/Gaspela04)