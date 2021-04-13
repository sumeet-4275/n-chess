# Board Design Starts here
import pygame as pg
from n-chess import engine

width = height = 512
dimension = 8
sq_size = height // dimension
max_fps = 15
images = {}

def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.image.load("images/" + piece + ".png")


def main():
    p.init() 
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = engine.state()
    #print(gs.board)
    loadImages()
    running = True
    sqSelected = ()
    playerClicks = []
    while running:
        for e in p.event.get():
            if  e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0]//sq_size
                row = location[1]//sq_size
                if sqSelected == (row,col):
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected =(row,col)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2:
                    




        drawGameState(screen, gs)
        clock.tick(max_fps)
        p.display.flip()

def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)


def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(dimension):
        for c in range(dimension):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen,color,p.Rect(c*sq_size, r*sq_size,sq_size,sq_size)
            


def drawPieces(screen, board):
    for r in range(dimension):
        for c in range(dimension):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece],p.Rect(c*sq_size, r*sq_size,sq_size,sq_size))




if __name__ == "__main__":

    main()
