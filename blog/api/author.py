from flask_combo_jsonapi import ResourceDetail, ResourceList
from combojsonapi.event.resource import EventsResource

from blog.schemas import AuthorSchema
from blog.models.database import db
from blog.models import Author, Article


class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
        "session": db.session,
        "model": Author,
    }

class AuthorDetailEvents(EventsResource):
    def event_get_articles_count(self, **kwargs):
        return {"count": Article.query.filter(Article.author_id == kwargs["id"]).count()}

class AuthorDetail(ResourceDetail):
    schema = AuthorSchema
    events = AuthorDetailEvents
    data_layer = {
        "session": db.session,
        "model": Author,
    }

