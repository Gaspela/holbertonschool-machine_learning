<h1 class="gap">0x06. Keras</h1>

<article id="description" class="gap formatted-content">
    <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/11/c48e37d9cda2293173b7.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20200831%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20200831T171223Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=37c2f7e2803bf04b5fa38ad81ea05f6865ff4fdf95f84c3a835fc65d818c146d" alt="" style=""></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/Q6LXU1f1JwaOe7fakxQYMA" title="Keras Explained" target="_blank">Keras Explained</a> (<em>starting at 3:48</em>)</li>
<li><a href="/rltoken/aMY5GW_HGJwP9Q5wvSI-Pw" title="Keras" target="_blank">Keras</a> <strong>(up to <code>Eager execution</code>, excluded, skipping <code>Train from tf.data datasets</code>, <code>Model subclassing</code>, and <code>Custom layers</code>)</strong></li>
<li><a href="/rltoken/9wXncIBTP1NMQZ-djKipUw" title="Hierarchical Data Format" target="_blank">Hierarchical Data Format</a> </li>
</ul>

<p><strong>References</strong>:</p>

<ul>
<li><a href="/rltoken/QIr8pYMIq97fL1W_0Xf5Lw" title="tf.keras" target="_blank">tf.keras</a>

<ul>
<li><a href="/rltoken/tt59IJwHm-jR6wsj3-xGmg" title="tf.keras.models" target="_blank">tf.keras.models</a> </li>
<li><a href="/rltoken/RkojCB9z3AMwRhfwGn8-Sg" title="tf.keras.activations" target="_blank">tf.keras.activations</a> </li>
<li><a href="/rltoken/4nuPR_tgTHRVPJf58q1GkQ" title="tf.keras.callbacks" target="_blank">tf.keras.callbacks</a> </li>
<li><a href="/rltoken/MGIvFa_LFN9vJZDgyDxEIg" title="tf.keras.initializers" target="_blank">tf.keras.initializers</a> </li>
<li><a href="/rltoken/RcHDkU1YPRDB0jvJpQydlw" title="tf.keras.layers" target="_blank">tf.keras.layers</a> </li>
<li><a href="/rltoken/8WAjEs_O7B1e4mSbrxe1ug" title="tf.keras.losses" target="_blank">tf.keras.losses</a> </li>
<li><a href="/rltoken/CIyMKjRfwJrGHoMjYUOW7w" title="tf.keras.metrics" target="_blank">tf.keras.metrics</a> </li>
<li><a href="/rltoken/2xQZg3VcLSTSZuc3ZiaTtw" title="tf.keras.optimizers" target="_blank">tf.keras.optimizers</a> </li>
<li><a href="/rltoken/GTDal6CFChWOd2a0aL8ilw" title="tf.keras.regularizers" target="_blank">tf.keras.regularizers</a> </li>
<li><a href="/rltoken/HzhMInrXwKYfoymxD5nndQ" title="tf.keras.utils" target="_blank">tf.keras.utils</a> </li>
</ul></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/PCF_6RIHFTGdVz23h5v2fg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is Keras?</li>
<li>What is a model?</li>
<li>How to instantiate a model (2 ways)</li>
<li>How to build a layer</li>
<li>How to add regularization to a layer</li>
<li>How to add dropout to a layer</li>
<li>How to add batch normalization</li>
<li>How to compile a model</li>
<li>How to optimize a model</li>
<li>How to fit a model</li>
<li>How to use validation data</li>
<li>How to perform early stopping</li>
<li>How to measure accuracy</li>
<li>How to evaluate a model</li>
<li>How to make a prediction with a model</li>
<li>How to access the weights/outputs of a model</li>
<li>What is HDF5?</li>
<li>How to save and load a model’s weights, a model’s configuration, and the entire model</li>
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
<li>Unless otherwise noted, you are not allowed to import any module except <code>import tensorflow.keras as K</code></li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

  </article>

## Author
* **Samir millan** - [Gaspela04](https://github.com/Gaspela04)
