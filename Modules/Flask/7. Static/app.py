from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/info',methods=['POST','GET'])
def Information():
    if request.method=='POST':
        data=request.form
        return render_template('Information.html',dict=data)
    
if __name__=="__main__":
    app.run(debug=True)