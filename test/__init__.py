import unittest
from .test_constructor import AllArgsConstructorTestCase

if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest([
        AllArgsConstructorTestCase()
    ])

    unittest.TextTestRunner().run(suite)
