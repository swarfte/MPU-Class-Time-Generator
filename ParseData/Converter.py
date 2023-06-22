from abc import ABC, abstractmethod
import Tool.Decorator as Decorator
import bs4


class AbstractConverter(ABC):
    """
    Abstract class for one data format to another data format
    """

    def __init__(self, data: object) -> None:
        self.original_data: object = data
        self.converted_data: object = None

    @abstractmethod
    def convert(self) -> str | list | dict:
        """
        convert the original data to another data format
        :return:
        """
        pass

    @Decorator.RunTimeMonitor("AbstractConverter: get_data")
    def get_data(self) -> str | list | dict:
        if self.converted_data is None:
            self.converted_data = self.convert()
        return self.converted_data


class HTML2CSVConverter(AbstractConverter):
    """
    this class is used to convert the html table to csv
    """

    def __init__(self, data: str) -> None:
        super().__init__(data)
        self.original_data: str = data
        self.soup: bs4.BeautifulSoup = bs4.BeautifulSoup(self.original_data, features="html.parser")
        self.rows: list[bs4.ResultSet] = self.get_rows()

    @Decorator.RunTimeMonitor("HTML2CSVConverter: convert")
    def convert(self) -> str | list | dict:
        """
        convert the html to csv
        :return: csv data
        """
        print(self.rows)

    def get_rows(self) -> list[bs4.ResultSet]:
        """
        get the rows from the html table
        :return: rows
        """
        table: bs4.Tag | bs4.NavigableString = self.soup.find("table")
        return table.find_all("tr")
