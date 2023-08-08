from abc import ABC, abstractmethod
import Tool.Decorator as Decorator
import bs4
import ParseData.Filter as Filter
import csv


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
            records[:-1])  # remove the last row (the last row only include the total number of the class)
        return filtered_records

    def filter_header(self, header: list[str]) -> list[str]:
        """
        replace the space and \n in the original header
        :param header: the header as a str
        :return: filtered header
        """
        header_filter: Filter.AbstractFilter = Filter.HeaderFilter(header)  # it can be optimized
        return header_filter.get_data()

    def filter_records(self, records: list[list[str]]) -> list[list[str]]:
        """
        replace the space and \n in the original records
        :param records: the records as a str
        :return: filtered records
        """
        record_filter: Filter.AbstractFilter = Filter.RecordFilter(records)  # it can be optimized
        return record_filter.get_data()


class WeekToNumberConverter(AbstractConverter):
    """
    this class is used to convert the week to number
    """

    def __init__(self, data: list[list[str]]) -> None:
        super().__init__(data)
        self.title_data: list[str] = data[0][:8] + ["day"]
        self.original_data: list[list[str]] = data[1:]

    @Decorator.RunTimeMonitor("WeekToNumberConverter: convert")
    def convert(self) -> list[list[str]]:
        """
        convert the week to number
        :return: the list data that the week is converted to number
        """
        records: list[list[str]] = []
        for row in self.original_data:
            result:list[list[str]] = self.convertRow(row)
            records.extend(result)
        records.insert(0,self.title_data)
        return records

    def convertRow(self,row:list[str]) -> list[list[str]]:
        """
        example :
        Sem,Class Code,Learning Module,Instructor,Venue,Start time,End time,Time,Sun,Mon,Tue,Wed,Thu,Fri,Sat
        """
        check_column:list[int] = [
            8,9,10,11,12,13,14 # Sun,Mon,Tue,Wed,Thu,Fri,Sat
        ]
        day_offset: int = 8
        records:list[list[str]] = []
        for day in check_column:
            if row[day] == "1":
                records.append(row[:8]+[str(day - day_offset)])
        return records
