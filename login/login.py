import base64
import logging
import warnings

import pika
# packages for swagger
from flasgger import Swagger
from flasgger import swag_from
from flask import Flask, render_template, request, jsonify, make_response, json
from flask_pymongo import PyMongo


app = Flask(__name__)

swagger = Swagger(app)

# setup logger
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
warnings.filterwarnings("ignore", category=DeprecationWarning)

myclient = PyMongo(app, uri="mongodb://rs1:27041/test")
@app.route('/login', methods=['GET','POST'])
@app.route('/', methods=['GET','POST'])

def login():
    if request.method == 'POST':
        username=request.values['username']
        password=request.values['password']
        if (username=="")or(password==""):
           return "<h1>input error!</h1>"
        else:
           users = myclient.db.col.find_one({'username':username})
           if users:
               name = users['username']
               pas  = users['password'] 
               epassword = base64.b64encode(password.encode('utf-8')).decode()
           
               if (name==username)and(pas==epassword):
                   return '<h1>Login Success</h1>'
               else:
                   return "<h1>login error check the name or password!</h1>"    
           else:
               return "<h1>login error check the name or password!</h1>"
    else:
        return render_template('login.html')

@app.route('/')
def index():
    return 'Web App with Python Flask!'
    
if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5002)
