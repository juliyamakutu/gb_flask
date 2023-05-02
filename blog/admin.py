from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


from blog import models
from blog.models.database import db


# Customized admin interface
class CustomView(ModelView):
    pass


class TagAdminView(CustomView):
    column_searchable_list = ("name",)
    column_filters = ("name",)
    can_export = True
    export_types = ["csv", "xlsx"]
    create_modal = True
    edit_modal = True



# Create admin with custom base template
admin = Admin(name="Blog Admin", template_mode="bootstrap4")

# Add views
admin.add_view(CustomView(models.Tag, db.session, category="Models"))

# Add views
admin.add_view(CustomView(models.Tag, db.session, category="Models"))
admin.add_view(CustomView(models.Article, db.session, category="Models"))

admin.add_view(TagAdminView(models.Tag, db.session, category="Models"))

class UserAdminView(CustomView):
    column_exclude_list = ("_password",)
    column_searchable_list = ("first_name", "last_name", "username", "is_staff", "email")
    column_filters = ("first_name", "last_name", "username", "is_staff", "email")
    column_editable_list = ("first_name", "last_name", "is_staff")
    can_create = True
    can_edit = True
    can_delete = False

admin.add_view(UserAdminView(models.User, db.session, category="Models"))

