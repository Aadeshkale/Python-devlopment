from unittest import TestCase

from MyMath.mathematics import Maths


class TestMaths(TestCase):

    def setUp(self):
        print('setup called')
        self.m = Maths()

    def tearDown(self):
        del self.m
        print('tearDown called')

    def test_add(self):

        self.assertTrue(self.m.add(4,5) == 9)
        self.assertTrue(self.m.add(-2,5) == 3)
        print('test_add called')

    def test_sub(self):

        self.assertFalse(self.m.sub(4,5) == 1)
        self.assertTrue(self.m.sub(5,-2) == 7)
        print('test_sub called')

    def test_div(self):

        self.assertEqual(self.m.div(5, 3), 1)
        self.assertTrue(self.m.div(7, 4) == 1)
        print('test_div called')
