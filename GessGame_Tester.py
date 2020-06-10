import unittest
from GessGame import *


class TestGessGame(unittest.TestCase):
    """
    Contains unit tests for GessGame.py
    The tests for each class are separated by docstrings.
    The tests for each method area separated by their own comments. The tests for each method starts at 1,
    to help track potential future implementations of tests.
    """

    """
    TESTS RELATING TO STONE CLASS:
    """
    # Tests relating to get_color.
    def test_1_stone_get_color(self):
        # Testing stone's get color method.
        stone = Stone("BLACK", "b2")
        output = stone.get_color()

        self.assertEqual(output, "BLACK")

    # Tests relating to get_coordinate.
    def test_1_stone_get_coordinate(self):
        # Testing stone's get coordinate method.
        stone = Stone("BLACK", "b2")
        output = stone.get_coordinate()

        self.assertEqual(output, "b2")

    # Tests relating to change_coordinate.
    def test_1_stone_change_coordinate(self):
        # Testing stone's change coordinate method.
        stone = Stone("BLACK", "b2")
        stone.change_coordinate("c3")
        output = stone.get_coordinate()

        self.assertEqual(output, "c3")

    """
    TESTS RELATING TO PIECE CLASS:
    """
    # Tests relating to is_piece_valid.
    def test_1_is_piece_valid(self):
        # Testing validity of blank piece.
        current_player = "BLACK"
        piece = Piece("b2", [["", "", ""], ["", "", ""], ["", "", ""]])
        output = piece.is_piece_valid(current_player)

        self.assertEqual(output, False)

    def test_2_is_piece_valid(self):
        # Testing validity of a legal piece.
        current_player = "BLACK"
        stone_1 = Stone("BLACK", "b2")
        stone_2 = Stone("BLACK", "c3")
        piece = Piece("b2", [["", "", ""], ["", stone_1, ""], ["", "", stone_2]])
        output = piece.is_piece_valid(current_player)

        self.assertEqual(output, True)

    def test_3_is_piece_valid(self):
        # Testing validity of an illegal piece with multiple stone colors.
        current_player = "BLACK"
        stone_1 = Stone("BLACK", "b2")
        stone_2 = Stone("WHITE", "c3")
        piece = Piece("b2", [["", "", ""], ["", stone_1, ""], ["", "", stone_2]])
        output = piece.is_piece_valid(current_player)

        self.assertEqual(output, False)

    def test_4_is_piece_valid(self):
        # Testing validity of piece with only a stone in its center.
        current_player = "BLACK"
        stone_1 = Stone("BLACK", "b2")
        piece = Piece("b2", [["", "", ""], ["", stone_1, ""], ["", "", ""]])
        output = piece.is_piece_valid(current_player)

        self.assertEqual(output, False)

    def test_5_is_piece_valid(self):
        # Testing validity of piece with its center off the board(illegal).
        current_player = "BLACK"
        stone_1 = Stone("BLACK", "b1")
        piece_1 = Piece("b1", [["", "", ""], ["", stone_1, ""], ["", "", ""]])
        output_1 = piece_1.is_piece_valid(current_player)
        stone_2 = Stone("BLACK", "a6")
        piece_2 = Piece("a6", [["", "", ""], ["", stone_1, ""], ["", "", ""]])
        output_2 = piece_2.is_piece_valid(current_player)
        stone_3 = Stone("BLACK", "k20")
        piece_3 = Piece("k20", [["", "", ""], ["", stone_1, ""], ["", "", ""]])
        output_3 = piece_3.is_piece_valid(current_player)
        stone_4 = Stone("BLACK", "t9")
        piece_4 = Piece("t9", [["", "", ""], ["", stone_1, ""], ["", "", ""]])
        output_4 = piece_4.is_piece_valid(current_player)
        output = [output_1, output_2, output_3, output_4]

        self.assertEqual(output, [False, False, False, False])

    # Tests relating to get_piece_directions.
    def test_1_get_piece_directions(self):
        # Testing the directions a piece can move.
        stone_1 = Stone("BLACK", "b1")
        stone_2 = Stone("BLACK", "c2")
        stone_3 = Stone("BLACK", "c3")
        piece = Piece("b2", [["", stone_1, ""], ["", "", stone_2], ["", "", stone_3]])
        output = piece.get_piece_directions()

        self.assertEqual(output, ["N", "E", "SE"])

    # Tests relating to get_piece_range.
    def test_1_get_piece_range(self):
        # Testing when the range of a piece is 3.
        stone_1 = Stone("BLACK", "b1")
        stone_2 = Stone("BLACK", "c2")
        stone_3 = Stone("BLACK", "c3")
        piece = Piece("b2", [["", stone_1, ""], ["", "", stone_2], ["", "", stone_3]])
        output = piece.get_piece_range()

        self.assertEqual(output, 3)

    def test_2_get_piece_range(self):
        # Testing when the rnage of a piece is unlimited (set as 20).
        stone_1 = Stone("BLACK", "b2")
        stone_2 = Stone("BLACK", "c3")
        piece = Piece("b2", [["", "", ""], ["", stone_1, ""], ["", "", stone_2]])
        output = piece.get_piece_range()

        self.assertEqual(output, 20)

    # Tests relating to get_direction_needed.
    def test_1_get_direction_needed(self):
        # Testing when the end point is an illegal direction (not directly in cardinal path).
        stone_1 = Stone("BLACK", "b2")
        stone_2 = Stone("BLACK", "c3")
        piece = Piece("b2", [["", "", ""], ["", stone_1, ""], ["", "", stone_2]])
        output = piece.get_direction_needed("c4")

        self.assertEqual(output, False)
        
    def test_2_get_direction_needed(self):
        # Testing when the end point is the same as the starting point.
        stone_1 = Stone("BLACK", "b2")
        stone_2 = Stone("BLACK", "c3")
        piece = Piece("b2", [["", "", ""], ["", stone_1, ""], ["", "", stone_2]])
        output = piece.get_direction_needed("b2")

        self.assertEqual(output, False)

    def test_3_get_direction_needed(self):
        # Testing when the end point is north of the piece.
        stone_1 = Stone("BLACK", "c3")
        stone_2 = Stone("BLACK", "d4")
        piece = Piece("c3", [["", "", ""], ["", stone_1, ""], ["", "", stone_2]])
        output = piece.get_direction_needed("c4")

        self.assertEqual(output, "N")

    def test_4_get_direction_needed(self):
        # Testing when the end point is south of the piece.
        stone_1 = Stone("BLACK", "c3")
        stone_2 = Stone("BLACK", "d4")
        piece = Piece("c3", [["", "", ""], ["", stone_1, ""], ["", "", stone_2]])
        output = piece.get_direction_needed("c2")

        self.assertEqual(output, "S")

    def test_5_get_direction_needed(self):
        # Testing when the end point is east of the piece.
        stone_1 = Stone("BLACK", "c3")
        stone_2 = Stone("BLACK", "d4")
        piece = Piece("c3", [["", "", ""], ["", stone_1, ""], ["", "", stone_2]])
        output = piece.get_direction_needed("d3")

        self.assertEqual(output, "E")

    def test_6_get_direction_needed(self):
        # Testing when the end point is west of the piece.
        stone_1 = Stone("BLACK", "c3")
        stone_2 = Stone("BLACK", "d4")
        piece = Piece("c3", [["", "", ""], ["", stone_1, ""], ["", "", stone_2]])
        output = piece.get_direction_needed("b3")

        self.assertEqual(output, "W")

    def test_7_get_direction_needed(self):
        # Testing when the end point is northeast of the piece.
        stone_1 = Stone("BLACK", "c3")
        stone_2 = Stone("BLACK", "d4")
        piece = Piece("c3", [["", "", ""], ["", stone_1, ""], ["", "", stone_2]])
        output = piece.get_direction_needed("d4")

        self.assertEqual(output, "NE")

    def test_8_get_direction_needed(self):
        # Testing when the end point is northwest of the piece.
        stone_1 = Stone("BLACK", "c3")
        stone_2 = Stone("BLACK", "d4")
        piece = Piece("c3", [["", "", ""], ["", stone_1, ""], ["", "", stone_2]])
        output = piece.get_direction_needed("b4")

        self.assertEqual(output, "NW")

    def test_9_get_direction_needed(self):
        # Testing when the end point is southeast of the piece.
        stone_1 = Stone("BLACK", "c3")
        stone_2 = Stone("BLACK", "d4")
        piece = Piece("c3", [["", "", ""], ["", stone_1, ""], ["", "", stone_2]])
        output = piece.get_direction_needed("d2")

        self.assertEqual(output, "SE")

    def test_10_get_direction_needed(self):
        # Testing when the end point is southwest of the piece.
        stone_1 = Stone("BLACK", "c3")
        stone_2 = Stone("BLACK", "d4")
        piece = Piece("c3", [["", "", ""], ["", stone_1, ""], ["", "", stone_2]])
        output = piece.get_direction_needed("b2")

        self.assertEqual(output, "SW")

    # Tests relating to get_range_needed.
    def test_1_get_range_needed(self):
        # Testing range when the end point is north of the piece.
        stone_1 = Stone("BLACK", "c3")
        stone_2 = Stone("BLACK", "d4")
        piece = Piece("c3", [["", "", ""], ["", stone_1, ""], ["", "", stone_2]])
        output = piece.get_range_needed("c4")

        self.assertEqual(output, 1)

    def test_2_get_range_needed(self):
        # Testing range when the end point is south of the piece.
        stone_1 = Stone("BLACK", "c3")
        stone_2 = Stone("BLACK", "d4")
        piece = Piece("c3", [["", "", ""], ["", stone_1, ""], ["", "", stone_2]])
        output = piece.get_range_needed("c2")

        self.assertEqual(output, 1)

    def test_3_get_range_needed(self):
        # Testing range when the end point is east of the piece.
        stone_1 = Stone("BLACK", "c3")
        stone_2 = Stone("BLACK", "d4")
        piece = Piece("c3", [["", "", ""], ["", stone_1, ""], ["", "", stone_2]])
        output = piece.get_range_needed("d3")

        self.assertEqual(output, 1)

    def test_4_get_range_needed(self):
        # Testing range when the end point is west of the piece.
        stone_1 = Stone("BLACK", "c3")
        stone_2 = Stone("BLACK", "d4")
        piece = Piece("c3", [["", "", ""], ["", stone_1, ""], ["", "", stone_2]])
        output = piece.get_range_needed("b3")

        self.assertEqual(output, 1)

    def test_5_get_range_needed(self):
        # Testing range when the end point is northeast of the piece.
        stone_1 = Stone("BLACK", "c3")
        stone_2 = Stone("BLACK", "d4")
        piece = Piece("c3", [["", "", ""], ["", stone_1, ""], ["", "", stone_2]])
        output = piece.get_range_needed("d4")

        self.assertEqual(output, 1)

    def test_6_get_range_needed(self):
        # Testing range when the end point is northwest of the piece.
        stone_1 = Stone("BLACK", "c3")
        stone_2 = Stone("BLACK", "d4")
        piece = Piece("c3", [["", "", ""], ["", stone_1, ""], ["", "", stone_2]])
        output = piece.get_range_needed("b4")

        self.assertEqual(output, 1)

    def test_7_get_range_needed(self):
        # Testing range when the end point is southeast of the piece.
        stone_1 = Stone("BLACK", "c3")
        stone_2 = Stone("BLACK", "d4")
        piece = Piece("c3", [["", "", ""], ["", stone_1, ""], ["", "", stone_2]])
        output = piece.get_range_needed("d2")

        self.assertEqual(output, 1)

    def test_8_get_range_needed(self):
        # Testing range when the end point is southwest of the piece.
        stone_1 = Stone("BLACK", "c3")
        stone_2 = Stone("BLACK", "d4")
        piece = Piece("c3", [["", "", ""], ["", stone_1, ""], ["", "", stone_2]])
        output = piece.get_range_needed("b2")

        self.assertEqual(output, 1)

    # Test relating to can_piece_move_to.
    def test_1_can_piece_move_to(self):
        # Trying to move a piece to an illegal spot.
        stone_1 = Stone("BLACK", "c3")
        stone_2 = Stone("BLACK", "d4")
        piece = Piece("c3", [["", "", ""], ["", stone_1, ""], ["", "", stone_2]])
        output = piece.can_piece_move_to("e2")

        self.assertEqual(output, False)

    def test_2_can_piece_move_to(self):
        # Trying to move the piece to its starting spot.
        stone_1 = Stone("BLACK", "c3")
        stone_2 = Stone("BLACK", "d4")
        piece = Piece("c3", [["", "", ""], ["", stone_1, ""], ["", "", stone_2]])
        output = piece.can_piece_move_to("c3")

        self.assertEqual(output, False)

    def test_3_can_piece_move_to(self):
        # Trying to move a piece (range 3 and direction north) to end point in range.
        stone_1 = Stone("BLACK", "f5")
        piece = Piece("f6", [["", stone_1, ""], ["", "", ""], ["", "", ""]])
        output = piece.can_piece_move_to("f9")

        self.assertEqual(output, True)

    def test_4_can_piece_move_to(self):
        # Trying to move a piece (range unlimited and direction north) to end point in range.
        stone_1 = Stone("BLACK", "f5")
        stone_2 = Stone("BLACK", "f6")
        piece = Piece("f6", [["", stone_1, ""], ["", stone_2, ""], ["", "", ""]])
        output = piece.can_piece_move_to("f10")

        self.assertEqual(output, True)

    def test_5_can_piece_move_to(self):
        # Trying to move a piece (range 3 and direction north) to end point out of range.
        stone_1 = Stone("BLACK", "f5")
        piece = Piece("f6", [["", stone_1, ""], ["", "", ""], ["", "", ""]])
        output = piece.can_piece_move_to("f10")

        self.assertEqual(output, False)

    def test_6_can_piece_move_to(self):
        # Trying to move a piece (range 3 and direction south) to end point in range.
        stone_1 = Stone("BLACK", "f7")
        piece = Piece("f6", [["", "", ""], ["", "", ""], ["", stone_1, ""]])
        output = piece.can_piece_move_to("f3")

        self.assertEqual(output, True)

    def test_7_can_piece_move_to(self):
        # Trying to move a piece (range unlimited and direction south) to end point in range.
        stone_1 = Stone("BLACK", "f7")
        stone_2 = Stone("BLACK", "f6")
        piece = Piece("f6", [["", "", ""], ["", stone_2, ""], ["", stone_1, ""]])
        output = piece.can_piece_move_to("f2")

        self.assertEqual(output, True)

    def test_8_can_piece_move_to(self):
        # Trying to move a piece (range 3 and direction south) to end point out of range.
        stone_1 = Stone("BLACK", "f7")
        piece = Piece("f6", [["", "", ""], ["", "", ""], ["", stone_1, ""]])
        output = piece.can_piece_move_to("f2")

        self.assertEqual(output, False)

    def test_9_can_piece_move_to(self):
        # Trying to move a piece (range 3 and direction east) to end point in range.
        stone_1 = Stone("BLACK", "g6")
        piece = Piece("f6", [["", "", ""], ["", "", stone_1], ["", "", ""]])
        output = piece.can_piece_move_to("j5")

        self.assertEqual(output, False)

    def test_10_can_piece_move_to(self):
        # Trying to move a piece (range unlimited and direction east) to end point in range.
        stone_1 = Stone("BLACK", "g6")
        stone_2 = Stone("BLACK", "f6")
        piece = Piece("f6", [["", "", ""], ["", stone_2, stone_1], ["", "", ""]])
        output = piece.can_piece_move_to("j6")

        self.assertEqual(output, True)

    def test_11_can_piece_move_to(self):
        # Trying to move a piece (range 3 and direction east) to end point out of range.
        stone_1 = Stone("BLACK", "g6")
        piece = Piece("f6", [["", "", ""], ["", "", stone_1], ["", "", ""]])
        output = piece.can_piece_move_to("j6")

        self.assertEqual(output, False)

    def test_12_can_piece_move_to(self):
        # Trying to move a piece (range 3 and direction west) to end point in range.
        stone_1 = Stone("BLACK", "e6")
        piece = Piece("f6", [["", "", ""], [stone_1, "", ""], ["", "", ""]])
        output = piece.can_piece_move_to("c6")

        self.assertEqual(output, True)

    def test_13_can_piece_move_to(self):
        # Trying to move a piece (range unlimited and direction west) to end point in range.
        stone_1 = Stone("BLACK", "e6")
        stone_2 = Stone("BLACK", "f6")
        piece = Piece("f6", [["", "", ""], [stone_1, stone_2, ""], ["", "", ""]])
        output = piece.can_piece_move_to("b6")

        self.assertEqual(output, True)

    def test_14_can_piece_move_to(self):
        # Trying to move a piece (range 3 and direction west) to end point out of range.
        stone_1 = Stone("BLACK", "e6")
        piece = Piece("f6", [["", "", ""], [stone_1, "", ""], ["", "", ""]])
        output = piece.can_piece_move_to("b6")

        self.assertEqual(output, False)

    def test_15_can_piece_move_to(self):
        # Trying to move a piece (range 3 and direction northeast) to end point in range.
        stone_1 = Stone("BLACK", "g5")
        piece = Piece("f6", [["", "", stone_1], ["", "", ""], ["", "", ""]])
        output = piece.can_piece_move_to("i9")

        self.assertEqual(output, True)

    def test_16_can_piece_move_to(self):
        # Trying to move a piece (range 3 and direction northeast) to end point out of range.
        stone_1 = Stone("BLACK", "g5")
        stone_2 = Stone("BLACK", "f6")
        piece = Piece("f6", [["", "", stone_1], ["", stone_2, ""], ["", "", ""]])
        output = piece.can_piece_move_to("j10")

        self.assertEqual(output, True)

    def test_17_can_piece_move_to(self):
        # Trying to move a piece (range 3 and direction northeast) to end point out of range.
        stone_1 = Stone("BLACK", "g5")
        piece = Piece("f6", [["", "", stone_1], ["", "", ""], ["", "", ""]])
        output = piece.can_piece_move_to("j10")

        self.assertEqual(output, False)

    def test_18_can_piece_move_to(self):
        # Trying to move a piece (range 3 and direction northwest) to end point in range.
        stone_1 = Stone("BLACK", "e5")
        piece = Piece("f6", [[stone_1, "", ""], ["", "", ""], ["", "", ""]])
        output = piece.can_piece_move_to("c9")

        self.assertEqual(output, True)

    def test_19_can_piece_move_to(self):
        # Trying to move a piece (range unlimited and direction northwest) to end point in range.
        stone_1 = Stone("BLACK", "e5")
        stone_2 = Stone("BLACK", "f6")
        piece = Piece("f6", [[stone_1, "", ""], ["", stone_2, ""], ["", "", ""]])
        output = piece.can_piece_move_to("b10")

        self.assertEqual(output, True)

    def test_20_can_piece_move_to(self):
        # Trying to move a piece (range 3 and direction northwest) to end point out of range.
        stone_1 = Stone("BLACK", "e5")
        piece = Piece("f6", [[stone_1, "", ""], ["", "", ""], ["", "", ""]])
        output = piece.can_piece_move_to("b10")

        self.assertEqual(output, False)

    def test_21_can_piece_move_to(self):
        # Trying to move a piece (range 3 and direction southeast) to end point in range.
        stone_1 = Stone("BLACK", "g7")
        piece = Piece("f6", [["", "", ""], ["", "", ""], ["", "", stone_1]])
        output = piece.can_piece_move_to("i3")

        self.assertEqual(output, True)

    def test_22_can_piece_move_to(self):
        # Trying to move a piece (range unlimited and direction southeast) to end point in range.
        stone_1 = Stone("BLACK", "g7")
        stone_2 = Stone("BLACK", "f6")
        piece = Piece("f6", [["", "", ""], ["", stone_2, ""], ["", "", stone_1]])
        output = piece.can_piece_move_to("j2")

        self.assertEqual(output, True)

    def test_23_can_piece_move_to(self):
        # Trying to move a piece (range 3 and direction southeast) to end point out of range.
        stone_1 = Stone("BLACK", "g7")
        piece = Piece("f6", [["", "", ""], ["", "", ""], ["", "", stone_1]])
        output = piece.can_piece_move_to("j2")

        self.assertEqual(output, False)

    def test_24_can_piece_move_to(self):
        # Trying to move a piece (range 3 and direction southwest) to end point in range.
        stone_1 = Stone("BLACK", "e7")
        piece = Piece("f6", [["", "", ""], ["", "", ""], [stone_1, "", ""]])
        output = piece.can_piece_move_to("c3")

        self.assertEqual(output, True)

    def test_25_can_piece_move_to(self):
        # Trying to move a piece (range unlimited and direction southwest) to end point in range.
        stone_1 = Stone("BLACK", "e7")
        stone_2 = Stone("BLACK", "f6")
        piece = Piece("f6", [["", "", ""], ["", stone_2, ""], [stone_1, "", ""]])
        output = piece.can_piece_move_to("b2")

        self.assertEqual(output, True)

    def test_26_can_piece_move_to(self):
        # Trying to move a piece (range 3 and direction southwest) to end point out of range.
        stone_1 = Stone("BLACK", "e7")
        piece = Piece("f6", [["", "", ""], ["", "", ""], [stone_1, "", ""]])
        output = piece.can_piece_move_to("b2")

        self.assertEqual(output, False)

    def test_1_move_piece(self):
        # Testing moving a piece 1 unit to the north.
        stone_1 = Stone("BLACK", "c5")
        stone_2 = Stone("BLACK", "d5")
        stone_3 = Stone("BLACK", "e5")
        stone_4 = Stone("BLACK", "c4")
        stone_5 = Stone("BLACK", "d4")
        stone_6 = Stone("BLACK", "e4")
        stone_7 = Stone("BLACK", "c3")
        stone_8 = Stone("BLACK", "d3")
        stone_9 = Stone("BLACK", "e3")
        piece = Piece("d4", [[stone_1, stone_2, stone_3], [stone_4, stone_5, stone_6], [stone_7, stone_8, stone_9]])
        piece.move_piece("d5")
        output = [stone_1.get_coordinate(), stone_2.get_coordinate(), stone_3.get_coordinate(),
                  stone_4.get_coordinate(), stone_5.get_coordinate(), stone_6.get_coordinate(),
                  stone_7.get_coordinate(), stone_8.get_coordinate(), stone_9.get_coordinate()]
        expected = ["c6", "d6", "e6", "c5", "d5", "e5", "c4", "d4", "e4"]

        self.assertEqual(output, expected)

    def test_2_move_piece(self):
        # Testing moving a piece 1 unit to the south.
        stone_1 = Stone("BLACK", "c5")
        stone_2 = Stone("BLACK", "d5")
        stone_3 = Stone("BLACK", "e5")
        stone_4 = Stone("BLACK", "c4")
        stone_5 = Stone("BLACK", "d4")
        stone_6 = Stone("BLACK", "e4")
        stone_7 = Stone("BLACK", "c3")
        stone_8 = Stone("BLACK", "d3")
        stone_9 = Stone("BLACK", "e3")
        piece = Piece("d4", [[stone_1, stone_2, stone_3], [stone_4, stone_5, stone_6], [stone_7, stone_8, stone_9]])
        piece.move_piece("d3")
        output = [stone_1.get_coordinate(), stone_2.get_coordinate(), stone_3.get_coordinate(),
                  stone_4.get_coordinate(), stone_5.get_coordinate(), stone_6.get_coordinate(),
                  stone_7.get_coordinate(), stone_8.get_coordinate(), stone_9.get_coordinate()]
        expected = ["c4", "d4", "e4", "c3", "d3", "e3", "c2", "d2", "e2"]

        self.assertEqual(output, expected)

    def test_3_move_piece(self):
        # Testing moving a piece 1 unit to the east.
        stone_1 = Stone("BLACK", "c5")
        stone_2 = Stone("BLACK", "d5")
        stone_3 = Stone("BLACK", "e5")
        stone_4 = Stone("BLACK", "c4")
        stone_5 = Stone("BLACK", "d4")
        stone_6 = Stone("BLACK", "e4")
        stone_7 = Stone("BLACK", "c3")
        stone_8 = Stone("BLACK", "d3")
        stone_9 = Stone("BLACK", "e3")
        piece = Piece("d4", [[stone_1, stone_2, stone_3], [stone_4, stone_5, stone_6], [stone_7, stone_8, stone_9]])
        piece.move_piece("e4")
        output = [stone_1.get_coordinate(), stone_2.get_coordinate(), stone_3.get_coordinate(),
                  stone_4.get_coordinate(), stone_5.get_coordinate(), stone_6.get_coordinate(),
                  stone_7.get_coordinate(), stone_8.get_coordinate(), stone_9.get_coordinate()]
        expected = ["d5", "e5", "f5", "d4", "e4", "f4", "d3", "e3", "f3"]

        self.assertEqual(output, expected)

    def test_4_move_piece(self):
        # Testing moving a piece 1 unit to the west.
        stone_1 = Stone("BLACK", "c5")
        stone_2 = Stone("BLACK", "d5")
        stone_3 = Stone("BLACK", "e5")
        stone_4 = Stone("BLACK", "c4")
        stone_5 = Stone("BLACK", "d4")
        stone_6 = Stone("BLACK", "e4")
        stone_7 = Stone("BLACK", "c3")
        stone_8 = Stone("BLACK", "d3")
        stone_9 = Stone("BLACK", "e3")
        piece = Piece("d4", [[stone_1, stone_2, stone_3], [stone_4, stone_5, stone_6], [stone_7, stone_8, stone_9]])
        piece.move_piece("c4")
        output = [stone_1.get_coordinate(), stone_2.get_coordinate(), stone_3.get_coordinate(),
                  stone_4.get_coordinate(), stone_5.get_coordinate(), stone_6.get_coordinate(),
                  stone_7.get_coordinate(), stone_8.get_coordinate(), stone_9.get_coordinate()]
        expected = ["b5", "c5", "d5", "b4", "c4", "d4", "b3", "c3", "d3"]

        self.assertEqual(output, expected)

    def test_5_move_piece(self):
        # Testing moving a piece 1 unit to the northeast.
        stone_1 = Stone("BLACK", "c5")
        stone_2 = Stone("BLACK", "d5")
        stone_3 = Stone("BLACK", "e5")
        stone_4 = Stone("BLACK", "c4")
        stone_5 = Stone("BLACK", "d4")
        stone_6 = Stone("BLACK", "e4")
        stone_7 = Stone("BLACK", "c3")
        stone_8 = Stone("BLACK", "d3")
        stone_9 = Stone("BLACK", "e3")
        piece = Piece("d4", [[stone_1, stone_2, stone_3], [stone_4, stone_5, stone_6], [stone_7, stone_8, stone_9]])
        piece.move_piece("e5")
        output = [stone_1.get_coordinate(), stone_2.get_coordinate(), stone_3.get_coordinate(),
                  stone_4.get_coordinate(), stone_5.get_coordinate(), stone_6.get_coordinate(),
                  stone_7.get_coordinate(), stone_8.get_coordinate(), stone_9.get_coordinate()]
        expected = ["d6", "e6", "f6", "d5", "e5", "f5", "d4", "e4", "f4"]

        self.assertEqual(output, expected)

    def test_6_move_piece(self):
        # Testing moving a piece 1 unit to the northwest.
        stone_1 = Stone("BLACK", "c5")
        stone_2 = Stone("BLACK", "d5")
        stone_3 = Stone("BLACK", "e5")
        stone_4 = Stone("BLACK", "c4")
        stone_5 = Stone("BLACK", "d4")
        stone_6 = Stone("BLACK", "e4")
        stone_7 = Stone("BLACK", "c3")
        stone_8 = Stone("BLACK", "d3")
        stone_9 = Stone("BLACK", "e3")
        piece = Piece("d4", [[stone_1, stone_2, stone_3], [stone_4, stone_5, stone_6], [stone_7, stone_8, stone_9]])
        piece.move_piece("c5")
        output = [stone_1.get_coordinate(), stone_2.get_coordinate(), stone_3.get_coordinate(),
                  stone_4.get_coordinate(), stone_5.get_coordinate(), stone_6.get_coordinate(),
                  stone_7.get_coordinate(), stone_8.get_coordinate(), stone_9.get_coordinate()]
        expected = ["b6", "c6", "d6", "b5", "c5", "d5", "b4", "c4", "d4"]

        self.assertEqual(output, expected)

    def test_7_move_piece(self):
        # Testing moving a piece 1 unit to the southeast.
        stone_1 = Stone("BLACK", "c5")
        stone_2 = Stone("BLACK", "d5")
        stone_3 = Stone("BLACK", "e5")
        stone_4 = Stone("BLACK", "c4")
        stone_5 = Stone("BLACK", "d4")
        stone_6 = Stone("BLACK", "e4")
        stone_7 = Stone("BLACK", "c3")
        stone_8 = Stone("BLACK", "d3")
        stone_9 = Stone("BLACK", "e3")
        piece = Piece("d4", [[stone_1, stone_2, stone_3], [stone_4, stone_5, stone_6], [stone_7, stone_8, stone_9]])
        piece.move_piece("e3")
        output = [stone_1.get_coordinate(), stone_2.get_coordinate(), stone_3.get_coordinate(),
                  stone_4.get_coordinate(), stone_5.get_coordinate(), stone_6.get_coordinate(),
                  stone_7.get_coordinate(), stone_8.get_coordinate(), stone_9.get_coordinate()]
        expected = ["d4", "e4", "f4", "d3", "e3", "f3", "d2", "e2", "f2"]

        self.assertEqual(output, expected)

    def test_8_move_piece(self):
        # Testing moving a piece 1 unit to the southwest.
        stone_1 = Stone("BLACK", "c5")
        stone_2 = Stone("BLACK", "d5")
        stone_3 = Stone("BLACK", "e5")
        stone_4 = Stone("BLACK", "c4")
        stone_5 = Stone("BLACK", "d4")
        stone_6 = Stone("BLACK", "e4")
        stone_7 = Stone("BLACK", "c3")
        stone_8 = Stone("BLACK", "d3")
        stone_9 = Stone("BLACK", "e3")
        piece = Piece("d4", [[stone_1, stone_2, stone_3], [stone_4, stone_5, stone_6], [stone_7, stone_8, stone_9]])
        piece.move_piece("c3")
        output = [stone_1.get_coordinate(), stone_2.get_coordinate(), stone_3.get_coordinate(),
                  stone_4.get_coordinate(), stone_5.get_coordinate(), stone_6.get_coordinate(),
                  stone_7.get_coordinate(), stone_8.get_coordinate(), stone_9.get_coordinate()]
        expected = ["b4", "c4", "d4", "b3", "c3", "d3", "b2", "c2", "d2"]

        self.assertEqual(output, expected)

    def test_9_move_piece(self):
        # Testing moving a piece 1 unit to the southwest, and checking that its center attribute is updated.
        stone_1 = Stone("BLACK", "c5")
        stone_2 = Stone("BLACK", "d5")
        stone_3 = Stone("BLACK", "e5")
        stone_4 = Stone("BLACK", "c4")
        stone_5 = Stone("BLACK", "d4")
        stone_6 = Stone("BLACK", "e4")
        stone_7 = Stone("BLACK", "c3")
        stone_8 = Stone("BLACK", "d3")
        stone_9 = Stone("BLACK", "e3")
        piece = Piece("d4", [[stone_1, stone_2, stone_3], [stone_4, stone_5, stone_6], [stone_7, stone_8, stone_9]])
        piece.move_piece("c3")
        output = piece.get_center()
        expected = "c3"

        self.assertEqual(output, expected)

    """
    TESTS RELATING TO BOARD CLASS:
    """
    # Tests relating to get_rings.
    def test_1_get_rings(self):
        # Testing getting the black player's rings.
        board = Board()
        output = board.get_rings("BLACK")

        self.assertEqual(output, ["l3"])

    def test_2_get_rings(self):
        # Testing getting the white player's rings.
        board = Board()
        output = board.get_rings("WHITE")

        self.assertEqual(output, ["l18"])

    # Test relating to add_ring.
    def test_1_add_ring(self):
        # Testing adding a ring.
        board = Board()
        board.add_ring("b5", "BLACK")
        output = board.get_rings("BLACK")

        self.assertEqual(output, ["l3", "b5"])

    def test_2_add_ring(self):
        # Testing adding a duplicate ring.
        board = Board()
        board.add_ring("l3", "BLACK")
        output = board.get_rings("BLACK")

        self.assertEqual(output, ["l3"])

    # Test relating to remove_ring.
    def test_1_remove_ring(self):
        # Testing removing a ring
        board = Board()
        board.remove_rings("BLACK")
        output = board.get_rings("BLACK")

        self.assertEqual(output, [])

    # Test relating to get_space.
    def test_1_get_space(self):
        # Tests that the stone returned is the exact stone we want.
        board = Board()
        output = board.get_space("c7")
        expected = board._board[7][2]

        self.assertIs(output, expected)

    # Test relating to get_neighbors.
    def test_1_get_neighbors(self):
        # Tests that the neighbors are the exact objects we want.
        board = Board()
        output = board.get_neighbors("d5")
        expected = ["", "", "", "", "", board._board[4][2], "", board._board[4][4]]

        self.assertEqual(output, expected)

    # Tests relating to is_a_ring.
    def test_1_is_a_ring(self):
        # Tests if the piece is not a ring if the center has a stone.
        board = Board()
        output = board.is_a_ring("f7", "BLACK")

        self.assertEqual(output, False)

    def test_2_is_a_ring(self):
        # Tests if the piece is a ring when the ring is broken.
        board = Board()
        output = board.is_a_ring("g3", "BLACK")

        self.assertEqual(output, False)

    def test_3_is_a_ring(self):
        # Tests if the piece is a valid ring
        board = Board()
        output = board.is_a_ring("l3", "BLACK")

        self.assertEqual(output, True)

    def test_4_is_a_ring(self):
        # Tests if the piece is a ring but not of the current player's color.
        board = Board()
        output = board.is_a_ring("l3", "WHITE")

        self.assertEqual(output, False)

    # Tests relating to clear_area.
    def test_1_clear_area(self):
        # Tests that the desired area is cleared after the function call.
        board = Board()
        board.clear_area("c3")
        output = board.get_neighbors("c3")
        output.append(board.get_space("c3"))
        expected = ["", "", "", "", "", "", "", "", ""]

        self.assertEqual(output, expected)

    # Tests relating to clear_edges.
    def test_1_clear_edge(self):
        # Tests that when a piece moves so part of it is on the edge, the edge is cleared of stones.
        board = Board()
        stone_1 = Stone("BLACK", "c4")
        stone_2 = Stone("BLACK", "b3")
        stone_3 = Stone("BLACK", "c3")
        stone_4 = Stone("BLACK", "d3")
        stone_5 = Stone("BLACK", "c2")
        piece = Piece("c3", [["", stone_1, ""], [stone_2, stone_3, stone_4], ["", stone_5, ""]])
        board.clear_area(piece.get_center())
        piece.move_piece("c2")
        board.clear_area(piece.get_center())
        board.place_piece(piece)
        board.clear_edges()
        # Remove comment from below to display board. It will show the piece at c1 is cleared from the edge.
        # board.display_board()

    # Tests relating to place_piece.
    def test_1_place_piece(self):
        # Testing if moving a piece one space triggers it hitting anything.
        board = Board()
        stone_1 = Stone("BLACK", "c7")
        piece = Piece("c6", [["", stone_1, ""], ["", "", ""], ["", "", ""]])
        board.clear_area(piece.get_center())
        piece.move_piece("c7")
        board.place_piece(piece)
        # Remove comment from below to display board. It will show the black stone at c7 being moved to c8.
        # board.display_board()

    def test_2_place_piece(self):
        # Testing if moving a piece replaces another piece
        board = Board()
        stone_1 = Stone("BLACK", "c4")
        stone_2 = Stone("BLACK", "b3")
        stone_3 = Stone("BLACK", "c3")
        stone_4 = Stone("BLACK", "d3")
        stone_5 = Stone("BLACK", "c2")
        piece = Piece("c3", [["", stone_1, ""], [stone_2, stone_3, stone_4], ["", stone_5, ""]])
        board.clear_area(piece.get_center())
        # Moving piece 3 steps. This will be automated in the program to check for other stone interactions.
        for i in range(0,3):
            piece.move_piece("c6")
        board.clear_area(piece.get_center())
        board.place_piece(piece)
        # Remove comment from below to display board. It will show the piece at c3 being moved to c6.
        # board.display_board()

    # Tests relating to does_interaction_occur.
    def test_1_does_interaction_occur(self):
        # Tests if moving a piece to interact with a same color stone counts as an interaction.
        board = Board()
        stone_1 = Stone("BLACK", "c4")
        stone_2 = Stone("BLACK", "b3")
        stone_3 = Stone("BLACK", "c3")
        stone_4 = Stone("BLACK", "d3")
        stone_5 = Stone("BLACK", "c2")
        piece = Piece("c3", [["", stone_1, ""], [stone_2, stone_3, stone_4], ["", stone_5, ""]])
        board.clear_area(piece.get_center())
        end = "c6"
        # Moving piece 3 steps. This will be automated in the program to check for other stone interactions.
        for i in range(0,3):
            piece.move_piece(end)
        output = board.does_interaction_occur(piece, end)

        self.assertEqual(output, True)

    def test_2_does_interaction_occur(self):
        # Tests if moving a piece to a blank space that isn't its end doesn't count as an interaction
        board = Board()
        stone_1 = Stone("BLACK", "c4")
        stone_2 = Stone("BLACK", "b3")
        stone_3 = Stone("BLACK", "c3")
        stone_4 = Stone("BLACK", "d3")
        stone_5 = Stone("BLACK", "c2")
        piece = Piece("c3", [["", stone_1, ""], [stone_2, stone_3, stone_4], ["", stone_5, ""]])
        board.clear_area(piece.get_center())
        end = "c5"
        piece.move_piece(end)
        output = board.does_interaction_occur(piece, end)

        self.assertEqual(output, False)

    def test_3_does_interaction_occur(self):
        # Tests if moving a piece to the board limits counts as an interaction.
        board = Board()
        stone_1 = Stone("BLACK", "c4")
        stone_2 = Stone("BLACK", "b3")
        stone_3 = Stone("BLACK", "c3")
        stone_4 = Stone("BLACK", "d3")
        stone_5 = Stone("BLACK", "c2")
        piece = Piece("c3", [["", stone_1, ""], [stone_2, stone_3, stone_4], ["", stone_5, ""]])
        board.clear_area(piece.get_center())
        end = "c2"
        piece.move_piece(end)
        output = board.does_interaction_occur(piece, end)

        self.assertEqual(output, True)

    def test_4_does_interaction_occur(self):
        # Tests if moving a piece to its end point counts as an interaction.
        board = Board()
        stone_1 = Stone("BLACK", "c4")
        stone_2 = Stone("BLACK", "b3")
        stone_3 = Stone("BLACK", "c3")
        stone_4 = Stone("BLACK", "d3")
        stone_5 = Stone("BLACK", "c2")
        piece = Piece("c3", [["", stone_1, ""], [stone_2, stone_3, stone_4], ["", stone_5, ""]])
        board.clear_area(piece.get_center())
        end = "c4"
        piece.move_piece(end)
        output = board.does_interaction_occur(piece, end)

        self.assertEqual(output, True)

    def test_5_does_interaction_occur(self):
        # Tests if moving a piece to interact with another color stones counts as an interaction.
        # Note: The move I'm making is illegal, but this is just for testing.
        board = Board()
        stone_1 = Stone("BLACK", "c7")
        piece = Piece("c6", [["", stone_1, ""], ["", "", ""], ["", "", ""]])
        board.clear_area(piece.get_center())
        end = "c13"
        for i in range(0, 7):
            piece.move_piece(end)
        output = board.does_interaction_occur(piece, end)

        self.assertEqual(output, True)

    # Tests relating to check_rings.
    def test_1_check_rings(self):
        # Testing the original board layout for rings.
        board = Board()
        board.remove_rings("BLACK")
        board.check_rings("BLACK")
        output = board.get_rings("BLACK")

        self.assertEqual(output, ["l3"])

    def test_2_check_rings(self):
        # Testing the original board layout for rings. This employs an illegal move of not stopping after a stone
        # intersection. But this is for testing purposes only.
        board = Board()
        stone_1 = Stone("BLACK", "c4")
        stone_2 = Stone("BLACK", "b3")
        stone_3 = Stone("BLACK", "c3")
        stone_4 = Stone("BLACK", "c2")
        piece = Piece("b3", [["", "", stone_1], ["", stone_2, stone_3], ["", "", stone_4]])
        board.clear_area(piece.get_center())
        for i in range(0,3):
            piece.move_piece("e3")
        board.clear_area(piece.get_center())
        board.place_piece(piece)
        board.check_rings("BLACK")
        output = board.get_rings("BLACK")

        self.assertCountEqual(output, ["l3", "g3"])

    """
    TESTS RELATING TO GESSGAME CLASS
    """
    # Tests relating to get_game_state.
    def test_1_get_game_state(self):
        # Testing output of get_game_state.
        game = GessGame()
        output = game.get_game_state()

        self.assertEqual(output, "UNFINISHED")

    # Tests relating to resign_game.
    def test_1_resign_game(self):
        # Testing black player's resignation.
        game = GessGame()
        game.resign_game()
        output = game.get_game_state()

        self.assertEqual(output, "WHITE_WON")

    def test_2_resign_game(self):
        # Testing white player's resignation.
        game = GessGame()
        game._current_player = "WHITE"
        game.resign_game()
        output = game.get_game_state()

        self.assertEqual(output, "BLACK_WON")

    # Tests relating to make_move
    def test_1_make_move(self):
        # Testing game start and invalid piece creation. Remove comment to see output.
        game = GessGame()
        """
        game.make_move("c9", "c10")
        game.make_move("c13", "c14")
        game.make_move("a3", "a5")
        game.make_move("c7", "c8")
        """

    def test_2_make_move(self):
        # Testing game start and invalid end point. Remove comment to see output.
        game = GessGame()
        """
        game.make_move("c6", "b7")
        game.make_move("c6", "d7")
        game.make_move("c6", "b6")
        game.make_move("c6", "d6")
        game.make_move("c6", "b5")
        game.make_move("c6", "c5")
        game.make_move("c6", "d5")
        """

    def test_3_make_move(self):
        # Testing after valid piece creation and end point choice, that the piece is removed from the board.
        # Remove comment to see output.
        game = GessGame()
        # game.make_move("c3", "c7")
        # game.display_board()

    def test_4_make_move(self):
        # Testing after valid piece creation and end point choice, that the piece is removed from the board
        # and its new spot is cleared, with the piece placed properly. Remove comment to see output.
        game = GessGame()
        # game.make_move("c3", "c7")
        #game.make_move("c3", "c1")


if __name__ == "__main__":
    unittest.main()
