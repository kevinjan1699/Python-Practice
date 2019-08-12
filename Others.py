'''
Created on 2019年8月12日

@author: 8406040
'''

if __name__ == '__main__':
    pass

from PIL import Image
img=Image.open('oreilly.png')
print(img.format, img.size, img.mode)
img.show()
