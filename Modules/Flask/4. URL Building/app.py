from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route('/')
def Home():
    return "<h1>Home Page</h1>"

@app.route('/login')
def Login():
    a=int(input("Enter the Number 1: "))
    b=int(input("Enter the Number 2: "))
    if a>b:
        return redirect(url_for('Chat'))
    else:
        return redirect(url_for('Wrong'))

@app.route('/Chat')
def Chat():
    return "Logged in"

@app.route('/wrong')
def Wrong():
    return "Wrong Address"

if __name__=="__main__":
    app.run(debug=True)