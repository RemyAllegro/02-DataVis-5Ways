import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# simple helper function
def plot_manufacturer(ax, manufacturer):
    pass


data = pandas.read_csv("cars-sample.csv")
manufacturers = ["bmw", "ford", "honda", "mercedes", "toyota"]

axes = plt.gca()
