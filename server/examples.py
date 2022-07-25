from database import init_db, db_session
from models import Tag, Document

init_db()

Document.query.delete()
Tag.query.delete()

tags = [Tag("new"),Tag("old")]
doc = Document("Hello everybodies", tags=tags)

for i in tags:
    db_session.add(i)

db_session.commit()

db_session.add(doc)
db_session.commit()

docs = Document.query.all()

print([(i.id, i.text, i.tags) for i in docs])

doc = docs[0]

print(doc.to_json())

db_session.remove()