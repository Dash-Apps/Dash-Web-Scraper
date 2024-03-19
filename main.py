import flask
import logging
from flask import Flask, request
import requests
list = open("urls.txt","a")
URL = "https://coolmathgames.com"

app = Flask(__name__)
@app.route('/')
def main():
    new_url = f"{URL}{request.full_path}"
    return requests.get(url=new_url).text

@app.route('/<path:path>')
def catchall(path):
    list.write(path)
    # -- Drop Certain Requests --
 
    if "ads" in path:
        return "No ads!"
    #  --- Send out request and return it ---
    new_url = f"{URL}{request.full_path}"
    return requests.get(url=new_url).text

app.run(debug=True,port=8080)
