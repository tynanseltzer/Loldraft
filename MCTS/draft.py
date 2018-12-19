# This is very similar to the draft class in minimax, but has slightly different
# structure
# to agree with the mcts library
from input.names import nameList
from copy import deepcopy
from heuristics.heuristics import alphabetic, valuation, amateur, train
from mcts.graph import (StateNode)
from mcts.mcts import *
import mcts.tree_policies as tree_policies
import mcts.default_policies as default_policies
import mcts.backups as backups


class Draft:
    def __init__(self, heuristic, rolloutNumber, banditC):
        self.blueTeam = []
        self.redTeam = []
        self.blueBans = []
        self.redBans = []
        self.actionCounter = 0
        self.heuristic = heuristic
        if self.heuristic == amateur:
            self.model = train()
        self.actions = self.getPossibleActions()
        self.mcts = MCTS(tree_policy=tree_policies.UCB1(c=banditC),
            default_policy=default_policies.random_terminal_roll_out,
                backup=backups.Bellman(gamma=.8))
        self.rolloutNumber = rolloutNumber


    def isBluePick(self):
        return self.actionCounter in [6, 9, 10, 17, 18]

    def isRedPick(self):
        return self.actionCounter in [7, 8, 11, 16, 19]

    def isBlueBan(self):
        return self.actionCounter in [0, 2, 4, 13, 15]

    def isRedBan(self):
        return self.actionCounter in [1, 3, 5, 12, 14]

    def getPossibleActions(self):
        return [champ for champ in nameList if champ not in self.blueBans and
                champ not in self.redBans and champ not in self.blueTeam and
                champ not in self.redTeam]


    def perform(self, action):
        newState = deepcopy(self)
        if newState.isBlueBan():
            newState.blueBans.append(action)
        elif newState. isRedBan():
            newState.redBans.append(action)
        elif newState.isBluePick():
            newState.blueTeam.append(action)
        else:
            newState.redTeam.append(action)

        newState.actionCounter += 1

        return newState


    def is_terminal(self):
        return self.actionCounter == 20


    def reward(self, parent, action):
        return self.heuristic(self)

    def getMove(self):
        if self.isBlueBan() or self.isBluePick():
            return self.mcts(StateNode(parent=None, state=self),
                             teamIsBlue=True, n=self.rolloutNumber)
        else:
            return self.mcts(StateNode(parent=None, state=self),
                             teamIsBlue=False, n=self.rolloutNumber)

    def makeMove(self, champion):
        if self.isBlueBan():
            self.blueBans.append(champion)
        elif self. isRedBan():
            self.redBans.append(champion)
        elif self.isBluePick():
            self.blueTeam.append(champion)
        else:
            self.redTeam.append(champion)

        self.actions = self.getPossibleActions()
        self.actionCounter += 1

    def printDraft(self):
        print("Blue Bans:", self.blueBans)
        print("Blue Picks:", self.blueTeam)
        print("Red Bans:", self.redBans)
        print("Red Picks", self.redTeam)

    def __hash__(self):
        return hash(tuple(self.blueBans + self.redBans + self.blueTeam + self.redTeam + [self.actionCounter]))

    def __eq__(self, other):
        return (self.redTeam == other.redTeam and self.blueTeam ==
        other.blueTeam and self.blueBans == other.blueBans and self.redBans == other.redBans and self.actionCounter == other.actionCounter)


class Action:
    def __init__(self, champ, counter):
        self.champion = champ

    def __str__(self):
        return self.champion

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                self.champion == other.champion )

    def __hash__(self):
        return hash(self.champion)




