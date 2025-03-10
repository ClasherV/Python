from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/login',methods = ['POST'])
def login():
   if request.method == 'POST':
      user = request.form # throws error if not found
      # user = request.form.get('nm') return error if not found 
      return f"{user}"

if __name__ == '__main__':
   app.run(debug = True)