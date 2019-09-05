

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
    return id_set

def sorted_dict(dictionary,reverse = False):
    sorted_dict = {}
    for key in sorted(dictionary,reverse = reverse) :
        sorted_dict[key] = dictionary[key]
    return sorted_dict


