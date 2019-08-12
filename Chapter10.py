'''
Created on 2019年8月7日

@author: 8406040
'''

if __name__ == '__main__':
    pass
import os
'''
name='oops.txt'
print(os.path.exists(name))
print(os.path.exists('Chapter10.py'))
'''
'''
import subprocess
ret=subprocess.getoutput('date /t')
print(ret)

#ret=subprocess.check_output(['date','/t'])
ret=subprocess.getstatusoutput('date /t')
print(ret)
print(ret[0])
'''
'''
from datetime import date, time
with open('today.txt','wt') as fout:
    today=date.today()
    print(today, file=fout)
with open('today.txt','rt') as fin:
    today_str=fin.read()
    print(today_str)
#today2=date(today_str)
print('today %s/%s/%s' % (today.year, today.month, today.day))    
'''

'''
import os
print(os.listdir('..'))
'''

import multiprocessing
import datetime
import time
import random 
import os

def whoami(what):
    print("I'm %s, in process %s" % (what, os.getpid()))
    
def loopy(name1):

    whoami(name1)
    current=datetime.datetime.now()
#    print (current)
    print('start: current time %s at PID %s' % (current, os.getpid()))
    i=random.randint(1,30)
    time.sleep(i) #sleep i seconds
    current=datetime.datetime.now()
    print('end: current time %s at PID %s' % (current, os.getpid()))
   

if __name__ == "__main__":
    whoami("main")
    for n in range(4):
        p=multiprocessing.Process(target=loopy, args=('Loopy',)) #'Loopy 後移掉要有 , 號
        p.start()

'''
import datetime
my_birthday=datetime.date(1967,9,28)
print('Which weekday:',my_birthday.strftime('%A'))
thatday=my_birthday+datetime.timedelta(days=10000)
print(thatday)
'''

