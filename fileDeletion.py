import time
import os
import shutil

path = input("Input the file directory you want cleaned.")
listOfFiles = os.listdir(path)
time = time.time()
print(time)
isExist = os.path.exists(path)

for file in listOfFiles :
    if isExist == True :
        allFiles = os.walk(path)
        folders = os.path.join(path)
        ctime = os.stat(path).st_ctime
        print(ctime)
        if ctime + 259.2 < time :
            os.remove(path+'/'+file)
            shutil.rmtree(path+'/'+file)