from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Welcome to Tic-Tac-Toe")
ico = Image.open('Red_TicTacToe.PNG')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

#Restart Game
def reset_game():
    """
    This function is used to reset the game and Building Buttons For the Board
    :return:
    """
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global b_clicked,count
    b_clicked =True
    count = 0
    b1 = Button(root, text=' ', font=("Arial", 20), height=3, width=6,
                bg="SystemButtonFace", command=lambda: button_click(b1))

    b2 = Button(root, text=' ', font=("Arial", 20), height=3, width=6,
                bg="SystemButtonFace", command=lambda: button_click(b2))
    b3 = Button(root, text=' ', font=("Arial", 20), height=3, width=6,
                bg="SystemButtonFace", command=lambda: button_click(b3))
    b4 = Button(root, text=' ', font=("Arial", 20), height=3, width=6,
                bg="SystemButtonFace", command=lambda: button_click(b4))
    b5 = Button(root, text=' ', font=("Arial", 20), height=3, width=6,
                bg="SystemButtonFace", command=lambda: button_click(b5))
    b6 = Button(root, text=' ', font=("Arial", 20), height=3, width=6,
                bg="SystemButtonFace", command=lambda: button_click(b6))
    b7 = Button(root, text=' ', font=("Arial", 20), height=3, width=6,
                bg="SystemButtonFace", command=lambda: button_click(b7))
    b8 = Button(root, text=' ', font=("Arial", 20), height=3, width=6,
                bg="SystemButtonFace", command=lambda: button_click(b8))
    b9 = Button(root, text=' ', font=("Arial", 20), height=3, width=6,
                bg="SystemButtonFace", command=lambda: button_click(b9))



    # Grid our button to the screen

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


def disabled_all_buttons():
    """
    This function is used to disable all the buttons after the game is over
    :return:
    """
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)





def check_winner():
    """
    This function is used to check the winner of the game
    :return:
    """
    global winner
    winner = False
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X" or b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X" \
            or b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X" or \
            b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X" or\
            b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X" or \
            b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X" or \
            b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X" or \
            b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        winner=True
        messagebox.showinfo("Tic-Tac-Toe","Congratulations! X Wins the Game!! ")
        disabled_all_buttons()

    # Check for O wins !!
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O" or b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O" \
            or b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O" or \
            b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O" or\
            b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O" or \
            b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O" or \
            b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O" or \
            b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        winner=True
        messagebox.showinfo("Tic-Tac-Toe","Congratulations! O Wins the Game!! ")
        disabled_all_buttons()

    # Check if Tie
    if count == 9 and winner == False:
        messagebox.showinfo("Tic-Tac-Toe","Its a Tie!")
        disabled_all_buttons()






# X Define as True
b_clicked = True
count = 0 # for the option of tie in game !


#Button Click Function
def button_click(b :Button):
    """
    This function is used to check the button clicked by the user
    :param b:
    :return:
    """
    global b_clicked,count

    if b["text"] == " " and b_clicked == True :
        b["text"] = "X"
        b_clicked = False
        count+=1
        check_winner()
    elif b["text"] == " " and b_clicked == False :
         b["text"] = "O"
         b_clicked = True
         count += 1
         check_winner()
    else :
        messagebox.showerror("Tic Tac Toe","Hey! that box is already been "
                                           "selected as {} ,Please choose Another box ".format(b["text"]))


#Creating Menu

my_menu = Menu()
root.config(menu=my_menu)

#Creating Options for menu

Options = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Options",menu=Options)
Options.add_command(label="Reset Game",command=reset_game)

exit_game=Menu(Options,tearoff=False)
Options.add_command(label="Exit Game",command=quit)

reset_game()
root.mainloop()
