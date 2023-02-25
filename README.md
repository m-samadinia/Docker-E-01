[![Python](https://img.shields.io/badge/python-3.7-green)](https://www.python.org/downloads/release/python-370/)
# DOCKER-E-01
<p> This is an example for Dockerizing the FastAPI services</p>

## Steps
<br/>
<b>Step 1.</b> Create a new virtual environment 
<pre>
python -m venv .env
</pre> 
<br/>
<b>Step 2.</b> Activate your virtual environment
<pre>
source .env/bin/activate # Linux
.\.env\Scripts\activate # Windows 
</pre>
<br/>
<b>Step 3.</b> Install dependencies
<pre>
python -m pip install --upgrade pip
pip install -r requirements.txt
</pre>
<br/>
<b>Step 4.</b> Set environment variable
<pre><code>set DEFAULT_PORT=8080 # windows</code></pre>
<br/>
<b>Step 5.</b> run app
<pre><code>python main.py</code></pre>

<h2> Dockerizing</h2>
You can Dockerizing app with two way

<b>solution 1.</b>
<pre><code>docker build -t e-01 .</code>
<code>docker run -d --name fastapi_docker -p 8080:8080 --restart always e-01</code></pre>
<br/>
<b>solution 2.</b>
<pre><code>docker-compose up -d</code></pre>
<br/>


<h2> Notices</h2>
You can see APIDoc
<pre><code>http://localhost:8080/redoc   or</code>
<code>http://localhost:8080/docs   </code></pre>


<h2> Usage Example</h2>
<pre><code>http://localhost:8080/api/routes/helloworld</code></pre> 
<pre><code>http://localhost:8080/api/routes/author</code>