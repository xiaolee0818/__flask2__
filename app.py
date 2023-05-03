from flask import Flask
from flask import render_template
app = Flask(__name__)




@app.route("/learning/")
def learning():
    return render_template("learning.jinja.html")
