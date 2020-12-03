from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    match_name = db.Column(db.String, nullable=False)
    date = db.Column(db.Integer, nullable=False)
    winner1 = db.Column(db.String, nullable=False)
    winner2 = db.Column(db.String, nullable=False)
    loser1 = db.Column(db.String, nullable=False)
    loser2 = db.Column(db.String, nullable=False)
    winner_get_game = db.Column(db.Integer, nullable=False)
    loser_get_game = db.Column(db.Integer, nullable=False)
    

    def __repr__(self):
        return f"<Match {self.id} {self.match_name} >"


def parse_records(db_records):
    parsed_list = []
    for record in db_records:
        parsed_record = record.__dict__
        print(parsed_record)
        del parsed_record["_sa_instance_state"]
        parsed_list.append(parsed_record)
    return parsed_list
