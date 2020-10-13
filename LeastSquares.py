import numpy as np
from typing import List
from DataParser import DataPoint


class LeastSquares:

    def __init__(self, data: List[DataPoint]):
        self.data = self.prepare_data(data)

    def fit(self):
        # does the curve fitting algorithm
        pass

    def prepare_data(self, data):
        processed_data = []
        for i in range(len(data)):
            year, previous_date_year = [data[i].year, data[i - 1].year]

            if year == previous_date_year:
                data[i].day = data[i - 1].day + 1

            processed_data.append([data[i].day, data[i].temperature])

        return processed_data

    def to_matrix(self):
        return np.array(self.data)


