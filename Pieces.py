class game:
    def __init__(self):
        self.wCheck = False
        self.bCheck = False
        self.board = []
        for i in range(64):
            self.board.append(0)
        self.board[8] = pawn(8, "b", 0, 100)
        self.board[9] = pawn(9, "b", 100, 100)
        self.board[10] = pawn(10, "b", 200, 100)
        self.board[11] = pawn(11, "b", 300, 100)
        self.board[12] = pawn(12, "b", 400, 100)
        self.board[13] = pawn(13, "b", 500, 100)
        self.board[14] = pawn(14, "b", 600, 100)
        self.board[15] = pawn(15, "b", 700, 100)
        self.board[0] = rook(0, "b", 0, 0)
        self.board[1] = Knight(1, "b", 100, 0)
        self.board[2] = bishop(2, "b", 200, 0)
        self.board[3] = queen(3, "b", 300, 0)
        self.board[4] = King(4, "b", 400, 0)
        self.board[5] = bishop(5, "b", 500, 0)
        self.board[6] = Knight(6, "b", 600, 0)
        self.board[7] = rook(7, "b", 700, 0)


        self.board[48] = pawn(48, "w", 0, 600)
        self.board[49] = pawn(49, "w", 100, 600)
        self.board[50] = pawn(50, "w", 200, 600)
        self.board[51] = pawn(51, "w", 300, 600)
        self.board[52] = pawn(52, "w", 400, 600)
        self.board[53] = pawn(53, "w", 500, 600)
        self.board[54] = pawn(54, "w", 600, 600)
        self.board[55] = pawn(55, "w", 700, 600)
        self.board[56] = rook(56, "w", 0, 700)
        self.board[57] = Knight(57, "w", 100, 700)
        self.board[58] = bishop(58, "w", 200, 700)
        self.board[59] = queen(59, "w", 300, 700)
        self.board[60] = King(60, "w", 400, 700)
        self.board[61] = bishop(61, "w", 500, 700)
        self.board[62] = Knight(62, "w", 600, 700)
        self.board[63] = rook(63, "w", 700, 700)
        self.pieces = []
        for i in range(len(self.board)):
            if self.board[i] != 0:
                self.pieces.append(self.board[i])

    def setBoard(self, position, object):
        self.board[position] = object

    def getBoard(self):
        return self.board

    def getPieces(self):
        return self.pieces

    def print_board(self):
        """Prints board using 8 character buffers for each space, might change if more optimal way of doing this"""
        return_string = "{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}\n{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}\n" \
                        "{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}\n{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}\n" \
                        "{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}\n{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}\n" \
                        "{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}\n{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}"
        print(return_string.format(str(self.board[0]), str(self.board[1]), str(self.board[2]), str(self.board[3]), str(self.board[4]),
                                   str(self.board[5]), str(self.board[6]), str(self.board[7]),
                                   str(self.board[8]), str(self.board[9]), str(self.board[10]), str(self.board[11]), str(self.board[12]),
                                   str(self.board[13]), str(self.board[14]), str(self.board[15]),
                                   str(self.board[16]), str(self.board[17]), str(self.board[18]), str(self.board[19]), str(self.board[20]),
                                   str(self.board[21]), str(self.board[22]), str(self.board[23]),
                                   str(self.board[24]), str(self.board[25]), str(self.board[26]), str(self.board[27]), str(self.board[28]),
                                   str(self.board[29]), str(self.board[30]), str(self.board[31]),
                                   str(self.board[32]), str(self.board[33]), str(self.board[34]), str(self.board[35]), str(self.board[36]),
                                   str(self.board[37]), str(self.board[38]), str(self.board[39]),
                                   str(self.board[40]), str(self.board[41]), str(self.board[42]), str(self.board[43]), str(self.board[44]),
                                   str(self.board[45]), str(self.board[46]), str(self.board[47]),
                                   str(self.board[48]), str(self.board[49]), str(self.board[50]), str(self.board[51]), str(self.board[52]),
                                   str(self.board[53]), str(self.board[54]), str(self.board[55]),
                                   str(self.board[56]), str(self.board[57]), str(self.board[58]), str(self.board[59]), str(self.board[60]),
                                   str(self.board[61]), str(self.board[62]), str(self.board[63])))


class bishop:
    def __init__(self, position, color, x, y):
        self.position = position
        self.color = color
        self.x = x
        self.y = y

    def __str__(self):
        return self.color + "_bishop"

    def isking(self):
        return False

    def can_move(self, position, board):
        if position > self.position:
            if (position - self.position) % 9 == 0:
                incr = 9
            elif (position - self.position) % 7 == 0:
                incr = 7
            else:
                return False  # Checks if position cannot be reached by bishop e.g. horizontal
            temp = self.position
            while temp < position:
                temp += incr
                if board[temp] != 0:
                    if temp != position:
                        return False
                    elif temp == position:
                        if board[position].color == self.color:
                            return False
            return True
        if position < self.position:
            if (self.position - position) % 9 == 0:
                incr = 9
            elif (self.position - position) % 7 == 0:
                incr = 7
            else:
                return False  # Checks for invalid position
            temp = self.position
            while temp > position:
                temp -= incr
                if board[temp] != 0:
                    if temp != position:
                        return False
                    elif temp == position:
                        if board[position].color == self.color:
                            return False
            return True
        return False  # Shouldn't be able to move to the same square


