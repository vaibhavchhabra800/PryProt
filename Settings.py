from tkinter import *

import tkinter as Tk
from tkinter import ttk
from pyprot import *
#from main import obj_pryprot
from sys import platform
import os
import re

#from virtual_memory import psutil
class Settingsclass1:


    def callsettings(self,master):
        self.construct2(master)

    def hidesettings(self):
        framesettings1.pack_forget()


    def calcram(self):
        #self.u = shutil.disk.usage()
       ''' mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')  # e.g. 4015976448
        mem_gib = mem_bytes/(1024.**3)
        return mem_bytes'''
    def shutdownpc(self):
        if platform == "linux" or platform == "linux2":
            os.system('shutdown now ')
        elif platform == 'darwin':
            os.system("shutdown -h now")
        else :


                 os.system('shutdown -s -t 1')


    def restartpc(self):
        if platform == "linux" or platform == "linux2":
            os.system('reebot now ')
        else:
            os.system('shutdown -r -t 1')


    def action(self):
        self.restartpc()



    def callback(self):
        self.shutdownpc()



    def afunccc(self):
        if platform == "linux" or platform == "linux2":
             return 'Linux'
        elif platform == "darwin":
              return 'OS X'
        elif platform == "win32":
            return 'Windows'


    def construct2(self,master):

        global framesettings1
        framesettings1=Frame(master)

        framesettings1.configure(background='WHITE')
        framesettings1.pack(fill="both", expand=True,side=RIGHT)

        lanel1=Label(framesettings1,text="")
        abb=self.afunccc()
        lanel1.config(text='Your Operating System is '+abb,padx=15,pady=15,background='WHITE',foreground='BLACK')
        lanel1.config(pady=80,padx=40,font="Courier 12 bold")
        lanel1.pack(side=LEFT,anchor="nw")
        button1 =Button(framesettings1,text='Shut Down PC',command= lambda: self.callback(),backgroun='white',foreground='blue',padx=10,pady=10)
        #button1.config(padx=40)
        button1.pack(side=LEFT,anchor='nw',pady=150)#,padx=10)

        button2 =Button(framesettings1,text='Restart PC',command= lambda: self.action(),background='white',foreground='blue',padx=10,pady=10)
        #button2.pack(side=TOP,anchor='sw',pady=0)#,padx=10)


