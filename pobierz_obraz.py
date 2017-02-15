import urllib
import time
import os
import datetime

data=str(datetime.date.today())
h=time.strftime("%H")
m=time.strftime("%M")
godz=time.strftime("%H%M")
filename=""+data+"/oka_"+godz+".jpg"

print(godz)
print(data)
print(filename)

try:
    os.stat(data)
except:
    os.mkdir(data)
urllib.urlretrieve("http://www.ostroleka.pl/panorama/000M.jpg", filename)