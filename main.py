import sys
import os
import shutil
import os.path
import time
import datetime
from PIL import Image
import subprocess

def createDir(dir, date):
    if date != '0':
        directorio = f'{dir}/{date}'
    else:
        directorio = dir
    try:
        os.mkdir(directorio)
    except OSError:
        directorio = ''

def checkDate(dir):
    date_created_obj = time.localtime(os.path.getctime(dir))
    return (f'{date_created_obj.tm_year}.{date_created_obj.tm_mon}.{date_created_obj.tm_mday}')

def thumb(imagen,dir):
    nom,ext = os.path.splitext(imagen)
    if ext == ".mp4" or ext == ".avi":
        image = nom+".png"
        subprocess.call(['ffmpeg', '-i', imagen, '-ss', '00:00:10.000', '-vframes', '1', image])
        image = Image.open(image)
        ext = '.png'
        os.remove(nom+".png")
    else:
        image = Image.open(imagen)
    MAX_SIZE = (100, 100)
    aa = nom.split("/")
    n = len(aa)
    nom = aa[n-1]
    image.thumbnail(MAX_SIZE)
    nueva = dir+"/thumbs"
    createDir(nueva,"0")
    image.save(nueva+"/"+nom+"_thumb"+ext)

def moveFiles(path,pp): 
    try:
        files_list = sorted(os.listdir(path))
        n = len(files_list)
        for a in range(n):
            file = files_list[a]
            nom,ext=os.path.splitext(file)
            if ext == '.png' or ext == '.mp4' or ext == '.avi' or ext == '.jpg':
                url = f'{path}/{file}'
                date = checkDate(url)
                createDir(pp , date)
                finalDir = f'{pp}/{date}'
                shutil.copyfile(os.path.join(path+"/",file),os.path.join(finalDir+"/",file))
                thumb(url,finalDir)
    except:
        print('Invalid dir')

  
if(len(sys.argv) == 3):
    moveFiles(sys.argv[1],sys.argv[2])
else:
    print('Error, not enough arguments')

   