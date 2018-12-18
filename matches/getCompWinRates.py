import cassiopeia as cass
from cassiopeia import Summoner, Match
from cassiopeia.data import Season, Queue
import pickle
import math

cass.set_riot_api_key("RGAPI-e2ea041a-5f1d-4158-90fd-1d73fd1e3465") # Expires Dec 18
cass.set_default_region("NA")

champion_id_to_name_mapping = {champion.id: champion.name for champion in cass.get_champions(region="NA")} # From Cass examples match.py

with open('../input/match_ids.txt') as f:
    ids = f.read().splitlines()
    print("Length of match_ids.txt: "+str(len(ids)))

# Load in data (dict of drafts and winrates)
with open('../input/data.pickle', 'rb') as handle:
    data = pickle.load(handle)

print("Length of dict: " +str(len(data)))

# data = dict() # Initialize data

# for team, result in data.items():
#     print(team)
#     print(result)
#     if(len(result) > 1):
#         print("-----------MULTIPLE GAMES-----------")

for i in range(27800, len(ids)):

    if i%50 == 0: # Save data every once in a while
        # Pickle data to disk
        print("Pickling...")
        print("Matches analyzed so far: "+str(i))
        print("Drafts analyzed: " + str(len(data)))
        # print("Rejected: " + str(rejected))
        with open('../input/data.pickle', 'wb') as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # Don't waste time accessing the match if we know it's old.
    if int(ids[i]) < 2893574694: # Smaller than this and the match is definitely old.
        continue

    # print(ids[i])
    match = cass.get_match(int(ids[i]))
    # print(match)
    # print(match.patch, match.is_remake, match.blue_team)
    # print(str(match.patch))

    if str(match.patch) not in ["8.24","8.23","8.22","8.21"]: # Recent games only
        print(str(i) + " – BAD (old)")
        print(str(match.patch))
        continue
    if match.is_remake: # No remakes
        print(str(i)+ " – BAD (remake)")
        continue

    if match.blue_team.win:
        winning_team = match.blue_team
        losing_team = match.red_team
    else:
        winning_team = match.red_team
        losing_team = match.blue_team
    winning_team_champs = []
    losing_team_champs = []
    for participant in winning_team.participants:
        winning_team_champs.append(participant.champion.id)
        # print(champion_id_to_name_mapping[participant.champion.id])
    winning_team_champs = tuple(sorted(winning_team_champs)) # Sort for easy comparison, convert to tuple to use as key
    # winning_names = []
    # for i in range(len(winning_team_champs)):
    #     winning_names.append(champion_id_to_name_mapping[winning_team_champs[i]])
    # print("Winning team: " + str(winning_names))

    for participant in losing_team.participants:
        losing_team_champs.append(participant.champion.id)
    losing_team_champs = tuple(sorted(losing_team_champs)) # Sort for easy comparison, convert to tuple to use as key
    # losing_names = []
    # for id in losing_team_champs:
    #     losing_names.append(champion_id_to_name_mapping[id])
    # print("Losing team: " + str(losing_names))
    winFirst = winning_team_champs + losing_team_champs
    loseFirst = losing_team_champs + winning_team_champs
    if winFirst in data:
        data[winFirst].append(1) # Add a win
    elif loseFirst in data:
        data[loseFirst].append(0) # Add a loss
    else:
        data[winFirst] = [1] # This is a new comp. Default to winning team first

    print(str(i) + " – GOOD") # Need to know where to pick back up after we crash

# Save again if we finish the loop
with open('../input/data.pickle', 'wb') as handle:
    pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
