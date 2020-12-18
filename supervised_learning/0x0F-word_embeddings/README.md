<h1 class="gap">0x0F. Natural Language Processing - Word Embeddings</h1>

<article id="description" class="gap formatted-content">
    <p><a href="https://ibb.co/g9DY4v3"><img src="https://i.ibb.co/QQ60D8f/a2fa719214e8c81107842b9fcd97defd08ba3d82.png" alt="a2fa719214e8c81107842b9fcd97defd08ba3d82" border="0"></a></p>

<h2>Resources</h2>

<p><strong>Read or watch:</strong></p>

<ul>
<li><a href="/rltoken/-a-kPuLr3JNsmoBdj0Fnxg" title="An Introduction to Word Embeddings" target="_blank">An Introduction to Word Embeddings</a></li>
<li><a href="/rltoken/XcXiOu4G1cQmPsMCSV6iKg" title="Introduction to Word Embeddings" target="_blank">Introduction to Word Embeddings</a></li>
<li><a href="/rltoken/MFWRUck_pP6wWTo-Hk-uNA" title="Natural Language Processing|Bag Of Words Intuition" target="_blank">Natural Language Processing|Bag Of Words Intuition</a></li>
<li><a href="/rltoken/wNtfvYw0_t9__T34QullnQ" title="Natural Language Processing|TF-IDF Intuition| Text Prerocessing" target="_blank">Natural Language Processing|TF-IDF Intuition| Text Prerocessing</a></li>
<li><a href="/rltoken/EDAtqjDC2WJsCmc9DJHBsA" title="Word Embedding - Natural Language Processing| Deep Learning" target="_blank">Word Embedding - Natural Language Processing| Deep Learning</a></li>
<li><a href="/rltoken/e2onm8dzf3tnjAzhbqmY7w" title="Word2Vec Tutorial - The Skip-Gram Model" target="_blank">Word2Vec Tutorial - The Skip-Gram Model</a></li>
<li><a href="/rltoken/Oor3scClDEHAjTzs2UcLDg" title="Word2Vec Tutorial Part 2 - Negative Sampling" target="_blank">Word2Vec Tutorial Part 2 - Negative Sampling</a></li>
<li><a href="/rltoken/H8pvG3dA8erkvprE4w_cew" title="GloVe Explained" target="_blank">GloVe Explained</a></li>
<li><a href="/rltoken/4ESL4A9lp7IjiiWXeMT8Gg" title="FastText: Under the Hood" target="_blank">FastText: Under the Hood</a></li>
<li><a href="/rltoken/AgbAR_i53dGSLWFwcdJaBQ" title="ELMo Explained" target="_blank">ELMo Explained</a></li>
</ul>

<p><strong>Definitions to skim</strong></p>

<ul>
<li><a href="/rltoken/NLdhMq0eP7RCBdgTC2xXng" title="Natural Language Processing" target="_blank">Natural Language Processing</a></li>
</ul>

<p><strong>References:</strong></p>

<ul>
<li><a href="/rltoken/o6Kw0bZixZlCgSp8kv_d_A" title="Efficient Estimation of Word Representations in Vector Space (Skip-gram, 2013)" target="_blank">Efficient Estimation of Word Representations in Vector Space (Skip-gram, 2013)</a></li>
<li><a href="/rltoken/ibPaFuTAg_iFEUnXw6fi9g" title="Distributed Representations of Words and Phrases and their Compositionality (Word2Vec, 2013)" target="_blank">Distributed Representations of Words and Phrases and their Compositionality (Word2Vec, 2013)</a></li>
<li><a href="/rltoken/r_s4n4jWmHnUKnzd35_ayA" title="GloVe: Global Vectors for Word Representation (website)" target="_blank">GloVe: Global Vectors for Word Representation (website)</a></li>
<li><a href="/rltoken/m3mB2j5a1DLVtZs2yvjn9A" title="GloVe: Global Vectors for Word Representation (2014)" target="_blank">GloVe: Global Vectors for Word Representation (2014)</a></li>
<li><a href="/rltoken/XMu3K4vgAU3gXwdWbMYA7w" title="fastText (website)" target="_blank">fastText (website)</a></li>
<li><a href="/rltoken/gK1mwr5kB-fJL3aFab1lHQ" title="Bag of Tricks for Efficient Text Classification (fastText, 2016)" target="_blank">Bag of Tricks for Efficient Text Classification (fastText, 2016)</a></li>
<li><a href="/rltoken/QgTup8akJ4AXifvCTrNcYw" title="Enriching Word Vectors with Subword Information (fastText, 2017)" target="_blank">Enriching Word Vectors with Subword Information (fastText, 2017)</a></li>
<li><a href="/rltoken/0mqEv_KsCH8LRGIa1YpaiQ" title="Probabilistic FastText for Multi-Sense Word Embeddings (2018)" target="_blank">Probabilistic FastText for Multi-Sense Word Embeddings (2018)</a></li>
<li><a href="/rltoken/jAs-99Y2LO5u0ciCKLKOxw" title="ELMo (website)" target="_blank">ELMo (website)</a></li>
<li><a href="/rltoken/Waz8-ebrM2X8VNlmuVK3EQ" title="Deep contextualized word representations (ELMo, 2018)" target="_blank">Deep contextualized word representations (ELMo, 2018)</a></li>
<li><a href="/rltoken/KWBPHJxFppnvEBAdAqyoOQ" title="sklearn.feature_extraction.text.CountVectorizer" target="_blank">sklearn.feature_extraction.text.CountVectorizer</a></li>
<li><a href="/rltoken/L1tR8a5IxijX0iPSF9Zgdg" title="sklearn.feature_extraction.text.TfidfVectorizer" target="_blank">sklearn.feature_extraction.text.TfidfVectorizer</a></li>
<li><a href="/rltoken/-x-mXaagTBNvEUDbd1D84Q" title="genism.models.word2vec" target="_blank">genism.models.word2vec</a></li>
<li><a href="/rltoken/KvUoA9pXEKUOBaXb8Azd2g" title="genism.models.fasttext" target="_blank">genism.models.fasttext</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/tXju-4X_Z5aAxG7ROdFlvQ" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is natural language processing?</li>
<li>What is a word embedding?</li>
<li>What is bag of words?</li>
<li>What is TF-IDF?</li>
<li>What is CBOW?</li>
<li>What is a skip-gram?</li>
<li>What is an n-gram?</li>
<li>What is negative sampling?</li>
<li>What is word2vec, GloVe, fastText, ELMo?</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 16.04 LTS using <code>python3</code> (version 3.5)</li>
<li>Your files will be executed with <code>numpy</code> (version 1.15) and <code>tensorflow</code> (version 1.12)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>All of your files must be executable</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should follow the <code>pycodestyle</code> style (version 2.4)</li>
<li>All your modules should have documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
</ul>

<h2>Download Gensim 3.8.x</h2>

<pre><code>pip install --user gensim==3.8
</code></pre>

<h2>Download Keras 2.2.5</h2>

<pre><code>pip install --user keras==2.2.5
</code></pre>

  </article>

## Author
* **Samir millan** - [Gaspela04](https://github.com/Gaspela04)
