from flask import Flask
app=Flask(__name__)

@app.route('/<name>')
def Home(name):
    return f"<h1>Welcome {name}<h1>"

if __name__=="__main__":
    app.run(debug=True)