from flask import Flask, render_template, request
import google.generativeai as palm
import os

api_key = os.getenv("GOOGLE_API")
palm.configure(api_key=api_key)

#defaults = { 'model': "models/text-bison-001"}
app = Flask(__name__)
model = palm.GenerativeModel("gemini-1.5-flash")

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        t = request.form.get("txt")
        #r = palm.generate_text(**defaults,messages=t)
        r = model.generate_content(t)
        #return(render_template("index.html",result=r.last))
        return(render_template("index.html",result=r.candidates[0].content.parts[0].text))
    else:
        return(render_template("index.html",result="waiting"))

if __name__ == "__main__":
    app.run()
