from flask import Flask
def Create_app():
    app = Flask(__name__)
    app.config ["SECRET_KEY"] = "@Aa1444422"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    return app
