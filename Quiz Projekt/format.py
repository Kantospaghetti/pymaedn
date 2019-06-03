from tkinter import *
from random import randint
import re

ATTEMPTS = 3
LEVEL_POINTS = {
    "baby": 1,
    "easy": 2,
    "normal": 4,
    "hard": 8,
    "extreme": 10 
}

class Question:
    def __init__(self, Question="", Answer="", Level="normal", Category="Allgemein", Regexp=None, Tip=None):
        self.value = Question
        self.answer = Answer
        self.level = Level
        self.catergory = Category
        self.regexp = Regexp
        self.tip = Tip

    def check_answer(self, answer):
        if self.regexp:
            return re.search(self.regexp.upper(), answer.upper())
        else:
            return answer.upper() == self.answer.upper()

class Quiz:
    def __init__(self, root):
        self.root = root
        # tkinter
        root.title("Quiz")
        self.main = Frame(master=root, padx=10)
        self.main.pack(expand=True)
        label_question_info = Label(master=self.main, text="Frage:")
        label_question_info.pack()
        self.label_question = Label(master=self.main, wraplength=300, text="loading...")
        self.label_question.pack()
        label_answer = Label(master=self.main, text="Ihre Antwort:")
        label_answer.pack()
        self.entry_answer = Entry(master=self.main, bg="lightgrey", width=50)
        self.entry_answer.pack(fill=X, pady=5)
        self.label_right_answer_info = Label(master=self.main, text="Richtige Antwort:")
        self.label_right_answer = Label(master=self.main, text="loading...")
        self.button_answer = Button(master=root, text="Antworten", bg="#4286f4", disabledforeground="black", width=50, height=2, \
                                    command=lambda: self.validate_answer(self.entry_answer.get()))
        self.button_answer.pack(pady=10, padx=20)
        # gameplay
        self.questions = []
        self.question = None
        self.points = 0
        # start game
        self.load_questions()
        self.ask_question()

    def load_questions(self):
        data = open("questions.txt", "r", encoding='utf8')
        question = {}
        for line in data:
            if line[0] == "\n":
                self.questions.append(Question(**question))
                question = {}
            else:
                key, value = line.split(":", 1)
                question[key] = value.strip()
    
    def ask_question(self):
        self.question = self.questions[randint(0, len(self.questions)-1)]
        self.questions.remove(self.question)
        self.label_question.config(text=self.question.value)
        self.button_answer.config(state=NORMAL, bg="#4286f4")
        self.label_right_answer_info.pack_forget()
        self.label_right_answer.pack_forget()
        self.entry_answer.delete(0, 'end')
        self.entry_answer.focus_set()

    def validate_answer(self, answer):
        if self.question.check_answer(answer):
            # correct answer
            self.points += LEVEL_POINTS[self.question.level]
            self.button_answer.config(state=DISABLED, bg="green")
        else:
            # wrong anser
            self.points -= 1
            self.button_answer.config(state=DISABLED, bg="red")
            self.label_right_answer_info.pack()
            self.label_right_answer.config(text=self.question.answer)
            self.label_right_answer.pack()
        self.root.after(2000, self.ask_question)
        
        
root = Tk()
Quiz(root)

root.mainloop()

