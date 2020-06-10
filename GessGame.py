# Author: Zachary Levaton (OSU ID #934224677)
# Date: 5/31/2020
# Description: Houses all of the classes and methods associated with the game Gess.
#              Game rules taken from https://www.chessvariants.com/crossover.dir/gess.html
#              Board is displayed with rows increasing from bottom to top, and columns lettered from left to right.


class Stone:
    """
    This class will house all methods and attributes associated with the stones.
    The Stone can also get all neighboring spaces’ coordinates, to make Piece creation easier.
    The Stone will be used by the Piece and Board classes, since the Stones themselves are the basis of
        how and to where a player may move.
    """
    def __init__(self, color, coordinate):
        """Instantiates a Stone object with a color and coordinate."""
        self._color = color
        self._coordinate = coordinate

    def get_color(self):
        """Get method for Stone's color."""
        return self._color

    def get_coordinate(self):
        """Get method for Stone's coordinate."""
        return self._coordinate

    def change_coordinate(self, new_coordinate):
        """Set method that updates the Stone's coordinate."""
        self._coordinate = new_coordinate


class Piece:
    """
    This class will house all methods and attributes associated with the piece. It will help organize
        the methods that determine the validity of a piece and its movements.
    This class utilizes the Stone class, since a Piece is made of at least 1 stone. From this, the
        piece class is able to gather all information relating to its stones (color and coordinate).
    The Piece class is used by the GessGame class extensively, since a new piece is created for each
        move the player attempts to make.
    """
    def __init__(self, center, spaces):
        """
        Instantiates a Piece object from the parameter piece, which is composed of Stone objects and empty strings,
        in the form [ [], [], [] ].
        """
        self._center = center
        self._piece = spaces

    def get_center(self):
        """Get method for piece's center coordinate."""
        return self._center

    def get_piece(self):
        """Get method for the piece."""
        return self._piece

    def is_piece_valid(self, current_player):
        """Checks if the Piece object only has empty spaces and stones of current player's color."""
        # Checks if the piece is void of any stones around its center.
        if self._piece[0] == ["", "", ""] and self._piece[2] == ["", "", ""]:
            if self._piece[1][0] == "" and self._piece[1][2] == "":
                return False

        # Checks if the center of the piece is out of bounds on edges:
        if self._center[0] in "at" or int(self._center[1:]) in [1, 20]:
            return False

        # Cycles through all the spaces that make up a piece.
        for row in self._piece:
            for space in row:
                # Passes if the space is blank
                if space == "":
                    pass
                # Returns False if there's a stone that isn't that current player's color.
                elif space.get_color() != current_player:
                    return False

        # If the piece is valid, returns True.
        return True

    def get_piece_directions(self):
        """Evaluates the cardinal directions that the piece is able to move."""
        # Lists all possible directions.
        possible_directions = ["NW", "N", "NE", "W", "", "E", "SW", "S", "SE"]
        # Tracks the piece's possible movement directions.
        piece_directions = []
        # Counter to track index.
        counter = 0

        # Cycles through all the spaces that make up a piece.
        for row in self._piece:
            for space in row:
                # If the space is not blank, adds the appropriate direction to the piece's possible direction
                if space != "":
                    piece_directions.append(possible_directions[counter])
                    counter += 1
                else:
                    counter += 1

        # Returns all piece directions.
        return piece_directions

    def get_piece_range(self):
        """Evaluates a piece's range"""
        # If the center of the piece is blank, the range is set to 3.
        if self._piece[1][1] == "":
            return 3
        # If the center of the piece has a stone, it has unlimited range (capped at board's limit of 20).
        else:
            return 20

    def get_direction_needed(self, end):
        """Gets the direction needed for a piece to move towards the end point."""
        # Sets the piece's center letter and number
        center_letter = self._center[0]
        center_number = int(self._center[1:])
        # Sets the end's letter and number
        end_letter = end[0]
        end_number = int(end[1:])

        # Finding the vertical and horizontal distances need to move from piece center to end.
        vertical = end_number - center_number
        horizontal = ord(end_letter) - ord(center_letter)

        # Because of movement characteristics, absolute non-zero vertical and horizontal distance are always equal.
        if abs(vertical) != abs(horizontal) and vertical != 0 and horizontal != 0:
            return False
        # Accounting for an end point that is the same as the starting point.
        elif vertical == 0 and horizontal == 0:
            return False

        # North or South movement.
        if horizontal == 0:
            # Positive vertical movement means North.
            if vertical > 0:
                return "N"
            # Non-positive vertical movement means South.
            else:
                return "S"
        # East and West movement.
        elif vertical == 0:
            # Positive horizontal movement means East.
            if horizontal > 0:
                return "E"
            # Non-positive horizontal movement means West.
            else:
                return "W"
        # Northeast movement.
        elif vertical > 0 and horizontal > 0:
            return "NE"
        # Northwest movement.
        elif vertical > 0 and horizontal < 0:
            return "NW"
        # Southeast movement.
        elif vertical < 0 and horizontal > 0:
            return "SE"
        # Southwest movement.
        elif vertical < 0 and horizontal < 0:
            return "SW"
        else:
            # Error message :-)
            return "Something went wrong... You shouldn't be seeing this."

    def get_range_needed(self, end):
        """Gets the range needed for a piece to move to the end point."""
        # Sets the piece's center letter and number
        center_letter = self._center[0]
        center_number = int(self._center[1:])
        # Sets the end's letter and number
        end_letter = end[0]
        end_number = int(end[1:])

        # Finding the vertical and horizontal distances need to move from piece center to end.
        vertical = end_number - center_number
        horizontal = ord(end_letter) - ord(center_letter)

        # Only vertical movement is needed if there isn't horizontal movement.
        if horizontal == 0:
            return abs(vertical)
        # Only horizontal movement is needed if there isn't vertical movement.
        elif vertical == 0:
            return abs(horizontal)
        else:
            # With a legal move, vertical and horizontal are equal, so it doesn't matter which is returned.
            return abs(vertical)

    def can_piece_move_to(self, end):
        """Determines if a piece is able to move in the direction and range of an end point."""
        # Determines if the piece can move to the end point's direction.
        direction_is_good = self.get_direction_needed(end) in self.get_piece_directions()
        # Determines if the piece can move in the range of the end point.
        range_is_good = self.get_range_needed(end) <= self.get_piece_range()

        # If the end point is in an appropriate direction and range, returns True. Otherwise, returns False.
        if direction_is_good and range_is_good:
            return True
        else:
            return False

    def move_piece(self, end):
        """
        Moves the piece(and all stones within the piece) one unit towards the end point.
        """
        # Finding the direction the piece needs to move.
        direction = self.get_direction_needed(end)
        # Dictionary of [horizontal, vertical] values for each cardinal direction key.
        movements = {"N":[0, 1], "S":[0, -1], "E":[1, 0], "W":[-1, 0],
                     "NE":[1, 1], "NW":[-1, 1], "SE":[1, -1], "SW":[-1, -1]}

        # Cycles through all the spaces that make up a piece.
        for row in self._piece:
            for space in row:
                # Skips blank spaces in piece.
                if space == "":
                    pass
                else:
                    # Grabbing the letter and number of the old coordinate.
                    old_coordinate_letter = space.get_coordinate()[0]
                    old_coordinate_number = int(space.get_coordinate()[1:])
                    # Updating the new coordinate to be moved 1 space in the desired direction.
                    new_coordinate_letter = chr(ord(old_coordinate_letter) + movements[direction][0])
                    new_coordinate_number = old_coordinate_number + movements[direction][1]

                    # Changes the coordinates of the stones in the piece to move in the desired direction.
                    space.change_coordinate(new_coordinate_letter + str(new_coordinate_number))

        # Changes piece's center location attribute.
        old_center_letter = self._center[0]
        old_center_number = int(self._center[1:])
        new_center_letter = chr(ord(old_center_letter) + movements[direction][0])
        new_center_number = old_center_number + movements[direction][1]

        self._center = new_center_letter + str(new_center_number)


