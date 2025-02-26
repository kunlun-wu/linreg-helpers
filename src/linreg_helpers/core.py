import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def plot_sloping_line(x, slope, intercept):
    """Plot a line from slope and intercept."""
    xline = np.linspace(min(x), max(x), 100)
    y = intercept + slope * xline
    plt.plot(xline, y, "--")


def plot_linreg(X, y, lr):
    print("plot_linreg: plotting data and linear regression line")
    xvec = X.T[0, :]
    slope = lr.coef_
    intercept = lr.intercept_
    plt.plot(xvec, y, "o")
    plot_sloping_line(X, slope, intercept)
    plt.title("plot from plot_linreg()")


def train_linreg(X, y):
    print("train_linreg: returning trained model lr")
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    lr = LinearRegression().fit(X_train, y_train)
    return lr