import pickle
import random
import csv

# Load in data (dict of drafts and winrates)
with open('../input/data.pickle', 'rb') as handle:
    data = pickle.load(handle)

newdata = []

for team, result in data.items():
    team1 = list(team[0:5])
    team2 = list(team[5:10])
    for outcome in result:
        if random.randint(0,1):
            unflipped = team1 + team2 + [outcome]
            print('Unflipped!')
            newdata.append(unflipped)
        else:
            flipped_outcome = 1-outcome
            flipped = team1 + team2 + [flipped_outcome]
            print('Flipped!')
            newdata.append(flipped)

with open ('../input/drafts.csv', mode='w') as disk:
    writer = csv.writer(disk, delimiter = ",")
    for match in newdata:
        writer.writerow(match)