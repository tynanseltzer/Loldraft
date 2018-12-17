from minimax.names import number

def alphabetic(game):
    return sum([number[champ] for champ in game.blueTeam]) - \
           sum([number[champ] for champ in game.redTeam])
