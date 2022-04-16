from django.core.management.base import BaseCommand
from datetime import date, timedelta

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Command(BaseCommand):
    help = "Generate data from Likert Scale"

    def handle(self, *args, **options):
    
        # Open File
        sheetID = '1i73xYnbaWpPsx6RjaUljmC3zIo8VP0muRzls8-lP8MY'
        df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheetID}/export?format=csv")

        # Rename College Department Column
        df.rename(columns = {'collegeDepartments':'College Departments'}, inplace = True)

        # Replace all departments with its nicknames
        df['College Departments'].fillna("N/A", inplace=True)
        df['generalDepartments'].fillna("N/A", inplace=True)

        # College Departments
        df.loc[df['College Departments'] == 'College of Engineering (CENGG)', 'College Departments'] = 'CENGG'
        df.loc[df['College Departments'] == 'College of Dentistry (CDENT)', 'College Departments'] = 'CDENT'
        df.loc[df['College Departments'] == 'College of Business Administration (CBA)', 'College Departments'] = 'CBA'
        df.loc[df['College Departments'] == 'College of Computer Studies and Systems (CCSS)', 'College Departments'] = 'CCSS'
        df.loc[df['College Departments'] == 'College of Law', 'College Departments'] = 'LAW'
        df.loc[df['College Departments'] == 'College of Arts and Sciences (CAS)', 'College Departments'] = 'CAS'
        df.loc[df['College Departments'] == 'College of Education (CEDUC)', 'College Departments'] = 'CEDUC'

        # Null Values
        df.loc[df['College Departments'] == 'N/A', 'College Departments'] = 'General'
        df.loc[df['generalDepartments'] == 'N/A', 'generalDepartments'] = 'College'

        # Rename columns for easy understanding
        df.rename(columns = {'scoreOne':'Communication'}, inplace = True)
        df.rename(columns = {'scoreTwo':'Professionalism'}, inplace = True)
        df.rename(columns = {'scoreThree':'Connection With Students'}, inplace = True)
        df.rename(columns = {'scoreFour':'Availability and Accessibility'}, inplace = True)
        df.rename(columns = {'scoreFive':'Data Privacy Adherence'}, inplace = True)

        df.rename(columns = {'collegeDepartments':'College Departments'}, inplace = True)

        today = date.today()
        yesterday = today - timedelta(days = 1)
        filename = "LS" + str(yesterday)
        static_dir_str_charts = "base/static/base/charts/"

        # Plot comparison using Seaborn
        sns.catplot(x='College Departments', hue='Communication', data=df, kind='count', height=6, aspect=1.5)
        plt.savefig(static_dir_str_charts + filename + 'comm.png')

        sns.catplot(x='College Departments', hue='Professionalism', data=df, kind='count', height=6, aspect=1.5)
        plt.savefig(static_dir_str_charts + filename + 'prof.png')

        sns.catplot(x='College Departments', hue='Connection With Students', data=df, kind='count', height=6, aspect=1.5)
        plt.savefig(static_dir_str_charts + filename + 'conn.png')

        sns.catplot(x='College Departments', hue='Availability and Accessibility', data=df, kind='count', height=6, aspect=1.5)
        plt.savefig(static_dir_str_charts + filename + 'avail.png')

        sns.catplot(x='College Departments', hue='Data Privacy Adherence', data=df, kind='count', height=6, aspect=1.5)
        plt.savefig(static_dir_str_charts + filename + 'dpa.png')



