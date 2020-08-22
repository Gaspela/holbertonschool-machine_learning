<h1 class="gap">0x03. Optimization</h1>

<article id="description" class="gap formatted-content">
    <p><a href="https://imgbb.com/"><img src="https://i.ibb.co/hH7SR4C/2bc924532bc4a901e74d.jpg" alt="2bc924532bc4a901e74d" border="0"></a></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/1QBGvpFW16wWkdzpbPQ3DQ" title="Hyperparameter (machine learning)" target="_blank">Hyperparameter (machine learning)</a> </li>
<li><a href="/rltoken/w-mu-1FTMnCw_bo51x1H1w" title="Feature scaling" target="_blank">Feature scaling</a> </li>
<li><a href="/rltoken/GGzAGiwPp84A1_Oz9KL3tQ" title="Why, How and When to Scale your Features" target="_blank">Why, How and When to Scale your Features</a></li>
<li><a href="/rltoken/qAJARRbV2HbG-xSTK_Ioxw" title="Normalizing your data" target="_blank">Normalizing your data</a> </li>
<li><a href="/rltoken/_Na-3oh6JT9YqhWnxE5cRg" title="Moving average" target="_blank">Moving average</a> </li>
<li><a href="/rltoken/-TMwJwWHSavWMohuQ5yQvA" title="An overview of gradient descent optimization algorithms" target="_blank">An overview of gradient descent optimization algorithms</a> </li>
<li><a href="/rltoken/-Bpr2w5FmPvMnmn-EHW6Rw" title="A Gentle Introduction to Mini-Batch Gradient Descent and How to Configure Batch Size" target="_blank">A Gentle Introduction to Mini-Batch Gradient Descent and How to Configure Batch Size</a> </li>
<li><a href="/rltoken/OQ37CrydFEL93rCxFkyC8w" title="Stochastic Gradient Descent with momentum" target="_blank">Stochastic Gradient Descent with momentum</a> </li>
<li><a href="/rltoken/ReFIVBjk0_CsH1yv1nEFQg" title="Understanding RMSprop" target="_blank">Understanding RMSprop</a> </li>
<li><a href="/rltoken/uKCErhYQXBp-Lb2WFfRe1Q" title="Adam" target="_blank">Adam</a> </li>
<li><a href="/rltoken/0J5PD8a-UTeFLiS2mGqcsw" title="Learning Rate Schedules" target="_blank">Learning Rate Schedules</a></li>
<li><a href="/rltoken/-tmvgOpWb_sjJzR5hv6VyA" title="deeplearning.ai" target="_blank">deeplearning.ai</a> videos (<em>Note: I suggest watching these video at 1.5x - 2x speed</em>):

<ul>
<li><a href="/rltoken/cXcbUMLDZZHhvQb9jDQweg" title="Normalizing Inputs" target="_blank">Normalizing Inputs</a> </li>
<li><a href="/rltoken/BI4l4WlyRrmNLbjpfJPLCQ" title="Mini Batch Gradient Descent" target="_blank">Mini Batch Gradient Descent</a></li>
<li><a href="/rltoken/dsdZXmqN6wm9EC4HuQOD6g" title="Understanding Mini-Batch Gradient Descent" target="_blank">Understanding Mini-Batch Gradient Descent</a></li>
<li><a href="/rltoken/5N75PDrSPlBuQEXyV5lTuw" title="Exponentially Weighted Averages" target="_blank">Exponentially Weighted Averages</a></li>
<li><a href="/rltoken/V1fGt--3DYdXIlFaZKxQ1Q" title="Understanding Exponentially Weighted Averages" target="_blank">Understanding Exponentially Weighted Averages</a></li>
<li><a href="/rltoken/F4Of4Km8QRl2mH6iCdGReg" title="Bias Correction of Exponentially Weighted Averages" target="_blank">Bias Correction of Exponentially Weighted Averages</a></li>
<li><a href="/rltoken/DwaovproRxolK5BN2LTbQQ" title="Gradient Descent With Momentum" target="_blank">Gradient Descent With Momentum</a></li>
<li><a href="/rltoken/knRX814HFUQcumxnOOJSyw" title="RMSProp" target="_blank">RMSProp</a></li>
<li><a href="/rltoken/c9O01hgfn3335zzQPGtlkQ" title="Adam Optimization Algorithm" target="_blank">Adam Optimization Algorithm</a></li>
<li><a href="/rltoken/PXmH63ae5SdNBSvwZOcN5w" title="Learning Rate Decay" target="_blank">Learning Rate Decay</a></li>
<li><a href="/rltoken/bbhczA5i6hu1KC1SVFZf1g" title="Normalizing Activations in a Network" target="_blank">Normalizing Activations in a Network</a></li>
<li><a href="/rltoken/tjvojWwSp0hhFontTO7ygw" title="Fitting Batch Norm Into Neural Networks" target="_blank">Fitting Batch Norm Into Neural Networks</a></li>
<li><a href="/rltoken/14HrGT4EmpD5lhQThvFOhg" title="Why Does Batch Norm Work?" target="_blank">Why Does Batch Norm Work?</a></li>
<li><a href="/rltoken/RQob4hYaNfjmDDeW7j49bA" title="Batch Norm At Test Time" target="_blank">Batch Norm At Test Time</a></li>
<li><a href="/rltoken/mHsAE3RUtXZ0UQTOgtab9A" title="The Problem of Local Optima" target="_blank">The Problem of Local Optima</a></li>
</ul></li>
</ul>

