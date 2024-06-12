from tkinter import *
from tkinter import messagebox
import random

root=Tk()
root.title("TO-DO LIST")
root.geometry("500x300")
list_frame=Frame(root)
list_frame.pack()

listbox=Listbox(list_frame,height=20,width=50)
listbox.pack(side=LEFT)

scroller=Scrollbar(list_frame)
scroller.pack(side=RIGHT,fill=Y)

add_task=listbox(root,yscrollcommand=scroller.set)





root.mainloop()