import numpy as np
import pylab as pl

def simple_plot(arff_data):

    data = arff_data["data"]
    x = []
    y = []
    for row in data:
        x.append(row[0])
        y.append(row[1])

    pl.plot(x, y)

    pl.show()