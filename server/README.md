# FlaskArchitecture

## Install requirements
```
pip install -r requirements.txt
```

## App details

App needs some persistance for recommendation model.

2 options:
* **use Azure App Service - always running, saves new model every night**
  * simple flask server, with PostgreSQL DB for documents...
* use Azure Functions and some triggers to train and save the model somewhere every night 🤷‍♂️

As a proof-of-concept, app uses in-memory DB - sqlite

## REST API - supported routes:

**/docs**

GET: get all documents

POST: create document
  
    {"text": "Hello yellow", "tags":[{"id": 1, "text": "new"}, {"id": 2, "text": "old"}]}

**/docs/:id**

GET: get one document with *id*

**/tags**

GET: get all tags

**/recommend**

POST: recommends hashtags for *text* based on similarity to top K documents

    {"text": "Hello yellow"}
    
    
## Other stuff

**./prototypes**

contains [jupyter notebook](./prototypes/hashtags_recommender.ipynb) with recommender prototypes and comparison of approaches
