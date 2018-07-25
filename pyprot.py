from tkinter import *;
from tkinter import ttk
from Settings import *
from functions1 import *
import time
# import winshell
# import shutil
# import tempfile
# import os
# import shutil
# import subprocess
class pryprotclass:

    def onFrameConfigure(self, event):
        self.canvas1.configure(scrollregion=self.canvas1.bbox("all"))

    def callback(self):

        callingallfuncions=allfunctions1()

        #progressbar.start()

        progressbar.config(mode='determinate',maximum=7.0,value=0)
        callingallfuncions.opera()
        progressbar.step()
        callingallfuncions.jumplist()
        progressbar.step()
        callingallfuncions.runhistory()
        progressbar.step()
        callingallfuncions.recyclebin()
        progressbar.step()
        callingallfuncions.tempfiles()
        progressbar.step()
        callingallfuncions.clipboard()
        progressbar.step()
        callingallfuncions.dns()
        progressbar.step()
        progressbar.config(value=7.0)







        chromeclearlabel=Label(frame5,text="Opera Cleared")
        #firefoxclearlabel=Label(frame5,text="Firefox Cleared")
        explorerclearlabel=Label(frame5,text="Explorer Cleared")
        Systemclearlabel=Label(frame5,text="System Cleared")

        chromeclearlabel.config(pady=10,background="#FAF8F8",anchor="w")
        #firefoxclearlabel.config(pady=10,background="WHITE",anchor="w")
        explorerclearlabel.config(pady=10,background="WHITE",anchor="w")
        Systemclearlabel.config(pady=10,background="#FAF8F8",anchor="w")


        chromeclearlabel.pack(side=TOP,fill='x')

        #firefoxclearlabel.pack(side=TOP,fill='x')
        explorerclearlabel.pack(side=TOP,fill='x')
        Systemclearlabel.pack(side=TOP,fill='x')


    def settingsbuttonclick(self,master):
         frame2.pack_forget()
         obbj=Settingsclass1()
         obbj.callsettings(master)


    def PryProtbuttonclick(self,master):
    #     obbj2=Settingsclass1(master)
    #     obbj2.hidesettings()
    #
    #     #frame2.pack(fill="both", expand=True,side=RIGHT);
          print('hi')



    def cb(self,i):
        cc[i].select()


    def contruct1(self,master):


        global frame2
        frame2=Frame(master);
        #frame2.config( width=100 );
        frame2.configure(background='violet')
      #  frame2.pack_propagate(False) ;

        frame2.pack(fill="both", expand=True,side=RIGHT);

        #frame2.pack_forget()

