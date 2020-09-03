# -*- coding: utf-8 -*-

from .context import sample

import unittest
import numpy as np


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(sample.hmm())

    print(np.array)

if __name__ == '__main__':
    unittest.main()
