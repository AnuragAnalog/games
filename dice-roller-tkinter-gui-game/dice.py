from tkinter import *
from random import randint

root = Tk()
root.title("Dice")
root.configure(bg="#d1f5d3")
root.iconbitmap(r'Dice.ico')
height = 520
width = 350
root.geometry(f"{width}x{height}")

# stylig and layout


f1 = Frame(root,borderwidth=1.9,relief="groove",bg="#75daad").place(relheight=0.07,relwidth=1)
l1= Label(f1,text="DICE",font="Helvetica 18 bold",bg="#75daad",fg="#231903",borderwidth=0.5,relief="groove").place(relheight=0.05,relwidth=0.24,relx=0.4,rely=0.068)

f2 = Frame(root,bg="#75daad").place(relheight=0.04,relwidth=1,rely=0.98)

# dice immages
dice_image = []

dice1 = PhotoImage(file="e:\programming\practice\dice1.png")
dice2 = PhotoImage(file="e:\programming\practice\dice2.png")
dice3 = PhotoImage(file="e:\programming\practice\dice3.png")
dice4 = PhotoImage(file="e:\programming\practice\dice4.png")
dice5 = PhotoImage(file="e:\programming\practice\dice5.png")
dice6 = PhotoImage(file="e:\programming\practice\dice6.png")

dice_image.append(dice1)
dice_image.append(dice2)
dice_image.append(dice3)
dice_image.append(dice4)
dice_image.append(dice5)
dice_image.append(dice6)

# dice function 

def roll():
    global output
    choose = randint(0,5)
    output = Label(root,image=f"{dice_image[choose]}").place(relx=0.36,rely=0.32)

    

# roll button
roll = Button(root,text="ROLL",font="Helvetica 7 bold",command=roll).place(relheight=0.08,relwidth=0.4,relx=0.33,rely=0.6)


root.mainloop()
