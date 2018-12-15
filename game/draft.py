class Draft:
    def __init__(self, blueTree, redTree):
        # Storing what has been done so far
        self.blueTeam = []
        self.redTeam = []
        self.blueBans = []
        self.redBans = []
        self.actionCounter = 0
        self.blueTree = blueTree
        self.redTree = redTree

    # Given a champion selection, change the game state to reflect picking
    # or banning that champion
    def isBluePick(self):
        return self.actionCounter in [6, 9, 10, 17, 18]

    def isRedPick(self):
        return self.actionCounter in [7, 8, 11, 16, 19]

    def isBlueBan(self):
        return self.actionCounter in [0, 2, 4, 13, 15]

    def isRedBan(self):
        return self.actionCounter in [1, 3, 5, 12, 14]


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

    def isOver(self):
        return self.actionCounter == 20


    def getMove(self):
        if self.isBluePick() or self.isBlueBan():
            return self.blueTree.stepMaximize(self.blueTeam, self.redTeam,
                                              self.blueBans, self.redBans,
                                              self.actionCounter)
        else:
            return self.redTree.stepMaximize(self.blueTeam, self.redTeam,
                                              self.blueBans, self.redBans,
                                              self.actionCounter)

    def printDraft(self):
        print("Blue Bans:", self.blueBans)
        print("Blue Picks:", self.blueTeam)
        print("Red Bans:", self.redBans)
        print("Red Picks", self.redTeam)