from tkinter import*
from tkinter import ttk
root = Tk()
def callback():
        print('i am clicked ')


button = ttk.Button(root,text='click me ',command=callback()).pack()





