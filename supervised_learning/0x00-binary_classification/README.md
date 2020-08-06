<h1 class="gap">0x00. Binary Classification</h1>

<article id="description" class="gap formatted-content">
    <p><a href="https://ibb.co/CHYhFVy"><img src="https://i.ibb.co/LZcnf9y/83672a47323d70a88c5e.jpg" alt="83672a47323d70a88c5e" border="0"></a></p>

<h2>Background Context</h2>

<p>Welcome to your first project on supervised learning! At the end of this project, you should be able to build your own binary image classifier from scratch using <code>numpy</code>. As you might already see, there are a <strong>LOT</strong> of resources for you to read/watch. It may be tempting to dive into the projects right away, but it is <strong>HIGHLY RECOMMENDED</strong> that you spend <strong>AT LEAST</strong> 1 whole day going over the following materials. You should only start the project once you have a decent understanding of all the topics mentioned in <strong>Learning Objectives</strong>. You may also notice that there are multiple resources that cover the same topic, with some more technical than others. If you find yourself getting lost in a resource, move on to another and come back to the more technical one after you intuitively understand that topic. Good luck and have fun!</p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/16mL_gwlZqRa3NAv325YiQ" title="Supervised vs. Unsupervised Machine Learning" target="_blank">Supervised vs. Unsupervised Machine Learning</a> </li>
<li><a href="/rltoken/A1B1qLJgpKvA4RySpI6r7g" title="How would you explain neural networks to someone who knows very little about AI or neurology?" target="_blank">How would you explain neural networks to someone who knows very little about AI or neurology?</a> </li>
<li><a href="/rltoken/EjjENEVXJKiAZsqSqWMl-w" title="Using Neural Nets to Recognize Handwritten Digits" target="_blank">Using Neural Nets to Recognize Handwritten Digits</a> (<em>until “A simple network to classify handwritten digits” (excluded)</em>)</li>
<li><a href="/rltoken/da0lo6JbjEDxCbffjRHc7g" title="Forward propagation" target="_blank">Forward propagation</a> </li>
<li><a href="/rltoken/hz77ChKoiSjMFzi7mgMzBA" title="Understanding Activation Functions in Neural Networks" target="_blank">Understanding Activation Functions in Neural Networks</a></li>
<li><a href="/rltoken/KgRV0-l2LBdQciUXGIeCqQ" title="Loss function" target="_blank">Loss function</a> </li>
<li><a href="/rltoken/7iSJelYELwy7C8cCsGk5hw" title="Gradient descent" target="_blank">Gradient descent</a> </li>
<li><a href="/rltoken/BONZS65eZnIMjngFhr7dPA" title="Calculus on Computational Graphs: Backpropagation" target="_blank">Calculus on Computational Graphs: Backpropagation</a> </li>
<li><a href="/rltoken/Arpa6EFk9q5gD9aJ4Wl5qA" title="Backpropagation calculus" target="_blank">Backpropagation calculus</a> </li>
<li><a href="/rltoken/EkncpxTwCUJztJsYI0wciA" title="What is a Neural Network?" target="_blank">What is a Neural Network?</a> </li>
<li><a href="/rltoken/LoWxJZN-JA0VkV13QQrw1g" title="Supervised Learning with a Neural Network" target="_blank">Supervised Learning with a Neural Network</a> </li>
<li><a href="/rltoken/cFuQ0hUHg_SpVCHvKrXMzg" title="Binary Classification" target="_blank">Binary Classification</a> </li>
<li><a href="/rltoken/sGIlY030fFNX4nNQidq5fw" title="Logistic Regression" target="_blank">Logistic Regression</a> </li>
<li><a href="/rltoken/xZTVYTU5pSnSK3a7o3OuIQ" title="Logistic Regression Cost Function" target="_blank">Logistic Regression Cost Function</a></li>
<li><a href="/rltoken/M3YbEr_BqYcILJNz7YzLaQ" title="Gradient Descent" target="_blank">Gradient Descent</a></li>
<li><a href="/rltoken/X5CelY1ajZt3wHrjtls6Fg" title="Computation Graph" target="_blank">Computation Graph</a> </li>
<li><a href="/rltoken/HLxYo6tgVumVNRysPUxKNA" title="Logistic Regression Gradient Descent" target="_blank">Logistic Regression Gradient Descent</a> </li>
<li><a href="/rltoken/Zxdbe_-GWZRfXKfs5JM9ig" title="Vectorization" target="_blank">Vectorization</a></li>
<li><a href="/rltoken/HQ9VuO9c4XPJgIm6Nxyn5Q" title="Vectorizing Logistic Regression" target="_blank">Vectorizing Logistic Regression</a></li>
<li><a href="/rltoken/RaswXJ2G9LHswV0CypjA0A" title="Vectorizing Logistic Regression's Gradient Computation" target="_blank">Vectorizing Logistic Regression’s Gradient Computation</a> </li>
<li><a href="/rltoken/wKRb7J-yeA92EF5aEJd3oA" title="A Note on Python/Numpy Vectors" target="_blank">A Note on Python/Numpy Vectors</a> </li>
<li><a href="/rltoken/JyhRr98YlhACYERu0GncNQ" title="Neural Network Representations" target="_blank">Neural Network Representations</a> </li>
<li><a href="/rltoken/Lpcj3uH_6hh8Fp1dXzKkCw" title="Computing Neural Network Output" target="_blank">Computing Neural Network Output</a> </li>
<li><a href="/rltoken/uWY4JFKkT58mrHSBig_f5A" title="Vectorizing Across Multiple Examples" target="_blank">Vectorizing Across Multiple Examples</a> </li>
<li><a href="/rltoken/Q583jTfE8BfU5hPW1xlDiQ" title="Gradient Descent For Neural Networks" target="_blank">Gradient Descent For Neural Networks</a> </li>
<li><a href="/rltoken/2uZWU7WaWSQfwGNKlcgZig" title="Random Initialization" target="_blank">Random Initialization</a> </li>
<li><a href="/rltoken/iMyExMqGZGcawyK51FcdzQ" title="Deep L-Layer Neural Network" target="_blank">Deep L-Layer Neural Network</a> </li>
<li><a href="/rltoken/varxWT03Dy39WlyrZBGAVQ" title="Train/Dev/Test Sets" target="_blank">Train/Dev/Test Sets</a> </li>
<li><a href="/rltoken/Lw4QRvFzjkICRmzyl1-8-Q" title="Random Initialization For Neural Networks : A Thing Of The Past" target="_blank">Random Initialization For Neural Networks : A Thing Of The Past</a> </li>
<li><a href="/rltoken/ymVrn0IFwxnzoo3WwEZzcQ" title="Initialization of deep networks" target="_blank">Initialization of deep networks</a> </li>
<li><a href="/rltoken/Ho3q2XEingriAApbvjTy6w" title="numpy.zeros" target="_blank">numpy.zeros</a> </li>
<li><a href="/rltoken/JFRl_j_ebMhXasgQ_geUug" title="numpy.random.randn" target="_blank">numpy.random.randn</a> </li>
<li><a href="/rltoken/AjRCO7Yh0JW4lC0xuGmbOg" title="numpy.exp" target="_blank">numpy.exp</a> </li>
<li><a href="/rltoken/AtD0YS-8Q3Oc0TN1MQ6Wuw" title="numpy.log" target="_blank">numpy.log</a> </li>
<li><a href="/rltoken/Xb26cP7K6Bqtoc_NhQXosg" title="numpy.sqrt" target="_blank">numpy.sqrt</a> </li>
<li><a href="/rltoken/6owcKbc6MWk7JlnlM0AaWA" title="numpy.where" target="_blank">numpy.where</a> </li>
</ul>

