'''
Created on 2019年8月12日

@author: 8406040
'''

from PIL import Image
def show_img(imgfile):
    img=Image.open(imgfile)
    fmt=[img.format, img.size, img.mode]
    print(fmt)
    img.show()
    return fmt

if __name__ == '__main__':
    show_img('oreilly.png')



