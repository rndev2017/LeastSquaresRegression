from LeastSquares import LeastSquares
from DataParser import DataParser
import sys


def main(file_path):
    parser = DataParser(file_path=file_path)
    detroit_weather_data = parser.parse_data()

    ls = LeastSquares(data=detroit_weather_data)


if __name__ == "__main__":
    main(sys.argv[1])
