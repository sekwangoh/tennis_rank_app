from flask import Blueprint, render_template, jsonify
from local_tennis_rank_app.models import Match, parse_records, db



main_routes = Blueprint('main_routes', __name__)


@main_routes.route('/')
def index():
    data = Match.query.all()
    return render_template("index.html", data=data)

@main_routes.route('/reset')
def reset_db():
  db.drop_all()
  db.create_all()
  return 'DB refreshed'

# @main_routes.route('/menu.json')
# def json_data():
#     raw_data = Coffee.query.all()
#     parsed_data = parse_records(raw_data)
    
#     return jsonify(parsed_data)
