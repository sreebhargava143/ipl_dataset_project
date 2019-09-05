from matplotlib import pyplot as plotter
from ipl_helper import *
import random

def plot_matches_won(matches_won):
    bottom = [0]*10
    color_set = set()
    color = '#012345'
    color_set.add(color)
    plotter.figure(figsize=(20,20))
    plotter.style.use("fivethirtyeight")
    for team in matches_won:
        x_axis = list(matches_won[team].keys())
        y_axis = list(matches_won[team].values())
        plotter.bar(x_axis,y_axis, label = team, bottom = bottom, color = color)
        bottom = [(x+y) for x,y in zip(y_axis,bottom)]
        while color in color_set:
            color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        color_set.add(color)
    plotter.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plotter.tight_layout()
    plotter.show()

def find_matches_won(csv_file):
    matches = extract_matches(csv_file)
    matches_won = get_team_season_dict(matches)
    for match in matches:
        if  match['winner'] == '':
            continue
        matches_won[match['winner']][match['season']] += 1
    plot_matches_won(matches_won)

find_matches_won('matches.csv')