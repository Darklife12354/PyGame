import random
import tkinter.messagebox
from tkinter import *

window = Tk()
window.geometry('400x200')
window.configure(bg="black")
startMsg = Label(text="PyGame", font=('Times', 40), bg="black", fg="white")
startMsg.pack()


def gameWindow():
    game = Tk()
    game.title("PyGame")
    game.geometry('400x200')
    game.configure(background="black")
    num1 = random.randint(1, 50000)
    num2 = random.randint(1, 50000)
    sum_num = num1 + num2
    startMSg = Label(text="Lets play a game...", font=('Times', 40), bg="black", fg="white")
    question = Label(text="What's " + str(num1) + " + " + str(num2) + " ?", font=('Times', 30), bg="black", fg="white")
    answer = Entry(width=50, bg="black", fg="white", font=('Times', 20))

    def onclicksubmit():
        if not answer.get().isdigit():
            tkinter.messagebox.showinfo(title="Error!", message="You can only use numbers!")
        else:
            if int(answer.get()) == int(sum_num):
                tkinter.messagebox.showinfo(title="Correct!", message=f"The answer was {sum_num} !")
                yesOrNo = tkinter.messagebox.askyesno(title="Continue?", message="Do you wish to play the game again?")
                game.destroy()
                if yesOrNo:
                    gameWindow()
            else:
                tkinter.messagebox.showinfo(title="Wrong!", message=f"The correct answer is {sum_num}!")
                yesOrNo = tkinter.messagebox.askyesno(title="Continue?", message="Do you wish to play the game again?")
                game.destroy()
                if yesOrNo:
                    gameWindow()
    submit = Button(text="Submit Answer", background="gray", fg="white", font=('Times', 15), command=onclicksubmit)
    startMSg.pack()
    question.pack()
    answer.pack()
    submit.pack()
    game.mainloop()


def startgame():
    window.destroy()
    gameWindow()


button = Button(window, text="Start!", activebackground="lightblue", bg="grey", command=startgame, fg="white",
                font=('Times', 20))

button.pack()
window.mainloop()
