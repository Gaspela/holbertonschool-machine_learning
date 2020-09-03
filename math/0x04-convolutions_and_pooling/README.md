<h1 class="gap">0x04. Convolutions and Pooling</h1>

<article id="description" class="gap formatted-content">
    <p><a href="https://imgbb.com/"><img src="https://i.ibb.co/JdNh2Lm/ed9ca14839ad0201f19e.gif" alt="ed9ca14839ad0201f19e" border="0"></a></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/Qeq8i5dhkR9Tlp-IgFDzQw" title="Image Kernels" target="_blank">Image Kernels</a> </li>
<li><a href="/rltoken/g8kHsJFzC51whRSEupvidw" title="Undrestanding Convolutional Layers" target="_blank">Undrestanding Convolutional Layers</a> </li>
<li><a href="/rltoken/crEEAb4sDHc30ntPwY-qsQ" title="What is max pooling in convolutional neural networks?" target="_blank">What is max pooling in convolutional neural networks?</a> </li>
<li><a href="/rltoken/nV4RcnhzFvjLfl7z2k5-Cw" title="Edge Detection Examples" target="_blank">Edge Detection Examples</a></li>
<li><a href="/rltoken/WZ_a9ntwdJ_AU51W46KOlw" title="Padding" target="_blank">Padding</a></li>
<li><a href="/rltoken/yupMT890fCjD5XVyogDkmg" title="Strided Convolutions" target="_blank">Strided Convolutions</a> </li>
<li><a href="/rltoken/vdFQg1m-0BJ_s0lg8b3fkg" title="Convolutions over Volumes" target="_blank">Convolutions over Volumes</a></li>
<li><a href="/rltoken/Z0dPond1Oi9a04MiWsbgXA" title="Pooling Layers" target="_blank">Pooling Layers</a></li>
<li><a href="/rltoken/gJgrOuiHHqu6aNVZoX7iBA" title="Implementing 'SAME' and 'VALID' padding of Tensorflow in Python" target="_blank">Implementing ‘SAME’ and ‘VALID’ padding of Tensorflow in Python</a>

<ul>
<li><strong>NOTE: In this document, there is a mistake regarding valid padding. Floor rounding should be used for valid padding instead of ceiling</strong></li>
</ul></li>
</ul>

<p><strong>Definitions to skim:</strong></p>

<ul>
<li><a href="/rltoken/xbzvTRaBX2LUOM7A1NazVQ" title="Convolution" target="_blank">Convolution</a> </li>
<li><a href="/rltoken/lsI2xbijDWAiKDFuCYkcAA" title="Kernel (image processing)" target="_blank">Kernel (image processing)</a> </li>
</ul>

<p><strong>References:</strong></p>

<ul>
<li><a href="/rltoken/QkWjIyjvPImhaA4HJGGz-w" title="numpy.pad" target="_blank">numpy.pad</a> </li>
<li><a href="/rltoken/ZJItcZYPPp4e6bAV-xaMkw" title="A guide to convolution arithmetic for deep learning" target="_blank">A guide to convolution arithmetic for deep learning</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/qTkzSfy5DRC1VkBEPRt4Ag" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is a convolution?</li>
<li>What is max pooling? average pooling?</li>
<li>What is a kernel/filter?</li>
<li>What is padding?</li>
<li>What is “same” padding? “valid” padding?</li>
<li>What is a stride?</li>
<li>What are channels?</li>
<li>How to perform a convolution over an image</li>
<li>How to perform max/average pooling over an image</li>
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
<li>Your code should use the <code>pycodestyle</code> style (version 2.5)</li>
<li>All your modules should have documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>Unless otherwise noted, you are not allowed to import any module except <code>import numpy as np</code> and <code>from math import ceil, floor</code></li>
<li>You are not allowed to use <code>np.convolve</code></li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h2>More Info</h2>

<h3>Testing</h3>

<p>Please download <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-ml/animals_1.npz" title="this dataset" target="_blank">this dataset</a> for use in some of the following main files.</p>

  </article>

