# __minimax algo impelmentation

from header import MARK, SIZE
from board import Board

class engine:
    def __init__(self, player : MARK, opponent : MARK,  depth : int) -> None:
        self.depth = depth
        self.player = player
        self.opponent = opponent

    def __minimax(self, turn : bool, board : Board, depth: int):
        if board.check() != MARK.EMPTY:
            if turn:
                return (-1, None)
            else:
                return (1, None)
        elif not board.has_empty() or depth == 0:
            return (0, None)
        
        elif turn:
            best = (-2, None)
            for i in range(SIZE * SIZE):
                if board[i] == MARK.EMPTY:
                    board[i] = self.player
                    value = self.__minimax(not turn, Board(board), depth-1)[0]
                    if value > best[0]:
                        best = (value, i)
                    board[i] = MARK.EMPTY
            return best
        else:
            best = (2, None)
            for i in range(SIZE * SIZE ):
                if board[i] == MARK.EMPTY:
                    board[i] = self.opponent
                    value = self.__minimax(not turn, Board(board), depth-1)[0]
                    if value < best[0]:
                        best = (value, i)
                    board[i]=MARK.EMPTY
            return best

    def run(self, board: Board, turn : MARK):
        return self.__minimax(turn==self.player, Board(board), self.depth)[1]
    

