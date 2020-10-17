import re
import sys
from typing import List


class DataPoint:
    def __init__(self, month: int, day: int, year: int, temperature: float):
        self.month = month
        self.day = day
        self.year = year
        self.temperature = temperature

    def __repr__(self):
        return "The temperature on %d/%d/%d was %f" % (self.month, self.day, self.year, self.temperature)


class DataParser:
    """Parses data from the txt format"""

    def __init__(self, file_path: str):
        self.file_path: str = file_path
        self.data: List[DataPoint] = []

    def parse_data(self) -> List[DataPoint]:
        regex_string = "(\d*\.?\d+)"
        # Prevents data from being re added again
        self.data.clear()
        try:
            with open(self.file_path, "r") as data:
                for datum in data.readlines():
                    weather_data = re.findall(regex_string, datum)
                    self.data.append(
                        DataPoint(
                            month=int(weather_data[0]),
                            day=int(weather_data[1]),
                            year=int(weather_data[2]),
                            temperature=float(weather_data[-1])
                        )
                    )
        except FileNotFoundError:
            print(f"File, {self.file_path}, could not be found!")
            sys.exit(1)
        finally:
            return self.data