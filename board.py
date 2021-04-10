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
    while running:
        for e in p.event.get():
            if  e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(max_fps)
        p.display.flip()

def drawBoard(screen):


def drawPieces(screen, board):


def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)


if __name__ == "__main__":

    main()