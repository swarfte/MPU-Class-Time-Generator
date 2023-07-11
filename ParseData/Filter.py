from abc import ABC, abstractmethod
import Tool.Decorator as Decorator


class AbstractFilter(ABC):
    """
    Abstract class for selecting data from the given data
    """

    def __init__(self, data: object) -> None:
        self.original_data: object = data
        self.filtered_data: object = None

    @abstractmethod
    def filter(self) -> str | list | dict:
        """
        Filter the original data
        :return: filtered data
        """
        pass

    @Decorator.RunTimeMonitor("AbstractFilter: get_data")
    def get_data(self) -> str | list | dict:
        """
        Get the filtered data
        :return: filtered data
        """
        if self.filtered_data is None:
            self.filtered_data = self.filter()
        return self.filtered_data


class NBSPFilter(AbstractFilter):
    """
    this class is used to filter the nbsp from the html
    """

    def __init__(self, data: str) -> None:
        super().__init__(data)
        self.original_data: str = data

    @Decorator.RunTimeMonitor("NBSPFilter: filter")
    def filter(self) -> str | list | dict:
        """
        filter the nbsp from the html
        :return: data without nbsp
        """
        return self.original_data.replace(" ", " ")


class HeaderFilter(AbstractFilter):
    """
    this class is used to filter the header from the html table
    """

    def __init__(self, header: list[str]):
        super().__init__(header)
        self.original_data: list[str] = header

    @Decorator.RunTimeMonitor("HeaderFilter: filter")
    def filter(self) -> list[str]:
        """
        filter the space and \n in the header
        :return: the new header without space and \n
        """
        return [str.strip(column) for column in self.original_data]


class RecordFilter(AbstractFilter):
    """
    this class is used to filter the records from the html table
    """

    def __init__(self, records: list[list[str]]):
        super().__init__(records)
        self.original_data: list[list[str]] = records

    @Decorator.RunTimeMonitor("RecordFilter: filter")
    def filter(self) -> list[list[str]]:
        """
        filter the space and \n in the records
        :return: the new records without space and \n
        """
        filterer_data: list[list[str]] = []
        for record in self.original_data:
            temp_record: list[str] = record[:]
            if not self.detect_subject(record):
                temp_record = temp_record[1:]  # remove the empty column
                temp_record.insert(0, "null")  # insert an empty value for the sem column
                temp_record.insert(0, "null")  # insert an empty value for the class code column
                temp_record.insert(0, "null")  # insert an empty value for the learning module column
            filterer_data.append(self.filter_subject_record(temp_record))
        return filterer_data

    def detect_subject(self, record: list[str]) -> bool:
        """
        to check the row is the header of the subject (include sem, class code, learning module column) or not
        if not , it means the row is the same subject but different time
        """
        number_of_header_subject_column: int = 14
        number_of_follow_subject_column: int = 12

        if len(record) == number_of_header_subject_column:
            return True
        elif len(record) == number_of_follow_subject_column:
            return False
        else:
            raise ValueError("The number of column is not correct")

    def filter_subject_record(self, record: list[str]) -> list[str]:
        """
        filter the subject record
        """
        filterer_record: list[str] = []
        for column in record:
            if self.check_week(record, column):
                if self.check_attend(column):
                    filterer_record.append("1")
                else:
                    filterer_record.append("0")
            else:
                filterer_record.append(str.strip(column))
        return filterer_record

    def check_week(self, record: list[str], column: str) -> bool:
        """
        to check the column is the week column or not
        :param record: the record of the subject
        :param column: the column of the record
        :return:
        """
        week_index: int = 7
        return record.index(column) >= week_index

    def check_attend(self, data: str) -> bool:
        """
        to check the data is go to school or not
        """
        attend_symbol: str = " \n\n"  # the original data is " \n\n" if the student need to go to school
        return data == attend_symbol
