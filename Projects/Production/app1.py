from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:#ClasherV05@localhost/Users"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
users=SQLAlchemy(app)

# class User(users.Model):
#     SNo=users.Column(users.Integer, primary_key=True)
#     email=users.Column(users.String(200), nullable=False)
#     Description=DB.Column(DB.String(500), nullable=False)
#     Date_Created=DB.Column(DB.DateTime, default=datetime.utcnow)

#     def __repr__(self)->str:
#         return f"{self.SNo} - {self.Title}"

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def Login():
        return render_template('login_index.html')
    
@app.route('/bot', methods=['GET','POST'])
def Bot():
#        username=request.form['username']
#        password=request.form['password']
#        if username in users and users[username]==password:
        return render_template('Bot.html')
#        else:
#         return render_template('login_index.html', error="Account not found or incorrect password.")
    
@app.route("/signup",methods=['GET','POST'])
def SignUp():
        # if request.method=='POST':
        #      email=request.form['email']
        #      password=request.form['password']
        #      users[email]=password
        #      return redirect(url_for('Login'))
        return render_template("signup.html")

if __name__=="__main__":
    app.run(debug=True)