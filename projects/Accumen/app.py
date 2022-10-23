from flask import Flask, render_template, request
from sawo import createTemplate, verifyToken
import json
import os
import LinearP
API_KEY = "67f7c7df-4430-49c7-ae39-1876732a708e"


app = Flask(__name__)
# using flask = True genrates flask template
createTemplate("templates/partials", flask=True)

load = ''
loaded = 0


def setPayload(payload):
    global load
    load = payload


def setLoaded(reset=False):
    global loaded
    if reset:
        loaded = 0
    else:
        loaded += 1


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login_page")
def login_page():
    setLoaded()
    setPayload(load if loaded < 2 else '')
    sawo = {
        "auth_key": API_KEY,
        "to": "login",
        "identifier": "email"
    }
    return render_template("login.html", sawo=sawo, load=load)





@app.route("/login", methods=["POST", "GET"])
def login():
    print((request.data))

    payload = json.loads(request.data)["payload"]
    setLoaded(True)
    setPayload(payload)
    if(verifyToken(payload)):
        print("Logged in")
        status = 200
    else:
        print("Failed login")
        status = 404
    return {"status": status}
@app.route("/calculate", methods=["POST", "GET"])
def calculate():
    Payload = {}  
    if request.method == 'POST':
        budget  = int(request.form['budget'])
        hours   = int(request.form['hours'])
        Payload = LinearP.Solve(budget,hours)
    return render_template("Calci.html", Payload = Payload)

if __name__ == '__main__':
    app.run()
