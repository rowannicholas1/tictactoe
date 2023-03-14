'''main.py'''
import turtle as trtl
import random as rand

go_first = rand.randint(0, 1)
if go_first == 0:
    print("computer will go first")
    PLAYER_TURN = 0  # not players turn
if go_first == 1:
    print("player will fo first")
    PLAYER_TURN = 1  # players turn

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
C1 = WIDTH/2
C2 = WIDTH*3/2
C3 = WIDTH*5/2
R1 = -WIDTH/2
R2 = -WIDTH*3/2
R3 = -WIDTH*5/2


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

PENCIL_IMAGE = "~/Documents/github/tictactoe/pencil.gif"
wn.addshape(PENCIL_IMAGE)
pencil = trtl.Turtle(shape=PENCIL_IMAGE)
pencil.speed(10)
pencil.penup()
pencil.ht()
pencil.shape(PENCIL_IMAGE)
pencil_default = (300, 0)
pencil.goto(pencil_default)
pencil.st()
wn.update()

# maybe change to for loop because there is only 9 moves total
if PLAYER_TURN == 1:
    print("it is your turn. select a box using your number keys")
    # player does the things to make their turn
    PLAYER_TURN == 0
elif PLAYER_TURN == 0:
    print("it is the computers turn")
    # computer makes their turn
    PLAYER_TURN == 1


def draw_x():
    '''draws an x'''
    pencil.circle(60)  # placeholder until i find a good way to draw an x


def draw_o():
    '''draws an o'''
    pencil.circle(20)

# TODO: add method to prevent player from spamming buttons to draw many shapes


def keypress():
    '''executes drawing on key press'''
    pencil.pendown()
    if PLAYER_LETTER == 1:
        draw_x()
    if PLAYER_LETTER == 0:
        draw_o()
    pencil.penup()
    pencil.goto(pencil_default)
    wn.update()
    wn.tracer(False)


def key_1():
    '''sends pencil to coordinate'''
    wn.tracer(True)
    pencil.goto(C1, R1)
    keypress()


def key_2():
    '''sends pencil to coordinate'''
    wn.tracer(True)
    pencil.goto(C2, R1)
    keypress()


def key_3():
    '''sends pencil to coordinate'''
    wn.tracer(True)
    pencil.goto(C3, R1)
    keypress()


def key_4():
    '''sends pencil to coordinate'''
    wn.tracer(True)
    pencil.goto(C1, R2)
    keypress()


def key_5():
    '''sends pencil to coordinate'''
    wn.tracer(True)
    pencil.goto(C2, R2)
    keypress()


def key_6():
    '''sends pencil to coordinate'''
    wn.tracer(True)
    pencil.goto(C3, R2)
    keypress()


def key_7():
    '''sends pencil to coordinate'''
    wn.tracer(True)
    pencil.goto(C1, R3)
    keypress()


def key_8():
    '''sends pencil to coordinate'''
    wn.tracer(True)
    pencil.goto(C2, R3)
    keypress()


def key_9():
    '''sends pencil to coordinate'''
    wn.tracer(True)
    pencil.goto(C3, R3)
    keypress()


wn.onkeypress(key_1, "1")
wn.onkeypress(key_2, "2")
wn.onkeypress(key_3, "3")
wn.onkeypress(key_4, "4")
wn.onkeypress(key_5, "5")
wn.onkeypress(key_6, "6")
wn.onkeypress(key_7, "7")
wn.onkeypress(key_8, "8")
wn.onkeypress(key_9, "9")

wn.listen(True)
wn.mainloop()