#now left of pryport goes here



        framezz3=Frame(frame2)

        self.canvas1 = Canvas(framezz3, borderwidth=0, background="#f3f3f3")
        vsb = Scrollbar(framezz3, orient="vertical", command=self.canvas1.yview)
        self.canvas1.configure(yscrollcommand=vsb.set)

        self.canvas1.configure(width=225)
        self.canvas1.pack(side="left", fill="both", expand=True)
        vsb.pack(side="right", fill="y")

        frame3=Frame(self.canvas1);
        self.canvas1.create_window((4,4), window=frame3, anchor="nw")
        frame3.bind("<Configure>", self.onFrameConfigure),
        framezz3.pack()

        framezz3.config( width=300 )
        frame3.config( width=300 )
        frame3.configure(background='#f3f3f3')

        label=Label(frame3,text='ALL TASKS')
        label.configure(background="#f3f3f3",font="Courier 14 bold")
        label.pack(side=TOP,anchor="nw",padx=10,pady=10)
        #####now all the things

        operalolo=PhotoImage(file="./Images/operagif.gif")
        operalolo=operalolo.subsample(16,16)
        labelopera=Label(frame3,text="Opera")
        labelopera.config(image=operalolo)
        labelopera.config(background='#f3f3f3')
        labelopera.config(compound='left')
        labelopera.image=operalolo
        labelopera.pack(side=TOP,anchor="nw")

        global cc
        cc=[]
        for i1 in range(1,23):
            cc.append(i1)
        global ghistory
        ghistory =IntVar()
        cc[0]=Checkbutton(frame3,text="History",variable=ghistory,command=lambda:ghistory.set(1))
        cc[1]=Checkbutton(frame3,text="Cookies",variable=ghistory,command=lambda:ghistory.set(1))
        cc[2]=Checkbutton(frame3,text="Saved Passwords",variable=ghistory,command=lambda:ghistory.set(1))
        cc[3]=Checkbutton(frame3,text="Download History",variable=ghistory,command=lambda:ghistory.set(1))
        cc[4]=Checkbutton(frame3,text="Last Download Location",variable=ghistory,command=lambda:ghistory.set(1))

        for i1 in range (0,5):
            cc[i1].config(background='#f3f3f3',state=NORMAL)
            cc[i1].select()
        for i1 in range (0,5):
            cc[i1].pack(anchor="nw",padx=30)



        # firefoxlogo=PhotoImage(file="./Images/firefox.gif")
        #
        # firefoxlogo=firefoxlogo.subsample(18,18)
        # labelfirefox=Label(frame3,text="Firefox")
        # labelfirefox.config(background='#f3f3f3')
        #
        # labelfirefox.config(image=firefoxlogo)
        # labelfirefox.config(compound='left')
        # labelfirefox.image=firefoxlogo
        # labelfirefox.pack(side=TOP,anchor="nw")

        cc[5]=Checkbutton(frame3,text="Synchroniztion Data",variable=ghistory,command=lambda:ghistory.set(1))
        cc[6]=Checkbutton(frame3,text="Bookmarks",variable=ghistory,command=lambda:ghistory.set(1))
        cc[7]=Checkbutton(frame3,text="Current Sessionss",variable=ghistory,command=lambda:ghistory.set(1))
        cc[8]=Checkbutton(frame3,text="Last Closed Tab Cache",variable=ghistory,command=lambda:ghistory.set(1))
        cc[9]=Checkbutton(frame3,text="Last Shutdown Time",variable=ghistory,command=lambda:ghistory.set(1))
        cc[10]=Checkbutton(frame3,text="Preferences",variable=ghistory,command=lambda:ghistory.set(1))
        for i1 in range (5,11):
            cc[i1].config(background='#f3f3f3')
            cc[i1].select()
        for i1 in range (5,11):
            cc[i1].pack(anchor="nw",padx=30)

        #print(ghistory.get())




        # iexplorelogo=PhotoImage(file="./Images/iexplore.gif")
        #
        # iexplorelogo=iexplorelogo.subsample(12,12)
        # labeliexplore=Label(frame3,text="Internet Explorer")
        # labeliexplore.config(image=iexplorelogo)
        # labeliexplore.config(background='#f3f3f3')
        #
        # labeliexplore.config(compound='left')
        # labeliexplore.image=iexplorelogo
        # labeliexplore.pack(side=TOP,anchor="nw")
        # cc[10]=Checkbutton(frame3,text="History")
        # cc[11]=Checkbutton(frame3,text="Cookies")
        # cc[12]=Checkbutton(frame3,text="Last Download Location")
        # cc[13]=Checkbutton(frame3,text="Temporary Internet Files")
        # cc[14]=Checkbutton(frame3,text="Autocomplete Form History")
        #
        # for i1 in range (10,15):
        #     cc[i1].config(background='#f3f3f3')
        # for i1 in range (10,15):
        #     cc[i1].select()
        #     cc[i1].pack(anchor="nw",padx=30)



        explorerlogo=PhotoImage(file="./Images/explorer.gif")

        explorerlogo=explorerlogo.subsample(16,16)
        explorerlabel=Label(frame3,text="Windows Explorer")
        explorerlabel.config(image=explorerlogo)
        explorerlabel.config(background='#f3f3f3')

        explorerlabel.config(compound='left')
        explorerlabel.image=explorerlogo
        explorerlabel.pack(side=TOP,anchor="nw")

        cc[11]=Checkbutton(frame3,text=" Jump Lists",variable=ghistory,command=lambda:ghistory.set(1))
        cc[12]=Checkbutton(frame3,text="Run(in Start Menu)",variable=ghistory,command=lambda:ghistory.set(1))
        cc[13]=Checkbutton(frame3,text="Recycle Bin",variable=ghistory,command=lambda:ghistory.set(1))
        for i1 in range (11,14):
            cc[i1].select()
            cc[i1].config(background='#f3f3f3')
        for i1 in range (11,14):
            cc[i1].pack(anchor="nw",padx=30)



        systemlogo=PhotoImage(file="./Images/system.gif")

        systemlogo=systemlogo.subsample(16,16)
        systemlabel=Label(frame3,text="System")
        systemlabel.config(image=systemlogo)
        systemlabel.config(background='#f3f3f3')

        systemlabel.config(compound='left')
        systemlabel.image=systemlogo
        systemlabel.pack(side=TOP,anchor="nw")
        #cc[14]=Checkbutton(frame3,text="Recycle Bin",variable=ghistory,command=lambda:ghistory.set(1))
        cc[14]=Checkbutton(frame3,text="Temporary Files",variable=ghistory,command=lambda:ghistory.set(1))
        cc[15]=Checkbutton(frame3,text="Clipboard",variable=ghistory,command=lambda:ghistory.set(1))
        cc[16]=Checkbutton(frame3,text="DNS Cache",variable=ghistory,command=lambda:ghistory.set(1))
        for i1 in range (14,17):
            cc[i1].select()
            cc[i1].config(background='#f3f3f3')
        for i1 in range (14,17):
            cc[i1].pack(anchor="nw",padx=30)









        framezz3.pack(fill="y", expand=False,side="left");
###########################################################################################



#the right of PryProt goes here down  now
        frame4=Frame(frame2);
        #frame4.config( width=300 );
        frame4.configure(background='WHITE')
        frame4.pack_propagate(False) ;
        global frame5
        frame5=Frame(frame4)
        frame5.configure(background="WHITE")

        #frame5.config(relief=RAISED)
        global progressbar
        progressbar=ttk.Progressbar(frame4,orient=HORIZONTAL)
        #progressbar.config(mode='indeterminate')
        progressbar.pack(fill=BOTH,padx=20,pady=15)
        run_PryPro=Button(frame4,text="RUN",command = lambda:self.callback())
        run_PryPro.config(command= lambda:self.callback())


        frame5.configure(height=300)
        frame5.pack(fill=BOTH,expand=True,padx=20)
        run_PryPro.pack(padx=60,pady=25,ipadx=20,ipady=10)
        #run_PryPro.pack(relx=1.0,x=-10,anchor='se')




        frame4.pack(fill="both", expand=True,side="right");





####################################################################################################
