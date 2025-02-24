from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:#ClasherV05@localhost/College"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
DB=SQLAlchemy(app)
class Student(DB.Model):
    Roll_No=DB.Column(DB.Integer, primary_key=True)
    Name=DB.Column(DB.String(20), nullable=False)
    Age=DB.Column(DB.Integer, nullable=False)
    DOB=DB.Column(DB.DateTime, default=datetime.utcnow)

def __repr__(self)->str:
    return f"{self.Roll_No} - {self.Name}"

@app.route('/')
def Function():
    student=Student(Name="Vaibhav Raikwar",Age=19)
    DB.session.add(student)
    DB.session.commit()
    return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True)