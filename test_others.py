'''
Created on 2019年8月12日

@author: 8406040
'''
import unittest
import others


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

        
    def test_fmt(self):
        format='PNG'
        result=others.show_img('oreilly.png')
        self.assertEqual(result[0], format)

    def test_size(self):
        size=(154,141)
        result=others.show_img('oreilly.png')
        self.assertEqual(result[1], size)

    def test_type(self):
        imgtype='RGB'
        result=others.show_img('oreilly.png')
        self.assertEqual(result[2], imgtype)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testsize']
    unittest.main()