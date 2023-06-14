from abc import ABC, abstractmethod
from overrides import override
import bs4


class AbstractSelector(ABC):
    """
    Abstract class for selecting data from the given data
    """

    def __init__(self, data: str | list | dict) -> None:
        self.data: str | list | dict = data

    @abstractmethod
    def filter(self) -> str | list | dict:
        """
        Filter the original data
        :return: filtered data
        """
        pass


class TableSelector(AbstractSelector):
    """
    this class is used to select the table from the html
    """

    def __init__(self, data: str, expression: str) -> None:
        super().__init__(data)
        self.expression: str = expression

    @override
    def filter(self) -> bs4.ResultSet:
        """
        Filter the original data
        :return: filtered data
        """
        soup: bs4.BeautifulSoup = bs4.BeautifulSoup(self.data, features="html.parser")
        table: bs4.ResultSet = soup.find_all('table')
        return table
