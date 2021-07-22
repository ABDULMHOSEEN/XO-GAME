# This is a XO game

# Fist of all I will import the Tkinter
from tkinter import *
from tkinter.font import Font
import pygame

# for some sound

def sound(number):
    pygame.mixer.init()
    if number == 1:
        pygame.mixer.music.load("lose.mp3")
        pygame.mixer.music.play(loops=0)
    elif number == 2:
        pygame.mixer.music.load("start game.mp3")
        pygame.mixer.music.play(loops=0)

# make a root
root = Tk()
# Give a title name
root.title("XO Game")
# add icon
root.iconbitmap("xo_game2.ico")

# Make a list that will be used to know how win
list_XO = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
# Define a font
title_font = Font(
    family="Bahnschrift Light Condensed",
    size=20,
    weight="bold")
box_font = Font(
    family="Helvetica",
    size=12,
    weight="bold")

# display who is tern and define the color
turn = "O"
colour = "#D1E3D1"
# Make a label with some information
label = Label(root, text="Player_1 (" + turn + ")", padx=75, pady=20, font=title_font).grid(row=0, column=0,
                                                                                            columnspan=3)


# renew the game
def again():
    sound(2)
    root.geometry("270x350")
    global check
    global colour
    global list_XO
    global turn
    # renew the list
    list_XO = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
    # renew the buttons
    button1 = Button(root, text=" # ", padx=30, pady=30, font=box_font, command=lambda: XO(1)).grid(row=1, column=0)
    button2 = Button(root, text=" # ", padx=30, pady=30, font=box_font, command=lambda: XO(2)).grid(row=1, column=1)
    button3 = Button(root, text=" # ", padx=30, pady=30, font=box_font, command=lambda: XO(3)).grid(row=1, column=2)

    button4 = Button(root, text=" # ", padx=30, pady=30, font=box_font, command=lambda: XO(4)).grid(row=2, column=0)
    button5 = Button(root, text=" # ", padx=30, pady=30, font=box_font, command=lambda: XO(5)).grid(row=2, column=1)
    button6 = Button(root, text=" # ", padx=30, pady=30, font=box_font, command=lambda: XO(6)).grid(row=2, column=2)

    button7 = Button(root, text=" # ", padx=30, pady=30, font=box_font, command=lambda: XO(7)).grid(row=3, column=0)
    button8 = Button(root, text=" # ", padx=30, pady=30, font=box_font, command=lambda: XO(8)).grid(row=3, column=1)
    button9 = Button(root, text=" # ", padx=30, pady=30, font=box_font, command=lambda: XO(9)).grid(row=3, column=2)

    # Make check as False
    check = False
    # renew the win par
    turn = "O"
    colour = "#D1E3D1"
    # Make a label with some information
    label = Label(root, text="Player_1 (" + turn + ")", padx=75, pady=20, font=title_font).grid(row=0, column=0,
                                                                                                columnspan=3)


# Function to check if there are a winner
def win(number):
    global check
    # Not finish amd no win
    if number == 0:
        pass
    elif number == 1:
        sound(1)
        root.geometry("270x445")
        check = True
        # O is win in this case
        label_win = Label(root, text="The winner is O", padx=60, pady=20, bg="#D1E3D1", font=title_font).grid(row=0,
                                                                                                             column=0,
                                                                                                              columnspan=3)
        renew_button = Button(root, text="Play Again!", padx=73, pady=20, font=title_font,
                              command=lambda: again(),bg = "#ebb973").grid(row=4,
                                                            column=0,
                                                            columnspan=3)

    elif number == 2:
        sound(1)
        root.geometry("270x445")
        check = True
        # X is win in this case
        label_win = Label(root, text="The winner is X", padx=60, pady=20, bg="#65c5f7", font=title_font).grid(row=0,
                                                                                                              column=0,
                                                                                                              columnspan=3)
        renew_button = Button(root, text="Play Again!", padx=73, pady=20, font=title_font,
                              command=lambda: again(),bg = "#ebb973").grid(row=4,
                                                            column=0,
                                                            columnspan=3)

    elif number == -1:
        sound(1)
        root.geometry("270x445")
        # no one win
        label_win = Label(root, text="NO BODY WIN", padx=73, pady=20, bg="#d93838", font=title_font).grid(row=0,
                                                                                                          column=0,
                                                                                                          columnspan=3)
        renew_button = Button(root, text="Play Again!", padx=73, pady=20, font=title_font,
                              command=lambda: again(),bg = "#ebb973").grid(row=4,
                                                            column=0,
                                                            columnspan=3)


# This function is made to make the changes that happen
check = False


