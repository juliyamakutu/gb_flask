from flask_combo_jsonapi import ResourceDetail, ResourceList

from blog.schemas import ArticleSchema
from blog.models.database import db
from blog.models import Article


class ArticleList(ResourceList):
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article,
    }

class ArticleDetail(ResourceDetail):
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article,
    }
