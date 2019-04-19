import time
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd

def read_data_from_file(filename, sep):
    xdata = []
    ydata = []
    f = open(filename, "r")
    line = f.readline()
    while line:
        aux = [1]
        array = line.split(sep)
        for elem in array:
            aux.append(float(elem))
        xdata.append(aux[:-1])
        ydata.append(aux[-1])
        line = f.readline()
    f.close()
    return xdata, ydata



def expression_func1(X, th0, th1, th2, th3, th4, th5, th6, th7, th8, th9, th10, th11):
    res = X[0]*th0 + X[1]*th1 + X[2]*th2 + X[3]*th3 + X[4]*th4 + X[5]*th5 + X[6]*th6
    res += X[7]*th7 + X[8]*th8 + X[9]*th9 + X[10]*th10 + X[11]*th11
    return res


def test(xdata_test, ydata_test, popt, tol):
    good = 0
    length = len(xdata_test)
    for i in range(length):
        if abs(expression_func1(xdata_test[i], *popt) - ydata[i]) < tol:
            good += 1
    return (good/length)*100


FILENAME = "35K.csv"
SEP = ", "
TRAIN_TEST_TH = 30000
if __name__ == "__main__":
    # Reading
    data = np.loadtxt(FILENAME, delimiter=SEP, usecols=range(11))
    ydata = np.loadtxt(FILENAME, usecols=11)

    # Adding one column of 1's at the beginning
    ones_col = np.ones((data.shape[0], 1))
    xdata = np.append(ones_col, data, 1)
    xdata_train = xdata[:TRAIN_TEST_TH]
    xdata_test = xdata[TRAIN_TEST_TH:]
    ydata_train = ydata[:TRAIN_TEST_TH]
    ydata_test = ydata[TRAIN_TEST_TH:]
    xdata_train = np.transpose(xdata_train)
    print("xdata shape: ", xdata_train.shape)
    print("ydata shape: ", ydata_train.shape)

    popt, pcov = curve_fit(expression_func1, xdata_train, ydata_train)
    print("Popt: ", popt)
    perr = np.sqrt(np.diag(pcov))
    print("perr: ", perr)

    print(test(xdata_test, ydata_test, popt, 3))
