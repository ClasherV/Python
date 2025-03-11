from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/result', methods=['POST','GET'])
def Result():
    if request.method=='POST':
        result=request.form
        return render_template('result.html',result=result)
    else:
        pass

if __name__=="__main__":
    app.run(debug=True)