from MCTS.draft import Draft
from heuristics.heuristics import alphabetic, valuation


game = Draft(valuation, 1500, 1.41)

choice = input("Choose red side or blue side to draft from, or auto to have "
               "computer do both sides, " "by entering 'red', 'blue', or 'auto:")

if choice == "blue":
    while not game.is_terminal():
        if game.isBlueBan():
            champion = input("Choose a champion to ban:")
        elif game.isBluePick():
            champion = input("Choose a champion to pick:")
        else:
            champion = game.getMove()

        game.makeMove(champion)

        game.printDraft()
elif choice == "red":
    while not game.is_terminal():
        if game.isRedBan():
            champion = input("Choose a champion to ban:")
        elif game.isRedPick():
            champion = input("Choose a champion to pick:")
        else:
            champion = game.getMove()

        game.makeMove(champion)

        game.printDraft()

else:
    while not game.is_terminal():
        champion = game.getMove()
        game.makeMove(champion)
        game.printDraft()