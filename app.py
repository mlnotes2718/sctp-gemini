from flask import Flask, render_template, request
from google import genai
import markdown
import os

api_key = os.getenv("GOOGLE_API")
client = genai.Client(api_key=api_key)

app = Flask(__name__)
model = "gemini-2.0-flash"

@app.route("/",methods=["GET","POST"])
def index():
        return(render_template("index.html"))

@app.route("/gemini",methods=["GET","POST"])
def gemini():
    return(render_template("gemini.html"))

@app.route("/gemini_reply",methods=["GET","POST"])
def gemini_reply():
    #q = request.form.get("q")
    if request.method == "POST":
        t = request.form.get("txt")
        r = client.models.generate_content(model=model,contents=t,)
        html = markdown.markdown(
            r.text,
            extensions=["fenced_code", "codehilite"]  # optional for code blocks
        )
        return(render_template("index.html",result_html=html))
    else:
        return(render_template("index.html",result_html="waiting"))

if __name__ == "__main__":
    app.run()
