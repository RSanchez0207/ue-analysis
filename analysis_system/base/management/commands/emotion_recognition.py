from transformers import TFRobertaForSequenceClassification, pipeline
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from sqlalchemy import create_engine

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import json
import csv

class Command(BaseCommand):
    help = "A command to run Emotion Recognition"

    def handle(self, *args, **options):
        
        # Get date today
        today = date.today()

        # Get date yesterday
        yesterday = today - timedelta(days = 1)

        # Create Filename
        filename = "ER" + str(yesterday)

        count = 0

        model = TFRobertaForSequenceClassification.from_pretrained("arpanghoshal/EmoRoBERTa")

        emotion = pipeline('sentiment-analysis', 
                            model='arpanghoshal/EmoRoBERTa')

        # Get Spreadsheet from Google Form
        sheetID = '1i73xYnbaWpPsx6RjaUljmC3zIo8VP0muRzls8-lP8MY'
        df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheetID}/export?format=csv")
        df["comments"].fillna("None", inplace=True)
        comment_list = df["comments"].tolist()

        emotion_labels = emotion(comment_list)

        # Create Filename For Figures
        filename = "ER" + str(yesterday)
        filename_fig = "ERFIG" + str(yesterday)
        filename_top = "ERFIGTOP" + str(yesterday)
        static_dir_str_charts = "base/static/base/charts/"

        # Dump emotion recognition output to JSON file
        myjson = open("results/json/" + str(filename) + ".json", "w")
        json.dump(emotion_labels, myjson, indent=6)
        myjson.close()

        # Convert JSON File to CSV File
        with open("results/json/" + str(filename) + '.json') as json_file:
            jsondata = json.load(json_file)

        mycsv = open("results/csv/" + str(filename) + '.csv', 'w', newline='')
        csv_writer = csv.writer(mycsv)

        count = 0
        for data in jsondata:
            if count == 0:
                header = data.keys()
                csv_writer.writerow(header)
                count+=1
            csv_writer.writerow(data.values())
        mycsv.close()

        # Open ER CSV File
        df_ER = pd.read_csv("results/csv/" + str(filename) + ".csv")

        # Naming Chart and Size
        plt.figure(figsize=(15,5))

        # Plot Chart
        sns.countplot(x='label',data=df_ER, palette='bright')

        # Naming x and y
        plt.ylabel('Count', fontsize=12)
        plt.xlabel('Emotion', fontsize=12)

        # Save Figure
        plt.savefig(static_dir_str_charts + filename_fig + '.png')

        # TOP FIVE EMOTIONS
        n = 5
        x_top = df_ER['label'].value_counts()[:n]
        y_top = df_ER['label'].value_counts()[:n].index.tolist()

        plt.figure(figsize=(10,5))
        sns.barplot(x=x_top, y=y_top, palette='bright')
        plt.xlabel('Count')

        # Save Figure
        plt.savefig(static_dir_str_charts + filename_top + '.png')