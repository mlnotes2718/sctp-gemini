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
    if request.method == "POST":
        t = request.form.get("txt")
        r = client.models.generate_content(model=model,contents=t,)
        return(render_template("index.html",result=r.text))
    else:
        return(render_template("index.html",result="waiting"))

if __name__ == "__main__":
    app.run()
