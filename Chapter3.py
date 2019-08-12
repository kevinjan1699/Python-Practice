#-*- coding: utf-8 -*-
'''
Created on 2019�~7��10��

@author: 8406040
'''

if __name__ == '__main__':
    pass

'''
guess_me=7
start=1
while True:
    if start < guess_me:
        print('too low\n')
    elif start == guess_me:
        print('found it \n')
        break
    else:
        print('OOPs\n')
    start+=1
'''
'''
things=['mozzarella','cin derella','salmonella']
print(things)
for i in range(len(things)):
    things[i]=things[i].capitalize()    
    print(things[i].upper())
    print(things[i].reserves())
print(things)
'''
'''
e2f={'dog':'chien','cat':'chat','walrus':'morse'}
print(e2f)
print(e2f.get('walrus'))
ee=e2f.keys()
ff=e2f.values()
f2e={}
for e, f in zip(ee, ff):
    f2e[f]=e
print(f2e)
print(f2e['chien'])
print(e2f.keys())
'''

life ={'animal': {'cats':['Henri','Grumpy','Lucy'],
                  'octopi':[],
                  'emus':[]},                 
        'plant':{},
        'others':{}
        }
print(set(life.keys()))
print(set(life['animal'].keys()))
print(life['animal']['cats'])
