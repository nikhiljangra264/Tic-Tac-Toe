from enum import Enum

class MARK(Enum):
    EMPTY = 0
    PLAYER_1 = 1
    PLAYER_2 = 2

SIZE = 3
PATHS = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]