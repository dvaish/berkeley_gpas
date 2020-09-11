import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'/Users/dhruvvaish/Documents/data_files/UCB_GPAs.csv')

class GPA_college:

    def __init__(self, data_file):
        self.data = data_file
        self.years = np.array(self.data['Academic Year'].unique().tolist())
        self.colleges = np.array(self.data['College/School'].unique().tolist())

    def average_gpa(self, year, college):
        parse_target = self.data.loc[(self.data['Academic Year'] == year) & (self.data['College/School'] == college), ['Headcount', 'Average GPA']]
        average_gpa = sum(parse_target['Average GPA'].mul(parse_target['Headcount'], fill_value=0) / sum(parse_target['Headcount']))
        return average_gpa

    def plotter(self):
        fig, ax = plt.subplots()
        for college in self.colleges:
            plot_array = np.array([self.average_gpa(year, college) for year in self.years])
            ax.plot(self.years, plot_array, label=college)
        plt.legend()
        plt.show()





    
        

