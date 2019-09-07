from ipl_helper import *
from matplotlib import pyplot as plotter
from csv import DictReader as reader


def plot_extras_conceded(year,extras_conceded):
    plotter.figure(figsize=(13,10))
    plotter.style.use("fivethirtyeight")
    plotter.barh(list(extras_conceded.keys()),list(extras_conceded.values()))
    plotter.xlabel("Extra Runs Conceded")
    plotter.title('For the year '+ str(year)+ ' plot the extra runs conceded per team.')
    plotter.tight_layout()
    plotter.show()

def find_extra_runs_conceded(year, matches_csv, deliveries_csv):
    id_set = extract_id_set(year, matches_csv)
    extra_runs_conceded = {}
    with open(deliveries_csv) as deliveriescsv:
        deliveries = reader(deliveriescsv)
        for delivery in deliveries:
            bowling_team = delivery['bowling_team']
            if delivery['match_id'] in id_set:
                if bowling_team not in extra_runs_conceded:
                    extra_runs_conceded[bowling_team] = 0
                extra_runs_conceded[bowling_team] += int(delivery['extra_runs'])
    plot_extras_conceded(year,sorted_dict(extra_runs_conceded,by = 'value')) 

find_extra_runs_conceded(2016, 'matches.csv', 'deliveries.csv')