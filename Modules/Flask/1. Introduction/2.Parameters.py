# host=localhost
"""
from flask import Flask
app=Flask(__name__)

@app.route('/')
def Host():
    return "host=localhost"

if __name__=="__main__":
    app.run(host="localhost")
"""

# host=0.0.0.0
"""
from flask import Flask
app=Flask(__name__)

@app.route('/')
def Host():
    return "host=0.0.0.0"

if __name__=="__main__":
    app.run(host="0.0.0.0")
"""

# port=5000
"""
from flask import Flask
app=Flask(__name__)

@app.route('/')
def Port():
    return "port=5000"

if __name__=="__main__":
    app.run(port=8000)
"""

# port=8000
"""
from flask import Flask
app=Flask(__name__)

@app.route('/')
def Port():
    return "port=8000"

if __name__=="__main__":
    app.run(port=8000)
"""

# debug=False
"""
from flask import Flask
app=Flask(__name__)

@app.route('/')
def Debug():
    return "Debug=False"

if __name__=="__main__":
    app.run(debug=False)
"""

# debug=True
"""
from flask import Flask
app=Flask(__name__)

@app.route('/')
def Debug():
    return "Debug=True"

if __name__=="__main__":
    app.run(debug=True)
"""

from flask import Flask
app=Flask(__name__)

@app.route('/')
def Parameters():
    return "Parameters"

if __name__=="__main__":
    app.run(host="localhost",port=8000,debug=True)