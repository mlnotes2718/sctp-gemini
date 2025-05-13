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

if __name__ == "__main__":
    app.run()
