import numpy as np
from math import cos, sin, pi
from numpy.linalg import lstsq
import matplotlib.pyplot as plt
from typing import List
from Question1.DataParser import DataPoint

"""
Plotting functions & Data Preparation
"""


def CoefficientArray(k: int):
    return [1, cos(k * 2 * pi / 365.25), sin(k * 2 * pi / 365.25)]


def prepare_data_for_fit(data: List[DataPoint]):
    A = []
    b = []
    for i in range(len(data)):
        year, previous_date_year = [data[i].year, data[i - 1].year]

        if year == previous_date_year:
            data[i].day = data[i - 1].day + 1

        b.append([data[i].temperature])
        A.append(CoefficientArray(data[i].day))

    return A, b


def prepare_data_for_plot(data: List[DataPoint]):
    days = []
    temps = []
    for i in range(len(data)):
        year, previous_date_year = [data[i].year, data[i - 1].year]

        if year == previous_date_year:
            data[i].day = data[i - 1].day + 1

        days.append(data[i].day)
        temps.append(data[i].temperature)

    return days, temps


def plot_original_data(data: List[DataPoint]):
    days, temps = prepare_data_for_plot(data)
    plt.plot(days, temps, "b.", label="original data")


def plot_fit(data: List[DataPoint], least_squares_coefficient: List):
    days_fit = np.linspace(1, 365, num=365)
    temp_predict = []
    for day in days_fit:
        prediction = least_squares_coefficient[0][0] + \
                     (least_squares_coefficient[1][0] * cos(day * 2 * pi / 365.25)) + \
                     (least_squares_coefficient[2][0] * sin(day * 2 * pi / 365.25))

        temp_predict.append(prediction)\
    
    plot_original_data(data)
    plt.plot(days_fit, temp_predict, "r--", label="prediction")
    plt.legend(loc="best")
    plt.show()

    return np.argmin(temp_predict), np.argmax(temp_predict)


class LeastSquares:
    """
    Calculates the Least Squared Solutions for
    """

    def __init__(self, data: List[DataPoint]):
        self.A, self.b = prepare_data_for_fit(data)

    def fit(self):
        A_matrix = np.array(self.A)
        b_vector = np.array(self.b)

        return lstsq(a=A_matrix, b=b_vector, rcond=-1)[0]
