import unittest
import parseData.Selector as Selector


class TableSelectorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.data: str = """<!DOCTYPE html>
<html>
<head>
    <title>Test</title>
</head>
<body>
<table border="0" cellpadding="3" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%">
</table>
<table width="98%" border="0" align="center" cellpadding="0" cellspacing="0">
</table>
<table width="100%" border="0" align="center" cellpadding="1" cellspacing="0">
</table>
<table width="100%" border="1" align="center" cellpadding="1" cellspacing="0" bordercolor="#EAEAEA">
</table>
</body>
</html>"""
        self.expression: str = "body > strong:nth-child(2) > table:nth-child(3)"

    def tearDown(self) -> None:
        self.data = None
        self.expression = None

    def test_TableSelector(self) -> None:
        selector: Selector.AbstractSelector = Selector.TableSelector(self.data, self.expression)
        expected: str = """<table width="100%" border="1" align="center" cellpadding="1" cellspacing="0" bordercolor="#EAEAEA">
</table>"""
        result: str = selector.get_data()
        self.assertEqual(expected, result)
