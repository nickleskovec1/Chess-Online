import Pieces
import pygame
import sys
from network import Network
import os.path

try: ASSETS = sys._MEIPASS+"//Assets"
except Exception: ASSETS = os.path.abspath(".")+"//Assets"
#ASSETS = os.path.abspath(".")+"//Assets"

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
        print("yo")
        return False
    if board[king.position+1] != 0 or board[king.position+2] != 0:
        print("yo1")
        return False
    if board[king.position + 3] == 0 or type(board[king.position + 3]) != Pieces.rook:
        print("yo2")
        return False
    if not board[king.position + 3].first_move:
        print("yo3")
        return False
    return True


def kingmove(position, board, moveto):
    if board[position].isking():
        if moveto == position + 2:
            if attempt_castle_right(board[position], board):
                # if board[moveto] != 0:
                #     board[moveto.x] = 900
                board[position].first_move = False
                board[position + 1] = board[position + 3]
                board[position + 1].x -= 200
                board[position + 3].position = position + 1
                board[position + 3] = 0
                board[moveto] = board[position]
                board[moveto].position = moveto
                board[moveto].x = returnWidth(moveto)
                board[position] = 0
                return True
        elif moveto == position - 2:
            if attempt_castle_left(board[position], board):
                board[position].first_move = False
                board[position - 1] = board[position - 4]
                board[position - 1].x += 300
                board[position - 4].position = position - 1
                board[position - 4] = 0
                board[moveto] = board[position]
                board[moveto].position = moveto
                board[moveto].x = returnWidth(moveto)
                board[position] = 0
                return True
    return False


def move(position, board, moveto):
    if board[position] == 0:
        print("hi")
        return False
    if colorToPlayer[net.id] != board[position].color:
        print("hi1")
        return False
    if board[position].can_move(moveto, board):
        if kingmove(position, board, moveto):
            return True
            #CHECK FOR CASTLEING
        if board[moveto] != 0:
            board[moveto].x = 1200
            board[moveto].y = 1200
        board[moveto] = board[position]
        board[moveto].position = moveto
        board[moveto].x = returnWidth(moveto)
        board[moveto].y = returnHeight(moveto)
        board[position] = 0
        print("hi3")
        return True
    return False


def force_move(position, board, moveto):
    if kingmove(position, board, moveto):
        return
    if board[moveto] != 0:
        board[moveto].x = 1200
        board[moveto].y = 1200
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
    """Prepares all images, and links with the __str__ method of each piece"""
    #os.path.join(ASSETS, "board.png")
    b_rook = pygame.image.load(os.path.join(ASSETS, "b_rook.png"))
    b_knight = pygame.image.load(os.path.join(ASSETS, "b_knight.png"))
    b_bishop = pygame.image.load(os.path.join(ASSETS, "b_bishop.png"))
    b_king = pygame.image.load(os.path.join(ASSETS, "b_king.png"))
    b_queen = pygame.image.load(os.path.join(ASSETS, "b_queen.png"))
    b_pawn = pygame.image.load(os.path.join(ASSETS, "b_pawn.png"))
    w_rook = pygame.image.load(os.path.join(ASSETS, "w_rook.png"))
    w_knight = pygame.image.load(os.path.join(ASSETS, "w_knight.png"))
    w_bishop = pygame.image.load(os.path.join(ASSETS, "w_bishop.png"))
    w_king = pygame.image.load(os.path.join(ASSETS, "w_king.png"))
    w_queen = pygame.image.load(os.path.join(ASSETS, "w_queen.png"))
    w_pawn = pygame.image.load(os.path.join(ASSETS, "w_pawn.png"))
    images = {"B_rook": b_rook,
              "B_knight": b_knight,
              "B_bishop": b_bishop,
              "B_king": b_king,
              "B_queen": b_queen,
              "B_pawn": b_pawn,
              "w_rook": w_rook,
              "w_knight": w_knight,
              "w_bishop": w_bishop,
              "w_king": w_king,
              "w_queen": w_queen,
              "w_pawn": w_pawn}
    return images


def turn_timer(time, screen, other):
    font = pygame.font.Font((os.path.join(ASSETS, "helloAmargo.ttf")), 32)
    text = font.render(str(int(time)), True, (0, 255, 0), (0, 0, 128))
    text1 = text.get_rect()
    text1.x = 800
    player1 = net.id == "0"
    if other:
        if player1:
            text1.y = 0
        else:
            text1.y = 600
    else:
        if player1:
            text1.y = 600
        else:
            text1.y = 0
    screen.blit(text, text1)


#INITIALIZE NETWORK CODE
ip = input("Enter in Ip Address: ")
port = int(input("Enter in Port Number: "))
#ip = "192.168.0.199"
#port = 5555
net = Network(ip, port)
turn = int(net.id)

colorToPlayer = {"0":"w", "1":"B"}
isSelected = (False, 0, (0,0))
game = Pieces.game()
pygame.init()
size = 900, 800
screen = pygame.display.set_mode(size)
bg = pygame.image.load(os.path.join(ASSETS, "board.png"))
#bg = pygame.image.load(f"{ASSETS}\\board.png").convert()
images = imagePrep()
clock = pygame.time.Clock()
time, time1 = 300, 300
f = 60
first_turn = True
print(turn)
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
                #turn_timer(time, screen)
                x, y = event.pos
                print(x, y)
                if x <= 800 or y <= 800:  # Is in bounds of game
                    print(x, y)
                    x = x//100
                    y = y//100
                    pos = x + (y*8)
                    print("POSITION IDIOT:", pos)
                    if isSelected[0]:
                        print(isSelected[1], pos)
                        flag = move(isSelected[1], game.board, pos)
                        print(flag)
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
    if turn == 0:
        time -= (1/60)
    else:
        time1 -= (1/60)
    turn_timer(time, screen, False)
    turn_timer(time1, screen, True)
    drawPieces(screen, images)
    pygame.display.flip()
