from flask import Flask
from flask import  render_template, request, redirect,url_for
import datetime

app = Flask (__name__)

@app.route('/')
def home_page():
    name = 'jenya'
    return f'<html><h1><b>welcome to flask! {name}</b></h1></html>'

@app.route('/w3')
def goto_w3():
    return redirect ('https://www.w3schools.com/')





app.run()
