from tkinter import*

class MathsQuiz:
    def __init__(self,parent):
        self.Welcome = Frame(parent)
        self.Welcome.grid(row=0, column=0)
        
        self.TitleLable = Label(self.Welcome, text = "Welcome to Maths Quiz", bg = "black", fg = "white", width = 20, padx = 30, pady = 10, font = ("Time", "14", "bold italic"))
        self.TitleLable.grid(columnspan = 2)
        
        self.NextButton = Button(self.Welcome, text = 'Next')
        self.NextButton.grid(row = 8, column = 1)
        
if __name__ == "__main__":
    root = Tk()
    frames = MathsQuiz(root)
    root.title("Quiz")
    root.mainloop()