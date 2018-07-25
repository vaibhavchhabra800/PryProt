from tkinter import *
from lefttoolbar import *
from pyprot import *
from logotop import *
from Settings import *
root=Tk()

class aclass:
      def __init__(self,master):

        obj_logotop=logotop1(root)
        obj_pryprot=pryprotclass()
        obj_pryprot.contruct1(root)
        obj_leftone=leftone(root)
        #obj_settings=Settingsclass1(root)




        icon=PhotoImage(file="./Images/minor-logo.png")
        icon = icon.subsample(7,6)
        root.tk.call('wm','iconphoto',root._w,icon)
        root.config(bg="white")
        root.title("PryProt")
        root.minsize(800, 500)



aobj=aclass(root)

root.mainloop()