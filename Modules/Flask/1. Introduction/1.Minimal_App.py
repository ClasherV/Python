from flask import Flask
app=Flask(__name__)

@app.route('/')
def Minimal():
    return "Hello World"

if __name__=="__main__":
    app.run()