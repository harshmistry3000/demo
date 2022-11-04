from tkinter import *
import tkinter as tk 
root = Tk()
root.geometry("300x200")

w = Label(root,text='GUJ UNI',font="50" ).pack()

Checkbutton1=tk.IntVar()
Checkbutton2=tk.IntVar()
Checkbutton3=tk.IntVar()
Checkbutton4=tk.IntVar()

Button1=Checkbutton(root,text="tutorial",variable=Checkbutton1,onvalue=0,offvalue=1,height=2,width=10)
Button2=Checkbutton(root,text="Student",variable=Checkbutton2,onvalue=0,offvalue=0,height=2,width=10)
Button3=Checkbutton(root,text="Course",variable=Checkbutton3,onvalue=0,offvalue=0,height=2,width=10)
Button4=Checkbutton(root,text="Teacher",variable=Checkbutton4,onvalue=0,offvalue=0,height=2,width=10)

Button1.pack()
Button2.pack()
Button3.pack()
Button4.pack()

root.mainloop()