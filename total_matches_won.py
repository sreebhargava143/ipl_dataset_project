from matplotlib import pyplot as plotter
from csv import DictReader as reader
from ipl_helper import *


def plot_matches_won(matches_won):
    bottom = [0]*10
    color_set = list(get_unique_colors(len(matches_won.keys())))
    # print(color_set)
    plotter.figure(figsize=(15,15))
    plotter.style.use("fivethirtyeight")
    color = 0
    for team in matches_won:
        x_axis = list(matches_won[team].keys())
        y_axis = list(matches_won[team].values())
        plotter.bar(x_axis,y_axis, label = team, bottom = bottom, color = color_set[color])
        color+=1
        bottom = [(x+y) for x,y in zip(y_axis,bottom)]
    plotter.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plotter.ylabel('WINS')
    plotter.title('TOTAL MATCHES WON BY TEAM PER YEAR')
    plotter.tight_layout()
    plotter.show()

def find_matches_won(matches_csv):
    matches_won = {}
    seasons_set = set()
    with open(matches_csv) as matches_file:
        matches = reader(matches_file)
        for match in matches:
            team1 = match['team1']
            team2 = match['team2']
            season = match['season']
            winner = match['winner']
            seasons_set.add(season)
            if team1 not in matches_won:
                matches_won[team1] = {}
            if season not in matches_won[team1]:
                matches_won[team1][season]=0
            if team2 not in matches_won:
                matches_won[team2] = {}
            if season not in matches_won[team2]:
                matches_won[team2][season]=0
            if  winner == '':
                continue
            matches_won[winner][season] += 1
            
    for team in matches_won:
        for season in seasons_set:
            if seasons_set == matches_won[team].keys():
                break
            if season not in matches_won[team]:
                matches_won[team][season]=0
        matches_won[team] = sorted_dict(matches_won[team])
    plot_matches_won(matches_won)

find_matches_won('matches.csv')