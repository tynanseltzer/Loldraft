from input.names import number
from input.names import beliefs
from input.names import nameList
from itertools import permutations, combinations
import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb
import numpy as np

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



def train():
    data = pd.read_csv("input/long_form_drafts.csv", header=None)
    X = data.loc[:, :281]
    Y = data.loc[:, 282]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0,
                                                        random_state=182)
    model = xgb.XGBClassifier()
    model.fit(X_train, y_train)
    return model

def transform(blueTeam, redTeam):
    '''
    
    :param blueTeam:
    Some list length 5 of form ["Galio", "Irelia"...]
    :param redTeam:
    Same as above
    :return:
    Length 282 vector one hot encoded
    '''
    champion_names = nameList
    vector = [0] * 282
    for champ in blueTeam:
        id = champion_names.index(champ)
        vector[id] = 1
    for champ in redTeam:
        id = champion_names.index(champ)
        vector[id+141] = 1
        
    return vector

def amateur(game):
    vector = transform(game.blueTeam, game.redTeam)
    array = np.asarray(vector)
    array = array.reshape((1,282))
    array = pd.DataFrame(data=array, index=[0], columns=range(282))
    values = game.model.predict_proba(array)
    return values[0][1] - values[0][0]
