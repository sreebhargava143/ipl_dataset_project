from csv import DictReader as reader
from matplotlib import pyplot as plotter
from ipl_helper import *

def calculate_strike_rate(batsmen_runs_balls,year,batsmen_performances):
    for batsman in batsmen_runs_balls:
        strike_rate = round((batsmen_runs_balls[batsman][0]/batsmen_runs_balls[batsman][1])*100,2)
        batsmen_performances[batsman][year] = strike_rate
    return batsmen_performances

def plot_strike_rates(strike_rate_score_board):
    plotter.figure(figsize = (15,15))
    color_set = get_unique_colors(len(strike_rate_score_board.keys()))
    color = 0
    for batsman in strike_rate_score_board:
        plotter.plot(list(strike_rate_score_board[batsman].keys()),list(strike_rate_score_board[batsman].values()), label = batsman, color = color_set[color])
        color+=1
    plotter.title('STRIKE RATE OF THE BATSMEN')
    plotter.xlabel('Strike rate')
    plotter.legend(bbox_to_anchor=(1.05, 1), loc = 'right', borderaxespad=0)
    plotter.tight_layout()
    plotter.show()
    

def get_batsmen_strike_rate(batsmen_list,matches_csv, deliveries_csv):
    season_dict = get_dict(matches_csv, 'season', 0)
    if not bool(batsmen_list):
        batsmen_performances = get_plotable_matches_dict(deliveries_csv, 'batsman', matches_csv, 'season', 0)
    else:
        batsmen_performances = {}
        with open(deliveries_csv) as deliveries_file:
            deliveries = reader(deliveries_file)
            for delivery in deliveries:
                if delivery['batsman'] in batsmen_list:
                    if delivery['batsman'] not in batsmen_performances:
                        batsmen_performances[delivery['batsman']] = season_dict.copy()
    batsmen_runs_balls = {}
    years_set = season_dict.keys()
    # (get_dict(matches_csv, 'season', 0)).keys()
    for year in years_set:
        id_set = extract_id_set(int(year), matches_csv)
        deliveries = extract_deliveries(deliveries_csv, id_set)
        for match_id in id_set:
            for delivery in deliveries[match_id]:
                if delivery['batsman'] in batsmen_performances.keys():
                    if delivery['batsman'] not in batsmen_runs_balls:
                        batsmen_runs_balls[delivery['batsman']] = []
                        batsmen_runs_balls[delivery['batsman']].append(0)
                        batsmen_runs_balls[delivery['batsman']].append(0)
                    batsmen_runs_balls[delivery['batsman']][0]+=int(delivery ['batsman_runs'])
                    batsmen_runs_balls[delivery['batsman']][1]+=1
        batsmen_performances = calculate_strike_rate(batsmen_runs_balls, year, batsmen_performances)
        batsmen_runs_balls.clear()

    plot_strike_rates(batsmen_performances)
    
get_batsmen_strike_rate(['DA Warner','S Dhawan','MC Henriques'],'matches.csv', 'deliveries.csv')