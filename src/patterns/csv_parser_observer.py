from patterns.csv_utils import CsvParser


class CsvParserObserver:
    def __init__(self, csv_parser: CsvParser):
        self.csv_parser = csv_parser

    def update(self):
        rides = self.csv_parser.rides


__all__ = ["CsvParserObserver"]
