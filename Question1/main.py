from Question1.LeastSquares import LeastSquares, plot_fit
from Question1.DataParser import DataParser
import sys


def main(file_path):
    parser = DataParser(file_path=file_path)
    detroit_weather_data = parser.parse_data()

    ls = LeastSquares(data=detroit_weather_data)

    solutions = ls.fit()

    min_temp, max_temp = plot_fit(detroit_weather_data, solutions)

    print("The %dth day is the coldest day of the year" % min_temp)
    print("The %drh day is the warmest day of the year" % max_temp)


if __name__ == "__main__":
    main(sys.argv[1])
