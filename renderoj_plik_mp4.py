import os
import datetime

dzisiaj = str(datetime.date.today())
wczoraj = str(datetime.date.today()-datetime.timedelta(days=1))
print(dzisiaj)
print(wczoraj)

os.system("ffmpeg -framerate 30 -pattern_type glob -i '"+wczoraj+"/*.jpg' -c:v ibx264 "+wczoraj+"/"+wczoraj+".mp4")
#ffmpeg -framerate 30 -pattern_type glob -i '2016-11-10/*.jpg' -c:v libx264 2016-11-10/2016-11-10.mp4