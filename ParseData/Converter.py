from abc import ABC, abstractmethod
import Tool.Decorator as Decorator
import bs4
import ParseData.Filter as Filter


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
    def get_data(self) -> str | list | dict | tuple:
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
        self.rows: bs4.ResultSet = self.get_rows()

    @Decorator.RunTimeMonitor("HTML2CSVConverter: convert")
    def convert(self) -> tuple[list[str], list[list[str]]]:
        """
        convert the html to csv
        :return: header and records
        """
        header: list = self.get_header()
        records: list = self.get_records()
        return header, records

    def get_rows(self) -> bs4.ResultSet:
        """
        get the rows from the html table
        :return: rows
        """
        table: bs4.Tag | bs4.NavigableString = self.soup.find("table")
        return table.find_all("tr")

    def get_header(self) -> list[str]:
        """
        get the header from the html table
        :return: header
        """
        header: list = []
        for cell in self.rows[0].find_all("td"):
            header.append(cell.get_text())
        filtered_header = self.filter_header(header)
        return filtered_header

    def get_records(self) -> list[list[str]]:
        """
        get the records from the html table
        :return: records
        """
        records: list = []
        for row in self.rows[1:]:
            record: list = []
            for cell in row.find_all("td"):
                record.append(cell.get_text())
            records.append(record)
        filtered_records = self.filter_records(
            records[:-1])  # remove the last row ( the last row only include the total number of the class)
        return filtered_records

    def filter_header(self, header: list[str]) -> list[str]:
        """
        replace the space and \n in the original header
        :param header: the header as a str
        :return: filtered header
        """
        header_filter: Filter.AbstractFilter = Filter.HeaderFilter(header)
        return header_filter.get_data()

    def filter_records(self, records: list[list[str]]) -> list[list[str]]:
        """
        replace the space and \n in the original records
        :param records: the records as a str
        :return: filtered records
        """
        record_filter: Filter.AbstractFilter = Filter.RecordFilter(records)
        return record_filter.get_data()
