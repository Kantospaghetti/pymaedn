from tkinter import *
data = open("questions.txt", "r")
output = open("questions.json", "w")
questions = []
question = {}

for line in data:
    if line[0] == "\n":
        questions.append(question)
        question = {}
    else:
        key, value = line.split(":", 1)
        question[key] = value.strip()

class Player:
    def __init__(self):
        self.points = 0

    def setPunkte():
        if getAnswer(): points += 1
        if getAnswer() == false: points -= 2
    def getPunkte():
        pass
class Application:
    def __init__(self, root):
        root.title("Quiz")
        root.geometry("600x600")
        entryAnswer = Entry(master=root, bg="lightgrey")
        entryAnswer.place(x=150, y=450, width=300, height=27)
        
        



    #def getAnswer():
        #Answer = (entryAnswer.get())


root = Tk()
Application(root)
root.mainloop()




