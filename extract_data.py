import numpy
import plot_data as plotter
import confidence as conf

DEBUG = False;

def extract_data():
    data = numpy.genfromtxt("./hw2-prob1-data.txt", encoding = "utf-16");
    if DEBUG:
        print(data)
    return data

def run():
    data = extract_data()

    print("arithmetic mean")
    print(conf.confidence_arithmetic(data, 0.90))
    print("\n")
    #
    # print("harmonic mean")
    # print(conf.confidence_harmonic(data, 0.90))
    # print("\n")
    #
    # print("jackknife mean")
    # #Unit test
    # # print(conf.confidence_jackknife([402,386,407,403,398], 0.90))
    # print(conf.confidence_jackknife(data, 0.90))
    # print("\n")

    # print("bootstrap selections")
    # print(conf.confidence_bootstrap(data, 10))
    # print("\n")

    #Plot data
    # plotter.plot(data);