class Board:
    """
    This class will create the board that the game is based off of. The board itself stores all Stone
        objects and blank spaces. It also tracks each player's rings, and has methods to check if new
        rings are formed, or old ones destroyed.
    The GessGame class will exclusively interact with the board class.
    """
    def __init__(self):
        """Instantiates a Board object, containing a dictionary that pertains to the board setup from the game rules."""
        self._board = {}

        # Cycles through all letters/numbers in the standard game setup. Places black/white stones where needed.
        for number in range (1,21):
            self._board[number] = []
            for letter in "abcdefghijklmnopqrst":
                coordinate = letter + str(number)
                if number in [2, 4] and letter in "ceghijklmnpr":
                    self._board[number].append(Stone("BLACK", coordinate))
                elif number in [17, 19] and letter in "ceghijklmnpr":
                    self._board[number].append(Stone("WHITE", coordinate))
                elif number == 3 and letter in "bcdfhijkmoqrs":
                    self._board[number].append(Stone("BLACK", coordinate))
                elif number == 18 and letter in "bcdfhijkmoqrs":
                    self._board[number].append(Stone("WHITE", coordinate))
                elif number == 7 and letter in "cfilor":
                    self._board[number].append(Stone("BLACK", coordinate))
                elif number == 14 and letter in "cfilor":
                    self._board[number].append(Stone("WHITE", coordinate))
                else:
                    self._board[number].append("")

        # Tracks the center coordinate of rings on the board. Game starts with one ring for black/white each.
        self._rings = {"BLACK":["l3"], "WHITE":["l18"]}

    def get_space(self, coordinate):
        """Get method for a specific coordinate on the board."""
        # Getting the index of the coordinate's letter. Ord has a 97 offset from 0 index for lower case letters.
        letter_index = ord(coordinate[0]) - 97
        # Getting the row number from the coordinate.
        row_number = int(coordinate[1:])

        return self._board[row_number][letter_index]

    def get_rings(self, color):
        """Returns the ring center locations for a specified player."""
        return self._rings[color]

    def add_ring(self, coordinate, color):
        """Adds the ring center location for a specified player."""
        if coordinate not in self._rings[color]:
            self._rings[color].append(coordinate)

    def remove_rings(self, color):
        """Removes ring for specified player."""
        self._rings[color] = []

    def get_neighbors(self, coordinate):
        """Returns all neighboring coordinates around a coordinate."""
        neighbors = []

        # Finds the Stone's coordinate letter and number
        center_letter = coordinate[0]
        center_number = int(coordinate[1:])

        # Cycles from row to left to row to right of Stone.
        for num in range(center_number + 1, center_number - 2, -1):
            # Adds left/center/right letters plus row number, then appends to neighbor list.
            neighbors.append(self.get_space(chr(ord(center_letter) - 1) + str(num)))
            neighbors.append(self.get_space(chr(ord(center_letter)) + str(num)))
            neighbors.append(self.get_space(chr(ord(center_letter) + 1) + str(num)))

        # Removes the coordinate itself from the neighbors list.
        neighbors.pop(4)
        return neighbors

    def is_a_ring(self, coordinate, color):
        """Determines if a given coordinate is a ring."""
        # If the given coordinate is not blank, it cannot form a ring.
        if self.get_space(coordinate) != "":
            return False

        # Getting the neighboring
        neighbors = self.get_neighbors(coordinate)
        for space in neighbors:
            # If the space is blank, the spot is not a ring.
            if space == "":
                return False
            elif space.get_color() != color:
                return False

        return True

    def clear_area(self, coordinate):
        """Clears the area around a coordinate."""
        # Gets all neighboring spaces
        area = self.get_neighbors(coordinate)
        # Sets the coordinate to be blank.
        self._board[int(coordinate[1:])][ord(coordinate[0]) - 97] = ""

        # Cycles through the coordinate's neighbors, making all of their spaces blank.
        for space in area:
            if space == "":
                pass
            else:
                space_coord = space.get_coordinate()
                self._board[int(space_coord[1:])][ord(space_coord[0]) - 97] = ""

    def clear_edges(self):
        """Clears the board edges, where no Stone is allowed to be."""
        # Clears top and bottom rows.
        for letter in "abcdefghijklmnopqrst":
            for number in [1, 20]:
                self._board[number][ord(letter) - 97] = ""

        # Clears left and right edges.
        for letter in "at":
            for number in range(1,21):
                self._board[number][ord(letter) - 97] = ""

    def place_piece(self, piece):
        """Method that sets a piece in a specific location, clearing the area beforehand."""
        # Getting the piece's center location.
        piece_center = piece.get_center()
        # Clearing that area on the board
        self.clear_area(piece_center)

        # Piece placement.
        for row in piece.get_piece():
            for space in row:
                if space == "":
                    pass
                else:
                    # Altering the stone's coordinate to be searchable in Board's dictionary.
                    coordinate = space.get_coordinate()
                    coordinate_letter = ord(coordinate[0]) - 97
                    coordinate_number = int(coordinate[1:])

                    # Setting the stone at its location.
                    self._board[coordinate_number][coordinate_letter] = space

    def does_interaction_occur(self, piece, end):
        """Checks if the currently moved piece intersects with another stone or the board's edge."""
        # After the piece is moved 1 space, checks the piece's center coordinate.
        piece_center = piece.get_center()
        # Gets all neighboring spots on the board.
        neighbors = self.get_neighbors(piece_center)

        # Checking if the piece's center is at the edge of the playable area.
        if piece_center[0] in "bs" or int(piece_center[1:]) in [2, 19]:
            return True
        # If the piece has reached its desired end point.
        elif piece_center == end:
            return True
        # Goes through all neighboring spots to see if they have a stone.
        else:
            for space in neighbors:
                if space != "":
                    return True

        # Interaction doesn't occur
        return False

    def check_rings(self, color):
        """Checks the entire board for rings of a specific player's color."""
        # Clears all existing rings
        self.remove_rings(color)

        # Cycling through the center locations where a ring can exist.
        for number in range (3, 19):
            for letter in "cdefghijklmnopqr":
                # For readability, creates the string of the current coordinate.
                current_coordinate = letter + str(number)
                # Checks if the space is a ring, adding it to the player color's collection of rings.
                if self.is_a_ring(current_coordinate, color):
                    self.add_ring(current_coordinate, color)

    def display_board(self):
        """Print out the board. Used for testing/visualization."""
        for number in range(20,0,-1):
            row = []
            for space in self._board[number]:
                if space == "":
                    row.append(".")
                elif space.get_color() == "BLACK":
                    row.append("b")
                elif space.get_color() == "WHITE":
                    row.append("w")
            print(row)


