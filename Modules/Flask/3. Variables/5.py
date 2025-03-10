from flask import Flask
app=Flask(__name__)

@app.route("/Path/<path:val>")
def Hello(val):
    return f"Given Value is: {val}"

if __name__=="__main__":
    app.run(debug=True)