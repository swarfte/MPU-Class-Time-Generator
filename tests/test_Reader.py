import unittest
import ManageData.Reader as Reader


class ReaderTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.file_name: str = "test"
        self.expected: str = """<!DOCTYPE html>
<html>
<head>
    <title>Test</title>
</head>
<body>
<h1>Test</h1>
<p>Test</p>
</body>
</html>"""

    def tearDown(self) -> None:
        self.file_name = None

    def test_HTMLReader(self) -> None:
        reader: Reader.AbstracterReader = Reader.HTMLReader(self.file_name)
        result: str = reader.get_data()
        self.assertEqual(self.expected, result)
