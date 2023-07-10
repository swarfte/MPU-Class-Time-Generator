import unittest
import ManipulateData.Writer as Writer


class HTMLWriterTestCase(unittest.TestCase):
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


class CSVWriterTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.file_name: str = "timetable"
        self.header: list[str] = ['Sem', 'Class Code', 'Learning Module', 'Instructor', 'Venue', 'Period',
                                  'Time',
                                  'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
        self.records: list[list[str]] = [['2',
                                          'COMP221-221',
                                          'OBJECT ORIENTED TECHNOLOGIES',
                                          'WONG UN HONG',
                                          'N_54',
                                          '2023/01/05-2023/04/22',
                                          '10:00-11:30',
                                          '0',
                                          '0',
                                          '1',
                                          '0',
                                          '0',
                                          '0',
                                          '0'],
                                         ['null',
                                          'null',
                                          'null',
                                          'WONG UN HONG',
                                          'N_54',
                                          '2023/01/05-2023/04/22',
                                          '11:30-13:00',
                                          '0',
                                          '0',
                                          '0',
                                          '0',
                                          '1',
                                          '0',
                                          '0'],
                                         ['2',
                                          'COMP222-221',
                                          'INTERNET PROGRAMMING I',
                                          'CALANA CHAN MEI POU',
                                          'N_54',
                                          '2023/01/05-2023/04/22',
                                          '10:00-11:30',
                                          '0',
                                          '1',
                                          '0',
                                          '0',
                                          '0',
                                          '0',
                                          '0'],
                                         ['null',
                                          'null',
                                          'null',
                                          'CALANA CHAN MEI POU',
                                          'N_54',
                                          '2023/01/05-2023/04/22',
                                          '11:30-13:00',
                                          '0',
                                          '0',
                                          '0',
                                          '0',
                                          '0',
                                          '1',
                                          '0'],
                                         ['2',
                                          'COMP223-221',
                                          'SOFTWARE ENGINEERING',
                                          'AMANG KIM SONGKYOO',
                                          'N_56',
                                          '2023/01/05-2023/04/22',
                                          '11:30-13:00',
                                          '0',
                                          '1',
                                          '0',
                                          '0',
                                          '0',
                                          '0',
                                          '0'],
                                         ['null',
                                          'null',
                                          'null',
                                          'AMANG KIM SONGKYOO',
                                          'N_56',
                                          '2023/01/05-2023/04/22',
                                          '10:00-11:30',
                                          '0',
                                          '0',
                                          '0',
                                          '0',
                                          '0',
                                          '1',
                                          '0'],
                                         ['2',
                                          'COMP224-221',
                                          'DATABASE MANAGEMENT SYSTEMS',
                                          'YANG XU',
                                          'A214',
                                          '2023/01/05-2023/04/22',
                                          '11:30-13:00',
                                          '0',
                                          '0',
                                          '1',
                                          '0',
                                          '0',
                                          '0',
                                          '0'],
                                         ['null',
                                          'null',
                                          'null',
                                          'YANG XU',
                                          'A211',
                                          '2023/01/05-2023/04/22',
                                          '10:00-11:30',
                                          '0',
                                          '0',
                                          '0',
                                          '0',
                                          '1',
                                          '0',
                                          '0'],
                                         ['2',
                                          'COMP225-221',
                                          'NETWORK AND SYSTEM ADMINISTRATION',
                                          'LIAM LEI KIN',
                                          'N_54',
                                          '2023/01/05-2023/04/22',
                                          '14:30-17:30',
                                          '0',
                                          '1',
                                          '0',
                                          '0',
                                          '0',
                                          '0',
                                          '0'],
                                         ['2',
                                          'MENG221-221',
                                          'ENGLISH IV',
                                          'CHUI SAI CHAK',
                                          'N_52',
                                          '2023/01/05-2023/04/22',
                                          '14:30-17:30',
                                          '0',
                                          '0',
                                          '0',
                                          '0',
                                          '0',
                                          '1',
                                          '0'],
                                         ['null',
                                          'null',
                                          'null',
                                          'HO SIO WA',
                                          'B304',
                                          '2023/02/13-2023/03/18',
                                          '14:30-17:30',
                                          '0',
                                          '0',
                                          '1',
                                          '0',
                                          '0',
                                          '0',
                                          '0']]
        self.data: list[list[str], list[list[str]]] = [self.header, self.records]
        self.expected: bool = True

    def tearDown(self) -> None:
        self.file_name = None
        self.data = None
        self.expected = None

    def test_CSVWriter(self) -> None:
        writer: Writer.AbstractWriter = Writer.CSVWriter(self.data)
        result: bool = writer.save_as(self.file_name)
        self.assertEqual(self.expected, result)
