import RequestData.Requester as Req
import RequestData.User as User
import ManageData.Writer as Saver
import ParseData.Selector as Selector
import sys


def run() -> None:
    username: str = sys.argv[1]
    password: str = sys.argv[2]
    user_account: User.AbstractUser = User.Student(username, password)
    requester: Req.AbstractRequester = Req.PlaywrightRequester(user_account)
    html: str = requester.get_timetable_html()

    selector: Selector.AbstractSelector = Selector.TableSelector(html)
    table: str = selector.get_data()
    Saver.HTMLWriter(table).save_as("timetable")


if __name__ == '__main__':
    run()
