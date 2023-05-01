from sqlalchemy import Table, Column, Integer, ForeignKey
from blog.models.database import db


article_tag_association_table = Table(
    "article_tag_association",
    db.metadata,
    Column("article_id", Integer, ForeignKey("article.id"), nullable=False),
    Column("tag_id", Integer, ForeignKey("tag.id"), nullable=False),
)
