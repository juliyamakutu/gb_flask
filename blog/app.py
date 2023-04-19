from datetime import datetime
from werkzeug.exceptions import BadRequest
from flask import Flask, request, g, render_template
from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.models.database import db
from blog.views.auth import auth_app, login_manager
import os


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/greet/<name>/")
def greet_name(name: str):
    return f"Hello {name}!"


@app.route("/user/")
def read_user():
    name = request.args.get("name")
    surname = request.args.get("surname")
    return f"User {name or '[no name]'} {surname or '[no surname}'}!"


@app.route("/status/", methods=["GET", "POST"])
def custom_status_code():
    if request.method == "GET":
        return """\
        To get response with custom status code
        send request using POST method
        and pass `code` in JSON body / FormData
        """

    print("raw bytes data:", request.data)

    if request.form and "code" in request.form:
        return "code from form", request.form["code"]

    if request.json and "code" in request.json:
        return "code from json", request.json["code"]

    return "", 204


@app.before_request
def process_before_request():
    """
    Sets start_time to `g` object
    """
    g.start_time = datetime.now()


@app.after_request
def process_after_request(response):
    """
    adds process time in header
    """
    if hasattr(g, "start_time"):
        response.headers["process-time"] = datetime.now() - g.start_time

    return response


@app.route("/power/")
def power_value():
    x = request.args.get("x") or ""
    y = request.args.get("y") or ""
    if not (x.isdigit() and y.isdigit()):
        app.logger.info("invalid values for power: x=%r and y=%r", x, y)
        raise BadRequest("please pass integers in `x` and `y` query params")

    x = int(x)
    y = int(y)
    result = x ** y
    app.logger.debug("%s ** %s = %s", x, y, result)
    return str(result)


@app.route("/divide-by-zero/")
def do_zero_division():
    return 1 / 0


@app.errorhandler(ZeroDivisionError)
def handle_zero_division_error(error):
    print(error)  # prints str version of error: 'division by zero'
    app.logger.exception("Here's traceback for zero division error")
    return "Never divide by zero!", 400


@app.cli.command("init-db")
def init_db():
    """
    Run in your terminal:
        flask init-db
    """
    db.create_all()
    print("done!")


@app.cli.command("create-users")
def create_users():
    """
    Run in your terminal:
        flask create-users
        > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    from blog.models.user import User
    admin = User(username="admin", is_staff=True)
    james = User(username="james")

    db.session.add(admin)
    db.session.add(james)
    db.session.commit()

    print("done! created users:", admin, james)


app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")
app.register_blueprint(auth_app, url_prefix="/auth")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# для работы авторизации нам обязательно нужен SECRET_KEY в конфигурации, добавляем
app.config["SECRET_KEY"] = "abcdefg123456"

login_manager.init_app(app)

cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
app.config.from_object(f"blog.config.{cfg_name}")

db.init_app(app)
