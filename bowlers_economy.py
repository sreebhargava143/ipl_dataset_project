from ipl_helper import *
from matplotlib import pyplot as plotter

def plot_bowler_economies(bowler_economy_leader_board):
    plotter.figure(figsize = (20,20))
    plotter.barh(list(bowler_economy_leader_board.values())[-30:],list(bowler_economy_leader_board.keys())[-30:])
    plotter.title('TOP 30 ECONOMICAL BOWLERS')
    plotter.yticks( verticalalignment='center')
    plotter.xlabel('ECONOMY')
    plotter.show()

def calculate_economies(bowler_runs_balls):
    bowler_economy_dict = {}
    for bowler in bowler_runs_balls:
        economy = round((bowler_runs_balls[bowler][0]/bowler_runs_balls[bowler][1])*6,2)
        bowler_economy_dict[economy] = bowler
    return bowler_economy_dict

def find_top_economical_bowlers(year, matches_csv, deliveries_csv):
    bowler_runs_balls = {}
    id_set = extract_id_set(year, matches_csv)
    deliveries = extract_deliveries(deliveries_csv, id_set)
    for match_id in id_set:
        for delivery in deliveries[match_id]:
            if delivery['is_super_over'] == '1':
                continue
            runs_conceded = int(delivery['total_runs'])-int(delivery['legbye_runs'])-int(delivery['bye_runs'])
            if delivery['bowler'] not in bowler_runs_balls:
                bowler_runs_balls[delivery['bowler']] = []
                bowler_runs_balls[delivery['bowler']].append(runs_conceded)
                bowler_runs_balls[delivery['bowler']].append(1)
            else:
                bowler_runs_balls[delivery['bowler']][0]+=runs_conceded
                bowler_runs_balls[delivery['bowler']][1]+=1
    
    bowler_economy_leader_board = sorted_dict(calculate_economies(bowler_runs_balls),reverse=True)
    
    plot_bowler_economies(bowler_economy_leader_board)

find_top_economical_bowlers(2015, 'matches.csv', 'deliveries.csv')