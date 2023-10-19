from patterns.Observable import Observable
# patron de diseño de observador
import csv
from datetime import datetime
from dataclasses import dataclass


@dataclass
class Ride:
    error: str
    taxi_id: int
    pick_up_time: datetime
    drop_of_time: datetime
    passenger_count: int
    trip_distance: float
    tolls_amount: float


class CsvParser(Observable):
    def __init__(self):
        super().__init__()
        self.rides = []

    def parse_file(self, csv_file: str):
        with open(csv_file) as file:
            csv_reader = csv.DictReader(file, delimiter=",")
            for row in csv_reader:
                ride = Ride(
                    error="",
                    taxi_id=row['TaxiID'],
                    pick_up_time=datetime.strptime(row['lpep_pickup_datetime'], '%Y-%m-%d %H:%M:%S'),
                    drop_of_time=datetime.strptime(row['lpep_dropoff_datetime'], '%Y-%m-%d %H:%M:%S'),
                    passenger_count=int(row["passenger_count"]),
                    trip_distance=float(row["trip_distance"]),
                    tolls_amount=float(row["total_amount"])
                )
                self.rides.append(ride)

        self.notify_observers()



    def notify_observers(self):
        for observer in self.observers:
            observer.update()



def parse_file(csv_file: str):
    csv_parser = CsvParser()

    from patterns.report_observer import CsvParserObserver

    csv_parser.register_observer(CsvParserObserver(csv_parser))

    csv_parser.parse_file(csv_file)

    return csv_parser.rides


__all__ = ["CsvParser", "parse_file"]
