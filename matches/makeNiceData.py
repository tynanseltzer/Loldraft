import pickle
import random
import csv
import cassiopeia as cass

# Load in data (dict of drafts and winrates)
with open('../input/data.pickle', 'rb') as handle:
    data = pickle.load(handle)

newdata = []

for team, result in data.items():
    # print("Dict entry",team,result)
    team1 = list(team[0:5])
    team2 = list(team[5:10])
    for outcome in result:
        if random.randint(0,1):
            unflipped = team1 + team2 + [outcome]
            # print('Unflipped!',unflipped)
            newdata.append(unflipped)
        else:
            flipped_outcome = 1-outcome
            flipped = team2 + team1 + [flipped_outcome]
            # print('Flipped!',flipped)
            newdata.append(flipped)

with open ('../input/drafts.csv', mode='w') as disk:
    writer = csv.writer(disk, delimiter = ",")
    for match in newdata:
        writer.writerow(match)

### Convert to 142-column format

champion_names = [champion.name for champion in cass.get_champions(region="NA")]
champion_id_to_our_id_mapping = {champion.id: champion_names.index(champion.name) for champion in cass.get_champions(region="NA")}

longdata = [[0]*283 for line in newdata]
for i in range(len(newdata)):
    match = newdata[i]
    longdata[i][-1] = match[-1]
    for champ in match[0:5]:
        our_id = champion_id_to_our_id_mapping[champ]
        longdata[i][our_id] = 1
    for champ in match[5:10]:
        our_id = champion_id_to_our_id_mapping[champ]
        longdata[i][our_id+141] = 1

# print(longdata[1])

with open ('../input/long_form_drafts.csv', mode='w') as disk:
    writer = csv.writer(disk, delimiter = ",")
    for match in longdata:
        writer.writerow(match)

# print(champion_names)