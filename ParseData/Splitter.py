from abc import ABC, abstractmethod
import Tool.Decorator as Decorator


class AbstractSpliter(ABC):
    """
    Abstract class for splitting the data
    """

    def __init__(self, data: object) -> None:
        self.original_data: object = data
        self.split_data: object = None

    @abstractmethod
    def split(self) -> list[any]:
        """
        split the original data
        :return: split data
        """
        pass

    @Decorator.RunTimeMonitor("AbstractSpliter: get_data")
    def get_data(self) -> list[any]:
        """
        Get the split data from the original data
        :return: split data
        """
        if self.split_data is None:
            self.split_data = self.split()
        return self.split_data


class PeriodSplitter(AbstractSpliter):
    """
    this class is used to split the data by period from the csv file
    """

    def __init__(self, csv_table: list[list[str]]):
        super().__init__(csv_table)
        self.header: list[str] = csv_table[0]
        self.original_data: list[list[str]] = csv_table[1:]

    @Decorator.RunTimeMonitor("PeriodSplitter: split")
    def split(self) -> list[list[str]]:
        """
        split the data by period from the csv file
        :return: split data
        """
        self.header = self.split_header(self.header)
        self.original_data = self.split_record(self.original_data)
        return [self.header] + self.original_data

    def split_header(self, header: list[str]) -> list[str]:
        """
        transform the period field to start time and end time field
        :param header: csv header
        :return: split header
        """
        temp_header: list[str] = []
        period_field: str = "Period"
        for value in header:
            if value == period_field:
                temp_header.append("Start time")
                temp_header.append("End time")
            else:
                temp_header.append(value)
        return temp_header

    def split_record(self, record: list[list[str]]):
        """
        split the record from the csv file
        :param record:
        :return:
        """
        temp_record: list[list[str]] = []
        for row in record:
            temp_record.append(self.split_row(row))
        return temp_record

    def split_row(self, row: list[str]) -> list[str]:
        """
        split the period field from the row
        :param row: csv row
        :return: split row
        """
        temp_row: list[str] = []
        period_index: int = 5
        for value in row:
            if row.index(value) == period_index:
                temp_row.extend(self.split_period(value))
            else:
                temp_row.append(value)
        return temp_row

    def split_period(self, period: str) -> list[str]:
        """
        split the period by year and season
        :param period: period
        :return: split period
        """
        return period.split("-")
