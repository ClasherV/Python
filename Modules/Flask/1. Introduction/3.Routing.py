# Decorator
"""
from flask import Flask
app=Flask(__name__)

@app.route('/home')
def Home():
    return "Home Page"

if __name__=="__main__":
    app.run(debug=True)
"""

# Function
"""
from flask import Flask
app=Flask(__name__)

def Home():
    return "Home Page"
app.add_url_rule('/','home',Home)

if __name__=="__main__":
    app.run(debug=True)
"""