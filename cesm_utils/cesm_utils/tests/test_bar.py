#!/usr/bin/env python

import unittest

from cesm_utils.bar_util import bar_ify, bar_sqrt

class TestBar(unittest.TestCase):
    """unit tests for the cesm_utils bar functionality
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_bar_ify(self):
        msg = 'abc'
        result = bar_ify(msg)
        self.assertTrue(msg in result)
        self.assertTrue("BAR" in result)

    def test_bar_sqrt_4(self):
        result = bar_sqrt(4.0)
        self.assertEqual(result, 2.0)

    def test_bar_sqrt_9(self):
        result = bar_sqrt(9.0)
        self.assertEqual(result, 3.0)


if __name__ == '__main__':
    unittest.main()
