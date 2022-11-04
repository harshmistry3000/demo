from tkinter import Tk, messagebox
root = Tk()

root.geometry("300x300")

messagebox.showinfo("Info","Saved Successfully")
messagebox.showerror("Error")
root.mainloop()