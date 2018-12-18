from minimax.draft import Draft
from minimax.tree import Tree
from heuristics.heuristics import alphabetic
from heuristics.heuristics import valuation






game = Draft(Tree(valuation), Tree(valuation), 2, 2)

choice = input("Choose red side or blue side to draft from, or auto to have "
               "computer do both sides, " "by entering 'red', 'blue', or 'auto:")

if choice == "blue":
    while not game.isTerminal():
        if game.isBlueBan():
            champion = input("Choose a champion to ban:")
        elif game.isBluePick():
            champion = input("Choose a champion to pick:")
        else:
            champion = game.getMove()

        game.makeMove(champion)

        game.printDraft()
elif choice == "red":
    while not game.isTerminal():
        if game.isRedBan():
            champion = input("Choose a champion to ban:")
        elif game.isRedPick():
            champion = input("Choose a champion to pick:")
        else:
            champion = game.getMove()

        game.makeMove(champion)

        game.printDraft()

else:
    while not game.isTerminal():
        champion = game.getMove()
        game.makeMove(champion)
        game.printDraft()