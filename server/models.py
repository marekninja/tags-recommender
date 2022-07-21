from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from database import Base
import json as js


DocumentTag = Table(
    "documents_tags",
    Base.metadata,
    Column("documents_id",ForeignKey("documents.id")),
    Column("tags_id", ForeignKey("tags.id")),
)


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    text = Column(String(50), unique=True)
    documents = relationship("Document", secondary=DocumentTag, back_populates="tags")

    def to_dict(self):
        return {'id':self.id, 'text':self.text}

    def to_json(self):
        serialized = {'id':self.id, 'text':self.text}
        return js.dumps(serialized)

    def __init__(self, text=None):
        self.text = text


class Document(Base):
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True)
    text = Column(String(500))
    
    tags = relationship("Tag", secondary=DocumentTag, back_populates="documents")

    def __init__(self, text=None, tags = None):
        self.text = text
        self.tags = tags

    # def get_tags(self):
    #     return tags

    def to_dict(self):
        serialized = {'id':self.id, 'text':self.text}
        tags = [ t.to_dict() for t in self.tags]
        serialized['tags'] = tags
        return serialized

    def to_json(self):
        serialized = {'id':self.id, 'text':self.text}
        tags = [ t.to_dict() for t in self.tags]
        serialized['tags'] = tags
        return js.dumps(serialized)
    