<p><strong>References</strong>:</p>

<ul>
<li><a href="/rltoken/J5BKKhzfFgESH_Cn8xw-Sw" title="numpy.random.permutation" target="_blank">numpy.random.permutation</a> </li>
<li><a href="/rltoken/s17yxnfOfqpAD_TEboHqFg" title="tf.nn.moments" target="_blank">tf.nn.moments</a> </li>
<li><a href="/rltoken/ynknPVmMj0QOZ_3KGe4yOg" title="tf.train.MomentumOptimizer" target="_blank">tf.train.MomentumOptimizer</a> </li>
<li><a href="/rltoken/vckCzM32lR3Vv628QX15QA" title="tf.train.RMSPropOptimizer" target="_blank">tf.train.RMSPropOptimizer</a> </li>
<li><a href="/rltoken/zmm4PCMEzzCnHNX12aZBhg" title="tf.train.AdamOptimizer" target="_blank">tf.train.AdamOptimizer</a> </li>
<li><a href="/rltoken/RM0nF8Xm36tYOfgPouRTMA" title="tf.nn.batch_normalization" target="_blank">tf.nn.batch_normalization</a> </li>
<li><a href="/rltoken/rRHcYKGdx5AgSFQ54kScNA" title="tf.train.inverse_time_decay" target="_blank">tf.train.inverse_time_decay</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/pGZiNGsTQx3yGYEd6O7w9A" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is a hyperparameter?</li>
<li>How and why do you normalize your input data?</li>
<li>What is a saddle point?</li>
<li>What is stochastic gradient descent?</li>
<li>What is mini-batch gradient descent?</li>
<li>What is a moving average? How do you implement it?</li>
<li>What is gradient descent with momentum? How do you implement it?</li>
<li>What is RMSProp? How do you implement it?</li>
<li>What is Adam optimization? How do you implement it?</li>
<li>What is learning rate decay? How do you implement it?</li>
<li>What is batch normalization? How do you implement it?</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 16.04 LTS using <code>python3</code> (version 3.5)</li>
<li>Your files will be executed with <code>numpy</code> (version 1.15) and tensorflow (version 1.12)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.4)</li>
<li>All your modules should have documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>Unless otherwise noted, you are not allowed to import any module except <code>import numpy as np</code> and/or <code>import tensorflow as tf</code></li>
<li>You should not import any module unless it is being used</li>
<li>You are not allowed to use the <code>keras</code> module in <code>tensorflow</code></li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h2>More Info</h2>

<h3>Testing</h3>

<p>Please use the following checkpoints for to accompany the following <code>tensorflow</code> main files. You do not need to push these files to GitHub. Your code will not be tested with these files.</p>

<ul>
<li><a href="/rltoken/K61Yny_5XY-LD75_CnGuPw" title="graph.ckpt.data-00000-of-00001" target="_blank">graph.ckpt.data-00000-of-00001</a></li>
<li><a href="/rltoken/c5j9qA0uWGWmX0jg8GbPew" title="graph.ckpt.index" target="_blank">graph.ckpt.index</a></li>
<li><a href="/rltoken/6kgrAdCqPwhJl8fuFjo_6g" title="graph.ckpt.meta" target="_blank">graph.ckpt.meta</a></li>
</ul>

  </article>
