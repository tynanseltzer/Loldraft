from game.draft import Draft
from game.tree import Tree
from game.names import number

def isLegalPick(game, pick):
    return (pick not in game.blueTeam and pick not in game.redTeam and
            pick not in game.bans and pick in number.keys())


game = Draft(Tree(0), Tree(0))

choice = input("Choose red side or blue side, by entering 'red' or 'blue':")

if choice == "blue":
    while not game.isOver():
        if game.isBlueBan():
            champion = input("Choose a champion to ban:")
        elif game.isBluePick():
            champion = input("Choose a champion to pick:")
        else:
            champion = game.getMove()

        game.makeMove(champion)

        game.printDraft()
else:
    while not game.isOver():
        if game.isRedBan():
            champion = input("Choose a champion to ban:")
        elif game.isRedPick():
            champion = input("Choose a champion to pick:")
        else:
            champion = game.getMove()

        game.makeMove(champion)

        game.printDraft()

