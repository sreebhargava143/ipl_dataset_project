from ipl_helper import *
from matplotlib import pyplot as plotter
from csv import DictReader as reader


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
        economy = (bowler_runs_balls[bowler][0]/bowler_runs_balls[bowler][1])*6
        bowler_economy_dict[economy] = bowler
    return bowler_economy_dict

def find_top_economical_bowlers(year, matches_csv, deliveries_csv):
    bowler_runs_balls = {}
    id_set = extract_id_set(year, matches_csv)
    with open(deliveries_csv) as deliveries_file:
        deliveries = reader(deliveries_file)
        for delivery in deliveries:
            if delivery['match_id'] in id_set:
                if delivery['is_super_over'] == '1':
                    continue
                runs_conceded = int(delivery['total_runs'])-int(delivery['legbye_runs'])-int(delivery['bye_runs'])
                if delivery['bowler'] not in bowler_runs_balls:
                    bowler_runs_balls[delivery['bowler']] = [0,0]
                bowler_runs_balls[delivery['bowler']][0] += runs_conceded
                if delivery['wide_runs'] == '0' and delivery['noball_runs'] == '0' :
                    bowler_runs_balls[delivery['bowler']][1]+=1               
    bowler_economy_leader_board = calculate_economies(bowler_runs_balls)    
    plot_bowler_economies(sorted_dict(bowler_economy_leader_board, reverse = True))
    
find_top_economical_bowlers(2015, 'matches.csv', 'deliveries.csv')