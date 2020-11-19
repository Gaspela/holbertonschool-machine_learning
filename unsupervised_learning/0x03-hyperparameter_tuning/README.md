<h1 class="gap">0x03. Hyperparameter Tuning</h1>

<article id="description" class="gap formatted-content">
    <p><a href="https://imgbb.com/"><img src="https://i.ibb.co/3TK6c78/ff91ee0b5a39abcf086a.jpg" alt="ff91ee0b5a39abcf086a" border="0"></a></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/LVmEm_zt83iEKEQ8D2_oaw" title="Hyperparameter Tuning in Practice" target="_blank">Hyperparameter Tuning in Practice</a></li>
<li><a href="/rltoken/1suHjfI2RmB7HGUkPe0qSA" title="Orthogonalization" target="_blank">Orthogonalization</a> </li>
<li><a href="/rltoken/mHDoDo0R2RgDsns-ho_B-Q" title="Single Number Evaluation Metric" target="_blank">Single Number Evaluation Metric</a> </li>
<li><a href="/rltoken/S-CqOTV5KvSz-6zgqVYSGQ" title="Satisficing and Optimizing Metrics" target="_blank">Satisficing and Optimizing Metrics</a> </li>
<li><a href="/rltoken/qJMsx3m-MecQGuHIiWmPVg" title="Gaussian process" target="_blank">Gaussian process</a></li>
<li><a href="/rltoken/jGdxmGdHXEATzO1ie3M2Zg" title="Kriging" target="_blank">Kriging</a></li>
<li><a href="/rltoken/k6HZ2Sg5pRuXPE05wmarfA" title="Machine learning - Introduction to Gaussian processes" target="_blank">Machine learning - Introduction to Gaussian processes</a> </li>
<li><a href="/rltoken/t3m8B0_XJTUYblxKW2qY-Q" title="Machine learning - Gaussian processes" target="_blank">Machine learning - Gaussian processes</a> </li>
<li><a href="/rltoken/4yLuCWiPvAUAmFUwNUi-lg" title="Quick Start to Gaussian Process Regression" target="_blank">Quick Start to Gaussian Process Regression</a></li>
<li><a href="/rltoken/3Xgwc7ddcXcBoRaurvfKXA" title="Gaussian processes" target="_blank">Gaussian processes</a></li>
<li><a href="/rltoken/r_AicUZLRVINuXAEiR0ugA" title="Machine learning - Bayesian optimization and multi-armed bandits" target="_blank">Machine learning - Bayesian optimization and multi-armed bandits</a> </li>
<li><a href="/rltoken/3nJ8PFZXkdbX33nMrDuuTA" title="Bayesian Optimization" target="_blank">Bayesian Optimization</a></li>
<li><a href="/rltoken/ICAbvZAnezCius35JPtixg" title="Bayesian Optimization" target="_blank">Bayesian Optimization</a></li>
<li><a href="/rltoken/Zg6LyIfrtOr-RWTMrGXhXw" title="A Tutorial on Bayesian Optimization" target="_blank">A Tutorial on Bayesian Optimization</a></li>
<li><a href="/rltoken/dArkynGcqzwjsxahKI4arg" title="GPy documentation" target="_blank">GPy documentation</a>

<ul>
<li><a href="/rltoken/CVHw9tEMXCKL_GQx7YcpcA" title="GPy.kern.src" target="_blank">GPy.kern.src</a></li>
<li><a href="/rltoken/a4u5-JZkKxHIIlbMafkixw" title="GPy.plotting.gpy_plot" target="_blank">GPy.plotting.gpy_plot</a></li>
</ul></li>
<li><a href="/rltoken/MxJBvbwWsx4Mo833htW5DQ" title="GPyOpt documentation" target="_blank">GPyOpt documentation</a>

<ul>
<li><a href="/rltoken/Dw6-zZ3eol5cHYh4kxHWgA" title="GPyOpt.methods.bayesian_optimization" target="_blank">GPyOpt.methods.bayesian_optimization</a></li>
<li><a href="/rltoken/v-zTr1M0n1ZI5jG4to2uPg" title="GPyOpt.core.task.space" target="_blank">GPyOpt.core.task.space</a></li>
</ul></li>
</ul>

<h2>Learning Objectives</h2>

<ul>
<li>What is Hyperparameter Tuning?</li>
<li>What is random search? grid search?</li>
<li>What is a Gaussian Process?</li>
<li>What is a mean function?</li>
<li>What is a Kernel function?</li>
<li>What is Gaussian Process Regression/Kriging?</li>
<li>What is Bayesian Optimization?</li>
<li>What is an Acquisition function?</li>
<li>What is Expected Improvement?</li>
<li>What is Knowledge Gradient?</li>
<li>What is Entropy Search/Predictive Entropy Search?</li>
<li>What is GPy?</li>
<li>What is GPyOpt?</li>
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
<li>Your code should use the <code>pycodestyle</code> style (version 2.4), but can ignore error <code>E741</code></li>
<li>All your modules should have documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>Unless otherwise noted, you are not allowed to import any module except <code>import numpy as np</code></li>
<li>All your files must be executable</li>
</ul>

<h2>Install GPy and GPyOpt</h2>

<pre><code>pip install --user GPy
pip install --user gpyopt
</code></pre>

  </article>

## Author
* **Samir millan** - [Gaspela04](https://github.com/Gaspela04)
