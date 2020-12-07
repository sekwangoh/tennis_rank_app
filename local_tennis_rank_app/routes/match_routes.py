from flask import Blueprint, render_template, request
from local_tennis_rank_app.models import db, Match
from sqlalchemy import or_, and_
from sqlalchemy.sql import func



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

@match_routes.route('/rank', methods=["GET", "POST"])
def rank():
    match_info = None
    victory_count = None
    defeat_count = None
    get_win_game = None
    get_lose_game = None
    rankpoint = None
    if request.method == "POST":
        print(dict(request.form))

        result = request.form
        input_name = result['player']

        #match_info = Match.query.filter(or_(Match.winner1==input_name, Match.winner2==input_name, Match.loser1==input_name, Match.loser2==input_name)) 

        victory_info = Match.query.filter(or_(Match.winner1==input_name, Match.winner2==input_name))
        victory_count = victory_info.count() 

        defeat_info = Match.query.filter(or_(Match.loser1==input_name, Match.loser2==input_name))
        defeat_count = defeat_info.count()

        get_win_game = 6 * victory_count
        get_lose_game = defeat_info

        rankpoint =  victory_count*100 + get_win_game*10 
        

        # game_info = Match.query.filter(Match.winner_get_game==input_name)
        # #, Match.loser_get_game==input_name))
        # get_game_info = game_info

        

    return render_template("rank.html", victory = victory_count, defeat = defeat_count, game1 = get_win_game, data = get_lose_game, rank=rankpoint )

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
    #match_data = None
    match_data = None
    if request.method == "POST":
        print(dict(request.form))

        result = request.form
        # input_list = result['match_list'] 
        # match_list = Match.query.filter(Match.id==input_list)

        input_id = result['match_id'] 
        match_info = Match.query.filter_by(id=input_id)

        print(input_id)
        print(match_info)

        match_info.delete()
        match_data = Match.query.all()

        db.session.commit()

    return render_template("delete.html", data=match_data)

@match_routes.route('/update', methods=["GET", "POST"])
def update():
    match_info = None
    if request.method == "POST":
        print(dict(request.form))

        result = request.form
        
        #old_name = result['old_winner1_name']
        new_name1 = result['new_winner1_name']
        new_name2 = result['new_winner2_name']
        new_name3 = result['new_loser1_name']
        new_name4 = result['new_loser2_name']
        new_win_game = result['win_game']
        new_lose_game = result['lose_game']


        input_id = result['match_id'] 
        
        Match.query.filter(Match.id==input_id).update({'winner1':new_name1})
        Match.query.filter(Match.id==input_id).update({'winner2':new_name2})
        Match.query.filter(Match.id==input_id).update({'loser1':new_name3})
        Match.query.filter(Match.id==input_id).update({'loser2':new_name4})
        Match.query.filter(Match.id==input_id).update({'winner_get_game':new_win_game})
        Match.query.filter(Match.id==input_id).update({'loser_get_game':new_lose_game})

        #match_info = Match.query.filter(Match.id==input_id)
        match_info = Match.query.all()

        db.session.commit()

    return render_template("update.html", data=match_info)