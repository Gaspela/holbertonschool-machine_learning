<h1 class="gap">0x02. Tensorflow</h1>

<article id="description" class="gap formatted-content">
    <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/10/6f157fe3360e5ec1ceb6.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20200816%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20200816T155702Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=58136dc9168085b7c678d941db66f18f1fd6e80a3f1ec13b8ebe9958b5dbad0e" alt="" style=""></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/NCuz9NxxUi3cSwIPFa2JJw" title="Low Level Intro" target="_blank">Low Level Intro</a>  <strong>(Excluding <code>Datasets</code> and <code>Feature columns</code>)</strong></li>
<li><a href="/rltoken/37gGDNtBD6VWB0oNJBzvgw" title="Graphs" target="_blank">Graphs</a> </li>
<li><a href="/rltoken/6R5R5RMtcecU1sdmMjXoNw" title="Tensors" target="_blank">Tensors</a> </li>
<li><a href="/rltoken/YZilxEbcFuvS8kGhRDhCjw" title="Variables" target="_blank">Variables</a> </li>
<li><a href="/rltoken/hv3HqhZFTHIf0X5OMMrgRw" title="Placeholders" target="_blank">Placeholders</a> </li>
<li><a href="/rltoken/GxnmEnPfxVLA9QRQEM998g" title="Save and Restore" target="_blank">Save and Restore</a> <strong>(Up to <code>Save and restore models</code>, excluded)</strong></li>
<li><a href="/rltoken/YvqhzzepzXxhivU2L1DqIw" title="TensorFlow, why there are 3 files after saving the model?" target="_blank">TensorFlow, why there are 3 files after saving the model?</a> </li>
<li><a href="/rltoken/HIAgr0xW-aEvfCpxEJnj8w" title="Exporting and Importing a MetaGraph" target="_blank">Exporting and Importing a MetaGraph</a> </li>
<li><a href="/rltoken/qqVDNbC7gGaHP82zGkJcQQ" title="TensorFlow - import meta graph and use variables from it" target="_blank">TensorFlow - import meta graph and use variables from it</a> </li>
</ul>

<p><strong>References</strong>: </p>

<ul>
<li><a href="/rltoken/TbSeD8MOTEJwsohwwK64Og" title="tf.Graph" target="_blank">tf.Graph</a> </li>
<li><a href="/rltoken/infyePgJiCFB1U3bjJtIwg" title="tf.Session" target="_blank">tf.Session</a> 

<ul>
<li><a href="/rltoken/8ajLSmNmwxAnyGiY47cvmg" title="tf.Session.run" target="_blank">tf.Session.run</a> </li>
</ul></li>
<li><a href="/rltoken/1gpB1z9ptlePj5Iq4Tfyyw" title="tf.Tensor" target="_blank">tf.Tensor</a> </li>
<li><a href="/rltoken/KYblPwi0zDfxVd9LBkkMoA" title="tf.Variable" target="_blank">tf.Variable</a> </li>
<li><a href="/rltoken/M7s4gxCwIQ7TVH6zCT2YmQ" title="tf.constant" target="_blank">tf.constant</a> </li>
<li><a href="/rltoken/Gsar0Zmc7qjm88eMscHyyA" title="tf.placeholder" target="_blank">tf.placeholder</a> </li>
<li><a href="/rltoken/M7GgNusP8s1AtUPfpB6ZDQ" title="tf.Operation" target="_blank">tf.Operation</a> </li>
<li><a href="/rltoken/CktRWcAj2FoAZYty-ZH8RA" title="tf.layers" target="_blank">tf.layers</a> 

<ul>
<li><a href="/rltoken/nUEZ1NneM8nKz076yGN9mA" title="tf.layers.Dense" target="_blank">tf.layers.Dense</a> </li>
</ul></li>
<li><a href="/rltoken/TlYNLPU6qFryRNO9gnOENA" title="tf.contrib.layers.variance_scaling_initializer" target="_blank">tf.contrib.layers.variance_scaling_initializer</a> </li>
<li><a href="/rltoken/QGpJMlscoeM40MAFm9MhQA" title="tf.nn" target="_blank">tf.nn</a> 

