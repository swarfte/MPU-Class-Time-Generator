import unittest
import ManageData.Reader as Reader


class HTMLReaderTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.file_name: str = "test"

    def tearDown(self) -> None:
        self.file_name = None

    def test_HTMLReader(self) -> None:
        reader: Reader.AbstracterReader = Reader.HTMLReader(self.file_name)
        expected: str = """<!DOCTYPE html>
<html>
<head>
    <title>Test</title>
</head>
<body>
<h1>Test</h1>
<p>Test</p>
</body>
</html>"""
        result: str = reader.get_data()
        self.assertEqual(expected, result)
