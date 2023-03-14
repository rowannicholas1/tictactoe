'''main.py'''
import turtle as trtl
import random as rand

go_first = rand.randint(0, 1)
if go_first == 0:
    print("computer will go first")
    PLAYER_MOVE = 0
    COMPUTER_MOVE = 1
if go_first == 1:
    print("player will fo first")
    PLAYER_MOVE = 1
    COMPUTER_MOVE = 0

x_o = rand.randint(0, 1)
if x_o == 0:
    print("player will be x, computer will be o")
    PLAYER_LETTER = 1  # X
    COMPUTER_LETTER = 0  # O
if x_o == 1:
    print("player will be o, computer will be x")
    PLAYER_LETTER = 0  # X
    COMPUTER_LETTER = 1  #

wn = trtl.Screen()
wn.tracer(False)

board = trtl.Turtle()
board.ht()
board.pensize(5)
board.setheading(90)
board.penup()

BOARD_WIDTH = 65
BOARD_LENGTH = 200

WIDTH = 150
c1 = WIDTH/2
c2 = WIDTH*3/2
c3 = WIDTH*5/2
r1 = -WIDTH/2
r2 = -WIDTH*3/2
r3 = -WIDTH*5/2


def board_move():
    '''removes repetitive code'''
    board.pendown()
    board.forward(400)
    board.penup()


board.goto(-BOARD_WIDTH, -BOARD_LENGTH)
board_move()
board.goto(BOARD_WIDTH, -BOARD_LENGTH)
board_move()
board.setheading(0)
board.goto(-BOARD_LENGTH, -BOARD_WIDTH)
board_move()
board.goto(-BOARD_LENGTH, BOARD_WIDTH)
board_move()

if go_first == 1:
    print("select a box using your number keys")

PENCIL_IMAGE = "~/Documents/github/tictactoe/pencil.gif"
wn.addshape(PENCIL_IMAGE)
pencil = trtl.Turtle(shape=PENCIL_IMAGE)
pencil.penup()
pencil.ht()
pencil.shape(PENCIL_IMAGE)
pencil_default = (300, 0)
pencil.goto(pencil_default)
pencil.st()
wn.update()


def draw_x():
    pencil.circle(60)  # placeholder until i find a good way to draw an x


def draw_o():
    pencil.circle(20)


def key_1():
    wn.tracer(True)
    pencil.goto(c1, r1)
    pencil.pendown()
    if PLAYER_LETTER == 1:
        draw_x()
    if PLAYER_LETTER == 0:
        draw_o()
    pencil.penup()
    pencil.goto(pencil_default)
    wn.update()
    wn.tracer(False)


wn.onkeypress(key_1, "1")

wn.listen()
wn.mainloop()
