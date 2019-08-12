'''
Created on 2019年7月25日

@author: 8406040
'''

if __name__ == '__main__':
    pass
'''
mystery='\U0001f4a9'
print(mystery)
import unicodedata
def unitcode_test(value):
    name=unicodedata.name(value)
    value2=unicodedata.lookup(name)
    print('value={0} name={1} value2={2}'.format(value,name,value2))

unitcode_test(mystery)
ds=mystery.encode('utf-8')
print(ds)
print(len(ds))
sd=ds.decode('utf-8')
print(sd)
print(len(sd))
'''

'''
print("My kitty cat like %s,\r\
My kitty cat like %s,\r\
My kitty cat fell on his %s,\r\
And now thins he's a %s" % ('roast beef', 'ham', 'head', 'clam'))
'''


letter='''
Dear {salutation} {name},

Thank you for your letter. We are sorry that our {product} {verbed} in your \{fdffsdf\}

Sincerely,
{spokesman}
{job_title}
'''
response={'salutation':'Miss. ','name':'Lily','product':'Server', 'verbed':'0001','spokesman':'Kevin','job_title':'Sr. Director'}
#print(letter.format(**response))

mammoth='''
We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.

All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.

Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.

May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.

Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.

We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon.
'''

'''
import re
pat=r'\bc\w{3}'
print(re.findall(pat,mammoth))
'''

import sys
for place in sys.path:
    print(place)




