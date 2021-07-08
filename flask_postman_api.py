from flask import Flask
from flask import  render_template, request,redirect, url_for
import datetime
import json

app = Flask(__name__)

@app.route('/custemers', methods = ['POST','GET','PUT','DELETE'])
def homepage():
    print(request.__dict__)
    print(request.get_json())
    return request.method
    #return '[{"userId": 1,"id": 1,  "title": "quidem molestiae enim"},{"userId": 1,"id": 2,    "title": "sunt qui excepturi placeat culpa"}]'


 #return '[{"userId": 1,"id": 1,"title": "quidem molestiae enim"},{"userId": 1,"id": 2,    "title": "sunt qui excepturi placeat culpa"}]'
app.run()

'''from flask import Flask
from flask import render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/customers_get', methods = ['GET'])
def getcustomers():
    #return '[{"userId": 1,"id": 1,"title": "quidem molestiae enim"},{"userId": 1,"id": 2,    "title": "sunt qui excepturi placeat culpa"}]'
    return 'GET'

# create post
# create put
# create delete

# use postman to verify it works...
'''