<p><strong>Optional</strong>:</p>

<ul>
<li><a href="/rltoken/Bp_21TFndH5cSWLBObZuzQ" title="Predictive analytics" target="_blank">Predictive analytics</a> </li>
<li><a href="/rltoken/XKoD7TJFrpjB9xjY8L1t-w" title="Maximum Likelihood Estimation" target="_blank">Maximum Likelihood Estimation</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/yKtIe6fSEklenpymZ18Xrw" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is a model?</li>
<li>What is supervised learning?</li>
<li>What is a prediction?</li>
<li>What is a node?</li>
<li>What is a weight?</li>
<li>What is a bias?</li>
<li>What are activation functions?

<ul>
<li>Sigmoid?</li>
<li>Tanh?</li>
<li>Relu?</li>
<li>Softmax?</li>
</ul></li>
<li>What is a layer?</li>
<li>What is a hidden layer?</li>
<li>What is Logistic Regression?</li>
<li>What is a loss function?</li>
<li>What is a cost function?</li>
<li>What is forward propagation?</li>
<li>What is Gradient Descent?</li>
<li>What is back propagation?</li>
<li>What is a Computation Graph?</li>
<li>How to initialize weights/biases</li>
<li>The importance of vectorization</li>
<li>How to split up your data</li>
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
<li>Unless otherwise noted, you are not allowed to import any module except <code>import numpy as np</code></li>
<li>Unless otherwise noted, you are not allowed to use any loops (<code>for</code>, <code>while</code>, etc.)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h2>More Info</h2>

<h3>Matrix Multiplications</h3>

<p>For all matrix multiplications in the following tasks, please use <a href="/rltoken/Ox8bY8ogmUftzjR96IrMDw" title="numpy.matmul" target="_blank">numpy.matmul</a></p>

<h3>Testing your code</h3>

<p>In order to test your code, you’ll need DATA! Please download these datasets (<a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-ml/Binary_Train.npz" title="Binary_Train.npz" target="_blank">Binary_Train.npz</a>, <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-ml/Binary_Dev.npz" title="Binary_Dev.npz" target="_blank">Binary_Dev.npz</a>) to go along with all of the following main files. You <strong>do not</strong> need to upload these files to GitHub. Your code will not necessarily be tested with these datasets. All of the following code assumes that you have stored all of your datasets in a separate <code>data</code> directory.</p>

<pre><code>alexa@ubuntu-xenial:0x00-binary_classification$ cat show_data.py
#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

lib_train = np.load('../data/Binary_Train.npz')
X_3D, Y = lib_train['X'], lib_train['Y']

fig = plt.figure(figsize=(10, 10))
for i in range(100):
    fig.add_subplot(10, 10, i + 1)
    plt.imshow(X_3D[i])
    plt.title(Y[0, i])
    plt.axis('off')
plt.tight_layout()
plt.show()
alexa@ubuntu-xenial:0x00-binary_classification$ ./show_data.py
</code></pre>

<p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/10/9bf500103f10b830474e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20200806%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20200806T141630Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=c2627571e3072ad74ce319812532aad715271cf1bb5f5d5bdc69f2267f042781" alt="" style=""></p>

  </article>
