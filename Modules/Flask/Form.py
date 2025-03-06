from flask import Flask, request, render_template, redirect, url_for
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('css_login.html')

@app.route('/login', methods=['POST'])
def login():
    username=request.form.get('username')
    password=request.form.get('password')
    return redirect(url_for('welcome'))

@app.route('/welcome')
def welcome():
    return render_template('css_index.html')

if __name__=='__main__':
    app.run(debug=True)