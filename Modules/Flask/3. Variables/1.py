from flask import Flask
app=Flask(__name__)

@app.route("/Name/<name>")
def Hello(name):
    return f"Your Name is: {name}"

if __name__=="__main__":
    app.run(debug=True)