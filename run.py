import RequestData.Requester as Req
import RequestData.User as User
import ManipulateData.Writer as Writer
import ParseData.Selector as Selector
import ParseData.Filter as Filter
import ParseData.Converter as Converter
import sys


def run() -> None:
    username: str = sys.argv[1]
    password: str = sys.argv[2]
    user_account: User.AbstractUser = User.Student(username, password)

    requester: Req.AbstractRequester = Req.PlaywrightRequester(user_account)
    html: str = requester.get_timetable_html()

    selector: Selector.AbstractSelector = Selector.TableSelector(html)
    original_table: str = selector.get_data()

    nbsp_filter: Filter.AbstractFilter = Filter.NBSPFilter(original_table)
    filtered_table: str = nbsp_filter.get_data()

    writer: Writer.AbstractWriter = Writer.HTMLWriter(filtered_table)
    writer.save_as("timetable")

    converter: Converter.AbstractConverter = Converter.HTML2CSVConverter(filtered_table)
    header, records = converter.get_data()


if __name__ == '__main__':
    run()
