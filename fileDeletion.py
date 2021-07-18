import time
import os
import shutil

path = input("Input the file directory you want cleaned.")
listOfFiles = os.listdir(path)
time = time.time()
print(time)
isExist = os.path.exists(path)

for file in listOfFiles :
    name, ext = os.path.splitext(file)
    ext = ext[1:]
    if isExist == True :
        allFiles = os.walk(path)
        folders = os.path.join(path)
        ctime = os.stat(path).st_ctime
        print(ctime)
        if ctime + 37339 < time :
            if ext == "":
                shutil.rmtree(path+'/'+file)
            else :
                os.remove(path+'/'+file)