class GessGame:
    """
    This is the main class housing the implementation of the Gess game.
    The init method will initialize the board, game status, and current player, with get_game_status
        and resign_game methods doing as they sound.
    The make_move method houses the majority of the Gess game functionality. It makes extensive use of
        the methods from the Stone, Piece and Board classes to deal with the intricacies of the rules
        surrounding the rules of Gess. The make_move method also makes calls to determine if a game is
        won (all rings of a certain color destroyed).
    """
    def __init__(self):
        """Instantiates a GessGame object with a new board, unifinished game state, and black up first."""
        self._board = Board()
        self._game_state = "UNFINISHED"
        self._current_player = "BLACK"

    def get_game_state(self):
        """Get method for game state."""
        return self._game_state

    def resign_game(self):
        """Method that allows the current player to resign the game."""
        if self._current_player == "BLACK":
            self._game_state = "WHITE_WON"
        else:
            self._game_state = "BLACK_WON"

    def display_board(self):
        """Method to display board."""
        self._board.display_board()

    def make_move(self, start, end):
        """Docstring here."""
        # Checking if the game has been won. Returns False to indicate the game has been won.
        if self._game_state != "UNFINISHED":
            return False

        # Getting the start space and its neighbors, and combining them into a single list.
        neighbors = self._board.get_neighbors(start)
        center = self._board.get_space(start)
        neighbors.insert(4, center)
        # For readability, setting the rows of the piece to match how it will appear on the board.
        piece_rows = [neighbors[0:3], neighbors[3:6], neighbors[6:]]
        # Creating the Piece object.
        piece = Piece(start, piece_rows)

        # If the piece is not valid, returns False to indicate the move is invalid.
        if piece.is_piece_valid(self._current_player) is False:
            print("The space you chose for the piece is not valid. Please choose another spot.")
            return False
        # If the end spot chosen is not valid, returns False to indicate the move is invalid.
        elif piece.can_piece_move_to(end) is False:
            return False

        # Clears the piece's space on the board.
        self._board.clear_area(start)

        # Moves piece for its first step, in case the center is at board's the boundary.
        piece.move_piece(end)

        # Moves the piece until it hits another stone or hits the board's edge.
        while self._board.does_interaction_occur(piece, end) is False:
            piece.move_piece(end)

        # Clears the area where the piece has moved to, effectively taking off the existing pieces.
        self._board.clear_area(piece.get_center())
        # Places the piece in its new location.
        self._board.place_piece(piece)
        # Clears all edges where any stones may have been moved to.
        self._board.clear_edges()

        # UNCOMMENT BELOW IF YOU WANT THE BOARD TO BE DISPLAYED AFTER EACH MOVE IS MADE.
        # self.display_board()

        # Checking the for rings of the black player.
        self._board.check_rings("BLACK")
        black_rings = self._board.get_rings("BLACK")

        # Checking the for rings of the black player.
        self._board.check_rings("WHITE")
        white_rings = self._board.get_rings("WHITE")

        # If the black player has no rings, white wins.
        if len(black_rings) == 0:
            self._game_state = "WHITE_WON"
        # If the white player has no rings, black wins.
        elif len(white_rings) == 0:
            self._game_state = "BLACK_WON"

        # If both players have rings, then this will switch the current player.
        # Returns true to indicate the game is still continuing.
        else:
            if self._current_player == "BLACK":
                self._current_player = "WHITE"
                return True
            else:
                self._current_player = "BLACK"
                return True
