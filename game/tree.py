from .names import number

class Tree:
    def __init__(self, heuristic):
        self.heurisic = heuristic



    def stepMaximize(self, game, depth, alpha = -99999, beta=99999):
        if depth == 0 or game.isOver():
            game.num_nodes += 1
            return (self.heurisic(game), "Garen")
        # Who is maximizing
        if game.isBluePick() or game.isBlueBan():
            moveValue = (-99999, "Garen")

            for move in game.getLegalMoves():
                game.makeMove(move)
                futureMoveValue = self.stepMaximize(game, depth - 1)
                # Note that we combine the tuples. The value is what the future
                # returns, but the actual champion is the move.
                if futureMoveValue[0] > moveValue[0]:
                    moveValue = (futureMoveValue[0], move)

                game.undoMove()
            return moveValue

        else:
            moveValue = (99999, "Garen")
            for move in game.getLegalMoves():
                game.makeMove(move)
                futureMoveValue = self.stepMaximize(game, depth - 1)
                if futureMoveValue[0] < moveValue[0]:
                    moveValue = (futureMoveValue[0], move)
                game.undoMove()


            return moveValue