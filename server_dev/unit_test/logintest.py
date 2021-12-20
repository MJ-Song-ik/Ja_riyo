import unittest


import unittest

from unittest import TestCase

class MyTest(TestCase):
    def test_one_plus_two(self):
        self.assertEqual(1+2,3)