import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import pprint as pp

matplotlib.interactive("True")

df = pd.read_csv(r'/UCB_GPAs.csv')
data = pd.DataFrame(df)

years = data['Academic Year'].unique().tolist()
colleges = data['College/School'].unique().tolist()

def avg_college(year, college):
    headcount = sum(data.loc[(data['Academic Year'] == year) & (data['College/School'] == college), 'Headcount'])
    gpa_column = data.loc[(data['Academic Year'] == year) & (data['College/School'] == college), 'Average GPA']
    weight_column = data['Headcount'] / headcount
    weighted_gpas = gpa_column.mul(weight_column, fill_value=0)
    average_gpa = sum(weighted_gpas)
    return average_gpa

def make_full(year_list, college_list):
    dict_list = []
    for years in year_list:
        int_list = []
        for college in college_list:
            int_list.append(avg_college(years, college))
        dict_entry = dict(zip(college_list, int_list))
        dict_list.append(dict_entry)
    full_list = dict(zip(year_list, dict_list))
    return full_list

def make_plot(input_directory, desired_colleges):
    for college in desired_colleges:
        parsed_array = np.array([input_directory[i][college] for i in input_directory])
        plt.plot(parsed_array, label=college)
    plt.legend()
    plt.show()
    return

# gpa_directory = make_full(years, colleges)
# make_plot(gpa_directory, colleges)

majors_list = data.loc[(data['College/School'] == 'Clg of Engineering')]['Major'].unique().tolist()

def make_ae(major):
    want_array = data.loc[(data['Major'] == major), ['Academic Year', 'Average GPA']]
    array1 = np.array(want_array['Academic Year'])
    array2 = np.array(want_array['Average GPA'])
    return array1, array2

plt.ioff()

def plotter(majors_list=majors_list):
    fig, ax = plt.subplots()
    for i in majors_list:
        xdata, ydata = make_ae(i)
        ax.plot(xdata, ydata, label=i)
    plt.legend()
    plt.show()

plotter()
