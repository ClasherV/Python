from flask import Flask, render_template, request, session, Response, stream_with_context
import google.generativeai as genai
import os
import time

app = Flask(__name__)
app.secret_key = os.urandom(24)

genai.configure(api_key="AIzaSyCuceXvq3CcMoq_JLCHdt_j3LF2vW-naBU")  # Replace this with your API key

def stream_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-1.5-pro")
    response_stream = model.generate_content_stream(prompt)

    for chunk in response_stream:
        if chunk.text:
            yield chunk.text
        time.sleep(0.05)  # Smooth streaming effect

@app.route("/", methods=["GET", "POST"])
def chat():
    if "chat_history" not in session:
        session["chat_history"] = []

    if request.method == "POST":
        user_input = request.form["query"]
        session["chat_history"].append(("You", user_input))

        def generate():
            yield "<div class='bot-response'><strong>FinBot:</strong> "
            response = ""
            for chunk in stream_gemini_response(user_input):
                response += chunk
                yield chunk
            yield "</div>"

            session["chat_history"].append(("FinBot", response))
            session.modified = True

        return Response(stream_with_context(generate()), content_type="text/html")

    return render_template("index.html", chat_history=session["chat_history"])

if __name__ == "__main__":
    app.run(debug=True)
