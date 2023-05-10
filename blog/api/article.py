from flask_combo_jsonapi import ResourceDetail, ResourceList
from combojsonapi.event.resource import EventsResource

from blog.schemas import ArticleSchema
from blog.models.database import db
from blog.models import Article


class ArticleListEvents(EventsResource):
    def event_get_count(self):
        return {"count": Article.query.count()}


class ArticleList(ResourceList):
    schema = ArticleSchema
    events = ArticleListEvents
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
