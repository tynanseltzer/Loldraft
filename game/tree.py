from .names import number

class Tree:
    def __init__(self, heuristic):
        self.heurisic = heuristic



    def stepMaximize(self, game, depth, champion):
        if depth == 0 or game.isOver():
            return (self.heurisic(game), champion)
        # Who is maximizing
        if game.isBluePick() or game.isBlueBan():
            moveValue = (-99999, champion)

            for move in game.getLegalMoves():
                game.makeMove(move)
                futureMoveValue =
                moveValue = max(moveValue, self.stepMaximize(game, depth - 1, move))
                game.undoMove()
            return moveValue

        else:
            moveValue = (99999, champion)
            for move in game.getLegalMoves():
                game.makeMove(move)
                moveValue = min(moveValue, self.stepMaximize(game, depth - 1, move))
                game.undoMove()


            return moveValue