# Times table tester (Andre)


import random
from tkinter import *

class timetableinterface:
    def __init__(self, parent): # All of the follwing are widgets
        self.input = StringVar() 
        self.input.set(0)
        self.gen = question_generator()

        self.title = Label(parent, text = "Times table tester")
        self.title.grid(column=1, row=0)
        
        self.question = Label(parent, text = self.gen.question)
        self.question.grid(column=0, row=1, pady=20, padx=20)

        self.textbox = Entry(parent)
        self.textbox.grid(column=1, row=1)

        self.verify = Button(parent,text = "Check answer", command= self.displayanswer)
        self.verify.grid(column=1, row=3)

        self.next = Button(parent, text = "Next", command= self.updatequestions)
        self.next.grid(column=2, row=1, padx= 20)
        
        self.result = Label(parent, text= "")
        self.result.grid(column=0, row=4)

    def returninput(self): # Returns entrybox input
        return self.textbox.get()
        
    def displayanswer(self): # Checks entrybox answers and displays if it is correct or not
        self.result.configure(text= self.gen.displayanswer(self.returninput()))
    
    def updatequestions(self): # When next buttons is pressed, the class reruns and changes question accordingly
        self.textbox.delete(0, 'end')
        self.gen = question_generator()
        self.question["text"] = self.gen.question


# Data class
class question_generator:
    def __init__(self): #The following uses the imported random module to randomly generate numbers
        self.number1 = random.randint(1, 10)
        self.number2 = random.randint(1, 10)
        self.question = (f"{self.number1} x {self.number2} =")


    def answer(self):
        return self.number1 * self.number2

    
    def displayanswer(self, answer): #Returns if answer is correct or not, has basic error check
        try:
            if int(answer) == self.answer():
                return "Correct!"
            else:
                return "Incorrect!"
        except:
            return "Invalid input!"



if __name__ =="__main__":
    root = Tk()
    gui = timetableinterface(root)
    root.geometry("300x200")
    root.title("Times table tester")
    root.mainloop()
