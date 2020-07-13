<h1 class="gap">0x00. Linear Algebra</h1>

<article id="description" class="gap formatted-content">
    <p><a href="https://imgbb.com/"><img src="https://i.ibb.co/wrJtGdY/54daaf81421a9b894688.jpg" alt="54daaf81421a9b894688" border="0"></a></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/C05mTOfKzZgz_AVSosNKIw" title="Introduction to vectors" target="_blank">Introduction to vectors</a> </li>
<li><a href="/rltoken/vLe4BBPfmLXy2s_Idqo87w" title="What is a matrix?" target="_blank">What is a matrix?</a> (<em>not <a href="/rltoken/Zad2ReJ9SU4IuQ3ZX986qw" title="the matrix" target="_blank">the matrix</a></em>)</li>
<li><a href="/rltoken/xHWwQjqH9tgEcskvFQaV7A" title="Transpose" target="_blank">Transpose</a> </li>
<li><a href="/rltoken/2tYcOFY35stXjd0nhTpgFA" title="Understanding the dot product" target="_blank">Understanding the dot product</a> </li>
<li><a href="/rltoken/pV4znghCxaXAAny4Ou-cNw" title="Matrix Multiplication" target="_blank">Matrix Multiplication</a> </li>
<li><a href="/rltoken/ih50DhE4FvilyItYPo1x5A" title="What is the relationship between matrix multiplication and the dot product?" target="_blank">What is the relationship between matrix multiplication and the dot product?</a> </li>
<li><a href="/rltoken/DnAvjbmojZutluWV9OJVOg" title="The Dot Product, Matrix Multiplication, and the Magic of Orthogonal Matrices" target="_blank">The Dot Product, Matrix Multiplication, and the Magic of Orthogonal Matrices</a> (<em>advanced</em>)</li>
<li><a href="/rltoken/MBHHb0eiN0OummbEdI9g_Q" title="numpy tutorial" target="_blank">numpy tutorial</a> (<em>until Shape Manipulation (excluded)</em>)</li>
<li><a href="/rltoken/L8RdIDGi3GGO-_erGcMORg" title="numpy basics" target="_blank">numpy basics</a> (<em>until Universal Functions (included)</em>)</li>
<li><a href="/rltoken/aP6pS5OhR5TLg9ZB9AkSiw" title="array indexing" target="_blank">array indexing</a> </li>
<li><a href="/rltoken/slRzAgt6aom5-Nj5XSdUcQ" title="numerical operations on arrays" target="_blank">numerical operations on arrays</a> </li>
<li><a href="/rltoken/xgq6QIOHufhg8lHCZn0jwA" title="Broadcasting" target="_blank">Broadcasting</a> </li>
<li><a href="/rltoken/Ns14y44s9aapxgagPJYGWQ" title="numpy mutations and broadcasting" target="_blank">numpy mutations and broadcasting</a> </li>
<li><a href="/rltoken/QwlSVWZcJNeGHmgPJMNtHg" title="numpy.ndarray" target="_blank">numpy.ndarray</a> </li>
<li><a href="/rltoken/wBmTVyayvO4hHbyT6wpt0g" title="numpy.ndarray.shape" target="_blank">numpy.ndarray.shape</a> </li>
<li><a href="/rltoken/I1V8iDWar7Hnoh_VwQzZ_Q" title="numpy.transpose" target="_blank">numpy.transpose</a> </li>
<li><a href="/rltoken/iv73fN04gTbpeV_XcIIaPQ" title="numpy.ndarray.transpose" target="_blank">numpy.ndarray.transpose</a> </li>
<li><a href="/rltoken/MbHJEqjwavimnL8HRtaYCA" title="numpy.matmul" target="_blank">numpy.matmul</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/HK6YZ7VcaX6RKNRxQLfCuA" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is a vector? </li>
<li>What is a matrix?</li>
<li>What is a transpose?</li>
<li>What is the shape of a matrix?</li>
<li>What is an axis?</li>
<li>What is a slice?</li>
<li>How do you slice a vector/matrix?</li>
<li>What are element-wise operations?</li>
<li>How do you concatenate vectors/matrices?</li>
<li>What is the dot product?</li>
<li>What is matrix multiplication?</li>
<li>What is <code>Numpy</code>?</li>
<li>What is parallelization and why is it important?</li>
<li>What is broadcasting?</li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 16.04 LTS using <code>python3</code> (version 3.5)</li>
<li>Your files will be executed with <code>numpy</code> (version 1.15)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should follow <code>pycodestyle</code> (version 2.5)</li>
<li>All your modules should have documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li><strong>Unless otherwise noted, you are not allowed to import any module</strong></li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h2>More Info</h2>

<h3>Installing Ubuntu 16.04 and Python 3.5</h3>

<p>Follow the instructions listed in <a href="/rltoken/XTxOgs8R1UADvjdxl5daXA" title="Using Vagrant on your personal computer" target="_blank">Using Vagrant on your personal computer</a>, with the caveat that you should be using <code>ubuntu/xenial64</code> instead of <code>ubuntu/trusty64</code>.</p>

<p><em>Python 3.5 comes pre-installed on Ubuntu 16.04. How convenient! You can confirm this with</em> <code>python3 -V</code></p>

<h3>Installing pip 19.1</h3>

<pre><code>wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
rm get-pip.py
</code></pre>

<p>To check that pip has been successfully downloaded, use <code>pip -V</code>. Your output should look like:</p>

<pre><code>$ pip -V
pip 19.1.1 from /usr/local/lib/python3.5/dist-packages/pip (python 3.5)
</code></pre>

<h3>Installing numpy 1.15,  scipy 1.3, and pycodestyle 2.5</h3>

<pre><code>$ pip install --user numpy==1.15
$ pip install --user scipy==1.3
$ pip install --user pycodestyle==2.5
</code></pre>

<p>To check that all have been successfully downloaded, use <code>pip list</code>.</p>

  </article>

## Author
* **Samir millan** - [Gaspela04](https://github.com/Gaspela04)
