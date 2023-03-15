'''main.py'''
import turtle as trtl
import random as rand


wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.tracer(False)
SCORES_FILE = "~/Documents/github/tictactoe/scores.txt"
PENCIL_IMAGE = "~/Documents/github/tictactoe/pencil.gif"
names = []
scores = []


drawer = trtl.Turtle()
drawer.ht()
WIDTH = 150
INDEX = 0
numlist = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
OFFSET = 180
drawer.penup()
drawer.goto(-OFFSET, OFFSET)
drawer.pendown()


scorer = trtl.Turtle()
scorer.ht()
scorer.penup()


x1 = drawer.xcor()
# left to right, top to bottom
C1 = WIDTH/2-OFFSET
C2 = WIDTH*3/2-OFFSET
C3 = WIDTH*5/2-OFFSET
R1 = -WIDTH/2+OFFSET
R2 = -WIDTH*3/2+OFFSET
R3 = -WIDTH*5/2+OFFSET


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


def check_player(ind):
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
        wn.tracer(True)
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
    if PLAYER_TURN == 0:
        win_msg = "Computer wins"
    else:
        win_msg = "Player wins"
    # preset winning game scenarios
    if numlist[0] == numlist[1] == numlist[2]:
        print(win_msg)
        update_scores(PLAYER_TURN)
    elif numlist[3] == numlist[4] == numlist[5]:
        print(win_msg)
        update_scores(PLAYER_TURN)
    elif numlist[6] == numlist[7] == numlist[8]:
        print(win_msg)
        update_scores(PLAYER_TURN)
    elif numlist[0] == numlist[3] == numlist[6]:
        print(win_msg)
        update_scores(PLAYER_TURN)
    elif numlist[1] == numlist[4] == numlist[7]:
        print(win_msg)
        update_scores(PLAYER_TURN)
    elif numlist[2] == numlist[5] == numlist[8]:
        print(win_msg)
        update_scores(PLAYER_TURN)
    elif numlist[0] == numlist[4] == numlist[8]:
        print(win_msg)
        update_scores(PLAYER_TURN)
    elif numlist[6] == numlist[4] == numlist[2]:
        print(win_msg)
        update_scores(PLAYER_TURN)


def draw_shape(LETTER):
    '''draws a shape'''
    pencil.pendown()
    if LETTER == "x":
        # placeholder until i find a good way to draw an x
        pencil.circle(20, 180, 4)
    if LETTER == "o":
        pencil.circle(20)
    pencil.penup()
    pencil.setheading(0)


board()
get_scores()
draw_scores()


# pencil
wn.addshape(PENCIL_IMAGE)
pencil = trtl.Turtle(shape=PENCIL_IMAGE)
pencil.speed(5)
pencil.penup()
pencil.ht()
pencil.shape(PENCIL_IMAGE)
pencil_default = (300, 0)
pencil.goto(pencil_default)
pencil.st()
wn.update()


go_first = rand.randint(0, 1)
if go_first == 0:
    PLAYER_TURN = 0  # not players turn
if go_first == 1:
    PLAYER_TURN = 1  # players turn


x_o = rand.randint(0, 1)
if x_o == 0:
    # print("player will be x, computer will be x")
    PLAYER_LETTER = "x"
    COMPUTER_LETTER = "o"
if x_o == 1:
    # print("player will be o, computer will be o")
    PLAYER_LETTER = "o"
    COMPUTER_LETTER = "x"


for number in numlist:
    wn.onkeypress(check_and_send(number), number)


wn.listen()
wn.mainloop()
