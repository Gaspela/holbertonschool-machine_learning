<h1 class="gap">0x12. Transformer Applications</h1>

<article id="description" class="gap formatted-content">
    <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/2b6bbd4de27e8b9b147fb397906ee5e822fe6fa3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210115%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20210115T165113Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=d7c234b7454add2e3c9790935d1a07eeaeecd9651efa623a210e714e9f5648d4" alt="" style=""></p>

<h2>Resources</h2>

<p><strong>Read or watch:</strong></p>

<ul>
<li><a href="/rltoken/jxxAqYmZVG_896LjsHA0SA" title="TFDS Overview" target="_blank">TFDS Overview</a></li>
<li><a href="/rltoken/3jhsMi8_VIZd2uzlyN-SaQ" title="TFDS Keras Example" target="_blank">TFDS Keras Example</a></li>
<li><a href="/rltoken/PBFAFa4q7sbMhLyrBg84Xg" title="Customizing what happens in fit" target="_blank">Customizing what happens in fit</a></li>
</ul>

<p><strong>References:</strong></p>

<ul>
<li><a href="/rltoken/_Sot-yIEG4acO7oABwji-Q" title="tfds" target="_blank">tfds</a>

<ul>
<li><a href="/rltoken/zlfIaVsEPgK3M-PFqYx8kw" title="tfds.load" target="_blank">tfds.load</a></li>
<li><a href="/rltoken/pVFn4RX89X8AK9l1CICrZw" title="tfds.features.text.SubwordTextEncoder" target="_blank">tfds.features.text.SubwordTextEncoder</a></li>
</ul></li>
<li><a href="/rltoken/C1R6GSnrg7By7F1ZozYALQ" title="tf.py_function" target="_blank">tf.py_function</a></li>
<li><a href="/rltoken/4EiwSWc51djgL5YL8CPyWw" title="tf.linalg.band_part" target="_blank">tf.linalg.band_part</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/_8t31BZ1oiscVowS0fV5xw" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>How to use Transformers for Machine Translation</li>
<li>How to write a custom train/test loop in Keras</li>
<li>How to use Tensorflow Datasets</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 16.04 LTS using <code>python3</code> (version 3.6.12)</li>
<li>Your files will be executed with <code>numpy</code> (version 1.16) and <code>tensorflow</code> (version 1.15)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>All of your files must be executable</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should follow the <code>pycodestyle</code> style (version 2.4)</li>
<li>All your modules should have documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>Unless otherwise stated, you cannot import any module except <code>import tensorflow.compat.v2 as tf</code> and <code>import tensorflow_datasets as tfds</code></li>
</ul>

<h2>TF Datasets</h2>

<p>For machine translation, we will be using the prepared <a href="/rltoken/JpNiruFnMoCN2ElftkLWUw" title="Tensorflow Datasets" target="_blank">Tensorflow Datasets</a> <a href="/rltoken/w3kBudIiwPqWRxfTEld95g" title="ted_hrlr_translate/pt_to_en" target="_blank">ted_hrlr_translate/pt_to_en</a>  for English to Portuguese translation</p>

<p>To download Tensorflow Datasets, please use:</p>

<pre><code>pip install --user tensorflow-datasets
</code></pre>

<p>To use this dataset, we will have to use the Tensorflow 2.0 compat within Tensorflow 1.15 and download the content:</p>

<pre><code>$ cat load_dataset.py
#!/usr/bin/env python3
import tensorflow.compat.v2 as tf
import tensorflow_datasets as tfds

tf.compat.v1.enable_eager_execution()
pt2en_train = tfds.load('ted_hrlr_translate/pt_to_en', split='train', as_supervised=True)
for pt, en in pt2en_train.take(1):
  print(pt.numpy().decode('utf-8'))
  print(en.numpy().decode('utf-8'))
$ ./load_dataset.py
e quando melhoramos a procura , tiramos a única vantagem da impressão , que é a serendipidade .
and when you improve searchability , you actually take away the one advantage of print , which is serendipity .
$
</code></pre>

  </article>

## Author
* **Samir millan** - [Gaspela04](https://github.com/Gaspela04)