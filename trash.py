shutil.rmtree(r'C:\Users\Anurag\AppData\Roaming\Mozilla\Firefox\Profiles\82539yoi.default')
        l2 = Label(frame5, text='howdy!!!!!!!FF  folder cleared ')
        l2.pack()
        os.remove(r'C:\Users\Anurag\AppData\Roaming\Mozilla\Firefox\Profiles\82539yoi.default')
       l2 = Label(frame5, text='howdy!!!!!!!FF  file cleared ')
        l2.pack()

l2 = Label(frame5, text='recycle bin cleared ')
l2.pack()

bprocess.Popen('del /S /Q /F %s\\*.*' % del_dir, shell=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        rTup = pObj.communicate()
        rCod = pObj.returncode
        try:bprocess.Popen('del /S /Q /F %s\\*.*' % del_dir, shell=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        rTup = pObj.communicate()
        rCod = pObj.returncode
        try:bprocess.Popen('del /S /Q /F %s\\*.*' % del_dir, shell=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        rTup = pObj.communicate()
        rCod = pObj.returncode
        try: