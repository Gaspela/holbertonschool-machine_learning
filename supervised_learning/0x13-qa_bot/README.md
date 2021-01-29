<h1 class="gap">0x13. QA Bot</h1>

<article id="description" class="gap formatted-content">
    <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/11/52f1c0b37c7c58d30706b7e24bb7534b5a5889db.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210129%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20210129T160553Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=accc853a50bc6cac31c3dcdf53d468878617aba85c852701782cd128098b9c32" alt="" style=""></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>: </p>

<ul>
<li><a href="/rltoken/isif62esIXAxfKrVWRFUvA" title="Improving Language Understanding by Generative Pre-Training (2018)" target="_blank">Improving Language Understanding by Generative Pre-Training (2018)</a></li>
<li><a href="/rltoken/tFF7DtiDKAHOB_AnliLQ-w" title="BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (2018)" target="_blank">BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (2018)</a></li>
<li><a href="/rltoken/TWw2zYrbEv1A6Xp7Q5xeIg" title="SQuAD 2.0" target="_blank">SQuAD 2.0</a></li>
<li><a href="/rltoken/JDS8l-V-AyRMgZ-VWCR4mg" title="Know What You Don’t Know: Unanswerable Questions for SQuAD (2018)" target="_blank">Know What You Don’t Know: Unanswerable Questions for SQuAD (2018)</a></li>
<li><a href="/rltoken/G5RYcXocPNTEGSeiWFfT9Q" title="GLUE Benchmark" target="_blank">GLUE Benchmark</a></li>
<li><a href="/rltoken/58OooeuXuihK66vnEQL5og" title="GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding (2019)" target="_blank">GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding (2019)</a></li>
<li><a href="/rltoken/t0l-uUrcWnFizy9y6ySnOg" title="Speech-transformer: A no-recurrence sequence-to-sequence model for speech recognition (2018)" target="_blank">Speech-transformer: A no-recurrence sequence-to-sequence model for speech recognition (2018)</a></li>
</ul>

<p><strong>More recent papers in NLP:</strong></p>

<ul>
<li><a href="/rltoken/fLho-pVtLacRpYcoeKQlbw" title="Generating Long Sequences with Sparse Transformers (2019)" target="_blank">Generating Long Sequences with Sparse Transformers (2019)</a></li>
<li><a href="/rltoken/DNjHiFbB_cOVhIB7usnx8A" title="Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context (2019)" target="_blank">Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context (2019)</a></li>
<li><a href="/rltoken/fr6iKOeQ2J2I3m-2mnVk5w" title="XLNet: Generalized Autoregressive Pretraining for Language Understanding (2019)" target="_blank">XLNet: Generalized Autoregressive Pretraining for Language Understanding (2019)</a></li>
<li><a href="/rltoken/4eTrqxWdepAKneRJsjaD8g" title="Language Models are Unsupervised Multitask Learners (GPT-2, 2019)" target="_blank">Language Models are Unsupervised Multitask Learners (GPT-2, 2019)</a></li>
<li><a href="/rltoken/-LbOp0yRvuSn1Hqzd2OF2Q" title="Language Models are Few-Shot Learners (GPT-3, 2020)" target="_blank">Language Models are Few-Shot Learners (GPT-3, 2020)</a></li>
<li><a href="/rltoken/s4A59Pf2b2QjWT8NjgWB8g" title="ALBERT: A Lite BERT for Self-Supervised Learning of Language Representations (2020)" target="_blank">ALBERT: A Lite BERT for Self-Supervised Learning of Language Representations (2020)</a></li>
</ul>

<p>To keep up with the newest papers and their code bases go to <a href="/rltoken/Glv09z1yOkMl0Gsl0zBHjg" title="paperswithcode.com" target="_blank">paperswithcode.com</a>. For example, check out the <a href="/rltoken/DZKmWejiXC0czbR9j32N_g" title="raked list of state of the art models for Language Modelling on Penn Treebank" target="_blank">raked list of state of the art models for Language Modelling on Penn Treebank</a>.</p>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/gQzVqyxWWUByblpobq6iTA" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is Question-Answering?</li>
<li>What is Semantic Search?</li>
<li>What is BERT?</li>
<li>How to develop a QA chatbot</li>
<li>How to use the <code>transformers</code> library</li>
<li>How to use the <code>tensorflow-hub</code> library</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 16.04 LTS using <code>python3</code> (version 3.6.12)</li>
<li>Your files will be executed with <code>numpy</code> (version 1.18) and <code>tensorflow</code> (version 2.3)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>All of your files must be executable</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should follow the <code>pycodestyle</code> style (version 2.4)</li>
<li>All your modules should have documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
</ul>

<h2>Upgrade to Tensorflow 2.3</h2>

<p><code>pip install --user tensorflow==2.3</code></p>

<h2>Install Tensorflow Hub</h2>

<p><code>pip install --user tensorflow-hub</code></p>

<h2>Install Transformers</h2>

<p><code>pip install --user transformers</code></p>

<h2>Zendesk Articles</h2>

<p>For this project, we will be using a collection of Holberton USA Zendesk Articles, <a href="/rltoken/ujQQ_o24BufzUPyWrR7IGA" title="ZendeskArticles.zip" target="_blank">ZendeskArticles.zip</a>.</p>

  </article>

## Author
* **Samir millan** - [Gaspela04](https://github.com/Gaspela04)
