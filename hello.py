from flask import Flask, url_for
from flask import request
from flask import json
from flask import Response
from flask import jsonify
from functools import wraps

app = Flask(__name__)

# @app.get("/")
# def api_root():
#     return "welcome"

# @app.get("/articles")
# def api_articles():
#     return "list of articles " + url_for("api_articles")

# @app.get("/articles/<int:articles_id>")
# def api_article(articles_id):
#     return "you are reading article " + str(articles_id)

# @app.get('/hello')
# def api_hello():
#     if 'name' in request.args:
#         return "Hello" + request.args['name']
#     else:
#         return "Hello John Doe"
 

# @app.route("/echo", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
# def api_echo():
#     if request.method == 'GET':
#         return "echo: GET\n"
    
#     elif request.method == 'POST':
#         return "echo: POST\n"

#     elif request.method == 'PATCH':
#         return "echo: PATCH\n"
    
#     elif request.method == 'PUT':
#         return "echo: PUT\n"
    
#     elif request.method == 'DELETE':
#         return "echo: DELETE\n"
 

# @app.route('/messages', methods = ['POST'])
# def api_message():
#     if request.headers['Content-Type'] == 'text/plain':
#         return "Text message: " + request.data + "\n"

#     elif request.headers['Content-Type'] == 'application/json':
#         return "JSON message: " + json.dumps(request.json) + "\n"
    
#     elif request.headers['Content-Type'] == 'application/octet-stream':
#         f = open('./binary', 'wb')
#         f.write(request.data)
#         f.close()
#         return "Binary message written!" + "\n"
    
#     else:
#         return "415 Unsupported Media Type ;)" + "\n"
  
 
# @app.route('/hello', methods = ['get'])
# def hello_response():
    
#     data = {
#         'hello': 'world',
#         'number': 3
#     }
    
#     js = json.dumps(data)
    
#     resp = Response(js, status=200, mimetype='application/json')
#     resp.headers['Link'] = 'https://build-these.vercel.app/'
    
#     return resp
 

# @app.errorhandler(404)
# def not_found():
#     message = {
#         'status': 404,
#         'message': 'Not Found: ' + request.url
#     }
    
#     resp = jsonify(message)
#     resp.status_code = 404
    
#     return resp

# @app.route('/users/<userid>', methods = ['GET'])
# def api_users(userid):
#     users = {
#         '1': 'Josh',
#         '2': 'Steve',
#         '3': 'ostan'
#     }
    

def check_auth(username, password):
    return username == 'admin' and password == 'secret'

def authenticate():
    message = {
        'message': 'Authenticate.'
    }
    
    resp = jsonify(message)
    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'
    
    return resp
 
def requires_auth(f):
    @wraps(f)
    def decoded(*args, **kwargs):
        auth = request.authorization
        
        if not auth:
            return authenticate()
        
        elif not check_auth(auth.username, auth.password):
            return authenticate()
        
        return f(*args, **kwargs)
    
    return decoded


@app.route('/secrets')
def api_hello():
    return "top secret, spy stuff!!"

if __name__ == "__main__":
    app.run()