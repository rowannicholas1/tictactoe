import turtle as trtl
import random as rand

# TODO: assign variables before printed text
go_first = rand.randint(0, 1)
if go_first == 0:
    print("computer will go first")
if go_first == 1:
    print("player will fo first")

x_o = rand.randint(0, 1)
if x_o == 0:
    print("player will be x, computer will be o")
if x_o == 1:
    print("player will be x, computer will be o")

wn = trtl.Screen()
wn.tracer(False)

board = trtl.Turtle()
board.ht()
board.pensize(5)
board.setheading(90)
board.penup()

board_width = 65
board_length = 200


def board_move():
    board.pendown()
    board.forward(400)
    board.penup()


board.goto(-board_width, -board_length)
board_move()
board.goto(board_width, -board_length)
board_move()
board.setheading(0)
board.goto(-board_length, -board_width)
board_move()
board.goto(-board_length, board_width)
board_move()


wn.mainloop()
