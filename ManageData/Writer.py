from abc import ABC, abstractmethod
from overrides import override
import tool.decorator as decorator
import os


class AbstractWriter(ABC):
    """
    Abstract class for writing data to the given path
    """

    def __init__(self, data: str | list | dict) -> None:
        self.data: str | list | dict = data
        self.root_path: str = "./temp/"
        self.check_root_path()

    @decorator.RunTimeMonitor("AbstractWriter: check_root_path")
    def check_root_path(self) -> None:
        """
        Check if the root path is existed, if not, create it
        :return: None
        """
        if not os.path.exists(self.root_path):
            os.makedirs(self.root_path)

    @abstractmethod
    def save_as(self, file_name: str) -> bool:
        """
        Save the data to the path
        :param file_name: the relative path to save the data
        :return: None
        """
        pass


class HTMLWriter(AbstractWriter):
    """
    this class is used to save the html to the path
    """

    def __init__(self, data) -> None:
        super().__init__(data)
        self.extension_name: str = ".html"

    @decorator.RunTimeMonitor("HTMLWriter: save_as")
    @override
    def save_as(self, file_name: str) -> bool:
        with open(self.root_path + file_name + self.extension_name, 'w') as f:
            f.write(self.data)
        return self.check_file_exist(file_name)

    @decorator.RunTimeMonitor("HTMLWriter: check_file_exist")
    def check_file_exist(self, file_name: str) -> bool:
        return os.path.exists(self.root_path + file_name + self.extension_name)
