'''
calculates performance of batsman based on strike rate
'''
from csv import DictReader as reader
from matplotlib import pyplot as plotter
from ipl_helper import get_unique_colors as colors
from ipl_helper import extract_deliveries as extract_deliveries
from ipl_helper import sorted_dict as sorted_dict


def get_season_id_dict(matches_csv):
    '''
    creates a season and id dictionary
    '''
    season_id_dict = {}
    try:
        if not matches_csv.endswith(".csv"):
            raise TypeError
        with open(matches_csv) as matches_file:
            matches = reader(matches_file)
            for match in matches:
                season = match['season']
                match_id = match['id']
                if season not in season_id_dict:
                    season_id_dict[season] = []
                season_id_dict[season].append(match_id)
    except FileNotFoundError:
        print("*"*5,"FILE NOT FOUND","*"*5)
        raise
    except TypeError:
        print("*"*5,"Required .csv file","*"*5)
        raise
    except KeyError:
        print("*"*5,"Required matches.csv file","*"*5)
        raise
    return season_id_dict

def calculate_strike_rate(batsmen_runs_balls, seasons_set):
    '''
    calculate strike rate
    '''
    batsmen_performances = {}
    for batsman in batsmen_runs_balls:
        batsmen_performances[batsman] = {}
        for season in seasons_set:
            if bool(batsmen_runs_balls[batsman][season]):
                strike_rate = round((batsmen_runs_balls[batsman][season][0]/
                                     batsmen_runs_balls[batsman][season][1])*100, 2)
            else:
                strike_rate = None
            batsmen_performances[batsman][season] = strike_rate
    return batsmen_performances

def plot_strike_rates(strike_rate_score_board):
    '''
    plots curves for strike rates
    '''
    plotter.figure(figsize=(15, 15))
    color_set = colors(len(strike_rate_score_board.keys()))
    color = 0
    for batsman in strike_rate_score_board:
        x_axis = list(strike_rate_score_board[batsman].keys())
        y_axis = list(strike_rate_score_board[batsman].values())
        plotter.plot(x_axis, y_axis, linewidth=3, markersize=8, label=batsman,
                     color=color_set[color], marker='o')
        color += 1
    plotter.title('STRIKE RATE OF THE BATSMEN')
    plotter.xlabel('Strike rate')
    plotter.legend(bbox_to_anchor=(1.05, 1), loc='right', borderaxespad=0)
    plotter.tight_layout()
    plotter.show()

def get_batsmen_strike_rate(batsmen_list, matches_csv, deliveries_csv):
    '''
    main function
    '''
    season_id_dict = get_season_id_dict(matches_csv)
    deliveries = extract_deliveries(deliveries_csv)
    batsmen_runs_balls = {}
    for season in season_id_dict:
        for match_id in season_id_dict[season]:
            for delivery in deliveries[match_id]:
                batsman = delivery['batsman']
                runs = int(delivery['batsman_runs'])
                if batsman in batsmen_list or not bool(batsmen_list):
                    if batsman not in batsmen_runs_balls:
                        batsmen_runs_balls[batsman] = {}
                    if season not in batsmen_runs_balls[batsman]:
                        batsmen_runs_balls[batsman][season] = [0, 0]
                    batsmen_runs_balls[batsman][season][0] += runs
                    if delivery['wide_runs'] == '0' and delivery['noball_runs'] == '0':
                        batsmen_runs_balls[batsman][season][1] += 1
    seasons_set = season_id_dict.keys()
    for batsman in batsmen_runs_balls:
        for season in seasons_set:
            if seasons_set == batsmen_runs_balls[batsman].keys():
                break
            if season not in batsmen_runs_balls[batsman]:
                batsmen_runs_balls[batsman][season] = []
        batsmen_runs_balls[batsman] = sorted_dict(batsmen_runs_balls[batsman])
    print(batsmen_runs_balls)
    print("#"*20)
    print(sorted(seasons_set))
    print("#"*20)
    batsmen_performances = calculate_strike_rate(batsmen_runs_balls, sorted(seasons_set))
    return batsmen_performances

if __name__ == "__main__":
    plot_strike_rates(get_batsmen_strike_rate(['S Dhawan', 'DA Warner', 'MS Dhoni'], 'matches.csv', 'deliveries.csv'))
