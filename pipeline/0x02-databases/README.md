<h1 class="gap">0x02. Databases</h1>

<div class="gap" id="project-description">
  <p><a href="https://ibb.co/qxgnpyH"><img src="https://i.ibb.co/M91h72z/9649007e163d3f014a46.jpg" alt="9649007e163d3f014a46" border="0"></a></p>

<p>After fetching data via APIs, storing them is also really important for training a Machine Learning model.</p>

<p>You have multiple option: </p>

<ul>
<li>Relation database</li>
<li>Not Relation database</li>
<li>Key-Value storage</li>
<li>Document storage</li>
<li>Data Lake</li>
<li>etc.</li>
</ul>

<p>In this project, you will touch the first 2: relation and not relation database.</p>

<p>Relation databases are mainly used for application, not for source of data for training your ML models, but it can be really useful for the data processing, labeling and injection in another data storage. In this project, you will play with basic SQL commands but also create automation and computing on your data directly in SQL - less load at your application level since the computing power is dispatched to the database.</p>

<p>Not relation databases, known as NoSQL, will give you flexibility on your data: document, versioning, not a fix schema, no validation to improve performance, complex lookup, etc.</p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li>MySQL:

<ul>
<li><a href="/rltoken/4iEQPoYZrI0gwzf8Oh9xrQ" title="What is Database &amp; SQL?" target="_blank">What is Database &amp; SQL?</a> </li>
<li><a href="/rltoken/H8uUw93po3lj8SYPEDupSg" title="MySQL Cheat Sheet" target="_blank">MySQL Cheat Sheet</a> </li>
<li><a href="/rltoken/UP6ueU3eUTEj0U0xU-9pBA" title="MySQL 5.7 SQL Statement Syntax" target="_blank">MySQL 5.7 SQL Statement Syntax</a> </li>
<li><a href="/rltoken/6UgmWa0wvDAC11VKBTDHfQ" title="MySQL Performance: How To Leverage MySQL Database Indexing" target="_blank">MySQL Performance: How To Leverage MySQL Database Indexing</a></li>
<li><a href="/rltoken/CWCXdKG0Rv9oeyRZPfL-4g" title="Stored Procedure" target="_blank">Stored Procedure</a></li>
<li><a href="/rltoken/bPZ-uwznI-ynPg_wVkg9RA" title="Triggers" target="_blank">Triggers</a></li>
<li><a href="/rltoken/moa3QlE8qKR1x-cfQo786A" title="Views" target="_blank">Views</a></li>
<li><a href="/rltoken/oy1_ueDdXR2FdI1pb_G0JQ" title="Functions and Operators" target="_blank">Functions and Operators</a></li>
<li><a href="/rltoken/J9R8qLW8CAAjCSTz9R9yTw" title="Trigger Syntax and Examples" target="_blank">Trigger Syntax and Examples</a></li>
<li><a href="/rltoken/2EsRzUQc_SYEezEKrknRlA" title="CREATE TABLE Statement" target="_blank">CREATE TABLE Statement</a></li>
<li><a href="/rltoken/QALbcWcfMrfyifFXdWFcZQ" title="CREATE PROCEDURE and CREATE FUNCTION Statements" target="_blank">CREATE PROCEDURE and CREATE FUNCTION Statements</a></li>
<li><a href="/rltoken/G5iUoR6uBpLXNAlH2bAjSw" title="CREATE INDEX Statement" target="_blank">CREATE INDEX Statement</a></li>
<li><a href="/rltoken/WIOV_d5KAXYBssFzN3rXng" title="CREATE VIEW Statement" target="_blank">CREATE VIEW Statement</a></li>
</ul></li>
<li>NoSQL:

