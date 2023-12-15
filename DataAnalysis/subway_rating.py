import csv
import json
import numpy as np
import pandas as pd
import math
from math import sin, cos, atan2, sqrt
import pickle as pkl
from sklearn.preprocessing import normalize
import os

def dist_lon_lat(lat1,lon1,lat2,lon2): # distance between two pts based on longtitude and lagtitude
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 3963.0 * c # 3963.0 = radius of Earth in mile
    return distance

def find_n_closest_stops(apt_loc, subway_station_data,  n=5): # apt_loc=(lat,lon); subway_station_data: list of (lat,lon)
    dist_set = []
    for i in range(len(subway_station_data)):
        distance = dist_lon_lat(subway_station_data.iat[i,1], subway_station_data.iat[i,2], apt_loc[0], apt_loc[1])
        dist_set.append(distance)
    dist_set_order = sorted(dist_set)
    return dist_set_order[0:n]

    
def get_bus_rating(apt_loc, subway_station_data):
    n_closest = find_n_closest_stops(apt_loc, subway_station_data, n=5)
    rating = 0
    for dist in n_closest:
        rating += 1 / (dist ** 2 + 3600)
    return rating

def normalize_ratings(raw_ratings):
    raw_rating_num = []
    for rating in raw_ratings:
        raw_rating_num.append(rating[1])
    mean_rating = np.nanmean((np.array(raw_rating_num, dtype=float)))
    std_dev = np.nanstd((np.array(raw_rating_num, dtype=float)))
    norm_ratings = []
    # normalize by maximum score
    for entire_rating in raw_ratings:
        norm_ratings.append([entire_rating[0], np.clip((entire_rating[1] - mean_rating) / std_dev * 50 + 50, a_max=100, a_min=0)])
    #print(mean_rating)
    #print(std_dev)
    return norm_ratings


#if (not os.path.exists('../../data/raw_subway_scores.pkl')):
    with open("/Users/Ceci/Desktop/PublicTrans/SubwayInfo.csv") as subway_info:
        subway_station_data = pd.read_csv(subway_info)
        apt_data = pd.read_csv("/Users/Ceci/Desktop/apartments.csv")
        raw_rating = []
        for i in range(len(apt_data)):
            apt_loc = (apt_data.iat[i,1], apt_data.iat[i,2])
            raw_rating.append((apt_data.iat[i,0], get_bus_rating(apt_loc, subway_station_data)))
        pkl.dump(raw_rating, open('/Users/Ceci/Desktop/raw_subway_scores.pkl', 'wb'))
#raw_rating = pkl.load(open('/Users/Ceci/Desktop/raw_subway_scores.pkl', 'rb'))
#print("Raw Ratings")
#print(raw_rating)

with open("/Users/Ceci/Desktop/PublicTrans/SubwayInfo.csv") as subway_info:
    subway_data = pd.read_csv(subway_info)
    apt_data = pd.read_csv("/Users/Ceci/Desktop/apartments.csv")
    raw_rating = []
    for i in range(len(apt_data)):
        apt_loc = (apt_data.iat[i,1], apt_data.iat[i,2])
        raw_rating.append((apt_data.iat[i,0], get_bus_rating(apt_loc, subway_data)))
    with open("/Users/Ceci/Desktop/raw_subway_scores.csv", "w") as file:
        writer = csv.writer(file)
        for score in raw_rating:
            writer.writerow(score)

norm_ratings = normalize_ratings(raw_rating)
with open("/Users/Ceci/Desktop/norm_subway_scores.csv", "w") as file1:
    writer = csv.writer(file1)
    for norm_score in norm_ratings:
        writer.writerow(norm_score)

#print('Normalized Rating')
#print(norm_ratings)
#pkl.dump(norm_ratings, open('/Users/Ceci/Desktop/normalized_subway_ratings.pkl', 'wb'))     