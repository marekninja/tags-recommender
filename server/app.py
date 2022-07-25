from flask import Flask, Response, request
# import requests as rq
import json as js
import database as db
from models import Tag, Document
import persistance as pt

app = Flask(__name__)

@app.route("/docs")
def docs():
  # get all documents - pagination needed?
  documents = pt.get_docs()
  return js.dumps(documents)

# CRU - create, retrieve, update, delete

@app.route("/docs",methods = ['POST'])
def create_doc():
  # create one document
  request_data = request.get_json()  # getting data from client
  pt.create_doct(request_data["text"], request_data["tags"],)
  response = Response("Document added", 201, mimetype='application/json')
  return response

@app.route("/docs/<int:id>",methods = ['GET',])
def get_doc(id):
  # get one document
  doc = pt.get_doc(id)
  return js.dumps(doc)

@app.route("/docs/<int:id>",methods = ['PUT'])
def update_doc(id):

  pass


@app.route("/tags")
def tags():
  # get all tags
  tags = pt.get_tags()
  # tags = Tag.query.all()
  # tags = [i.to_dict() for i in tags]
  return js.dumps(tags)

@app.route("/recommend",methods = ['GET'])
def recommend():
  # recommend tags for document
  data = request.get_json()

  pass

@app.teardown_appcontext
def shutdown_session(exception=None):
  print("session removed")
  db.db_session.remove()
  print("session removed")

if __name__ == '__main__':
  db.init_db()
  app.run(debug=True,host='localhost', port=5000)
  # app.run()