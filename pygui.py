import tkinter as tk 
from tkinter import ttk 
from tkinter import scrolledtext

win = tk.Tk()
win.title("Python GUI")
aLabel=ttk.Label(win,text="Name")
aLabel.grid(column=0,row=0)


def clickMe():
	action.configure(text='Hello ' + name.get())

	

ttk.Label(win,text="Enter a name: ").grid(column=0,row=0)

#button
action = ttk.Button(win, text="Click Me!", command=clickMe)   
action.grid(column=1,row=1)
name = tk.StringVar()
nameEntered=ttk.Entry(win,width=12,textvariable=name)
nameEntered.grid(column=0,row=1)
nameEntered.focus()

#combo box
ttk.Label(win,text="Choose a number:").grid(column=1,row=0)
number= tk.StringVar()
numberChosen= ttk.Combobox(win,width=12,textvariable=number)
numberChosen['values'] =(1,2,4,42,100)
numberChosen.grid(column=1,row=1)
numberChosen.current(0)


#3 checkbox
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win,text="Disabled",variable=chVarDis,state='disabled')

check1.select()
check1.grid(column=0,row=4,sticky=tk.W)
check1.select()
check1.grid(column=0,row=4,sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win,text="UnChecked",variable=chVarUn)

check2.deselect()
check2.grid(column=1,row=4,sticky=tk.W)



chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win,text="Checked",variable=chVarEn)

check3.select()
check3.grid(column=2,row=4,sticky=tk.W)

#radio

colors =["Blue","Gold","Red"]

radVar = tk.IntVar()
radVar.set(99)
def radCall():
	radSel=radVar.get()
	win.configure(background=colors[radSel])
 
for col in range(3):
	curRad = 'rad' + str(col)
	curRad = tk.Radiobutton(win,text=colors[col],variable=radVar,value=col,command=radCall)
	curRad.grid(column=col,row=5,sticky=tk.W)


#scolled text
scrolW = 30
scrolH = 3
scr = scrolledtext.ScrolledText(win,width=scrolW,height=scrolH,wrap=tk.WORD)
scr.grid(column=0,columnspan=3)

win.mainloop()