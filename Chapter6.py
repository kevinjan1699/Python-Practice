'''
Created on 2019年7月23日

@author: 8406040
'''
from test.leakers import test_selftype

if __name__ == '__main__':
    pass
'''
class thing:
    def __init__(self):
        pass

print(thing)
example=thing()
print(example)
'''
'''
class Thing2:
    def __init__(self,input_name):
        self.letters=input_name
    word='123'
print(Thing2.word)
AA=Thing2('abc')
print(AA.letters)
print(AA.word)
'''
'''
class Element:
    def __init__(self,name,symbol,number):
        self.name=name
        self.symbol=symbol
        self.number=number
    def dump(self):
        print(self.name)
        print(self.symbol)
        print(self.number)
    def __str__(self):
        return('name=%s symbol=%s number=%s' % (self.name,self.symbol,self.number))

EE=Element('Hydrogen','H',1)
#print(EE.name)
dic={'name':'Hydrogen', 'symbol':'H', 'number':1}
hydrogen=Element(**dic)
#print(hydrogen.name)
#hydrogen.dump()
print(hydrogen)
'''
'''
class Element:
    def __init__(self,name,symbol,number):
        self.name=name
        self.symbol=symbol
        self.number=number
    def dump(self):
        print(self.name)
        print(self.symbol)
        print(self.number)
    def __str__(self):
        return('name=%s symbol=%s number=%s' % (self.name,self.symbol,self.number))
    def get_name(self):
        print('in get_name')
        return self.name
    def set_name(self,name):
        print('in set_name')
        self.name=name
    name1=property(get_name,set_name)
    def get_symbol(self):
        print('in get_symbol')
        return self.symbol
    def set_symbol(self,symbol):
        print('in set symbol')
        self.symbol=symbol
    symbol1=property(get_symbol,set_symbol)
    def get_number(self):
        print('in get_number')
        return self.number
    def set_number(self,number):
        print('in set number')
        self.number=number
    number1=property(get_number,set_number)

EE=Element('Hydrogen','H',1)
#print(EE.name)
dic={'name':'Hydrogen', 'symbol':'H', 'number':1}
hydrogen=Element(**dic)
#print(hydrogen.name)
#hydrogen.dump()
#print(hydrogen)
bb=hydrogen.name1
cc=hydrogen.symbol1
dd=hydrogen.number1
hydrogen.name='123'
hydrogen.name1='456'
'''
'''
class Bear:
    def eats(self):
        return 'berries'
class Rabbit:
    def eats(self):
        return 'clover'
class Octothorpe:
    def eats(self):
        return 'campers'
bb=Bear()
print(bb.eats())
'''
class Laser:
    def does(self):
        return 'disintegrate'
class Claw:
    def does(self):
        return 'crush'
class SmartPhone:
    def does(self):
        return 'ring'
class Robot:
    a=Laser()
    b=Claw()
    c=SmartPhone()
    def does(self):
        print (self.a.does(),self.b.does(),self.c.does())
rr=Robot()
rr.does()
    
      
    