import unittest
import tests.test_Reader as test_Reader
import tests.test_Writer as test_Writer
import tests.test_Selector as test_Selector
import tests.test_Filter as test_Filter


def run():
    module_list: list = [
        test_Writer,
        test_Reader,
        test_Selector,
        test_Filter
    ]  # order is important

    all_suit: list[unittest.TestSuite] = [
        unittest.TestLoader().loadTestsFromModule(test_module) for test_module in module_list
    ]

    all_test: unittest.TestSuite = unittest.TestSuite(all_suit)
    unittest.TextTestRunner(verbosity=2).run(all_test)


if __name__ == '__main__':
    run()
