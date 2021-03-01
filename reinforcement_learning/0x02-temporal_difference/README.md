<h1 class="gap">0x02. Temporal Difference</h1>

<div class="gap" id="project-description">
  <p><a href="https://imgbb.com/"><img src="https://i.ibb.co/2KsBT8D/585a265aeec957ee2e307cbf638f69d325c079b8.jpg" alt="585a265aeec957ee2e307cbf638f69d325c079b8" border="0"></a></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/UhMzeMiBhdT6fLwuHZOD9Q" title="RL Course by David Silver - Lecture 4: Model-Free Prediction" target="_blank">RL Course by David Silver - Lecture 4: Model-Free Prediction</a></li>
<li><a href="/rltoken/HdjREYGtAmh_0tVVd0vKlQ" title="RL Course by David Silver - Lecture 5: Model Free Control" target="_blank">RL Course by David Silver - Lecture 5: Model Free Control</a></li>
<li><a href="/rltoken/5iRtO0r2yA3kKU1VaGExaw" title="Simple Reinforcement Learning: Temporal Difference Learning" target="_blank">Simple Reinforcement Learning: Temporal Difference Learning</a></li>
<li><a href="/rltoken/g2TAyv6DCK0cDHywwEj3Fg" title="On-Policy TD Control" target="_blank">On-Policy TD Control</a></li>
</ul>

<p><strong>Definitions to skim:</strong></p>

<ul>
<li><a href="/rltoken/6HSTI0OqJMmjH7qqwy2TaQ" title="Monte Carlo method" target="_blank">Monte Carlo method</a></li>
<li><a href="/rltoken/Up_ZNMP2uvVMOAadqg_94g" title="Temporal difference learning" target="_blank">Temporal difference learning</a></li>
<li><a href="/rltoken/rl_suhee8QQjLBCfOTzuUA" title="State–action–reward–state–action" target="_blank">State–action–reward–state–action</a></li>
</ul>

<h2>Learning Objectives</h2>

<ul>
<li>What is Monte Carlo?</li>
<li>What is Temporal Difference?</li>
<li>What is bootstrapping?</li>
<li>What is n-step temporal difference?</li>
<li>What is TD(λ)?</li>
<li>What is an eligibility trace?</li>
<li>What is SARSA? SARSA(λ)? SARSAMAX?</li>
<li>What is ‘on-policy’ vs ‘off-policy’?</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 16.04 LTS using <code>python3</code> (version 3.5)</li>
<li>Your files will be executed with <code>numpy</code> (version 1.15), and <code>gym</code> (version 0.7)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.4)</li>
<li>All your modules should have documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>All your files must be executable</li>
<li><strong>Your code should use the minimum number of operations</strong></li>
</ul>

</div>

## Author
* **Samir millan** - [Gaspela04](https://github.com/Gaspela04)