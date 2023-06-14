import RequestData.Requester as Req
import RequestData.User as User
import ManageData.Writer as Saver
import sys


def run() -> None:
    username: str = sys.argv[1]
    password: str = sys.argv[2]
    user_account: User.AbstractUser = User.Student(username, password)
    requester: Req.AbstractRequester = Req.PlaywrightRequester(user_account, is_debug=False)
    html: str = requester.get_timetable_html()
    Saver.HTMLWriter(html).save_as("original_timetable")


if __name__ == '__main__':
    run()
