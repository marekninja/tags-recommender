from flask import Flask
import requests as rq
import json as js
from database import init_db, db_session
from models import Tag, Document

app = Flask(__name__)

@app.route("/docs")
def docs():
  # get all documents - pagination needed?
  documents = Document.query.all()
  documents = [i.to_dict() for i in documents]
  return js.dumps(documents)

@app.route("/docs/<int:doc_id>")
def index():
  # get one document
  pass

@app.route("/tags")
def tags():
  # get all tags
  tags = Tag.query.all()
  tags = [i.to_dict() for i in tags]
  return js.dumps(tags)

@app.route("/recommend",methods = ['GET'])
def recommend():
  # recommend tags for document

  pass

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
  init_db()
  app.run(debug=True,host='0.0.0.0', port=666)
  # app.run()