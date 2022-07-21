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