class rook:
    def __init__(self, position, color, x, y):
        self.position = position
        self.color = color
        self.x = x
        self.y = y

    def __str__(self):
        return self.color + "_rook"

    def isking(self):
        return False

    def can_move(self, position, board):
        incr = 0
        if position < self.position:
            if (self.position - position) % 8 == 0:
                incr = -8
        if position > self.position:
            if (position - self.position) % 8 == 0:
                incr = 8
        temp = self.position % 8  # Finds base number of current position of piece
        temp = self.position - temp  # Subtracts base number of current position to get beginning of row of position
        temp1 = temp + 7  # End of Row
        temp_pos = self.position
        if temp <= position <= temp1:
            if position > self.position:
                incr = 1
            elif position < self.position:
                incr = -1
        if incr == 0:
            return False  # Handles impossible movement of piece
        while temp_pos != position:
            temp_pos += incr
            if board[temp_pos] != 0:
                if temp_pos != position:  # Running into a piece before final destination returns false
                    return False
                elif temp_pos == position:
                    if board[position].color == self.color:  # Can't take your own pieces
                        return False
        return True


class queen(bishop, rook):
    def __init__(self, position, color, x, y):
        self.position = position
        self.color = color
        self.x = x
        self.y = y
        #super(queen, self).__init__(position, color)

    def __str__(self):
        return self.color + "_queen"

    def isking(self):
        return False

    def can_move(self, position, board):
        if any(cls.can_move(self, position, board) for cls in queen.__bases__):
            return True
        return False


class King:
    def __init__(self, position, color, x, y, in_check = False, first_move = True):
        self.position = position
        self.color = color
        self.in_check = in_check
        self.x = x
        self.y = y
        self.first_move = first_move

    def __str__(self):
        return self.color + "_king"

    def isking(self):
        return True

    def can_move(self, pos, board):
        curpos = self.position
        if board[pos] != 0:
            if board[pos].color == self.color:
                return False
        if pos == curpos+1 or pos == curpos-1 or pos == curpos+8 or pos == curpos-8:
            if self.in_check:
                if 1 == 0:  # TODO STUB, change to if the move does not put the king out of danger
                    return False
            self.first_move = False
            return True
        if pos == curpos+7 or pos == curpos+9 or pos == curpos-7 or pos == curpos-9:
            if self.in_check:
                if 1 == 0:  # TODO STUB, change to if the move does not put the king out of danger
                    return False
            self.first_move = False
            return True
        return False


class Knight:
    def __init__(self, position, color, x, y):
        self.position = position
        self.color = color
        self.x = x
        self.y = y

    def __str__(self):
        return self.color + "_knight"

    def isking(self):
        return False

    def can_move(self, position, board):
        if board[position] != 0:
            if board[position].color == self.color:
                return False
        up_right = position == self.position - 15
        up_left = position == self.position - 17
        right_up = position == self.position - 6
        left_up = position == self.position - 10
        down_right = position == self.position + 17
        down_left = position == self.position + 15
        right_down = position == self.position + 10
        left_down = position == self.position + 6
        if up_right or up_left or right_up or left_up or down_right or down_left or right_down or left_down:
            return True
        return False


class pawn():
    def __init__(self, position, color, x, y, first_move=True):
        self.position = position
        self.color = color
        self.first_move = True
        self.x = x
        self.y = y
        #print(super(pawn, self).getBoard())

    def __str__(self):
        return self.color + "_pawn"

    def isking(self):
        return False

    def can_move(self, position, board):
        if self.color == "w":
            if self.first_move and position == (self.position - 16):  # Handles first move to move 2 spaces
                if board[self.position - 8] != 0 or board[position] != 0:
                    return False
                else:
                    self.first_move = False
                    return True
            if not (7 <= (self.position - position) <= 9):  # handles illegal moves
                return False
            if self.position - position == 7 or self.position - position == 9:
                if board[position] == 0:
                    return False
                elif board[position].color == "w":
                    return False
                else:
                    return True
            if self.position - position == 8:
                print(board)
                if board[position] != 0:
                    return False
                return True
        if self.color == "b":
            if self.first_move and position == (self.position + 16):  # Handles first move to move 2 spaces
                if board[self.position + 8] != 0 or board[position] != 0:
                    return False
                else:
                    self.first_move = False
                    return True
            if position - self.position == 8:
                if board[position] != 0:
                    return False
                self.first_move = False
                return True
            if not (7 <= (position - self.position) <= 9):  # handles illegal moves
                return False
            if position - self.position == 7 or position - self.position == 9:
                if board[position] == 0:
                    return False
                elif board[position].color == "b":
                    return False
                else:
                    return True








