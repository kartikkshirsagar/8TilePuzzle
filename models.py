class Board:
    def __init__(self, _config):
        self.config = _config  # config should be a 3*3 matrix
        self.parent = None
        self.move = None

    def print(self):
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.config]))
        # print("Move played: ",self.move)
        print("\n")

    def __eq__(self,other):
        if isinstance(other,Board):
            return self.config == other.config
        return False
    def __hash__(self):
        return hash(self.config)
    def getNeighbours(self):
        ret_list = []
        gap = (0, 0)
        for i in range(3):
            for j in range(3):
                if self.config[i][j] == "_":
                    gap = (i, j)
        if gap[0] > 0:
            newConf = [list(row[:]) for row in self.config]
            newConf[gap[0]][gap[1]] = newConf[gap[0]-1][gap[1]]
            newConf[gap[0]-1][gap[1]] = "_"
            newConft = tuple(tuple(row[:]) for row in newConf)
            board = Board(newConft)
            board.parent = self
            board.move = "up" 
            ret_list.append(board)
        if gap[0] < 2:
            newConf = [list(row[:]) for row in self.config]
            newConf[gap[0]][gap[1]] = newConf[gap[0]+1][gap[1]]
            newConf[gap[0]+1][gap[1]] = "_"
            newConft = tuple(tuple(row[:]) for row in newConf)
            board = Board(newConft)
            board.parent = self
            board.move = "down" 
            ret_list.append(board)
        if gap[1] > 0:
            newConf = [list(row[:]) for row in self.config]
            newConf[gap[0]][gap[1]] = newConf[gap[0]][gap[1]-1]
            newConf[gap[0]][gap[1]-1] = "_"
            newConft = tuple(tuple(row[:]) for row in newConf)
            board = Board(newConft)
            board.parent = self
            board.move = "left" 
            ret_list.append(board)
        if gap[1] < 2:
            newConf = [list(row[:]) for row in self.config]
            newConf[gap[0]][gap[1]] = newConf[gap[0]][gap[1]+1]
            newConf[gap[0]][gap[1]+1] = "_"
            newConft = tuple(tuple(row[:]) for row in newConf)
            board = Board(newConft)
            board.parent = self
            board.move = "right" 
            ret_list.append(board)
        return ret_list
