# testbreakthroughgame.py
# Andrew Poock
""" Tests for Implementation of Breakthrough game rules

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

import unittest
from breakthroughgame import BreakthroughGame, BLACK, WHITE


class TestBreakthrough(unittest.TestCase):

    def setUp(self):
      self.btg = BreakthroughGame()

    # board setup tests
    def test_index_8_is_out_of_range(self):
      with self.assertRaises(IndexError):
        self.btg.get_piece_at((8,0))
      with self.assertRaises(IndexError):
        self.btg.get_piece_at((8,8))
      with self.assertRaises(IndexError):
        self.btg.get_piece_at((0,8))

    def test_row_one_and_two_are_black(self):
      for i in range(2):
        for piece in self.btg.board.locations[i]:
          self.assertEqual(BLACK, piece)

    def test_row_six_and_seven_are_white(self):
      for i in range(6,7):
        for piece in self.btg.board.locations[i]:
          self.assertEqual(WHITE, piece)

    def test_empty_rows(self):
      for i in range(2,6):
        for piece in self.btg.board.locations[i]:
          self.assertEqual(None, piece)

    # first move test
    def test_white_moves_first(self):
      self.assertEqual(self.btg.turn, WHITE)

    # turn switch
    def test_black_moves_second(self):
      self.btg.move((6,6), (5,5))
      #self.assertEqual(self.btg.turn, BLACK)
      pass

    # get piece test
    def test_get_piece(self):
      self.assertEqual(WHITE, self.btg.get_piece_at((7,7)))
      self.assertEqual(BLACK, self.btg.get_piece_at((0,1)))
      self.assertEqual(None, self.btg.get_piece_at((4,4)))
      self.assertEqual(None, self.btg.get_piece_at((5,3)))

    # winner tests
    def test_get_winner_white(self):
      for i in range(8):
          self.btg.move((7,i),(0,i))
          self.assertEqual(WHITE, self.btg.get_winner())
          self.btg.board.reset()

    def test_get_winner_black(self):
      for i in range(8):
          self.btg.move((0,i),(7,i))
          self.assertEqual(BLACK, self.btg.get_winner())
          self.btg.board.reset()
    
    def test_rows_1_to_6_no_winner(self):
      self.assertEqual(None, self.btg.get_winner())

    # board reset test
    def test_board_resets(self):
      pass

    #move test
    def test_move(self):
      self.btg.move((6,6), (5,5))
      self.assertEqual(WHITE, self.btg.get_piece_at((5,5)))
      self.assertEqual(None, self.btg.get_piece_at((6,6)))


if __name__ == "__main__":
    unittest.main()
