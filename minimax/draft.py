from input.names import nameList
from heuristics.heuristics import alphabetic
from heuristics.heuristics import valuation
class Draft:
    def __init__(self, blueTree, redTree, blueDepth, redDepth):
        # Storing what has been done so far
        self.blueTeam = []
        self.redTeam = []
        self.blueBans = []
        self.redBans = []
        self.actionCounter = 0
        self.blueTree = blueTree
        self.redTree = redTree
        self.blueDepth = blueDepth
        self.redDepth = redDepth
        # A testing parameter, to judge efficiency
        self.num_nodes = 0

    # Given a champion selection, change the minimax state to reflect picking
    # or banning that champion
    def isBluePick(self):
        return self.actionCounter in [6, 9, 10, 17, 18]

    def isRedPick(self):
        return self.actionCounter in [7, 8, 11, 16, 19]

    def isBlueBan(self):
        return self.actionCounter in [0, 2, 4, 13, 15]

    def isRedBan(self):
        return self.actionCounter in [1, 3, 5, 12, 14]


    # Actually make the move
    def makeMove(self, champion):
        if self.isBlueBan():
            self.blueBans.append(champion)
        elif self. isRedBan():
            self.redBans.append(champion)
        elif self.isBluePick():
            self.blueTeam.append(champion)
        else:
            self.redTeam.append(champion)

        self.actionCounter += 1

    def isTerminal(self):
        return self.actionCounter == 20


    def getMove(self):
        if self.isBluePick() or self.isBlueBan():
            return self.blueTree.stepMaximize(self, self.blueDepth)[1]
        else:
            return self.redTree.stepMaximize(self, self.redDepth)[1]

    def undoMove(self):
        if self.actionCounter in [7, 10, 11, 18, 19]:
            champion = self.blueTeam[-1]
            self.blueTeam = self.blueTeam[:-1]
        elif self.actionCounter in [8, 9, 12, 17, 20]:
            champion = self.redTeam[-1]
            self.redTeam = self.redTeam[:-1]
        elif self.actionCounter in [1, 3, 5, 14, 16]:
            champion = self.blueBans[-1]
            self.blueBans = self.blueBans[:-1]
        elif self.actionCounter in [2, 4, 6, 13, 15]:
            champion = self.redBans[-1]
            self.redBans = self.redBans[:-1]

        self.actionCounter -= 1

    def getLegalMoves(self):
        return [champ for champ in nameList if champ not in self.blueBans and
                champ not in self.redBans and champ not in self.blueTeam and
                champ not in self.redTeam]

    def printDraft(self):
        print("Blue Bans:", self.blueBans)
        print("Blue Picks:", self.blueTeam)
        print("Red Bans:", self.redBans)
        print("Red Picks", self.redTeam)
        print(valuation(self))