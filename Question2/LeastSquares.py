import numpy as np
from numpy.linalg import lstsq
import matplotlib.pyplot as plt
from typing import List
from Question2.DataParser import DataPoint

"""
Plotting functions & Data Preparation
"""


def CoefficientArray(t: float):
    return [0.5*(t**2), t, 1]


def prepare_data_for_fit(data: List[DataPoint]):
    A = []
    b = []
    for i in range(len(data)):
        b.append([data[i].distance])
        A.append(CoefficientArray(data[i].time))

    return A, b


def prepare_data_for_plot(data: List[DataPoint]):
    time = []
    distance = []
    for i in range(len(data)):
        time.append(data[i].time)
        distance.append(data[i].distance)

    return time, distance


def plot_original_data(data: List[DataPoint]):
    time, distance = prepare_data_for_plot(data)
    plt.plot(time, distance, "b.", label="original data")


def plot_fit(data: List[DataPoint], least_squares_coefficient: List):
    time = np.linspace(1, 13, num=20)
    distance_predict = []

    for t in time:
        prediction = 0.5*least_squares_coefficient[0][0]*(t**2) + least_squares_coefficient[1][0]*t + \
            least_squares_coefficient[2][0]
        distance_predict.append(prediction)
    
    plot_original_data(data)
    plt.plot(time, distance_predict, "r--", label="prediction")
    plt.legend(loc="best")
    plt.show()



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
