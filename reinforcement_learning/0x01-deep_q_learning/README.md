<h1 class="gap">0x01. Deep Q-learning</h1>

<div class="gap">
  <p><a href="https://imgbb.com/"><img src="https://i.ibb.co/Mh8Lh9Q/9239a27ccd609cb9092aba0e6bb55ba7b5cf0b6b.gif" alt="9239a27ccd609cb9092aba0e6bb55ba7b5cf0b6b" border="0"></a></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/vf8M2yFL9vWcFftBWFG2KQ" title="Deep Q-Learning - Combining Neural Networks and Reinforcement Learning" target="_blank">Deep Q-Learning - Combining Neural Networks and Reinforcement Learning</a></li>
<li><a href="/rltoken/LciKBr548xY_iD4QkUatNw" title="Replay Memory Explained - Experience for Deep Q-Network Training" target="_blank">Replay Memory Explained - Experience for Deep Q-Network Training</a></li>
<li><a href="/rltoken/ZwReaNdr4Ei4GxWr-56oFg" title="Training a Deep Q-Network - Reinforcement Learning" target="_blank">Training a Deep Q-Network - Reinforcement Learning</a></li>
<li><a href="/rltoken/xAP3VzSnw0HLwjrBRn46Xw" title="Training a Deep Q-Network with Fixed Q-targets - Reinforcement Learning" target="_blank">Training a Deep Q-Network with Fixed Q-targets - Reinforcement Learning</a></li>
</ul>

<p><strong>References</strong>:</p>

<ul>
<li><a href="/rltoken/mSQhyiu7FEaFi_qTft1G2w" title="keras-rl" target="_blank">keras-rl</a>

<ul>
<li><a href="https://github.com/keras-rl/keras-rl/blob/master/rl/policy.py" title="rl.policy" target="_blank">rl.policy</a></li>
<li><a href="https://github.com/keras-rl/keras-rl/blob/master/rl/memory.py" title="rl.memory" target="_blank">rl.memory</a></li>
<li><a href="https://github.com/keras-rl/keras-rl/blob/master/rl/agents/dqn.py" title="rl.agents.dqn" target="_blank">rl.agents.dqn</a></li>
</ul></li>
<li><a href="/rltoken/SekcqEIbg0hxdEvoQSB-kA" title="Playing Atari with Deep Reinforcement Learning" target="_blank">Playing Atari with Deep Reinforcement Learning</a></li>
</ul>

<h2>Learning Objectives</h2>

<ul>
<li>What is Deep Q-learning?</li>
<li>What is the policy network?</li>
<li>What is replay memory?</li>
<li>What is the target network?</li>
<li>Why must we utilize two separate networks during training?</li>
<li>What is keras-rl? How do you use it?</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 16.04 LTS using <code>python3</code> (version 3.5)</li>
<li>Your files will be executed with <code>numpy</code> (version 1.15),  <code>gym</code> (version 0.17.2), <code>keras</code> (version 2.2.5), and <code>keras-rl</code> (version 0.4.2)</li>
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

<h2>Installing Keras-RL</h2>

<pre><code>pip install --user keras-rl
</code></pre>

<h3>Dependencies (that should already be installed)</h3>

<pre><code>pip install --user keras==2.2.4
pip install --user Pillow
pip install --user h5py
</code></pre>

</div>

## Author
* **Samir millan** - [Gaspela04](https://github.com/Gaspela04)