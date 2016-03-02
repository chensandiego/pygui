import tkinter as tk 
from tkinter import ttk 

win = tk.Tk()
win.title("Python GUI")
aLabel=ttk.Label(win,text="A label")
aLabel.grid(column=0,row=0)


def clickMe():
	action.configure(text="**I have been clicked**")
	aLabel.configure(foreground='red')
	
action =ttk.Button(win,text="Click me",command=clickMe)
action.grid(column=1,row=0)
win.mainloop()