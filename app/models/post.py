import datetime
from models import db
from sqlalchemy_serializer import SerializerMixin


class Post(db.Model, SerializerMixin):
    __tablename__ = 'post'

    id = db.Column(db.Integer(), primary_key=True)
    content = db.Column(db.String(200), nullable=True)
    created_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, content):
        self.content = content
