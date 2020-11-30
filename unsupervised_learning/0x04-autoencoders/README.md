<h1 class="gap">0x04. Autoencoders</h1>

<article id="description" class="gap formatted-content">
    <p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/WMbe5eWUHhyFet68Kf9pwQ" title="Autoencoder - definition" target="_blank">Autoencoder - definition</a></li>
<li><a href="/rltoken/9c-itgW_s8KR3osdRmmnKw" title="Autoencoder - loss function" target="_blank">Autoencoder - loss function</a></li>
<li><a href="/rltoken/3hm5-oOrajXejrCH4P1-Mg" title="Deep learning - deep autoencoder" target="_blank">Deep learning - deep autoencoder</a></li>
<li><a href="/rltoken/qoMN_ZeSetmF92dXhinEAA" title="Introduction to autoencoders" target="_blank">Introduction to autoencoders</a></li>
<li><a href="/rltoken/6TUoTdWuAyB4SGEw5Jf-Cg" title="Variational Autoencoders - EXPLAINED!" target="_blank">Variational Autoencoders - EXPLAINED!</a> <em>up to</em> <strong>12:55</strong></li>
<li><a href="/rltoken/VV_w6WaFyY8e0jF5qXmy4g" title="Variational Autoencoders" target="_blank">Variational Autoencoders</a></li>
<li><a href="/rltoken/_oLm95ldasv-53oQsJdw-A" title="Intuitively Understanding Variational Autoencoders" target="_blank">Intuitively Understanding Variational Autoencoders</a></li>
<li><a href="/rltoken/YBRNT168BX-HdinAUZCV3g" title="Deep Generative Models" target="_blank">Deep Generative Models</a> <em>up to</em> <strong>Generative Adversarial Networks</strong></li>
</ul>

<p><strong>Definitions to skim</strong>:</p>

<ul>
<li><a href="/rltoken/M0-vm4JIoP-Msl5SemHDDA" title="Kullback–Leibler divergence" target="_blank">Kullback–Leibler divergence</a> <em>recall its use in t-SNE</em></li>
<li><a href="/rltoken/kgDcseTs0_TQ5X7nPs7EeQ" title="Autoencoder" target="_blank">Autoencoder</a></li>
<li><a href="/rltoken/oICoCfZORJNQFwcpR-Kq1w" title="Generative model" target="_blank">Generative model</a></li>
</ul>

<p><strong>References</strong>:</p>

<ul>
<li><a href="/rltoken/lAQEyGkZx9q4vnXTD8noxQ" title="The Deep Learning textbook - Chapter 14: Autoencoders" target="_blank">The Deep Learning textbook - Chapter 14: Autoencoders</a></li>
<li><a href="/rltoken/EsJJMSqKlVcbBvjLEMhutQ" title="Reducing the Dimensionality of Data with Neural Networks 2006" target="_blank">Reducing the Dimensionality of Data with Neural Networks 2006</a></li>
</ul>

<h2>Learning Objectives</h2>

<ul>
<li>What is an autoencoder?</li>
<li>What is latent space?</li>
<li>What is a bottleneck?</li>
<li>What is a sparse autoencoder?</li>
<li>What is a convolutional autoencoder?</li>
<li>What is a generative model?</li>
<li>What is a variational autoencoder?</li>
<li>What is the Kullback-Leibler divergence?</li>
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
<li>Unless otherwise noted, you are not allowed to import any module except <code>import tensorflow.keras as keras</code></li>
<li>All your files must be executable</li>
</ul>

  </article>

## Author
* **Samir millan** - [Gaspela04](https://github.com/Gaspela04)

