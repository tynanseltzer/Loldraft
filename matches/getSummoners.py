import cassiopeia as cass
from cassiopeia import Summoner, Match
from cassiopeia.data import Season, Queue

cass.set_riot_api_key("RGAPI-8f0b3a2f-502b-4822-bc30-a6a7b62f8a3d") # Expires Dec 18
cass.set_default_region("NA")

# Step 1: Generate a bunch of summoners

# summoners = ["Imaqtpie"] # Seed

with open('../input/summoners.txt') as f:
    summoners = f.read().splitlines()
    print("Length of summoners.txt: "+str(len(summoners)))

for i in range(2,10): # Change on crashes

    summoner = cass.get_summoner(name=summoners[i])
    print("Querying match history of "+summoners[i])
    match_history = cass.get_match_history(summoner=summoner,
        seasons={Season.season_8}, queues={Queue.ranked_solo_fives})

    # for participant in match_history[0].participants:
    #     print(participant.summoner.name)

    j = 0
    for match in match_history: # Check match history of this summoner
        for participant in match.participants: # Get new summoners
            if participant.summoner.name not in summoners:
                summoners.append(participant.summoner.name)
        if j == 50:
            # Save summoners to file
            print("Writing summoners to file...")
            with open('summoners.txt', 'w') as f:
                for item in summoners:
                    f.write("%s\n" % item)
            j = 0
        j += 1
        
# Save summoners to file
with open('../input/summoners.txt', 'w') as f:
    for item in summoners:
        f.write("%s\n" % item)