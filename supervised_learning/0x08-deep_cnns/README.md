<h1 class="gap">0x08. Deep Convolutional Architectures</h1>

<article id="description" class="gap formatted-content">
    <p><a href="https://imgbb.com/"><img src="https://i.ibb.co/H25GxRF/b65616d913a345dcbd8e.jpg" alt="b65616d913a345dcbd8e" border="0"></a></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/mQKrG3YdbOZdhZ_ZvlDLNA" title="Vanishing Gradient Problem" target="_blank">Vanishing Gradient Problem</a> </li>
<li><a href="/rltoken/VD6BdzGLeGcpfdv_hglj7g" title="1x1 Convolutions" target="_blank">1x1 Convolutions</a> </li>
<li><a href="/rltoken/3fzjrt4yRo7Co3w-O-mAwA" title="What does 1x1 convolution mean in a neural network?" target="_blank">What does 1x1 convolution mean in a neural network?</a> </li>
<li><a href="/rltoken/rCqBgTDQkhRzYfS0N_GvZg" title="GoogLeNet Tutorial" target="_blank">GoogLeNet Tutorial</a> </li>
<li><a href="/rltoken/qDsTUcHiJn1wMK8wgA4n_Q" title="Review: GoogLeNet (Inception v1)— Winner of ILSVRC 2014 (Image Classification)" target="_blank">Review: GoogLeNet (Inception v1)— Winner of ILSVRC 2014 (Image Classification)</a> </li>
<li><a href="/rltoken/y78eU46XkU7YSWMYYB41LQ" title="Residual Neural Network" target="_blank">Residual Neural Network</a> </li>
<li><a href="/rltoken/vnYqHjVEzGTKAlhHimBrOQ" title="An Overview of ResNet and its Variants" target="_blank">An Overview of ResNet and its Variants</a> </li>
<li><a href="/rltoken/6VbH97ULfEabeoBizlqtBA" title="Review: ResNet — Winner of ILSVRC 2015 (Image Classification, Localization, Detection)" target="_blank">Review: ResNet — Winner of ILSVRC 2015 (Image Classification, Localization, Detection)</a> </li>
<li><a href="/rltoken/CYKvTKlf0VOGGXgfCgCEXQ" title="Deep Residual Learning for Image Recognition" target="_blank">Deep Residual Learning for Image Recognition</a> </li>
<li><a href="/rltoken/IXjA1KbNtghviYlMrz03ew" title="Review: ResNeXt — 1st Runner Up in ILSVRC 2016 (Image Classification)" target="_blank">Review: ResNeXt — 1st Runner Up in ILSVRC 2016 (Image Classification)</a> </li>
<li><a href="/rltoken/erexu3VwUWuUJ8doIviwxw" title="Review: DenseNet — Dense Convolutional Network (Image Classification)" target="_blank">Review: DenseNet — Dense Convolutional Network (Image Classification)</a> </li>
<li><a href="/rltoken/uOvJC3vVXrDFIba05rgYsA" title="Densely Connected Convolutional Networks" target="_blank">Densely Connected Convolutional Networks</a> </li>
<li><a href="/rltoken/Ojhi5RRK-gRiBUb8TarnhQ" title="Network In Network" target="_blank">Network In Network</a> (<em>Note: I suggest watching this video at 1.5x - 2x speed</em>)</li>
<li><a href="/rltoken/mPZn8RaZSd-mrtLFpgQxeA" title="Inception Network Motivation" target="_blank">Inception Network Motivation</a> (<em>Note: I suggest watching this video at 1.5x - 2x speed</em>)</li>
<li><a href="/rltoken/kW9ikSvwlX4SnKd2ByHsUQ" title="Inception Network" target="_blank">Inception Network</a> (<em>Note: I suggest watching this video at 1.5x - 2x speed</em>)</li>
<li><a href="/rltoken/A7I7yn7TKmjxrzFbTYzpWA" title="Resnets" target="_blank">Resnets</a> (<em>Note: I suggest watching this video at 1.5x - 2x speed</em>)</li>
<li><a href="/rltoken/dpEseLBJZ972kxgT9TjwgQ" title="Why ResNets Work" target="_blank">Why ResNets Work</a> (<em>Note: I suggest watching this video at 1.5x - 2x speed</em>)</li>
<li><a href="/rltoken/OleBG27CponGcwbW3yzCUg" title="Network in Network (2014)" target="_blank">Network in Network (2014)</a> </li>
<li><a href="/rltoken/qV99KcXnC4ubPeyJNIXJoQ" title="Going Deeper with Convolutions (2014)" target="_blank">Going Deeper with Convolutions (2014)</a> </li>
<li><a href="/rltoken/x6taRFfkp4JSEoKjz3ritA" title="Highway Networks (2015)" target="_blank">Highway Networks (2015)</a> </li>
<li><a href="/rltoken/wuLTyqZfGDJGXQr7ZD2s7A" title="Deep Residual Learning for Image Recognition (2015)" target="_blank">Deep Residual Learning for Image Recognition (2015)</a> </li>
<li><a href="/rltoken/JqUHv0O5g8hHsRdvfQh64A" title="Aggregated Residual Transformations for Deep Neural Networks (2017)" target="_blank">Aggregated Residual Transformations for Deep Neural Networks (2017)</a> </li>
<li><a href="/rltoken/Qs0mYOJOO77ZiZBEdREYzQ" title="Densely Connected Convolutional Networks (2018)" target="_blank">Densely Connected Convolutional Networks (2018)</a> </li>
<li><a href="/rltoken/FiCDt9En4pLwPNcvFRYbPQ" title="Multi-Scale Dense Networks for Resource Efficient Image Classification (2018)" target="_blank">Multi-Scale Dense Networks for Resource Efficient Image Classification (2018)</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/dVCJlCkerLRmFm2iiw3KwA" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is a skip connection?</li>
<li>What is a bottleneck layer?</li>
<li>What is the Inception Network?</li>
<li>What is ResNet? ResNeXt? DenseNet?</li>
<li>How to replicate a network architecture by reading a journal article</li>
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
