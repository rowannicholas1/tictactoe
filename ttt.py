'''ttt.py'''
import turtle as trtl
import random as rand

wn = trtl.Screen()
wn.setup(width=0.5, height=0.8)
wn.tracer(False)

SCORES_FILE = "scores.txt"
PENCIL_IMAGE = "pencil.gif"
names = []
scores = []

drawer = trtl.Turtle()
drawer.ht()
WIDTH = 150
INDEX = 0
numlist = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
OFFSET = 180
X_ANGLE = 45
X_LENGTH = 27
X_SQUARE_1 = X_LENGTH ^ 2

drawer.penup()
drawer.goto(-OFFSET, OFFSET)
drawer.pendown()

scorer = trtl.Turtle()
scorer.ht()
scorer.penup()

writer = trtl.Turtle()
writer.ht()
writer.penup()
writer.goto(-OFFSET, OFFSET)
writer.goto(writer.xcor()+WIDTH*1.5, writer.ycor()-WIDTH*3.5)
x1 = drawer.xcor()

C1 = WIDTH/2-OFFSET
C2 = WIDTH*3/2-OFFSET
C3 = WIDTH*5/2-OFFSET
R1 = -WIDTH/2+OFFSET
R2 = -WIDTH*3/2+OFFSET
R3 = -WIDTH*5/2+OFFSET
# defined functions


def board():
    for i in range(3):
        tiles()
    wn.update()
    drawer.penup()


def tiles():
    for i in range(3):
        square()
        drawer.forward(WIDTH)
    drawer.penup()
    drawer.goto(x1, drawer.ycor()-WIDTH)
    drawer.pendown()


def square():
    global INDEX
    for i in range(4):
        drawer.forward(WIDTH)
        drawer.setheading(drawer.heading()-90)
    drawer.penup()
    drawer.goto(drawer.xcor()+WIDTH/15, drawer.ycor()-WIDTH/5.5)
    drawer.write(numlist[INDEX], font=("comic sans", 18, "normal"))
    INDEX += 1
    drawer.goto(drawer.xcor()-WIDTH/15, drawer.ycor()+WIDTH/5.5)
    drawer.pendown()


def update_scores(value):
    file2 = open(SCORES_FILE, "w")
    if value == 0:  # computer
        index = 0
        scores[index] = int(scores[index]) + 1
        for index in range(len(scores)):
            file2.write(names[index] + "," + str(scores[index]) + "\n")
    elif value == 1:  # player
        index = 1
        scores[index] = int(scores[index]) + 1
        for index in range(len(scores)):
            file2.write(names[index] + "," + str(scores[index]) + "\n")
    file2.close()
    draw_scores()


def draw_scores():
    scorer.clear()
    index = 0
    scorer.goto(-OFFSET, OFFSET + WIDTH/6)
    for i in range(len(scores)):
        scorer.write(names[index] + ":" + str(scores[index]),
                     font=("comic sans", 18, "normal"))
        index += 1
        scorer.goto(-OFFSET + WIDTH*2, scorer.ycor())


def get_scores():
    file2 = open(SCORES_FILE, "r")
    for line in file2:
        name = ""
        score = ""
        index = 0
        while (line[index] != ","):
            name = name + line[index]
            index = index + 1
        names.append(str(name))
        while (line[index] == ","):
            index = index + 1
        while (line[index] != "\n"):
            score = score + line[index]
            index = index + 1
        scores.append(int(score))
    file2.close()


def check_player(ind):  # checks who is playing that turn and then draws their corresponding shape
    if PLAYER_TURN == 1:
        numlist[ind] = PLAYER_LETTER
        draw_shape(PLAYER_LETTER)
    elif PLAYER_TURN == 0:
        numlist[ind] = COMPUTER_LETTER
        draw_shape(COMPUTER_LETTER)


def check(number):
    ind = int(number) - 1
    if number == "1":
        if numlist[ind] == "1":
            pencil.goto(C1, R1)
            check_player(ind)
    elif number == "2":
        if numlist[ind] == "2":
            pencil.goto(C2, R1)
            check_player(ind)
    elif number == "3":
        if numlist[ind] == "3":
            pencil.goto(C3, R1)
            check_player(ind)
    elif number == "4":
        if numlist[ind] == "4":
            pencil.goto(C1, R2)
            check_player(ind)
    elif number == "5":
        if numlist[ind] == "5":
            pencil.goto(C2, R2)
            check_player(ind)
    elif number == "6":
        if numlist[ind] == "6":
            pencil.goto(C3, R2)
            check_player(ind)
    elif number == "7":
        if numlist[ind] == "7":
            pencil.goto(C1, R3)
            check_player(ind)
    elif number == "8":
        if numlist[ind] == "8":
            pencil.goto(C2, R3)
            check_player(ind)
    elif number == "9":
        if numlist[ind] == "9":
            pencil.goto(C3, R3)
            check_player(ind)


def check_and_send(number):
    def send():
        global PLAYER_TURN
        if PLAYER_TURN == 1:
            check(number)
        elif PLAYER_TURN == 0:
            numlist2 = []
            for index in numlist:
                if index != "x":
                    if index != "o":
                        numlist2.append(index)
            ind1 = rand.randint(0, len(numlist2) - 1)
            num = numlist2[ind1]
            check(num)
        pencil.goto(pencil_default)
        check_win()
        if PLAYER_TURN == 0:
            PLAYER_TURN = 1
        else:
            PLAYER_TURN = 0
    return send


