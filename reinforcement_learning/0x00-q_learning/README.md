<h1 class="gap">0x00. Q-learning</h1>

<article id="description" class="gap formatted-content">
    <p><a href="https://ibb.co/vh6HDBW"><img src="https://i.ibb.co/8bL0XBw/5478322429e44f196aff6896f42ce2ea0741ba36.jpg" alt="5478322429e44f196aff6896f42ce2ea0741ba36" border="0"></a></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/uSJcrn4-wamVCfbQQtI9EA" title="An introduction to Reinforcement Learning" target="_blank">An introduction to Reinforcement Learning</a></li>
<li><a href="/rltoken/zG8n_isnc-gv766bLi_NBw" title="Simple Reinforcement Learning: Q-learning" target="_blank">Simple Reinforcement Learning: Q-learning</a></li>
<li><a href="/rltoken/km2Nyp6zyAast1k5v9P_wQ" title="Markov Decision Processes (MDPs) - Structuring a Reinforcement Learning Problem" target="_blank">Markov Decision Processes (MDPs) - Structuring a Reinforcement Learning Problem</a></li>
<li><a href="/rltoken/mM6iGVu8uSr7siZJCM-D-Q" title="Expected Return - What Drives a Reinforcement Learning Agent in an MDP" target="_blank">Expected Return - What Drives a Reinforcement Learning Agent in an MDP</a></li>
<li><a href="/rltoken/HgOMxHB7SipUwDk6s3ZhUA" title="Policies and Value Functions - Good Actions for a Reinforcement Learning Agent" target="_blank">Policies and Value Functions - Good Actions for a Reinforcement Learning Agent</a></li>
<li><a href="/rltoken/Pd4kGKXr9Pd0qQ4RO93Xww" title="What do Reinforcement Learning Algorithms Learn - Optimal Policies" target="_blank">What do Reinforcement Learning Algorithms Learn - Optimal Policies</a></li>
<li><a href="/rltoken/vj2E0Jizi5qUKn6hLUnVSQ" title="Q-Learning Explained - A Reinforcement Learning Technique" target="_blank">Q-Learning Explained - A Reinforcement Learning Technique</a></li>
<li><a href="/rltoken/zQNxN36--R7hzP0ktiKOsg" title="Exploration vs. Exploitation - Learning the Optimal Reinforcement Learning Policy" target="_blank">Exploration vs. Exploitation - Learning the Optimal Reinforcement Learning Policy</a></li>
<li><a href="/rltoken/GMcf0lCJ-SlaF6FSUKaozA" title="OpenAI Gym and Python for Q-learning - Reinforcement Learning Code Project" target="_blank">OpenAI Gym and Python for Q-learning - Reinforcement Learning Code Project</a></li>
<li><a href="/rltoken/GE2nKBHgehHdd_XN7lK0Gw" title="Train Q-learning Agent with Python - Reinforcement Learning Code Project" target="_blank">Train Q-learning Agent with Python - Reinforcement Learning Code Project</a></li>
<li><a href="/rltoken/Dz37ih49PpmrJicq_IP3aA" title="Markov Decision Processes" target="_blank">Markov Decision Processes</a></li>
</ul>

<p><strong>Definitions to skim:</strong></p>

<ul>
<li><a href="/rltoken/z1eKcn91HbmHYtdwYEEXOQ" title="Reinforcement Learning" target="_blank">Reinforcement Learning</a></li>
<li><a href="/rltoken/PCdKyrHQRNARmxeSUCiOYQ" title="Markov Decision Process" target="_blank">Markov Decision Process</a></li>
<li><a href="/rltoken/T80msozXZ3wlSmq0ScCvrQ" title="Q-learning" target="_blank">Q-learning</a></li>
</ul>

<p><strong>References</strong>:</p>

<ul>
<li><a href="/rltoken/P8gDRc_PRTeK4okeztvmDQ" title="OpenAI Gym" target="_blank">OpenAI Gym</a></li>
<li><a href="https://github.com/openai/gym/blob/master/gym/envs/toy_text/frozen_lake.py" title="OpenAI Gym: Frozen Lake env" target="_blank">OpenAI Gym: Frozen Lake env</a></li>
</ul>

<h2>Learning Objectives</h2>

<ul>
<li>What is a Markov Decision Process?</li>
<li>What is an environment?</li>
<li>What is an agent?</li>
<li>What is a state?</li>
<li>What is a policy function?</li>
<li>What is a value function? a state-value function? an action-value function?</li>
<li>What is a discount factor?</li>
<li>What is the Bellman equation?</li>
<li>What is epsilon greedy?</li>
<li>What is Q-learning?</li>
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

<h2>Installing OpenAI’s Gym</h2>

<pre><code>pip install --user gym
</code></pre>

  </article>

## Author
* **Samir millan** - [Gaspela04](https://github.com/Gaspela04)