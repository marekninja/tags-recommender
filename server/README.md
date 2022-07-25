# FlaskArchitecture

## Install requirements
```
pip install -r requirements.txt
```

## App details

As a proof-of-concept, app uses in-memory DB - sqlite
Recommender model is saved pickle-d

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
