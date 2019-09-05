from csv import DictReader as reader

def get_seasons_dict(matches):
    total_seasons = set()
    seasons = {}
    for match in matches:
        total_seasons.add(match['season'])
    for season in sorted(total_seasons):
        seasons[season] = 0
    return seasons

def get_team_season_dict(matches):
    seasons = get_seasons_dict(matches)
    total_teams = {}
    for match in matches:
        if match['team1'] not in total_teams:
            total_teams[match['team1']] = seasons.copy()
    # print(total_teams)
    return total_teams


def get_id_set(year,matches):
    id_set = set()
    for match in matches:
        if year==int(match['season']):        
            id_set.add(match['id'])
    return sorted(id_set)

def sorted_dict(dictionary,reverse = False):
    sorted_dict = {}
    for key in sorted(dictionary,reverse = reverse) :
        sorted_dict[key] = dictionary[key]
    return sorted_dict

def extract_list(csv_file):
    matches_data = []
    with open(csv_file) as matches_csv:
        matches = reader(matches_csv)
        for match in matches:
            matches_data.append(match)
    return matches_data

def extract_deliveries(csv_file):
    deliveries_dict = {}
    with open(csv_file) as deliveriescsv:
        deliveries = reader(deliveriescsv)
        for delivery in deliveries:
            if delivery['match_id'] not in deliveries_dict:
                deliveries_dict[delivery['match_id']] = []
            deliveries_dict[delivery['match_id']].append(delivery)
    return deliveries_dict


