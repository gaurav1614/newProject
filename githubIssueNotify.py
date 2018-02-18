from urllib.request import urlopen
from bs4 import BeautifulSoup
import pynotify
import subprocess

soup= BeautifulSoup(urlopen("https://github.com/gaurav1614/ticTacToe/issues"),'html.parser').find_all("a", {"href": "/gaurav1614/ticTacToe/issues"})
k = int(soup[1].find_all('span')[1].text)
print(k)





'''if(k>0):
    pynotify.init("issueNotifier")
    x=pynotify.Notification("Important","New issue opened")
    x.set_urgency(pynotify.URGENCY_NORMAL)
    x.set_timeout(pynotify.EXPIRES_NEVER)
    x.show()


    #subprocess.Popen(['notify-send',"New issue opened in the provided repository."])  '''  
   

