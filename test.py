#Practicing Generating Questions.
#basicguiwithquestions.py    
#K.Nguyen Feb 2020

from tkinter import*
from random import*

root=Tk()
root.title("Frames")
root.geometry("600x300+850+0")

def Screen1():
    global frame1
    global frame2
    
    frame2.grid_remove()
    frame1 = LabelFrame(root, height = "450", width = "400", bg ="light blue")
    frame1.grid (row=0, column=0)
    
    TitleLabel=Label (frame1, bg="black", fg="white", width=20, padx=30, pady=1, text="Welcome to my Maths Quiz", font=("Times","14","bold"))
    TitleLabel.grid (columnspan = 2)

    text=Text(frame1, width=16, height=1, bg="light blue")
    text.insert(INSERT, "Are you over 12?")
    text.grid(row=1,column=0)

    radiobutton1=Radiobutton(frame1, text="Yes", value=1, bg="light blue")
    radiobutton1.grid(row=2,column=0)    
    
    radiobutton2=Radiobutton(frame1, text="No", value=2, bg="light blue")
    radiobutton2.grid(row=3,column=0)
    
    text=Text(frame1, width=10, height=1, bg="light blue")
    text.insert(INSERT, "Enter age:")
    text.grid(row=2,column=1)    
    
    entry=Entry(frame1)
    entry.grid(row=3,column=1)    
    
    button1=Button(frame1, text="Next Page", anchor = W, command = Screen2)
    button1.grid(row=4,column=0)
    
    
def Screen2():
    global frame1
    global frame2
    
    frame1.grid_remove()
    frame2 = LabelFrame(root,height="450",width="400", bg="green")
    frame2.grid(row=0, column=1)
    
    QuestionsPage=Label(frame2,bg="black",fg="white",width=20,padx=30,pady=10,
                     text="Questions", font=("Times","14","bold"))
    QuestionsPage.grid(columnspan=2)
    
    questions=Label(frame2,bg="green",width=15,height=3, text="")
    questions.grid(row=1,column=1, sticky = W)
    
    answer=Entry(frame2,width=20)
    answer.grid(row=1,column=1,sticky=W)
    
    homescreen=Button(frame2,text="Home Page",anchor=W,command=Screen1)
    homescreen.grid(row=10,column=0)
    
    checkanswer=Button(frame2,text="Check Answer",anchor=W,command=next_problem)
    checkanswer.grid(row=10,column=1)
    
def next_problem():
    x=randrange(10)
    y=randrange(10)
    answer=x+y
    
    problem_text=str(x) + " + " + str(y) + " = "
    questions.configure(text=problem_text)
    
frame1=Frame(root)
frame2=Frame(root)

Screen1()
root.mainloop()