<ul>
<li><a href="/rltoken/JtrFE1Dfpn12iuv0ieLkzQ" title="NoSQL Databases Explained" target="_blank">NoSQL Databases Explained</a> </li>
<li><a href="/rltoken/LAfX9ZUu763LFZAwb8gcAw" title="What is NoSQL ?" target="_blank">What is NoSQL ?</a> </li>
<li><a href="/rltoken/OsYxp_-MEzj7RWd3zEW48w" title="Building Your First Application: An Introduction to MongoDB" target="_blank">Building Your First Application: An Introduction to MongoDB</a> </li>
<li><a href="/rltoken/O_AwY40S_lzoAXrPbqeQCA" title="MongoDB Tutorial 2 : Insert, Update, Remove, Query" target="_blank">MongoDB Tutorial 2 : Insert, Update, Remove, Query</a> </li>
<li><a href="/rltoken/NtR645bGNduOeeQ4fCV2iw" title="Aggregation" target="_blank">Aggregation</a> </li>
<li><a href="/rltoken/Y7VsI8r5r85G_s4Tqv7Jnw" title="Introduction to MongoDB and Python" target="_blank">Introduction to MongoDB and Python</a> </li>
<li><a href="/rltoken/d5PF_1NZwdcKlsvD5yPHNg" title="mongo Shell Methods" target="_blank">mongo Shell Methods</a> </li>
<li><a href="/rltoken/PTbmjWlVmaHyx2X1PpJFmw" title="The mongo Shell" target="_blank">The mongo Shell</a> </li>
</ul></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/B-T3tvS2uN0O6s96h8OZwA" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What’s a relational database</li>
<li>What’s a none relational database</li>
<li>What is difference between SQL and NoSQL</li>
<li>How to create tables with constraints</li>
<li>How to optimize queries by adding indexes</li>
<li>What is and how to implement stored procedures and functions in MySQL</li>
<li>What is and how to implement views in MySQL</li>
<li>What is and how to implement triggers in MySQL</li>
<li>What is ACID</li>
<li>What is a document storage</li>
<li>What are NoSQL types</li>
<li>What are benefits of a NoSQL database</li>
<li>How to query information from a NoSQL database</li>
<li>How to insert/update/delete information from a NoSQL database</li>
<li>How to use MongoDB</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>All your SQL files will be executed on Ubuntu 16.04 LTS (or 18.04) using <code>MySQL 5.7</code> (version 5.7.30)</li>
<li>All your SQL queries should have a comment just before (i.e. syntax above)</li>
<li>All SQL keywords should be in uppercase (<code>SELECT</code>, <code>WHERE</code>…)</li>
<li>All your Mongo files will be interpreted/compiled on Ubuntu 16.04 LTS (or 18.04) using <code>MongoDB</code> (version 4.2)</li>
<li>The first line of all your Mongo files should be a comment: <code>// my comment</code></li>
<li>All your Python files will be interpreted/compiled on Ubuntu 16.04 LTS (or 18.04) using <code>python3</code> (version 3.5 or 3.7) and <code>PyMongo</code> (version 3.10)</li>
<li>The first line of all Python your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>Your Python code should use the <code>pycodestyle</code> style (version 2.5.*)</li>
<li>All your Python modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your Python functions should have a documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code></li>
<li>Your Python code should not be executed when imported (by using <code>if __name__ == "__main__"</code>:)</li>
<li>All your files should end with a new line</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h2>More Info</h2>

<h3>MySQL</h3>

<h4>Comments for your SQL file:</h4>

<pre><code>$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
</code></pre>

<h4>Install locally</h4>

<pre><code>$  sudo apt-get install mysql-server
...
$ mysql -uroot -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 5
Server version: 5.7.31-0ubuntu0.16.04.1 (Ubuntu)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql&gt;
</code></pre>

<h4>Use “container-on-demand” to run MySQL</h4>

<ul>
<li>Ask for container <code>Ubuntu 18.04 - Python 3.7</code></li>
<li>Connect via SSH</li>
<li>Or via the WebTerminal</li>
<li>In the container, you should start MySQL before playing with it:</li>
</ul>

<pre><code>$ service mysql start
 * MySQL Community Server 5.7.30 is started
$
$ cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password: 
Database
information_schema
mysql
performance_schema
sys
$
</code></pre>

<p><strong>In the container, credentials are <code>root/root</code></strong></p>

<h4>How to import a SQL dump</h4>

<pre><code>$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
</code></pre>

<h3>MongoDB</h3>

<h4>Install MongoDB 4.2</h4>

<p><a href="/rltoken/LR58L0Dq-ipe1KVm6D7Xgg" title="Official installation guide" target="_blank">Official installation guide</a></p>

<pre><code>$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" &gt; /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
...
$  sudo service mongod status
mongod start/running, process 3627
$ mongo --version
MongoDB shell version v4.2.8
git version: 43d25964249164d76d5e04dd6cf38f6111e21f5f
OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
allocator: tcmalloc
modules: none
build environment:
    distmod: ubuntu1804
    distarch: x86_64
    target_arch: x86_64
$  
$ pip3 install pymongo
$ python3
&gt;&gt;&gt; import pymongo
&gt;&gt;&gt; pymongo.__version__
'3.10.1'
</code></pre>

<p>Potential issue if documents creation doesn’t work or this error: <code>Data directory /data/db not found., terminating</code> (<a href="/rltoken/3KCcy_chtJlZl0U4qMYhUw" title="source" target="_blank">source</a> and <a href="/rltoken/q-SrUv6LVACyW9l9av3agg" title="source" target="_blank">source</a>)</p>

<pre><code>$ sudo mkdir -p /data/db
</code></pre>

<h4>Use “container-on-demand” to run MongoDB</h4>

<ul>
<li>Ask for container <code>Ubuntu 18.04 - MongoDB</code></li>
<li>Connect via SSH</li>
<li>Or via the WebTerminal</li>
<li>In the container, you should start MongoDB before playing with it:</li>
</ul>

<pre><code>$ service mongod start
* Starting database mongod                                              [ OK ]
$
$ cat 0-list_databases | mongo
MongoDB shell version v4.2.8
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&amp;gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("70f14b38-6d0b-48e1-a9a4-0534bcf15301") }
MongoDB server version: 4.2.8
admin   0.000GB
config  0.000GB
local   0.000GB
bye
$
</code></pre>

</div>