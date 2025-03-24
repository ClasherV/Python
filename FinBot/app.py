from flask import Flask, render_template, request, session, redirect, url_for
import google.generativeai as genai
import os

app=Flask(__name__)
app.secret_key=os.urandom(24)
genai.configure(api_key="AIzaSyCuceXvq3CcMoq_JLCHdt_j3LF2vW-naBU")

def get_gemini_response(prompt):
    model=genai.GenerativeModel("gemini-1.5-pro")
    response=model.generate_content(prompt)
    return response.text if response.text else "No response received."

@app.route("/", methods=["GET", "POST"])
def chat():
    if "chat_history" not in session:
        session["chat_history"]=[]

    if request.method=="POST":
        user_input=request.form["query"]
        bot_response=get_gemini_response(user_input)

        session["chat_history"].append((user_input, bot_response))
        session.modified=True

        return redirect(url_for("chat"))
    
    return render_template("index.html", chat_history=session["chat_history"])

if __name__ == "__main__":
    app.run(debug=True)