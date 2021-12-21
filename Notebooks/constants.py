import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sales = pd.read_csv("\\Datasets and Projects\\SALES\\Data\\Processed\\Sales Dataset(processed data).csv")

years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']

regions = ['Asia', 'Australia and Oceania', 'Central America \nand the Caribbean', 'Europe',
         'Middle East \nand North Africa', 'North America', 'Sub-Saharan Africa']

sort_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']

figsize = (17, 7)
fonsize_title = 20
fonsize_x = 12
fonsize_y = 12
fonsize_label = 15
layout = 1.05
title_color = '#006400'
labelpad = 6

def add_value_labels(group, y_value):
    for x, y in zip(group, y_value):
        label = round(y/1000000000, 2)
        plt.annotate(label, (x, y), textcoords="offset points", xytext=(0, 10), ha='center')


def arange_y_ticks(number):
    y = np.arange(0, number*100000000000+1, step=50000000000)
    y_ticks_list = []
    for i in y:
        i = i//1000000000
        tick = f'$ {i} B'
        y_ticks_list.append(tick)
    plt.yticks(y, y_ticks_list, fontsize=fonsize_y)
    return y, y_ticks_list

def arange_x_ticks(values):
   x = np.arange(len(values))
   plt.xticks(x, values, fontsize=fonsize_x)
   return x

def arange_subplots_labels(ax):
    for rect in ax.patches:
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2
        space = 5
        label = round(y_value/1000000000, 2)
        plt.annotate(label, (x_value, y_value), xytext=(0, space), textcoords="offset points", ha='center', va='bottom',
                     fontsize=12)