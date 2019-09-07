from matplotlib import pyplot as plotter
from csv import DictReader as reader
from ipl_helper import *


def plot_matches_played(year_match_map):
    plotter.style.use("fivethirtyeight")
    plotter.bar(list(year_match_map.keys()),list(year_match_map.values()))
    plotter.xlabel('Years')
    plotter.ylabel('Matches Played')
    plotter.title('IPL Matches Played Per Year')
    plotter.show()

def find_matches_per_year(csvfile):
    yearMatchMap = {}
    
    with open(csvfile) as matches_csv:
        matches = reader(matches_csv)
        for match in matches:
            season = match['season']
            if season not in yearMatchMap:
                yearMatchMap[season] = 1
            else:
                yearMatchMap[season] +=1
                
    plot_matches_played(sorted_dict(yearMatchMap))

find_matches_per_year('matches.csv')