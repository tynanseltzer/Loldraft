from game.draft import Draft
from game.tree import Tree
from game.names import number
from game.heuristics import alphabetic





game = Draft(Tree(alphabetic), Tree(alphabetic), 4, 4)

choice = input("Choose red side or blue side to draft from, or auto to have "
               "computer do both sides, " "by entering 'red', 'blue', or 'auto:")

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
elif choice == "red":
    while not game.isOver():
        if game.isRedBan():
            champion = input("Choose a champion to ban:")
        elif game.isRedPick():
            champion = input("Choose a champion to pick:")
        else:
            champion = game.getMove()

        game.makeMove(champion)

        game.printDraft()

else:
    while not game.isOver():
        champion = game.getMove()
        game.makeMove(champion)
        game.printDraft()