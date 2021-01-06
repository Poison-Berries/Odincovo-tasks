from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def task():
    return render_template("page.html")