<ul>
<li><a href="/rltoken/_Vz8d--SWiB2vV_Pvc4DHg" title="tf.nn.relu" target="_blank">tf.nn.relu</a></li>
<li><a href="/rltoken/XrNyw-JqRkZbRizUr0vDuw" title="tf.nn.sigmoid" target="_blank">tf.nn.sigmoid</a></li>
<li><a href="/rltoken/eAMpEIxRRFVyYW_hSgGAiA" title="tf.nn.tanh" target="_blank">tf.nn.tanh</a></li>
</ul></li>
<li><a href="/rltoken/UeKK4-AU3ved6LDqWC5Jqw" title="tf.losses" target="_blank">tf.losses</a> 

<ul>
<li><a href="/rltoken/-EAXiuDfwG3vRJWoT9dQXQ" title="tf.losses.softmax_cross_entropy" target="_blank">tf.losses.softmax_cross_entropy</a> </li>
</ul></li>
<li><a href="/rltoken/PibDlLzY868MjsnN0rClMw" title="tf.train" target="_blank">tf.train</a> 

<ul>
<li><a href="/rltoken/ol5IIMmshNODLl0o0C-y0A" title="tf.train.GradientDescentOptimizer" target="_blank">tf.train.GradientDescentOptimizer</a> 

<ul>
<li><a href="/rltoken/KUncv1A0Bpbme-y1IkuxGA" title="tf.train.GradientDescentOptimizer.minimize" target="_blank">tf.train.GradientDescentOptimizer.minimize</a> </li>
</ul></li>
<li><a href="/rltoken/Lor8NfNcQV3hoSVr5c8QHg" title="tf.train.Saver" target="_blank">tf.train.Saver</a> 

<ul>
<li><a href="/rltoken/Lor8NfNcQV3hoSVr5c8QHg" title="tf.train.Saver.save" target="_blank">tf.train.Saver.save</a> </li>
<li><a href="/rltoken/Lor8NfNcQV3hoSVr5c8QHg" title="tf.train.Saver.restore" target="_blank">tf.train.Saver.restore</a> </li>
</ul></li>
</ul></li>
<li><a href="/rltoken/9IQdGI9QLowCejMv3CVl6g" title="tf.add_to_collection" target="_blank">tf.add_to_collection</a></li>
<li><a href="/rltoken/J4hJnLXeSleN2ZzIM8Fotg" title="tf.get_collection" target="_blank">tf.get_collection</a></li>
<li><a href="/rltoken/EBxOjAAUzcmSnuxsuszWuw" title="tf.global_variables_initializer" target="_blank">tf.global_variables_initializer</a> </li>
<li><a href="/rltoken/EB8VWs61u_yiEBFqtNkdjA" title="tf.argmax" target="_blank">tf.argmax</a> </li>
<li><a href="/rltoken/VjS8GfzTkWGEwutbuY-v-g" title="tf.equal" target="_blank">tf.equal</a> </li>
<li><a href="/rltoken/TBb2GYY_reysO2huNAeVWw" title="tf.set_random_seed" target="_blank">tf.set_random_seed</a> </li>
<li><a href="/rltoken/nxW64Pqj0lpC2QhMY48OeA" title="tf.name_scope" target="_blank">tf.name_scope</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/TkDp43tDqNSGq-DVx6AFQg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is tensorflow?</li>
<li>What is a session? graph?</li>
<li>What are tensors?</li>
<li>What are variables? constants? placeholders? How do you use them?</li>
<li>What are operations? How do you use them?</li>
<li>What are namespaces? How do you use them?</li>
<li>How to train a neural network in tensorflow</li>
<li>What is a checkpoint?</li>
<li>How to save/load a model with tensorflow</li>
<li>What is the graph collection?</li>
<li>How to add and get variables from the collection</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 16.04 LTS using <code>python3</code> (version 3.5)</li>
<li>Your files will be executed with <code>numpy</code> (version 1.15) and <code>tensorflow</code> (version 1.12)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.4)</li>
<li>All your modules should have documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>Unless otherwise noted, you are not allowed to import any module except <code>import tensorflow as tf</code></li>
<li>You are not allowed to use the <code>keras</code> module in <code>tensorflow</code></li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h2>More Info</h2>

