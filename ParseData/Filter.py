from abc import ABC, abstractmethod
from overrides import override


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

    @override
    def filter(self) -> str | list | dict:
        """
        filter the nbsp from the html
        :return: data without nbsp
        """
        return self.original_data.replace(" ", " ")
