from input.names import number
from input.names import beliefs
from itertools import permutations, combinations

def alphabetic(game):
    return sum([number[champ] for champ in game.blueTeam]) - \
           sum([number[champ] for champ in game.redTeam])


#Helper function

def teamValue(order):
    roles = (combinations(range(5), len(order)))
    best = 0
    for roleset in roles:
        best = max(best, sum([beliefs[order[i]][roleset[i]] for i in range(len(order))]))
    return best


# Another Heuristic
def valuation(game):
    return max(map(teamValue, list(permutations(game.blueTeam)))) - \
        max(map(teamValue, list(permutations(game.redTeam))))