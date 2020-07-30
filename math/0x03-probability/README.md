<h1 class="gap">0x03. Probability</h1>

<article id="description" class="gap formatted-content">
    <p><a href="https://imgbb.com/"><img src="https://i.ibb.co/4Z052zp/f7d69a8ae2b2f71d007b.jpg" alt="f7d69a8ae2b2f71d007b" border="0"></a></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/ZggoiEvv6Yi28ddpDdRf5A" title="Probability" target="_blank">Probability</a></li>
<li><a href="/rltoken/rP2DkSL-d-ug2B6VDXyBFA" title="Basic Concepts" target="_blank">Basic Concepts</a></li>
<li><a href="/rltoken/d3V6VMIBciqUciimA0uG7g" title="Intro to probability 1: Basic notation" target="_blank">Intro to probability 1: Basic notation</a></li>
<li><a href="/rltoken/q-lZzr4Y2ACNzE-P4W0v1Q" title="Intro to probability 2: Independent and disjoint" target="_blank">Intro to probability 2: Independent and disjoint</a></li>
<li><a href="/rltoken/_AYQ5zzBgJ8AaZRHUIj4sw" title="Intro to Probability 3: General Addition Rule; Union; OR" target="_blank">Intro to Probability 3: General Addition Rule; Union; OR</a></li>
<li><a href="/rltoken/v5eLcUN_15IraTYt_LmHIA" title="Intro to Probability 4: General multiplication rule; Intersection; AND" target="_blank">Intro to Probability 4: General multiplication rule; Intersection; AND</a></li>
<li><a href="/rltoken/XA_WRfsUAeIql7JLxe8J2w" title="Permutations and Combinations" target="_blank">Permutations and Combinations</a></li>
<li><a href="/rltoken/42CEUdBffkNdfw0_xtidWw" title="Probability distribution" target="_blank">Probability distribution</a></li>
<li><a href="/rltoken/wwSIDquJxD3IRhPqfFGibg" title="Probability Theory" target="_blank">Probability Theory</a></li>
<li><a href="/rltoken/1rQ3Is5znPPsP__vso935w" title="Cumulative Distribution Functions" target="_blank">Cumulative Distribution Functions</a></li>
<li><a href="/rltoken/Igose8HXOpWt_J2bRN7Ipg" title="Common Probability Distributions: The Data Scientist’s Crib Sheet" target="_blank">Common Probability Distributions: The Data Scientist’s Crib Sheet</a></li>
<li><a href="/rltoken/B1qQQHvRWmWFRYMPEdXmUg" title="NORMAL MODEL PART 1 --- EMPIRICAL RULE" target="_blank">NORMAL MODEL PART 1 — EMPIRICAL RULE</a></li>
<li><a href="/rltoken/COhfVdgzwr78gFqWPoj9fQ" title="Normal Distribution" target="_blank">Normal Distribution</a></li>
<li><a href="/rltoken/dsXzwQ3vLRrmZhy60Ciqyw" title="Variance" target="_blank">Variance</a></li>
<li><a href="/rltoken/tvnDhgxyEVovjx68hWTGWA" title="Variance (Concept)" target="_blank">Variance (Concept)</a></li>
<li><a href="/rltoken/xNgZVUblDZ-r1zKScLpHaA" title="Binomial Distribution" target="_blank">Binomial Distribution</a></li>
<li><a href="/rltoken/7l0nmdir-iJVeOmj6vp0ZA" title="Poisson Distribution" target="_blank">Poisson Distribution</a></li>
<li><a href="/rltoken/qQwH7bS7Q8g1N1Cd_uudnA" title="Hypergeometric Distribution" target="_blank">Hypergeometric Distribution</a></li>
</ul>

<p><strong>As references</strong>:</p>

<ul>
<li><a href="/rltoken/5WwREyqDXOrhPGaLX7gc8g" title="numpy.random.poisson" target="_blank">numpy.random.poisson</a></li>
<li><a href="/rltoken/_7-nlxL_33YHvsUnRLKTFg" title="numpy.random.exponential" target="_blank">numpy.random.exponential</a></li>
<li><a href="/rltoken/uX5Oa-kr8rf4mP-NwX5bLA" title="numpy.random.normal" target="_blank">numpy.random.normal</a></li>
<li><a href="/rltoken/rxyVIsnHhnWD4ZFYPbA3jQ" title="numpy.random.binomial" target="_blank">numpy.random.binomial</a></li>
<li><a href="/rltoken/solZkrICzuv3a6Bbxgpqdg" title="erf" target="_blank">erf</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/eh9zZy41B9jxrUWVGpJlRw" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is probability?</li>
<li>Basic probability notation</li>
<li>What is independence? What is disjoint?</li>
<li>What is a union? intersection?</li>
<li>What are the general addition and multiplication rules?</li>
<li>What is a probability distribution?</li>
<li>What is a probability distribution function? probability mass function?</li>
<li>What is a cumulative distribution function?</li>
<li>What is a percentile?</li>
<li>What is mean, standard deviation, and variance?</li>
<li>Common probability distributions</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 16.04 LTS using <code>python3</code> (version 3.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.5)</li>
<li>All your modules should have documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>Unless otherwise noted, you are not allowed to import any module</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h2>Mathematical Approximations</h2>

<p>For the following tasks, you will have to use various irrational numbers and functions. Since you are not able to import any libraries, please use the following approximations:</p>

<ul>
<li><em>π</em> = 3.1415926536</li>
<li><em>e</em> = 2.7182818285</li>
<li><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/4/5e71204ca545072e8766.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20200730%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20200730T171627Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=597d2613966f3fdbaada2cb8dedab4ce7db232ee40447de1e5afe37408f66f19" alt="" style=""></li>
</ul>

  </article>

## Author
* **Samir millan** - [Gaspela04](https://github.com/Gaspela04)
