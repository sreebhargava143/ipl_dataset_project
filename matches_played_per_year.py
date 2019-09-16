from matplotlib import pyplot as plotter
from csv import DictReader as reader
from ipl_helper import sorted_dict as sorted_dict


def plot_matches_played(year_match_map):
    plotter.style.use("fivethirtyeight")
    plotter.bar(list(year_match_map.keys()), list(year_match_map.values()))
    plotter.xlabel('Years')
    plotter.ylabel('Matches Played')
    plotter.title('IPL Matches Played Per Year')
    plotter.show()

def find_matches_per_year(csvfile):
    year_match_map = {}
    try:
        if not csvfile.endswith(".csv"):
            raise TypeError
        with open(csvfile) as matches_csv:
            matches = reader(matches_csv)
            for match in matches:
                season = match['season']
                if season not in year_match_map:
                    year_match_map[season] = 1
                else:
                    year_match_map[season] +=1
    except FileNotFoundError as e:
        print("*"*10,"FILE NOT FOUND", "*"*10)
        raise
    except TypeError:
        print("*"*10,"Required : CSV file", "*"*10)
        raise
    except KeyError:
        print("*"*10,"Required : MATCHES.CSV file", "*"*10)
        raise
    return sorted_dict(year_match_map)

if __name__ == "__main__":
    plot_matches_played(find_matches_per_year('matches.csv'))