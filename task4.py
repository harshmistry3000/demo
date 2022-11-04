import tkinter as tk
from tkinter import *

root = Tk()
root.geometry("500x500")

def getCourselist():
    selectedCourses=[]
    curSelected=lb.curselection()
    for i in curSelected:
        c=lb.get(i)
        selectedCourses.append(c)
    print(selectedCourses)
#declaring Label
courses=Label(text="Select Courses")
courses.pack()
coursesList=['Software Develpoment','Animation','ITIMS','Digital Design']
lb=Listbox(font=("Arail",16),selectmode="multipal")
root.mainloop()