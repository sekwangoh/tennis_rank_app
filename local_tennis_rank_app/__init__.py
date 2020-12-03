# import os
from flask import Flask
from local_tennis_rank_app.routes import main_routes, match_routes
from local_tennis_rank_app.models import db, migrate
# from dotenv import load_dotenv

# load_dotenv()


# URI = os.getenv('POSTGRES_URL') 
# USER = os.getenv('POSTGRES_USER')
# PASSWORD = os.getenv('POSTGRES_PW')
# DB = os.getenv('POSTGRES_DB')

DATABASE_URL = 'sqlite:///local_tennis_rank_app.sqlite3'


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main_routes.main_routes)
    app.register_blueprint(match_routes.match_routes, url_prefix='/match')
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
