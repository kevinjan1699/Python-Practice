#-*- coding: utf-8 -*-
'''
Created on 2019年7月16日

@author: 8406040
'''

if __name__ == '__main__':
    pass

'''
import sys
for place in sys.path:
    print(place)
'''    

'''
import os
os.getcwd()      # Return the current working directory
os.chdir('/temp')   # Change current working directory
os.system('mkdir today')   # Run the command mkdir in the system shell
os.system('dir')
'''
'''
from collections import defaultdict
def no_idea():
    return 'Huh'
bestiary = defaultdict(no_idea)
bestiary['A']='Abominalble Snowman'
bestiary['B']='Basilisk'
bestiary['A']
bestiary['B']
bestiary['C']
print(bestiary)
'''
from collections import defaultdict as dd
dic=dd(int)
for nn,aa in enumerate(['a','b','c'],1):
    dic[aa]=nn
print(dic)    