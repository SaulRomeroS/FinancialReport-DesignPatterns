from patterns.Observable import Observer
from patterns.csv_parser_observer import CsvParser


class CsvParserObserver(Observer):
    def __init__(self, csv_parser: CsvParser):
        self.csv_parser = csv_parser

    def update(self):
        rides = self.csv_parser.rides


__all__ = ["CsvParserObserver"]

