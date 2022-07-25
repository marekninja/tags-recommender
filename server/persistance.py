from database import db_session
from models import Tag, Document


def get_tags():
    tags = Tag.query.all()
    tags = [i.to_dict() for i in tags]
    return tags

def add_tag(text : str):
    tag = Tag(text)
    db_session.add(tag)
    db_session.commmit()



def get_docs():
    documents = Document.query.all()
    documents = [i.to_dict() for i in documents]
    return documents

def get_docs_sorted():
    documents = Document.query.order_by(Document.id.asc()).all()
    documents = [i.to_dict() for i in documents]
    return documents

def get_doc(id: int):
    doc = Document.query.filter_by(id=id).first()
    return doc.to_dict() if doc is not None else {}

def create_doc(text, tags):
    print(text)
    print(tags)
    persisted_tags = [db_session.get(Tag,i['id']) for i in tags]
    print(persisted_tags)
    doc = Document(text,persisted_tags)
    db_session.add(doc)
    db_session.commit()
