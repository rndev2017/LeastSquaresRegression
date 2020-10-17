import sys

from Question2.DataParser import DataParser

from Question2.LeastSquares import LeastSquares, plot_fit


def main(file_path):
    parser = DataParser(file_path=file_path)
    hundred_meter_data = parser.parse_data()
    
    for data in hundred_meter_data:
        print(data)

    ls = LeastSquares(data=hundred_meter_data)

    solutions = ls.fit()

    print(solutions)
    plot_fit(hundred_meter_data, solutions)


if __name__ == "__main__":
    main(sys.argv[1])
