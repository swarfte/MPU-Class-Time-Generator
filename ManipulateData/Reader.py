from abc import ABC, abstractmethod
import Tool.Decorator as Decorator
import os
import csv


class AbstracterReader(ABC):
    """
    Abstract class for reading data from the given path
    """

    def __init__(self, relative_path: str) -> None:
        self.relative_path: str = relative_path
        self.root_path: str = "./temp/"
        self.check_root_path()
        self.data: object = None

    @Decorator.RunTimeMonitor("AbstracterReader: check_root_path")
    def check_root_path(self) -> None:
        """
        Check if the root path is existed, if not, throw an error
        :return: None
        """
        assert os.path.exists(self.root_path), "Root path is not existed"

    @abstractmethod
    def read(self) -> str | list | dict:
        """
        Read the data from the path
        :return: the data
        """
        pass

    @Decorator.RunTimeMonitor("AbstracterReader: get_data")
    def get_data(self) -> str | list | dict:
        if self.data is None:
            self.data = self.read()
        return self.data


class HTMLReader(AbstracterReader):
    """
    this class is used to read the html from the path
    """

    def __init__(self, file_name: str) -> None:
        self.extension_name: str = ".html"
        super().__init__(file_name)

    @Decorator.RunTimeMonitor("HTMLReader: read")
    def read(self) -> str | list | dict:
        with open(self.root_path + self.relative_path + self.extension_name, 'r') as f:
            return f.read()


class CSVReader(AbstracterReader):
    """
    this class is used to read the csv from the path
    """

    def __init__(self, file_name: str) -> None:
        self.extension_name: str = ".csv"
        super().__init__(file_name)

    @Decorator.RunTimeMonitor("CSVReader: read")
    def read(self) -> str | list | dict:
        with open(self.root_path + self.relative_path + self.extension_name, 'r') as f:
            reader = csv.reader(f)
            return [row for row in reader]
