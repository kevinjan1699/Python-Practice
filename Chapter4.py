'''
Created on 2019年7月11日

@author: 8406040
'''
import _functools
from _ast import Try

if __name__ == '__main__':
    pass

'''
string=[3,2,1,0]
for i in string:
    print(i)

link=range(0,11,2)
print(link)
'''

'''
words='letters'
letter_counts={letter:words.count(letter) for letter in set(words)}
print(letter_counts)
'''
'''
squares={number:number*number for number in range(10)}
print(squares)
'''

'''
odd={number for number in range(10) if (number % 2)!=0}
print(odd)
'''

'''
got_number=['Got ' + str(number) for number in range(10)]
print(got_number)  
for thing in ('Got %s' % number for number in range(10)):
    print(thing)
'''

'''
def good():
    return ['Harry','Ron','Hermione']

print(good())
'''
'''
def get_odds():
    odds=[number for number in range(10) if (number % 2)==1]
    return odds

i=1
for number in get_odds():
    if i==3:
        print(number)
    i+=1   
'''
'''
def get_odds():
    number=range(10)
    i=0
    while i<10:
        #if (number[i] % 2)==1:
        yield number[i]
        i+=1

odd_list=[]
for thing in get_odds():
    if (thing % 2)==1:
        odd_list.append(thing)
    #print(thing)
    #odd_list.append(thing)
print(odd_list[2])
'''
'''
def test(func):
    def new_function(*args,**kwargs):
        print('function start')
        result=func(*args,**kwargs)
        print('function end')
        return result
    return new_function

@test
def add_ints(a,b):
    print('function is running')
    return a+b

#cooler_add_ints=test(add_ints)
#cooler_add_ints(3,5)
add_ints(3,5)
'''
'''
class OopsException(Exception):
    print('Caught an oops')
    
try:
    raise OopsException()
except OopsException as exc:
    #print(exc)
    pass
'''
titles=['Create of Habit', 'Crewel Fate']
plots=['A nun turns into a monster','A haunted yarn shop']
print(dict(zip(titles,plots)))
    

