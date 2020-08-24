<h1 class="gap">0x04. Error Analysis</h1>

<article id="description" class="gap formatted-content">
    <p><a href="https://imgbb.com/"><img src="https://i.ibb.co/nfRF8Vt/e3786a3d84e36ff800d8.jpg" alt="e3786a3d84e36ff800d8" border="0"></a></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/Bn9M-MGfoJrw0-TpHTa9Uw" title="Confusion matrix" target="_blank">Confusion matrix</a> </li>
<li><a href="/rltoken/fxhGH4L-87fD_e11L-T0IA" title="Type I and type II errors" target="_blank">Type I and type II errors</a> </li>
<li><a href="/rltoken/jn65gXxuPRCOX3zo7ZMAVg" title="Sensitivity and specificity" target="_blank">Sensitivity and specificity</a> </li>
<li><a href="/rltoken/a2j2_WIV27HgPCm2rXYW0A" title="Precision and recall" target="_blank">Precision and recall</a> </li>
<li><a href="/rltoken/n0icgR0KqaHEdpn3FAbJoQ" title="F1 score" target="_blank">F1 score</a> </li>
<li><a href="/rltoken/qocVwJJrC7gC9cOUc2Wn7A" title="What is a Confusion Matrix in Machine Learning?" target="_blank">What is a Confusion Matrix in Machine Learning?</a> </li>
<li><a href="/rltoken/YSLbZZN4UAp33VXvfhFWyA" title="Simple guide to confusion matrix terminology" target="_blank">Simple guide to confusion matrix terminology</a> </li>
<li><a href="/rltoken/eWYy4ivH1yTEU0SYElZNxA" title="Bias-variance tradeoff" target="_blank">Bias-variance tradeoff</a> </li>
<li><a href="/rltoken/aPtj03_mws2J_d50hWU8TA" title="What is bias and variance" target="_blank">What is bias and variance</a> </li>
<li><a href="/rltoken/VC4wmuWuQH7Du-uLOZ2AZg" title="Bayes error rate" target="_blank">Bayes error rate</a> </li>
<li><a href="/rltoken/x6wgEm5-QbyIehgFZCb2rQ" title="What is Bayes Error in machine learning?" target="_blank">What is Bayes Error in machine learning?</a> </li>
<li><a href="/rltoken/OXuEmLkHubDofoueWMlY7A" title="Bias/Variance" target="_blank">Bias/Variance</a> (<em>Note: I suggest watching this video at 1.5x - 2x speed</em>)</li>
<li><a href="/rltoken/gVKdBNxmO8FU3eQaNClVZQ" title="Basic Recipe for Machine Learning" target="_blank">Basic Recipe for Machine Learning</a> (<em>Note: I suggest watching this video at 1.5x - 2x speed</em>)</li>
<li><a href="/rltoken/M6c62wjBk5AOOowkj14ITA" title="Why Human Level Performance" target="_blank">Why Human Level Performance</a> (<em>Note: I suggest watching this video at 1.5x - 2x speed</em>)</li>
<li><a href="/rltoken/1yhh1YA_Xa_R3t0xUy4p9Q" title="Avoidable Bias" target="_blank">Avoidable Bias</a> (<em>Note: I suggest watching this video at 1.5x - 2x speed</em>)</li>
<li><a href="/rltoken/YtDkYixp6TUAxMc4liTtBg" title="Understanding Human-Level Performance" target="_blank">Understanding Human-Level Performance</a> (<em>Note: I suggest watching this video at 1.5x - 2x speed</em>)</li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/awuH81I13hn7SPnYtLzlBQ" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is the confusion matrix?</li>
<li>What is type I error? type II?</li>
<li>What is sensitivity? specificity? precision? recall?</li>
<li>What is an F1 score?</li>
<li>What is bias? variance?</li>
<li>What is irreducible error?</li>
<li>What is Bayes error?</li>
<li>How can you approximate Bayes error?</li>
<li>How to calculate bias and variance</li>
<li>How to create a confusion matrix</li>
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
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

  </article>

## Author
* **Samir millan** - [Gaspela04](https://github.com/Gaspela04)
