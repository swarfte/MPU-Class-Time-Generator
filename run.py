import RequestData.Requester as Requester
import RequestData.User as User
import ManipulateData.Writer as Writer
import ParseData.Selector as Selector
import ParseData.Filter as Filter
import ParseData.Converter as Converter
import ParseData.Splitter as Splitter
import sys


def run() -> None:
    username: str = sys.argv[1]
    password: str = sys.argv[2]
    user_account: User.AbstractUser = User.Student(username, password)

    requester: Requester.AbstractRequester = Requester.PlaywrightRequester(user_account)
    html_page: str = requester.get_timetable_html()

    selector: Selector.AbstractSelector = Selector.TableSelector(html_page)
    original_table: str = selector.get_data()

    nbsp_filter: Filter.AbstractFilter = Filter.NBSPFilter(original_table)
    filtered_table: str = nbsp_filter.get_data()

    html_writer: Writer.AbstractWriter = Writer.HTMLWriter(filtered_table)
    html_writer.save_as("original_timetable")

    converter: Converter.AbstractConverter = Converter.HTML2CSVConverter(filtered_table)
    header, records = converter.get_data()

    csv_file = [header] + records
    splitter: Splitter.AbstractSpliter = Splitter.PeriodSplitter(csv_file)
    split_csv_file: list[list[str]] = splitter.get_data()

    csv_writer: Writer.AbstractWriter = Writer.CSVWriter(split_csv_file)
    csv_writer.save_as("timetable")


if __name__ == '__main__':
    run()
