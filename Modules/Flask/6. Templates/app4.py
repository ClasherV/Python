from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def Home():
    return render_template('jinja2.html')

@app.route('/result')
def Result():
    dict={'Physics':50,'Chemistry':60,'Mathematics':70}
    return render_template('result.html',result=dict)

if __name__=="__main__":
    app.run(debug=True)