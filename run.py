import RequestData.Requester as Requester
import RequestData.User as User
import ManipulateData.Writer as Writer
import ParseData.Selector as Selector
import ParseData.Filter as Filter
import ParseData.Converter as Converter
import ParseData.Splitter as Splitter
import sys

from ManipulateData import Reader


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

    converter: Converter.AbstractConverter = Converter.HTML2CSVConverter(filtered_table)
    header, records = converter.get_data()

    csv_file = [header] + records
    splitter: Splitter.AbstractSpliter = Splitter.PeriodSplitter(csv_file)
    split_csv_file: list[list[str]] = splitter.get_data()

    null_record_filter: Filter.AbstractFilter = Filter.NullRecordFilter(split_csv_file)
    filtered_csv_file: list[list[str]] = null_record_filter.get_data()

    week_to_number_converter: Converter.AbstractConverter = Converter.WeekdayToNumberConverter(filtered_csv_file)
    converted_csv_file: list[list[str]] = week_to_number_converter.get_data()

    certain_day_splitter: Splitter.AbstractSpliter = Splitter.CertainDaySplitter(converted_csv_file)
    split_csv_file: list[list[str]] = certain_day_splitter.get_data()

    csv_writer: Writer.AbstractWriter = Writer.CSVWriter(split_csv_file)
    csv_writer.save_as("timetable")


def test():
    csv_reader: Reader.AbstractReader = Reader.CSVReader("timetable")
    split_csv_file: list[list[str]] = csv_reader.get_data()

    null_record_filter: Filter.AbstractFilter = Filter.NullRecordFilter(split_csv_file)
    filtered_csv_file: list[list[str]] = null_record_filter.get_data()

    week_to_number_converter: Converter.AbstractConverter = Converter.WeekdayToNumberConverter(filtered_csv_file)
    converted_csv_file: list[list[str]] = week_to_number_converter.get_data()

    csv_writer: Writer.AbstractWriter = Writer.CSVWriter(converted_csv_file)
    csv_writer.save_as("converted_timetable")


if __name__ == '__main__':
    run()
    # test()
