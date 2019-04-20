import time
import numpy as np
from scipy.optimize import curve_fit
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
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


def my_test(xdata_test, ydata_test, popt, intercepter, tol):
    good = 0
    m, n_feat = xdata_test.shape
    for i in range(m):
        pred = 0
        for j in range(n_feat-1):
            pred += popt[j]*xdata_test[i][j+1]
        pred += intercepter
        print("pred:", pred)
        print("ydata_test:", ydata_test[i])
        if pred > tol and ydata_test[i] > tol:
            good += 1
        elif pred < -tol and ydata_test[i] < -tol:
            good += 1
        elif (pred < tol and pred > -tol) and (ydata_test[i] < tol and ydata_test[i] > -tol):
            good += 1
        else:
            continue
    return (good/m)*100

def my_test2(y_pred, y_test, tol):
    good = 0
    length = len(y_pred)
    for i in range(length):
        if y_pred[i]>tol and y_test[i]>tol:
            good += 1
        elif y_pred[i]<-tol and y_test[i]<-tol:
            good += 1
        elif (y_pred[i]<tol and y_pred[i]>-tol) and (y_test[i]<tol and y_test[i]>-tol):
            good += 1
        else:
            continue
    return (good/length)*100


def linear_regression(filename, train_test_h, feat_degree):
    # Reading
    data = np.loadtxt(filename, delimiter=SEP, usecols=range(Y_COL))
    ydata = np.loadtxt(filename, usecols=Y_COL)

    # Feature preparation
    poly_feat = PolynomialFeatures(feat_degree)
    xdata = poly_feat.fit_transform(data)

    # Train and test set
    xdata_train = xdata[:train_test_h]
    xdata_test = xdata[train_test_h:]
    ydata_train = ydata[:train_test_h]
    ydata_test = ydata[train_test_h:]

    # Linear regression (actually polynomial regression)
    lin_reg = LinearRegression()
    # Fitting
    lin_reg.fit(xdata_train, ydata_train)
    # Predicting
    y_pred = lin_reg.predict(xdata_test)

    print("YPRED:")
    print(y_pred)

    # The coefficients
    print('Coefficients: \n', lin_reg.coef_)
    # The mean squared error
    print("Mean squared error: %.2f" % mean_squared_error(ydata_test, y_pred))
    # Explained variance score: 1 is perfect prediction
    print('Variance score: %.2f' % r2_score(ydata_test, y_pred))

    print("My test: ", my_test2(y_pred, ydata_test, 1))


def curve_fitting(filename, train_test_h, feat_degree):
    # Reading
    data = np.loadtxt(FILENAME, delimiter=SEP, usecols=range(Y_COL))
    ydata = np.loadtxt(FILENAME, usecols=Y_COL)

    # Feature preparation
    poly_feat = PolynomialFeatures(FEAT_DEGREE)
    xdata = poly_feat.fit_transform(data)

    # Train and test set
    xdata_train = xdata[:TRAIN_TEST_TH]
    xdata_test = xdata[TRAIN_TEST_TH:]
    ydata_train = ydata[:TRAIN_TEST_TH]
    ydata_test = ydata[TRAIN_TEST_TH:]
    #xdata_train = np.transpose(xdata_train) # <--- curve_fit 


    #popt, pcov = curve_fit(expression_func1, xdata_train, ydata_train)
    #print("Popt: ", popt)
    #perr = np.sqrt(np.diag(pcov))
    #print("perr: ", perr)

    #print(test(xdata_test, ydata_test, popt, 3))




FILENAME = "190K.csv"
SEP = ", "
TRAIN_TEST_TH = 160000
Y_COL = 11
FEAT_DEGREE = 2

if __name__ == "__main__":

    linear_regression(FILENAME, TRAIN_TEST_TH, FEAT_DEGREE)

