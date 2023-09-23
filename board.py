# board

from header import MARK, SIZE, PATHS

class Board:
    def __init__(self, other=None) -> None:
        self.m_board = [MARK.EMPTY] * SIZE * SIZE
        if other:
            self.m_board = other.m_board.copy()

    def __getitem__(self, pos):
        return self.m_board[pos]
    
    def __setitem__(self, pos, value):
        self.m_board[pos] = value
    
    def check(self):
        for path in PATHS:
            if(self.m_board[path[0]]==MARK.EMPTY):
                continue
            elif(self.m_board[path[0]]==self.m_board[path[1]]==self.m_board[path[2]]):
                return self.m_board[path[0]]
        
        return MARK.EMPTY
    

    def has_empty(self):
        return any(cell == MARK.EMPTY for cell in self.m_board)
    
    def reset(self):
        self.m_board = [MARK.EMPTY] * SIZE * SIZE
