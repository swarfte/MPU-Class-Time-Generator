from abc import ABC, abstractmethod
from overrides import override
import tool.decorator as decorator
import os


class AbstracterReader(ABC):
    """
    Abstract class for reading data from the given path
    """

    def __init__(self, relative_path: str) -> None:
        self.relative_path: str = relative_path
        self.root_path: str = "./temp/"
        self.check_root_path()
        self.data: object = None

    @decorator.RunTimeMonitor("AbstracterReader: check_root_path")
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

    @decorator.RunTimeMonitor("AbstracterReader: get_data")
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

    @decorator.RunTimeMonitor("HTMLReader: read")
    @override
    def read(self) -> str | list | dict:
        with open(self.root_path + self.relative_path + self.extension_name, 'r') as f:
            return f.read()
