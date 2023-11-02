# breakthroughgame.py
# Andrew Poock
""" Implementation of Breakthrough game rules

Initial Board: White moves first.

    0   1   2   3   4   5   6   7
  +---+---+---+---+---+---+---+---+
0 | B | B | B | B | B | B | B | B |
  +---+---+---+---+---+---+---+---+
1 | B | B | B | B | B | B | B | B |
  +---+---+---+---+---+---+---+---+
2 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
3 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
4 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
5 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
6 | W | W | W | W | W | W | W | W |
  +---+---+---+---+---+---+---+---+
7 | W | W | W | W | W | W | W | W |
  +---+---+---+---+---+---+---+---+
"""

from pprint import pprint

# Constants to identify pieces and players
BLACK = "BLACK"
WHITE = "WHITE"


class BreakthroughGame:    
    """Implementation of the rules of breakthrough.  Assumes an 8x8 board
    with rows and columns numbered 0--7. A location on the board is
    given as a pair: (row, column). Black pawns start on rows 0 and 1 while
    white pawns start on rows 6 and 7.
    """

    class Board:
      def __init__(self):
        self.locations = [[None for _ in range(8)] for x in range(8)]
        self.set_board()
      
      def reset(self):
        self.locations = [[None for _ in range(8)] for x in range(8)]
        self.set_board()

      def set_board(self):
        for i in range(8):
          self.locations[0][i] = BLACK
          self.locations[1][i] = BLACK
          self.locations[6][i] = WHITE
          self.locations[7][i] = WHITE

    def __init__(self):
      self.board = self.Board()
      self.turn = WHITE

    def get_piece_at(self, loc):
        """return owner of piece at loc (row, column)
        pre: loc is a valid (row,col) board location
        post: result in [BLACK, WHITE, None]
        """
        return self.board.locations[loc[0]][loc[1]]

    def get_player_in_turn(self):
        """ return the player that is in turn, i.e. allowed to move.
        post: result in [BLACK, WHITE]
        """
        return self.turn

    def get_winner(self):
        """return the winner of the game or None, if game is still in progress
        post: result in [BLACK, WHITE, None]
        """
        if WHITE in self.board.locations[0]:
          return WHITE
        if BLACK in self.board.locations[7]:
          return BLACK
        return None

    def is_valid_move(self, fromloc, toloc):
        """validate a move from fromLoc to toLoc
        pre: fromloc and toloc are valid (row, column) board locations
        post: returns True if move is valid, False otherwise
        """
        if 8 in fromloc or 8 in toloc:
          return False

        fx, fy = fromloc
        tx, ty = toloc
        dx = abs(fx-tx)

        if self.turn == WHITE:
          if fy+1 == ty:
            if dx == 0 and self.board.locations[tx][ty] == None:
              return True
            if dx == 1 and self.board.locations[tx][ty] != WHITE:
              return True

        if self.turn == BLACK:
          if fy-1 == ty:
            if dx == 0 and self.board.locations[tx][ty] == None:
              return True
            if dx == 1 and self.board.locations[tx][ty] != BLACK:
              return True

        return False


    def move(self, fromloc, toloc):
        """ move piece from fromloc to toloc
        pre: fromloc and toloc are valid (row, column) board locations
             and there is a piece at fromloc
        post: the move is performed
        note: move does not have to be valid
        """
        fx, fy = fromloc
        tx, ty = toloc
        piece = self.get_piece_at(fromloc)
        self.board.locations[fx][fy] = None
        self.board.locations[tx][ty] = piece
        if self.turn == WHITE:
          self.turn = BLACK
        if self.turn == BLACK:
          self.turn = WHITE
    
    def _print(self):
      pprint(self.board.locations)
