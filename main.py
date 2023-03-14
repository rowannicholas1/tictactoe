'''main.py'''
import turtle as trtl
import random as rand

# TODO: assign variables before printed text
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

wn = trtl.Screen()
wn.tracer(False)

board = trtl.Turtle()
board.ht()
board.pensize(5)
board.setheading(90)
board.penup()

BOARD_WIDTH = 65
BOARD_LENGTH = 200


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


wn.mainloop()
