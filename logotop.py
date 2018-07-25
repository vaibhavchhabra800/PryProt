from tkinter import *


class logotop1:
    def __init__(self,master):
        frame1=Frame(master);
        frame1.config( height=50 );
        frame1.configure(background='#4d4d4d')
        logoimage1=PhotoImage(file="./Images/minor-logo.png");

        logoimage1 = logoimage1.subsample(6,6)


        logo=Label(frame1,image=logoimage1);
        logo.image=logoimage1;
        logo.pack(padx=30,side="left");
        labelPryProt=Label(frame1,text="PryProt")
        labelPryProt.pack(side=LEFT,fill=BOTH,expand=False)
        labelPryProt.configure(background="#4d4d4d",foreground="WHITE",font="Helvetica 18 bold")













        frame1.pack_propagate(False) ;
        frame1.pack(fill="both", expand=False)


