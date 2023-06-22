import unittest
import RequestData.User as User


class UserTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.username: str = "username"
        self.password: str = "password"

    def tearDown(self) -> None:
        self.username = None
        self.password = None

    def test_Student(self) -> None:
        student: User.Student = User.Student(self.username, self.password)
        self.assertEqual(self.username, student.get_username())
        self.assertEqual(self.password, student.get_password())
        self.assertEqual(f"username: {self.username}, password: {self.password}", str(student))
