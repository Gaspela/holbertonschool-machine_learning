<h1 class="gap">0x02. Hidden Markov Models</h1>

<article id="description" class="gap formatted-content">
    <p><a href="https://ibb.co/b6D06tX"><img src="https://i.ibb.co/XWMQWHt/027d4a67aea17e6fa181.jpg" alt="027d4a67aea17e6fa181" border="0"></a></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/F7v-6UX8GSo7tcrLuj3pTg" title="Markov property" target="_blank">Markov property</a></li>
<li><a href="/rltoken/pJySWk8zYyiFBbXha1v9Uw" title="Markov Chain" target="_blank">Markov Chain</a></li>
<li><a href="/rltoken/tJPuYPGZmTCCiajHOHzHPg" title="Properties of Markov Chains" target="_blank">Properties of Markov Chains</a></li>
<li><a href="/rltoken/ek3QosV9fS9Ep7hF7Z8UNA" title="Markov Chains" target="_blank">Markov Chains</a></li>
<li><a href="/rltoken/ismECln2KQ_NWqlhDi4SOA" title="Markov Matrices" target="_blank">Markov Matrices</a></li>
<li><a href="/rltoken/-P79YH94sPDmW3witwXEgA" title="1.3 Convergence of Regular Markov Chains" target="_blank">1.3 Convergence of Regular Markov Chains</a></li>
<li><a href="/rltoken/Gphacn9fdFCQFGMeMyYxlg" title="Markov Chains, Part 1" target="_blank">Markov Chains, Part 1</a></li>
<li><a href="/rltoken/flDg5iw0va1FhUjsMFHgdg" title="Markov Chains, Part 2" target="_blank">Markov Chains, Part 2</a></li>
<li><a href="/rltoken/zRg0ddD8arH7F1hiOlaNiA" title="Markov Chains, Part 3" target="_blank">Markov Chains, Part 3</a></li>
<li><a href="/rltoken/AD3VcrR0vmdPkLIHFCWd2Q" title="Markov Chains, Part 4" target="_blank">Markov Chains, Part 4</a></li>
<li><a href="/rltoken/V7XdIdjg5NJpuWgV_tVk3A" title="Markov Chains, Part 5" target="_blank">Markov Chains, Part 5</a></li>
<li><a href="/rltoken/Iyup5UA69u1UYzIsgcn4Fg" title="Markov Chains, Part 7" target="_blank">Markov Chains, Part 7</a></li>
<li><a href="/rltoken/wXvkFVOTl3NOKWgT63odOw" title="Markov Chains, Part 8" target="_blank">Markov Chains, Part 8</a></li>
<li><a href="/rltoken/UC94QIzIwcX280YAvJTJUA" title="Markov Chains, Part 9" target="_blank">Markov Chains, Part 9</a></li>
<li><a href="/rltoken/Qg8C9pzP1Yr4P8bxECb7pQ" title="Hidden Markov model" target="_blank">Hidden Markov model</a></li>
<li><a href="/rltoken/D4kPhrRbShrDWSANnlJdkQ" title="Hidden Markov Models" target="_blank">Hidden Markov Models</a></li>
<li><a href="/rltoken/CpcwO0SbMD05S7IOfc3jeA" title="(ML 14.1) Markov models - motivating examples" target="_blank">(ML 14.1) Markov models - motivating examples</a></li>
<li><a href="/rltoken/C-TgJ6CKgBUbL3yxfvJHqA" title="(ML 14.2) Markov chains (discrete-time) (part 1)" target="_blank">(ML 14.2) Markov chains (discrete-time) (part 1)</a></li>
<li><a href="/rltoken/zMjTTG-qtP0QfcbYXFujUg" title="(ML 14.3) Markov chains (discrete-time) (part 2)" target="_blank">(ML 14.3) Markov chains (discrete-time) (part 2)</a></li>
<li><a href="/rltoken/tMsk_K-n0mYOtsthhBrQcg" title="(ML 14.4) Hidden Markov models (HMMs) (part 1)" target="_blank">(ML 14.4) Hidden Markov models (HMMs) (part 1)</a></li>
<li><a href="/rltoken/2k8q4yyclHlMoE83WhKf8g" title="(ML 14.5) Hidden Markov models (HMMs) (part 2)" target="_blank">(ML 14.5) Hidden Markov models (HMMs) (part 2)</a></li>
<li><a href="/rltoken/Qljf3X5iH7oaKWuF2I165A" title="(ML 14.6) Forward-Backward algorithm for HMMs" target="_blank">(ML 14.6) Forward-Backward algorithm for HMMs</a></li>
<li><a href="/rltoken/Tc6D_BMgvdxMWGoBtvo-Nw" title="(ML 14.7) Forward algorithm (part 1)" target="_blank">(ML 14.7) Forward algorithm (part 1)</a></li>
<li><a href="/rltoken/AMUSX-wBTAeTsvJKFlOiIQ" title="(ML 14.8) Forward algorithm (part 2)" target="_blank">(ML 14.8) Forward algorithm (part 2)</a></li>
<li><a href="/rltoken/GuKHZZ4HNUS-xnbwBf8YsQ" title="(ML 14.9) Backward algorithm" target="_blank">(ML 14.9) Backward algorithm</a></li>
<li><a href="/rltoken/uZ3KdzsuS0YmbvxDD2G-NQ" title="(ML 14.10) Underflow and the log-sum-exp trick" target="_blank">(ML 14.10) Underflow and the log-sum-exp trick</a></li>
<li><a href="/rltoken/UAmz_LJdG5w3sS_8xSAsGg" title="(ML 14.11) Viterbi algorithm (part 1)" target="_blank">(ML 14.11) Viterbi algorithm (part 1)</a></li>
<li><a href="/rltoken/c0LxuyQ8HeprSObqEVkTQA" title="(ML 14.12) Viterbi algorithm (part 2)" target="_blank">(ML 14.12) Viterbi algorithm (part 2)</a></li>
</ul>

<h2>Learning Objectives</h2>

<ul>
<li>What is the Markov property?</li>
<li>What is a Markov chain?</li>
<li>What is a state?</li>
<li>What is a transition probability/matrix?</li>
<li>What is a stationary state?</li>
<li>What is a regular Markov chain?</li>
<li>How to determine if a transition matrix is regular</li>
<li>What is an absorbing state?</li>
<li>What is a transient state?</li>
<li>What is a recurrent state?</li>
<li>What is an absorbing Markov chain?</li>
<li>What is a Hidden Markov Model?</li>
<li>What is a hidden state?</li>
<li>What is an observation?</li>
<li>What is an emission probability/matrix?</li>
<li>What is a Trellis diagram?</li>
<li>What is the Forward algorithm and how do you implement it?</li>
<li>What is decoding?</li>
<li>What is the Viterbi algorithm and how do you implement it?</li>
<li>What is the Forward-Backward algorithm and how do you implement it?</li>
<li>What is the Baum-Welch algorithm and how do you implement it?</li>
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
</ul>

  </article>

## Author
* **Samir millan** - [Gaspela04](https://github.com/Gaspela04)