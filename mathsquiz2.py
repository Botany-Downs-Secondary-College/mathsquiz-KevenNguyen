from tkinter import*
from random import*

class MathsQuiz:
    def __init__(self,parent):
        self.HomeFrame = Frame(parent)
        self.HomeFrame.grid(row=0, column=0)
        
        self.TitleLable = Label(self.HomeFrame, text = "Welcome to Maths Quiz", bg = "black", fg = "white", width = 20, padx = 30, pady = 10, font = ("Time", "14", "bold italic"))
        self.TitleLable.grid(columnspan = 4)
        
        self.NextButton = Button(self.HomeFrame, text = 'Next', command = self.show_QuestionsFrame)
        self.NextButton.grid(row = 8, column = 1)
        
        self.QuestionsFrame = Frame(parent)
        self.HomeFrame.grid(row=0, column=1)
        
        self.QuestionsLabel = Label(self.QuestionsFrame, text = "Questions", bg = "black", fg = "white", width = 20, padx = 30, pady = 10, font = ("Time", "14", "bold italic"))
        self.QuestionsLabel.grid(columnspan = 4)
        
        self.HomeButton = Button(self.QuestionsFrame, text = "Home", command = self.show_HomeFrame)
        self.HomeButton.grid(row = 8, column = 1)
        
    def show_HomeFrame(self):
        self.QuestionsFrame.grid_remove()
        self.HomeFrame.grid()
        
    def show_QuestionsFrame(self):
        self.HomeFrame.grid_remove()
        self.QuestionsFrame.grid()
        
if __name__ == "__main__":
    root = Tk()
    frames = MathsQuiz(root)
    root.title("Quiz")
    root.mainloop()