from abc import ABC, abstractmethod
from overrides import override
import os


class AbstractWriter(ABC):
    """
    Abstract class for writing data to the given path
    """

    def __init__(self, data: str | list | dict) -> None:
        self.data: str | list | dict = data
        self.root_path: str = "./temp/"
        self.check_root_path()

    def check_root_path(self) -> None:
        """
        Check if the root path is existed, if not, create it
        :return: None
        """
        if not os.path.exists(self.root_path):
            os.makedirs(self.root_path)

    @abstractmethod
    def save_as(self, path: str) -> None:
        """
        Save the data to the path
        :param path: the relative path to save the data
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

    @override
    def save_as(self, file_name: str) -> None:
        with open(self.root_path + file_name + self.extension_name, 'w') as f:
            f.write(self.data)
