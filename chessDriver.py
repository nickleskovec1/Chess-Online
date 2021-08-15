import Pieces
import pygame
import sys
from network import Network

def nextTurn(turn):
    if turn == 0:
        return 1
    if turn == 1:
        return 0

def attempt_castle_left(king, board):
    if not king.first_move:
        return False
    if board[king.position-1] != 0 or board[king.position-2] != 0 or board[king.position - 3] != 0:
        return False
    if board[king.position - 4] == 0 or type(board[king.position - 4]) != Pieces.rook:
        return False
    if not board[king.position - 4].first_move:
        return False
    return True

def attempt_castle_right(king, board):
    if not king.first_move:
        return False
    if board[king.position+1] != 0 or board[king.position+2] != 0:
        return False
    if board[king.position + 3] == 0 or type(board[king.position + 3]) != Pieces.rook:
        return False
    if not board[king.position + 3].first_move:
        return False
    return True

def move(position, board, moveto):
    if board[position] == 0:
        return False
    if colorToPlayer[net.id] != board[position].color:
        return False
    if board[position].can_move(moveto, board):
        if board[position].isking():
            if moveto == position + 2:
                if attempt_castle_right(board[position], board):
                    #TODO CASTLING
                    pass
                if attempt_castle_left(board[position], board):
                    #TODO CASTLING
                    pass
            #CHECK FOR CASTLEING
        if board[moveto] != 0:
            board[moveto].x = 900
            board[moveto].y = 900
        board[moveto] = board[position]
        board[moveto].position = moveto
        board[moveto].x = returnWidth(moveto)
        board[moveto].y = returnHeight(moveto)
        board[position] = 0
        return True
    return False

def force_move(position, board, moveto):
    if board[moveto] != 0:
        board[moveto].x = 900
        board[moveto].y = 900
    board[moveto] = board[position]
    board[moveto].position = moveto
    board[moveto].x = returnWidth(moveto)
    board[moveto].y = returnHeight(moveto)
    board[position] = 0

def drawPieces(screen, images):
    for object in game.getPieces():
        rectangle = pygame.Rect(object.x, object.y, 100,100)
        screen.blit(images[str(object)], rectangle)

def returnWidth(position):
    return (position % 8) * 100

def returnHeight(position):
    return (position // 8) * 100

def imagePrep():
    b_rook = pygame.image.load("piece_sprites\\b_rook.png")
    b_knight = pygame.image.load("piece_sprites\\b_knight.png")
    b_bishop = pygame.image.load("piece_sprites\\b_bishop.png")
    b_king = pygame.image.load("piece_sprites\\b_king.png")
    b_queen = pygame.image.load("piece_sprites\\b_queen.png")
    b_pawn = pygame.image.load("piece_sprites\\b_pawn.png")
    w_rook = pygame.image.load("piece_sprites\\w_rook.png")
    w_knight = pygame.image.load("piece_sprites\\w_knight.png")
    w_bishop = pygame.image.load("piece_sprites\\w_bishop.png")
    w_king = pygame.image.load("piece_sprites\\w_king.png")
    w_queen = pygame.image.load("piece_sprites\\w_queen.png")
    w_pawn = pygame.image.load("piece_sprites\\w_pawn.png")
    images = {"b_rook": b_rook,
              "b_knight": b_knight,
              "b_bishop": b_bishop,
              "b_king": b_king,
              "b_queen": b_queen,
              "b_pawn": b_pawn,
              "w_rook": w_rook,
              "w_knight": w_knight,
              "w_bishop": w_bishop,
              "w_king": w_king,
              "w_queen": w_queen,
              "w_pawn": w_pawn}
    return images

#INITIALIZE NETWORK CODE
ip = input("Enter in Ip Address: ")
port = int(input("Enter in Port Number: "))
net = Network(ip, port)
turn = int(net.id)

colorToPlayer = {"0":"w", "1":"b"}
isSelected = (False, 0, (0,0))
game = Pieces.game()
pygame.init()
size = 800, 800
screen = pygame.display.set_mode(size)
bg = pygame.image.load("piece_sprites\\board.png")
images = imagePrep()
clock = pygame.time.Clock()
f = 60
while 1:
    clock.tick(f)
    if net.networkDataArrived():
        reply = net.receive().split(",")
        print(reply)
        force_move(int(reply[0]), game.board, int(reply[1]))
        turn = nextTurn(turn)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if turn == 0:
                x,y = event.pos
                print(x,y)
                x = x//100
                y = y//100
                pos = x + (y*8)
                print("POSITION IDIOT:", pos)
                if isSelected[0]:
                    print(isSelected[1], pos)
                    flag = move(isSelected[1], game.board, pos)
                    if flag:
                        net.send(str(net.id)+"," + str(isSelected[1]) + "," + str(pos))
                        game.print_board()
                        turn = nextTurn(turn)
                    isSelected = (False, 0)
                else:
                    isSelected = (True, pos, (x*100+2, y*100+2))
    screen.fill((120, 120, 120))
    screen.blit(bg, (0, 0))
    if isSelected[0]:
        pygame.draw.rect(screen, (0, 0, 255), (isSelected[2][0], isSelected[2][1], 96, 96))
    drawPieces(screen, images)
    pygame.display.flip()
