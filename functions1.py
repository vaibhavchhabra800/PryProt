from tkinter import *;
from tkinter import ttk
from Settings import *
from ctypes import windll
import winshell
import winreg as wreg
import shutil
import tempfile
import os
import socket
import shutil
import subprocess
class allfunctions1:
    def dns(self):
        socket.gethostbyname('test.somedomain.com')

    def recyclebin(self):
        try:
            winshell.recycle_bin().empty(confirm=False, show_progress=True, sound=False)
        except:
            z=5


    # def chrome(self):
    #     os.remove("C:\\Users\\Anurag\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History")
    #     driver.manage().deleteAllCookies()



    def tempfiles(self):
        del_dir = r'C:\\Users\\Anurag\\AppData\\Local\\Temp'
        pObj = subprocess.Popen('del /S /Q /F %s\\*.*' % del_dir, shell=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        rTup = pObj.communicate()
        rCod = pObj.returncode
        try:
            os.rmdir(del_dir)
        except:
            print("tempfiles")
        if rCod == 0:
            n6=1
        else:
            n6=6


    def clipboard(self):
        if windll.user32.OpenClipboard(None):
            windll.user32.EmptyClipboard()
            windll.user32.CloseClipboard()

    def opera(self):
        try:
            shutil.rmtree('C:/Users/Anurag/AppData/Roaming/Opera Software/Opera Stable')
        except:
            print("ok1")


    def runhistory(self):

        def deleteSubkey(key0, key1, key2=""):

            if key2 == "":
                currentkey = key1
            else:
                currentkey = key1 + "\\" + key2
            open_key=5
            try:
                open_key = wreg.OpenKey(key0, currentkey, 0, wreg.KEY_ALL_ACCESS)

                infokey = wreg.QueryInfoKey(open_key)
                for x in range(0, infokey[0]):
                    # NOTE:: This code is to delete the key and all subkeys.
                    #  If you just want to walk through them, then
                    #  you should pass x to EnumKey. subkey = _winreg.EnumKey(open_key, x)
                    #  Deleting the subkey will change the SubKey count used by EnumKey.
                    #  We must always pass 0 to EnumKey so we
                    #  always get back the new first SubKey.
                    subkey = wreg.EnumKey(open_key, 0)
                    try:
                        wreg.DeleteKey(open_key, subkey)
                        print("Removed %s\\%s " % (currentkey, subkey))
                    except:
                        deleteSubkey(key0, currentkey, subkey)
                        # no extra delete here since each call
                        # to deleteSubkey will try to delete itself when its empty.

                wreg.DeleteKey(open_key, "")
                open_key.Close()
                print("Removed %s" % (currentkey))
                return
            except:
                print('historyexcep')
                return

        # Here is an how you run it:
        # HKEY_CURRENT_USER\
        # deleteSubkey(wreg.HKEY_CURRENT_USER, "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU", "App")
        deleteSubkey(wreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU")


    def jumplist(self):
        try:
            shutil.rmtree('C:/Users/Anurag/AppData/Roaming/Microsoft/Windows/Recent/AutomaticDestinations')
        except:
            print("ok2")

