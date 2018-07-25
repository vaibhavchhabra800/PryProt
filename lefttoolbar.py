from tkinter import *
from tkinter import ttk
from pyprot import *
from Settings import *



class leftone:


    def settingsclick(self,master):
        obj4=pryprotclass()
        obj4.settingsbuttonclick(master)
        #obbj=Settingsclass1(master)
        #obbj.callsettings()
        #print('nononoln')
        obj2=Settingsclass1()
    def pryprotbuttonclick(self,master):
        obj6=Settingsclass1()
        obj6.hidesettings()
        obj7=pryprotclass()
        obj7.contruct1(master)




    def __init__(self,master):



        frame2=Frame(master);
        frame2.config( width=100 );
        frame2.configure(background='#676767')
        frame2.pack_propagate(False) ;
        Pyprot_button=ttk.Button(frame2,text="PryProt")
        Pyprot_button.config(command=lambda: self.pryprotbuttonclick(master))


        cleanerimage=PhotoImage(file="./Images/cleanerimage.png")
        cleanerimage = cleanerimage.subsample(6,6)
        Pyprot_button.image=cleanerimage;
        Pyprot_button.config(image=cleanerimage,compound=TOP)

        Settings_button=ttk.Button(frame2,text="Settings")
        Pyprot_button.pack(fill="x",expand=False,ipady=20);
        Settings_button.config(command=lambda: self.settingsclick(master))
        style=ttk.Style()
        style.configure('TButton',font="Comic 10 ")

        #print(style.theme_use())


        gear=PhotoImage(file="./Images/gear.png")
        gear = gear.subsample(6,6)
        #logo=Label(frame1,image=logoimage1);
        Settings_button.image=gear;
        Settings_button.config(image=gear,compound=TOP)
        Settings_button.pack(fill="x",expand=False,ipady=20);








        frame2.pack(fill="y", expand=False,side=LEFT);
