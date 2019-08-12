'''
Created on 2019年8月2日

@author: 8406040
'''

if __name__ == '__main__':
    pass


'''
import urllib.request as ur
import requests
#url='http://www.iheartquotes.com/api/v1/random'
url='https://tw.yahoo.com/'
#url='https://google.com/'


conn=ur.urlopen(url)
print(conn)
print(conn.status)
data=conn.read()
#print(conn.gethearders('Content-Type'))
print(data)

resp=requests.get(url)
resp
print(resp.text)

print('Done')
'''

'''
from bottle import route, run
@route('/')
def home():
    return "It isn't fancy, but  it's my home page"
run(host='localhost',port=9999)
print('Done')
'''
'''
from bottle import route, run,static_file
@route('/')
def main():
    return static_file('home.html', root='.')
run(host='localhost',port=9999)

import os
odir=os.getcwd()
print(odir)
'''

from flask import Flask, render_template, request
app = Flask(__name__)
#from flask.ext.bootstrap import Bootstrap
#bootstrap=Bootstrap(app)
@app.route('/')
def home():
    kwargs={}
    kwargs['thing']=request.args.get('thing')
    kwargs['height']=request.args.get('height')
    kwargs['color']=request.args.get('color')
    return render_template('home.html',**kwargs)
#    thing=request.values.get('thing')
#    height=request.values.get('height')
#    color=request.values.get('color')
#    return render_template('home.html',
#                           thing=thing,height=height, color=color)

app.run(port=5000, debug=True)
#app.run(port=5000)

print('Done')