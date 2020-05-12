# -*- coding: utf-8 -*-

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/1006")
def test():
    return render_template("htmltest.html")
 

#start the server
if __name__ == "__main__":
    app.run()