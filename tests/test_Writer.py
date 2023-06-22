import unittest
import ManageData.Writer as Writer


class WriterTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.file_name: str = "test"
        self.data: str = """<!DOCTYPE html>
<html>
<head>
    <title>Test</title>
</head>
<body>
<h1>Test</h1>
<p>Test</p>
</body>
</html>"""
        self.expected: bool = True

    def tearDown(self) -> None:
        self.file_name = None
        self.data = None
        self.expected = None

    def test_HTMLWriter(self) -> None:
        writer: Writer.AbstractWriter = Writer.HTMLWriter(self.data)
        result: bool = writer.save_as(self.file_name)
        self.assertEqual(self.expected, result)
