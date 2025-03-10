from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:#ClasherV05@localhost/Todo_Database"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
DB=SQLAlchemy(app)

class TodoList(DB.Model):
    SNo=DB.Column(DB.Integer, primary_key=True)
    Title=DB.Column(DB.String(200), nullable=False)
    Description=DB.Column(DB.String(500), nullable=False)
    Date_Created=DB.Column(DB.DateTime, default=datetime.utcnow)

    def __repr__(self)->str:
        return f"{self.SNo} - {self.Title}"

@app.route('/',methods=["GET","POST"])
def Form():
    if request.method=="POST":
        Title=request.form["Title"]
        Description=request.form["Description"]
        todo=TodoList(Title=Title,Description=Description)
        DB.session.add(todo)
        DB.session.commit()
    allTodo=TodoList.query.all()
    return render_template("BootStrap.html",allTodo=allTodo)

@app.route('/update/<int:SNo>', methods=['GET','POST'])
def Update(SNo):
    if request.method=='POST':
        Title=request.form["Title"]
        Description=request.form["Description"]
        todo=TodoList.query.filter_by(SNo=SNo).first()
        todo.Title=Title
        todo.Description=Description
        DB.session.add(todo)
        DB.session.commit()
        return redirect('/')
    todo=TodoList.query.filter_by(SNo=SNo).first()
    return render_template('update.html',todo=todo)

@app.route('/delete/<int:SNo>')
def Delete(SNo):
    todo=TodoList.query.filter_by(SNo=SNo).first()
    DB.session.delete(todo)
    DB.session.commit()
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True)