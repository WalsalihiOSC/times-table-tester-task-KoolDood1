# Times table tester (Andre)


import random
from tkinter import *

class timetableinterface:
    def __init__(self, parent):
        self.input = StringVar()
        self.input.set(0)
        self.gen = question_generator()
        
        self.question = Label(parent, text = self.gen.question)
        self.question.grid(column=0, row=0, pady=20, padx=20)

        self.textbox = Entry(parent)
        self.textbox.grid(column=1, row=0)

        self.verify = Button(parent,text = "Check answer", command= self.displayanswer)
        self.verify.grid(column=1, row=2)#clear textbox

        self.next = Button(parent, text = "Next", command= self.generatequestion)
        self.next.grid(column=2, row=0)#clear textbox
        
        self.result = Label(parent, text= "")
        self.result.grid(column=0, row=3)


    def checkanswer(self): #Configures result label
        self.result.configure(text= self.q.answer(self.input.get()))


        

class question_generator:
    def __init__(self):
        self.number1 = random.randint(1, 10)
        self.number2 = random.randint(1, 10)
        


    def answer(self):
        return self.number1 * self.number2

    
    def displayanswer(self):
        answercheck = self.input.get()
        if int(answercheck) == self.answer():
            self.result.configure(text= "Correct!")
        else:
            self.result.configure(text="Incorrect!")



if __name__ =="__main__":
    root = Tk()
    gui = timetableinterface(root)
    root.geometry("300x300")
    root.title("Times table tester")
    root.mainloop()