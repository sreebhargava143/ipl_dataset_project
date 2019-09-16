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
    try:
        if not isinstance(year, int):
            raise TypeError
        if not matches_csv.endswith(".csv") or not deliveries_csv.endswith(".csv"):
            raise TypeError
        id_set = extract_id_set(year, matches_csv)
        extra_runs_conceded = {}
        with open(deliveries_csv) as deliveriescsv:
            deliveries_reader = reader(deliveriescsv)
            for delivery in deliveries_reader:
                bowling_team = delivery['bowling_team']
                if delivery['match_id'] in id_set:
                    if bowling_team not in extra_runs_conceded:
                        extra_runs_conceded[bowling_team] = 0
                    extra_runs_conceded[bowling_team] += int(delivery['extra_runs'])
    except FileNotFoundError as e:
        print("*"*10,"FILE NOT FOUND", "*"*10)
        raise
    except KeyError:
        print("*"*10,"""PARAM 1 REQUIRED : YEAR INT
              PARAM 2 REQUIRED : MATCHES.CSV file
              PARAM 3 REQUIRED : DELIVERIES.CSV""", "*"*10)
        raise
    except TypeError:
        print("*"*10,"Required : CSV file as input", "*"*10)
        print("*"*10,"Required : year as integer", "*"*10)
        raise
    return sorted_dict(extra_runs_conceded,by = 'value')

if __name__ == "__main__":
    year = 2016
    extra_runs_conceded = find_extra_runs_conceded(year, 'matches.csv', 'deliveries.csv')
    plot_extras_conceded(year, extra_runs_conceded)
    