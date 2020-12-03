from flask import Blueprint, render_template, request
from local_tennis_rank_app.models import db, Match
from sqlalchemy import or_, and_
import pdb;


match_routes = Blueprint('match_routes', __name__)


@match_routes.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(dict(request.form))
        result = request.form

        db.session.add(Match(match_name=result["match_name"],
                              date=result["match_date"], 
                              winner1=result["match_winner1"],
                              winner2=result["match_winner2"], 
                              loser1=result["match_loser1"], 
                              loser2=result["match_loser2"], 
                              winner_get_game=result["match_winner_get_game"], 
                              loser_get_game=result["match_loser_get_game"]
                              ))
        db.session.commit()
    return render_template('match.html')

@match_routes.route('/get', methods=["GET", "POST"])
def get():
    match_info = None
    #winner_match_info = None
    #loser_match_info = None
    if request.method == "POST":
        print(dict(request.form))

        result = request.form
        input_name = result['player']

        match_info = Match.query.filter(or_(Match.winner1==input_name, Match.winner2==input_name, Match.loser1==input_name, Match.loser2==input_name)) 
        #winner_match_info = Match.query.filter_by(winner1=input_name) or Match.query.filter_by(winner2=input_name)
        #loser_match_info = or Match.query.filter_by(loser1=input_name) or Match.query.filter_by(loser2=input_name) 

        #match_data = Match.query.all()

        #player_victory = Match.query.filter_by(winner1=input_name).count() # Match.query.filter_by(winner2=input_name).count()
        # player_defeat = Match.query.filter_by(loser1=input_name).count() #Match.query.filter_by(loser2=input_name).count()

        # match_id = player_info.__dict__['id']

        # get_game1 = Match.query.filter_by(winner_get_game=winner_get_game) 
        # get_game2 = Match.query.filter_by(loser_get_game=loser_get_game)

    return render_template("get.html", data = match_info)#winner_data=winner_match_info, loser_data=loser_match_info)

@match_routes.route('/delete', methods=["GET", "POST"])
def delete():
    match_data = None
    if request.method == "POST":
        print(dict(request.form))

        result = request.form
        input_name = result['player']
        
        match_info = Match.query.filter_by(winner1=input_name) or Match.query.filter_by(match_winner2=input_name)

        match_data = Match.query.all()

        match_info.delete()

        db.session.commit()

    return render_template("delete.html", data=match_data)

@match_routes.route('/update', methods=["GET", "POST"])
def update():
    match_info = None
    if request.method == "POST":
        #print(dict(request.form))

        result = request.form
        input_id = result['match_id'] 
        match_info = Match.query.filter(Match.id==input_id)

        
        old_name = result['player1_name']
        new_name = result['edit_player1_name']

        test_1 = match_info.first()
        print(test_1.__dict__)

        #pdb.set_trace() 
        #breakpoint()
        #Match.query.filter(Match.id==input_id).filter(Match.winner1==old_name).update({'winner1':new_name})

        #print(old_name)
        #print(new_name)

        db.session.commit()

    return render_template("update.html", data=match_info)