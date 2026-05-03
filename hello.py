from flask import Flask, url_for
from flask import request
from flask import json

app = Flask(__name__)

@app.get("/")
def api_root():
    return "welcome"

@app.get("/articles")
def api_articles():
    return "list of articles " + url_for("api_articles")

@app.get("/articles/<int:articles_id>")
def api_article(articles_id):
    return "you are reading article " + str(articles_id)

@app.get('/hello')
def api_hello():
    if 'name' in request.args:
        return "Hello" + request.args['name']
    else:
        return "Hello John Doe"
 

@app.route("/echo", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "echo: GET\n"
    
    elif request.method == 'POST':
        return "echo: POST\n"

    elif request.method == 'PATCH':
        return "echo: PATCH\n"
    
    elif request.method == 'PUT':
        return "echo: PUT\n"
    
    elif request.method == 'DELETE':
        return "echo: DELETE\n"
 

@app.route('/messages', methods = ['POST'])
def api_message():
    if request.headers['Content-Type'] == 'text/plain':
        return "Text message: " + request.data  

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON message: " + json.dumps(request.data)
    
    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"
    
    else:
        return "415 Unsupported Media Type ;)"
  
 
if __name__ == "__main__":
    app.run()