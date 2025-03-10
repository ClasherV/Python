from flask import Flask, render_template, request, url_for, redirect
app=Flask(__name__)

@app.route('/')
def Home():
    return render_template('jinja2.html')

@app.route('/login/<name>')
def Login(name):
    return render_template('jinja2.html',name=name)

if __name__=="__main__":
    app.run(debug=True)