def check_win():
    writer.clear()
    pencil.pensize(6)
    pencil.pencolor("black")
    if PLAYER_TURN == 0:
        writer.write("Player's move", move=False, align="center",
                     font=('comic sans', 15, 'bold'))
        winn_msg = "Computer wins"
    else:
        win_msg = "Player wins"
        writer.write("Computer's move", move=False, align="center",
                     font=('comic sans', 15, 'bold'))
    if numlist[0] == numlist[1] == numlist[2]:
        writer.clear()
        writer.write(win_msg, move=False, align="center",
                     font=('comic sans', 20, 'bold'))
        pencil.goto(C1, R1)
        pencil.pendown()
        pencil.goto(C3, R1)
        update_scores(PLAYER_TURN)
    elif numlist[3] == numlist[4] == numlist[5]:
        writer.clear()
        writer.write(win_msg, move=False, align="center",
                     font=('comic sans', 20, 'bold'))
        pencil.goto(C1, R2)
        pencil.pendown()
        pencil.goto(C3, R2)
        update_scores(PLAYER_TURN)
    elif numlist[6] == numlist[7] == numlist[8]:
        writer.clear()
        writer.write(win_msg, move=False, align="center",
                     font=('comic sans', 20, 'bold'))
        pencil.goto(C1, R3)
        pencil.pendown()
        pencil.goto(C3, R3)
        update_scores(PLAYER_TURN)
    elif numlist[0] == numlist[3] == numlist[6]:
        writer.clear()
        writer.write(win_msg, move=False, align="center",
                     font=('comic sans', 20, 'bold'))
        pencil.goto(C1, R1)
        pencil.pendown()
        pencil.goto(C1, R3)
        update_scores(PLAYER_TURN)
    elif numlist[1] == numlist[4] == numlist[7]:
        writer.clear()
        writer.write(win_msg, move=False, align="center",
                     font=('comic sans', 20, 'bold'))
        pencil.goto(C2, R1)
        pencil.pendown()
        pencil.goto(C2, R3)
        update_scores(PLAYER_TURN)
    elif numlist[2] == numlist[5] == numlist[8]:
        writer.clear()
        writer.write(win_msg, move=False, align="center",
                     font=('comic sans', 20, 'bold'))
        pencil.goto(C3, R1)
        pencil.pendown()
        pencil.goto(C3, R3)
        update_scores(PLAYER_TURN)
    elif numlist[0] == numlist[4] == numlist[8]:
        writer.clear()
        writer.write(win_msg, move=False, align="center",
                     font=('comic sans', 20, 'bold'))
        pencil.goto(C1, R1)
        pencil.pendown()
        pencil.goto(C3, R3)
        update_scores(PLAYER_TURN)
    elif numlist[6] == numlist[4] == numlist[2]:
        writer.clear()
        writer.write(win_msg, move=False, align="center",
                     font=('comic sans', 20, 'bold'))
        pencil.goto(C1, R3)
        pencil.pendown()
        pencil.goto(C3, R1)
        update_scores(PLAYER_TURN)
    pencil.penup()
    pencil.goto(pencil_default)


def draw_shape(LETTER):
    pencil.pensize(4)
    # x letter drawing
    if LETTER == "x":
        pencil.pencolor("red")
        pencil.setheading(X_ANGLE)
        pencil.forward(X_LENGTH)
        pencil.pendown()
        pencil.setheading(X_ANGLE + 180)
        pencil.forward(X_LENGTH * 2)
        wn.tracer(False)
        pencil.backward(X_LENGTH)
        pencil.setheading(-X_ANGLE)
        pencil.backward(X_LENGTH)
        wn.tracer(True)
        pencil.forward(X_LENGTH * 2)
        pencil.penup()
    # o letter drawing
    if LETTER == "o":
        pencil.goto(pencil.xcor(), pencil.ycor()-WIDTH/6)
        pencil.pendown()
        pencil.pencolor("blue")
        pencil.circle(25)
        pencil.penup()
        pencil.goto(pencil.xcor(), pencil.ycor()+WIDTH/6)
    pencil.setheading(0)


board()
get_scores()
draw_scores()

wn.tracer(True)

wn.addshape(PENCIL_IMAGE)
pencil = trtl.Turtle(shape=PENCIL_IMAGE)
pencil.speed(10)
pencil.penup()
pencil.ht()
pencil.shape(PENCIL_IMAGE)
pencil_default = (-OFFSET+WIDTH*3.5, OFFSET-WIDTH*1.5)
pencil.goto(pencil_default)
pencil.st()
wn.update()

go_first = rand.randint(0, 1)
if go_first == 0:
    PLAYER_TURN = 0
    writer.write("Computer goes first, press any number 1-9",
                 move=False, align="center", font=('comic sans', 15, 'bold'))
if go_first == 1:
    PLAYER_TURN = 1
    writer.write("Player goes first, press a number 1-9", move=False,
                 align="center", font=('comic sans', 15, 'bold'))

x_o = rand.randint(0, 1)
writer.goto(writer.xcor(), writer.ycor()-WIDTH/5)
if x_o == 0:
    PLAYER_LETTER = "x"
    COMPUTER_LETTER = "o"
    writer.write("Player will be 'x', Computer will be 'o'",
                 move=False, align="center", font=('comic sans', 15, 'bold'))
if x_o == 1:
    PLAYER_LETTER = "o"
    COMPUTER_LETTER = "x"
    writer.write("Player will be 'o', Computer will be 'x'",
                 move=False, align="center", font=('comic sans', 15, 'bold'))
writer.goto(writer.xcor(), writer.ycor()+WIDTH/5)
for number in numlist:
    wn.onkeypress(check_and_send(number), number)

wn.listen()
wn.mainloop()