<h3>Installing Tensorflow 1.12</h3>

<pre><code>$ pip install --user tensorflow==1.12
</code></pre>

<h3>Optimize Tensorflow (Optional)</h3>

<p>In order to get full use of your computer’s hardware, you will need to build tensorflow from source.</p>

<p>Here are some extra reading on why/how to do this:</p>

<ul>
<li><a href="/rltoken/a68ppw4Kiya9v8LBWGtzDg" title="How to compile Tensorflow with SSE4.2 and AVX instructions?" target="_blank">How to compile Tensorflow with SSE4.2 and AVX instructions?</a></li>
<li><a href="/rltoken/tjzGgbUqSmOnfuDex8XJtg" title="Installing Bazel on Ubuntu" target="_blank">Installing Bazel on Ubuntu</a></li>
<li><a href="/rltoken/r7MqLv3S16v0flVqkjyu5w" title="Build from Source" target="_blank">Build from Source</a></li>
<li><a href="/rltoken/YNrw0GgZRRfp82L6HqyMAQ" title="Performance" target="_blank">Performance</a></li>
<li><a href="/rltoken/bOcLGCSg-SUtIa5hSJpKxQ" title="Python Configuration Error: 'PYTHON_BIN_PATH' environment variable is not set" target="_blank">Python Configuration Error: ‘PYTHON_BIN_PATH’ environment variable is not set</a></li>
</ul>

<p>The following instructions assume you already have <code>tensorflow</code> (version 1.12) installed and that you do not have access to a <a href="/rltoken/5Qbpp3Vkr46ybyNQG1cD0A" title="GPU" target="_blank">GPU</a>:</p>

<h4>0. Install All Dependencies:</h4>

<pre><code>$ sudo apt-get install pkg-config zip g++ zlib1g-dev unzip python python3-dev
</code></pre>

<h4>1. Install Bazel</h4>

<pre><code>$ wget https://github.com/bazelbuild/bazel/releases/download/0.18.1/bazel-0.18.1-installer-linux-x86_64.sh
$ chmod +x bazel-0.18.1-installer-linux-x86_64.sh
$ sudo ./bazel-0.18.1-installer-linux-x86_64.sh --bin=/bin
</code></pre>

<p>Add the line <code>source /usr/local/lib/bazel/bin/bazel-complete.bash</code> to your <code>~/.bashrc</code> if you want <code>bash</code> to tab complete <code>bazel</code>.</p>

<h4>2. Clone Tensorflow Repository</h4>

<pre><code>$ git clone https://github.com/tensorflow/tensorflow.git
$ cd tensorflow
$git checkout r1.12
</code></pre>

<h4>3. Build and Install Tensorflow</h4>

<pre><code>$ export PYTHON_BIN_PATH=/usr/bin/python3 # or wherever python3 is located
$ bazel build --config=mkl --config=opt //tensorflow/tools/pip_package:build_pip_package
$ ./bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg
$ pip install --user /tmp/tensorflow_pkg/tensorflow-1.12.0-cp35-cp35m-linux_x86_64.whl
</code></pre>

<h4>4. Remove Tensorflow Repository</h4>

<pre><code>$ cd ..
$ rm -rf tensorflow
</code></pre>

<p>Now <code>tensorflow</code> will be able to fully utilize the parallel processing capabilities of your computer’s hardware, which will make your training MUCH faster!</p>

  </article>

## Author
* **Samir millan** - [Gaspela04](https://github.com/Gaspela04)
