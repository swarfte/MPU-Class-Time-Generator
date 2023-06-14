import unittest
import tests.test_Reader as test_Reader
import tests.test_Writer as test_Writer


def run():
    reader_suit: unittest.TestSuite = unittest.TestLoader().loadTestsFromModule(test_Reader)
    writer_suit: unittest.TestSuite = unittest.TestLoader().loadTestsFromModule(test_Writer)

    all_suit: list[unittest.TestSuite] = [
        reader_suit,
        writer_suit
    ]
    all_test: unittest.TestSuite = unittest.TestSuite(all_suit)
    unittest.TextTestRunner(verbosity=2).run(all_test)


if __name__ == '__main__':
    run()
