import sys
sys.path.append('../')
from project.myfun import add
import unittest2
class Test(unittest2.TestCase):
    def test_add(self):
        self.assertEqual(add(10,20),30)

if __name__=="__main__":
    unittest2.main()