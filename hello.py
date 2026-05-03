from flask import Flask, url_for
from flask import request

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
 
if __name__ == "__main__":
    app.run()