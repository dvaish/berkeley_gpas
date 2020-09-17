import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'/UCB_GPAs.csv')

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

class GPA_major:

    def __init__(self, data_file, *args):
        self.data = data_file
        self.college = args
        self.majors = (self.data.loc[self.data['College/School'] == args]['Major'] if self.college else self.data['Major']).unique().tolist()

    def average_gpa(self, major):
        parse_target = self.data.loc[self.data['Major'] == major, ['College/School','Major', 'Average GPA', 'Headcount']]
        if self.college:
            parse_target = parse_target.loc[parse_target['College/School'] == self.college]
        average_gpa = sum(parse_target['Average GPA'].mul(parse_target['Headcount'], fill_value=0) / sum(parse_target['Headcount']))
        return average_gpa

    def dict_to_df(self):
        gpa_dictionary = dict(zip(self.majors, [self.average_gpa(i) for i in self.majors]))
        gpa_dataframe = pd.DataFrame(gpa_dictionary, index=['GPA']).swapaxes('index','columns').sort_values('GPA', ascending=False)
        return gpa_dataframe
    
    def top_gpas(self):
        head = int(input('How many majors?: '))
        frame_list = self.dict_to_df().head(head)
        return frame_list


    
        

