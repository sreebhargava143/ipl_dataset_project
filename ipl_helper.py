from csv import DictReader as reader
import collections
import random

def sorted_dict(dictionary,reverse = False, by = 'key'):
    sorted_dict = {}
    if(by=='key'):
        sorted_dict = sorted(dictionary.items(), key=lambda entry:entry[0], reverse=reverse)
        sorted_dict = collections.OrderedDict(sorted_dict)
    if(by=='value'):
        sorted_dict = sorted(dictionary.items(), key=lambda entry:entry[1], reverse=reverse)
        sorted_dict = collections.OrderedDict(sorted_dict)
    return sorted_dict

def extract_id_set(year, csv_file):
    id_set = set()
    with open(csv_file) as matches_csv:
        matches = reader(matches_csv)
        for match in matches:
            if year==int(match['season']):        
                id_set.add(match['id'])
    return sorted(id_set)

def get_unique_colors(number_of_colors):
    color_set = set()
    color = '#012345'
    for number in range(number_of_colors):
        while color in color_set:
            color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        color_set.add(color)
    return sorted(color_set)

def extract_deliveries(path):
    deliveriesDictionary = {}
    with open(path) as deliveries_csv:
        deliveries = reader(deliveries_csv)
        for delivery in deliveries:
            if delivery['match_id'] not in deliveriesDictionary:
                deliveriesDictionary[delivery['match_id']] = []
            deliveriesDictionary[delivery['match_id']].append(delivery)
    return deliveriesDictionary

# depricated
# def extract_deliveries(csv_file, id_set):
#     deliveries_dict = {}
#     with open(csv_file) as deliveriescsv:
#         deliveries = reader(deliveriescsv)
#         for delivery in deliveries:
#             if delivery['match_id'] in id_set:
#                 if delivery['match_id'] not in deliveries_dict:
#                     deliveries_dict[delivery['match_id']] = []
#                 deliveries_dict[delivery['match_id']].append(delivery)
#     return deliveries_dict


# def extract_list(csv_file):
#     csv_data = []
#     with open(csv_file) as opened_file:
#         data_file = reader(opened_file)
#         for data in data_file:
#             csv_data.append(data)
#     return csv_data


# def get_dict(csv_1, field, value):
#     nested_keys = set()
#     nested_dict = {}
#     with open(csv_1) as csv_file:
#         data_file = reader(csv_file)
#         for row in data_file:
#             nested_keys.add(row[field])
#     for key in sorted(nested_keys):
#         nested_dict[key] = value
#     return nested_dict

# def get_plotable_matches_dict(csv_1, field_1, csv_2, field_2, value):
#     nested_dict = get_dict(csv_2, field_2, value)
#     plotable_dict = {}
#     with open(csv_1) as csv_file:
#         data_file = reader(csv_file)
#         for row in data_file:
#             if row[field_1] not in plotable_dict:
#                 plotable_dict[row[field_1]] = nested_dict.copy()
#     return plotable_dict


# def get_id_set(year,matches):
#     id_set = set()
#     for match in matches:
#         if year==int(match['season']):        
#             id_set.add(match['id'])
#     return sorted(id_set)