import unittest
import ParseData.Selector as Selector


class SelectorTestCase(unittest.TestCase):
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
            <tbody>
                <tr>
                    <td>
                        <span>Sem</span>
                    </td>
                </tr>
            </tbody>
        </table>
    </body>
</html>"""

    def tearDown(self) -> None:
        self.data = None

    def check_table(self, data: str) -> bool:
        is_match: bool = True
        conditions: list = [
            "<table",
            "<tbody>",
            "<tr>",
            "<td>",
            "<span>",
            "</span>",
            "</td>",
            "</tr>",
            "</tbody>",
            "</table>",
            "bordercolor=\"#EAEAEA\"",
            "align=\"center\"",
            "border=\"1\"",
            "cellpadding=\"1\"",
            "cellspacing=\"0\"",
            "width=\"100%\""
        ]
        for condition in conditions:
            if condition not in data:
                is_match = False
                break
        return is_match

    def test_TableSelector(self) -> None:
        selector: Selector.AbstractSelector = Selector.TableSelector(self.data)
        result: str = selector.get_data()
        self.assertTrue(self.check_table(result))
