from tkinter import*
from random import*
from tkinter import ttk
import datetime

class MathsQuiz:
    def __init__(self,parent):
        self.HomeFrame = Frame(parent)
        self.HomeFrame.grid(row=0, column=0)
        
        #Title of Home Frame.
        self.TitleLabel = Label(self.HomeFrame, text = "Welcome to Maths Quiz", bg = "black", fg = "white", width = 26, padx = 30, pady = 10, font = ("Time", "14", "bold italic"))
        self.TitleLabel.grid(columnspan = 2)
        
        self.InfoLabel = Label(self.HomeFrame, text = "This quiz is designed for students 8-13 years old.", font = ("Time", "10"))
        self.InfoLabel.grid(row = 2, columnspan = 2)
        
        #Name label and entry.
        self.NameLabel = Label(self.HomeFrame, text = "Name: ", anchor = W, fg = "black", width = 10, padx = 30, pady = 10, font = ("Time", "12", "bold italic"))
        self.NameLabel.grid(row = 3, column = 0)
        
        self.name = StringVar()
        self.name.set("")
        self.NameInput = ttk.Entry(self.HomeFrame, width = 20)
        self.NameInput.grid(row = 3, column = 1, columnspan = 2)
        
        #Age label and entry.
        self.AgeLabel = Label(self.HomeFrame, text = "Age: ", anchor = W, fg = "black", width = 10, padx = 30, pady = 10, font = ("Time", "12", "bold italic"))
        self.AgeLabel.grid(row = 4, column = 0)
        
        self.age = IntVar()
        self.age.set("")
        self.AgeInput = ttk.Entry(self.HomeFrame, width = 20)
        self.AgeInput.grid(row = 4, column = 1)
        
        #Difficulty label and buttons.
        self.DifficultyLabel = Label(self.HomeFrame, text = "Choose Difficulty: ", anchor = W, fg = "black", width = 11, padx = 30, pady = 10, font = ("Time", "12", "bold italic"))
        self.DifficultyLabel.grid(row = 5, column = 0)
        
        self.Difficulties = ["Easy", "Medium", "Hard"]
        self.ChosenDifficulty = StringVar()
        self.ChosenDifficulty.set(0)
        self.DifficultyButtons = []
        
        for i in range(len(self.Difficulties)):
            button = Radiobutton(self.HomeFrame, variable = self.ChosenDifficulty, value = i, text = self.Difficulties[i], anchor = W, padx = 50, width = "5", height = "2")
            self.DifficultyButtons.append(button)
            button.grid(row = i+6, column = 0, sticky = W)
            
        self.WarningText = Label(self.HomeFrame, text = "", anchor=W,
                                 fg = "red", width = 20, padx = 30, pady = 10)
        self.WarningText.grid(row=5, column=1)
        
        #Next button.
        self.NextButton = ttk.Button(self.HomeFrame, text = 'Next', command = self.show_QuestionsFrame)
        self.NextButton.grid(row = 8, column = 1)
        
        #Question page.
        
        self.index = 0
        self.score = 0
        
        self.QuestionsFrame = Frame(parent)
        self.HomeFrame.grid(row=0, column=1)
        
        self.QuestionsLabel = Label(self.QuestionsFrame, text = "Questions", bg = "black", fg = "white", width = 20, padx = 30, pady = 10, font = ("Time", "14", "bold italic"))
        self.QuestionsLabel.grid(columnspan = 3)
        
        self.Problems = Label(self.QuestionsFrame, text = "", pady = 10)
        self.Problems.grid(row = 1, column = 0)
        
        self.AnswerInput = ttk.Entry(self.QuestionsFrame, width = 20)
        self.AnswerInput.grid(row = 1, column = 1)
        
        self.ScoreLabel = Label(self.QuestionsFrame, text = "", pady= 10)
        self.ScoreLabel.grid(row = 1, column = 2)
        
        self.feedback = Label(self.QuestionsFrame, text = "", fg = "red")
        self.feedback.grid(row = 2, columnspan = 3)
        
        self.HomeButton = ttk.Button(self.QuestionsFrame, text = "Home", command = self.show_HomeFrame)
        self.HomeButton.grid(row = 8, column = 0)
        
        self.CheckButton = ttk.Button(self.QuestionsFrame, text = "Check Answer", command = self.check_answer)
        self.CheckButton.grid(row = 8, column = 2)
        
        #Results Page
        
        self.ResultsFrame = Frame(parent)
        self.ResultsFrame.grid_propagate(4)
        
        ResultsPage = ["Name", "Age", "Score"]
        self.ResultsLabels = []
        
        for i in range(len(ResultsPage)):
            ColumnHeading = Label(self.ResultsFrame, text = ResultsPage[i], width = "7", height = "2", font = ("Times", "14", "bold"))
            self.ResultsLabels.append(ColumnHeading)
            ColumnHeading.grid(row = 1, column = i+1)
            
        self.ResultsLabel = Label(self.ResultsFrame, text = "Results for Quiz", bg = "black", fg = "white", width = 26, padx = 30, pady = 10, font = ("Time", "14", "bold italic"))
        self.ResultsLabel.grid(row = 0, columnspan = 5)
            
        self.user_name = Label(self.ResultsFrame, textvariable = self.name)
        self.user_name.grid(row = 3, column = 1)
        
        self.user_age = Label(self.ResultsFrame, textvariable = self.age)
        self.user_age.grid(row = 3, column = 2)
        
        self.user_score = Label(self.ResultsFrame, text = "")
        self.user_score.grid(row = 3, column = 3)
        
        self.Home = ttk.Button(self.ResultsFrame, text = 'Home', command = self.show_HomeFrame)
        self.Home.grid(row = 4, column = 1)
        
        self.Exit = ttk.Button(self.ResultsFrame, text = 'Close', command = root.destroy)
        self.Exit.grid(row = 4, column = 3)
        
        self.report_treeview = ttk.Treeview(self.ResultsFrame)
        
        self.report_treeview.configure(columns=('age', 'score', 'date'))
        
        self.report_treeview.heading('#0', text='Name', anchor='w')
        self.report_treeview.column('#0', anchor='w')
        
        self.report_treeview.heading('age', text='Age')
        self.report_treeview.column('age', anchor='center')
        
        self.report_treeview.heading('score', text='Score')
        self.report_treeview.column('score', anchor='center')
        
        self.report_treeview.heading('date', text ='Date')
        self.report_treeview.column('date', anchor='center')
        
        self.DataHomeButton = ttk.Button(self.ResultsFrame, text="Home", command=self.HomeFrame)
                
    def show_HomeFrame(self):
        self.ResultsFrame.grid_remove()
        self.QuestionsFrame.grid_remove()
        self.HomeFrame.grid()
        
    def show_QuestionsFrame(self):
        
        try:
            if self.NameInput.get() == "":
                self.WarningText.configure(text = "Please enter a name: ")
                self.NameInput.focus()
                
            elif self.NameInput.get().isalpha() == False:
                self.WarningText.configure(text = "Please enter text, not numbers")
                self.NameInput.delete(0, END)
                self.NameInput.focus()
            
            elif self.AgeInput.get() == "":
                self.WarningText.configure(text = "Enter an age.")
                self.AgeInput.delete(0, END)
                self.AgeInput.focus()
                
            elif int(self.AgeInput.get()) > 14:
                self.WarningText.configure(text = "This quiz is designed for people under 14")
                self.AgeInput.delete(0,END)
                self.AgeInput.focus()
                     
            elif int(self.AgeInput.get()) < 0:
                self.WarningText.configure(text = "You are too old!")
                self.AgeInput.delete(0,END)
                self.AgeInput.focus()
                
            elif int(self.AgeInput.get()) < 7:
                self.WarningText.configure(text = "You are too young!")
                self.AgeInput.delete(0,END)
                self.AgeInput.focus() 
                
            else:
                self.name.set(self.NameInput.get())
                self.age.set(self.AgeInput.get())
                self.HomeFrame.grid_remove()
                self.QuestionsFrame.grid()
                self.NextQuestion()
                score_text = "Score = " + str(self.score)
                self.ScoreLabel.configure(text = score_text)
                
        except ValueError:
            self.WarningText.configure(text = "Please enter a number")
            self.AgeInput.delete(0, END)
            self.AgeInput.focus()
            
    def NextQuestion(self):
        x = randrange (10)
        y = randrange (10)
        self.answer = x + y
        self.index += 1
        
        questiontext = str(x) + " + " + str(y) + " = "
        self.Problems.configure(text = questiontext)
        self.QuestionsLabel.configure(text = "Quiz Question " + str(self.index) + "/3")
        if self.index >= 4:
            self.QuestionsFrame.grid_remove()
            self.ResultsFrame.grid(row = 1, columnspan = 4)
            
            self.report_treeview.grid(row=0, column=0)
            self.DataHomeButton.grid(row=1, column=0, sticky='w')
            
            with open('records.txt', 'a+') as data_file:
                data_file.write(self.name.get() + ' ' + str(self.age.get()) + ' ' + str(self.score + ' ' + '\n'))
                                
            self.display_all_data()
        
    def check_answer(self):
        try:
            ans = int(self.AnswerInput.get())
            
            if ans == self.answer:
                self.feedback.configure(text = "Correct Answer")
                self.score += 1
                score_text = "Score = " + str(self.score) + "/3"
                self.ScoreLabel.configure(text = score_text)
                self.user_score.configure(text = score_text)
                self.AnswerInput.delete(0, END)
                self.AnswerInput.focus()
                self.NextQuestion()
                
            else:
                self.feedback.configure(text = "Wrong Answer")
                self.AnswerInput.delete(0, END)
                self.AnswerInput.focus()
                self.NextQuestion()
                
        except ValueError:
            self.feedback.configure(text = "Please enter an answer")
            self.AnswerInput.delete(0, END)
            self.AnswerInput.focus()
            
    def Restart(self):
        self.Report_frame.grid_remove()
        restart = MathsQuiz(root)  
        
    def display_all_data(self):
        self.report_treeview.delete(*self.report_treeview.get_children())
        
        with open('records.txt', 'r') as scores_file:
            scores = []
            for line in scores_file.readlines():
                scores.append([line.split()[0], line.split()[1], line.split()[2], line.split()[3]])
                
            scores.sort(key=lambda score: (score[3], score[2], score[1], score[0]), reverse = True)
            for score in scores:
                self.report_treeview.insert('', 'end', text = score[0], values=(score[1], score[2], score[3]))
        
if __name__ == "__main__":
    root = Tk()
    frames = MathsQuiz(root)
    root.title("Quiz")
    root.mainloop()