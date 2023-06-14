import unittest
import ManageData.Writer as Writer


class HTMLWriterTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.file_name: str = "test"

    def tearDown(self) -> None:
        self.file_name = None

    def test_HTMLWriter(self) -> None:
        data: str = """<!DOCTYPE html>
<html>
<head>
    <title>Test</title>
</head>
<body>
<h1>Test</h1>
<p>Test</p>
</body>
</html>"""
        writer: Writer.AbstractWriter = Writer.HTMLWriter(data)
        expected: bool = True
        result: bool = writer.save_as(self.file_name)
        self.assertEqual(expected, result)
