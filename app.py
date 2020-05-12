# -*- coding: utf-8 -*-

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/tea")
def tea():
    return render_template("tea.html")

@app.route("/travel")
def travel():
    return render_template("travel.html")
 

#start the server
if __name__ == "__main__":
    app.run()