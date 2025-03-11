from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def Home():
    return render_template('jinja2.html')

@app.route('/marks/<int:score>')
def marks(score):
    return render_template('score.html',marks=score)

if __name__=="__main__":
    app.run(debug=True)