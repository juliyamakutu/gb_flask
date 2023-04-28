from sqlalchemy import Column, Integer, String
from blog.models.database import db


class Tag(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, default="", server_default="")

