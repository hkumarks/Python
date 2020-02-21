import time
from datetime import datetime as d

temp_path=r'C:\Users\Harsha Kumar\Desktop\Python_udemy\hosts'
file_path=r'C:\Windows\System32\drivers\etc\hosts'
weblist=['\n',"youtube.com","www.youtube.com",'www.google.com','google.com']
redirect='127.0.0.1'

while True:
    if d(d.now().year,d.now().month,d.now().day,14) < d.now() < d(d.now().year,d.now().month,d.now().day,23):
        print("Working hours")
        with open(file_path,'r+') as file:
            content=file.read()
            for i in weblist:
                if i in content:
                    continue
                else:
                    file.write(redirect+"   "+i+'\n')    
    else:
        with open(file_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in weblist):
                    file.write(line)
            file.truncate()    
        print("Free time")     
    time.sleep(5)
    