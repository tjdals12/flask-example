from models import db
from sqlalchemy_serializer import SerializerMixin


class Post(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    created_time = db.Column(db.DateTime)
