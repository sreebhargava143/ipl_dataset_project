from ipl_helper import *
from matplotlib import pyplot as plotter
from csv import DictReader as reader
def plot_extras_conceded(year,extras_conceded):
    plotter.barh(list(extras_conceded.keys()),list(extras_conceded.values()))
    plotter.style.use("fivethirtyeight")
    plotter.xlabel("Extra Runs Conceded")
    plotter.title('For the year '+ str(year)+ ' plot the extra runs conceded per team.')
    plotter.tight_layout()
    plotter.show()

def find_extra_runs_conceded(year, matches_csv, deliveries_csv):
    matches = extract_list(matches_csv)
    id_set = get_id_set(year, matches)
    extra_runs_conceded = {}
    deliveries = extract_deliveries(deliveries_csv)
    for match_id in id_set:
        for delivery in deliveries[match_id]:
                if delivery['bowling_team'] not in extra_runs_conceded:
                    extra_runs_conceded[delivery['bowling_team']] = 0
                extra_runs_conceded[delivery['bowling_team']] += int(delivery['extra_runs'])

    plot_extras_conceded(year,extra_runs_conceded) 

find_extra_runs_conceded(2016, 'matches.csv', 'deliveries.csv')