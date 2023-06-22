from abc import ABC, abstractmethod
import tool.decorator as decorator


class AbstractUser(ABC):
    """
    Abstract class for user , including username and password
    """

    def __init__(self, username: str, password: str) -> None:
        self.username: str = username
        self.password: str = password

    @decorator.RunTimeMonitor("AbstractUser: get_username")
    def get_username(self) -> str:
        return self.username

    @decorator.RunTimeMonitor("AbstractUser: get_password")
    def get_password(self) -> str:
        return self.password

    def __str__(self) -> str:
        return f"username: {self.username}, password: {self.password}"


class Student(AbstractUser):
    """
    Student class, used to log in  SIWeb
    """

    def __init__(self, username: str, password: str) -> None:
        super().__init__(username, password)
