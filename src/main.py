from patterns import csv_utils
from patterns import web_report
from patterns import print_reporter

CSV_FILE = "taxi-data.csv"


def main():
    rides = csv_utils.parse_file(CSV_FILE)
    html_report = web_report.create_content(rides)
    web_report.create_file(html_report)
    print_reporter.print_report(rides)


if __name__ == '__main__':
    main()
