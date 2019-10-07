import matplotlib.pyplot as plt


def plot(data):
    plt.hist(data, 'auto')
    plt.title("TPS Of A Specific Program")
    plt.show()