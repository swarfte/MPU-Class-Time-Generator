from abc import ABC, abstractmethod


class AbstractDataType(ABC):
    """
    An abstract class that create a data type for easy manipulate data
    """

    def __init__(self, data: object):
        self.original_data: object = data
        self.initialization()

    @abstractmethod
    def get_data(self) -> object:
        """
        get the data that match the data type
        :return:
        """
        pass

    @abstractmethod
    def set_data(self, data: object) -> None:
        """
        set the data that match the data type
        :param data:
        :return:
        """
        pass

    @abstractmethod
    def initialization(self) -> None:
        """
        initialization used for convert the original data to specify format
        :return:
        """
        pass


class CSV(AbstractDataType):
    def __init__(self, header: list[str], context: list[list[str | int | float]]) -> None:
        self.header: list[str] = header
        self.output_data: str = ""
        super().__init__(context)

    def get_data(self) -> str:
        """
        get the csv data as the str type
        :return:
        """
        return self.output_data

    def set_data(self, context: list[list[str | int | float]]) -> None:
        """
        use the new context to replace the old context
        :param context:
        :return:
        """
        self.original_data = context

    def initialization(self) -> None:
        self.init_header()
        self.init_context()

    def init_header(self) -> None:
        self.output_data += self.get_row(self.header)

    def init_context(self) -> None:
        for record in self.original_data:
            self.output_data += self.get_row(record)

    def get_row(self, record: list[str | int | float]) -> str:
        """
        get a list as a record then return the row in csv as str type
        :param record:
        :return:
        """
        result: str = ""
        for data in record:
            result += data + ","
        result = result[:-1]
        result += "/n"
        return result
