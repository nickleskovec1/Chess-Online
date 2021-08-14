import Pieces
import pygame
import sys
from network import Network

def move(position, board, moveto, net):
    if board[position] == 0:
        return
    if board[position].can_move(moveto, board):
        sendData(net, position, moveto)
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

def sendData(net, pos, moveto):
    net.send(str(net.id) + "," + str(pos) + "," + str(moveto))

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
net = Network()

isSelected = (False, 0, (0,0))
game = Pieces.game()
pygame.init()
size = 800, 800
screen = pygame.display.set_mode(size)
bg = pygame.image.load("piece_sprites\\board.png")
images = imagePrep()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            print(x,y)
            x = x//100
            y = y//100
            pos = x + (y*8)
            print("POSITION IDIOT:", pos)
            if isSelected[0]:
                print(isSelected[1], pos)
                move(isSelected[1], game.board, pos, net)
                game.print_board()
                isSelected = (False, 0)
            else:
                isSelected = (True, pos, (x*100+2,y*100+2))
        screen.fill((120,120,120))
        screen.blit(bg,(0,0))
        if isSelected[0]:
            pygame.draw.rect(screen, (0,0,255), (isSelected[2][0],isSelected[2][1],96, 96))
        drawPieces(screen, images)
        pygame.display.flip()
