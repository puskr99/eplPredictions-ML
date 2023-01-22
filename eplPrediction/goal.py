import pandas as pd 
import math

data = pd.read_csv('./dataset/results_r_copy.csv')


def get_goals(home_team_name,away_team_name):
    ## Historical Avg scores at home ##
    home_stats = data.FTHG[(data.home_team_name == home_team_name)]
    avg_home_goals = home_stats.mean()
    # print(avg_home_goals)

    ## Historical Avg scores at Away ##
    away_stats = data.FTAG[(data.away_team_name == away_team_name)]
    avg_away_goals = away_stats.mean()
    # print(avg_home_goals)

    ### Fixture goals scored per game by HOME team ###
    fixture_goals_scored_by_home_team = data.FTHG[(data.home_team_name == home_team_name)&(data.away_team_name== away_team_name)]
    avg_fixture_goals_scored_by_home_team = fixture_goals_scored_by_home_team.mean()
    # print("Avergage fixture goals scored by",  home_team_name  ,"is",   avg_fixture_goals_scored_by_home_team) 

    ### Fixture goals scored per game by AWAY team ###
    fixture_goals_scored_by_away_team = data.FTAG[(data.home_team_name == home_team_name)&(data.away_team_name== away_team_name)]
    avg_fixture_goals_scored_by_away_team = fixture_goals_scored_by_away_team.mean()
    # print("Avergage fixture goals scored by",  away_team_name  ,"is",avg_fixture_goals_scored_by_away_team) 

    ### Avg FIXTURE goals ###
    avg_fixture_goals = float(avg_fixture_goals_scored_by_away_team) + float(avg_fixture_goals_scored_by_home_team)
    # print("Average Fixture goals is",   avg_fixture_goals)

    ### Avg Home team stats ###
    ################
    home_team_stats = data.FTHG[(data.home_team_name == home_team_name)]
    avg_home_team_goals = home_team_stats.mean()
    # print("Average",  home_team_name,  " Home Goals is" ,   avg_home_team_goals) 

    ### Avg Away team stats ###
    ###############
    away_team_stats = data.FTAG[(data.away_team_name == away_team_name)]
    avg_away_team_goals = away_team_stats.mean()
    # print("Average",  away_team_name,  "Away Goals is" ,avg_away_team_goals)



    ####### Last 7 games Stats Goals ########

    #home_team#
    team_stats_home_team = data[(data.home_team_name == home_team_name) | (data.away_team_name == home_team_name)]
    last_7_games_stats_home = team_stats_home_team.head(7);
    # print(last_7_games_stats_home);

    team_stats_home_team_home_goal = last_7_games_stats_home.FTHG[(data.home_team_name == home_team_name)]
    # print(team_stats_home_team_home_goal.mean())
    team_stats_home_team_away_goal = last_7_games_stats_home.FTAG[(data.away_team_name == home_team_name)]
    # print(team_stats_home_team_away_goal.mean())
    last_7_game_home = ((team_stats_home_team_home_goal.mean()+team_stats_home_team_away_goal.mean())/2)
    # print(last_7_game_home)

    #away team#

    team_stats_away_team = data[(data.home_team_name == away_team_name) | (data.away_team_name == away_team_name)]
    last_7_games_stats_away = team_stats_away_team.head(7);
    # print(last_7_games_stats_away);

    team_stats_away_team_home_goal = last_7_games_stats_away.FTHG[(data.home_team_name == away_team_name)]
    # print(team_stats_away_team_home_goal.mean())
    team_stats_away_team_away_goal = last_7_games_stats_away.FTAG[(data.away_team_name == away_team_name)]
    # print(team_stats_away_team_away_goal.mean())
    last_7_game_away = ((team_stats_away_team_home_goal.mean()+team_stats_away_team_away_goal.mean())/2)
    # print(last_7_game_away)


    ### HOME ATTACK ###
    home_goals_scored = data.FTHG[(data.home_team_name == home_team_name)]
    avg_home_goals_scored = home_goals_scored.mean()
    home_attack = (avg_home_goals_scored/avg_home_team_goals)
    print("Home attack is  ",home_attack)


    ### AWAY DEFENCE ###
    away_goals_conceded = data.FTHG[(data.away_team_name == away_team_name)]
    avg_goals_conceded_away = away_goals_conceded.mean()
    away_defence = (avg_goals_conceded_away/avg_home_team_goals)
    print("Away defense is  ",away_defence)


    ### AWAY ATTACK ###
    away_goals_scored = data.FTAG[(data.away_team_name == away_team_name)]
    avg_goals_scored_away = away_goals_scored.mean()
    away_attack = (avg_goals_scored_away/avg_away_team_goals)
    print("Away attack is   ",away_attack)


    ### HOME DEFENCE ###
    home_goals_conceded = data.FTAG[(data.home_team_name == home_team_name)]
    avg_home_goals_conceded = home_goals_conceded.mean()
    home_defence = (avg_home_goals_conceded/avg_away_team_goals)
    print("Home defence is  ",home_defence)

    ## Projected Home Goals ##
    phg = (home_attack*away_defence+ last_7_game_home )/2
    print("Projected ", home_team_name, "Goals is(s)",   phg)

    ## Projected Away Goals ##
    pag = (away_attack*home_defence+last_7_game_away )/2
    print("Projected ", away_team_name, " Goal(s) is", pag)

    ## Projected Total goals ##
    # = home goals + away goals
    ptg = float(phg) + float(pag)
    print("Projected goals in the game is ",  ptg)

    return round(phg,2),round(pag,2),round(ptg,2)



