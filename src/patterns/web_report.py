from patterns.csv_utils import Ride
# patrón de diseño Adaptador

class RideAdapter:
    def __init__(self, ride: Ride):
        self.ride = ride
    def get_taxi_id(self):
        return self.ride.taxi_id
    def get_pick_up_time(self):
        return self.ride.pick_up_time
    def get_drop_off_time(self):
        return self.ride.drop_of_time
    def get_passenger_count(self):
        return self.ride.passenger_count
    def get_trip_distance(self):
        return self.ride.trip_distance
    def get_tolls_amount(self):
        return self.ride.tolls_amount


def create_content(rides):
    builder = [_create_headers("Taxi Report"), _create_table_headers()]
    for ride in rides:
        ride_adapter = RideAdapter(ride)
        builder.append(_add_ride(ride_adapter))
    builder.append(_close_table_headers())

    return "".join(builder)


def create_file(content: str):
    with open("financial-report.html", "w") as file:
        file.write(content)


def _create_headers(title: str):
    return f"<h1>{title}</h1>"


def _create_table_headers():
    return """
    <table>
        <tr>
            <th> TaxiID </th>
            <th> Pickup time </th>
            <th> Dropoff time </th>
            <th> Passenger count </th>
            <th> Trip Distance </th>
            <th> Total amount </th>
        </tr>
    """


def _close_table_headers():
    return "</table>"


def _add_ride(ride_adapter):
    return "".join([
        "<tr>",
        f"<td>{ride_adapter.get_taxi_id()}</td>",
        f"<td>{ride_adapter.get_pick_up_time().isoformat()}</td>",
        f"<td>{ride_adapter.get_drop_off_time().isoformat()}</td>",
        f"<td>{ride_adapter.get_passenger_count()}</td>",
        f"<td>{ride_adapter.get_trip_distance()}</td>",
        f"<td>{_format_amount(ride_adapter.get_tolls_amount())}</td>",
        "</tr>"
    ])


def _format_amount(amount):
    if amount < 0:
        return f"<span style='color:red'>{amount}</span>"
    return str(amount)
