import re
import sys
from typing import List


class DataPoint:
    def __init__(self, time: float, distance: float):
        self.time = time
        self.distance = distance

    def __repr__(self):
        return "The runner ran %d meters at time %d seconds" % (self.distance, self.time)


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
                    position_data = re.findall(regex_string, datum)
                    self.data.append(
                        DataPoint(
                            time=float(position_data[0]),
                            distance=float(position_data[-1])
                        )
                    )
        except FileNotFoundError:
            print(f"File, {self.file_path}, could not be found!")
            sys.exit(1)
        finally:
            return self.data
