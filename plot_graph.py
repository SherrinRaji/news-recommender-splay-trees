from matplotlib import pyplot
import numpy as np
from constants import *
import timeit
from functools import partial
from time import time
import utility
from recommender import *
def plot_time(func, inputs, repeats, n_tests):
    newspaper_dict: dict = utility.load_splay(NEWS_PATH)
    lookup_dict: dict = utility.load_lookup(LOOKUP_PATH)
    x, y, y_err = [], [], []
    for input in inputs:
        print("for inout: {}".format(input))
        i = utility.load_test_data(input)
        timer = timeit.Timer(partial(func, newspaper_dict, lookup_dict,i))
        t = timer.repeat(repeat=repeats, number=n_tests)
        x.append(len(i))
        y.append(np.mean(t))
        y_err.append(np.std(t) / np.sqrt(len(t)))
    pyplot.errorbar(x, y, yerr=y_err, fmt='-o', label=func.__name__)


def plot_times(functions, inputs, repeats=3, n_tests=1, file_name_prefix=""):
    for func in functions:
        print("running: {}".format(func.__name__))
        plot_time(func, inputs, repeats, n_tests)
    pyplot.legend()
    pyplot.xlabel("Input")
    pyplot.ylabel("Time [s]")
    if not file_name_prefix:
        pyplot.show()
    else:
        pyplot.savefig(file_name_prefix + str(round(time() * 1000)))

if __name__ == "__main__":

    plot_times([splay_driver,treap_driver],FILE_LIST,repeats=1, n_tests=1, file_name_prefix="plot-")