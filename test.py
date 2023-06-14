import unittest
import tests.test_Reader as test_Reader


def run():
    reader_suit: unittest.TestSuite = unittest.TestLoader().loadTestsFromModule(test_Reader)
    unittest.TextTestRunner(verbosity=2).run(reader_suit)


if __name__ == '__main__':
    run()
