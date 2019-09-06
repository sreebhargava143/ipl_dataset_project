from matplotlib import pyplot as plotter
from csv import DictReader as reader
from ipl_helper import *


def plot_matches_won(matches_won):
    bottom = [0]*10
    color_set = list(get_unique_colors(len(matches_won.keys())))
    print(color_set)
    plotter.figure(figsize=(15,15))
    plotter.style.use("fivethirtyeight")
    color = 0
    for team in matches_won:
        x_axis = list(matches_won[team].keys())
        y_axis = list(matches_won[team].values())
        plotter.bar(x_axis,y_axis, label = team, bottom = bottom, color = color_set[color])
        color+=1
        # plotter.plot(x_axis,y_axis,label = team, color = color)
        bottom = [(x+y) for x,y in zip(y_axis,bottom)]
    plotter.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plotter.ylabel('WINS')
    plotter.title('TOTAL MATCHES WON BY TEAM PER YEAR')
    plotter.tight_layout()
    plotter.show()

def find_matches_won(matches_csv):
    matches_won = get_plotable_matches_dict(matches_csv, 'team1', matches_csv, 'season', 0)
    with open(matches_csv) as matches_file:
        matches = reader(matches_file)
        for match in matches:
            if  match['winner'] == '':
                continue
            matches_won[match['winner']][match['season']] += 1
    plot_matches_won(matches_won)

find_matches_won('matches.csv')