from abc import ABC, abstractmethod
import Tool.Decorator as Decorator
import bs4


class AbstractSelector(ABC):
    """
    Abstract class for selecting data from the given data
    """

    def __init__(self, data: object) -> None:
        self.original_data: object = data
        self.selected_data: object = None

    @abstractmethod
    def selects(self) -> str | list | dict:
        """
        selects the data from the original data according to the expression
        :return: filtered data
        """
        pass

    @Decorator.RunTimeMonitor("AbstractSelector: get_data")
    def get_data(self) -> str | list | dict:
        if self.selected_data is None:
            self.selected_data = self.selects()
        return self.selected_data


class TableSelector(AbstractSelector):
    """
    this class is used to select the table from the html
    """

    def __init__(self, data: str, expression: dict = None) -> None:
        """
        :param data: html data
        :param expression: default expression is {"bordercolor": "#EAEAEA"}
        """
        if expression is None:
            expression = {
                "bordercolor": "#EAEAEA"
            }
        self.expression: dict = expression
        super().__init__(data)

    @Decorator.RunTimeMonitor("TableSelector: selects")
    def selects(self) -> str | list | dict:
        """
        Filter the original data
        :return: filtered data
        """
        soup: bs4.BeautifulSoup = bs4.BeautifulSoup(self.original_data, features="html.parser")
        table: bs4.Tag | bs4.NavigableString = soup.find("table", attrs=self.expression)
        return str(table)


class CSVSortSelector(AbstractSelector):
    """
    this class is sort the csv file according to the given column name
    """

    def __init__(self, csv_data: list[list[str]], column_name: str):
        super().__init__(csv_data)
        self.title_row: list[str] = csv_data[0]
        self.original_data: list[list[str]] = csv_data[1:]
        self.column_name: str = column_name
        self.column_index: int = self.title_row.index(self.column_name)

    @Decorator.RunTimeMonitor("CSVSortSelector: selects")
    def selects(self) -> str | list | dict:
        """
        sort the csv file according to the given column index
        """
