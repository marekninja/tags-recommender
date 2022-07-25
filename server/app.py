from flask import Flask, Response, request
from flask_cors import CORS

import json as js
import database as db
import persistance as pt
from recommender import init_recommender, get_recommendations

app = Flask(__name__)
CORS(app)

@app.route("/docs")
def docs():
  # get all documents - pagination needed?
  documents = pt.get_docs()
  return js.dumps(documents)

# CRU - create, retrieve, update, delete

@app.route("/docs",methods = ['POST'])
def create_doc():
  # create one document
  request_data = request.get_json(force=True)  # getting data from client
  pt.create_doc(request_data["text"], request_data["tags"],)
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

@app.route("/recommend",methods = ['POST'])
def recommend():
  # recommend tags for document
  init_recommender()
  data = request.get_json(force=False)
  # data = request.get_json(force=True)
  print(data)
  text = data['text']
  tags = get_recommendations(text)
  return js.dumps(tags)

@app.teardown_appcontext
def shutdown_session(exception=None):
  print("session removed")
  db.db_session.remove()
  print("session removed")

if __name__ == '__main__':
  db.init_db()
  # init_recommender()
  app.run(debug=True,host='localhost', port=5000)
  # app.run()