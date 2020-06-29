<h1 class="gap">0x07. Convolutional Neural Networks</h1>
<article id="description" class="gap formatted-content">
    <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/9/c9d2bd7153ac51f24e52.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20200629%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20200629T155439Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=591e05646b0590dba1a2b1e039fc81385cd723c48c047c01e4a5f759283d53b2" alt="" style=""></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/KOQSWajVz2BF6QuIM0ZyXg" title="Convolutional neural network" target="_blank">Convolutional neural network</a> </li>
<li><a href="/rltoken/YsCwFCpCZn5dIJM95qc2Dg" title="Convolutional Neural Networks (CNNs) explained" target="_blank">Convolutional Neural Networks (CNNs) explained</a> </li>
<li><a href="/rltoken/lOzKGVsnF4czDq1iVG5CJw" title="The best explanation of Convolutional Neural Networks on the Internet!" target="_blank">The best explanation of Convolutional Neural Networks on the Internet!</a> (<em>It’s pretty good but I wouldn’t call it the best…</em>)</li>
<li><a href="/rltoken/S99iSsHQKr6d73WbYH5uEw" title="Machine Learning is Fun! Part 3: Deep Learning and Convolutional Neural Networks" target="_blank">Machine Learning is Fun! Part 3: Deep Learning and Convolutional Neural Networks</a> </li>
<li><a href="/rltoken/XrV_YYGzqFEIZ6QIvDG7pQ" title="Convolutional Neural Networks: The Biologically-Inspired Model" target="_blank">Convolutional Neural Networks: The Biologically-Inspired Model</a> </li>
<li><a href="/rltoken/iA2Fms5XMdRM7qxt22D7aQ" title="Back Propagation in Convolutional Neural Networks — Intuition and Code" target="_blank">Back Propagation in Convolutional Neural Networks — Intuition and Code</a> </li>
<li><a href="/rltoken/X2wFWCk1U97QfUUMV7hcwA" title="Pooling Layer" target="_blank">Pooling Layer</a> </li>
<li><a href="/rltoken/BE_hLHcLBPNMkWJFFGaHNw" title="deeplearning.ai" target="_blank">deeplearning.ai</a> videos (<em>Note: I suggest watching these videos at 1.5x - 2x speed</em>):

<ul>
<li><a href="/rltoken/pbJeODUGde5jWyVRzbYZWA" title="Why Convolutions" target="_blank">Why Convolutions</a> </li>
<li><a href="/rltoken/hQJA3cgC2mGBk4OfQkRqzg" title="One Layer of a Convolutional Net" target="_blank">One Layer of a Convolutional Net</a></li>
<li><a href="/rltoken/8AU4cPmX3jn8wkd0f0h-bg" title="Simple Convolutional Network Example" target="_blank">Simple Convolutional Network Example</a></li>
<li><a href="/rltoken/JXJg5MMzZ4JEbM8Wv7oemw" title="CNN Example" target="_blank">CNN Example</a></li>
</ul></li>
<li><a href="/rltoken/R84em95wWIF6PEEu4WG7HA" title="Gradient-Based Learning Applied to Document Recognition (LeNet-5)" target="_blank">Gradient-Based Learning Applied to Document Recognition (LeNet-5)</a> </li>
</ul>

<p><strong>References</strong>:</p>

<ul>
<li><a href="/rltoken/DVk3zlZ0Q-qGix8jJS27bA" title="tf.layers.Conv2D" target="_blank">tf.layers.Conv2D</a> </li>
<li><a href="/rltoken/PpoH6RtuEqP9GWIgDi18Sg" title="tf.keras.layers.Conv2D" target="_blank">tf.keras.layers.Conv2D</a> </li>
<li><a href="/rltoken/PkgB8zBWir6YXZ4gvCB1RQ" title="tf.layers.AveragePooling2D" target="_blank">tf.layers.AveragePooling2D</a> </li>
<li><a href="/rltoken/j4DpfEFcJtEUCuSgt8ajUQ" title="tf.keras.layers.AveragePooling2D" target="_blank">tf.keras.layers.AveragePooling2D</a> </li>
<li><a href="/rltoken/zWhYkmtNCgm-mcYhQpfc9w" title="tf.layers.MaxPooling2D" target="_blank">tf.layers.MaxPooling2D</a> </li>
<li><a href="/rltoken/npndxYxY_sK3UkY9wixirg" title="tf.keras.layers.MaxPooling2D" target="_blank">tf.keras.layers.MaxPooling2D</a> </li>
<li><a href="/rltoken/CratgY38hewNI2b5Ggl63g" title="tf.layers.Flatten" target="_blank">tf.layers.Flatten</a> </li>
<li><a href="/rltoken/KMgCZoFmgC5644KqsAivPA" title="tf.keras.layers.Flatten" target="_blank">tf.keras.layers.Flatten</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/aQ-z_4V5LRCdYapcTGaQig" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is a convolutional layer?</li>
<li>What is a pooling layer?</li>
<li>Forward propagation over convolutional and pooling layers</li>
<li>Back propagation over convolutional and pooling layers</li>
<li>How to build a CNN using Tensorflow and Keras</li>
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
<li>Unless otherwise noted, you are not allowed to import any module</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

  </article>

## Author
* **Samir millan** - [Gaspela04](https://github.com/Gaspela04)
