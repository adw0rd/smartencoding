# coding: utf-8
import os
import sys
import unittest
from nose.tools import eq_

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from smartencoding import smart_unicode


class TestSmartEncoding(unittest.TestCase):

    def test_smart_unicode(self):
        eq_(smart_unicode("Hello"), "Hello")
        eq_(smart_unicode("Привет"), u"Привет")

if __name__ == '__main__':
    unittest.main()

# To run the test suite
# pip install nose
# python tests.py -v
