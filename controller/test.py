from chess_board import chess_board
from gui import display
import profile

#  test temp work
def run():
    chess_board_one = chess_board.ChessBoard()
    gui = display.GUI(chess_board_one)
    gui.display()

if __name__ == "__main__":
    profile.run("run()")
#  pygame shit
