from tkinter import*

class MathsQuiz:
    def __init__(self,parent):
        self.HomeFrame = Frame(parent)
        self.HomeFrame.grid(row=0, column=0)
        
        #Title of Home Frame.
        self.TitleLable = Label(self.HomeFrame, text = "Welcome to Maths Quiz", bg = "black", fg = "white", width = 20, padx = 30, pady = 10, font = ("Time", "14", "bold italic"))
        self.TitleLable.grid(columnspan = 2)
        
        #Name label and entry.
        self.NameLabel = Label(self.HomeFrame, text = "Name: ", anchor = W, fg = "black", width = 10, padx = 30, pady = 10, font = ("Time", "12", "bold italic"))
        self.NameLabel.grid(row = 2, column = 0)
        
        self.NameInput = Entry(self.HomeFrame, width = 20)
        self.NameInput.grid(row = 2, column = 1)
        
        #Age label and entry.
        self.AgeLabel = Label(self.HomeFrame, text = "Age: ", anchor = W, fg = "black", width = 10, padx = 30, pady = 10, font = ("Time", "12", "bold italic"))
        self.AgeLabel.grid(row = 3, column = 0)
        
        self.AgeInput = Entry(self.HomeFrame, width = 20)
        self.AgeInput.grid(row = 3, column = 1)
        
        #Difficulty label and buttons.
        self.DifficultyLabel = Label(self.HomeFrame, text = "Choose Difficulty: ", fg = "black", width = 10, padx = 30, pady = 10, font = ("Time", "12", "bold italic"))
        self.DifficultyLabel.grid(row = 4, column = 0)
        
        self.Difficulties = ["Easy", "Medium", "Hard", "Extreme"]
        self.ChosenDifficulty = StringVar()
        self.ChosenDifficulty.set(0)
        self.DifficultyButtons = []
        
        for i in range(len(self.Difficulties)):
            button = Radiobutton(self.HomeFrame, variable = self.ChosenDifficulty, value = i, text = self.Difficulties[i], anchor = W, padx = 50, width = "5", height = "2")
            self.DifficultyButtons.append(button)
            button.grid(row = i+5, column = 0, sticky = W)
        
        #Next button.
        self.NextButton = Button(self.HomeFrame, text = 'Next', command = self.show_QuestionsFrame)
        self.NextButton.grid(row = 8, column = 1)
        
        self.QuestionsFrame = Frame(parent)
        self.HomeFrame.grid(row=0, column=1)
        
        self.QuestionsLabel = Label(self.QuestionsFrame, text = "Questions", bg = "black", fg = "white", width = 20, padx = 30, pady = 10, font = ("Time", "14", "bold italic"))
        self.QuestionsLabel.grid(columnspan = 2)
        
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