def XO(number):
    # Make the value as global
    global turn
    global colour
    global list_XO
    if check:
        pass

    else:
        # set the value that will be used in the list to know who win
        if turn == "O":
            value = 1
        else:
            value = 2
        # Check where the player click and change
        if number == 1:
            button1 = Button(root, text=turn, padx=30, pady=30, bg=colour, font=box_font).grid(row=1, column=0)
            list_XO[0][0] = value
        elif number == 2:
            button2 = Button(root, text=turn, padx=30, pady=30, bg=colour, font=box_font).grid(row=1, column=1)
            list_XO[0][1] = value
        elif number == 3:
            button3 = Button(root, text=turn, padx=30, pady=30, bg=colour, font=box_font).grid(row=1, column=2)
            list_XO[0][2] = value

        elif number == 4:
            button3 = Button(root, text=turn, padx=30, pady=30, bg=colour, font=box_font).grid(row=2, column=0)
            list_XO[1][0] = value
        elif number == 5:
            button3 = Button(root, text=turn, padx=30, pady=30, bg=colour, font=box_font).grid(row=2, column=1)
            list_XO[1][1] = value
        elif number == 6:
            button3 = Button(root, text=turn, padx=30, pady=30, bg=colour, font=box_font).grid(row=2, column=2)
            list_XO[1][2] = value

        elif number == 7:
            button3 = Button(root, text=turn, padx=30, pady=30, bg=colour, font=box_font).grid(row=3, column=0)
            list_XO[2][0] = value
        elif number == 8:
            button3 = Button(root, text=turn, padx=30, pady=30, bg=colour, font=box_font).grid(row=3, column=1)
            list_XO[2][1] = value
        elif number == 9:
            button3 = Button(root, text=turn, padx=30, pady=30, bg=colour, font=box_font).grid(row=3, column=2)
            list_XO[2][2] = value

        # Change the turn from the Player to the next one
        if turn == "X":
            turn = "O"
            colour = "#D1E3D1"
            label = Label(root, text="Player_1 (" + turn + ")", padx=75, pady=20, font=title_font).grid(row=0, column=0,
                                                                                                        columnspan=3)
        else:
            turn = "X"
            colour = "#65c5f7"
            label = Label(root, text="Player_2 (" + turn + ")", padx=75, pady=20, font=title_font).grid(row=0, column=0,
                                                                                                        columnspan=3)

        # Check if there are a win
        board_line = []
        for i in list_XO:
            for j in i:
                board_line.append(j)
        if (1 == board_line[0]) and (1 == board_line[1]) and (1 == board_line[2]):
            win(1)
        elif (2 == board_line[0]) and (2 == board_line[1]) and (2 == board_line[2]):
            win(2)

        elif (1 == board_line[3]) and (1 == board_line[4]) and (1 == board_line[5]):
            win(1)
        elif (2 == board_line[3]) and (2 == board_line[4]) and (2 == board_line[5]):
            win(2)

        elif (1 == board_line[6]) and (1 == board_line[7]) and (1 == board_line[8]):
            win(1)
        elif (2 == board_line[6]) and (2 == board_line[7]) and (2 == board_line[8]):
            win(2)

        elif (1 == board_line[0]) and (1 == board_line[3]) and (1 == board_line[6]):
            win(1)
        elif (2 == board_line[0]) and (2 == board_line[3]) and (2 == board_line[6]):
            win(2)

        elif (1 == board_line[1]) and (1 == board_line[4]) and (1 == board_line[7]):
            win(1)
        elif (2 == board_line[1]) and (2 == board_line[4]) and (2 == board_line[7]):
            win(2)

        elif (1 == board_line[2]) and (1 == board_line[5]) and (1 == board_line[8]):
            win(1)
        elif (2 == board_line[2]) and (2 == board_line[5]) and (2 == board_line[8]):
            win(2)

        elif (1 == board_line[0]) and (1 == board_line[4]) and (1 == board_line[8]):
            win(1)
        elif (2 == board_line[0]) and (2 == board_line[4]) and (2 == board_line[8]):
            win(2)

        elif (1 == board_line[2]) and (1 == board_line[4]) and (1 == board_line[6]):
            win(1)
        elif (2 == board_line[2]) and (2 == board_line[4]) and (2 == board_line[6]):
            win(2)

        elif 0 in board_line:
            win(0)
        else:
            win(-1)


# Make the buttons
button1 = Button(root, text=" # ", padx=30, pady=30, font=box_font, command=lambda: XO(1)).grid(row=1, column=0)
button2 = Button(root, text=" # ", padx=30, pady=30, font=box_font, command=lambda: XO(2)).grid(row=1, column=1)
button3 = Button(root, text=" # ", padx=30, pady=30, font=box_font, command=lambda: XO(3)).grid(row=1, column=2)

button4 = Button(root, text=" # ", padx=30, pady=30, font=box_font, command=lambda: XO(4)).grid(row=2, column=0)
button5 = Button(root, text=" # ", padx=30, pady=30, font=box_font, command=lambda: XO(5)).grid(row=2, column=1)
button6 = Button(root, text=" # ", padx=30, pady=30, font=box_font, command=lambda: XO(6)).grid(row=2, column=2)

button7 = Button(root, text=" # ", padx=30, pady=30, font=box_font, command=lambda: XO(7)).grid(row=3, column=0)
button8 = Button(root, text=" # ", padx=30, pady=30, font=box_font, command=lambda: XO(8)).grid(row=3, column=1)
button9 = Button(root, text=" # ", padx=30, pady=30, font=box_font, command=lambda: XO(9)).grid(row=3, column=2)

root.mainloop()
