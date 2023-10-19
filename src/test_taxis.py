import pytest
import os

from patterns import csv_utils
from patterns import web_report


@pytest.mark.parametrize("file_name", ["taxi-data.csv"])
def test_load_file(file_name):
    rides = csv_utils.parse_file(file_name)

    assert rides is not None
    assert len(rides) > 0


def test_create_report():
    rides = csv_utils.parse_file("taxi-data.csv")
    html_report = web_report.create_content(rides)
    web_report.create_file(html_report)

    assert os.path.exists("financial-report.html")


if __name__ == "__main__":
    pytest.main()