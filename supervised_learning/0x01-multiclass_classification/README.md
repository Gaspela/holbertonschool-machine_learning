<h1 class="gap">0x01. Multiclass Classification</h1>

<article id="description" class="gap formatted-content">
    <p><a href="https://ibb.co/4s624Bg"><img src="https://i.ibb.co/LQLr94h/e536dd3962cc3767ee0a.jpg" alt="e536dd3962cc3767ee0a" border="0"></a></p>

<h2>Readme</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/Nc2jgG8os13kpadHOq4utg" title="Multiclass classification" target="_blank">Multiclass classification</a> </li>
<li><a href="/rltoken/krZzggd-4r5fsm7J9HNYPQ" title="Derivation: Derivatives for Common Neural Network Activation Functions" target="_blank">Derivation: Derivatives for Common Neural Network Activation Functions</a> </li>
<li><a href="/rltoken/2d2caYmx9ulpY1F5BQjFCw" title="What is One Hot Encoding? Why And When do you have to use it?" target="_blank">What is One Hot Encoding? Why And When do you have to use it?</a> </li>
<li><a href="/rltoken/qo1iqiNRmbJ6TT735yDi2w" title="Softmax function" target="_blank">Softmax function</a> </li>
<li><a href="/rltoken/R6SOD-SEQ5CEVwZt8BE7RQ" title="What is the intuition behind SoftMax function?" target="_blank">What is the intuition behind SoftMax function?</a> </li>
<li><a href="/rltoken/aAydHAsto3SH9fVuoxoPyg" title="Cross entropy" target="_blank">Cross entropy</a> </li>
<li><a href="/rltoken/eFtqFGQb9i87VYuVXTcSaw" title="Loss Functions: Cross-Entropy" target="_blank">Loss Functions: Cross-Entropy</a> </li>
<li><a href="/rltoken/Tb1OUtLpFJbpRwjkcg_3mQ" title="Softmax Regression" target="_blank">Softmax Regression</a> (<em>Note: I suggest watching this video at 1.5x - 2x speed</em>)</li>
<li><a href="/rltoken/elYQKuvvcOQD1m0uRzLe3w" title="Training Softmax Classifier" target="_blank">Training Softmax Classifier</a> (<em>Note: I suggest watching this video at 1.5x - 2x speed</em>)</li>
<li><a href="/rltoken/V0n0v0Bf3JWXL0HvNOfDYQ" title="What is Pickle in python?" target="_blank">What is Pickle in python?</a> </li>
<li><a href="/rltoken/dIIiln-0zMvyNU8_X2489w" title="numpy.max" target="_blank">numpy.max</a> </li>
<li><a href="/rltoken/TxReKsm8qpXy0bUkCsNcrA" title="numpy.sum" target="_blank">numpy.sum</a> </li>
<li><a href="/rltoken/khzCPahSnOFmLz9ZKmqspQ" title="numpy.argmax" target="_blank">numpy.argmax</a> </li>
<li><a href="/rltoken/mBhamUwokBCNKc8Do7WGUQ" title="pickle" target="_blank">pickle</a> </li>
<li><a href="/rltoken/BXVRHw3G2bWdh9XTxreVIA" title="pickle.dump" target="_blank">pickle.dump</a> </li>
<li><a href="/rltoken/Ifm1r_Chh1s68guu-EI8ww" title="pickle.load" target="_blank">pickle.load</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/1hitJEaZpuNwMr_-9myzSA" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is multiclass classification?</li>
<li>What is a one-hot vector?</li>
<li>How to encode/decode one-hot vectors</li>
<li>What is the softmax function and when do you use it?</li>
<li>What is cross-entropy loss?</li>
<li>What is pickling in Python?</li>
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
<li>Your code should use the <code>pycodestyle</code> style (version 2.4)</li>
<li>All your modules should have documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h2>More Info</h2>

<h3>Testing your code</h3>

<p>In order to test your code, you’ll need DATA! Please download <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-ml/MNIST.npz" title="this dataset" target="_blank">this dataset</a> to go along with all of the following main files. You <strong>do not</strong> need to upload this file to GitHub. Your code will not necessarily be tested with this dataset.</p>

<pre><code>alexa@ubuntu-xenial:0x01-multiclass_classification$ cat show_data.py
#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

lib = np.load('../data/MNIST.npz')
print(lib.files)
X_train_3D = lib['X_train']
Y_train = lib['Y_train']

fig = plt.figure(figsize=(10, 10))
for i in range(100):
    fig.add_subplot(10, 10, i + 1)
    plt.imshow(X_train_3D[i])
    plt.title(str(Y_train[i]))
    plt.axis('off')
plt.tight_layout()
plt.show()
alexa@ubuntu-xenial:0x01-multiclass_classification$ ./show_data.py
['Y_test', 'X_test', 'X_train', 'Y_train', 'X_valid', 'Y_valid']
</code></pre>

<p><a href="https://ibb.co/ygpDD04"><img src="https://i.ibb.co/442ccW1/c713f61a7e8fe61e1442.png" alt="c713f61a7e8fe61e1442" border="0"></a></p>

  </article>

## Author
* **Samir millan** - [Gaspela04](https://github.com/Gaspela04)
