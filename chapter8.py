'''
Created on 2019年8月1日

@author: 8406040
'''

if __name__ == '__main__':
    pass

import os
odir=os.getcwd()
print(odir)
#os.chdir('/temp')
'''
fout=open('test.txt','wt')
test1='This is a test of the emergency text system'
fout.write(test1)
fout.close()

fin=open('test.txt','rt')
test2=fin.read()
print(test2)
print(test1==test2)
#os.chdir(odir)
cdir=os.getcwd()
print(cdir)
'''
import csv
'''
testcsv=[
    ['author','book'],
    ['J R R Tolkien','The Hobbit'],
    ['Lynne Truss','Eats|, Shoots & Leaves']]
with open('testcsv.csv','wt',newline='') as fout:
    csvout=csv.writer(fout,delimiter='|')
    csvout.writerows(testcsv)

with open('testcsv.csv','rt',newline='') as fin:
    csvin=csv.DictReader(fin,fieldnames=['first','last'],delimiter='|')
    testcsv2=[row for row in csvin]
    print(testcsv2)
    print(type(testcsv2))
'''
import sqlite3

conn=sqlite3.connect('books.db')
conn.execute('DROP TABLE book')
curs=conn.cursor()
curs.execute('''CREATE TABLE book
(title VARCHAR(10) PRIMARY KEY,
author VARCHAR(100),
year INT)''')

ins='INSERT INTO book VALUES(?,?,?)'

with open('books.csv','rt') as fin:
    csvin=csv.DictReader(fin)
    for row in csvin:
        curs.execute(ins,(row['title'],row['author'],row['year']))
curs.execute('SELECT * from book ORDER BY title')
for abook in curs.fetchall():
    print(abook)
conn.commit()

print('Use SQLAlchemy package now')

import sqlalchemy as sa
conn=sa.create_engine('sqlite:///books.db')
rows=conn.execute('select title from book order by title')
for row in rows:
    print(*row,sep=', ')



