import unittest
import ParseData.Converter as Converter
import ManipulateData.Reader as Reader


class ConverterTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.reader: Reader.AbstracterReader = Reader.HTMLReader("timetable")
        self.html: str = self.reader.get_data()

    def tearDown(self) -> None:
        self.html = None

    def test_HTML2CSVConverter(self) -> None:
        converter: Converter.AbstractConverter = Converter.HTML2CSVConverter(self.html)
        # print(converter.get_data())
