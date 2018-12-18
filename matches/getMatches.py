import cassiopeia as cass
from cassiopeia import Summoner, Match
from cassiopeia.data import Season, Queue

cass.set_riot_api_key("RGAPI-8f0b3a2f-502b-4822-bc30-a6a7b62f8a3d") # Expires Dec 18
cass.set_default_region("NA")

# Step 2: Get a bunch of matches

with open('summoners.txt') as f:
    summoners = f.read().splitlines()
    print("Length of summoners.txt: "+str(len(summoners)))

with open('match_ids.txt') as f:
    ids = f.read().splitlines()
    print("Length of match_ids.txt: "+str(len(ids)))

start = summoners.index("kennyd15") # Index starting with last one we were looking it before crashing

for i in range(start+2, len(summoners)): # Change on crashes

    summoner = cass.get_summoner(name=summoners[i])
    print("Querying match history of "+summoners[i])
    match_history = cass.get_match_history(summoner=summoner,
        seasons={Season.season_8}, queues={Queue.ranked_solo_fives})

    # for participant in match_history[0].participants:
    #     print(participant.summoner.name)

    for match in match_history: # Check match history of this summoner
        if match.id not in ids:
            ids.append(match.id)
    # Save IDs to file
    print("Writing match IDs to file...")
    print("Length of match_ids.txt: "+str(len(ids)))
    with open('match_ids.txt', 'w') as f:
        for item in ids:
            f.write("%s\n" % item)