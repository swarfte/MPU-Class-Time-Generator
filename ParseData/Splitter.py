from abc import ABC, abstractmethod
import Tool.Decorator as Decorator
import datetime


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


class CertainDaySplitter(AbstractSpliter):
    """
    this class is used to split the class time to the specify day
    """

    def __init__(self, records: list[list[str]]):
        super().__init__(records)
        self.original_data: list[list[str]] = records[1:]
        self.title_row: list[str] = records[0]
        self.title_row = self.title_row[:5] + self.title_row[7:8] + ["day"]

    @Decorator.RunTimeMonitor("TimeAtDaySpliter: split")
    def split(self) -> list[list[str]]:
        split_data: list[list[str]] = [self.title_row]
        for record in self.original_data:
            split_data.extend(self.split_record(record))
        return split_data

    def split_record(self, record: list[str]) -> list[list[str]]:
        """
        split the record to the specify day
        :param record: contain start time and end time record
        :return: certain day record
        """
        split_records: list[list[str]] = []
        start_time: str = record[5]
        end_time: str = record[6]
        class_weekday: int = int(record[8])
        first_day: str = self.getFirstDay(start_time, class_weekday)
        class_duration: int = self.getDuration(first_day, end_time)
        current_day: datetime.datetime = datetime.datetime.strptime(first_day, "%Y/%m/%d")
        number_of_week: int = class_duration // 7 + 1

        for _ in range(number_of_week):
            split_records.append(self.getCertainDayRecord(record, current_day.strftime("%Y/%m/%d")))
            current_day += datetime.timedelta(days=7)
        return split_records

    def getCertainDayRecord(self, record: list[str], date: str) -> list[str]:
        """
        get the certain record for the week
        """
        certain_record: list[str] = record[:5] + record[7:8]  # reaming the original data
        certain_record.append(date)
        return certain_record

    def getDuration(self, start_time: str, end_time: str) -> int:
        """
        get the duration of the class
        """
        start = datetime.datetime.strptime(start_time, "%Y/%m/%d")
        end = datetime.datetime.strptime(end_time, "%Y/%m/%d")
        duration = (end - start).days
        return duration

    def getWeekday(self, date: str) -> int:
        """
        get the weekday of the date
        """
        dt = datetime.datetime.strptime(date, "%Y/%m/%d")
        weekday = dt.weekday()
        return (weekday + 1) % 7  # 0 is Sunday, 6 is Saturday

    def getFirstDay(self, date: str, class_weekday: int) -> str:
        """
        get the first day of the class
        """
        dt = datetime.datetime.strptime(date, "%Y/%m/%d")
        weekday = self.getWeekday(date)
        # if the weekday is before the class weekday, then add the days to the next class weekday
        if weekday < class_weekday:
            dt += datetime.timedelta(days=(class_weekday - weekday))
        # if the weekday is after the class weekday, then add the days to the next week
        elif weekday > class_weekday:
            dt += datetime.timedelta(days=7 - (weekday - class_weekday))

        return dt.strftime("%Y/%m/%d")
