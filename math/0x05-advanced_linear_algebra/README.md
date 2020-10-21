<h1 class="gap">0x05. Advanced Linear Algebra</h1>

<article id="description" class="gap formatted-content">
    <p><a href="https://imgbb.com/"><img src="https://i.ibb.co/Y0XMHKZ/dfef9b5a1411d49808c1.jpg" alt="dfef9b5a1411d49808c1" border="0"></a></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/F61LWMDnv216TI4VURIavQ" title="The determinant | Essence of linear algebra" target="_blank">The determinant | Essence of linear algebra</a></li>
<li><a href="/rltoken/d_uY4uoRqk7EU4Pg9qz7Ig" title="Determinant of a Matrix" target="_blank">Determinant of a Matrix</a></li>
<li><a href="/rltoken/eLZ_J1BAltkAFuNsOhutKQ" title="Determinant" target="_blank">Determinant</a></li>
<li><a href="/rltoken/5REQT4orNW4FNpoDdy0RLg" title="Determinant of an empty matrix" target="_blank">Determinant of an empty matrix</a></li>
<li><a href="/rltoken/5alpJ5Uyeb8QWaWmKeIFcA" title="Inverse matrices, column space and null space" target="_blank">Inverse matrices, column space and null space</a></li>
<li><a href="/rltoken/nAtBpV2gGB1PhMtfw8JWww" title="Inverse of a Matrix using Minors, Cofactors and Adjugate" target="_blank">Inverse of a Matrix using Minors, Cofactors and Adjugate</a></li>
<li><a href="/rltoken/IAjFHGF9pgUlajyVY0ytaA" title="Minor" target="_blank">Minor</a></li>
<li><a href="/rltoken/KykXUKmSVLjYmT7z_Nc07g" title="Cofactor" target="_blank">Cofactor</a></li>
<li><a href="/rltoken/30NiZqFhPtoe61DUmXkUCA" title="Adjugate matrix" target="_blank">Adjugate matrix</a></li>
<li><a href="/rltoken/Wdpp4xtLOgxFq5kGyBpZsw" title="Singular Matrix" target="_blank">Singular Matrix</a></li>
<li><a href="/rltoken/MRQqIv0dCyRivrpld6_5TQ" title="Elementary Matrix Operations" target="_blank">Elementary Matrix Operations</a></li>
<li><a href="/rltoken/VTo7Q09EqloHCv-q6XGw3g" title="Gaussian Elimination" target="_blank">Gaussian Elimination</a></li>
<li><a href="/rltoken/CMLsBAfm0W4uqe2r_Oezkw" title="Gauss-Jordan Elimination" target="_blank">Gauss-Jordan Elimination</a></li>
<li><a href="/rltoken/2Oz0LITPFPX9PTNn9zqrwQ" title="Matrix Inverse" target="_blank">Matrix Inverse</a></li>
<li><a href="/rltoken/E8_Gy9NO7Gjb4LxN0jUFWQ" title="Eigenvectors and eigenvalues | Essence of linear algebra" target="_blank">Eigenvectors and eigenvalues | Essence of linear algebra</a></li>
<li><a href="/rltoken/n1w31RZHRl8_tNhUY1-TRA" title="Eigenvalues and eigenvectors" target="_blank">Eigenvalues and eigenvectors</a></li>
<li><a href="/rltoken/ZSkHYcwTonsySFhCBrM8uA" title="Eigenvalues and Eigenvectors" target="_blank">Eigenvalues and Eigenvectors</a></li>
<li><a href="/rltoken/qODLYtIIrUMQLsEENialNQ" title="Definiteness of a matrix" target="_blank">Definiteness of a matrix</a> <strong>Up to Eigenvalues</strong></li>
<li><a href="/rltoken/cuiQxdTiqu_4T4k2kVVelQ" title="Definite, Semi-Definite and Indefinite Matrices" target="_blank">Definite, Semi-Definite and Indefinite Matrices</a> <strong>Ignore Hessian Matrices</strong></li>
<li><a href="/rltoken/rYtty7OT1dlzKac_-QGPhA" title="Tests for Positive Definiteness of a Matrix" target="_blank">Tests for Positive Definiteness of a Matrix</a></li>
<li><a href="/rltoken/S-Yndhr3Pr-rTmzGgiIHTQ" title="Positive Definite Matrices and Minima" target="_blank">Positive Definite Matrices and Minima</a></li>
<li><a href="/rltoken/j-ejEoIpd7Cg6SxMlChpew" title="Positive Definite Matrices" target="_blank">Positive Definite Matrices</a></li>
</ul>

<p><strong>As references</strong>:</p>

<ul>
<li><a href="/rltoken/AiJWrZH4RCkUydqzEeut-A" title="numpy.linalg.eig" target="_blank">numpy.linalg.eig</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/O3m0XVEZljm-F7oY7gwkPw" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is a determinant? How would you calculate it?</li>
<li>What is a minor, cofactor, adjugate? How would calculate them?</li>
<li>What is an inverse? How would you calculate it?</li>
<li>What are eigenvalues and eigenvectors? How would you calculate them?</li>
<li>What is definiteness of a matrix? How would you determine a matrix’s definiteness?</li>
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
<li>Unless otherwise noted, you are not allowed to import any module</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

  </article>

## Author
* **Samir millan** - [Gaspela04](https://github.com/Gaspela04)