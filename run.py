import RequestData.Requester as Req
import RequestData.User as User
import ManipulateData.Writer as Writer
import ParseData.Selector as Selector
import ParseData.Filter as Filter
import ParseData.Converter as Converter
import ManipulateData.Reader as Reader
import sys


def run() -> None:
    username: str = sys.argv[1]
    password: str = sys.argv[2]
    user_account: User.AbstractUser = User.Student(username, password)

    requester: Req.AbstractRequester = Req.PlaywrightRequester(user_account)
    html_page: str = requester.get_timetable_html()

    selector: Selector.AbstractSelector = Selector.TableSelector(html_page)
    original_table: str = selector.get_data()

    nbsp_filter: Filter.AbstractFilter = Filter.NBSPFilter(original_table)
    filtered_table: str = nbsp_filter.get_data()

    html_writer: Writer.AbstractWriter = Writer.HTMLWriter(filtered_table)
    html_writer.save_as("timetable")

    converter: Converter.AbstractConverter = Converter.HTML2CSVConverter(filtered_table)
    header, records = converter.get_data()

    csv_writer: Writer.AbstractWriter = Writer.CSVWriter([header, records])
    csv_writer.save_as("timetable")

    csv_reader: Reader.AbstracterReader = Reader.CSVReader("timetable.csv")
    csv_data: list[list[str]] = csv_reader.get_data()


if __name__ == '__main__':
    run()
