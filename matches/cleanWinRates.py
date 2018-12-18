import pickle
import random
import csv

# Load in data (dict of drafts and winrates)
with open('../input/data.pickle', 'rb') as handle:
    data = pickle.load(handle)

newdata = []

for team, result in data.items:
    team1 = team[0:5]
    team2 = team[5:10]
    for outcome in result:
        if random.randint(0,1):
            newdata.append(team1+team2+outcome)
        else:
            newdata.append(team2+team1+(1-outcome))

with open ('matches.csv' as)