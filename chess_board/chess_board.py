from chess_board.cell import Cell

class ChessBoard:
    def __init__(self, length=10):
        self.length = length
        self.cells = [[Cell() for i in range(self.length)] for i in range(self.length)]

    def get_cell_status(self, x, y):
        """get the status of cell with coordinates x and y"""
        tx = x
        ty = y
        if tx >= self.length:
            tx -= self.length
        if ty >= self.length:
            ty -= self.length
        return self.cells[tx][ty].status

    def get_status_around(self, x, y):
        """get the sum of cells nearby"""
        nearby = [self.get_cell_status(x + tx, y + ty) for tx in [-1, 0, 1] for ty in [-1, 0, 1]
                  if not (tx == 0 and ty == 0)]
        cnt = sum(nearby)
        return cnt

    def update_cells_status(self):
        """update all cells status"""
        for i in range(self.length):
            for j in range(self.length):
                self.cells[i][j].update()

    def update_chess_board(self):
        """update the whole chessboard and the status of the cell"""
        for i in range(self.length):
            for j in range(self.length):
                cnt_around = self.get_status_around(i, j)
                if cnt_around == 3:
                    self.cells[i][j].next_status = True
                elif cnt_around < 2 or cnt_around > 3:
                    self.cells[i][j].next_status = False
                else:
                    self.cells[i][j].next_status = self.cells[i][j].status
        self.update_cells_status()

    def show_cell_status(self):
        """Show the status of all cells"""
        for i in range(self.length):
            for j in range(self.length):
                if self.cells[i][j].status:
                    print('1\t', end='')
                else:
                    print('0\t', end='')
            print('\n')

