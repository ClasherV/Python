from flask import Flask, redirect, url_for
app=Flask(__name__)

@app.route('/')
def Home():
    return "<h1>Home Page</h1>"

@app.route('/Chat')
def Chat():
    return "<h1>Chat Bot</h1>"

@app.route('/Wrong')
def Wrong():
    return "<h1>Wrong Address</h1>"

@app.route('/login/<username>')
def Username(username):
    if username=="Vaibhav":
        return redirect(url_for('Chat'))
    else:
        return redirect(url_for('Wrong'))

if __name__=="__main__":
    app.run(debug=True)